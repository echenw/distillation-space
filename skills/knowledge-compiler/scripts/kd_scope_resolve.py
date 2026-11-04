#!/usr/bin/env python3
"""S04 kd_scope_resolve -- resolve BOTH scope objects and prove each field has a consumer.

Contract (12-SKILL-DESIGN-BRIEF.md line 45 / w1a.json S04):
  inputs  : each evidence / candidate record + scope configuration
  outputs : scope.jsonl (one `scope` and one `cohort` per line) + scope_consumers.json
            (per-field, per-file:line static read points and a verdict per field)
  exit    : 2 = scope consumer missing/pending, or the input contains malformed/rejected
            rows or no resolved rows. A successful consumer scan never excuses invalid data.

TWO SCOPE OBJECTS, ONE AUTHORITATIVE SHAPE EACH (Round 2 left two triples on the page and the
Wave 1 builders had to paper over it):
  * `scope`  = {workspace, project, layer}  -- 05-DATA-MODEL.md line 174 (SC11, CM-54). Its
    adjudicated consumer is the S10 promotion tree (Wave 3): Project Rule and Global Rule are two
    different terminal states, which is what `layer` exists for.
  * `cohort` = {workspace, project, path}   -- 05-DATA-MODEL.md line 177 invariant 4 ("Typed
    3-tuple identity (workspace_id, project_id, path) on every domain row"), which is exactly what
    the frozen kernel reads: kd_provenance.cohort_key() takes workspace, project, path (kernel
    lines 55-63) and is_independent / independent_support read rec["cohort"].

Before this file the two shapes shared ONE key: SC01 embedded SC11's triple under the kernel's
name `cohort`, so `cohort.layer` existed although the kernel never reads it, while `cohort.path`
was optional. S04 now emits both objects separately and the schemas name them separately.
`kd_provenance.cohort_key` was NOT renamed or edited -- it is the frozen kernel, the S19 mutation
gate depends on it, and its REQUIRED_EVIDENCE names `cohort`.

Why the consumer half exists at all: `worker-caveats 02` recorded that `SessionDescriptor.project`
and `cohort_key` were *computed but never used for grouping*, so aggregation / promotion / dedupe
ran globally (05 §5.3 lines 167-181; DD-6 reopen condition item 5, mirrored as DEFERRED id
DD-6-sub44 -- this script makes the defect detectable, it does not re-decide DD-6). 05 §5.3 S2
names the test: "判定方法 = 静态列出该列的全部读取点，为空即拒" and `12` line 764 rule 9 turns it
into exit code 2.

Fail-closed scope rule (05 §5.3 S1, line 176): a missing or unresolvable triple is REJECTED,
never defaulted to `global`.

Stdlib only. `repos/` is never read -- excluded from the static scan by name.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import kd_provenance as prov  # reuse only -- NEVER edit the kernel

EXIT_OK = 0
EXIT_NO_CONSUMER = 2

REPO_ROOT = SCRIPT_DIR  # installed runtime scans its own consumers, never a guessed host root
CONSUMERS_SCHEMA = "kd-scope-consumers/2"

NEVER_SCANNED = ("repos", ".git", "__pycache__", "node_modules", ".venv", "venv")

SCOPE_FIELDS = ("workspace", "project", "layer")            # 05 line 174 (SC11)
COHORT_FIELDS = ("workspace", "project", "path")            # 05 line 177 (identity triple)
LAYERS = ("project", "global", "cohort")

VERDICT_CONSUMED = "CONSUMED"
VERDICT_PENDING = "PENDING_CONSUMER"
VERDICT_NO_CONSUMER = "NO_CONSUMER"
READ = "read"
MATERIALISED = "materialisation"

# Kernel call sites. Matched on the CALL TOKEN, not the module path, so `import kd_provenance as
# prov` + `prov.cohort_key({...})` is recognised; each match is reported with file:line + text.
KERNEL_CALLS = (("cohort_key", re.compile(r"\bcohort_key\s*\(")),
                ("independent_support", re.compile(r"\bindependent_support\s*\(")))

# Per-field read patterns: rule S2 asks for the read points of THE COLUMN, so every field of
# every object gets its own pattern set.
FIELD_PATTERNS = {
    "scope.workspace": [re.compile(r"""scope\.workspace|["']workspace["']""")],
    "scope.project": [re.compile(r"""scope\.project|["']project["']""")],
    "scope.layer": [re.compile(r"""scope\.layer|["']layer["']""")],
    "cohort.workspace": [re.compile(r"""cohort\.workspace|["']workspace["']""")],
    "cohort.project": [re.compile(r"""cohort\.project|["']project["']""")],
    "cohort.path": [re.compile(r"""cohort\.path|["']path["']""")],
}

