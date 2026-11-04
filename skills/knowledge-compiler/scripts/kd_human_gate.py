#!/usr/bin/env python3
"""G1 -- the only human position in the pipeline (`#22` 人类批准, `12:137`).

This module is data and predicates, not a runtime: it records an approval as a row, decides
whether a human is required at all, and hands the approved bundle to S12. It writes nothing
and imports no write path, so it cannot become a second authority for what was approved
(`06:247` N27 五要素 4 is honoured the same way W2-C honoured it in `kd_quarantine.apply_bundle`:
the module holds NO approval state of its own -- the approval arrives as an argument, and the
durable record of it is one `lifecycle_event` row written by S12/S17).

Classification authority (verbatim Round 2 wording, cited per row below):
  * `06:212` N23 [DET] 该动作是否触碰常驻层（AGENTS.md / CLAUDE.md / rules / skills / 项目文档）？
        no -> N24, yes -> N25
  * `06:214-215` N24 [DET] 「可无人在场」的三条件门（全部成立才放行）：
        (a) 机械可判定 (b) 可逆 (c) 幂等，且不越 ownership 边界（只动 self-authored 条目）
  * `06:221` 物理删除一律不得进 R0 分支（N25 R2）
  * `06:225` R1 常驻层写入（Project Rule / Global Rule / Skill）→ 人审，且逐条 verdict（不糊批）
  * `06:226` R2 不可逆（任何 delete、以及会销毁内容的 merge）→ 人审 + 确认 flag 是契约本身
  * `06:247` N27 approve 与 apply 同事务：任一步失败则整批不落，不留 created_by=null 的半记录
  * `04:54` row 8 human 列 = 需要：durable 写的批准门（CM-35）；`04:61` row 15 = 授权门唯一持有者
  * `04:60` row 14 human 列 = 无（`pinned` 由人设置，转换本身自动）

These rows classify historical action risk; they do not admit a durable write. In particular,
R0's no-human classification is retained for comparison, but its write route is currently
DEFERRED/REFUSE at S10 N24. R1/R2 still require their existing human decisions and the complete
S10/S12 checks. Neither `classify_action` nor `describe_gate` grants write permission.

Stdlib only. No model client, no write primitive, no `kd_write_txn` import.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import kd_provenance as prov                 # noqa: E402  wave 0 kernel (frozen, imported)
import kd_provenance_stamp as stamp          # noqa: E402  S13: the digest authority

# --------------------------------------------------------------------- vocabulary
#: Same actor vocabulary W2-C froze in `kd_quarantine.HUMAN_DECISION_ACTORS`, reused rather
#: than re-invented so "human" means one thing across the package (`12:137` G1 是唯一人类门).
HUMAN_ACTORS = ("human", "user")
#: Anything that can PRODUCE a proposal can never approve one (`04:17` I-2).
NON_HUMAN_ACTORS = ("model", "compiler", "automation", "system", "agent", "import", "curator")

TIER_R0 = "R0"      # 历史无人风险分类；当前 N24 拒绝正式写入
TIER_R1 = "R1"      # 人审，逐条 verdict（常驻层写入）
TIER_R2 = "R2"      # 人审 + 确认 flag 是契约本身（不可逆 / 销毁内容）

CLASSIFICATION_SCOPE = "RISK_ONLY_NOT_WRITE_PERMISSION"
WRITE_ADMISSION_BY_TIER = {
    TIER_R0: "DEFERRED_REFUSED",
    TIER_R1: "REQUIRES_S10_S12",
    TIER_R2: "REQUIRES_S10_S12",
}

RESIDENT_LAYER_MARKERS = ("AGENTS.md", "CLAUDE.md", "rules/", "skills/", "project docs")


class GateRefusal(Exception):
    """A fail-closed refusal. Carries a code so a caller can react without parsing prose."""

    def __init__(self, code, message, detail=None):
        Exception.__init__(self, message)
        self.code, self.message, self.detail = code, message, (detail or {})


# --------------------------------------------------------------------- classification as DATA
#: One row per action class, each carrying the four N24 booleans plus its citation. The `tier`
#: column is NOT trusted: `_derive_tier` recomputes it from the flags at every call and
#: `_check_table` proves the table and the rule agree, so the classification stays one
#: authoritative rule set instead of 14 separate hunches.
ACTION_CLASS_ROWS = (
    {"action": "normalise-exact-duplicate", "touches_resident_layer": False,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R0,
     "cites": ["`06:214-215` N24 三条件门",
               "`06:216-218` 11:governed-sleep-proposal-ledger T0 确定性段直接写盘，全为可逆归一化"
               "（_merge_exact_duplicates / _merge_near_duplicate_groups / _normalise_dates）"]},
    {"action": "normalise-dates", "touches_resident_layer": False,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R0, "cites": ["`06:216-218` 11:governed-sleep-proposal-ledger T0 可逆归一化"
                                "（_normalise_dates）", "`06:214-215` N24 三条件门"]},
    {"action": "pattern-count-only", "touches_resident_layer": False,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R0,
     "cites": ["`06:260` L-PATTERN 只累计数、只留身份，不产提案、不落常驻层，是否需要人工=否"]},
    {"action": "nothing-silent", "touches_resident_layer": False,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R0, "cites": ["`06:261` L-NOTHING 是否需要人工=否"]},
    {"action": "nothing-with-ledger", "touches_resident_layer": False,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R0,
     "cites": ["`06:262` L-NOTHING+账 必须写 lifecycle_event，不得沉默消失；是否需要人工=否"]},
    {"action": "lifecycle-counter-or-state-transition", "touches_resident_layer": False,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R0,
     "cites": ["`04:60` row 14 Lifecycle：Deterministic 唯一，Human 列=无（转换本身自动）"]},
    {"action": "archive-superseded-entry", "touches_resident_layer": False,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R0,
     "cites": ["`06:270` L-ARCHIVE 是否需要人工=否（可逆），永不 delete",
               "`07` §3.1 archive 是破坏性上限"]},
    {"action": "archive-resident-entry", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R1, "cites": ["2026-10-07 approved S12 lifecycle contract: retire resident entry"]},
    {"action": "archive-resident-global", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": True, "irreversible": False, "destroys_content": False,
     "tier": TIER_R1, "requires_second_approver": True,
     "cites": ["2026-10-07 approved S12 lifecycle contract; global still needs two humans"]},
    {"action": "restore-committed-entry", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": False,
     "crosses_ownership": False, "irreversible": False, "destroys_content": True,
     "tier": TIER_R2, "requires_confirmation_flag": True,
     "cites": ["2026-10-07 approved inverse: replaces current content, retains immutable history"]},
    {"action": "restore-committed-global", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": False,
     "crosses_ownership": True, "irreversible": False, "destroys_content": True,
     "tier": TIER_R2, "requires_confirmation_flag": True, "requires_second_approver": True,
     "cites": ["2026-10-07 approved inverse; R2 confirmation and two independent humans"]},
    {"action": "write-lint", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R1, "cites": ["`06:264` L-LINT 需要人工=R1"]},
    {"action": "write-test", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R1, "cites": ["`06:265` L-TEST 需要人工=R1"]},
    {"action": "write-script", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R1, "cites": ["`06:263` L-SCRIPT 需要人工=R1"]},
    {"action": "write-eval", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R1, "cites": ["`06:266` L-EVAL 需要人工=R1"]},
    {"action": "write-skill", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R1, "cites": ["`06:267` L-SKILL 需要人工=R1（删除性归并升 R2）"]},
    {"action": "write-rule-project", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R1, "cites": ["`06:268` L-RULE-PROJECT 需要人工=R1"]},
    {"action": "write-rule-global", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": True, "irreversible": False, "destroys_content": False,
     "tier": TIER_R1, "requires_second_approver": True,
     "cites": ["`06:269` L-RULE-GLOBAL 需要人工=R1 + 显式第二人门（该档由 DD-1 外推，`06` 自标 [I]，"
               "本实现按已裁的 R1 处理并要求第二人，不把它当已证常量）"]},
    {"action": "merge-destroying-content", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": False, "idempotent": False,
     "crosses_ownership": True, "irreversible": True, "destroys_content": True,
     "tier": TIER_R2, "requires_confirmation_flag": True,
     "cites": ["`06:226` R2 不可逆（任何 delete、以及会销毁内容的 merge）→ 人审 + 确认 flag 是契约本身",
               "`06:267` L-SKILL 删除性归并升 R2"]},
    {"action": "merge-destroying-content-global", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": False, "idempotent": False,
     "crosses_ownership": True, "irreversible": True, "destroys_content": True,
     "tier": TIER_R2, "requires_confirmation_flag": True, "requires_second_approver": True,
     "cites": ["`06:226` content-destroying MERGE keeps R2 confirmation",
               "`06:269` global resident mutation keeps the explicit second human gate"]},
    {"action": "physical-delete", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": False, "idempotent": True,
     "crosses_ownership": True, "irreversible": True, "destroys_content": True,
     "tier": TIER_R2, "requires_confirmation_flag": True, "reachable_from_write_path": False,
     "cites": ["`06:221` 物理删除一律不得进 R0 分支",
               "`04:61` row 15 Deletion：human 是授权门唯一持有者，执行与回滚归确定性",
               "`07` §3.1 archive 是破坏性上限：kd_gate.apply_mutation 对 to == 'deleted' 直接 raise"]},
    {"action": "set-pinned", "touches_resident_layer": True,
     "mechanically_decidable": True, "reversible": True, "idempotent": True,
     "crosses_ownership": False, "irreversible": False, "destroys_content": False,
     "tier": TIER_R1,
     "cites": ["`04:60` row 14 human 列原文：无（`pinned` 由人设置，转换本身自动）-- 转换可自动，"
               "pinned 这个决定本身只有人能设"]},
)

#: The model-step payload shapes G1 must refuse to treat as consent, whatever a host does.
FORGED_APPROVAL_KEYS = ("human_approved", "approved", "approved_by", "auto_approved",
                        "waive_gate", "skip_human_gate")


def _derive_tier(flags: dict) -> str:
    """N23/N24/N25 as one computable rule, in the order Round 2 wrote them."""
    if flags.get("irreversible") or flags.get("destroys_content"):
        return TIER_R2                                   # `06:226`
    if flags.get("touches_resident_layer"):
        return TIER_R1                                   # `06:212` yes -> N25
    if (flags.get("mechanically_decidable") and flags.get("reversible")
            and flags.get("idempotent") and not flags.get("crosses_ownership")):
        return TIER_R0                                   # `06:214-215` all three hold
    # An action that cannot show all three conditions is not classified as free: `06:221`
    # closes the R0 branch to anything unproven, and a guess here is the rubber-stamp failure
    # mode `06:233` measured in three separate reference repos.
    return TIER_R1


def _index() -> dict:
    return {row["action"]: row for row in ACTION_CLASS_ROWS}


def _check_table() -> list:
    """Table-vs-rule drift check. A row whose stated tier is not what the rule derives is a
    second authority for the same decision, so it is reported, not silently tolerated."""
    drift = []
    for row in ACTION_CLASS_ROWS:
        derived = _derive_tier(row)
        if derived != row["tier"]:
            drift.append({"action": row["action"], "stated": row["tier"], "derived": derived})
    return drift


TABLE_DRIFT = _check_table()


def classify_action(action, *, target: str = "", flags: dict = None) -> dict:
    """N23 + N24 risk classification with citations, not write admission.

    `action` is an action-class name (`ACTION_CLASS_ROWS`) or an intent dict carrying the
    flags itself; `target` is the path/kind the action lands on -- a resident-layer marker in
    it forces N23 to yes even for an action class listed as R0, because N23 asks about the
    layer, not about the verb (`06:212`). `requires_human` describes that risk tier only:
    R0 remains historically human-free but is currently refused by N24, while R1/R2 must
    still pass the complete S10/S12 commit checks.
    """
    if TABLE_DRIFT:
        raise GateRefusal("CLASSIFICATION_DRIFT",
                          f"G1 refuses to classify while its table and its rule disagree: "
                          f"{TABLE_DRIFT}")
    row = None
    supplied = dict(flags or {})
    name = action
    if isinstance(action, dict):
        supplied = {**{k: v for k, v in action.items()
                       if k in ("touches_resident_layer", "mechanically_decidable", "reversible",
                                "idempotent", "crosses_ownership", "irreversible",
                                "destroys_content")}, **supplied}
        name = action.get("action") or action.get("op")
    if isinstance(name, str):
        row = _index().get(name)

    if row is not None:
        merged = {k: row[k] for k in ("touches_resident_layer", "mechanically_decidable",
                                      "reversible", "idempotent", "crosses_ownership",
                                      "irreversible", "destroys_content")}
        merged.update(supplied)
        cites, known = list(row["cites"]), True
    else:
        merged = {"touches_resident_layer": False, "mechanically_decidable": False,
                  "reversible": False, "idempotent": False, "crosses_ownership": False,
                  "irreversible": False, "destroys_content": False}
        merged.update(supplied)
        cites = ["`06:212-215` (no table row for this action: fail-closed, an unclassified "
                 "action is never treated as the no-human branch)"]
        known = False

    forced_by_target = [marker for marker in RESIDENT_LAYER_MARKERS if marker in str(target)]
    if forced_by_target:
        merged["touches_resident_layer"] = True
        cites = cites + [f"`06:212` N23 yes: target {target!r} carries resident-layer marker(s) "
                         f"{forced_by_target}"]

    tier = _derive_tier(merged)
    return {
        "action": name,
        "classified": known,
        "tier": tier,
        "classification_scope": CLASSIFICATION_SCOPE,
        "write_admission": WRITE_ADMISSION_BY_TIER[tier],
        "requires_human": tier in (TIER_R1, TIER_R2),
        "n23_touches_resident_layer": bool(merged["touches_resident_layer"]),
        "n24_conditions": {
            "mechanically_decidable": bool(merged["mechanically_decidable"]),
            "reversible": bool(merged["reversible"]),
            "idempotent": bool(merged["idempotent"]),
            "within_ownership": not bool(merged["crosses_ownership"]),
        },
        "route": ("N24 -> DEFERRED/REFUSE（R0 历史分类未获准正式写入）" if tier == TIER_R0
                  else f"N25 [HUMAN] {tier}"
                       + (" + 确认 flag 是契约本身" if tier == TIER_R2 else "")),
        "requires_confirmation_flag": bool(row and row.get("requires_confirmation_flag"))
                                      or tier == TIER_R2,
        "requires_second_approver": bool(row and row.get("requires_second_approver")),
        "basis": cites,
        "no_human_reason": (None if tier != TIER_R0 else
                            "仅历史风险分类：机械可判定 + 可逆 + 幂等 + 不越 ownership，"
                            "且未触碰常驻层（`06:214-215`）；当前 N24 未准入，"
                            "不得据此无人提交正式知识"),
        "target": str(target or ""),
    }


# --------------------------------------------------------------------- the digest of what was approved
def approved_digest(proposal) -> str:
    """Digest of EXACTLY what was approved, computed by S13's `subject_digest` so the number
    means the same thing here as it does on the write path (provenance-bearing and
    transaction-bookkeeping keys stripped, `05-DATA-MODEL.md:47`)."""
    if not isinstance(proposal, dict) or not proposal:
        raise GateRefusal("DIGEST_LESS_PROPOSAL",
                          "G1 cannot approve an absent or empty proposal: an approval that pins "
                          "no content is consent to nothing (`06:247` 五要素 2/4 -- the artifact "
                          "hash is what makes an approval checkable at apply time)")
    body = {k: v for k, v in proposal.items() if k not in FORGED_APPROVAL_KEYS}
    if not any(k in body for k in ("payload", "step", "artifact_id", "record", "content",
                                   "intent", "text")):
        raise GateRefusal("DIGEST_LESS_PROPOSAL",
                          "G1 cannot approve a proposal with no approvable content: refusing "
                          "rather than recording a digest over an empty body")
    try:
        return stamp.subject_digest(body)
    except (TypeError, ValueError, RecursionError) as exc:
        raise GateRefusal("PROPOSAL_MALFORMED", "approval proposal must be finite, bounded JSON") from exc


def intent_digest(record_digest: str, target: str = "") -> str:
    """§12 / RH-P0-08: bind the storage TARGET to the approved record digest, so an approval for a
    record cannot be replayed onto a different write target. `op`/`to_state` stay constrained by
    kd_gate.apply_mutation's state-machine boundary and the tier check; this closes the target axis
    of the Commit Authorization Bundle. G1 computes it at approval time and S12 recomputes it at
    verify time from the same two inputs, so a post-approval change to the record OR the target is
    an AUTHORIZATION_DIGEST_MISMATCH and writes nothing.
    """
    return stamp.subject_digest({"record_digest": record_digest, "target": target or ""})


def binding_digest(binding: dict) -> str:
    """Authorization binding does NOT strip provenance, mutation or target fields."""
    try:
        raw = json.dumps(binding, sort_keys=True, ensure_ascii=False, separators=(",", ":"),
                         allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise GateRefusal("BINDING_MALFORMED", "authorization binding must be finite JSON") from exc
    return hashlib.sha256(raw).hexdigest()


def verify_host_approval(proof, binding: dict, verifier) -> dict:
    """Authenticate consent through an injected host capability, never through a label.

    The host owns its confirmation/signature channel and supplies verifier(proof, binding).
    This module cannot invent that authority. No CLI/file names a Python verifier. An absent
    verifier fails closed; a JSON object claiming verified=true is still just the proof input.
    The verifier returns {verified: true, binding_digest, approvers: {artifact_id: [principal]}};
    each principal has a stable id and kind='human'. Global actions need distinct identities.
    """
    if not callable(verifier):
        raise GateRefusal("TRUSTED_APPROVAL_SOURCE_MISSING", "the host must supply an authenticated approval verifier")
    try:
        result = verifier(copy.deepcopy(proof), copy.deepcopy(binding))
    except Exception as exc:
        raise GateRefusal("APPROVAL_AUTHENTICATION_FAILED", "host approval verification failed") from exc
    if not isinstance(result, dict) or result.get("verified") is not True \
            or result.get("binding_digest") != binding_digest(binding):
        raise GateRefusal("APPROVAL_AUTHENTICATION_FAILED", "approval is not authenticated for this exact binding")
    approvers = result.get("approvers")
    required = {item["artifact_id"]: item["required_approvers"] for item in binding["items"]}
    if not isinstance(approvers, dict) or set(approvers) != set(required):
        raise GateRefusal("APPROVAL_COVERAGE_MISMATCH", "authenticated consent must cover exactly this batch")
    principals = {}
    for aid, minimum in required.items():
        rows = approvers[aid]
        if not isinstance(rows, list) or len(rows) < minimum or any(
                not isinstance(row, dict) or row.get("kind") != "human"
                or not isinstance(row.get("id"), str) or not row["id"].strip()
                or row["id"] != row["id"].strip() for row in rows):
            raise GateRefusal("NOT_A_HUMAN_DECISION", "authenticated human principals are missing")
        ids = [row["id"] for row in rows]
        if len(set(ids)) != len(ids):
            raise GateRefusal("SECOND_APPROVER_MISSING", "duplicate labels cannot stand for two human identities")
        principals[aid] = ids
    return {"binding_digest": binding_digest(binding), "approvers": principals}


def verify_host_evaluation(proof, binding: dict, verifier) -> dict:
    """The independent runner must attest to the version measured, not just an artifact id.

    No SC09 fields are added. This versioned adapter binding sits beside the complete score
    document and covers its digest plus the exact record, action and expected revision.
    """
    if not callable(verifier):
        raise GateRefusal("TRUSTED_EVAL_SOURCE_MISSING", "the host must supply an independent Eval verifier")
    try:
        result = verifier(copy.deepcopy(proof), copy.deepcopy(binding))
    except Exception as exc:
        raise GateRefusal("EVAL_AUTHENTICATION_FAILED", "host Eval verification failed") from exc
    if not isinstance(result, dict) or result.get("verified") is not True \
            or result.get("independent") is not True \
            or result.get("binding_digest") != binding_digest(binding) \
            or not isinstance(result.get("runner_id"), str) or not result["runner_id"].strip() \
            or result["runner_id"] != result["runner_id"].strip():
        raise GateRefusal("EVAL_AUTHENTICATION_FAILED", "an independent runner did not attest to these exact versions")
    return {"binding_digest": binding_digest(binding), "runner_id": result["runner_id"]}


def _assert_not_forged(proposal, approver: str) -> None:
    """A model must never be able to forge an approval (`04:17` I-2, `12:137` G1 唯一人类门)."""
    if not isinstance(proposal, dict):
        return
    claims = {key: proposal.get(key) for key in FORGED_APPROVAL_KEYS if key in proposal}
    payload = proposal.get("payload")
    if isinstance(payload, dict):
        claims.update({key: payload.get(key) for key in FORGED_APPROVAL_KEYS if key in payload})
    truthy = {k: v for k, v in claims.items() if v}
    if truthy:
        raise GateRefusal(
            "APPROVAL_FORGERY",
            f"the proposal itself carries approval field(s) {sorted(truthy)}: approval is not a "
            "producer-supplied field. A payload that asserts its own human consent is refused "
            "before any approval is recorded (`04:17` I-2; kd_gate.apply_mutation holds the same "
            "line on the write side)",
            {"fields": sorted(truthy)})
    produced = proposal.get("produced_by")
    kind = produced.get("kind") if isinstance(produced, dict) else produced
    actor_is_not_human = str(approver).lower() in NON_HUMAN_ACTORS
    producer_is_machine = str(kind or "").lower() in ("model", "compiler", "automation",
                                                     "system")
    if actor_is_not_human or (producer_is_machine and str(approver).lower()
                              not in HUMAN_ACTORS):
        raise GateRefusal("NOT_A_HUMAN_DECISION",
                          f"approval actor {approver!r} is not human while the payload was "
                          f"produced by {kind or 'unknown'!r}: G1 是仅有的人类门（`12:137`），且模型"
                          "只有提案权（`04:17` I-2）")
    if str(approver).lower() not in HUMAN_ACTORS:
        raise GateRefusal("NOT_A_HUMAN_DECISION",
                          f"approval actor {approver!r} is not one of {HUMAN_ACTORS}: only a "
                          "human decision counts at G1（`12:137`、`06:224` N25 [HUMAN]）")


# --------------------------------------------------------------------- recording an approval
def record_approval(proposal, *, approver, txn_id, action=None, target="", at=None,
                    second_approver=None, confirmation_flag=False, verdict="approve") -> dict:
    """Turn one human decision into a row: who, when, what, and the digest of exactly what was
    approved. Nothing is written -- the row is data the caller hands to the ledger owner.
    """
    if not isinstance(proposal, dict):
        raise GateRefusal("DIGEST_LESS_PROPOSAL", "approval proposal must be a nonempty object")
    payload = proposal.get("payload")
    canonicalized = proposal.get("canonicalized")
    if payload is not None and not isinstance(payload, dict):
        raise GateRefusal("PROPOSAL_MALFORMED", "proposal payload must be an object")
    if canonicalized is not None and not isinstance(canonicalized, dict):
        raise GateRefusal("PROPOSAL_MALFORMED", "canonicalized must be an object")
    records = (canonicalized or {}).get("records", [])
    if not isinstance(records, list) or any(
            not isinstance(rec, dict) or
            (rec.get("derived") is not None and not isinstance(rec["derived"], dict))
            for rec in records):
        raise GateRefusal("PROPOSAL_MALFORMED", "canonicalized records must be objects with typed derivations")
    classification = classify_action(action, target=target)
    _assert_not_forged(proposal, approver)
    digest = approved_digest(proposal)
    if str(approver).lower() not in HUMAN_ACTORS:                 # belt and braces, in order
        raise GateRefusal("NOT_A_HUMAN_DECISION", f"approver {approver!r} is not human")
    if not str(txn_id or "").strip():
        raise GateRefusal("TXN_ID_MISSING",
                          "approve and apply are one transaction（`06:247` N27）, so an approval "
                          "without a transaction id cannot be bound to the apply it consents to")
    if verdict not in ("approve", "reject"):
        raise GateRefusal("BLANKET_APPROVAL",
                          f"verdict {verdict!r} is not a per-item verdict: R1 要求逐条 verdict"
                          "（不糊批）（`06:225`）")
    if verdict == "reject":
        raise GateRefusal("NOT_APPROVED",
                          "a rejection was recorded through the approval path: a refusal is not "
                          "consent（`06:233` 橡皮图章防线）")
    if type(confirmation_flag) is not bool:
        raise GateRefusal("CONFIRMATION_FLAG_MALFORMED", "confirmation_flag must be a boolean")
    if classification["requires_confirmation_flag"] and confirmation_flag is not True:
        raise GateRefusal("CONFIRMATION_FLAG_MISSING",
                          f"{classification['tier']} 确认 flag 是契约本身（`06:226`）: refusing to "
                          "record an approval for an irreversible / content-destroying action "
                          "without the explicit confirmation flag")
    if classification["requires_second_approver"] and (
            str(second_approver or "").lower() not in HUMAN_ACTORS
            or str(second_approver).lower() == str(approver).lower()):
        raise GateRefusal("SECOND_APPROVER_MISSING",
                          "global-rule write needs the explicit second human gate "
                          "（`06:269`），got second_approver=None")

    subject = {"step": proposal.get("step"), "record_type": proposal.get("record_type"),
               "produced_by": proposal.get("produced_by"),
               "context_digest": proposal.get("context_digest"),
               "artifact_id": (payload or {}).get("artifact_id")
               or proposal.get("artifact_id"),
               "identities": [rec["derived"].get("identity")
                               for rec in records if rec.get("derived")]}
    return {
        "gate": "G1",
        "txn_id": str(txn_id).strip(),
        "approved_by": str(approver).lower(),
        "approved_at": at or _now_placeholder(),
        "second_approver": second_approver,
        "confirmation_flag": bool(confirmation_flag),
        "per_item_verdict": verdict,
        "proposal_digest": digest,
        "intent_digest": intent_digest(digest, target),
        "approved_subject": subject,
        "classification": classification,
        # the durable write path reads exactly this flag; it is set here, by a human having
        # acted, and is the only place in the package where a model payload gains it
        "human_approved": True,
        "digest_of_exactly_what_was_approved": digest,
        "execution_model_controlled": False,
        "model_identity_verified": False,
        "model_identity_note": "which model produced this proposal is a host fact recorded in "
                               "the S13 stamp; Round 2 froze execution_model_controlled=false, so "
                               "G1 records the approval against the DIGEST, never against a model "
                               "name it cannot verify",
        "basis": classification["basis"],
    }


# IMPLEMENTATION_GAP: which clock owns `approved_at` (the caller's clock vs the S13 stamp's
# created_at) is not adjudicated in Round 2, and picking one here would make G1 a second
# authority for time. The row keeps the caller's value when supplied, else this visible marker.
# / DEFERRED id none registered (newly surfaced -- recorded in W3-E-REPORT.md)
def _now_placeholder() -> str:
    return "at-not-supplied:caller-owns-clock"


def record_batch_approval(items, *, approver, txn_id, at=None) -> dict:
    """`06:225`: 允许批量批准，但每条提案须有独立 verdict，不能以批次结论代替逐条裁决。

    `items` = [{"proposal": {...}, "action": ..., "target": ..., "verdict": "approve",
    "confirmation_flag": bool, "second_approver": ...}, ...]. One row per proposal, each with
    its own digest; a batch that omits a per-item verdict is refused rather than defaulted.
    """
    if not isinstance(items, list) or not items:
        raise GateRefusal("EMPTY_BATCH", "an empty approval batch is a visible refusal, not a "
                                         "no-op success")
    rows, refusals = [], []
    for index, item in enumerate(items):
        if not isinstance(item, dict) or "verdict" not in item:
            refusals.append({"index": index, "code": "BLANKET_APPROVAL",
                             "message": "item carries no per-item verdict; R1 要求逐条 verdict "
                                        "（不糊批）（`06:225`）"})
            continue
        if "proposal" not in item:
            refusals.append({"index": index, "code": "PROPOSAL_MALFORMED",
                             "message": "approval item must contain a proposal"})
            continue
        try:
            rows.append(record_approval(item["proposal"], approver=approver, txn_id=txn_id,
                                        action=item.get("action"), target=item.get("target", ""),
                                        at=at, verdict=item["verdict"],
                                        confirmation_flag=item.get("confirmation_flag", False),
                                        second_approver=item.get("second_approver")))
        except GateRefusal as exc:
            refusals.append({"index": index, "code": exc.code, "message": exc.message})
    if refusals:
        # a batch is one transaction: one bad item refuses the whole batch instead of letting
        # an approval ride in on a sibling's consent
        raise GateRefusal("BATCH_ITEM_REFUSED",
                          f"{len(refusals)} of {len(items)} batch item(s) failed the G1 checks; "
                          "the whole batch is refused（`06:247` 任一步失败则整批不落）",
                          {"refusals": refusals, "rows_recorded": 0})
    return {"gate": "G1", "txn_id": str(txn_id).strip(), "rows": rows, "batch_size": len(rows)}


# --------------------------------------------------------------------- approve + apply = one transaction
def approve_and_apply(approval_rows, proposals, txn_id, *, apply=None) -> dict:
    """The mechanical half of `06:247` N27, in W2-C's bundle shape (`apply_bundle`).

    Pure by construction: it writes nothing, so there is no 'approved yesterday, applied
    today' state to desynchronise. Every approval row must pin a digest that still matches the
    proposal being applied, and the only thing this returns is the bundle S12 must commit.
    When an `apply` probe is supplied it runs inside the same call: any failure raises and no
    bundle comes back, so no approval can be reported as successful.
    """
    if not str(txn_id or "").strip():
        raise GateRefusal("TXN_ID_MISSING", "one shared transaction id is the pair's proof "
                                           "（`06:247` 五要素 4）")
    rows = approval_rows.get("rows") if isinstance(approval_rows, dict) else list(approval_rows)
    if not rows:
        raise GateRefusal("APPROVAL_MISSING",
                          "apply refused: no approval accompanied this call, and approve must be "
                          "in the same transaction as apply（`06:247`）")
    for row in rows:
        if not isinstance(row, dict) or row.get("gate") != "G1" or row.get("per_item_verdict") != "approve":
            raise GateRefusal("NOT_APPROVED", "apply requires per-item G1 approval objects")
        if str(row.get("txn_id") or "").strip() != str(txn_id).strip():
            raise GateRefusal("APPROVE_APPLY_SPLIT",
                              f"approval carries txn_id {row.get('txn_id')!r} but apply was asked "
                              f"for {txn_id!r}: two transactions, so the pair is refused"
                              "（`06:247` 五要素 4）")
        if row.get("human_approved") is not True or str(row.get("approved_by") or "").lower() \
                not in HUMAN_ACTORS:
            raise GateRefusal("NOT_A_HUMAN_DECISION",
                              "an approval row without the required human label cannot authorise a "
                              "durable write（`12:137`）")

    intents, covered = [], set()
    for proposal in proposals:
        digest = approved_digest(proposal)
        matches = [row for row in rows if row.get("proposal_digest") == digest]
        if len(matches) != 1:
            # `06:186` fail-closed 拒绝 apply: the bytes at hand are not the bytes consented to
            raise GateRefusal("DIGEST_MISMATCH",
                              f"no approval pins digest {digest[:16]}... for step "
                              f"{proposal.get('step')}: refusing to apply, and writing nothing "
                              "as if it had（`06:186` 失配 → fail-closed 拒绝 apply）")
        covered.add(digest)
        classification = (matches[0].get("classification") or {})
        intents.append({
            "artifact_id": (proposal.get("payload") or {}).get("artifact_id")
            or proposal.get("artifact_id") or proposal.get("step"),
            "record": proposal,
            "op": "ADD" if classification.get("tier") != TIER_R2 else "SUPERSEDE",
            "approved_digest": digest,
            "tier": classification.get("tier"),
            "produced_by": (proposal.get("produced_by") or {}).get("kind"),
            "reason": None,
            "action": classification.get("action"),
            "target": classification.get("target", ""),
        })
    stale = [row.get("proposal_digest") for row in rows
             if row.get("proposal_digest") not in covered]
    if stale:
        raise GateRefusal("APPROVAL_NOT_APPLICABLE",
                          f"approval row(s) {stale[:3]} pin no proposal in this batch: an "
                          "approval for absent content is not consent（`06:247`）")

    bundle = {
        "single_transaction": True,
        "txn_id": str(txn_id).strip(),
        "approve_rows": rows,
        "apply_intents": intents,
        "release": {"txn_id": str(txn_id).strip(),
                    "only_after_S12_reports_committed": True},
        "durable_write_owner": "S12 kd_write_txn.commit_batch",
        "handoff": handoff_to_s12({"txn_id": str(txn_id).strip(), "apply_intents": intents,
                                    "approve_rows": rows},
                                  store_dir=None),
        "wrote_anything": False,
    }
    if apply is not None:
        # same call, same transaction: a failing apply means this function never returns a
        # bundle, so the caller cannot hold an approval that outlived the write
        receipt = apply(bundle)
        bundle["apply_receipt"] = receipt
        status = (receipt or {}).get("status") if isinstance(receipt, dict) else receipt
        if status != "COMMITTED":
            raise GateRefusal("APPLY_FAILED_NOT_PERSISTED",
                              f"apply reported {status!r}, not 'committed': the approval is "
                              "discarded with it, and no half record exists"
                              "（`06:247` 不留 created_by=null 的半记录）")
    return bundle


def approval_receipt(bundle, commit_receipt) -> dict:
    """Called only AFTER S12 reported a committed batch. Until then there is no receipt: the
    approval row lives inside the bundle, not in a state G1 owns."""
    if not isinstance(bundle, dict) or not bundle.get("single_transaction"):
        raise GateRefusal("NO_BUNDLE", "there is no approval to receipt: no single-transaction "
                                       "bundle was produced")
    status = (commit_receipt or {}).get("status") if isinstance(commit_receipt, dict) \
        else commit_receipt
    if status != "COMMITTED":
        raise GateRefusal("APPLY_NOT_COMMITTED",
                          f"commit receipt status={status!r}: the approval must not persist as "
                          "if applying succeeded（`06:247` N27）")
    receipt_txn = (commit_receipt or {}).get("txn_id") if isinstance(commit_receipt, dict) else None
    if str(receipt_txn or "").strip() != bundle["txn_id"]:
        raise GateRefusal("TRANSACTION_SPLIT",
                          f"commit receipt names txn {receipt_txn!r} but the approved transaction "
                          f"was {bundle['txn_id']!r}: two transactions, so no receipt")
    return {
        "gate": "G1", "txn_id": bundle["txn_id"],
        "lifecycle_event_rows": [{"entity": "approval", "entity_id": row["proposal_digest"],
                                 "op": "APPROVE", "at": row["approved_at"],
                                 "by": row["approved_by"], "tier": (row["classification"]
                                                                    or {}).get("tier")}
                                for row in bundle["approve_rows"]],
        "ledger_owner": "S17 kd_lifecycle / S12 kd_write_txn (append-only lifecycle_event, "
                        "`05` §2 行 lifecycle_event[])",
        "g1_wrote_anything": False,
    }


def handoff_to_s12(bundle, store_dir=None, evidence=None, facts_present=None) -> dict:
    """The hand-off as data. G1 does not import `kd_write_txn` and does not call it: naming a
    callee here would turn a gate into a runtime, and the pipeline owns the composition.
    """
    return {
        "call": "kd_write_txn.commit_batch",
        "kwargs": {"store_dir": store_dir,
                   "intents": list(bundle.get("apply_intents") or []),
                   "evidence": list(evidence or []),
                   "human_approved": True,
                   "approval": {"txn_id": bundle.get("txn_id"),
                                "approve_rows": list(bundle.get("approve_rows") or [])},
                   "facts": "host-supplied kd_provenance_stamp.RuntimeFacts"
                            if facts_present is None else ("supplied" if facts_present
                                                           else "MISSING")},
        "txn_id": bundle.get("txn_id"),
        "executable": False,
        "missing_host_inputs": ["RuntimeFacts", "SC12 adjudication", "SC09 score document", "SC04 artifact assembly"],
        "why_human_approved_true": "per-item G1 labels and digests are consistency checks, not "
                                   "authenticated signatures. Missing host inputs cannot be filled "
                                   "by treating this flag or the handoff as a commit authorization",
    }


def write_surface() -> tuple:
    """Names this module exports that could write durable state: empty by construction, and
    asserted empty of write primitives by the test file (`--audit` stays exit 0)."""
    return ()


def describe_gate() -> dict:
    """Describe risk tiers and their separate current write-admission boundaries for hosts."""
    tiers = {}
    for row in ACTION_CLASS_ROWS:
        tiers.setdefault(row["tier"], []).append(row["action"])
    return {"human_actors": HUMAN_ACTORS,
            "tiers": {tier: sorted(names) for tier, names in sorted(tiers.items())},
            "classification_scope": CLASSIFICATION_SCOPE,
            "requires_human_by_tier": {TIER_R0: False, TIER_R1: True, TIER_R2: True},
            "write_admission_by_tier": dict(WRITE_ADMISSION_BY_TIER),
            "table_drift": TABLE_DRIFT,
            "one_transaction_rule": "`06:247` N27 approve 与 apply 同事务",
            "no_state_held": "G1 keeps no approval state; the approval arrives as an argument "
                             "(same shape as `kd_quarantine.apply_bundle`, W2-C)"}
