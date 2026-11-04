#!/usr/bin/env python3
"""S17 -- kd_lifecycle: the knowledge body is allowed to SHRINK, and only in ways that undo.

Contract row (`12-SKILL-DESIGN-BRIEF.md:125`, S17 `kd_lifecycle`)
  inputs   计数器事件流 + 状态机配置
  outputs  状态迁移 + 审计行 + archive（非删除）
  exit     0；2 = 计数器缺「事件→写入者→消费者」任一段 ⇒ 禁进判据
  clusters CM-57 `zero-use-not-stale-never-delete` (CORE) · CM-55/CM-56 (SUPPORTING, O10)
  schema   SC05 `schemas/lifecycle-record.schema.json` (S17 checks lifecycle semantics; S12 is the durable writer; S09/S18 consume)
  stages   步 21、23 / pipeline 行 14 · 阶段 5「验证、检索、生命周期」

Authority: `.distill/round-2/07-LIFECYCLE-POLICY.md` §1 (6 storage states, `07:9-36`),
§2 A1..A8 (the 8 verbs, `07:40-130`), §3.1-3.6 (`07:150-200`) and
`.distill/round-2/05-DATA-MODEL.md` §3 (`05:75-98`, 15 entry columns + 1 config item),
§4 M4/M7/M9/M10 (`05:108-114`), §5.4 (`05:192-220` counter admission),
§5.6 (`05:225-240` revocable deletion bit).

What this module is NOT
  * not a deleter. `archive` is the destructive ceiling (`07:152`, `12:50` N3) and this file holds
    no unlink/remove/rmtree/move of an authoritative record; `delete()` raises, always. Deletion
    ELIGIBILITY is the revocable bit `tombstoned_at` (`07:159`, `05:225`), never an action here.
  * not a second ledger writer. It emits SC07-shaped rows and appends only through
    `kd_provenance.append_ledger` (the sanctioned writer) to a caller-supplied path; it never
    derives a store's own ledger path for itself -- see `append_events` / PENDING_CONSUMER.
  * not an owner of the store layout (S08), of the gate (S09/S10) or of durable records (S12).
  * not a source of new states or new numbers: the state enum, the column list, the counter list
    and the grace config are read out of SC05 AT CALL TIME (`load_record_schema`), so editing the
    schema bites this module on the next call instead of drifting.

python3 stdlib only.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PACKAGE_DIR = os.path.abspath(os.path.join(HERE, os.pardir))
SCHEMAS_DIR = os.path.join(PACKAGE_DIR, "schemas")
# RH-P0-02: this runtime module no longer hardcodes a monorepo-relative path to tests/. The
# counter-admission TEST segment is a build-time/CI proof (§6); CI passes an explicit --tests-root.
sys.path.insert(0, HERE)

import kd_provenance as prov            # noqa: E402  append_ledger: the one sanctioned ledger writer
import kd_store_layout as layout        # noqa: E402  S08 owns every store path; read-only here
import kd_validate as validate          # noqa: E402  S09 owns schema resolution + the gate

# --------------------------------------------------------------------------- exit codes
EXIT_OK = 0
EXIT_USAGE = 1
EXIT_COUNTER_NOT_ADMITTED = 2      # contract: a touched counter lacks 事件/写入者/消费者 => 禁进判据
EXIT_POLICY_REFUSAL = 3            # illegal transition, delete attempt, exemption, ceiling
EXIT_SCHEMA_VIOLATION = 4          # SC05/SC07 shape does not hold
EXIT_NOT_LANDED = 5                # a needed consumer/carrier of another agent has not landed

RECORD_SCHEMA_KIND = "lifecycle-record"           # SC05
LEDGER_SCHEMA_KIND = "lifecycle-event-ledger"     # SC07, on disk since W1-C
PATTERN_SCHEMA_KIND = "pattern"                   # SC03, read at call time only for M7 attribution

#: how many entry columns Round 2 admitted (`05:98` 原子列核算: 16 表行 = 15 条目列 + 1 配置项).
#: Kept as a number because it IS the contract row's wording (`SC05 ... 15 个条目列`); it is
#: compared against the schema file's own property list, never against a Python field list.
EXPECTED_ENTRY_COLUMNS = 15
EXPECTED_STATES = 6               # `07:9` §1 title + `07:36` 状态守恒声明
EXPECTED_CONFIG_ITEMS = 1         # `05:114` M10: exactly one configuration item


# --------------------------------------------------------------------- schema read AT CALL TIME
class LifecycleRefusal(Exception):
    """A policy refusal with a code the CLI can turn into an exit code."""

    def __init__(self, code: str, message: str, exit_code: int = EXIT_POLICY_REFUSAL):
        super().__init__(message)
        self.code = code
        self.exit_code = exit_code
        self.message = message


def load_record_schema(schemas_dir: str = SCHEMAS_DIR) -> dict:
    """SC05 is the authority for the field set; S09's loader resolves the path at call time and
    audits the whole keyword tree, so a stale or uninterpretable schema fails loudly (exit 3/2)."""
    return validate.load_schema(RECORD_SCHEMA_KIND, schemas_dir)


def load_ledger_schema(schemas_dir: str = SCHEMAS_DIR) -> dict:
    return validate.load_schema(LEDGER_SCHEMA_KIND, schemas_dir)


def entry_columns(schemas_dir: str = SCHEMAS_DIR) -> list:
    return sorted(load_record_schema(schemas_dir).get("properties", {}))


def state_enum(schemas_dir: str = SCHEMAS_DIR) -> list:
    return list(load_record_schema(schemas_dir)["properties"]["lifecycle_state"]["enum"])


def counter_columns(schemas_dir: str = SCHEMAS_DIR) -> list:
    """The counter columns, derived from the schema instead of copied: an SC05 property is a
    counter exactly when it is a nullable non-negative integer (05 §5.4 (3) requires that
    从未测得 and 0 be distinguishable, so every counter Round 2 admitted is `integer|null`)."""
    props = load_record_schema(schemas_dir)["properties"]
    out = []
    for name, spec in props.items():
        if not isinstance(spec, dict):
            continue
        want = spec.get("type")
        wants = want if isinstance(want, list) else [want]
        if "integer" in wants and "null" in wants and spec.get("minimum") == 0:
            out.append(name)
    return sorted(out)


def grace_config_item(schemas_dir: str = SCHEMAS_DIR) -> dict:
    """The one admitted configuration item, read from SC05's `$defs.lifecycle_config`."""
    doc = load_record_schema(schemas_dir)
    cfg = doc.get("$defs", {}).get("lifecycle_config", {})
    props = cfg.get("properties", {})
    return {"keys": sorted(props), "deletion_grace_days": props.get("deletion_grace_days", {})}


def deletion_grace_days(schemas_dir: str = SCHEMAS_DIR):
    """Round 2 left the VALUE unadjudicated, so it stays UNKNOWN here.

    # IMPLEMENTATION_GAP: `deletion_grace_days` is quoted as 参照值 180 (`07:87` A5 ①, from
    # `15:retention-decay-formula` hard_delete_after_days) but .distill/round-3/DEFERRED-PARAMETERS.yaml
    # DEFERRED-3 (DD-4) fixes the conservative temporary behaviour as「破坏性上限固定为可逆 archive，
    # 不启用自动 TTL 硬删」, so S17 refuses to pick a number. / DEFERRED id DEFERRED-3
    """
    spec = grace_config_item(schemas_dir).get("deletion_grace_days", {})
    allowed = spec.get("enum")
    if allowed != [None]:
        raise LifecycleRefusal(
            "DEFERRED_VALUE_ADOPTED",
            "SC05 admits a concrete deletion_grace_days value; DEFERRED-3 is not closed, so no "
            f"number may be used as a decision input (schema enum {allowed!r})",
            EXIT_POLICY_REFUSAL)
    return "UNKNOWN"