DEF_LINE = re.compile(r"^\s*(?:async\s+def|def)\s")
COMMENT_LINE = re.compile(r"^\s*#")
# Writing a key into a dict is not reading the column: these shapes are reported, but they can
# never satisfy rule S2 on their own (that is exactly the `02` "computed, never consumed" shape).
MATERIALISATION = (
    re.compile(r"""^[\w.\[\]"']*\[\s*["']\w+["']\s*\]\s*=(?!=)"""),
    re.compile(r"""^["']\w+["']\s*:"""),
    re.compile(r"""[,{]\s*["']\w+["']\s*:"""),
)

# Which consumer role a file plays (mechanical: path fragment -> role). `promotion` is the role
# that decides terminal states, i.e. the adjudicated consumer of `layer`.
# Wave 1 had no such file, so the resolver reported `PENDING_CONSUMER` and exited 2. S10's tree
# landed in Wave 3 (`scripts/kd_gate_tree.py`), so the promotion role now has a real reader.
ROLE_BY_FRAGMENT = (
    ("scripts/kd_provenance.py", "kernel-frozen"),
    ("scripts/kd_gate.py", "kernel-frozen"),
    ("scripts/kd_gate_tree.py", "promotion"),
    ("scripts/kd_identity_key.py", "identity"),
    ("scripts/kd_dedup_exact.py", "grouping-support"),
    ("scripts/kd_selfsource_filter.py", "exclusion"),
    ("scripts/kd_ingest.py", "writer"),
    ("scripts/kd_inventory.py", "writer"),
    ("scripts/kd_scope_resolve.py", "resolver"),
    ("scripts/kd_validate.py", "validation"),
    ("scripts/kd_refs_audit.py", "validation"),
    ("scripts/kd_store_layout.py", "layout"),
    ("scripts/kd_write_txn.py", "promotion"),
    ("tests/", "test"),
)
PROMOTION_ROLE = "promotion"

LAYER_PENDING = {
    "adjudicated_consumer": "S10 promotion tree (05 §5.3 S3/S4; 06-PROMOTION-POLICY.md)",
    "wave": "wave 3",
    "reason": ("`layer` is read in Wave 1 only by non-terminal readers (S05 identity field, S03 "
               "self-source exclusion path check). The reader that makes project/global/cohort "
               "differ as TERMINAL STATES is S10, which is Wave 3. No reader is faked to close "
               "this, and rule S2 is not relaxed."),
    "gap_id": "unknown",
}
# IMPLEMENTATION_GAP: Round 2 decides only "读取点为空即拒" (05 §5.3 S2) and "读取点数 >= 1"
# (`12` line 764 rule 9). It never says whether a field whose ADJUDICATED consumer is not on disk
# yet (PENDING_CONSUMER) exits 0 or 2. The stricter branch is taken for Wave 1: PENDING_CONSUMER
# exits 2 as well, with the reason visible in scope_consumers.json.
# DEFERRED id unknown -- .distill/round-3/DEFERRED-PARAMETERS.yaml has no entry for the
# pending-consumer exit code (nearest neighbour DD-6-sub44 stays deferred; all 52 stay deferred).


class ConsumerScanUnavailable(Exception):
    """The read-point scan itself could not be performed -- 'no consumers' would then be an
    unproven claim, so the scope field cannot be certified either."""


