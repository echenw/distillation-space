#!/usr/bin/env python3
"""R01 task-intake record: explicit intent, artifact routing, agent planning, revision audit.

This is a local advisory record, NOT a trusted human approval, knowledge writer,
host permission service, or worker dispatcher. Never interpret its confirmation
field as a G1/S12 authorization. Requires only the Python standard library.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, InvalidOperation
import posixpath
import re
from pathlib import Path

FORMAT = "knowledge-compiler-task-brief/1"
MAX_BYTES = 256 * 1024
MAX_NESTING = 64
MAX_REVISION = 9999
ID = re.compile(r"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$")
HEX = re.compile(r"^[a-f0-9]{64}$")
FILE = re.compile(r"^task-brief\.v([1-9][0-9]*)\.json$")
OUTPUTS = {"materials_only", "skill", "rule", "both", "recommend"}
KINDS = {"skill", "rule"}
MODES = {"propose", "create", "update"}
STYLES = {"workflow", "expert", "review", "mixed"}
DEPTHS = {"quick", "standard", "strict"}
RULE_SURFACES = {"project_rule", "host_global_rule", "knowledge_rule"}
PERMISSIONS = {
    "read_materials", "edit_skill_source", "edit_rule_source", "run_local_tests",
    "paid_model_call", "install_personal_skill", "git_commit", "git_push",
    "publish_release", "write_production",
}
TASK_ROLES = {"extract", "cross_check", "plan", "review"}


class Invalid(Exception):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


def require(value: bool, code: str) -> None:
    if not value:
        raise Invalid(code)


def choice(value: object, allowed: set[str], code: str) -> str:
    """Validate JSON enum shape before hashing it in a set lookup."""
    require(type(value) is str and value in allowed, code)
    return value


def identifier(value: object) -> str:
    require(isinstance(value, str) and bool(ID.fullmatch(value)), "INVALID_ID")
    return value


def nonblank(value: object, code: str) -> str:
    require(isinstance(value, str) and bool(value.strip()) and len(value) <= 4096, code)
    return value


def positive(value: object, code: str, top: int | None = None) -> int:
    require(type(value) is int and value >= 1 and (top is None or value <= top), code)
    return value


def worker_index_below(index: str, count: int) -> bool:
    """Compare canonical positive decimal IDs without parsing untrusted giant integers."""
    upper = str(count)
    return len(index) < len(upper) or (len(index) == len(upper) and index < upper)


def object_(value: object, code: str) -> dict:
    require(type(value) is dict, code)
    return value


def list_(value: object, code: str) -> list:
    require(type(value) is list, code)
    return value


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def plan_digest(plan: dict) -> str:
    return digest(canonical(plan))


def nested_beyond(value: object, limit: int) -> bool:
    """True when containers nest deeper than `limit`; iterative, so depth cannot overflow it."""
    pending = [(value, 1)]
    while pending:
        item, level = pending.pop()
        if type(item) is dict:
            children = item.values()
        elif type(item) is list:
            children = item
        else:
            continue
        if level > limit:
            return True
        pending.extend((child, level + 1) for child in children)
    return False


def parse(raw: bytes) -> dict:
    def unique_pairs(pairs: list) -> dict:
        out = {}
        for k, v in pairs:
            require(k not in out, "DUPLICATE_KEY")
            out[k] = v
        return out
    try:
        doc = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs)
    except (UnicodeError, ValueError, RecursionError) as exc:
        raise Invalid("INVALID_JSON") from exc
    # Where json.loads gives up on depth is an interpreter detail (about 1000 levels on
    # 3.9, far deeper from 3.12 on), so the documented refusal is enforced explicitly.
    require(not nested_beyond(doc, MAX_NESTING), "INVALID_JSON")
    return object_(doc, "NOT_OBJECT")


def read_file(path: Path) -> tuple[dict, bytes]:
    require(path.is_file() and not path.is_symlink(), "INPUT_NOT_REGULAR")
    require(path.stat().st_size <= MAX_BYTES, "INPUT_TOO_LARGE")
    with path.open("rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
    require(len(raw) <= MAX_BYTES, "INPUT_TOO_LARGE")
    return parse(raw), raw


def recommend(mode: str, host_limit: int | None, budget_limit: int | None,
              independent_units: int) -> int:
    """All limits count the lead agent. Unknown host capability => one agent."""
    choice(mode, {"auto", "single", "parallel"}, "INVALID_AGENT_MODE")
    units = positive(independent_units, "INVALID_UNITS")
    if host_limit is not None:
        positive(host_limit, "INVALID_HOST_LIMIT")
    if budget_limit is not None:
        positive(budget_limit, "INVALID_BUDGET_LIMIT")
    # Both capabilities must be explicit before any real parallel recommendation.
    capacity = min(host_limit or 1, budget_limit or 1)
    if mode == "single" or units < 2:
        return 1
    if mode == "parallel":
        return min(capacity, 1 + units)
    if units < 3:
        return 1
    return min(capacity, 1 + min(3, (units + 1) // 3))


def validate(doc: dict) -> dict:
    require(doc.get("format") == FORMAT, "FORMAT_MISMATCH")
    revision = positive(doc.get("revision"), "INVALID_REVISION", MAX_REVISION)
    previous = doc.get("previous_sha256")
    require((revision == 1 and previous is None) or
            (revision > 1 and isinstance(previous, str) and HEX.fullmatch(previous)),
            "PREVIOUS_REVISION_REQUIRED")
    state = choice(doc.get("state"), {"draft", "confirmed"}, "INVALID_STATE")
    plan = object_(doc.get("plan"), "PLAN_REQUIRED")
    depth = choice(plan.get("depth", "standard"), DEPTHS, "INVALID_EXECUTION_DEPTH")
    output = choice(plan.get("output"), OUTPUTS, "INVALID_OUTPUT_CHOICE")
    nonblank(plan.get("objective"), "OBJECTIVE_REQUIRED")
    nonblank(plan.get("success_definition"), "SUCCESS_DEFINITION_REQUIRED")
    if plan.get("max_cost_usd") is not None:
        require(type(plan["max_cost_usd"]) in {str, int, float}, "COST_BUDGET_INVALID")
        try:
            amount = Decimal(str(plan["max_cost_usd"]))
        except InvalidOperation as exc:
            raise Invalid("COST_BUDGET_INVALID") from exc
        require(amount.is_finite() and amount >= 0, "COST_BUDGET_INVALID")
    non_goals = list_(plan.get("non_goals", []), "NON_GOALS_INVALID")
    require(all(isinstance(x, str) and x.strip() for x in non_goals),
            "NON_GOALS_INVALID")
    materials = list_(plan.get("materials"), "MATERIALS_REQUIRED")
    require(materials, "MATERIALS_EMPTY")
    source_ids = set()
    for source in materials:
        source = object_(source, "MATERIAL_INVALID")
        sid = identifier(source.get("id"))
        require(sid not in source_ids, "MATERIAL_ID_DUPLICATE")
        source_ids.add(sid)
        nonblank(source.get("locator"), "MATERIAL_LOCATOR_REQUIRED")
        snap = source.get("snapshot_sha256")
        require(snap is None or (isinstance(snap, str) and HEX.fullmatch(snap)),
                "MATERIAL_DIGEST_INVALID")
        if state == "confirmed" and output not in {"materials_only", "recommend"}:
            require(snap is not None, "CONFIRMED_MATERIAL_SNAPSHOT_REQUIRED")

    products = list_(plan.get("deliverables", []), "DELIVERABLES_INVALID")
    if output in {"materials_only", "recommend"}:
        require(not products, "PREMATURE_DELIVERABLES")
    expected = {"skill": {"skill"}, "rule": {"rule"},
                "both": {"skill", "rule"}}
    if output in expected:
        require(all(type(p) is dict and type(p.get("kind")) is str for p in products),
                "DELIVERABLE_KIND_MISMATCH")
        require({p["kind"] for p in products} == expected[output],
                "DELIVERABLE_KIND_MISMATCH")
        require(1 <= len(products) <= 20, "DELIVERABLE_COUNT")
    if state == "confirmed" and depth == "quick":
        require(all(type(p) is dict and p.get("action") == "propose"
                    for p in products), "QUICK_DEPTH_REQUIRES_PROPOSALS")
    ids = set()
    destinations = set()
    for product in products:
        product = object_(product, "DELIVERABLE_INVALID")
        pid = identifier(product.get("id"))
        require(pid not in ids, "DELIVERABLE_ID_DUPLICATE")
        ids.add(pid)
        kind = choice(product.get("kind"), KINDS, "INVALID_DELIVERABLE_KIND")
        action = choice(product.get("action"), MODES, "INVALID_DELIVERABLE_ACTION")
        nonblank(product.get("purpose"), "DELIVERABLE_PURPOSE_REQUIRED")
        target = object_(product.get("target"), "TARGET_REQUIRED")
        destination = target.get("destination")
        if action != "propose":
            nonblank(destination, "TARGET_LOCATION_REQUIRED")
        else:
            require(destination is None or isinstance(destination, str),
                    "TARGET_LOCATION_INVALID")
        if destination is not None:
            require("\\" not in destination and "\x00" not in destination and
                    not destination.startswith(("http:", "https:")),
                    "TARGET_LOCATION_INVALID")
            canonical_destination = posixpath.normpath(destination)
            require(canonical_destination not in destinations and
                    canonical_destination not in {".", ".."} and
                    not canonical_destination.startswith("../"),
                    "DELIVERABLE_TARGET_COLLISION")
            destinations.add(canonical_destination)
        if action == "update" and state == "confirmed":
            before = target.get("before_sha256")
            require(type(before) is str and HEX.fullmatch(before),
                    "TARGET_BEFORE_DIGEST_REQUIRED")
        if kind == "skill":
            require(target.get("surface") == "skill_source", "SKILL_TARGET_SURFACE")
            choice(product.get("style"), STYLES, "SKILL_STYLE_REQUIRED")
            if action != "propose":
                nonblank(product.get("trigger"), "SKILL_TRIGGER_REQUIRED")
                nonblank(product.get("expected_result"), "SKILL_EXPECTED_RESULT_REQUIRED")
        else:
            require(product.get("style") is None, "RULE_HAS_SKILL_STYLE")
            surface = target.get("surface")
            choice(surface, RULE_SURFACES, "RULE_TARGET_SURFACE")
            if surface == "host_global_rule":
                nonblank(target.get("host"), "GLOBAL_HOST_REQUIRED")
                require(target.get("scope_layer") is None, "GLOBAL_SCOPE_MIXUP")
            elif surface == "knowledge_rule":
                require(action == "propose", "KNOWLEDGE_WRITER_BYPASS")
                choice(target.get("scope_layer"), {"project", "global", "cohort"},
                       "KNOWLEDGE_SCOPE_REQUIRED")
                if target.get("scope_layer") != "global":
                    nonblank(target.get("scope_id"), "KNOWLEDGE_SCOPE_ID_REQUIRED")
            else:
                require(target.get("scope_layer") is None, "PROJECT_RULE_SCOPE_MIXUP")
    acceptance = list_(plan.get("acceptance"), "ACCEPTANCE_REQUIRED")
    require(all(isinstance(x, str) and x.strip() for x in acceptance),
            "ACCEPTANCE_INVALID")
    if state == "confirmed" and output not in {"materials_only", "recommend"}:
        require(acceptance, "ACCEPTANCE_EMPTY")
    constraints = list_(plan.get("constraints", []), "CONSTRAINTS_INVALID")
    require(all(isinstance(x, str) and x.strip() for x in constraints), "CONSTRAINTS_INVALID")
    perms = list_(plan.get("requested_permissions", []), "PERMISSIONS_INVALID")
    require(all(type(p) is str and p in PERMISSIONS for p in perms) and
            len(perms) == len(set(perms)), "PERMISSIONS_INVALID")
    if state == "confirmed" and depth == "quick":
        require(not set(perms).intersection({"edit_skill_source", "edit_rule_source",
                                             "install_personal_skill", "write_production",
                                             "publish_release"}), "QUICK_DEPTH_WRITE_CONFLICT")

    agents = object_(plan.get("agents"), "AGENT_PLAN_REQUIRED")
    mode = agents.get("mode")
    units = positive(agents.get("independent_units"), "INVALID_UNITS")
    cap = agents.get("host_max_agents")
    budget = agents.get("budget_max_agents")
    recommended = recommend(mode, cap, budget, units)
    chosen = positive(agents.get("chosen_agents"), "AGENT_COUNT_REQUIRED")
    upper = min(cap or 1, budget or (units + 1), units + 1)
    require(chosen <= upper, "AGENT_COUNT_EXCEEDS_CAPACITY")
    if state == "confirmed" and mode == "parallel":
        require(cap is not None and budget is not None and chosen >= 2,
                "PARALLEL_REQUIRES_EXPLICIT_CAPACITY_AND_BUDGET")
    if state == "confirmed" and chosen > 1:
        require(cap is not None and budget is not None,
                "PARALLEL_REQUIRES_EXPLICIT_CAPACITY_AND_BUDGET")
    if mode == "single":
        require(chosen == 1, "SINGLE_AGENT_REQUIRED")
    if chosen != recommended:
        nonblank(agents.get("override_reason"), "AGENT_OVERRIDE_REASON_REQUIRED")
    work_units = list_(agents.get("work_units", []), "WORK_UNITS_INVALID")
    if state == "confirmed":
        require(len(work_units) == units, "WORK_UNIT_COUNT_MISMATCH")
    unit_ids = set()
    for task in work_units:
        task = object_(task, "WORK_UNIT_INVALID")
        wid = identifier(task.get("id"))
        require(wid not in unit_ids, "WORK_UNIT_ID_DUPLICATE")
        unit_ids.add(wid)
        nonblank(task.get("objective"), "WORK_UNIT_OBJECTIVE_REQUIRED")
        refs = list_(task.get("material_ids"), "WORK_UNIT_MATERIALS_INVALID")
        require(bool(refs) and all(type(x) is str and x in source_ids for x in refs),
                "WORK_UNIT_UNKNOWN_MATERIAL")
    routing = object_(agents.get("model_routing", {}), "MODEL_ROUTING_INVALID")
    for worker, cfg in routing.items():
        number = re.fullmatch(r"worker-([1-9][0-9]*)", worker) if type(worker) is str else None
        require(worker == "lead" or (number is not None and worker_index_below(number[1], chosen)),
                "MODEL_ROUTING_WORKER_INVALID")
        cfg = object_(cfg, "MODEL_ROUTING_INVALID")
        nonblank(cfg.get("model"), "MODEL_ROUTING_MODEL_REQUIRED")
        if cfg.get("max_context_tokens") is not None:
            positive(cfg["max_context_tokens"], "MODEL_CONTEXT_INVALID", 10000000)
    assignments = list_(agents.get("assignments", []), "ASSIGNMENTS_INVALID")
    assigned = set()
    assigned_units = set()
    for assignment in assignments:
        assignment = object_(assignment, "ASSIGNMENT_INVALID")
        choice(assignment.get("role"), TASK_ROLES, "ASSIGNMENT_ROLE_INVALID")
        worker = assignment.get("worker")
        require(isinstance(worker, str) and re.fullmatch(r"worker-[1-9][0-9]*", worker),
                "ASSIGNMENT_WORKER_INVALID")
        n = worker.split("-")[1]
        require(worker_index_below(n, chosen), "ASSIGNMENT_WORKER_OUT_OF_RANGE")
        require(n not in assigned, "DUPLICATE_WORKER_ASSIGNMENT")
        assigned.add(n)
        srcs = list_(assignment.get("material_ids"), "ASSIGNMENT_MATERIALS_INVALID")
        require(bool(srcs) and all(type(x) is str and x in source_ids for x in srcs),
                "ASSIGNMENT_UNKNOWN_MATERIAL")
        unit = identifier(assignment.get("work_unit_id"))
        require(unit in unit_ids, "ASSIGNMENT_UNKNOWN_UNIT")
        unit_source_ids = next(set(x["material_ids"]) for x in work_units if x["id"] == unit)
        require(set(srcs) <= unit_source_ids, "ASSIGNMENT_OUTSIDE_WORK_UNIT_SOURCES")
        require(unit not in assigned_units, "WORK_UNIT_MULTIPLE_OWNERS")
        assigned_units.add(unit)
    if state == "confirmed":
        # Every assigned index is already unique and in [1, chosen); comparing
        # cardinality proves completeness without expanding caller-declared counts.
        require(len(assigned) == chosen - 1, "WORKER_ASSIGNMENTS_INCOMPLETE")
        require(output != "recommend", "OUTPUT_NOT_RESOLVED")
        if output == "materials_only":
            require(not any(p in {"edit_skill_source", "edit_rule_source",
                                  "write_production"} for p in perms), "MATERIAL_ONLY_WRITE_CONFLICT")
        confirmation = object_(doc.get("confirmation"), "USER_CONFIRMATION_REQUIRED")
        nonblank(confirmation.get("user_message_ref"), "USER_MESSAGE_REF_REQUIRED")
        nonblank(confirmation.get("summary"), "CONFIRMATION_SUMMARY_REQUIRED")
        require(confirmation.get("plan_sha256") == plan_digest(plan),
                "CONFIRMATION_PLAN_DRIFT")
    else:
        require(doc.get("confirmation") is None, "DRAFT_CANNOT_CLAIM_CONFIRMATION")

    return {"status": "ADVISORY_CONFIRMED_REFERENCE_UNVERIFIED" if state == "confirmed"
            else "DRAFT", "revision": revision, "plan_sha256": plan_digest(plan),
            "output": output, "deliverables": len(products), "materials": len(materials),
            "recommended_agents": recommended, "chosen_agents": chosen,
            "confirmation_is_authority": False,
            "host_worker_execution": "NOT_RUN",
            "note": "Record is not G1 approval, real host attestation, permission grant, or a worker dispatch"}


def _record_path(round_path: Path, revision: int) -> Path:
    return round_path / ("task-brief.v%d.json" % revision)


def _history(round_path: Path) -> tuple[int, str | None, dict | None, dict | None, set[str]]:
    require(round_path.is_dir() and not round_path.is_symlink(), "ROUND_DIR_REQUIRED")
    revisions = {}
    for child in round_path.iterdir():
        m = FILE.fullmatch(child.name)
        if m:
            require(len(m[1]) <= len(str(MAX_REVISION)), "REVISION_NAME_INVALID")
            number = int(m.group(1))
            require(number <= MAX_REVISION, "REVISION_NAME_INVALID")
            require(number not in revisions, "REVISION_NAME_CONFLICT")
            revisions[number] = child
    if not revisions:
        return 0, None, None, None, set()
    # Sequence work scales with the records actually present, never with an
    # untrusted filename's declared revision number.
    require(sorted(revisions) == list(range(1, len(revisions) + 1)), "REVISION_GAP")
    previous = None
    current_doc = None
    last_confirmed = None
    all_confirmation_refs = set()
    for n in sorted(revisions):
        current_doc, raw = read_file(revisions[n])
        require(current_doc.get("revision") == n and
                current_doc.get("previous_sha256") == previous,
                "REVISION_CHAIN_BROKEN")
        validate(current_doc)
        if current_doc["state"] == "confirmed":
            last_confirmed = current_doc
            all_confirmation_refs.add(current_doc["confirmation"]["user_message_ref"])
        previous = digest(raw)
    return max(revisions), previous, current_doc, last_confirmed, all_confirmation_refs


def inspect(round_path: Path) -> dict:
    n, previous, last, _, _confirmations = _history(round_path)
    return {"check": "task_brief", "status": "EMPTY" if n == 0 else "PASS",
            "revisions": n, "latest_sha256": previous,
            "latest": validate(last) if last else None,
            "confirmation_is_authority": False}


def prepare(round_path: Path, doc: dict, raw: bytes | None = None) -> dict:
    """Validate next revision without writing. Host owns create-only persistence."""
    summary = validate(doc)
    n, prev_hash, prev_doc, last_confirmed, confirmed_refs = _history(round_path)
    require(doc["revision"] == n + 1 and doc["previous_sha256"] == prev_hash,
            "STALE_OR_SKIPPED_REVISION")
    if last_confirmed is not None and doc["state"] == "confirmed" and\
            doc["plan"] != last_confirmed["plan"]:
        require(doc["confirmation"]["user_message_ref"] not in confirmed_refs,
                "CONFIRMATION_REUSED")
    if prev_doc is not None and doc["state"] == "draft":
        require(doc["confirmation"] is None, "CONFIRMATION_REUSED")
    payload = raw if raw is not None else (
        json.dumps(doc, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    require(len(payload) <= MAX_BYTES, "INPUT_TOO_LARGE")
    require(parse(payload) == doc, "PREPARED_BYTES_DIFFER_FROM_DOCUMENT")
    target = _record_path(round_path, n + 1)
    require(not target.exists() and not target.is_symlink(), "REVISION_ALREADY_EXISTS")
    return {"check": "task_brief", "status": "PREPARED_NOT_WRITTEN",
            "file": target.name, "revision": n + 1,
            "sha256": digest(payload), "details": summary,
            "host_must_create_exclusively": True,
            "confirmation_is_authority": False}



def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Read-only task brief validation; explicit round record")
    sub = ap.add_subparsers(dest="action", required=True)
    c = sub.add_parser("check", help="Validate a prepared task-brief JSON, no writes")
    c.add_argument("--input", required=True)
    a = sub.add_parser("inspect", help="Inspect immutable revisions in an existing round")
    a.add_argument("--round", required=True)
    r = sub.add_parser("prepare", help="Read-only check of next record; host must create file")
    r.add_argument("--round", required=True)
    r.add_argument("--input", required=True)
    s = sub.add_parser("recommend", help="Compute only a host-cap-limited agent count")
    s.add_argument("--mode", choices=("auto", "single", "parallel"), default="auto")
    s.add_argument("--units", required=True, type=int)
    s.add_argument("--host-max", type=int)
    s.add_argument("--budget-max", type=int)
    args = ap.parse_args(argv)
    try:
        if args.action == "recommend":
            count = recommend(args.mode, args.host_max, args.budget_max, args.units)
            output = {"check": "task_brief", "status": "ADVISORY_ONLY",
                      "chosen_agents": count, "lead_agents": 1,
                      "subagents": count - 1, "host_worker_execution": "NOT_RUN",
                      "note": "Counts are inclusive of the lead agent; no workers spawned"}
        elif args.action == "inspect":
            output = inspect(Path(args.round))
        else:
            source, raw = read_file(Path(args.input))
            output = ({"check": "task_brief", **validate(source)}
                      if args.action == "check"
                      else prepare(Path(args.round), source, raw))
        print(json.dumps(output, ensure_ascii=False, sort_keys=True))
        return 0
    except (Invalid, OSError, ValueError, TypeError) as exc:
        code = exc.code if isinstance(exc, Invalid) else "IO_OR_TYPE_ERROR"
        print(json.dumps({"check": "task_brief", "status": "FAIL",
                          "error": code}, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
