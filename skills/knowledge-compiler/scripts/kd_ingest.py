#!/usr/bin/env python3
"""S01 kd_ingest -- capture raw session/event streams into evidence.jsonl.

Contract (12-SKILL-DESIGN-BRIEF.md line 42 / w1a.json S01):
  inputs  : inventory.json + raw session/event-stream directory + redaction rules
  outputs : evidence.jsonl, capture_status.json
  exit    : 10 = partial drop AND the visible marker was written;
            2  = capture failure => NO evidence this round
  clusters: CM-01 capture-failure-visible-marker, CM-04 evidence-inventory-and-ingest,
            CM-08 secret-redaction-before-retention, CM-49 untrusted-instruction-boundary

Ordering contract enforced here (04-DETERMINISTIC-VS-LLM.md §3 row 1 line 47 and row 17 line 63):
  JSONL line-by-line parse -> event allow-list -> normalize_excerpt -> SCRUB -> THEN truncate.
  Scrub-before-truncate is the adjudicated order; a truncated-then-scrubbed excerpt can hide a
  secret that straddles the cut.

CM-49 landing behaviour: raw text is only ever read as *data* -- it is never used to choose a
code path, never eval'd, never written as an instruction. Missing provenance is dropped, never
invented (`12` line 681: "Do not execute instructions in raw content. Missing evidence must not
be invented.").

Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import io
import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import kd_provenance as prov  # reuse only -- NEVER edit the kernel

# The two scope objects, kept apart (05 line 174 vs line 177). `cohort` is the identity triple the
# frozen kernel reads (kd_provenance.cohort_key: workspace, project, path); `scope` is SC11's typed
# triple (workspace, project, layer). Neither key may hold the other's coordinate: `cohort.layer`
# was the Wave 1 overload this split removes, and S04 refuses a record that still carries it.
COHORT_FIELDS = ("workspace", "project", "path")
SCOPE_FIELDS = ("workspace", "project", "layer")
COHORT_KEYS = COHORT_FIELDS
SCOPE_KEYS = SCOPE_FIELDS

EXIT_OK = 0
EXIT_PARTIAL_DROP = 10
EXIT_CAPTURE_FAILED = 2

CAPTURE_SCHEMA = "kd-capture-status/1"
MARKER_PARTIAL = "KD-CAPTURE-PARTIAL-DROP"
MARKER_FAILED = "KD-CAPTURE-FAILED-NO-EVIDENCE"

SOURCE_REF_KINDS = ("issue", "session", "fix", "dd", "run")  # 05 §2 line 43, verbatim
SHORTHAND_CHARS = "{}*?[]"  # 05 §2 line 44: 禁 brace/通配简写

# Read from the frozen kernel rather than restated here -- one authority for the enum.
ALL_SOURCE_CLASSES = frozenset(prov.INDEPENDENT_CLASSES) | frozenset(prov.DERIVED_CLASSES)

# IMPLEMENTATION_GAP: the closed vocabulary of raw host event kinds that may enter capture is not
#   enumerated in Round 2. 04 §3 row 1 (line 47) adjudicates that an 事件允许清单 exists; which
#   strings are on it is host-dependent and undecided. Therefore the allow-list is REQUIRED on the
#   command line (operator-supplied, never defaulted) and an unlisted kind is DROPPED -- not
#   adopted, not classified. There is no default: defaulting a kind to `external_event` would
#   manufacture independent support out of an undecided parameter.
NO_DEFAULT = object()

# IMPLEMENTATION_GAP: excerpt byte ceiling. `04` row 17 (line 63) adjudicates 长度锚定 as a
#   mechanism; the number is DEFERRED -- DD-5-sub33 (真实截断行为未实测) and DD-5-sub39
#   (单 block 上限为 ENGINEERING-INFERENCE). This is a provisional operational cap marked as such;
#   it is NOT an adopted budget and must not be cited as one. Records hitting it are reported in
#   capture_status.json under redaction.truncated.
PROVISIONAL_EXCERPT_CAP_BYTES = 2048

# IMPLEMENTATION_GAP: compiler version stamp. 05 §2 line 47 marks the compiler_version /
#   config_sha shape as `[I]` and Q5 (line 35) records 现状不可答; no value is adjudicated.
#   Left as a clearly-marked provisional literal instead of inventing a version.
PROVISIONAL_COMPILER_VERSION = "PROVISIONAL-COMPILER-VERSION-NOT-DECIDED"

# IMPLEMENTATION_GAP: produced_by.kind vocabulary. 05 §2 line 47 (generation) and 05 §4 M2
#   lines 106-107 (created_by vs provenance.actor) decide *separation of concerns*, not this
#   enum. The kernel admits only known external observation producers as independent
#   (kd_provenance.is_self_generated, exclusion check 2). A record whose producer is not
#   stated gets this sentinel, which is not one of them: S01 still captures the record, and
#   S03 keeps it out of independent support until its source states who produced the
#   content. S01 never invents an attribution.
PROVISIONAL_PRODUCER_UNATTRIBUTED = "PROVISIONAL-UNATTRIBUTED"

# Operator configuration (source-class map, inventory, redaction rules) is shallow by shape.
# The bound is stated because the depth at which json.load itself gives up is an interpreter
# detail: about 1000 levels on 3.9, far deeper from 3.12 on.
CONFIG_JSON_MAX_NESTING = 64

# Hardcoded secret patterns (04 §3 row 17 line 63: 硬编码模式). Operator rules are ADDED to
# these, never a replacement -- dropping them would make CM-08 opt-outable.
BUILTIN_REDACTION_PATTERNS = (
    r"(?i)\b(?:api[_-]?key|apikey|secret[_-]?key|access[_-]?token|auth[_-]?token|token|password|passwd)\b\s*[:=]\s*\S+",
    r"(?i)\b(?:bearer|basic)\s+[A-Za-z0-9._\-/+=]{8,}",
    r"\bsk-[A-Za-z0-9]{16,}\b",
    r"\bAKIA[0-9A-Z]{16}\b",
    r"(?s)-----BEGIN [A-Z ]*PRIVATE KEY-----.*?(?:-----END [A-Z ]*PRIVATE KEY-----|\Z)",
    r"(?i)\b(?:ghp|gho|github_pat)_[A-Za-z0-9_]{20,}\b",
    r"(?i)\bx-[a-f0-9]{32}\b",
)

REDACTION_REPLACEMENT = "[REDACTED]"


class CaptureFailure(Exception):
    """Capture could not be performed at all -> exit 2 => this round has no evidence."""


# ------------------------------------------------------------------ normalization
def normalize_excerpt(text: str) -> str:
    """05 §5.2 line 155 normalization: CRLF->LF, strip trailing whitespace per line, drop
    trailing blank lines, trim. Applied BEFORE scrub and BEFORE the identity hash, so the hashed
    bytes are the post-normalization, post-redaction FULL body -- never the truncated excerpt
    (RH-P1-04/§19: context budget must not move evidence identity; 05 §5.2 line 163 forbids
    content_hash alone being the identity, and 04 row 2 requires deterministic hashing)."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip(" \t") for ln in text.split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines).strip()