def role_of(rel: str) -> str:
    norm = rel.replace(os.sep, "/")
    for fragment, role in ROLE_BY_FRAGMENT:
        # Installed scans start at scripts/ itself, so their relative names have
        # no monorepo prefix. Match the registered module, not a guessed parent.
        if fragment in norm or (fragment.endswith(".py") and norm == fragment.rsplit("/", 1)[-1]):
            return role
    return "other"


def _classify_line(text: str) -> str:
    stripped = text.strip()
    if any(rx.search(stripped) for rx in MATERIALISATION):
        return MATERIALISED
    return READ


def scan_field_consumers(root: str):
    """Static, read-only per-field scan. Returns (counts, kernel_points, field_points,
    files_scanned, root_abs). `repos/` is never opened."""
    root_abs = os.path.abspath(root)
    if not os.path.isdir(root_abs):
        raise ConsumerScanUnavailable("scan root is not a directory: %s" % root_abs)

    kernel_points = {"%s(cohort)" % name: [] for name, _rx in KERNEL_CALLS}
    field_points = {key: [] for key in FIELD_PATTERNS}
    files_scanned = []

    def unreadable(error):
        raise ConsumerScanUnavailable("directory scan unavailable (" + type(error).__name__ + ")")

    for dirpath, dirnames, filenames in os.walk(root_abs, followlinks=False, onerror=unreadable):
        rel_dir = os.path.relpath(dirpath, root_abs).replace(os.sep, "/")
        dirnames[:] = sorted(d for d in dirnames
                             if d not in NEVER_SCANNED
                             and not os.path.islink(os.path.join(dirpath, d)))
        if rel_dir.split("/")[0] in NEVER_SCANNED:
            continue
        for name in sorted(filenames):
            if not name.endswith(".py"):
                continue
            full = os.path.join(dirpath, name)
            rel = name if rel_dir == "." else "%s/%s" % (rel_dir, name)
            try:
                with open(full, encoding="utf-8") as fh:
                    lines = fh.read().splitlines()
            except (OSError, UnicodeDecodeError) as exc:
                raise ConsumerScanUnavailable("source unavailable (" + type(exc).__name__ + ")") from None
            files_scanned.append(rel)
            for lineno, text in enumerate(lines, start=1):
                if DEF_LINE.match(text) or COMMENT_LINE.match(text):
                    continue          # a definition or a comment is not a consumer
                body = text.strip()
                for kname, rx in KERNEL_CALLS:
                    if rx.search(text):
                        kernel_points["%s(cohort)" % kname].append(
                            {"file": rel, "line": lineno, "role": role_of(rel), "kind": READ,
                             "text": body[:160]})
                for fkey, rxs in FIELD_PATTERNS.items():
                    if any(rx.search(text) for rx in rxs):
                        field_points[fkey].append(
                            {"file": rel, "line": lineno, "role": role_of(rel),
                             "kind": _classify_line(text), "text": body[:160]})
    counts = {k: len(v) for k, v in kernel_points.items()}
    counts.update({"field:%s" % k: len(v) for k, v in field_points.items()})
    return counts, kernel_points, field_points, sorted(set(files_scanned)), root_abs


def _by_file(points):
    per = {}
    for p in points:
        per.setdefault(p["file"], []).append(p["line"])
    return {f: sorted(lines) for f, lines in sorted(per.items())}


def _reads(points):
    return [p for p in points if p["kind"] == READ]


