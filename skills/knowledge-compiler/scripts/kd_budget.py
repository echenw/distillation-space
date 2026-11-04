#!/usr/bin/env python3
"""S18 kd_budget -- artifact and injection policy plus read-size diagnostics (CM-31 + CM-51).

Contract row (12-SKILL-DESIGN-BRIEF.md:126):
  inputs  whole artifact (frontmatter included) + selected-file sizes + injection blocks
  outputs write / injection verdicts, informational sizes, visible marker
  exit    2=write-side overflow; selected-file measurement is informational

Authority: .distill/round-2/09-CONTEXT-BUDGET.md
  §1.1 write/create layer  -> HARD REFUSAL (not a warning), measures the WHOLE artifact
                              including frontmatter
  §1.2 documents a host-specific chain cap; it is NOT adopted for Skill reads
  §1.3 injection layer     -> deterministic whole-block skip + visible marker
  §1.5                     -> warn-only is legal only when the generator is not the Owner;
                              for our own artifacts the disposition is the strongest one
  §3                       -> "threshold and the gate that runs must share one source, locked
                              by a test to the same number" is a CORE constraint
  §4 item10/11/12          -> numbers Round 2 left undecided

NO THRESHOLD LIVES IN THIS FILE. Every cap value is read from
`../references/budget-config.json` (the single definition point) and `verify_source_lock()`
re-reads the authority document and refuses to decide at all when the two stop agreeing.
The AST threshold binding of 09 §3 stayed IMPLEMENTATION_DETAIL (DD-5-sub35) and was NOT
built; the same-source lock was built instead.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG = os.path.join(HERE, os.pardir, "references", "budget-config.json")

EXIT_OK = 0
EXIT_WRITE_OVERFLOW = 2        # contract: hard refusal, nothing emitted
EXIT_CANNOT_DECIDE = 4         # config shape / source lock / authority mismatch: fail closed
EXIT_USAGE = 5

LAYERS = ("write", "injection")
ENFORCE_GATES = ("hard_refusal", "deterministic_skip", "advisory_mark")
REFUSAL_REASONS = ("DEFERRED", "IMPLEMENTATION_GAP")


class BudgetConfigError(Exception):
    """The config or the authority it is locked to is unusable; no verdict is produced."""


# ----------------------------------------------------------------------- config (the source)
def load_config(path: str = DEFAULT_CONFIG) -> dict:
    try:
        with open(path, encoding="utf-8") as fh:                    # read-only
            cfg = json.load(fh)
    except (OSError, ValueError) as exc:
        raise BudgetConfigError(f"budget config unreadable at {path}: {exc}") from exc
    validate_shape(cfg, path)
    return cfg


def validate_shape(cfg: dict, origin: str = "config") -> None:
    """The invariants the SC10 schema states, checked before any verdict is trusted.

    A cap that enforces must carry a value; a cap that does not enforce must carry NO value
    plus a reason and an id. That asymmetry is what makes "we refused to invent a number"
    mechanically visible instead of a comment.
    """
    if cfg.get("status") != "provisional":
        raise BudgetConfigError(f"{origin}: status must stay 'provisional' (09 §4 audit)")
    doc = cfg.get("authority") or {}
    for key in ("doc", "section", "row_pattern"):
        if not doc.get(key):
            raise BudgetConfigError(f"{origin}: authority.{key} missing")
    caps = cfg.get("caps") or []
    if not caps:
        raise BudgetConfigError(f"{origin}: no caps -- a budget gate with no caps is a lie")
    seen = set()
    for cap in caps:
        cid = cap.get("id")
        if not cid or cid in seen:
            raise BudgetConfigError(f"{origin}: cap id missing or duplicated: {cid!r}")
        seen.add(cid)
        if cap.get("layer") not in LAYERS:
            raise BudgetConfigError(f"{origin}/{cid}: unknown layer {cap.get('layer')!r}")
        if cap.get("enforce"):
            if cap.get("value") is None:
                raise BudgetConfigError(f"{origin}/{cid}: enforce=true needs a value")
            if cap.get("gate") not in ENFORCE_GATES:
                raise BudgetConfigError(f"{origin}/{cid}: enforce=true needs a real gate")
        else:
            if cap.get("value") is not None:
                raise BudgetConfigError(f"{origin}/{cid}: a non-enforced cap must carry value=null "
                                        "(09 §4 forbids parking an undecided number here)")
            if cap.get("refusal_reason") not in REFUSAL_REASONS:
                raise BudgetConfigError(f"{origin}/{cid}: refusal_reason must be DEFERRED or "
                                        "IMPLEMENTATION_GAP")
            if not (cap.get("deferred_id") or cap.get("gap_ref")):
                raise BudgetConfigError(f"{origin}/{cid}: refusal must name the id it waits on")
        for key in ("authority_item", "authority_token"):
            if not cap.get(key):
                raise BudgetConfigError(f"{origin}/{cid}: {key} missing")


def enforced_caps(cfg: dict, layer: str = None) -> list:
    return [c for c in cfg["caps"] if c["enforce"] and (layer is None or c["layer"] == layer)]


def refused_caps(cfg: dict) -> list:
    return [c for c in cfg["caps"] if not c["enforce"]]


# --------------------------------------------------------------------- source lock (09 §3)
def authority_rows(cfg: dict, root: str = None) -> dict:
    """{item number -> the authority table row text}, read from the frozen Round 2 document.

    RH-P0-02 / §6: `root` must be given explicitly (a Repo-A build-time/CI authority root). This
    runtime module no longer guesses a monorepo root via HERE/../../.. -- an installed Skill does
    not carry `.distill`, so the source-lock is a build-time check, never a runtime dependency."""
    doc = cfg["authority"]["doc"]
    if root is None and not os.path.isabs(doc):
        raise BudgetConfigError(
            "source-lock needs an explicit --authority-root (RH-P0-02, §6): the runtime Skill does "
            f"not guess a monorepo root to reach {doc}")
    path = doc if os.path.isabs(doc) else os.path.join(root, doc)
    if not os.path.exists(path):
        raise BudgetConfigError(f"authority document not reachable: {path}")
    with open(path, encoding="utf-8") as fh:                       # read-only
        text = fh.read()
    section = cfg["authority"]["section"]
    marker = text.find(section)
    if marker < 0:
        raise BudgetConfigError(f"authority section not found: {section!r} in {path}")
    rows = {}
    for line in text[marker:].splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|", line)
        if m:
            rows[m.group(1)] = line
        elif rows and not line.startswith("|"):
            break
    if not rows:
        raise BudgetConfigError(f"no numbered rows parsed under {section!r} of {path}")
    return rows


def _locked_references(cfg: dict) -> list:
    """Every place a quoted value or phrase came from an authority row."""
    refs = [(c["id"], c["authority_item"], c["authority_token"], c.get("value"))
            for c in cfg["caps"]]
    for key in ("ordering", "marker_contract"):
        block = cfg.get(key) or {}
        if block.get("authority_token"):
            refs.append((key, block["authority_item"], block["authority_token"], None))
    for cap in cfg["caps"]:
        sa = cap.get("stricter_alternative")
        if sa:
            refs.append((cap["id"] + ".stricter_alternative", sa["authority_item"],
                         sa["authority_token"], sa.get("value")))
    return refs


def verify_source_lock(cfg: dict, config_path: str = None, root: str = None) -> dict:
    """Prove the config's numbers still equal the numbers in the policy document.

    Three checks per locked reference: (a) the quoted token appears verbatim in its authority
    row; (b) the token contains exactly one integer and it equals the configured value;
    (c) non-enforced caps carry no value at all. A drift in either direction exits 4, which is
    the same class of failure 09 §3 recorded for five projects that documented one number and
    ran another.

    RH-P0-02 / §6: this is a BUILD-TIME/CI source-lock (it re-reads the frozen Round-2 authority
    document). An installed Skill has no monorepo, so with no explicit `root` it reports
    BUILD_TIME_ONLY instead of guessing ../../.. -- the runtime never depends on `.distill`.
    """
    if root is None:
        return {"check": "source-lock", "ok": False, "build_time_only": True,
                "detail": "no --authority-root given: verify_source_lock is a Repo-A build-time/CI "
                          "check that re-reads the frozen Round-2 authority doc (§6); an installed "
                          "Skill does not carry .distill and must not guess a monorepo root "
                          "(RH-P0-02).",
                "exit": EXIT_CANNOT_DECIDE}
    rows = authority_rows(cfg, root)
    mismatches = []
    for cid, item, token, value in _locked_references(cfg):
        row = rows.get(str(item))
        if row is None:
            mismatches.append({"ref": cid, "detail": f"authority row {item} does not exist"})
            continue
        if token not in row:
            mismatches.append({"ref": cid, "detail": f"token {token!r} not found in row {item}"})
            continue
        if value is not None:
            ints = [int(n) for n in re.findall(r"(?<![\d_])\d+(?![\d_])", token.replace("_", ""))]
            if ints != [int(value)]:
                mismatches.append({"ref": cid,
                                   "detail": f"value {value} != number(s) {ints} quoted in row "
                                             f"{item}"})
    return {
        "check": "source-lock",
        "ok": not mismatches,
        "config": os.path.abspath(config_path or DEFAULT_CONFIG),
        "authority": cfg["authority"]["doc"],
        "locked_reference_count": len(_locked_references(cfg)),
        "rows_parsed": len(rows),
        "mismatches": mismatches,
        "exit": EXIT_OK if not mismatches else EXIT_CANNOT_DECIDE,
    }


# --------------------------------------------------------------------------------- measuring
def measure(text: str, unit: str) -> int:
    if unit == "bytes":
        return len(text.encode("utf-8"))
    if unit == "lines":
        return len(text.splitlines())
    if unit == "chars":
        return len(text)
    raise BudgetConfigError(f"unit {unit!r} is not a measurable size (09 §2)")


# --------------------------------------------------------------------- layer 1: write-side hard rejection
def check_write(cfg: dict, artifact: str, object_class: str) -> dict:
    """Whole-artifact (frontmatter included) size verdict. Over a hard cap => refuse the write.

    An undecided class is not a pass: it is `cannot_decide`, because no justified cap exists.
    Explicitly unrestricted Skill descriptions are measured and accepted here; host policy is separate.
    """
    if not object_class:
        # Round 2 never decided which class the compiler's own entry file belongs to: the
        # ladder says level 0 is resident (cap 100 lines) while the delivery bound is a task
        # file (soft 500 / hard 600). Defaulting to one class would raise a hard refusal that
        # is really an undeclared question.
        return {"layer": "write", "disposition": "cannot_decide", "object_class": None,
                "cannot_decide": True, "reason": "CLASS_NOT_DECLARED",
                "exit": EXIT_CANNOT_DECIDE,
                "refused_to_enforce": ["<no object class declared: --class is required>"],
                "detail": "--class is required; 09 never adjudicated the class of an artifact, "
                          "and a guessed class fabricates a gate verdict",
                "checks": [], "measurements": {"bytes": len(artifact.encode("utf-8")),
                                               "lines": artifact.count("\n") + 1,
                                               "chars": len(artifact)},
                "hard_refusal": False}
    caps = [c for c in enforced_caps(cfg, "write")
            if c["object_class"] in (object_class, "*")]
    # A class without its own supported ceiling must not borrow a different class policy.
    absolute = [c for c in caps if c["object_class"] == object_class]
    # External project budgets never become unconditional Rule/Skill limits.
    # A caller can still supply an explicit, class-specific budget policy.
    permitted_without_default = object_class in {
        "rule_body", "skill_task", "skill_resident", "skill_description", "index_projection"}
    checks = []
    hard_over = advisory_over = 0
    for cap in caps:
        actual = measure(artifact, cap["unit"])
        over = actual > cap["value"]
        if over and cap["gate"] == "hard_refusal":
            hard_over += 1
        elif over:
            advisory_over += 1
        checks.append({"cap_id": cap["id"], "unit": cap["unit"], "value": cap["value"],
                       "actual": actual, "over": bool(over), "gate": cap["gate"],
                       "status": "over" if over else "within",
                       "authority_item": cap["authority_item"]})
    undecided = [c["id"] for c in refused_caps(cfg) if c["object_class"] == object_class]
    verdict = {
        "layer": "write",
        "disposition": ("hard_refusal_triggered" if hard_over else
                        "hard_refusal" if caps else
                        "no_applicable_limit" if permitted_without_default else "cannot_decide"),
        "object_class": object_class,
        "measurements": {u: measure(artifact, u) for u in ("bytes", "lines", "chars")},
        "checks": checks,
        "cap_count": len(caps),
        "hard_over_count": hard_over,
        "advisory_over_count": advisory_over,
        "undecided_caps_for_this_class": undecided,
        "hard_refusal": bool(hard_over),
        "cannot_decide": not absolute and not permitted_without_default,
        "warn_only_is_legal_here": False,          # 09 §1.5: we are the artifact Owner
    }
    if verdict["cannot_decide"]:
        verdict["exit"] = EXIT_CANNOT_DECIDE
        verdict["refused_to_enforce"] = undecided or [
            "<no cap declared for this object class: SC10 has no adjudicated value for it>"]
    else:
        verdict["exit"] = EXIT_WRITE_OVERFLOW if hard_over else EXIT_OK
    return verdict


# ----------------------------------------------------------- optional read-size diagnostics
def measure_content(files: list, read=None) -> dict:
    """Count selected input bytes, without a fixed ceiling or a refusal verdict.

    The actual model context capacity is host-dependent; this is NOT an estimate
    of remaining tokens or a gate on reference loading.
    """
    read = read or (lambda p: open(p, "rb").read().decode("utf-8"))
    total, steps = 0, []
    for path in files:
        count = measure(read(path), "bytes")
        total += count
        steps.append({"path": os.path.basename(path), "bytes": count,
                      "cumulative_bytes": total})
    return {"layer": "diagnostic", "disposition": "measurement_only",
            "total_bytes": total, "steps": steps, "enforced": False, "exit": EXIT_OK}


# ------------------------------------------------------------- layer 3: injection, visible skip
def plan_injection(cfg: dict, blocks: list, *, budget_bytes: int) -> dict:
    """Optional, caller-budgeted all-or-nothing planner (not a host size limit).

    A self-reported byte hint is never trusted over the exact UTF-8 text.
    No real source path can be attested by this pure planner.
    """
    if type(budget_bytes) is not int or budget_bytes <= 0:
        raise BudgetConfigError("plan_injection needs an explicit positive budget_bytes")
    if type(blocks) is not list:
        raise BudgetConfigError("injection blocks must be an array")
    seen, validated = set(), []
    for block in blocks:
        if type(block) is not dict or type(block.get("id")) is not str or not block["id"].strip():
            raise BudgetConfigError("each block needs a nonempty id")
        if block["id"] in seen:
            raise BudgetConfigError("injection block IDs must be unique")
        seen.add(block["id"])
        if type(block.get("text")) is not str:
            raise BudgetConfigError("every injection block must contain exact UTF-8 text")
        try:
            size = measure(block["text"], "bytes")
        except UnicodeError as exc:
            raise BudgetConfigError("injection text is not valid UTF-8") from exc
        if "bytes" in block and (type(block["bytes"]) is not int or block["bytes"] != size):
            raise BudgetConfigError("declared bytes must equal exact UTF-8 text bytes")
        if block.get("kind", "evidence") not in ("evidence", "advisory"):
            raise BudgetConfigError("unknown injection block kind")
        if type(block.get("weight", 0)) is not int:
            raise BudgetConfigError("injection block weight must be an integer")
        if type(block.get("updated", "")) is not str or type(block.get("name", "")) is not str:
            raise BudgetConfigError("injection order metadata must be strings")
        locator = block.get("path")
        if locator is not None and (type(locator) is not str or not locator.strip() or
                                    any(c in locator for c in "\r\n\x00")):
            raise BudgetConfigError("block path must be a printable nonempty locator")
        validated.append(dict(block, bytes=size))
    order_key = cfg["ordering"]["injection_break_order"]
    ranked = sorted(validated, key=lambda b: (-b.get("weight", 0),
                                              b.get("updated", ""), b.get("name", b["id"])))
    evidence = [b for b in ranked if b.get("kind", "evidence") != "advisory"]
    advisory = [b for b in ranked if b.get("kind") == "advisory"]
    cap = {"id": "caller_budget_bytes", "value": budget_bytes, "authority_item": None}
    kept, omitted, undecided = [], [], []
    used = 0
    for block in evidence + advisory:
        size = block["bytes"]
        if used + size > budget_bytes:
            if block.get("kind") == "advisory":
                undecided.append("advisory_share_fraction")
                omitted.append(_omit_record(block, size, cap, "advisory_all_or_nothing"))
            else:
                omitted.append(_omit_record(block, size, cap, "whole_block_skip"))
            continue
        used += size
        kept.append({"id": block["id"], "bytes": size,
                     "kind": block.get("kind", "evidence")})
    readable = [b.get("path") for b in evidence + advisory
                if any(o["id"] == b["id"] for o in omitted) and b.get("path")]
    marker = {
        "kept": [k["id"] for k in kept], "kept_bytes": used,
        "budget_bytes": budget_bytes, "omitted": omitted,
        "readable_path": None,  # no source file is checked for actual readability
        "unverified_source_locators": readable,
        "warning_queue": [_warning(o, cap) for o in omitted],
        "disposition": "whole_block_skip",
        "truncation": "NOT_IMPLEMENTED (line-boundary or partial truncation)",
    }
    missing = [f for f in cfg["marker_contract"]["required_fields"] if f not in marker]
    if missing:
        raise BudgetConfigError(f"injection marker fields missing: {missing}")
    return {"layer": "injection", "disposition": "deterministic_skip",
            "cap_id": cap["id"], "budget_bytes": budget_bytes,
            "budget_source": "explicit_caller", "used_bytes": used,
            "order_key": order_key, "kept": kept, "omitted": omitted,
            "undecided_caps_used": sorted(set(undecided)),
            "warn_only_is_legal_here": False, "marker": marker, "exit": EXIT_OK}


def _omit_record(block, size, cap, why):
    return {"id": block.get("id"), "bytes": size, "why": why,
            "cap_id": cap["id"], "authority_item": cap["authority_item"]}


def _warning(omitted, cap):
    return (f"omitted {omitted['id']} ({omitted['bytes']} bytes): over the injection cap "
            f"{cap['id']}={cap['value']} bytes, skipped whole at a block boundary")


# --------------------------------------------------------------------------- CM-51 ladder
def ladder(cfg: dict) -> dict:
    """Machine-readable disclosure ladder for Wave 4's SKILL.md assembly.

    Every level resolves to cap ids; the numbers stay in one place. A level whose cap list is
    empty is honestly unbudgeted and says so -- Wave 4 must not invent a size for it.
    """
    caps = {c["id"]: c for c in cfg["caps"]}
    out = []
    for level in cfg["ladder"]["levels"]:
        resolved = [{"cap_id": cid, "unit": caps[cid]["unit"], "value": caps[cid]["value"],
                     "gate": caps[cid]["gate"], "authority_item": caps[cid]["authority_item"],
                     "provisional": caps[cid].get("linked_deferred")}
                    for cid in level["caps"]]
        out.append(dict(level, resolved_caps=resolved))
    return {"cluster": "CM-51", "authority": cfg["ladder"]["authority"], "levels": out,
            "degraded_fallback": cfg["ladder"]["degraded_fallback"],
            "tier_defect_status": cfg["ladder"]["tier_defect_status"],
            "tier_defect_note": cfg["ladder"]["tier_defect_note"],
            "write_gate_exit": EXIT_WRITE_OVERFLOW}


def deferred_report(cfg: dict) -> dict:
    """What this module refuses to enforce, and the id it is waiting on."""
    return {"refused_caps": [{"id": c["id"], "reason": c["refusal_reason"],
                              "deferred_id": c.get("deferred_id"),
                              "gap_ref": c.get("gap_ref"),
                              "authority_item": c["authority_item"],
                              "basis": c["basis"]} for c in refused_caps(cfg)],
            "deferred_linkage": cfg["deferred_linkage"],
            "enforced_cap_count": len(enforced_caps(cfg)),
            "status": cfg["status"]}


# ------------------------------------------------------------------------------------- CLI
def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        prog="kd_budget.py",
        description="S18 kd_budget: write and injection policy, optional content measurement. "
                    "Exit 0=within, 2=write-side overflow (HARD REFUSAL, nothing emitted), "
                    "4=refuse to decide (source lock or "
                    "undecided cap), 5=usage. No threshold is hardcoded here; see "
                    "references/budget-config.json.",
        epilog="Layers: write (whole artifact) / injection (whole-block skip + marker); "
               "--measure-content is non-enforcing. --ladder shows progressive loading.",
    )
    p.add_argument("--config", default=DEFAULT_CONFIG)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--check-write", metavar="ARTIFACT", help="layer 1 verdict on a file")
    g.add_argument("--measure-content", nargs="+", metavar="FILE",
                   help="report selected input bytes, without an arbitrary refusal threshold")
    g.add_argument("--plan-injection", metavar="BLOCKS.json",
    help="optional planner: JSON blocks with exact text and optional matching bytes")
    p.add_argument("--budget-bytes", type=int,
                   help="explicit positive byte allowance for --plan-injection; no built-in host default")
    g.add_argument("--ladder", action="store_true", help="dump the CM-51 ladder with resolved caps")
    g.add_argument("--caps", action="store_true", help="dump the enforced cap set")
    g.add_argument("--deferred", action="store_true", help="dump what is refused, with ids")
    g.add_argument("--verify-source-lock", action="store_true",
                   help="assert config numbers still equal 09 §4 rows (BUILD-TIME/CI check)")
    p.add_argument("--class", dest="obj_class", default=None,
                   help="artifact class for --check-write (index_projection | skill_resident | "
                        "skill_task | skill_description (no universal limit) | compiler_prompt | quota_slot); "
                        "required, because 09 never adjudicated which class an artifact belongs to "
                        "and a guessed class would produce a hard refusal nobody can act on")
    p.add_argument("--authority-root", default=None,
                   help="explicit repo root holding the frozen Round-2 authority doc, for "
                        "--verify-source-lock (RH-P0-02, §6). Omit in an installed Skill: the "
                        "source-lock is build-time and the runtime never guesses a monorepo root.")
    p.add_argument("--emit", help="write the verdict JSON here; NEVER written on a hard refusal")
    args = p.parse_args(argv)

    try:
        cfg = load_config(args.config)
    except BudgetConfigError as exc:
        print(json.dumps({"check": "config", "ok": False, "detail": str(exc)},
                         ensure_ascii=False))
        return EXIT_CANNOT_DECIDE

    try:
        if args.verify_source_lock:
            verdict = verify_source_lock(cfg, args.config, root=args.authority_root)
        elif args.ladder:
            verdict = ladder(cfg)
        elif args.caps:
            verdict = {"check": "caps", "caps": enforced_caps(cfg),
                       "refused": [c["id"] for c in refused_caps(cfg)]}
        elif args.deferred:
            verdict = deferred_report(cfg)
        elif args.check_write:
            with open(args.check_write, encoding="utf-8") as fh:   # read-only
                artifact = fh.read()
            verdict = check_write(cfg, artifact, args.obj_class)
        elif args.measure_content:
            verdict = measure_content(args.measure_content)
        else:
            verdict = plan_injection(cfg, _read_blocks(args.plan_injection),
                                     budget_bytes=args.budget_bytes)
    except BudgetConfigError as exc:
        print(json.dumps({"check": "budget", "ok": False, "detail": str(exc)},
                         ensure_ascii=False))
        return EXIT_CANNOT_DECIDE
    except (OSError, ValueError) as exc:
        print(json.dumps({"check": "budget", "ok": False, "detail": f"{type(exc).__name__}: {exc}"},
                         ensure_ascii=False))
        return EXIT_USAGE

    print(json.dumps(verdict, ensure_ascii=False, indent=1))
    code = verdict.get("exit", EXIT_OK)
    if code == EXIT_OK and args.emit:
        import kd_store_layout as layout
        try:
            layout.assert_staging_path(args.emit)
        except layout.LayoutViolation as exc:
            print(f"output refused: {exc}", file=sys.stderr)
            return EXIT_USAGE
        # S18's own verdict report: a diagnostic copy no reader treats as authoritative state,
        # so it is not a second durable write path -- S12 kd_write_txn stays the only store
        # writer. This line is unreachable on a hard refusal (exit 2), which is the whole point.
        try:
            layout.write_staging_text(args.emit, json.dumps(verdict, ensure_ascii=False, indent=1))
        except (OSError, layout.LayoutViolation) as exc:
            print(f"output refused: {type(exc).__name__}", file=sys.stderr)
            return EXIT_USAGE
    return code


def _read_blocks(path: str) -> list:
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise BudgetConfigError("duplicate injection JSON key")
            result[key] = value
        return result

    def finite_constant(value):
        raise BudgetConfigError("nonfinite JSON constant in injection blocks")

    try:
        with open(path, encoding="utf-8") as fh:  # read-only
            blocks = json.load(fh, object_pairs_hook=unique,
                               parse_constant=finite_constant)
    except (RecursionError, UnicodeError, ValueError) as exc:
        raise BudgetConfigError("injection JSON is malformed or exceeds parser nesting") from exc
    if not isinstance(blocks, list):
        raise BudgetConfigError("injection blocks must be a JSON array")
    return blocks


if __name__ == "__main__":
    raise SystemExit(main())
