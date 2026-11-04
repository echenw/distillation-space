"""S06 -- kd_dedup_exact: exact grouping, canonical selection, and support that can only be
counted as DISTINCT COHORTS x DISTINCT content_hash.

Round 2 provenance
  12-SKILL-DESIGN-BRIEF.md:114  S06 "inputs `evidence.filtered.jsonl` / 分组结果 + canonical 选定
                                 （字典序最小） / 0；pending remove 幂等重跑必得同结果"
  05-DATA-MODEL.md:157-160 (5.2 a) identity = normalized full-text equality, "canonical = 字典序最小
                                 文件名，已有 pending remove 即幂等，--dry-run 不写不建目录"
  05-DATA-MODEL.md:194-205 (5.4)  counter admission: a counter needs a named writer event + call site
                                 + test; the headline counter-example is `times_applied`, a field with
                                 DEFAULT 0, three increment sites and NO caller, which still drove
                                 ordering, sampling, weighting, rendering and staleness hints.
  05-DATA-MODEL.md:199 (5.4 (3))  "默认值/无值状态不得被渲染成真实数据；模板必须能区分
                                 「从未测得」与「0」"
  05-DATA-MODEL.md:213-216 (5.4)  support_count / distinct_occurrence_count live on Pattern and are
                                 fed by L0 equality hits and canonical occurrence folding -- never by
                                 a raw event counter; M7 (sec 4) forbids the three carriers interoperating.
  12-SKILL-DESIGN-BRIEF.md:234   CM-27 per-item verdict, so a batch never reads as one pass/fail.
  12-SKILL-DESIGN-BRIEF.md:66 (N4) no cross-project/scope counting.

Two rejected drafts are made impossible here rather than commented against:
  * reading a counter with no writer -> every counter on an input record is audited against the
    store's writer manifest first; unregistered or bare-integer counters are REFUSED (exit 3) and
    never enter grouping, support, or the report.
  * merging counters with `max(old, new)` -> support is RECOMPUTED from evidence through
    kd_provenance.independent_support / cohort_key on every run; this module contains no counter
    merge operator at all, and an input that asks for one is refused.

python3 stdlib only. kd_provenance is imported, never edited.

Exit codes: 0 grouping completed / 1 input stream unreadable / 2 S05's identity guard fired /
3 support refused / 4 a named report could not be emitted (never a verdict code -- see
`EXIT_OUTPUT_ERROR`).

W2-A (ESC-W1-01, implementation defect, not a policy change): `12:114` declares S06's input as
`evidence.filtered.jsonl`, so `identity_of()` no longer demands the Stage-3 Pattern-Key or a worker
attribution as preconditions. It passes the semantic statement plus the scope/cohort through and
lets S05 join the two optional axes when a record carries them; the fail-closed half is unchanged
(no scope/cohort or no semantic field -> exit 2). The output document shape -- `groups`, `verdicts`,
`result_digest`, `support` and the intents list -- is untouched, and was re-verified byte-for-byte
against the pre-change S06 on the input class that already worked.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import kd_identity_key as ident          # noqa: E402  (S05: the audited key, no second derivation)
import kd_provenance as prov             # noqa: E402  (Wave 0 kernel: cohort + independent support)

SCHEMA_VERSION = "1"

# --------------------------------------------------------------------------- exit codes
EXIT_OK = 0             # contract: S06 exits 0 on a completed grouping
EXIT_INPUT_ERROR = 1    # unreadable / malformed input stream
EXIT_IDENTITY_GUARD = 2  # inherited from S05: a trim-only identity cannot group anything
EXIT_SUPPORT_REFUSED = 3  # a counter reached the gate with no registered writer, or asked to be merged
#: S06 could not emit a derived report it was told to emit. Deliberately NOT 0/2/3: an unusable
#: output path is neither a completed grouping nor an identity/support verdict, and must not be
#: readable as one -- the same shape W1-F filed against S09's exit 1 traceback. Owned by S05.
EXIT_OUTPUT_ERROR = ident.EXIT_OUTPUT_ERROR

#: counter-ish field names that must never be read as support
COUNTER_SUFFIX = "_count"
BANNED_COUNTER_FIELDS = ("times_applied", "apply_count", "reinforce_count")
#: the rejected merge semantics (05 sec 5.4 / the `max(old, new)` draft)
BANNED_MERGE_STRATEGIES = ("max", "sum", "coalesce", "greatest")

SUPPORT_SEMANTICS = "distinct_cohorts_x_distinct_content_hash"


class SupportRefused(Exception):
    """Refusal to use a counter that has no writer, or to merge counters at all."""

    def __init__(self, findings: list):
        super().__init__("; ".join(f["message"] for f in findings))
        self.findings = findings


# --------------------------------------------------------------------------- input
def read_jsonl(path: str) -> list:
    records = []
    with open(path, encoding="utf-8") as fh:
        for num, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except ValueError as exc:
                raise ValueError(f"{path}:{num}: {exc}") from exc
            if not isinstance(rec, dict):
                raise ValueError(f"{path}:{num}: expected an object")
            rec.setdefault("_source_line", num)
            records.append(rec)
    return records


def load_writer_owners(manifest_path: str | None) -> dict:
    """Registered writers come from the store's single-Owner layout. The layout manifest is read
    through S08 -- this module does not grow its own manifest parser (one Owner per meaning).

    No manifest == no registered writer == fail closed: 05 sec 5.4 condition (1) cannot be
    satisfied by wishful thinking, so a counter with no provable writer is refused.
    """
    if not manifest_path:
        return {}
    import kd_store_layout as layout
    with open(manifest_path, encoding="utf-8") as fh:
        doc = json.load(fh)
    try:
        layout.validate_manifest(os.path.dirname(os.path.abspath(manifest_path)), doc)
    except layout.LayoutViolation as exc:
        raise ValueError("writer manifest rejected by S08") from exc
    return {e["path"]: e["owner"] for e in doc["entries"]}


def _counter_like(key: str) -> bool:
    return key.endswith(COUNTER_SUFFIX) or key in BANNED_COUNTER_FIELDS


def audit_counters(records: list, writer_owners: dict) -> list:
    """05 sec 5.4 made mechanical: an incoming counter is admissible only with
    event -> writer -> consumer -> test AND a writer registered in the store layout."""
    findings = []
    for rec in records:
        eid = rec.get("evidence_id") or rec.get("learning_id") or "?"
        for key, value in rec.items():
            if not _counter_like(key):
                continue
            if not isinstance(value, dict):
                findings.append({
                    "code": "COUNTER_NO_WRITER", "evidence_id": eid, "field": key,
                    "message": f"{eid}.{key}={value!r} is a bare counter with no writer chain; "
                               "05 sec 5.4 (1)(2) refuse it and S06 never reads it as support",
                })
                continue
            missing = [f for f in ("writer_event", "writer_call_site", "consumer", "tests")
                       if not value.get(f)]
            if missing:
                findings.append({"code": "COUNTER_INCOMPLETE_ADMISSION", "evidence_id": eid,
                                 "field": key,
                                 "message": f"{eid}.{key} lacks the admission fields {missing} "
                                            "(05 sec 5.4 (1)(2))"})
                continue
            call_site = str(value["writer_call_site"])
            registered = {o for p, o in writer_owners.items() if p and (
                call_site == p or call_site.startswith(p + "/") or call_site.startswith(p + ":"))}
            if not registered:
                findings.append({"code": "COUNTER_WRITER_UNREGISTERED", "evidence_id": eid,
                                 "field": key,
                                 "message": f"{eid}.{key} names writer {call_site!r}, which the store "
                                            "layout does not register as an owner -- unregistered "
                                            "writers are the `times_applied` shape"})
            if str(value.get("merge_strategy", "")).lower() in BANNED_MERGE_STRATEGIES:
                findings.append({"code": "COUNTER_MERGE_REJECTED", "evidence_id": eid, "field": key,
                                 "message": f"{eid}.{key} asks for merge_strategy="
                                            f"{value['merge_strategy']!r}; support is recomputed from "
                                            "evidence, counters are never merged (05 sec 4 M7 / sec 5.4)"})
    return findings


# --------------------------------------------------------------------------- support semantics
def support_of(members: list, artifact_root: str = "store") -> dict:
    """Support for one identity group, counted ONLY as distinct cohorts x distinct content_hash.

    Composition of the kernel's primitives -- prov.independent_support for the headline numbers
    (so self-generated records can never enter), plus prov.cohort_key/prov.content_hash for the
    (cohort, hash) pair set. Nothing here re-implements independence.
    """
    base = prov.independent_support(members, artifact_root)
    pairs = set()
    for rec in members:
        if not prov.is_independent(rec, artifact_root):
            continue
        digest = rec.get("content_hash") or prov.content_hash(rec.get("content", {}))
        pairs.add((prov.cohort_key(rec.get("cohort") or {}), digest))
    return {
        "semantics": SUPPORT_SEMANTICS,
        "independent_cohorts": base["independent_cohorts"],
        "independent_cohort_count": base["independent_cohort_count"],
        "distinct_content_hash_count": base["distinct_evidence_count"],
        "distinct_cohort_hash_pairs": sorted(f"{c}::{h}" for c, h in pairs),
        "pair_count": len(pairs),
        "excluded": base["excluded"],
        "raw_event_count_never_used": len(members),
    }


# --------------------------------------------------------------------------- grouping
def _content_digest(rec: dict) -> str:
    """05 sec 5.2: content_hash is sha256 of the normalized body. Reuse the kernel's hash, or
    normalize the body ourselves -- but never accept an unverifiable hash silently."""
    stated = rec.get("content_hash")
    derived = prov.content_hash(rec.get("content", {}))
    return derived if not stated else str(stated)


def canonical_of(members: list) -> dict:
    """canonical = lexicographically smallest locator (05 sec 5.2 'canonical = 字典序最小文件名').
    evidence_id is the total tie-break so the choice never depends on input order."""
    return min(members, key=lambda r: (str(r.get("locator", "")), str(r.get("evidence_id", ""))))


def identity_of(rec: dict, spec: dict = None) -> dict:
    """Group on the S05 key. Raises IdentityGuardViolation (-> exit 2) for a trim-only identity,
    for a record that carries no scope/cohort, and for a record that carries no semantic field.

    ESC-W1-01: `12:114` declares S06's input as `evidence.filtered.jsonl`, and an Evidence record
    carries the semantic statement (`origin.problem`) plus `scope`/`cohort` -- it does NOT carry a
    Pattern-Key (`05:126`: LLM 命名, produced at Stage 3 step 12) or a worker attribution. Those two
    are the axes that participate when a record has them (`05:122` writes the identity as
    `sha256(canonical NUL-join)[0:40] ‖ 显式 Pattern-Key 字段` -- two axes, not one conjunction), so
    they are passed through here and S05 validates and joins them if present. `cohort.path` is
    deliberately NOT an identity field: it is the distinct-cohort axis of support (05 sec 5.4).
    """
    cohort = rec.get("cohort") or {}
    scope = rec.get("scope") or {}
    candidate = {
        "pattern_key": rec.get("pattern_key") or rec.get("workflow_key") or rec.get("identity_field"),
        "origin": {"problem": (rec.get("origin") or {}).get("problem")},
        "scope": {"workspace": scope.get("workspace") or cohort.get("workspace"),
                  "project": scope.get("project") or cohort.get("project"),
                  "layer": scope.get("layer") or rec.get("layer")},
        "source_worker": rec.get("source_worker")
                         or (rec.get("produced_by") or {}).get("worker")
                         or rec.get("worker"),
    }
    return ident.checked_derive(candidate, spec or ident.DEFAULT_IDENTITY_SPEC)


def group_exact(records: list, pending_removed: set, spec: dict = None,
                writer_owners: dict = None, artifact_root: str = "store") -> dict:
    """Deterministic exact-duplicate grouping + per-item verdicts + recomputed support."""
    findings = audit_counters(records, writer_owners or {})
    if findings:
        raise SupportRefused(findings)

    groups: dict = {}
    derived: dict = {}          # id(record) -> S05 derivation, so a group can name its key
    for rec in records:
        derivation = identity_of(rec, spec)
        derived[id(rec)] = derivation
        groups.setdefault(derivation["identity_digest"], []).append(rec)

    out_groups, verdicts = [], []
    for key in sorted(groups):
        members = sorted(groups[key], key=lambda r: (str(r.get("locator", "")),
                                                     str(r.get("evidence_id", ""))))
        live = [m for m in members if str(m.get("evidence_id")) not in pending_removed]
        dropped = [m for m in members if str(m.get("evidence_id")) in pending_removed]
        canonical = canonical_of(live) if live else None
        by_hash = {}
        for member in live:
            by_hash.setdefault(_content_digest(member), []).append(member)
        exact_canonical = {digest: canonical_of(same_bytes) for digest, same_bytes in by_hash.items()}
        support = support_of(live, artifact_root) if live else {
            "semantics": SUPPORT_SEMANTICS, "independent_cohorts": [], "independent_cohort_count": 0,
            "distinct_content_hash_count": 0, "distinct_cohort_hash_pairs": [], "pair_count": 0,
            "excluded": [], "raw_event_count_never_used": 0}
        out_groups.append({
            "identity_digest": key,
            "identity": derived[id(canonical)]["identity"] if canonical else None,
            "canonical_evidence_id": canonical.get("evidence_id") if canonical else None,
            "canonical_locator": canonical.get("locator") if canonical else None,
            "content_hashes": sorted({_content_digest(m) for m in live}),
            "member_count": len(live),
            "already_pending_removed": sorted(str(m.get("evidence_id")) for m in dropped),
            "support": support,
            "possible_duplicate": len({_content_digest(m) for m in live}) > 1,
        })
        for m in members:
            eid = str(m.get("evidence_id"))
            if eid in pending_removed:
                verdict = "pending_remove"
            elif canonical is None:
                verdict = "no_live_member"
            elif eid == canonical.get("evidence_id"):
                verdict = "canonical"
            elif eid == exact_canonical[_content_digest(m)].get("evidence_id"):
                verdict = "distinct_evidence"
            else:
                verdict = f"duplicate_of:{exact_canonical[_content_digest(m)].get('evidence_id')}"
            # CM-27: one verdict per item, never a batch pass/fail
            verdicts.append({"evidence_id": eid, "identity_digest": key, "verdict": verdict})

    result = {
        "schema_version": SCHEMA_VERSION,
        "support_semantics": SUPPORT_SEMANTICS,
        "normalizer_set": (spec or ident.DEFAULT_IDENTITY_SPEC).get("normalizer_set"),
        "groups": out_groups,
        "verdicts": verdicts,
        "refusals": [],
    }
    result["result_digest"] = hashlib.sha256(
        json.dumps({"groups": out_groups, "verdicts": verdicts}, sort_keys=True,
                   ensure_ascii=False).encode("utf-8")).hexdigest()
    return result


def pending_removal_intents(result: dict) -> list:
    """Removal intents for duplicates, keyed so a re-run over the same store yields the same set
    (05 sec 5.2 '已有 pending remove 即幂等'). The canonical member never gets an intent."""
    intents = []
    seen = set()
    for grp in result["groups"]:
        for verdict in result["verdicts"]:
            if verdict["identity_digest"] != grp["identity_digest"]:
                continue
            if verdict["verdict"].startswith("duplicate_of:"):
                payload = {"identity_digest": grp["identity_digest"],
                           "evidence_id": verdict["evidence_id"],
                           "keep": verdict["verdict"].split(":", 1)[1]}
                payload["intent_id"] = hashlib.sha256(
                    json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()
                ).hexdigest()[:16]
                # `intent_id` is derived from the payload, so an identical payload is the same
                # intent. Emitting it twice would make an idempotent re-run look like two
                # pending removals for one record (05 sec 5.2).
                if payload["intent_id"] in seen:
                    continue
                seen.add(payload["intent_id"])
                intents.append(payload)
    return sorted(intents, key=lambda i: i["intent_id"])


def load_pending_ids(path: str | None) -> set:
    if not path or not os.path.exists(path):
        return set()
    ids = set()
    for rec in read_jsonl(path):
        eid = rec.get("evidence_id") or rec.get("id")
        if eid:
            ids.add(str(eid))
    return ids


# --------------------------------------------------------------------------- CLI
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="kd_dedup_exact.py",
        description="S06 exact dedup: group `evidence.filtered.jsonl` on the S05 identity key, "
                    "pick the lexicographically smallest locator as canonical, and count support "
                    "as distinct cohorts x distinct content_hash. Counters with no registered "
                    "writer are refused; support is always recomputed, never merged.")
    ap.add_argument("--input", help="evidence.filtered.jsonl")
    ap.add_argument("--pending-remove", help="jsonl of already-issued removal intents (idempotent)")
    ap.add_argument("--manifest", help="store layout manifest (S08) supplying registered writers")
    ap.add_argument("--spec", help="identity field spec (default: the adjudicated minimum)")
    ap.add_argument("--artifact-root", default="store",
                    help="prefix treated as the authoritative store for self-generated exclusion")
    ap.add_argument("--out", help="write the grouping result JSON here")
    ap.add_argument("--emit-intents", help="write the removal intents (jsonl) here")
    ap.add_argument("--dry-run", action="store_true",
                    help="compute and report only; writes nothing (05 sec 5.2)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    # checked by hand: argparse's exit 2 is this package's "identity guard fired" code
    if not args.input:
        print("usage error: --input is required", file=sys.stderr)
        return EXIT_INPUT_ERROR

    try:
        records = read_jsonl(args.input)
    except OSError as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    except ValueError as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    spec = None
    if args.spec:
        try:
            with open(args.spec, encoding="utf-8") as fh:
                spec = json.load(fh)
        except (OSError, ValueError) as exc:
            print(f"input error: {exc}", file=sys.stderr)
            return EXIT_INPUT_ERROR
    try:
        owners = load_writer_owners(args.manifest)
        pending = load_pending_ids(args.pending_remove)
        result = group_exact(records, pending, spec, owners, args.artifact_root)
    except (OSError, ValueError) as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    except SupportRefused as exc:
        print(json.dumps({"refusal": "SUPPORT_REFUSED", "exit": EXIT_SUPPORT_REFUSED,
                          "findings": exc.findings}, ensure_ascii=False, indent=1),
              file=sys.stderr)
        return EXIT_SUPPORT_REFUSED
    except prov.AmbiguousOrigin as exc:
        print(f"input error: incomplete cohort/scope -- {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    except ident.IdentityGuardViolation as exc:
        print(json.dumps({"guard": "IDENTITY_GUARD_FAILED", "exit": EXIT_IDENTITY_GUARD,
                          "violations": exc.violations}, ensure_ascii=False, indent=1),
              file=sys.stderr)
        return EXIT_IDENTITY_GUARD

    payload = json.dumps(result, ensure_ascii=False, sort_keys=True)
    intents = pending_removal_intents(result)
    if not args.dry_run:
        try:
            if args.out:
                ident.write_derived_report(args.out, payload)
            if args.emit_intents:
                ident.write_derived_report(
                    args.emit_intents,
                    "".join(json.dumps(intent, ensure_ascii=False, sort_keys=True) + "\n"
                            for intent in sorted(intents, key=lambda i: i["intent_id"])))
        except OSError as exc:
            print(f"output error: {exc}", file=sys.stderr)
            return EXIT_OUTPUT_ERROR
    if not args.quiet:
        print(payload)
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