def check_field_set(schemas_dir: str = SCHEMAS_DIR) -> dict:
    """Mechanical conservation of Round 2's field-set decision (`05:98`, `07:36`)."""
    cols = entry_columns(schemas_dir)
    states = state_enum(schemas_dir)
    cfg = grace_config_item(schemas_dir)
    doc = load_record_schema(schemas_dir)
    findings = []
    if len(cols) != EXPECTED_ENTRY_COLUMNS:
        findings.append({"code": "COLUMN_COUNT",
                         "message": f"{len(cols)} entry columns, contract says {EXPECTED_ENTRY_COLUMNS} "
                                    f"(05:98)"})
    if len(states) != EXPECTED_STATES:
        findings.append({"code": "STATE_COUNT",
                         "message": f"{len(states)} storage states, contract says {EXPECTED_STATES} "
                                    f"(07:9, 07:36)"})
    for forbidden in ("stale", "tombstone", "probation", "dormant", "deleted", "hard-deleted"):
        if forbidden in states:
            findings.append({"code": "FORBIDDEN_STATE",
                             "message": f"{forbidden!r} is not a storage state (07 §1.1, 07:36)"})
    if cfg["keys"] != ["deletion_grace_days"]:
        findings.append({"code": "CONFIG_DRIFT",
                         "message": f"admitted config items are {cfg['keys']}, M10 admits exactly one "
                                    f"(05:114)"})
    # M7: the three carriers never share a column. adherence_rate is derived, so it must be absent
    # from every persisted contract; the Pattern counts must not leak into the lifecycle record.
    if "adherence_rate" in doc.get("properties", {}):
        findings.append({"code": "M7_VIOLATION",
                         "message": "adherence_rate must be computed at read time, not stored (M7)"})
    for leak in ("support_count", "distinct_occurrence_count", "contradiction_count"):
        if leak in cols:
            findings.append({"code": "M7_VIOLATION",
                             "message": f"{leak} is a Pattern-layer carrier, not a lifecycle column (M7)"})
    return {"valid": not findings, "columns": cols, "states": states,
            "counters": counter_columns(schemas_dir), "config": cfg, "findings": findings}


# --------------------------------------------------------------------- the 6 states and their edges
#: `07:21-26` §1 table, 进出转换 column, verbatim per row. `(from, to)` -> (edge id, cause, cite)
TRANSITIONS = {
    ("candidate", "active"):   ("accept", "人审 accept 且同事务落盘（candidate→active 的唯一通道）", "07:21"),
    ("candidate", "rejected"): ("reject", "人审 reject", "07:21"),
    ("candidate", "failed"):   ("error", "执行出错", "07:21"),
    ("active", "superseded"):  ("SUPERSEDE", "SUPERSEDE → superseded", "07:22"),
    ("active", "archived"):    ("ARCHIVE", "ARCHIVE 门 → archived（自动路径的破坏上限）", "07:22"),
    ("active", "active"):      ("MERGE", "MERGE 作为幸存伞形 → active（内容前进，同一状态）", "07:22"),
    ("active", "rejected"):    ("reject", "人审 reject", "07:22"),
    # a tombstone is NOT a state: `07:23` keeps the row inside superseded and writes the column
    ("superseded", "superseded"): ("revive", "同 path 重新写入 → 普通链成员，门票清除", "07:23"),
    ("archived", "active"):    ("restore", "restore → active；再次活动 → active（reactivated 语义）", "07:24"),
    ("rejected", "candidate"): ("new_evidence", "新的真实证据 → candidate（无新证据不得再提）", "07:25"),
    ("failed", "rejected"):    ("give_up", "人判定不重试 → rejected", "07:26"),
}

#: `07:21` 丢弃 → 无副作用退出: no state, no ledger row, no byte written.
NON_EFFECT_OUTCOMES = frozenset({"drop"})

#: `07:26` failed 的「重试成功 → 按动作的终态」is action-dependent, so it is resolved through the
#: post-state table below rather than being flattened into a stored edge.
RETRY_EDGE_CITE = "07:26"


# --------------------------------------------------------------------- the 8 verbs
#: `07:40-130` §2 A1..A8. Post-states are 07's 后置状态 rows; `None` means "no state change"
#: (A6 REINFORCE 不产生新行、不改状态; A7 DECAY 只改派生分数/权重，不是权威态).
ACTIONS = ("ADD", "MERGE", "UPDATE", "SUPERSEDE", "DELETE", "REINFORCE", "DECAY", "ARCHIVE")
# 2026-10-07: user-approved committed-history inverse. Not a new storage state,
# not an automatic ninth policy verb, and not crash recovery or physical deletion.
TRANSACTION_ACTIONS = ACTIONS + ("RESTORE",)
#: `07:131` §2.1: MOVE and AUTOMATE are 受限特例 of UPDATE / ARCHIVE and are NOT a 9th/10th action.
NOT_ACTIONS = ("MOVE", "AUTOMATE")

ACTION_POST_STATE = {
    "ADD": "active",          # 07:42 A1: candidate → 人审 accept 后 active
    "MERGE": "superseded",    # 07:53 A2: sibling → superseded + archived(带 absorbed_into)
    "UPDATE": "active",       # 07:65 A3: active（同 id，版本前进）
    "SUPERSEDE": "superseded",  # 07:76 A4
    "DELETE": None,           # 07:87 A5: hard-deleted 是行消失，非状态；S17 不可达
    "REINFORCE": None,        # 07:98 A6
    "DECAY": None,            # 07:109 A7
    "ARCHIVE": "archived",    # 07:120 A8
}
ACTION_REVERSIBLE = {          # 07 §2 可逆性 rows
    "ADD": True, "MERGE": True, "UPDATE": True, "SUPERSEDE": True,
    "DELETE": False, "REINFORCE": True, "DECAY": True, "ARCHIVE": True,
}
#: `07:87` A5 前置条件⑥ + `07:152` §3.1: gc 是唯一物理删除入口，任何自动路径不可达 unlink.
HUMAN_ONLY_ACTIONS = ("DELETE",)


def transition_is_legal(frm: str, to: str, edge: str | None = None) -> bool:
    """`07:21-26`. `edge` naming an action additionally allows A6/A7's no-state-change and the
    failed-retry edge resolved through ACTION_POST_STATE."""
    if edge is None:
        return (frm, to) in TRANSITIONS
    if edge == "RESTORE":
        return frm in ("active", "archived") and to == "active"
    if edge not in ACTIONS or edge == "DELETE":
        return False
    if edge in ("REINFORCE", "DECAY"):
        return frm == to and frm in state_enum()
    if edge == "MERGE" and frm == to == "active":
        return True  # surviving record is updated; absorbed siblings become superseded
    expected = ACTION_POST_STATE[edge]
    if to != expected:
        return False
    if edge == "ADD" and frm not in ("candidate", "failed"):
        return False
    if edge in ("UPDATE", "SUPERSEDE", "MERGE") and frm not in ("active", "failed"):
        return False
    return (frm, to) in TRANSITIONS or frm == "failed"


def assert_transition(frm: str, to: str, action: str | None = None) -> dict:
    """Fail-closed transition check with the citation of the edge that allows it (or of the
    rejection). States outside SC05's enum are refused before any edge lookup."""
    if action in NOT_ACTIONS:
        raise LifecycleRefusal(
            "NOT_AN_ACTION",
            f"{action} is not a lifecycle action: 07 §2.1 folds MOVE/AUTOMATE into UPDATE/ARCHIVE "
            "as 受限特例, they add no state semantics", EXIT_POLICY_REFUSAL)
    if action is not None and action not in TRANSACTION_ACTIONS:
        raise LifecycleRefusal("UNKNOWN_ACTION", f"{action!r} is not a transaction action {TRANSACTION_ACTIONS}",
                               EXIT_POLICY_REFUSAL)
    states = state_enum()
    for label, value in (("from_state", frm), ("to_state", to)):
        if value not in states:
            raise LifecycleRefusal(
                "STATE_NOT_ADJUDICATED",
                f"{label}={value!r} is outside SC05's 6 storage states {states}; 07:36 状态守恒声明 "
                "-- 任何未列出的状态一律不得新增，新增即需重新裁决", EXIT_POLICY_REFUSAL)
    if transition_is_legal(frm, to, action):
        edge = TRANSITIONS.get((frm, to))
        return {"legal": True, "from": frm, "to": to,
                "edge": edge[0] if edge else f"retry:{action}",
                "cite": edge[2] if edge else RETRY_EDGE_CITE}
    allowed = sorted(t for (f, t) in TRANSITIONS if f == frm)
    raise LifecycleRefusal(
        "ILLEGAL_TRANSITION",
        f"{frm} -> {to} (action={action}) is not an edge of 07 §1; {frm} may reach {allowed}. "
        "Not inventing a transition: a state edge Round 2 did not adjudicate needs a ruling, "
        "not a helper. / IMPLEMENTATION_GAP: active->failed and superseded->archived have no "
        "adjudicated edge (07:22, 07:23) / DEFERRED id none registered (newly surfaced by W3-B)",
        EXIT_POLICY_REFUSAL)