def classify_fields(kernel_points, field_points):
    """Rule S2 per field: enumerate read points, then decide a verdict and an exit code."""
    cohort_kernel = (kernel_points.get("cohort_key(cohort)", [])
                     + kernel_points.get("independent_support(cohort)", []))
    verdicts, offenders = {}, []
    worst = EXIT_OK

    for field in ("workspace", "project", "path"):
        pts = _reads(field_points["cohort.%s" % field])
        consumed = bool(pts) or bool(cohort_kernel)
        code = EXIT_OK if consumed else EXIT_NO_CONSUMER
        verdicts["cohort.%s" % field] = {
            "object": "cohort", "field": field,
            "verdict": VERDICT_CONSUMED if consumed else VERDICT_NO_CONSUMER,
            "exit_code": code, "read_points": pts, "by_file": _by_file(pts),
            "kernel_call_points": len(cohort_kernel),
            "adjudicated_consumer": "S03 exclusion path / S06 support counting / kd_gate -- all "
                                    "through kd_provenance.cohort_key",
            "owner_note": "field names belong to the frozen kernel; S04 proves consumption and "
                          "never re-derives the key"}
        if code != EXIT_OK:
            offenders.append("cohort.%s=%s" % (field, VERDICT_NO_CONSUMER))
            worst = max(worst, code)

    for field in SCOPE_FIELDS:
        key = "scope.%s" % field
        pts = _reads(field_points[key])
        note = {}
        if not pts:
            verdict, code = VERDICT_NO_CONSUMER, EXIT_NO_CONSUMER
            note["reason"] = "rule S2: zero read points for this scope field"
        elif field != "layer":
            verdict, code = VERDICT_CONSUMED, EXIT_OK
        else:
            promo = [p for p in pts if p["role"] == PROMOTION_ROLE]
            if promo:
                verdict, code = VERDICT_CONSUMED, EXIT_OK
            else:
                verdict, code = VERDICT_PENDING, EXIT_NO_CONSUMER
                note.update(dict(LAYER_PENDING,
                                 non_terminal_readers=sorted({p["role"] for p in pts}),
                                 promotion_role_read_points=0))
        verdicts[key] = dict(note, object="scope", field=field, verdict=verdict, exit_code=code,
                             read_points=pts, by_file=_by_file(pts),
                             materialisation_points=[p for p in field_points[key]
                                                     if p["kind"] != READ])
        if code != EXIT_OK:
            offenders.append("%s=%s" % (key, verdict))
            worst = max(worst, code)
    return verdicts, sorted(offenders), worst


