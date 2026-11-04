#!/usr/bin/env python3
"""S03 kd_selfsource_filter -- ingestion-side self-generated evidence exclusion.

Contract (12-SKILL-DESIGN-BRIEF.md line 44 / w1a.json S03):
  inputs  : evidence.jsonl + the exclusion set (RESOLVED absolute paths + content hashes)
  outputs : evidence.filtered.jsonl, excluded_report.json
  exit    : 2 = the exclusion predicate is UNDECIDABLE -- continuing silently is forbidden;
            0 = decidable (0 is also the "no self-produced artifacts" case the contract names)
  cluster : CM-09 self-generated-evidence-exclusion, DC-SP-1 gate 1

DC-SP-1 gate 1 verbatim (12-SKILL-DESIGN-BRIEF.md lines 517-524 and 551):
  按解析后绝对路径 + 内容哈希匹配；每条被采纳证据都要断言其来源不在排除集内；
  谓词失效或不可判定 ⇒ fail-closed 为「本轮无证据」，不得静默继续。

WHAT THIS SCRIPT IS NOT: it is not a second filter. `kd_provenance.is_self_generated` stays the
single authority for *what counts as self-generated*; this script contributes only the
ingestion-side mechanics the kernel cannot know -- resolving locators to absolute paths and
matching them and content hashes against the declared exclusion set -- plus the report and the
fail-closed exit. A file living in `store/` or produced by the compiler (kind=compiler) is handled by the kernel
(signal 3 / signal 2), and no store-path rule is duplicated here.

Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import kd_provenance as prov  # reuse only -- NEVER edit the kernel

EXIT_OK = 0
EXIT_UNDECIDABLE = 2

REPORT_SCHEMA = "kd-excluded-report/1"
MARKER_UNDECIDABLE = "KD-EXCLUSION-PREDICATE-UNDECIDABLE"
HEX64 = re.compile(r"^[0-9a-f]{64}$")


class PredicateUndecidable(Exception):
    """Raised for the whole run: the predicate cannot be evaluated, so the round has no evidence."""


def load_exclusions(path: str):
    """The contract input is *resolved absolute paths + content hashes*. Malformed or
    half-resolved entries make the predicate undecidable -- they are never quietly ignored."""
    try:
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
    except OSError as exc:
        raise PredicateUndecidable("exclusion set unreadable: %s (%s)" % (path, exc))
    except ValueError as exc:
        raise PredicateUndecidable("exclusion set malformed JSON: %s (%s)" % (path, exc))
    if not isinstance(doc, dict):
        raise PredicateUndecidable("exclusion set must be a JSON object: %s" % path)
    paths = doc.get("paths", [])
    hashes = doc.get("content_hashes", [])
    if not isinstance(paths, list) or not isinstance(hashes, list):
        raise PredicateUndecidable("exclusion set 'paths'/'content_hashes' must be arrays")
    resolved = []
    for p in paths:
        if not isinstance(p, str) or not p.strip():
            raise PredicateUndecidable("exclusion path is not a non-empty string: %r" % (p,))
        if not os.path.isabs(p):
            # 解析后绝对路径 is the contract: an unresolved entry cannot be matched against a
            # resolved locator, so the predicate has no answer for it.
            raise PredicateUndecidable("exclusion path is not absolute (contract requires "
                                      "resolved absolute paths): %r" % (p,))
        resolved.append(os.path.realpath(p))
    for h in hashes:
        if not isinstance(h, str) or not HEX64.match(h):
            raise PredicateUndecidable("exclusion content_hash is not 64-hex: %r" % (h,))
    return set(resolved), set(hashes), doc


def record_hash(rec):
    if isinstance(rec.get("content_hash"), str) and HEX64.match(rec["content_hash"]):
        return rec["content_hash"]
    if isinstance(rec.get("content"), dict):
        return prov.content_hash(rec["content"])  # kernel function, reused
    return None


def evaluate(rec, excluded_paths, excluded_hashes, resolve_root, artifact_root):
    """Return (verdict, detail). verdict in {'excluded', 'adopted', 'undecidable'}.

    The kernel is asked first and is authoritative. Path/hash membership is only consulted for
    records the kernel did not already exclude, and a record whose membership cannot be resolved
    while it claims independence is UNDECIDABLE -- never adopted by default."""
    if not isinstance(rec, dict):
        return "undecidable", "record is not a JSON object"
    try:
        if prov.is_self_generated(rec, artifact_root):
            return "excluded", "kernel_is_self_generated"
    except Exception as exc:  # the predicate itself blew up -> fail closed (DC-SP-1 gate 1)
        return "undecidable", "kernel predicate raised: %s: %s" % (type(exc).__name__, exc)

    locator = rec.get("locator")
    if not isinstance(locator, str) or not locator.strip():
        return "undecidable", "locator missing or blank: membership in the path exclusion set " \
                              "cannot be resolved for a record that claims independence"
    abs_loc = locator if os.path.isabs(locator) else os.path.join(resolve_root, locator)
    abs_loc = os.path.realpath(abs_loc)
    if abs_loc in excluded_paths:
        return "excluded", "resolved_path_in_exclusion_set"
    chash = record_hash(rec)
    if chash is None:
        return "undecidable", "no content_hash and no content body: hash membership cannot be " \
                              "evaluated for a record that claims independence"
    if chash in excluded_hashes:
        return "excluded", "content_hash_in_exclusion_set"
    return "adopted", {"resolved_path": abs_loc, "content_hash": chash}


def atomic_write(path: str, text: str) -> None:
    import kd_store_layout as layout
    layout.assert_staging_path(path)
    layout.assert_staging_path(path + ".tmp")
    if os.path.lexists(path + ".tmp"):
        raise OSError("refusing an existing temporary output")
    tmp = path + ".tmp"
    with open(tmp, "x", encoding="utf-8") as fh:  # KD-WRITE-EXEMPT: S03 evidence.filtered.jsonl tmp half -- the exclusion pass output, recomputable from S01's evidence.jsonl + the exclusion set
        fh.write(text)  # KD-WRITE-EXEMPT: filtered-evidence buffer -- a projection over captured evidence; support counts are always recomputed from it, never stored in it
        fh.flush()
        os.fsync(fh.fileno())  # KD-WRITE-EXEMPT: fsync of the derived filtered tmp file; durability here does not confer authority (CM-13)
    os.replace(tmp, path)  # KD-WRITE-EXEMPT: evidence.filtered.jsonl + excluded_report.json publish into --out-dir -- run artifacts under operator control, not the store


def write_report(path: str, doc: str) -> None:
    atomic_write(path, doc)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="kd_selfsource_filter.py",
        description="S03: apply the self-generated exclusion predicate to evidence.jsonl. "
                    "Undecidable predicate => exit 2 (fail closed, never continue silently).")
    parser.add_argument("--evidence", required=True, help="S01 evidence.jsonl")
    parser.add_argument("--exclusions", required=True,
                        help='JSON: {"paths": ["<abs path>", ...], "content_hashes": ["<sha256>", ...]}')
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--resolve-root", default=None,
                        help="root used to resolve relative locators (default: dirname of --evidence)")
    parser.add_argument("--artifact-root", default="store",
                        help="passed through to kd_provenance.is_self_generated unchanged")
    parser.add_argument("--ledger", default=None,
                        help="optional append-only ledger path (kd_provenance.append_ledger)")
    args = parser.parse_args(argv)

    out_dir = os.path.abspath(args.out_dir)
    import kd_store_layout as layout
    try:
        layout.assert_staging_path(out_dir)
        if args.ledger:
            layout.assert_staging_path(args.ledger)
    except layout.LayoutViolation as exc:
        print(f"S03 output refused: {exc}", file=sys.stderr)
        return 2
    os.makedirs(out_dir, exist_ok=True)  # KD-WRITE-EXEMPT: --out-dir scaffolding for S03's derived artifacts; the store tree is untouched by this module
    filtered_path = os.path.join(out_dir, "evidence.filtered.jsonl")
    report_path = os.path.join(out_dir, "excluded_report.json")
    resolve_root = os.path.abspath(args.resolve_root or os.path.dirname(os.path.abspath(args.evidence)))

    def fail_closed(reason, extra=None):
        """谓词不可判定 ⇒ fail-closed 为本轮无证据 (12 line 551). The filtered file is written
        EMPTY so no downstream step can consume an un-audited stream, and the reason is a visible
        marker rather than a silent zero."""
        atomic_write(filtered_path, "")
        doc = {
            "schema": REPORT_SCHEMA,
            "predicate_decidable": False,
            "exit_code": EXIT_UNDECIDABLE,
            "visible_marker": {"marker": MARKER_UNDECIDABLE, "same_as_normal_empty": False,
                               "carried_by": report_path},
            "reason": reason,
            "adopted": 0,
            "excluded": [],
            "undecidable": [],
        }
        if extra:
            doc.update(extra)
        write_report(report_path, json.dumps(doc, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
        print("S03 exit 2 (exclusion predicate undecidable, this round has no evidence): %s"
              % reason, file=sys.stderr)
        return EXIT_UNDECIDABLE

    # Guard-disabled check comes FIRST: a predicate that is switched off cannot decide anything,
    # and reporting "no self-produced artifacts" for it would be the exact silent continuation the
    # contract forbids. The constant itself is NOT modified here -- only read.
    if not getattr(prov, "SELF_GENERATED_EXCLUSION_ENABLED", False):
        return fail_closed("kernel exclusion guard kd_provenance.SELF_GENERATED_EXCLUSION_ENABLED "
                           "is disabled -- the predicate has no authority to decide")

    try:
        excluded_paths, excluded_hashes, exdoc = load_exclusions(args.exclusions)
    except PredicateUndecidable as exc:
        return fail_closed(str(exc))

    try:
        with open(args.evidence, encoding="utf-8") as fh:
            raw_lines = fh.read().splitlines()
    except OSError as exc:
        return fail_closed("evidence.jsonl unreadable: %s (%s)" % (args.evidence, exc))

    adopted, excluded, undecidable, truncated_dropped = [], [], [], []
    for lineno, line in enumerate(raw_lines, start=1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except ValueError as exc:
            undecidable.append({"line": lineno, "evidence_id": None,
                                "reason": "evidence line is not JSON: %s" % exc})
            continue
        verdict, detail = evaluate(rec, excluded_paths, excluded_hashes,
                                   resolve_root, args.artifact_root)
        eid = rec.get("evidence_id") if isinstance(rec, dict) else None
        if verdict == "adopted":
            adopted.append(rec)
        elif verdict == "excluded":
            excluded.append({"evidence_id": eid, "reason": detail,
                             "source_class": rec.get("source_class"),
                             "locator": rec.get("locator")})
        else:
            undecidable.append({"line": lineno, "evidence_id": eid, "reason": detail})

    if undecidable:
        return fail_closed("%d record(s) could not be decided by the exclusion predicate"
                           % len(undecidable),
                           extra={"undecidable": undecidable,
                                  "would_have_been_adopted": len(adopted),
                                  "would_have_been_excluded": len(excluded)})

    atomic_write(filtered_path, "".join(
        json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in adopted))

    # Every adopted record is asserted to be outside the exclusion set (DC-SP-1 gate 1 wording:
    # 每条被采纳证据都要断言其来源不在排除集内). A violation is an undecidable predicate.
    violations = []
    for rec in adopted:
        chash = record_hash(rec)
        loc = rec.get("locator", "")
        abs_loc = os.path.normpath(loc if os.path.isabs(loc) else os.path.join(resolve_root, loc))
        if chash in excluded_hashes or abs_loc in excluded_paths:
            violations.append({"evidence_id": rec.get("evidence_id"),
                               "resolved_path": abs_loc, "content_hash": chash})
    if violations:
        return fail_closed("adopted evidence still matches the exclusion set (predicate is not "
                           "being applied consistently): %s" % violations,
                           extra={"adopted": len(adopted), "excluded": excluded})

    # The filtered stream is consumed HERE by the kernel's own support function -- that call site
    # is one of the read points S04 counts (05 §5.3 S2, lines 180-181: computed but unconsumed is
    # the defect being closed).
    support = prov.independent_support(adopted, args.artifact_root)

    report = {
        "schema": REPORT_SCHEMA,
        "predicate_decidable": True,
        "exit_code": EXIT_OK,
        "visible_marker": None,
        "self_generated_present": bool(excluded),
        "counts": {"input": len(adopted) + len(excluded), "adopted": len(adopted),
                   "excluded": len(excluded), "undecidable": 0},
        "excluded": excluded,
        "undecidable": [],
        "exclusion_set": {"paths": sorted(excluded_paths), "content_hashes": sorted(excluded_hashes),
                          "declared_only": [k for k in exdoc if k not in ("paths", "content_hashes")]},
        "resolve_root": resolve_root,
        "artifact_root": args.artifact_root,
        "post_filter_support": support,
        "authority_note": "what counts as self-generated is decided by "
                         "kd_provenance.is_self_generated (frozen kernel); this script adds only "
                         "resolved-path / content-hash set membership and the report",
    }
    write_report(report_path, json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n")

    if args.ledger:
        prov.append_ledger(args.ledger, {"type": "selfsource_filter",
                                         "excluded": report["excluded"],
                                         "adopted": len(adopted),
                                         "predicate_decidable": True})
    print("S03 ok: %d adopted, %d excluded (%s)"
          % (len(adopted), len(excluded), "self-products present" if excluded else "无自产物"))
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