# --------------------------------------------------------------------- counter admission (exit 2)
#: `05:192-220` §5.4: 任何进入决策的计数器必须有可指认的写入者与测试；缺 (1) 或 (2) → 禁止进入任何
#: 决策，且不得作为「证据缺失」的旁证。The headline counterexample the shape must not repeat is
#: `08` pro-workflow `times_applied` (05:204-207): DEFAULT 0 + an increment function nobody calls,
#: while sorting, sampling, eval weights, template rendering and staleness hints all read it.
#:
#: Each triple is (event source -> writer symbol -> consumer symbol). `NOT_LANDED_YET:<who>` marks
#: a segment no landed code holds; those are reported, not skipped.
COUNTER_TRIPLES = {
    "use_count": {
        "layer": "evidence_event",
        "event": "NOT_LANDED_YET:S02-host-consumption-anchor",
        "event_note": "真实消费事件锚点未接线：O04 `CM-07 lifecycle-hook-capture-trigger` 是 "
                      "optional adapter，DD-4 DEFERRED-2 尚未证明 Knowledge Compiler 有等价真实消费事件接口",
        "writer": "kd_lifecycle::reinforce",
        "consumer": "kd_lifecycle::adherence_rate",
        "test": "test_w3b_lifecycle.py::test_reinforce_advances_use_and_clears_ticket",
    },
    "view_count": {
        "layer": "evidence_event",
        "event": "NOT_LANDED_YET:S02-display-anchor",
        "event_note": "读/展示事件锚点，`05:85`",
        "writer": "kd_lifecycle::reinforce",
        # `07:177` §3.5: view > 0 仅作为试用期结束评估中的保留依据，不计入分子、不加分；该评估路径由 S16 负责
        "consumer": "NOT_LANDED_YET:S16-graduation-review",
        "consumer_note": "S16 尚未接入基于 view_count 的试用期结束评估；kd_eval_score 已提供独立评测工具",
        "test": "test_w3b_lifecycle.py::test_view_count_never_enters_the_numerator",
    },
    "opportunity_anchor": {
        "layer": "evidence_anchor",
        "event": "kd_lifecycle::adopt",
        "event_note": "条目首次纳管时播种（`05:86`）",
        "writer": "kd_lifecycle::adopt",
        "consumer": "kd_lifecycle::opportunities",
        "test": "test_w3b_lifecycle.py::test_adopt_seeds_anchor_and_first_seen",
    },
    "layer_request_count": {
        "layer": "layer_request",
        "event": "NOT_LANDED_YET:S02-host-request-anchor",
        "event_note": "每层一个请求计数器；参照形状 `06:lib/counters.py::request_count,bump_request`"
                      "（`05:87`）",
        "writer": "NOT_LANDED_YET:S17-host-adapter",
        "writer_note": "O10 `CM-55/CM-56` 宿主埋点：仅当事件→写入者→消费者→测试闭环可指认时启用，"
                       "否则分母退化并产出恒 0 假数据",
        "consumer": "kd_lifecycle::opportunities",
        "test": "test_w3b_lifecycle.py::test_layer_request_count_absent_refuses_as_decision_input",
    },
}

#: `05:111` M7: three different carriers, 禁止互通、禁止相加.
CARRIER_LAYERS = {
    "evidence_event": "Evidence-layer event counts (use/view/patch) -- 05 §3 rows 3-4, 05 §6 Knowledge Artifact",
    "evidence_anchor": "Evidence-layer watermark anchors (opportunity_anchor) -- 05 §3 row 5",
    "layer_request": "Layer request counters (the denominator) -- 05 §3 row 6",
    "pattern": "Pattern-layer counts (support_count / distinct_occurrence_count) -- 晋升门唯一读取",
    "artifact_rate": "Artifact-layer adherence_rate -- 淘汰判据，只算不存",
}
PATTERN_COUNTERS = ("support_count", "distinct_occurrence_count", "near_duplicate_count",
                    "contradiction_count", "last_attempted_count")


def _top_level_symbols(path: str) -> set:
    """Names actually defined in a module file, read at call time (so a deleted writer cannot
    keep claiming to exist)."""
    if not os.path.isfile(path):
        return set()
    with open(path, encoding="utf-8") as fh:                     # read-only
        src = fh.read()
    try:
        tree = ast.parse(src, filename=path)
    except SyntaxError:
        return set()
    names = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    names.add(tgt.id)
    return names


def resolve_symbol(ref: str, tests_root: str = None) -> tuple:
    """Resolve `module::symbol` (a scripts/ module) or `test_file.py::test_name` against the real
    files. Returns (ok, detail).

    RH-P0-02: a runtime script must not know where the monorepo's tests/ live. A scripts-module
    holder resolves against THIS package's scripts/ (always shipped). A `*.py` test holder is a
    BUILD-TIME/CI concern (§6): it resolves only against an explicitly provided `tests_root`; with
    none (an installed Skill) it reports BUILD_TIME_ONLY instead of reaching up ../../tests."""
    if not ref or ref.startswith("NOT_LANDED_YET"):
        return False, ref
    if "::" not in ref:
        return False, f"{ref!r} names no symbol"
    holder, symbol = ref.split("::", 1)
    if holder.endswith(".py"):
        if not tests_root:
            return False, ("BUILD_TIME_ONLY: the counter-admission test segment is verified by "
                           "Repo-A CI against an explicit --tests-root, not by an installed Skill "
                           "(RH-P0-02, §6); no tests root was provided")
        path = os.path.join(tests_root, holder)
    else:
        path = os.path.join(HERE, f"{holder}.py")
    defined = _top_level_symbols(path)
    if symbol not in defined:
        return False, f"{path} defines no top-level {symbol!r}"
    return True, path


def admission_report(tests_root: str = None) -> list:
    """Every counter this module touches, with each of the three runtime segments (事件/写入者/
    消费者) verified against the shipped scripts/. A missing segment is a finding; findings are what
    makes S17 exit 2. The fourth `test` segment is a BUILD-TIME/CI proof (§6): it is resolved live
    only when `tests_root` is given; in an installed runtime it is build-attested and does not gate."""
    touched = set(counter_columns())
    rows = []
    for column in sorted(touched):
        triple = COUNTER_TRIPLES.get(column)
        if triple is None:
            rows.append({"counter": column, "admitted": False,
                         "missing": ["triple"],
                         "detail": "SC05 admits a counter column this module cannot account for"})
            continue
        missing, detail = [], {}
        for segment in ("event", "writer", "consumer", "test"):
            if segment == "test" and not tests_root:
                detail[segment] = "BUILD_TIME_ATTESTED (Repo-A CI verifies with --tests-root)"
                continue
            ok, why = resolve_symbol(triple[segment], tests_root=tests_root)
            detail[segment] = triple[segment] if ok else why
            if not ok:
                missing.append(segment)
        rows.append({"counter": column, "layer": triple["layer"],
                     "admitted": not missing, "missing": missing,
                     "event": triple["event"], "writer": triple["writer"],
                     "consumer": triple["consumer"], "test": triple["test"],
                     "detail": detail})
    return rows


def assert_admitted_for_decision(counters, purpose: str, tests_root: str = None) -> dict:
    """`禁进判据`: if any counter a decision reads is not admitted, refuse with exit 2 rather than
    letting a permanently-0 or never-measured column decide 去留, ordering, weights or hints."""
    rows = {row["counter"]: row for row in admission_report(tests_root=tests_root)}
    refused = []
    for name in counters:
        row = rows.get(name)
        if row is None:
            raise LifecycleRefusal(
                "COUNTER_NOT_IN_SCHEMA",
                f"{name} is not an SC05 counter column (SC05 counters: {sorted(rows)})",
                EXIT_SCHEMA_VIOLATION)
        if not row["admitted"]:
            refused.append({"counter": name, "missing": row["missing"],
                            "segments": {k: row["detail"][k] for k in row["missing"]}})
    if refused:
        raise LifecycleRefusal(
            "COUNTER_NOT_ADMITTED",
            f"{purpose} is barred from decision input: {json.dumps(refused, ensure_ascii=False)}. "
            "05 §5.4: 缺 (1) 写入者 或 (2) 测试 → 该字段禁止进入任何决策，且不得作为「证据缺失」的"
            "旁证. This is S17's contractual exit 2, and it is a REFUSAL, not a silent skip -- the "
            "08 pro-workflow `times_applied` shape (05:204-207) is what this check exists to catch.",
            EXIT_COUNTER_NOT_ADMITTED)
    return {"purpose": purpose, "counters": list(counters), "admitted": True}