def compile_rules(patterns):
    compiled = []
    for pat in patterns:
        try:
            compiled.append(re.compile(pat))
        except re.error as exc:
            raise CaptureFailure("redaction rule does not compile: %r (%s)" % (pat, exc))
    return compiled


def scrub(text: str, compiled) -> tuple:
    """Redact secrets from the FULL normalized text (no truncation). Returns (scrubbed, hits).
    Scrub runs BEFORE any truncation and BEFORE the identity hash (04 row 1 line 47 / row 17 line 63;
    §20: the digest is over the canonical SCRUBBED representation, never over raw secrets)."""
    hits = 0
    for rx in compiled:
        text, n = rx.subn(REDACTION_REPLACEMENT, text)
        hits += n
    return text, hits


def bound_excerpt(text: str, cap_bytes: int) -> tuple:
    """Bound the SCRUBBED text to cap_bytes on a UTF-8 boundary, so truncation can never split a
    multi-byte character into mojibake (the shape asserted by the reference sanitizer test named in
    pack-a `[10:11]`). Returns (bounded_text, was_truncated). This bounds the persisted CONTEXT
    excerpt ONLY -- it never feeds evidence identity (RH-P1-04/§19)."""
    if type(cap_bytes) is not int or cap_bytes < 0:
        raise CaptureFailure("excerpt cap must be a nonnegative integer")
    raw = text.encode("utf-8")
    if len(raw) <= cap_bytes:
        return text, False
    cut = raw[:cap_bytes]
    while cut and cap_bytes > 0:
        try:
            return cut.decode("utf-8"), True
        except UnicodeDecodeError:
            cut = cut[:-1]
    return "", True