def resolve_triple(rec, config_scope):
    """Return one scope.jsonl line carrying BOTH objects. Fail-closed: never a default `global`
    (05 §5.3 S1, line 176)."""
    eid = rec.get("evidence_id") or rec.get("candidate_id") or rec.get("id")
    if not isinstance(eid, str) or not eid.strip():
        return {"evidence_id": "<missing-id>", "resolution": "rejected",
                "reason": "record has no evidence_id/candidate_id"}
    raw_scope = rec.get("scope") if isinstance(rec.get("scope"), dict) else {}
    raw_cohort = rec.get("cohort") if isinstance(rec.get("cohort"), dict) else {}
    unknown = sorted(k for k in raw_scope if k not in SCOPE_FIELDS)
    if unknown:
        return {"evidence_id": eid, "resolution": "rejected",
                "reason": "scope carries fields outside the SC11 set %s: %s"
                          % (list(SCOPE_FIELDS), unknown)}
    unknown = sorted(k for k in raw_cohort if k not in COHORT_FIELDS)
    if unknown:
        # `layer` inside `cohort` is precisely the pre-split overload: the kernel never reads it
        # there, so a writer that put it there invented scope.
        return {"evidence_id": eid, "resolution": "rejected",
                "reason": "cohort carries fields outside the identity triple %s: %s -- `layer` "
                          "belongs to `scope` (05 line 174), `path` to `cohort` (05 line 177)"
                          % (list(COHORT_FIELDS), unknown)}
    scope = {k: v for k, v in (config_scope or {}).items()
             if k in SCOPE_FIELDS and v is not None}
    scope.update({k: v for k, v in raw_scope.items() if v is not None})
    cohort = {k: v for k, v in (config_scope or {}).items()
              if k in COHORT_FIELDS and v is not None}
    cohort.update({k: v for k, v in raw_cohort.items() if v is not None})

    for field in ("workspace", "project"):
        value = scope.get(field)
        if not isinstance(value, str) or not value.strip():
            return {"evidence_id": eid, "resolution": "rejected",
                    "reason": "scope.%s missing or blank -- refused, not defaulted (05 §5.3 S1)"
                              % field}
    layer = scope.get("layer")
    if layer not in LAYERS:
        return {"evidence_id": eid, "resolution": "rejected",
                "reason": "scope.layer %r is outside the adjudicated enum %s -- refused, not "
                          "defaulted" % (layer, list(LAYERS))}
    if "path" not in cohort:
        return {"evidence_id": eid, "resolution": "rejected",
                "reason": "cohort.path missing -- the identity triple is fail-closed on partial "
                          "scope (05 line 177 invariant 4); use \"\" for 'whole project' instead "
                          "of leaving the coordinate unobserved"}
    if not isinstance(cohort["path"], str):
        return {"evidence_id": eid, "resolution": "rejected",
                "reason": "cohort.path must be a string (may be \"\"), got %r" % cohort["path"]}
    for field in ("workspace", "project"):
        value = cohort.get(field)
        if not isinstance(value, str) or not value.strip():
            return {"evidence_id": eid, "resolution": "rejected",
                    "reason": "cohort.%s missing or blank -- identity triple refused (05 line 177)"
                              % field}
        if value != scope[field]:
            return {"evidence_id": eid, "resolution": "rejected",
                    "reason": "scope.%s=%r disagrees with cohort.%s=%r -- one name, one value"
                              % (field, scope[field], field, value)}
    try:
        # S04 consumes the kernel key itself: this call site is a read point, and writing the
        # result into scope.jsonl is what makes "computed but unconsumed" visible.
        key = prov.cohort_key({"workspace": cohort["workspace"],
                               "project": cohort["project"],
                               "path": cohort["path"]})
    except prov.AmbiguousOrigin as exc:
        return {"evidence_id": eid, "resolution": "rejected",
                "reason": "cohort_key undecidable: %s" % exc}
    return {"evidence_id": eid, "resolution": "resolved",
            "scope": {"workspace": scope["workspace"], "project": scope["project"],
                      "layer": layer},
            "cohort": {"workspace": cohort["workspace"], "project": cohort["project"],
                       "path": cohort["path"]},
            "cohort_key": key}


def atomic_write(path: str, text: str) -> None:
    import kd_store_layout as layout
    layout.assert_staging_path(path)
    layout.assert_staging_path(path + ".tmp")
    if os.path.lexists(path + ".tmp"):
        raise OSError("refusing an existing temporary output")
    tmp = path + ".tmp"
    with open(tmp, "x", encoding="utf-8") as fh:  # KD-WRITE-EXEMPT: tmp half of one S04 derived artifact (scope.jsonl / scope_consumers.json) -- staging file for the os.replace below, never a store path
        fh.write(text)  # KD-WRITE-EXEMPT: scope projection body -- recomputable from any evidence JSONL plus the run scope, so it can hold no promotion state of its own
        fh.flush()
        os.fsync(fh.fileno())  # KD-WRITE-EXEMPT: durability of the derived tmp file only; fsyncing a projection does not make it authoritative (CM-13 keeps authority in the store)
    os.replace(tmp, path)  # KD-WRITE-EXEMPT: publish the derived S04 artifact into the caller's --out-dir -- CLI output location, not the authoritative store, so no promotion tree state is reachable through it