def carrier_of(counter: str, schemas_dir: str = SCHEMAS_DIR) -> str:
    """Which M7 carrier a counter belongs to, resolved from the schema files rather than a table."""
    if counter == "adherence_rate":
        return "artifact_rate"
    if counter in entry_columns(schemas_dir):
        return COUNTER_TRIPLES.get(counter, {}).get("layer", "evidence_event")
    try:
        pattern_props = load_schema_props(PATTERN_SCHEMA_KIND, schemas_dir)
    except validate.SchemaProblem:
        pattern_props = {}
    if counter in pattern_props:
        return "pattern"
    return "unknown"


def load_schema_props(kind: str, schemas_dir: str = SCHEMAS_DIR) -> dict:
    return validate.load_schema(kind, schemas_dir).get("properties", {})


def sum_counters(values: dict) -> dict:
    """M7 (`05:111`): the three carriers may not be interchanged or summed. `adherence_rate` is a
    ratio, so it may not even be an addend."""
    layers = set()
    for name in values:
        if name == "adherence_rate":
            raise LifecycleRefusal("M7_VIOLATION",
                                   "adherence_rate is a rate, not a count: adding it to a count "
                                   "invents a number with no writer (05 §4 M7)", EXIT_POLICY_REFUSAL)
        layers.add(carrier_of(name))
    if "unknown" in layers:
        raise LifecycleRefusal("UNKNOWN_CARRIER",
                               f"cannot attribute {sorted(values)} to an M7 carrier; refusing to "
                               "count it", EXIT_SCHEMA_VIOLATION)
    if len(layers) > 1:
        raise LifecycleRefusal(
            "M7_VIOLATION",
            f"counters from different M7 carriers {sorted(layers)} must never be summed or "
            "exchanged (05:111): Evidence 事件计数 / Pattern support_count / Artifact "
            "adherence_rate are three carriers, and 混用一个计数器会让「被打开过」直接凑出晋升",
            EXIT_POLICY_REFUSAL)
    return {"layer": next(iter(layers)), "total": sum(int(v) for v in values.values())}


# --------------------------------------------------------------------- derived views (never stored)
def opportunities(record: dict) -> int:
    """`07:176` §3.5: opportunities = max(0, watermark - anchor). Null inputs are reported as
    从未测得 first (that is a record defect, `05:196` (3)), then both counters must clear admission
    -- a present-but-unowned counter is exactly the `times_applied` shape and may not feed a
    criterion."""
    request = record.get("layer_request_count")
    anchor = record.get("opportunity_anchor")
    for name, value in (("layer_request_count", request), ("opportunity_anchor", anchor)):
        if value is None:
            raise LifecycleRefusal(
                "DENOMINATOR_UNMEASURED",
                f"{name} is 从未测得 (null); 05 §5.4 (3) forbids rendering a missing value as real "
                "data, so opportunities cannot be computed", EXIT_COUNTER_NOT_ADMITTED)
    assert_admitted_for_decision(["layer_request_count", "opportunity_anchor"],
                                 "opportunities() denominator")
    return max(0, int(request) - int(anchor))


def adherence_rate(record: dict):
    """Artifact-layer rate (`05:111` M7 carrier 3, `07:176` the single main criterion
    rate = use / opportunities). Computed at read time, never persisted (SC05 has no column for
    it, and `check_field_set` fails if one appears)."""
    use = record.get("use_count")
    if use is None:
        return "UNKNOWN"
    opp = opportunities(record)
    if opp == 0:
        return "NO_OPPORTUNITY"        # probation-shaped:召回如常、不淘汰（07 §1.1 / 07:176）
    return round(int(use) / opp, 6)


def derive_staleness(record: dict) -> dict:
    """The READ-ONLY stale view (`07:32` §1.1: 只存计数器 + 时间戳 + 门票列，stale 每次读时计算，
    永不成为权威) and CM-57's core rule (`07:177` §3.5: 零使用 → 判为【证据缺失】，不归档，且必须
    回滚误标).

    It returns a label plus the reason; the label is a REINFORCE / re-validation CLUE, explicitly
    not a sufficient condition for ARCHIVE (`07:32`)."""
    use = record.get("use_count")
    view = record.get("view_count")
    zero_use = (use in (None, 0)) and (view in (None, 0))
    never_active = record.get("last_activity_at") is None
    if zero_use:
        return {"label": "insufficient_evidence", "stale": False, "archivable": False,
                "reason": "零使用（use==0 且 view==0，或从未测得）按 07 §3.5 判为证据缺失，"
                          "不是陈旧、不是归档理由（CM-57 zero-use-not-stale-never-delete）；"
                          "14 把 stale 物化的代价必须由 reanchor 回滚（07:32）",
                "cite": "07:177, 07:32"}
    if never_active:
        return {"label": "never_active", "stale": False, "archivable": False,
                "reason": "last_activity_at 为 null 且排除 created_at（05 §3 row 2）时，"
                          "「从未活动」必须与「陈旧」可分辨，否则新条目按创建时间被老化",
                "cite": "05:82"}
    # A real wall-clock cutoff exists as a floor only, and its value is deferred:
    # IMPLEMENTATION_GAP: stale 的墙钟兜底阈值数值未定案 / DEFERRED id DEFERRED-3
    return {"label": "activity_observed", "stale": None, "archivable": False,
            "reason": "the criterion is the opportunity denominator, not elapsed time "
                      "(07 §3.5); the wall-clock floor value is DEFERRED-3, so this view reports "
                      "no stale verdict",
            "cite": "07:185"}


def deletion_eligibility(record: dict) -> dict:
    """Deletion eligibility is a REVOCABLE STATE BIT, never an action (`07:159` §3.2, `05:225`
    §5.6). This function reads the bit; it does not remove anything, and nothing in this module
    can. A rewrite of the same path or a further real use clears `tombstoned_at` (revive below)."""
    ticket = record.get("tombstoned_at")
    if ticket is None:
        return {"eligible": False, "state": record.get("lifecycle_state"),
                "reason": "无门票（tombstoned_at=null）→ 无删除资格：普通 supersession 行不写该列，"
                          "所以 hard-delete pass 天然碰不到它们（07:78 A4 ③, 07:168 §3.3 ②）",
                "cite": "07:78"}
    grace = deletion_grace_days()
    return {"eligible": None, "state": record.get("lifecycle_state"), "ticket": ticket,
            "grace_days": grace,
            "reason": "门票非空只是资格的一半：还要 门票年龄 ≥ deletion_grace_days 且人工 gc 执行 "
                      "(07:87 A5 ①⑥). grace_days 值 DEFERRED-3 未定案 → 本报告为 UNKNOWN；"
                      "且 S17 无 unlink 路径，本函数不产生任何文件动作",
            "cite": "07:87, 05:114"}


# --------------------------------------------------------------------- the 8 verbs, in code
def blank_record(created_by: str, *, now: str | None = None, state: str = "candidate") -> dict:
    """A record with all 15 SC05 columns present. Counters start null = 从未测得, which is what
    keeps 05 §5.4 (3) true on day one: an unmeasured counter is never rendered as a zero."""
    return {
        "lifecycle_state": state,
        "last_activity_at": None,
        "use_count": None,
        "view_count": None,
        "opportunity_anchor": None,
        "layer_request_count": None,
        "created_by": created_by,
        "tombstoned_at": None,
        "absorbed_into": None,
        "first_seen_at": now,
        "pinned": False,
        "referenced_by_external": [],
        "decay_type": "unknown",
        "last_validated_at": None,
        "validation_state": "pending",
    }