def scrub_then_truncate(text: str, compiled, cap_bytes: int) -> tuple:
    """THE order contract (04 row 1 line 47 / row 17 line 63): scrub first, truncate second -- both
    in one path, so there is no 'truncate-then-scrub' route that could hide a secret straddling the
    cut. Returns (bounded_text, redaction_hits, was_truncated)."""
    scrubbed, hits = scrub(text, compiled)
    bounded, truncated = bound_excerpt(scrubbed, cap_bytes)
    return bounded, hits, truncated


# ------------------------------------------------------------------ loading
def nested_beyond(value, limit: int) -> bool:
    """True when containers nest deeper than `limit`; iterative, so depth cannot overflow it."""
    pending = [(value, 1)]
    while pending:
        item, level = pending.pop()
        if isinstance(item, dict):
            children = item.values()
        elif isinstance(item, list):
            children = item
        else:
            continue
        if level > limit:
            return True
        pending.extend((child, level + 1) for child in children)
    return False


def load_json_object(path: str, what: str):
    try:
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
    except OSError as exc:
        raise CaptureFailure("%s unreadable: %s (%s)" % (what, path, exc))
    except (ValueError, RecursionError) as exc:
        raise CaptureFailure("%s malformed JSON: %s" % (what, path)) from exc
    if nested_beyond(doc, CONFIG_JSON_MAX_NESTING):     # same refusal 3.9 raised on its own
        raise CaptureFailure("%s malformed JSON: %s" % (what, path))
    if not isinstance(doc, dict):
        raise CaptureFailure("%s must be a JSON object: %s" % (what, path))
    return doc