def strict_json_line(text: str):
    """Reject duplicate identities and nonfinite JSON before scope resolution."""
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate input JSON key")
            result[key] = value
        return result

    def reject_constant(_value):
        raise ValueError("nonfinite JSON constant")

    def finite_float(value):
        parsed = float(value)
        if not math.isfinite(parsed):
            raise ValueError("nonfinite JSON float")
        return parsed

    return json.loads(text, object_pairs_hook=unique,
                      parse_constant=reject_constant, parse_float=finite_float)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="kd_scope_resolve.py",
        description="S04: emit scope.jsonl carrying the SC11 `scope` triple and the kernel "
                    "`cohort` identity triple, plus scope_consumers.json with per-field, "
                    "per-file:line read points. Exit 2 for invalid/unresolved input, or when "
                    "a scope field has no adjudicated consumer.")
    parser.add_argument("--records", required=True,
                        help="JSONL of evidence or candidates (S01/S03 output, or a candidate stream)")
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--scope-config", default=None,
                        help='JSON: {"workspace","project","layer","path"} fallback run scope. '
                             "Without it a record with no cohort is rejected (fail-closed).")
    parser.add_argument("--scan-root", default=REPO_ROOT,
                        help="explicit source root for static read points (default: package scripts)")
    args = parser.parse_args(argv)

    out_dir = os.path.abspath(args.out_dir)
    import kd_store_layout as layout
    try:
        layout.assert_staging_path(out_dir)
    except layout.LayoutViolation as exc:
        print(f"S04 output refused: {exc}", file=sys.stderr)
        return EXIT_NO_CONSUMER
    os.makedirs(out_dir, exist_ok=True)  # KD-WRITE-EXEMPT: --out-dir scaffolding for derived S04 artifacts -- creates no store directory and holds no durable state
    lines_path = os.path.join(out_dir, "scope.jsonl")
    consumers_path = os.path.join(out_dir, "scope_consumers.json")

    config_scope = {}
    if args.scope_config:
        try:
            with open(args.scope_config, encoding="utf-8") as fh:
                doc = json.load(fh)
        except (OSError, ValueError) as exc:
            print("S04 exit 2: scope config unreadable/malformed: %s (%s)"
                  % (args.scope_config, exc), file=sys.stderr)
            return EXIT_NO_CONSUMER
        if not isinstance(doc, dict):
            print("S04 exit 2: scope config must be a JSON object", file=sys.stderr)
            return EXIT_NO_CONSUMER
        bad = sorted(k for k in doc if k not in set(SCOPE_FIELDS) | set(COHORT_FIELDS))
        if bad:
            print("S04 exit 2: scope config carries keys outside scope%s + cohort%s: %s"
                  % (list(SCOPE_FIELDS), list(COHORT_FIELDS), bad), file=sys.stderr)
            return EXIT_NO_CONSUMER
        config_scope = doc

    try:
        with open(args.records, encoding="utf-8") as fh:
            raw_lines = fh.read().splitlines()
    except OSError as exc:
        print("S04 exit 2: records unreadable: %s (%s)" % (args.records, exc), file=sys.stderr)
        return EXIT_NO_CONSUMER

    lines, malformed = [], []
    for lineno, text in enumerate(raw_lines, start=1):
        if not text.strip():
            continue
        try:
            rec = strict_json_line(text)
        except ValueError as exc:
            malformed.append({"line": lineno, "reason": "not JSON: %s" % exc})
            continue
        if not isinstance(rec, dict):
            malformed.append({"line": lineno, "reason": "JSON is not an object"})
            continue
        lines.append(resolve_triple(rec, config_scope))

    try:
        counts, kernel_points, field_points, files_scanned, scan_root = \
            scan_field_consumers(args.scan_root)
    except ConsumerScanUnavailable as exc:
        print("S04 exit 2: consumer scan unavailable: %s" % exc, file=sys.stderr)
        return EXIT_NO_CONSUMER

    verdicts, offenders, consumer_exit = classify_fields(kernel_points, field_points)
    resolved = [l for l in lines if l["resolution"] == "resolved"]
    rejected = [l for l in lines if l["resolution"] == "rejected"]
    input_refused = bool(malformed or rejected or not resolved)
    exit_code = EXIT_NO_CONSUMER if input_refused else consumer_exit
    total_kernel = sum(len(v) for v in kernel_points.values())
    total_reads = sum(len(_reads(v)) for v in field_points.values())
    consumers = {
        "schema": CONSUMERS_SCHEMA,
        "scan_root": scan_root,
        "never_scanned": list(NEVER_SCANNED),
        "python_files_scanned": len(files_scanned),
        "objects": {
            "scope": {"fields": list(SCOPE_FIELDS),
                      "authority": "05-DATA-MODEL.md line 174 (SC11 / CM-54 typed scope triple)",
                      "adjudicated_consumer": "S10 promotion tree (Wave 3); S05 identity and S03 "
                                              "exclusion are the Wave 1 non-terminal readers"},
            "cohort": {"fields": list(COHORT_FIELDS),
                       "authority": "05-DATA-MODEL.md line 177 invariant 4 (typed 3-tuple "
                                    "identity) == kd_provenance.cohort_key's expected keys",
                       "owner": "frozen kernel kd_provenance (names not edited)"},
        },
        "kernel_call_points": kernel_points,
        "field_read_points": field_points,
        "counts": counts,
        "totals": {"kernel_call_points": total_kernel, "field_read_points": total_reads},
        "field_verdicts": verdicts,
        "pending_consumers": {k: v for k, v in verdicts.items() if v["verdict"] == VERDICT_PENDING},
        "no_consumers": [k for k in offenders if k.endswith(VERDICT_NO_CONSUMER)],
        "verdict": "consumed" if not offenders else ",".join(offenders),
        "exit_code": exit_code,
        "exit_code_policy_note": "stricter branch: rule S2 decides 0 read points -> exit 2; "
                                 "PENDING_CONSUMER (adjudicated reader not on disk yet) is also "
                                 "exit 2 in Wave 1. Round 2 did not decide this case and no "
                                 "DEFERRED id covers it -> IMPLEMENTATION_GAP in the module "
                                 "docstring, DEFERRED id unknown (nearest: DD-6-sub44).",
        "scope_lines_emitted": len(lines),
        "scope_lines_resolved": len(resolved),
        "scope_lines_rejected": len(rejected),
        "input_verdict": "REFUSED" if input_refused else "ACCEPTED",
        "rejected_reasons": sorted({l["reason"] for l in rejected}),
        "malformed_input_lines": malformed,
        "method": "static read-only scan of *.py for (a) kernel call tokens cohort_key( / "
                  "independent_support( and (b) per-field patterns; definition and comment lines "
                  "excluded; assignment-target and dict-literal-key occurrences classified as "
                  "materialisation, not reads. 05 §5.3 S2 lines 180-181, 12 line 764 rule 9.",
        "reproducibility": "every point is emitted as file:line plus the raw source text and a "
                           "role, so counts are re-derivable by grep; they move only when a file "
                           "that consumes (or stops consuming) a field changes.",
        "authority_note": "the kernel owns cohort identity; S04 only proves consumption and never "
                          "re-derives the key by its own formula",
    }
    atomic_write(lines_path, "".join(
        json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n" for l in lines))
    atomic_write(consumers_path, json.dumps(consumers, ensure_ascii=False, sort_keys=True,
                                            indent=2) + "\n")

    if input_refused:
        print("S04 exit 2: input refused (%d resolved, %d rejected, %d malformed); "
              "scope consumers cannot turn missing/invalid evidence into success"
              % (len(resolved), len(rejected), len(malformed)), file=sys.stderr)
        return EXIT_NO_CONSUMER
    if consumer_exit != EXIT_OK:
        print("S04 exit %d: scope field(s) computed without an on-disk adjudicated consumer: %s"
              " -- rule S2 (05 §5.3) with the stricter pending-consumer branch"
              % (consumer_exit, ", ".join(offenders)), file=sys.stderr)
        return consumer_exit
    if total_kernel + total_reads == 0:
        print("S04 exit 2: scope triples were computed (%d resolved) but the static scan found "
              "ZERO read points -- computed-but-unconsumed scope is the `02` defect (05 §5.3 S2)"
              % len(resolved), file=sys.stderr)
        return EXIT_NO_CONSUMER
    print("S04 ok: %d scope lines (%d resolved, %d rejected); kernel points %d; field read points "
          "%d; verdict %s" % (len(lines), len(resolved), len(rejected), total_kernel, total_reads,
                              consumers["verdict"]))
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