def adopt(record: dict, *, request_watermark: int, now: str) -> dict:
    """A1's first half + the seeding machinery (`05:86` opportunity_anchor 首次纳管时播种,
    `05:93` first_seen_at 播种并推迟一个周期, `07:120` A8 ④ 播种时钟 ④: 首个 tick 绝不动库).

    Returns a NEW record (the state bit itself does not move: ADD lands `candidate` and only the
    human-reviewed, same-transaction accept reaches `active`)."""
    if not isinstance(request_watermark, int) or request_watermark < 0:
        raise LifecycleRefusal("BAD_WATERMARK",
                               f"request watermark must be a non-negative int, got "
                               f"{request_watermark!r} (07 A7 ⑤ clamps threshold floors: a value "
                               "below 1 lets a cutoff land after now and migrate the whole tree)",
                               EXIT_POLICY_REFUSAL)
    out = dict(record)
    out["opportunity_anchor"] = int(request_watermark)
    if out.get("first_seen_at") is None:
        out["first_seen_at"] = now
    return out


def committed_record(previous, *, action, to_state, created_by, at,
                     absorbed_into=None, evaluation_verified=False):
    """Pure SC05 builder used by S12 after full Eval and human admission.

    S17 owns state semantics; S12 alone persists this record with SC04 and SC07.
    There is no guessed request watermark, event count, activity time or deletion
    ticket. RESTORE preserves current counters/ownership, not old snapshot counters.
    """
    if evaluation_verified is not True:
        raise LifecycleRefusal("EVAL_NOT_VERIFIED", "full fresh Eval required", EXIT_POLICY_REFUSAL)
    if previous is None:
        if action != "ADD" or to_state != "active" or not created_by:
            raise LifecycleRefusal("LIFECYCLE_RECORD_MISSING", "only ADD may create SC05", EXIT_POLICY_REFUSAL)
        record = blank_record(created_by, now=at)
    else:
        if not validate.validate_artifact(RECORD_SCHEMA_KIND, previous)["valid"]:
            raise LifecycleRefusal("LIFECYCLE_RECORD_INVALID", "stored SC05 is invalid", EXIT_SCHEMA_VIOLATION)
        record = dict(previous)
    assert_transition(record["lifecycle_state"], to_state, action)
    if action == "ARCHIVE":
        record = archive(record, requested_by="human")["record"]
    elif action in ("ADD", "UPDATE", "SUPERSEDE", "MERGE", "RESTORE"):
        record["lifecycle_state"] = to_state
        if action == "MERGE" and to_state == "superseded":
            record["absorbed_into"] = absorbed_into
        if action == "RESTORE":
            record["absorbed_into"] = None
            record["tombstoned_at"] = None
    else:
        raise LifecycleRefusal("COUNTER_NOT_ADMITTED", "counter mutations need real event adapters", EXIT_COUNTER_NOT_ADMITTED)
    record["last_validated_at"] = at
    record["validation_state"] = "verified"
    if not validate.validate_artifact(RECORD_SCHEMA_KIND, record)["valid"]:
        raise LifecycleRefusal("LIFECYCLE_RECORD_INVALID", "assembled SC05 is invalid", EXIT_SCHEMA_VIOLATION)
    return record


def add(identity: str, created_by: str, *, now: str, human_approved: bool = False,
        request_watermark: int = 0) -> dict:
    """A1 ADD (`07:42`): born `candidate`; durable write needs 人审 accept in the same transaction,
    which is S12's `commit_batch` (and S09's gate) -- this module holds no write authority.

    A `DELETE`-shaped or `active`-shaped ADD is refused: candidate→active is the 唯一通道 and it
    requires a human (`07:21`, `07:42` ⑥)."""
    if not identity or not created_by:
        raise LifecycleRefusal("MISSING_IDENTITY",
                               "ADD needs identity + created_by: 07 A1 forbids a durable record "
                               "with created_by=null and it must fail closed like a missing one",
                               EXIT_POLICY_REFUSAL)
    rec = blank_record(created_by, now=now, state="candidate")
    rec = adopt(rec, request_watermark=request_watermark, now=now)
    outcome = {"artifact_id": identity, "record": rec, "events": [],
               "post_state": "candidate",
               "requires": "人审 accept + full Eval + three trusted receipts in S12 commit_batch; "
                           "S08 registers SC05; S17 returns a pure proposal, never persists it"}
    if human_approved:
        edge = assert_transition("candidate", "active", "ADD")
        moved = dict(rec, lifecycle_state="active")
        outcome["record"] = moved
        outcome["events"].append(make_event("ADD", "lifecycle", identity, actor="user",
                                            reason=None, detail="candidate -> active on human accept"))
        outcome["post_state"] = "active"
        outcome["edge"] = edge
    return outcome


def update(record: dict, *, mutation_kind: str, read_prior: bool, now: str,
           content_hash_before: str, content_hash_after: str, actor: str = "agent") -> dict:
    """A3 UPDATE (`07:65`). Three of its hard preconditions are mechanical here:
      ① read-before-write: an unread path is a design violation refused BEFORE the write (`07:74`);
      ② 措辞/补充可就地 update；事实本体改动必须走 SUPERSEDE (`07:67` ③);
      ③ identical content short-circuits, producing no new version (`07:78` ⑤)."""
    if not read_prior:
        raise LifecycleRefusal("READ_BEFORE_WRITE",
                               "UPDATE refused: the target path was not read first. 14's measured "
                               "cost of the missing discipline is ~142 denials + ~204 read-before-"
                               "write refusals in two days with almost no patch landing (07:74)",
                               EXIT_POLICY_REFUSAL)
    if mutation_kind == "ontology":
        raise LifecycleRefusal(
            "NEEDS_SUPERSEDE",
            "a change to the fact itself must go through SUPERSEDE, not in-place UPDATE "
            "(07:67 A3 ③): wording may move in place, the ontology may not", EXIT_POLICY_REFUSAL)
    if content_hash_before == content_hash_after:
        return {"short_circuit": True, "record": record, "events": [],
                "reason": "content_hash equal -> no new version, no fake chain link (07:78 ⑤)"}
    frm = record.get("lifecycle_state")
    edge = assert_transition(frm, frm, "UPDATE") if frm != "active" else None
    moved = dict(record, last_activity_at=now) if frm == "active" else dict(record)
    return {"short_circuit": False, "record": moved, "edge": edge, "actor": actor,
            "events": [make_event("UPDATE", "lifecycle", str(record.get("artifact_id") or ""),
                                  actor=actor, reason=None,
                                  detail=f"{content_hash_before[:8]} -> {content_hash_after[:8]}")]}


def supersede(record: dict, new_id: str, *, now: str, actor: str = "agent",
              ticket: bool = False) -> dict:
    """A4 SUPERSEDE (`07:76`) -- the only implementation of 减少而不销毁 (`07:23`).

    SUPERSEDE != DELETE, in code:
      * it writes NO deletion ticket. Only decay eviction and the reconcile-delete safety net may
        (`07:78` ③, `07:168` §3.3 ②), and S17 refuses a ticket on a plain supersession.
      * the old row stays reachable (state `superseded`, files intact) and the chain edges are
        recorded as `supersedes`/`superseded_by` in the SC07 ledger row, which is what makes the
        chain reversible and time-travellable (`07:79` 后置状态).
      * the promise is revocable; that promise must never extend to DELETE (`07:169`)."""
    if ticket:
        raise LifecycleRefusal(
            "TICKET_NOT_FROM_SUPERSEDE",
            "a plain supersession must not write tombstoned_at (07:78 A4 ③): keeping the ticket "
            "column empty is what makes the hard-delete pass structurally unable to reach ordinary "
            "chain members. Only decay eviction / the reconcile safety net write it, and both record "
            "their origin in lifecycle_event.reason (07:33, 05 §4 M4)", EXIT_POLICY_REFUSAL)
    frm = record.get("lifecycle_state")
    if new_id == record.get("artifact_id"):
        raise LifecycleRefusal("SELF_SUPERSESSION",
                               "a row may not supersede itself (07:78 A4 ② invariant)",
                               EXIT_POLICY_REFUSAL)
    edge = assert_transition(frm, "superseded", "SUPERSEDE")
    moved = dict(record, lifecycle_state="superseded", tombstoned_at=None)
    # IMPLEMENTATION_GAP: A4 ② requires `superseded_by` to imply `invalid_at`, but Round 2 put
    # neither column in SC05's 15 (`05:98`) and SC07's closed row has supersedes/superseded_by and
    # no `invalid_at` (schemas/lifecycle-event-ledger.schema.json). S17 therefore carries the chain
    # in the ledger row and refuses to invent a column; the carrier decision belongs to SC07's owner.
    ev = make_event("SUPERSEDE", "lifecycle", str(record.get("artifact_id") or new_id),
                    actor=actor, reason=None,
                    supersedes=None, superseded_by=new_id,
                    detail="old row stays reachable via the chain; no deletion ticket written")
    return {"record": moved, "edge": edge, "event": ev, "reversible": True,
            "ticket_written": False, "chain_carrier_gap": "invalid_at has no adjudicated carrier"}