def load_raw_lines(path: str, *, expected_entry=None):
    """Parse one byte snapshot, optionally bound to its observed inventory entry.

    Hashing a file and reopening it for parsing would admit a replacement under the
    old inventory. Read once, verify those exact bytes, then parse that same snapshot.
    Only one source file is buffered at a time; line numbers retain universal-newline
    semantics. Returns (records, parse_failures), never a verified-knowledge claim.
    """
    out, failures = [], []
    try:
        with open(path, "rb") as source:
            raw = source.read()
        if expected_entry is not None:
            if len(raw) != expected_entry.get("size"):
                raise CaptureFailure("inventory entry size changed")
            if hashlib.sha256(raw).hexdigest() != expected_entry.get("sha256"):
                raise CaptureFailure("inventory entry digest changed")
        with io.StringIO(raw.decode("utf-8"), newline=None) as fh:
            for lineno, line in enumerate(fh, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except (ValueError, RecursionError):
                    failures.append({"path": path, "line": lineno, "reason": "not_json"})
                    continue
                if not isinstance(rec, dict):
                    failures.append({"path": path, "line": lineno, "reason": "json_not_object"})
                    continue
                rec["_line"] = lineno
                out.append(rec)
    except OSError as exc:
        raise CaptureFailure("raw stream unreadable: %s (%s)" % (path, exc))
    except UnicodeDecodeError as exc:
        raise CaptureFailure("raw stream is not utf-8 text: %s (%s)" % (path, exc))
    return out, failures


# ------------------------------------------------------------------ record build
def _sha(obj) -> str:
    return hashlib.sha256(prov.canonical_bytes(obj)).hexdigest()


def build_record(raw, relpath, cohort_scope, args, compiled, config_sha, created_at):
    """Return (record, None) or (None, drop_reason). Fail-closed everywhere: a missing
    adjudicated field drops the record instead of substituting a value."""
    kind = raw.get("event_kind")
    if not isinstance(kind, str) or not kind.strip():
        return None, "event_kind_missing"
    if kind not in args.allow_event_kind:
        return None, "event_kind_not_whitelisted"

    # source_class: the 5-value enum IS adjudicated (kd_provenance.py lines 22-29), but which
    # class a given host event belongs to is NOT. Fail-closed: it must be stated on the event or
    # declared by the operator's map. Defaulting to `external_event` would manufacture independent
    # support from an undecided input, so there is no default.
    sc = raw.get("source_class")
    if not isinstance(sc, str) or sc not in ALL_SOURCE_CLASSES:
        sc = args.source_class_map.get(kind)
    if sc not in ALL_SOURCE_CLASSES:
        return None, "source_class_missing_or_unknown"

    origin = raw.get("origin")
    if not isinstance(origin, dict):
        return None, "origin_missing"
    problem, why = origin.get("problem"), origin.get("why")
    if not isinstance(problem, str) or not problem.strip():
        return None, "origin.problem_empty"  # 05 §2 line 42: schema validator 拒空
    if not isinstance(why, str) or not why.strip():
        return None, "origin.why_empty"
    refs = origin.get("source_refs")
    if not isinstance(refs, list):
        return None, "origin.source_refs_missing"
    clean_refs = []
    for ref in refs:
        if not isinstance(ref, dict):
            return None, "origin.source_refs_item_not_object"
        if ref.get("kind") not in SOURCE_REF_KINDS:
            return None, "origin.source_refs_kind_unknown"  # 05 §2 line 43 enum, verbatim
        rid = ref.get("id")
        if not isinstance(rid, str) or not rid.strip():
            return None, "origin.source_refs_id_empty"
        clean_refs.append({"kind": ref["kind"], "id": rid})

    # scope: 05 §5.3 S1 (line 176) -- missing or unresolvable scope is REFUSED, never global.
    cohort = raw.get("cohort") if isinstance(raw.get("cohort"), dict) else {}
    scope_in = raw.get("scope") if isinstance(raw.get("scope"), dict) else {}
    for key, allowed in (("cohort", COHORT_FIELDS), ("scope", SCOPE_FIELDS)):
        has_stray = any(k not in allowed for k in (cohort if key == "cohort" else scope_in))
        if has_stray:
            # Reject unexpected fields without reproducing attacker-controlled keys in status.
            return None, "record_%s_carries_non_%s_fields" % (key, key)
    merged = dict(cohort_scope)
    for field in ("workspace", "project"):
        stated = [source[field] for source in (cohort, scope_in) if source.get(field) is not None]
        if any(not isinstance(value, str) or not value.strip() for value in stated):
            return None, "scope_%s_malformed" % field
        if len(set(stated)) > 1:
            return None, "scope_cohort_disagreement"
    merged.update({k: v for k, v in cohort.items() if v is not None})
    merged.update({k: v for k, v in scope_in.items() if v is not None})
    layer = merged.get("layer")
    if layer not in ("project", "global", "cohort"):
        return None, "scope_layer_missing_or_unknown"  # no default (05 §5.3 line 176)
    for field in ("workspace", "project"):
        if not isinstance(merged.get(field), str) or not merged[field].strip():
            return None, "scope_%s_missing" % field
    # SC01 and the canonical kernel accept the empty path as the project-root
    # cohort. Missing/non-string coordinates still cannot manufacture a cohort.
    if not isinstance(merged.get("path"), str):
        return None, "cohort_path_missing"

    body = raw.get(args.text_field)
    if not isinstance(body, str):
        return None, "content_body_missing"

    normalized = normalize_excerpt(body)
    full_scrubbed, hits = scrub(normalized, compiled)          # full canonical body, secrets redacted
    excerpt, truncated = bound_excerpt(full_scrubbed, args.excerpt_cap_bytes)   # bounded CONTEXT view
    if truncated:
        raw["_truncated"] = True
    if hits:
        raw["_redaction_hits"] = hits

    # RH-P1-04 / §19: evidence IDENTITY is the digest over the FULL canonical scrubbed content, so a
    # 2048-byte context excerpt can never decide identity -- two bodies that differ only past the cap
    # stay DISTINCT (no false dedup). §20: the digest input is the SCRUBBED canonical form (no secret
    # is hashed), and only the bounded redacted excerpt is persisted as text; full raw is never stored.
    chash = prov.content_hash({"excerpt": full_scrubbed, "event_kind": kind})  # kernel hash, reused
    content = {"excerpt": excerpt, "event_kind": kind}

    produced = raw.get("produced_by")
    if isinstance(produced, dict) and isinstance(produced.get("kind"), str) and produced["kind"].strip():
        produced_by = {"kind": produced["kind"]}
        if isinstance(produced.get("detail"), str):
            produced_by["detail"] = produced["detail"]
    else:
        produced_by = {"kind": PROVISIONAL_PRODUCER_UNATTRIBUTED}

    ev_refs = [{
        "project": merged["project"],
        "path": relpath,
        "kind": "session_jsonl",
    }]
    for ref in ev_refs:  # 05 §2 line 44: no brace/glob shorthand, canonical relative path
        if any(ch in ref["path"] for ch in SHORTHAND_CHARS):
            return None, "evidence_refs_path_shorthand"

    locator = raw.get("locator")
    if not isinstance(locator, str) or not locator.strip():
        locator = relpath  # the inventory path is itself a resolvable locator
    locator = scrub(locator, compiled)[0]  # redact BEFORE it participates in evidence identity

    cohort_only = {k: v for k, v in merged.items() if k in COHORT_KEYS}
    key = _sha({"content_hash": chash, "cohort": prov.cohort_key(cohort_only),
                "locator": locator, "source_class": sc})
    rec = {
        "schema_version": prov.SCHEMA_VERSION,
        "evidence_id": key,  # content-addressed, full sha256 (see S01 header note on DM-1)
        "source_class": sc,
        "locator": locator,
        # 05 line 177 / kernel cohort_key: the identity triple only, never `layer`.
        "cohort": dict(cohort_only),
        # 05 line 174 (SC11): the typed scope triple, never `path`. S04/S05 read this, S10 (wave 3)
        # is its adjudicated consumer.
        "scope": {k: v for k, v in merged.items() if k in SCOPE_KEYS},
        "content": content,
        "produced_by": produced_by,
        "content_hash": chash,
        "origin": {"problem": problem, "why": why, "source_refs": clean_refs},
        "evidence_refs": ev_refs,
        # 05 §2 line 45: with no run record the forensic status can only be UNVERIFIED, and only
        # an eval/audit runner may write anything else. S01 is capture, so it never claims VERIFIED.
        "evidence": {"status": "UNVERIFIED", "status_basis": None},
        "generation": {
            "round_id": args.round_id,
            "pass_id": args.pass_id,
            "compiler_version": PROVISIONAL_COMPILER_VERSION,
            # 04 §0 line 15 (invariant #13 Zero-LLM default path): S01 calls no model.
            "model_id": "none",
            "config_sha": config_sha,
            "created_at": created_at,
        },
        "record_locator": "ledger:PENDING#%s" % chash[:16],
    }
    if isinstance(raw.get("record_type"), str):
        rec["record_type"] = raw["record_type"]
    # Redact every persisted untrusted string, not just the excerpt. Hashes above already
    # cover the scrubbed full body; metadata must never become a secret side channel.
    def redact_metadata(value):
        if isinstance(value, str):
            return scrub(value, compiled)[0]
        if isinstance(value, list):
            return [redact_metadata(item) for item in value]
        if isinstance(value, dict):
            return {key: redact_metadata(item) for key, item in value.items()}
        return value
    for field in ("origin", "produced_by", "locator", "record_type"):
        if field in rec:
            rec[field] = redact_metadata(rec[field])
    violations = prov.validate_evidence(rec)  # kernel is the sole schema witness at capture
    if violations:
        return None, "kernel_schema_invalid:" + ";".join(violations)
    return rec, None


# ------------------------------------------------------------------ outputs
def atomic_write(path: str, text: str) -> None:
    import kd_store_layout as layout
    layout.assert_staging_path(path)
    layout.assert_staging_path(path + ".tmp")
    if os.path.lexists(path + ".tmp"):
        raise CaptureFailure("refusing an existing temporary output")
    tmp = path + ".tmp"
    with open(tmp, "x", encoding="utf-8") as fh:  # KD-WRITE-EXEMPT: S01 evidence.jsonl/capture_status.json tmp half -- derived capture artifact under --out-dir, recomputable from the raw transcripts S02 enumerated; never a store record
        fh.write(text)  # KD-WRITE-EXEMPT: transient capture buffer into evidence.jsonl.tmp -- regenerated per round from source transcripts, so no promotion state depends on it
        fh.flush()
        os.fsync(fh.fileno())  # KD-WRITE-EXEMPT: durability of the derived evidence.jsonl.tmp only; fsyncing a regenerable capture artifact does not make it authoritative (CM-13)
    os.replace(tmp, path)  # KD-WRITE-EXEMPT: publish evidence.jsonl / capture_status.json into the CLI --out-dir -- S12's commit_batch owns every write under store/, so this projection cannot reach the promotion tree


def write_capture_status(path: str, doc: str) -> None:
    atomic_write(path, doc)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="kd_ingest.py",
        description="S01: capture inventory-listed raw event streams into evidence.jsonl "
                    "(scrub-before-truncate, fail-closed on missing provenance).")
    parser.add_argument("--inventory", required=True, help="S02 inventory.json")
    parser.add_argument("--raw-dir", required=True, help="raw session/event-stream directory")
    parser.add_argument("--redaction-rules", required=True,
                        help='JSON: {"patterns": ["<regex>", ...]} -- ADDED to the builtin set')
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--allow-event-kind", action="append", default=[],
                        help="event kind admitted by the allow-list (repeatable, REQUIRED -- no default)")
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--layer", required=True, choices=["project", "global", "cohort"],
                        help="05 §5.3 line 174 enum. Required: a missing layer must never be "
                             "defaulted to global (05 §5.3 S1, line 176).")
    parser.add_argument("--scope-path", default="")
    parser.add_argument("--text-field", default="excerpt",
                        help="key holding the raw body in each event record (host adapter knob)")
    parser.add_argument("--source-class-map", default=None,
                        help='JSON: {"<event_kind>": "<source_class>"} -- operator declaration for '
                             'events that do not state a source_class. Values must be one of the '
                             'kernel enum; there is no built-in map.')
    parser.add_argument("--round-id", default="round-3")
    parser.add_argument("--pass-id", default="wave-1")
    parser.add_argument("--excerpt-cap-bytes", type=int, default=PROVISIONAL_EXCERPT_CAP_BYTES)
    args = parser.parse_args(argv)

    # Prepare the safe staging sink before inspecting untrusted configuration:
    # every failed capture (including bad mapping types) must leave a marker.
    mapping_path = args.source_class_map
    args.source_class_map = {}
    out_dir = os.path.abspath(args.out_dir)
    import kd_store_layout as layout
    try:
        layout.assert_staging_path(out_dir)
    except layout.LayoutViolation as exc:
        print(f"S01 output refused: {exc}", file=sys.stderr)
        return EXIT_CAPTURE_FAILED
    evidence_path = os.path.join(out_dir, "evidence.jsonl")
    status_path = os.path.join(out_dir, "capture_status.json")
    ledger_path = os.path.join(out_dir, "capture-ledger.jsonl")
    os.makedirs(out_dir, exist_ok=True)  # KD-WRITE-EXEMPT: --out-dir scaffolding for S01's capture artifacts (evidence.jsonl, capture_status.json, capture-ledger.jsonl) -- a run directory, not the durable store layout
    created_at = _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")

    def fail(reason, extra=None):
        """exit 2 path: capture failed => NO evidence this round, and the failure is a VISIBLE
        marker, never the same shape as a normal empty result (`12` line 551, CM-01)."""
        atomic_write(evidence_path, "")
        doc = {
            "schema": CAPTURE_SCHEMA,
            "status": "failed",
            "exit_code": EXIT_CAPTURE_FAILED,
            "visible_marker": {"marker": MARKER_FAILED, "same_as_normal_empty": False,
                               "carried_by": status_path},
            "reason": reason,
            "counts": {"seen": 0, "adopted": 0, "dropped": 0},
            "dropped": [],
            "redaction": {"scrub_before_truncate": True, "patterns_applied": 0, "truncated": []},
            "repair": {"attempted": False,
                       "refused_reason": "the only legal repair for a schema-invalid evidence "
                                         "record would be inventing the missing provenance field "
                                         "(`12` line 681); so no bounded retry is attempted here"},
        }
        if extra:
            doc.update(extra)
        write_capture_status(status_path, json.dumps(doc, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
        print("S01 exit 2 (capture failed, this round has no evidence): %s" % reason, file=sys.stderr)
        return EXIT_CAPTURE_FAILED

    # Source-class mapping and allow-list checks are input-validation failures, not
    # successful empty captures. Neither can bypass the visible failure status.
    if mapping_path:
        try:
            loaded = load_json_object(mapping_path, "source class map")
        except CaptureFailure:
            return fail("source class map unavailable or invalid")
        for value in loaded.values():
            if type(value) is not str or value not in ALL_SOURCE_CLASSES:
                return fail("source class map contains an invalid source class")
        args.source_class_map = loaded

    if not args.allow_event_kind:
        return fail("event allow-list missing: --allow-event-kind required")

    try:
        inventory = load_json_object(args.inventory, "inventory.json")
        rules_doc = load_json_object(args.redaction_rules, "redaction rules")
    except CaptureFailure as exc:
        return fail(str(exc))

    patterns = rules_doc.get("patterns")
    if not isinstance(patterns, list) or any(not isinstance(p, str) for p in patterns):
        return fail("redaction rules 'patterns' must be an array of strings")
    try:
        compiled = compile_rules(list(BUILTIN_REDACTION_PATTERNS) + patterns)
    except CaptureFailure as exc:
        return fail(str(exc))

    entries = inventory.get("entries")
    if not isinstance(entries, list):
        return fail("inventory.json has no entries array")

    raw_abs = os.path.realpath(args.raw_dir)
    root_abs = inventory.get("root")
    if not isinstance(root_abs, str):
        return fail("inventory.json has no root")
    root_abs = os.path.realpath(root_abs)
    try:
        raw_rel = os.path.relpath(raw_abs, root_abs).replace(os.sep, "/")
    except ValueError:
        return fail("raw-dir is outside the inventory root")
    if raw_rel.startswith(".."):
        return fail("raw-dir %s is outside the inventory root %s -- the inventory does not cover "
                    "this round's input stream" % (raw_abs, root_abs))

    selected = []
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            return fail("inventory.json entry without a path field")
        p = entry["path"]
        try:
            full = layout.safe_path(root_abs, p)
        except layout.LayoutViolation:
            return fail("inventory contains an unsafe path")
        if raw_rel == "." or p == raw_rel or p.startswith(raw_rel + "/"):
            if not os.path.isfile(full) or os.path.getsize(full) != entry.get("size"):
                return fail("inventory entry is missing or changed")
            if entry.get("sha256") is None:
                return fail("inventory entry has no observed full-file digest")
            selected.append((p, full, entry))
    if not selected:
        return fail("inventory covers no file under raw-dir %s" % raw_rel)

    cohort_scope = {"workspace": args.workspace, "project": args.project,
                    "layer": args.layer, "path": args.scope_path}
    config_sha = _sha({
        "allow_event_kind": sorted(args.allow_event_kind),
        "redaction_patterns": sorted(list(BUILTIN_REDACTION_PATTERNS) + patterns),
        "excerpt_cap_bytes": args.excerpt_cap_bytes,
        "scope": cohort_scope,
        "text_field": args.text_field,
        "source_class_map": dict(args.source_class_map),
        "inventory_digest": inventory.get("digest"),
    })

    records, dropped, truncated, seen = [], [], [], 0
    for rel, full, entry in selected:
        try:
            rows, failures = load_raw_lines(full, expected_entry=entry)
        except CaptureFailure as exc:
            return fail(str(exc))
        for f in failures:
            dropped.append(f)
            seen += 1
        for raw in rows:
            seen += 1
            rec, reason = build_record(raw, rel, cohort_scope, args, compiled, config_sha, created_at)
            if reason:
                # Rejected input is still untrusted. An unknown/non-string event kind may
                # contain a whole private payload; never copy it into the diagnostic sink.
                # Keep only a scrubbed operator-allowlisted name, or explicit unknown/null.
                raw_kind = raw.get("event_kind")
                safe_kind = (scrub(raw_kind, compiled)[0]
                             if isinstance(raw_kind, str) and raw_kind in args.allow_event_kind
                             else None)
                dropped.append({"path": rel, "line": raw.get("_line"),
                                "reason": scrub(reason, compiled)[0], "event_kind": safe_kind})
                continue
            records.append(rec)
            if raw.get("_truncated"):
                truncated.append({"path": rel, "line": raw.get("_line"),
                                  "evidence_id": rec["evidence_id"]})

    if records:
        # The ledger line is written FIRST so that record_locator can point at it: 05 §2 line 51
        # requires the body to carry only a store-side ledger reference, never the authority.
        prov.append_ledger(ledger_path, {  # kernel-owned append-only ledger, reused
            "type": "capture_batch",
            "round_id": args.round_id,
            "config_sha": config_sha,
            "created_at": created_at,
            "adopted": len(records),
            "dropped": len(dropped),
            "evidence_ids": sorted(r["evidence_id"] for r in records),
        })
        for rec in records:
            rec["record_locator"] = "ledger:%s#%s" % (ledger_path, config_sha[:16])

    atomic_write(evidence_path, "".join(
        json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in records))

    # 12 line 551 row 1: a capture failure must be a VISIBLE marker and must never share the
    # shape of a normal empty result. Full drop == no evidence this round == the exit-2 branch;
    # partial drop (some records survived) == the exit-10 branch, which requires the marker file.
    all_dropped = bool(dropped) and not records
    marker = None
    if dropped:
        marker = {"marker": MARKER_FAILED if all_dropped else MARKER_PARTIAL,
                  "same_as_normal_empty": False,
                  "carried_by": status_path, "dropped_count": len(dropped)}
    doc = {
        "schema": CAPTURE_SCHEMA,
        "status": "failed" if all_dropped else ("partial_drop" if dropped else "ok"),
        "exit_code": EXIT_CAPTURE_FAILED if all_dropped else (EXIT_PARTIAL_DROP if dropped else EXIT_OK),
        "visible_marker": marker,
        "counts": {"seen": seen, "adopted": len(records), "dropped": len(dropped)},
        "dropped": dropped,
        "redaction": {"scrub_before_truncate": True, "patterns_applied": len(compiled),
                      "builtin_patterns": len(BUILTIN_REDACTION_PATTERNS),
                      "operator_patterns": len(patterns), "truncated": truncated},
        "repair": {"attempted": False,
                   "refused_reason": "bounded repair retry (`12` line 551 row 3 / 04 C1) would "
                                     "require filling a missing adjudicated field; missing "
                                     "evidence is not invented (`12` line 681)"},
        "inventory_digest": inventory.get("digest"),
        "raw_rel_prefix": raw_rel,
        "config_sha": config_sha,
    }
    write_capture_status(status_path, json.dumps(doc, ensure_ascii=False, sort_keys=True, indent=2) + "\n")

    if all_dropped:
        print("S01 exit 2 (capture failed, this round has no evidence): %d of %d candidate "
              "events dropped, marker %s written" % (len(dropped), seen, MARKER_FAILED),
              file=sys.stderr)
        return EXIT_CAPTURE_FAILED
    if dropped:
        if not os.path.exists(status_path):
            print("S01 exit 2: marker was not written, refusing to report a partial drop",
                  file=sys.stderr)
            return EXIT_CAPTURE_FAILED
        print("S01 exit 10: %d adopted, %d dropped, visible marker %s written"
              % (len(records), len(dropped), MARKER_PARTIAL))
        return EXIT_PARTIAL_DROP
    print("S01 ok: %d adopted, 0 dropped" % len(records))
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