def revive(record: dict, *, now: str, reason: str = "same-path rewrite",
           via: str = "rewrite") -> dict:
    """The revival path (`07:23`, `05:230` §5.6): a rewrite of the same path or a further real use
    CLEARS the ticket and keeps the chain, turning a hard-delete candidate back into a protected
    chain member. This is the whole reversibility argument, so it is a state transition with an
    audit row, not a repair tool."""
    if reason not in ("same-path rewrite", "real use"):
        raise LifecycleRefusal("BAD_REVIVAL_REASON",
                               f"reason={reason!r}: 05 §5.6 admits only 重新写入 or 再次真实使用 as "
                               "eligibility-revoking causes", EXIT_POLICY_REFUSAL)
    if record.get("tombstoned_at") is None and via == "rewrite":
        return {"record": dict(record), "events": [], "changed": False,
                "reason": "no ticket to clear; the row is already a protected chain member"}
    edge = assert_transition(record.get("lifecycle_state"), record.get("lifecycle_state"))
    moved = dict(record, tombstoned_at=None, last_activity_at=now)
    ev = make_event("SUPERSEDE", "lifecycle", str(record.get("artifact_id") or ""),
                    actor="agent", reason="reactivated",
                    detail=f"ticket cleared by {reason} (05 §5.6, 07:23)")
    return {"record": moved, "edge": edge, "events": [ev], "changed": True,
            "ticket_cleared": True}


def reinforce(record: dict, event: dict) -> dict:
    """A6 REINFORCE (`07:98`): counters and `last_activity_at` advance; NO new row, NO state
    change; the three signals stay split (`07:100` ②).

    `review 不是生命周期事件` is enforced: a review pass may not bump a recurrence counter, refresh
    a last-seen stamp or create a parallel registry (`07:100`, `05:97`)."""
    kind = event.get("kind")
    if kind in ("review", "audit", "curation_browse"):
        raise LifecycleRefusal(
            "REVIEW_IS_NOT_A_LIFECYCLE_EVENT",
            f"{kind} must not bump counters or refresh stamps (07:100 A6 ②, 05:97 row 16)",
            EXIT_POLICY_REFUSAL)
    if kind not in ("use", "view", "patch"):
        raise LifecycleRefusal("UNKNOWN_SIGNAL",
                               f"{kind!r} is not one of the three split signals use/view/patch "
                               "(05 §3 rows 3-4: patch 单独且不加分)", EXIT_POLICY_REFUSAL)
    stamp_at = event.get("at")
    out = dict(record)
    column = {"use": "use_count", "view": "view_count"}.get(kind)
    if column is None:
        # patch: 07 A6 ② gives it no numerator and SC05's 15 columns hold no patch column, so the
        # fact is recorded as an event row only -- inventing a record key would widen the field set.
        return {"record": out, "state_changed": False, "signal": kind,
                "events": [make_event("REINFORCE", "lifecycle",
                                      str(record.get("artifact_id") or ""), actor="agent",
                                      reason=None, detail="patch event: 改进标记, 不加分 (07:100 ②)")],
                "ledger": "patch is an event row, never a numerator (07:100)"}
    current = out.get(column)
    out[column] = 0 if current is None else int(current)   # 从未测得 -> first observation
    out[column] = int(out[column]) + 1
    out["last_activity_at"] = stamp_at
    events = [make_event("REINFORCE", "lifecycle", str(record.get("artifact_id") or ""),
                         actor="agent", reason=None,
                         detail=f"{column} += 1 on {kind} event")]
    result = {"record": out, "state_changed": False, "signal": kind, "events": events}
    if kind == "use" and record.get("tombstoned_at") is not None:
        # 05 §5.6: a further REAL use clears the ticket -- revival revokes deletion eligibility
        revived = dict(out, tombstoned_at=None)
        events.append(make_event("REINFORCE", "lifecycle",
                                 str(record.get("artifact_id") or ""), actor="agent",
                                 reason="reactivated",
                                 detail="real use cleared tombstoned_at (05 §5.6)"))
        result["record"] = revived
        result["ticket_cleared"] = True
    return result


def decay(record: dict, *, epsilon: float = 0.0) -> dict:
    """A7 DECAY (`07:109`): its post-state is 派生分数或权重变化（不是权威态）;越阈值只产生 stale
    派生标签与重验线索，**不直接进 archived** (`07:113`).

    Because the only criterion is the opportunity denominator (`07:176`), and that denominator
    needs `layer_request_count`, DECAY reads an unadmitted counter today -> `assert_admitted_for_decision`
    raises with S17's contractual exit 2. That refusal is the feature: it is precisely the shape
    that kept 14's wall-clock decay from being trustworthy and 08's counter from driving eviction."""
    assert_admitted_for_decision(["layer_request_count", "opportunity_anchor", "use_count"],
                                 "DECAY eviction criterion")
    view = derive_staleness(record)
    changed = abs(float(epsilon)) > 0            # only |delta| > epsilon writes back (07:111 ②)
    return {"record": dict(record), "state_changed": False, "derived": view,
            "write_back": bool(changed and view["label"] != "insufficient_evidence"),
            "clue_only": True,
            "reason": "DECAY may not move lifecycle_state; a derived label is a REINFORCE / "
                      "re-validation clue and explicitly not a sufficient condition for ARCHIVE "
                      "(07:113, 07:32)"}


def archive(record: dict, *, artifact_id: str = "", actor: str = "curator",
            requested_by: str = "automation", counters: dict | None = None,
            suspended: bool = False, exclude_faces: tuple = ("recall", "dedup")) -> dict:
    """A8 ARCHIVE (`07:120`): the DESTRUCTIVE CEILING of every automatic path -- it moves the
    record's state bit and never its bytes, so DECAY does not have to reach DELETE (`07:24`).

    Preconditions implemented: exemptions (⑦), the circuit breaker (⑧), both exclusion faces (②),
    the who+moved-why record (③), and CM-57's zero-use rule -- which is what makes the automatic
    path effectively unreachable from usage counts alone."""
    frm = record.get("lifecycle_state")
    if record.get("pinned"):
        raise LifecycleRefusal("PINNED_EXEMPT",
                               "pinned exempts every auto-transition and model review pass "
                               "(07:122 A8 ⑦, 07:154 §3.1)", EXIT_POLICY_REFUSAL)
    if record.get("referenced_by_external"):
        raise LifecycleRefusal("EXTERNAL_REFERENCE_EXEMPT",
                               "referenced_by_external is exemption axis 2 -- being referenced is "
                               "equivalent to pinned, so a low-frequency job must not be aged out "
                               "by the wall clock (05:92, 07:122 ⑦)", EXIT_POLICY_REFUSAL)
    if suspended:
        raise LifecycleRefusal("CIRCUIT_BREAKER_OPEN",
                               "paused / GRADUATION_REVIEW_SUSPENDED: archiving on zero usage "
                               "while recall checks are known to be broken conceals the failure that is "
                               "surfacing itself (07:123 A8 ⑧)", EXIT_POLICY_REFUSAL)
    if requested_by != "human":
        # CM-57 CORE: 零使用不是陈旧，永不单独构成删除/归档理由（07:177-179 §3.5）
        view = derive_staleness({**record})
        if view["label"] in ("insufficient_evidence", "never_active"):
            raise LifecycleRefusal(
                "ZERO_USE_IS_NOT_STALE",
                f"automatic ARCHIVE refused for a {view['label']} record: {view['reason']}. "
                "CM-57 zero-use-not-stale-never-delete; 01's contract line is literally 'Lack of "
                "use alone does not justify removing a rare safeguard' (07:178)",
                EXIT_POLICY_REFUSAL)
        # the surviving criterion is the opportunity denominator, so it must be admitted
        assert_admitted_for_decision(["layer_request_count", "opportunity_anchor", "use_count"],
                                     "automatic ARCHIVE gate")
        rate = adherence_rate(record)
        if rate in ("UNKNOWN", "NO_OPPORTUNITY"):
            raise LifecycleRefusal(
                "NO_ADMITTED_CRITERION",
                f"adherence_rate = {rate}: without an admitted denominator there is no criterion, "
                "and inventing one from elapsed time is the 07 §3.5 rejected shape (pure wall clock) "
                "-- 14's own implementation contains the corrective logic for that criticism",
                EXIT_POLICY_REFUSAL)
    if set(exclude_faces) != {"recall", "dedup"}:
        raise LifecycleRefusal("EXCLUSION_INCOMPLETE",
                               f"checks={sorted(exclude_faces)}: the archive predicate must apply "
                               "to BOTH recall and dedup checks, otherwise an obsolete "
                               "rule keeps participating in future dedup and 已覆盖 gets misjudged "
                               "(07:121 A8 ②, and `05` only did the recall half)",
                               EXIT_POLICY_REFUSAL)
    edge = assert_transition(frm, "archived", "ARCHIVE")
    moved = dict(record, lifecycle_state="archived")
    ev = make_event("ARCHIVE", "lifecycle", artifact_id or str(record.get("created_by")),
                    actor=actor, reason="archive",
                    detail="state bit moved; no byte operation performed; both exclusion faces set")
    return {"record": moved, "edge": edge, "event": ev, "bytes_touched": False,
            "excluded_faces": sorted(exclude_faces), "restorable": True,
            "restore": {"to": "active", "cite": "07:24"}}


def delete(*args, **kwargs):
    """A5 DELETE exists in the policy as the human-only, irreversible channel (`07:87`) and in this
    module as a REFUSAL only. There is no code path here that removes a file.

    `07:155` DD-4's own reason is the reason for the refusal: any automatic delete path lets
    memory poisoning or a captured reasoner cause irreversible loss. `kd_gate.apply_mutation`
    already refuses `to == "deleted"`; S17 opens no alternative door (`07:157` §3.1, `12:50` N3)."""
    raise LifecycleRefusal(
        "DESTRUCTIVE_CEILING",
        "DELETE is unreachable from S17: archive is the maximum destructive automatic action, "
        "gc by a human is the only physical removal and it requires tombstoned_at + grace + an "
        "explicit human flag (07:87 A5 ①④⑥, 07:152 §3.1). Deletion eligibility is the revocable "
        "bit read by deletion_eligibility(), never an action taken here.", EXIT_POLICY_REFUSAL)


def merge(*, umbrella: dict, siblings: list, destinations: set, consolidate_enabled: bool = False,
          removed: list | None = None) -> dict:
    """A2 MERGE (`07:53`) -- 减少的最强形式，也是代价最高的可逆动作（双层回滚）.

    The fail-closed checks Round 2 demanded, all mechanical:
      ① every removed sibling carries `absorbed_into` and the target exists, else the WHOLE intent
         is rejected (`07:170` §3.4, 事故 #29912);
      ③ conservation: each `removed` id lands in exactly one of consolidated | pruned, checked by
         set difference -- anything that simply disappears is a defect (`07:172`);
      ⑦ consolidate is OFF by default and must be switched on explicitly (`07:55` ⑦);
      ⑥ pinned siblings are exempt.
    """
    if not consolidate_enabled:
        raise LifecycleRefusal(
            "CONSOLIDATE_DISABLED_BY_DEFAULT",
            "MERGE/consolidate is off unless explicitly enabled: with zero model calls the worst "
            "case must be 不合并, not 错合并 (07:55 A2 ⑦, `04` C8, DD-2)", EXIT_POLICY_REFUSAL)
    removed = list(removed if removed is not None else [s.get("artifact_id") for s in siblings])
    consolidated, pruned, refused = [], [], []
    for sibling in siblings:
        sid = sibling.get("artifact_id")
        if sid not in removed:
            continue
        if sibling.get("pinned"):
            refused.append(sid)
            continue
        target = sibling.get("absorbed_into")
        if not target:
            raise LifecycleRefusal(
                "ABSORBED_INTO_MISSING",
                f"removed sibling {sid!r} carries no absorbed_into: 归档了一簇但没归并 is undetectable "
                "and exactly why the guard exists (07:54 A2 ①, #29912)", EXIT_POLICY_REFUSAL)
        if target not in destinations:
            raise LifecycleRefusal(
                "ABSORBED_TARGET_ABSENT",
                f"absorbed_into={target!r} is not an existing or newly created destination; a "
                "missing umbrella rejects the whole intent, never a partial delete (07:54 ①②)",
                EXIT_POLICY_REFUSAL)
        consolidated.append(sid)
    leftovers = sorted(set(removed) - set(consolidated) - set(pruned) - set(refused))
    if leftovers:
        raise LifecycleRefusal(
            "SET_CONSERVATION",
            f"removed ids accounted for by neither consolidated nor pruned: {leftovers} -- 任何"
            "「消失」都是缺陷 (07:172 §3.4 第二条守恒)", EXIT_POLICY_REFUSAL)
    moved_siblings, events = [], []
    for sibling in siblings:
        sid = sibling.get("artifact_id")
        if sid not in consolidated:
            continue
        edge = assert_transition(sibling.get("lifecycle_state"), "superseded", "MERGE")
        moved_siblings.append(dict(sibling, lifecycle_state="superseded"))
        events.append(make_event("MERGE", "lifecycle", sid, actor="merge", reason="absorbed",
                                 detail=f"absorbed_into={sibling.get('absorbed_into')}"))
    umb_edge = assert_transition(umbrella.get("lifecycle_state"), "active", "MERGE")
    return {"siblings": moved_siblings, "umbrella": dict(umbrella, lifecycle_state="active"),
            "events": events, "consolidated": sorted(consolidated), "pruned": sorted(pruned),
            "exempt_pinned": sorted(refused), "umbrella_edge": umb_edge,
            "rollback": "two layers required (per-change content-addressed ledger + whole-tree snapshot); "
                        "prune-only passes skip the snapshot (07:57 A2 失败回滚)"}


# --------------------------------------------------------------------- audit rows (SC07 shape)
def make_event(op: str, entity: str, entity_id: str, *, actor: str, reason, at: str | None = None,
               supersedes=None, superseded_by=None, detail: str | None = None) -> dict:
    """One SC07 row per batch operation, with `seq`/`record_locator` filled by `append_events`.

    `reason` stays inside 05 §4 M1's closed enum, and a tombstone's ORIGIN goes into it (`07:33`,
    `05:108` M4) instead of 15's two-ticket-sources-deliberately-indistinguishable design.
    `detail` is prose and never authoritative: every consumer in this module reads columns."""
    if op not in TRANSACTION_ACTIONS:
        raise LifecycleRefusal("UNKNOWN_OP", f"{op!r} is not a lifecycle transaction op",
                               EXIT_POLICY_REFUSAL)
    if entity not in ("evidence", "learning", "pattern", "artifact", "lifecycle"):
        raise LifecycleRefusal("UNKNOWN_ENTITY", f"{entity!r} is not one of 05 §1's five entities",
                               EXIT_SCHEMA_VIOLATION)
    if actor not in ("curator", "user", "merge", "agent", "human", "import", "shared"):
        raise LifecycleRefusal("UNKNOWN_ACTOR",
                               f"{actor!r} is outside SC07's actor enum (05 §4 M1 union)",
                               EXIT_SCHEMA_VIOLATION)
    return {"seq": 0, "at": at or "UNKNOWN_AT", "op": op, "actor": actor, "reason": reason,
            "entity": entity, "entity_id": entity_id or "unknown",
            "supersedes": supersedes, "superseded_by": superseded_by, "detail": detail,
            "record_locator": {"ledger": "unset", "seq": 0}}


def ledger_rows(events: list) -> list:
    """Every column a consumer needs comes out of the row's columns; `detail` is dropped from the
    decision surface on purpose (05 §2 row 8: detail 不作权威)."""
    return [{"op": e["op"], "actor": e["actor"], "reason": e["reason"],
             "entity": e["entity"], "entity_id": e["entity_id"],
             "supersedes": e["supersedes"], "superseded_by": e["superseded_by"]} for e in events]


def _existing_rows(path: str) -> list:
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8") as fh:                    # read-only
        return [json.loads(line) for line in fh if line.strip()]


def _stamp_row(row: dict) -> tuple:
    """Leave the hash to append_ledger. Project its actual bytes, without a self-referential
    placeholder that would override the kernel's freshly computed content_hash."""
    to_append = {key: value for key, value in row.items() if key != "content_hash"}
    stored = dict(to_append, content_hash=prov.content_hash(to_append))
    return to_append, stored


def append_events(events: list, ledger_path: str | None = None, *, store_dir: str | None = None,
                  at: str | None = None) -> dict:
    """The only durable effect S17 produces, and only through the sanctioned channel.

    S08 attributes SC07 and SC05 to S12. The 2026-10-07 approved contract keeps
    this Owner: lifecycle commits require full artifact intents, Eval and three
    receipts through S12. S17 refuses direct appends into an S08 store. An explicit
    ledger_path is accepted only for a staging report, never an ownership transfer.
    No standalone counter-event durable API is admitted here."""
    if store_dir is not None and ledger_path is None:
        raise LifecycleRefusal(
            "LEDGER_SLOT_NOT_TRANSFERRED",
            f"refusing to append into the store at {store_dir!r}: S08 registers "
            f"{layout.LIFECYCLE_LEDGER_FILE_REL} under the store slot owned by "
            f"{layout.OWNER_WRITE_TXN}, so S17 appending there would be a second appender on one "
            "carrier. Use the full S12 commit contract; an explicit ledger_path cannot transfer ownership.",
            EXIT_NOT_LANDED)
    if ledger_path is None:
        raise LifecycleRefusal("NO_LEDGER_TARGET",
                               "no ledger path supplied: S17 never invents a store path (S08 owns "
                               "the layout, CM-11)", EXIT_USAGE)
    try:
        layout.assert_staging_path(ledger_path)
    except layout.LayoutViolation as exc:
        raise LifecycleRefusal("LEDGER_SLOT_NOT_TRANSFERRED",
                               "explicit ledger paths cannot bypass store ownership or protected trees",
                               EXIT_NOT_LANDED) from exc
    rows = []
    projected = []
    seq = len(_existing_rows(ledger_path))
    for event in events:
        row = dict(event)
        if row["at"] == "UNKNOWN_AT":
            if at is None:
                raise LifecycleRefusal(
                    "NO_TIMESTAMP",
                    "SC07 needs one captured timestamp per batch (05 §2: 时间戳取一次); S17 will "
                    "not stamp a row with a guessed time or with a value the recorded object "
                    "自报, so the caller supplies it", EXIT_USAGE)
            row["at"] = at
        seq += 1
        row["seq"] = seq
        row["record_locator"] = {"ledger": ledger_path.replace(os.sep, "/"), "seq": seq}
        to_append, stored = _stamp_row(row)
        outcome = validate.validate_artifact(LEDGER_SCHEMA_KIND, stored, schemas_dir=SCHEMAS_DIR)
        if not outcome["valid"]:
            raise LifecycleRefusal("SC07_SHAPE",
                                   f"ledger row {seq} violates SC07: {outcome['violations']}",
                                   EXIT_SCHEMA_VIOLATION)
        rows.append(to_append)
        projected.append(stored)
    for row in rows:
        prov.append_ledger(ledger_path, row)         # the sanctioned writer (S08/S12 use the same one)
    return {"appended": len(rows), "ledger": ledger_path, "last_seq": seq,
            "projected_rows": projected,
            "authoritative_columns": ["seq", "at", "op", "actor", "reason", "entity",
                                      "entity_id", "supersedes", "superseded_by"]}


# --------------------------------------------------------------------- destructive-ceiling proof
DESTRUCTIVE_ATTRS = {"remove", "unlink", "rmdir", "removedirs", "renamedir", "truncate",
                     "rmtree", "move"}
DESTRUCTIVE_DOTS = {"os.remove", "os.unlink", "os.rmdir", "os.removedirs", "shutil.rmtree",
                    "shutil.move", "os.replace", "os.rename"}


def destructive_scan(module: str = __file__) -> dict:
    """The machine-checkable version of "S17 opens no delete path": parse THIS file and report
    every destructive call site, whatever the prose claims. Exit-0 only with zero sites."""
    with open(module, encoding="utf-8") as fh:                    # read-only
        tree = ast.parse(fh.read(), filename=module)
    sites = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        dotted = None
        if isinstance(fn, ast.Attribute):
            base = fn.value.id if isinstance(fn.value, ast.Name) else ""
            dotted = f"{base}.{fn.attr}" if base else fn.attr
            if fn.attr in DESTRUCTIVE_ATTRS or dotted in DESTRUCTIVE_DOTS:
                sites.append({"line": node.lineno, "call": dotted})
        elif isinstance(fn, ast.Name) and fn.id in {"remove", "unlink", "rmtree"}:
            sites.append({"line": node.lineno, "call": fn.id})
    return {"module": os.path.basename(module), "sites": sites, "clean": not sites}


# --------------------------------------------------------------------- CLI
class UsageError(Exception):
    pass


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise UsageError(message)


def build_parser() -> ArgumentParser:
    p = ArgumentParser(prog="kd_lifecycle.py",
                       description="S17 kd_lifecycle -- the 6-state lifecycle machine, the "
                                   "counter-admission gate (exit 2 = a counter missing 事件/写入者/"
                                   "消费者, so it may not feed any criterion) and the archive-as-"
                                   "ceiling refusal. Authority: 07-LIFECYCLE-POLICY.md §1/§2/§3, "
                                   "05-DATA-MODEL.md §3/§4/§5.4/§5.6. Writes nothing on its own: "
                                   "SC05 is the field set, S12 is the durable writer, "
                                   "kd_provenance.append_ledger is the only ledger channel.",
                       epilog="exit codes: 0 ok · 1 usage · 2 counter not admitted (禁进判据) · "
                              "3 policy refusal (illegal transition / delete attempt / exemption) · "
                              "4 SC05-SC07 shape violation · 5 needed carrier of another agent not "
                              "landed. Reads only; no store is created or modified.",
                       formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--check-schema", action="store_true",
                   help="report SC05's 15 entry columns, 6 storage states, counter columns and the "
                        "single admitted config item, all read from the schema file at call time")
    p.add_argument("--admission", action="store_true",
                   help="print every touched counter's 事件→写入者→消费者(+测试) triple; exit 2 if a "
                        "segment is missing")
    p.add_argument("--ceiling", action="store_true",
                   help="print the destructive-ceiling proof: the AST scan for delete-shaped calls "
                        "plus the delete()/DELETE refusal, and deletion_eligibility()'s UNKNOWN grace")
    p.add_argument("--zero-use", action="store_true",
                   help="print CM-57's derived staleness view for a never-used record")
    p.add_argument("--json", action="store_true", help="machine-readable output on stdout")
    p.add_argument("--tests-root", default=None,
                   help="BUILD-TIME/CI only (RH-P0-02, §6): explicit tests/ dir used to verify the "
                        "counter-admission test segment live. An installed Skill supplies none, so "
                        "the test segment is build-attested and never resolved against a monorepo path.")
    return p


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not any([args.check_schema, args.admission, args.ceiling, args.zero_use]):
        parser.print_help()
        return EXIT_OK
    report = {}
    exit_code = EXIT_OK
    try:
        if args.check_schema:
            report["field_set"] = check_field_set()
            if not report["field_set"]["valid"]:
                exit_code = EXIT_SCHEMA_VIOLATION
        if args.admission:
            rows = admission_report(tests_root=args.tests_root)
            report["admission"] = rows
            report["carriers"] = CARRIER_LAYERS
            if any(not row["admitted"] for row in rows):
                exit_code = EXIT_COUNTER_NOT_ADMITTED
        if args.ceiling:
            report["destructive_scan"] = destructive_scan()
            report["delete_call"] = {"raises": None}
            try:
                delete()
            except LifecycleRefusal as exc:
                report["delete_call"] = {"raises": exc.code, "message": exc.message}
            report["grace_days"] = deletion_grace_days()
            report["eligibility_example"] = deletion_eligibility(
                blank_record("compiler", now=None))
        if args.zero_use:
            report["zero_use_view"] = derive_staleness(blank_record("compiler"))
    except LifecycleRefusal as exc:
        report["refusal"] = {"code": exc.code, "message": exc.message}
        exit_code = exc.exit_code
    except validate.SchemaProblem as exc:
        report["schema_problem"] = str(exc)
        exit_code = EXIT_SCHEMA_VIOLATION
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1, sort_keys=True))
    else:
        for section, payload in report.items():
            print(f"{section}: {json.dumps(payload, ensure_ascii=False, sort_keys=True)}")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
