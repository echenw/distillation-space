#!/usr/bin/env python3
"""S10 kd_gate_tree -- the adjudicated promotion decision tree (`06-PROMOTION-POLICY.md` 1-5).

The tree is DATA: `NODE_TABLE` (38 nodes) plus `EDGE_TABLE` (87 branches), each edge carrying
its source, its condition id and its destination (a node, one of 11 terminal exits, or one of
2 explicit refusal exits). Node and branch counts are derived from these two tables by
`count_structure()`, never hardcoded -- Rounds 1 and 2 both shipped claimed counts that the
implementation did not have.

Adjudication is a walk: `EVALUATORS[node_id]` returns the condition id of the edge taken, and
the walk ends when the destination is a landing (`LANDINGS`) or a refusal (`REFUSALS`).
A node that cannot be decided without an undecided parameter or an unshipped sibling module
raises `GateRefusal` -- a named refusal -- rather than defaulting.

What this module deliberately does NOT do:
  * it writes nothing to disk (it emits an intent bundle for S12 `kd_write_txn.commit_batch`);
  * it gives the model no adjudication power (06 3: "Stage 1 模型无裁决权"; M1-M4 have proposal
    rights only). Model-produced values are admissible ONLY as recorded proposals feeding the
    four [LLM] Stage-0 diagnoses, and every durable exit still needs a human decision at N25;
  * it invents no threshold. Each node declares `threshold_keys`; a key that
    `references/promotion-config.json` does not carry produces `R-DEFERRED` with the DEFERRED id
    (06 6 leaves DD-1's 8 sub-parameters undecided and says so).

Clusters: CM-27 per-item verdict (one verdict per candidate, a batch pass/fail is refused by
`assert_per_item_verdict`), CM-31 approval view carries its budget owner (owner is S18),
CM-32 inert quarantine is Stage 2's five nodes -- a candidate that stops there produces no
proposal and no count.
"""
from __future__ import annotations

import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import kd_provenance as prov  # noqa: E402  frozen kernel: support counting + content hash

# ------------------------------------------------------------------ exit vocabulary (06 5.1)
#: 10 required landings; "do nothing" has TWO physical exits (silent / with ledger), so the
#: terminal dispatch node N29 has 11 out-edges (06 1 table row "终态落点分派").
LANDINGS = (
    "L-PATTERN",              # count only, keep identity, no proposal, never the resident layer
    "L-NOTHING",              # nothing to propose, silent
    "L-NOTHING+LEDGER",       # nothing to propose, but a lifecycle_event row is mandatory
    "L-SCRIPT",
    "L-LINT",
    "L-TEST",
    "L-EVAL",
    "L-SKILL",
    "L-RULE-PROJECT",         # scope.layer == "project"
    "L-RULE-GLOBAL",          # scope.layer == "global"  (R1 + an explicit second human gate)
    "L-ARCHIVE",              # reversible ceiling; never a physical delete
)
#: explicit refusal exits (06 1: every branch ends at a landing OR an explicit refusal exit)
REFUSALS = ("R-REROOT", "R-STAGE0-INCOMPLETE")

STAGE_NAMES = {0: "Stage 0 FAILED_RULE 前置路由", 1: "Stage 1 确定性准入",
               2: "Stage 2 惰性候选隔离", 3: "Stage 3 风险分层与写事务",
               4: "终态落点分派"}

# CM-27: the verdict vocabulary is PER ITEM. Nothing here can express "the batch passed".
ITEM_VERDICTS = ("PROMOTE", "HOLD_AT_PATTERN", "DROP_SILENT", "DROP_WITH_LEDGER",
                 "RETIRE_TO_ARCHIVE", "PROPOSE_DISPOSITION", "REFUSE")
#: batch-level wording is the shape Round 2 names as the failure: one verdict for a set
BATCH_FORBIDDEN_KEYS = ("verdicts", "batch_verdict", "all_passed", "any_failed", "aggregate")
BATCH_FORBIDDEN_WORDS = ("pass", "fail", "passed", "failed", "ok", "approved_batch")

#: RH-P0-05/06: keys a candidate (UNTRUSTED DOMAIN INPUT) must never use to impersonate a trusted
#: decision. `adjudicate` strips them on entry and records them in the verdict's
#: `ignored_untrusted_keys`; the human approval and the eval verdict reach S10 ONLY through the
#: independent `approval_context` (G1) and `eval_verdict` (S16) parameters. Untrusted Candidate
#: != Trusted Decision.
UNTRUSTED_DECISION_KEYS = ("human_decision", "eval_result", "eval_verdict", "approval_context",
                           "human_approved", "approved", "approved_by", "auto_approved",
                           "approval_level", "approval_digest", "waive_gate", "skip_human_gate")

#: M7 (`05-DATA-MODEL.md:111`) -- three carriers, never interchangeable.
M7_CARRIERS = {
    "evidence": ("use_count", "view_count", "patch_count"),
    "pattern": ("support_count", "distinct_occurrence_count"),
    "artifact": ("adherence_rate",),
}

#: SC11 `scope.layer` (05 5.3). Only project and global are standing-preference layers, so only
#: those two can be rule landings; `cohort` is an occurrence axis and is refused as a rule layer.
LAYERS = ("project", "global", "cohort")
RULE_LAYERS = {"project": "L-RULE-PROJECT", "global": "L-RULE-GLOBAL"}

DISPOSITIONS = ("ADD", "MOVE", "UPDATE", "MERGE", "AUTOMATE", "SUPERSEDE", "DELETE", "ARCHIVE", "RESTORE")

# --------------------------------------------------------------------------- node table (38)
NODE_TABLE = (
    # ---- Stage 0: 17 nodes (N00, N01-N08, N05a/N05b/N06a/N06b/N07a/N08a, N09, N09b)
    dict(id="N00", stage=0, judge="DET",
         condition="does this candidate's problem already have Rule/Skill/Doc coverage -- all "
                   "three of (a) L0 identity hit or same Pattern-Key, (b) scope predicate hit, "
                   "(c) non-empty trigger anchor intersection",
         requires=("known_coverage",)),
    dict(id="N01", stage=0, judge="DET",
         condition="D1 not loaded: the covered entry never appears in the read/injection ledger, "
                   "or the assembly layer can prove it is not in the load set",
         requires=("known_coverage",)),
    dict(id="N02", stage=0, judge="DET",
         condition="D2 wrong trigger: the trigger states periodicity only and no event anchor "
                   "('Periodically is not a trigger an agent can act on')",
         requires=("known_coverage",)),
    dict(id="N03", stage=0, judge="DET",
         condition="D3 wrong scope: the failure sample does not match the declared path/applyTo "
                   "predicate, or level (project/global) disagrees; a predicate that fails its "
                   "own self-check may not MOVE",
         requires=("known_coverage",)),
    dict(id="N04", stage=0, judge="DET",
         condition="D4 not mechanically enforceable: the rule id is bound to no assert/lint/type/"
                   "test -- the literal only appears in prompt text",
         requires=("known_coverage",)),
    dict(id="N05", stage=0, judge="LLM",
         condition="D5 ambiguous (after the deterministic prescreen: >=2 active entries under one "
                   "identity key, or the trigger words were eaten by the description window)",
         requires=("model_diagnoses",)),
    dict(id="N05a", stage=0, judge="LLM",
         condition="can one rewrite disambiguate it", requires=("model_diagnoses",)),
    dict(id="N05b", stage=0, judge="LLM",
         condition="is it the same item as the existing entry (yes -> MERGE with absorbed_into)",
         requires=("model_diagnoses",)),
    dict(id="N06", stage=0, judge="LLM",
         condition="D6 conflicting instruction: deterministic matching only catches same-shape "
                   "duplication, a real contradiction needs the model",
         requires=("model_diagnoses",)),
    dict(id="N06a", stage=0, judge="DET",
         condition="can the two coexist once scope/trigger are narrowed",
         requires=("known_coverage",)),
    dict(id="N06b", stage=0, judge="JUDGE",
         condition="which one is authoritative (undecidable -> record unresolved_conflict for the "
                   "human batch, the correct zero-LLM exit)",
         requires=("judge_decision",)),
    dict(id="N07", stage=0, judge="LLM",
         condition="D7 ignored: present AND still violated (presence side is decidable via the "
                   "Evidence-layer use/view carriers; the violation side has no mechanical "
                   "implementation in this round)",
         requires=("model_diagnoses",)),
    dict(id="N07a", stage=0, judge="DET",
         condition="is that rule mechanically decidable (reuse the D4 predicate) -- yes -> AUTOMATE "
                   "it into an assertion; no -> MOVE/UPDATE; ADD is explicitly forbidden here",
         requires=("known_coverage",)),
    dict(id="N08", stage=0, judge="LLM",
         condition="D8 outdated: must be a re-verification of the authority, never an age test "
                   "('Age alone proves neither that context is wrong nor that it should be "
                   "removed')",
         requires=("model_diagnoses",)),
    dict(id="N08a", stage=0, judge="DET",
         condition="is the authority a machine artifact (file/version/schema) -- then reverify: "
                   "pass -> SUPERSEDE, fail -> DELETE proposal through Stage 3 R2",
         requires=("known_coverage",)),
    dict(id="N09", stage=0, judge="DET",
         condition="did all eight diagnoses miss (a hit that was never routed is not a miss: the "
                   "tree refuses instead of continuing)",
         requires=("known_coverage",)),
    dict(id="N09b", stage=0, judge="DET",
         condition="ADD preconditions (a) born as an umbrella (b) the preference order did not "
                   "land on create (c) identity key resolved and content_hash differs",
         requires=("add_preconditions",)),
    # ---- Stage 1: 9 nodes (N10-N18), the model has no adjudication power here
    dict(id="N10", stage=1, judge="DET", condition="scope legal and non-empty (SC11 S1 fail-closed)",
         requires=("scope",)),
    dict(id="N11", stage=1, judge="DET", condition="identity L0 canonical key resolvable, and "
         "not model-produced (a model key would be the forbidden downgrade)",
         requires=("identity",)),
    dict(id="N12", stage=1, judge="DET", condition="refs_integrity has no dangling reference",
         requires=("refs",)),
    dict(id="N13", stage=1, judge="DET", condition="every evidence_refs resolver passes AND at "
         "least one runner-written PASS exists (this is the direct counter to 09's "
         "'codebase with an unenforced threshold')",
         requires=("refs", "evidence")),
    dict(id="N14", stage=1, judge="DET", threshold_keys=("min_distinct_evidence",),
         condition="Pattern-layer support_count >= MIN and the retry is monotonic (a new N+1th "
                   "piece of evidence, not the passage of time)", requires=("ledger",)),
    dict(id="N15", stage=1, judge="DET", threshold_keys=("min_independent_cohorts",),
         condition="distinct_occurrence_count >= minimum independent sources after dedup by scope "
                   "(two copies of one skill must not fake 2+)", requires=("ledger",)),
    dict(id="N16", stage=1, judge="DET",
         threshold_keys=("min_distinct_tasks", "min_tasks_not_this_session"),
         deferred=("DD-1-sub04", "06 6 DEF-4 / 05 F4: no shipped constant carries the task-span "
                                 "threshold, so this node cannot decide -- refused, not defaulted"),
         condition="sources span >= 2 distinct tasks and >= 1 task that is not this session",
         requires=("counts",)),
    dict(id="N17", stage=1, judge="DET", threshold_keys=("min_interval_hours",),
         deferred=("DD-1-sub08", "06 6 DEF-8 -> N17: the cooldown/debounce members were never "
                                 "evidenced, so the due gate has no interval to compare against"),
         condition="due gate: input digest unchanged OR min_interval_hours not elapsed -> the "
                   "whole pipeline does not enter and the model is called zero times",
         requires=("digest",)),
    dict(id="N18", stage=1, judge="DET",
         condition="mechanical decidability pre-judgement -> which landing class Stage 3 will "
                   "produce (3 exits: CI-evaluable / structural-assertable / behavioural-only)",
         requires=("mechanical_form",)),
    # ---- Stage 2: 5 nodes (N19, N20, N21, N22, N22b) -- CM-32 inert quarantine, 9 branches
    dict(id="N19", stage=2, judge="DET",
         condition="candidate is in the inert area and its sha256 still matches the stored draft "
                   "(five elements 1+2); mismatch -> fail-closed refusal to apply + failed ledger",
         requires=("pending",)),
    dict(id="N20", stage=2, judge="DET",
         condition="no pending candidate for the same target (conflict refusal, element 3); the "
                   "known side effect is logged as suppressed_by_pending, never bypassed",
         requires=("pending",)),
    dict(id="N21", stage=2, judge="DET",
         threshold_keys=("pending_ttl_hours",),
         deferred=("DD-1-sub02", "06 4 N21 needs a per-item watermark and an expiry channel; the "
                                 "expiry interval is not carried by the single constants file"),
         condition="idempotency watermark (no replay) and the proposal file has an expiry channel",
         requires=("pending",)),
    dict(id="N22", stage=2, judge="DET",
         condition="Rejected and Failed are kept apart (element 5): a rejected item may not be "
                   "re-proposed without new evidence, a failed one may",
         requires=("pending", "ledger")),
    dict(id="N22b", stage=2, judge="LLM",
         condition="the ONLY allowed model intervention: draft + suggested tier + size, and the "
                   "draft must be an executable-assertion candidate, not prose for a human to read",
         requires=("model_draft",)),
    # ---- Stage 3: 6 nodes (N23-N28), 12 branches
    dict(id="N23", stage=3, judge="DET",
         condition="does the action touch the resident layer (AGENTS.md / CLAUDE.md / rules / "
                   "skills / project docs)", requires=()),
    dict(id="N24", stage=3, judge="DET",
         deferred=("DD-1-sub01", "06 6 DEF-1 -> N25 R0/R1 boundary + DEF-3 -> N24 (a)(b)(c): the "
                                 "admitted unattended action set is 11's T0 six actions, which the "
                                 "slices never enumerate, so no action is admitted yet"),
         condition="the 'may run unattended' three-condition gate: mechanically decidable, "
                   "reversible, idempotent and inside the self-authored ownership boundary",
         requires=("unattended_claim",)),
    dict(id="N25", stage=3, judge="HUMAN",
         condition="human confirmation by write risk: R1 resident layer (per-item, no blanket "
                    "batch), R2 irreversible (any delete or content-destroying merge) needs the "
                    "confirmation flag as part of the contract; a global rule adds the explicit "
                    "second gate",
         requires=("human_decision",)),
    dict(id="N26", stage=3, judge="DET",
         condition="the single write path runs: validate-before-write admission, atomic write "
                   "(tmp+rename+fsync), the commit point last; this node emits the intent bundle "
                   "for S12 and never writes itself",
         requires=("write_target",)),
    dict(id="N27", stage=3, judge="DET",
         condition="approve and apply are ONE transaction -- the bundle must carry the approve "
                   "ledger row together with the applied rows, otherwise nothing lands",
         requires=("transaction",)),
    dict(id="N28", stage=3, judge="DET",
         condition="complete S16 score and subject verified before persistence (approval != "
                   "correctness): holdout regression and independent instrument. A real paid "
                   "runner/preflight adapter is not implemented by this node",
         requires=("eval_result",)),
    # ---- terminal dispatch: 1 node, 11 branches (10 landings, 'do nothing' split in two)
    dict(id="N29", stage=4, judge="DET",
         condition="dispatch the action x landing pair to one of the 11 physical exits",
         requires=()),
)

# --------------------------------------------------------------------------- edge table (87)
# (source, condition, destination, optional landing forced on arrival at N29)
EDGE_TABLE = (
    # Stage 0 -- 36 branches: N00 also routes an explicit approved-contract lifecycle request.
    ("N00", "already_covered", "N01"),
    ("N00", "not_covered", "N10"),
    ("N00", "lifecycle_requested", "N10"),
    ("N01", "hit", "N23", "MOVE"),
    ("N01", "miss", "N02"),
    ("N02", "hit", "N23", "UPDATE"),
    ("N02", "miss", "N03"),
    ("N03", "hit_and_predicate_ok", "N23", "MOVE"),
    ("N03", "hit_predicate_selfcheck_failed", "N29", "L-NOTHING+LEDGER"),
    ("N03", "miss", "N04"),
    ("N04", "hit", "N23", "AUTOMATE"),
    ("N04", "miss", "N05"),
    ("N05", "hit", "N05a"),
    ("N05", "miss", "N06"),
    ("N05a", "reword_resolves", "N23", "UPDATE"),
    ("N05a", "needs_identity_call", "N05b"),
    ("N05b", "same_item", "N23", "MERGE"),
    ("N05b", "unresolved_ambiguity", "N29", "L-NOTHING+LEDGER"),
    ("N06", "conflict", "N06a"),
    ("N06", "no_conflict", "N07"),
    ("N06a", "separable", "N23", "MOVE"),
    ("N06a", "inseparable", "N06b"),
    ("N06b", "authority_decidable", "N23", "SUPERSEDE"),
    ("N06b", "unresolved_conflict", "N29", "L-NOTHING+LEDGER"),
    ("N07", "ignored", "N07a"),
    ("N07", "miss", "N08"),
    ("N07a", "enforceable", "N23", "AUTOMATE"),
    ("N07a", "not_enforceable", "N23", "UPDATE"),
    ("N08", "hit", "N08a"),
    ("N08", "miss", "N09"),
    ("N08a", "reverify_pass", "N23", "SUPERSEDE"),
    ("N08a", "reverify_fail", "N23", "DELETE"),
    ("N09", "all_diagnoses_miss", "N09b"),
    ("N09", "diagnosis_unrouted", "R-STAGE0-INCOMPLETE"),
    ("N09b", "add_preconditions_hold", "N10"),
    ("N09b", "add_preconditions_fail", "N29", "L-PATTERN"),
    # Stage 1 -- 19 branches, N18 has 3 landing classes
    ("N10", "scope_ok", "N11"),
    ("N10", "scope_reject", "N29", "L-NOTHING+LEDGER"),
    ("N11", "key_resolvable", "N12"),
    ("N11", "key_unresolvable", "R-REROOT"),
    ("N12", "refs_clean", "N13"),
    ("N12", "refs_dangling", "N29", "L-NOTHING+LEDGER"),
    ("N13", "runner_pass_present", "N14"),
    ("N13", "no_runner_pass", "N29", "L-NOTHING"),
    ("N14", "support_met", "N15"),
    ("N14", "support_below", "N29", "L-PATTERN"),
    ("N15", "occurrences_met", "N16"),
    ("N15", "occurrences_below", "N29", "L-PATTERN"),
    ("N16", "span_met", "N17"),
    ("N16", "span_below", "N29", "L-PATTERN"),
    ("N17", "due", "N18"),
    ("N17", "not_due", "N29", "L-PATTERN"),
    ("N18", "ci_evaluable", "N19", "ADD"),
    ("N18", "structural_only", "N19", "ADD"),
    ("N18", "behavioural_only", "N19", "ADD"),
    # Stage 2 -- 9 branches (2+2+2+2+1; N22b is a single-out proposal node)
    ("N19", "digest_intact", "N20"),
    ("N19", "digest_mismatch", "N29", "L-NOTHING+LEDGER"),
    ("N20", "target_free", "N21"),
    ("N20", "pending_conflict", "N29", "L-NOTHING+LEDGER"),
    ("N21", "watermark_fresh", "N22"),
    ("N21", "replay_or_expired", "N29", "L-NOTHING+LEDGER"),
    ("N22", "admissible", "N22b"),
    ("N22", "rejected_without_new_evidence", "N29", "L-NOTHING+LEDGER"),
    ("N22b", "draft_proposed", "N23", "ADD"),
    # Stage 3 -- 12 branches
    ("N23", "touches_persistent", "N25"),
    ("N23", "not_persistent", "N24"),
    ("N24", "r0_unattended", "N26"),
    ("N24", "needs_human", "N25"),
    ("N25", "approved", "N26"),
    ("N25", "refused", "N29", "L-NOTHING+LEDGER"),
    ("N26", "write_staged", "N27"),
    ("N26", "slug_collision", "N29", "L-NOTHING+LEDGER"),
    ("N27", "intent_ready", "N28"),
    ("N27", "intent_incomplete", "N29", "L-NOTHING+LEDGER"),
    ("N28", "regression_pass", "N29"),
    ("N28", "regression_fail", "N29", "L-ARCHIVE"),
    # terminal dispatch -- 11 branches: the 10 landings, 'do nothing' split into two exits
    ("N29", "L-PATTERN", "L-PATTERN"),
    ("N29", "L-NOTHING", "L-NOTHING"),
    ("N29", "L-NOTHING+LEDGER", "L-NOTHING+LEDGER"),
    ("N29", "L-SCRIPT", "L-SCRIPT"),
    ("N29", "L-LINT", "L-LINT"),
    ("N29", "L-TEST", "L-TEST"),
    ("N29", "L-EVAL", "L-EVAL"),
    ("N29", "L-SKILL", "L-SKILL"),
    ("N29", "L-RULE-PROJECT", "L-RULE-PROJECT"),
    ("N29", "L-RULE-GLOBAL", "L-RULE-GLOBAL"),
    ("N29", "L-ARCHIVE", "L-ARCHIVE"),
)

#: N18 / dispositions -> landing class. `rule` is the only class whose physical exit is decided by
#: `scope.layer`, which is exactly what S04 says `layer` exists for (05 5.3 S3/S4).
CLASS_BY_MECHANICAL_FORM = {"ci_evaluable": "enforceable", "structural_only": "eval",
                            "behavioural_only": "rule"}
CLASS_BY_ENFORCE_FORM = {"test": "test", "lint": "lint", "script": "script", "eval": "eval",
                         "skill": "skill", "rule": "rule"}

#: disposition x class -> landing ("RULE_LAYER" = read scope.layer, the only real consumer)
LANDING_ROUTER = {
    ("ADD", "test"): "L-TEST", ("ADD", "lint"): "L-LINT", ("ADD", "script"): "L-SCRIPT",
    ("ADD", "eval"): "L-EVAL", ("ADD", "skill"): "L-SKILL", ("ADD", "rule"): "RULE_LAYER",
    ("UPDATE", "rule"): "RULE_LAYER", ("MOVE", "rule"): "RULE_LAYER",
    ("UPDATE", "skill"): "L-SKILL", ("MOVE", "skill"): "L-SKILL",
    ("MERGE", "skill"): "L-SKILL", ("MERGE", "rule"): "RULE_LAYER",
    ("SUPERSEDE", "skill"): "L-SKILL", ("SUPERSEDE", "rule"): "RULE_LAYER",
    ("SUPERSEDE", "retire"): "L-ARCHIVE", ("DELETE", "retire"): "L-ARCHIVE",
    ("AUTOMATE", "test"): "L-TEST", ("AUTOMATE", "lint"): "L-LINT",
    ("AUTOMATE", "script"): "L-SCRIPT", ("AUTOMATE", "eval"): "L-EVAL",
    ("AUTOMATE", "rule"): "RULE_LAYER",
    ("ARCHIVE", "retire"): "L-ARCHIVE",
    ("RESTORE", "test"): "L-TEST", ("RESTORE", "lint"): "L-LINT",
    ("RESTORE", "script"): "L-SCRIPT", ("RESTORE", "eval"): "L-EVAL",
    ("RESTORE", "skill"): "L-SKILL", ("RESTORE", "rule"): "RULE_LAYER",
}


class GateRefusal(Exception):
    """A named refusal: an undecided parameter, an unshipped sibling module, a carrier misuse.

    Carrying `exit_code`, `deferred_id` and `node` is the point -- a refusal must be attributable
    to the node that raised it and, where it is a deferred parameter, to the DEFERRED entry that
    owns it. Silence is the failure mode 06:run-account-anti-silence names.
    """

    def __init__(self, reason, node="", exit_code=2, deferred_id="", gap_id=""):
        super().__init__(reason)
        self.reason = reason
        self.node = node
        self.exit_code = exit_code
        self.deferred_id = deferred_id
        self.gap_id = gap_id


class NotLandedYet(GateRefusal):
    """A sibling module this tree calls against its contract row is absent (Wave 3, other agent)."""

    def __init__(self, module, contract_row, node=""):
        super().__init__("NOT_LANDED_YET: %s (contract %s) is not on disk, so %s cannot be "
                         "adjudicated by this process -- the tree refuses instead of doing the "
                         "missing module's job" % (module, contract_row, node or "this node"),
                         node=node, exit_code=2, gap_id="NOT_LANDED_YET")


class PerItemVerdictViolation(Exception):
    """CM-27: someone tried to give one verdict to a set."""


# ------------------------------------------------------------------ structure arithmetic
def node_ids():
    return tuple(n["id"] for n in NODE_TABLE)


def count_structure():
    """Counts derived from the tables themselves -- this is what the test asserts against."""
    nodes = list(NODE_TABLE)
    edges = list(EDGE_TABLE)
    by_stage = {}
    for n in nodes:
        by_stage.setdefault(n["stage"], {"nodes": 0, "branches": 0})
        by_stage[n["stage"]]["nodes"] += 1
    out = {}
    for e in edges:
        src = e[0]
        stage = next(n["stage"] for n in nodes if n["id"] == src)
        by_stage[stage]["branches"] += 1
        out[src] = out.get(src, 0) + 1
    return {"nodes": len(nodes), "branches": len(edges),
            "by_stage": {STAGE_NAMES[k]: v for k, v in sorted(by_stage.items())},
            "out_degree": dict(sorted(out.items())),
            "landings": len(LANDINGS), "refusals": len(REFUSALS)}


def validate_structure():
    """Structural self-check: no dangling branch, no unknown id, every node has out-edges."""
    ids = set(node_ids())
    sinks = set(LANDINGS) | set(REFUSALS)
    problems = []
    seen_pairs = set()
    for e in EDGE_TABLE:
        src, cond, dst = e[0], e[1], e[2]
        if src not in ids:
            problems.append("edge from unknown node %r" % src)
        if dst not in ids and dst not in sinks:
            problems.append("edge %s -> %s points at nothing" % (src, dst))
        if (src, cond) in seen_pairs:
            problems.append("duplicate condition %s/%s" % (src, cond))
        seen_pairs.add((src, cond))
    for n in NODE_TABLE:
        if n["id"] not in {e[0] for e in EDGE_TABLE}:
            problems.append("node %s is a dead end (0 out-edges)" % n["id"])
    for n in NODE_TABLE:
        for key in ("condition", "judge", "stage"):
            if key not in n:
                problems.append("node %s carries no %s" % (n["id"], key))
    return problems


# ------------------------------------------------------------------ helpers used by evaluators
def threshold_for(node_id, cfg, key):
    """Read one threshold out of the single constants file, or refuse with its DEFERRED id."""
    node = NODE_BY_ID[node_id]
    if key not in (cfg or {}):
        deferred = node.get("deferred") or ("DD-1 group",
                                            "%s needs %r which references/promotion-config.json "
                                            "does not carry" % (node_id, key))
        raise GateRefusal("threshold %r for %s is not carried by the single constants file: %s"
                          % (key, node_id, deferred[1]),
                          node=node_id, exit_code=2, deferred_id=deferred[0],
                          gap_id="IMPLEMENTATION_GAP / DEFERRED")
    return cfg[key]


def read_pattern_carrier(ledger, field, node_id):
    """M7 (`05:111`): the promotion gate reads the Pattern layer only. Reading the wrong carrier
    is a bug with a name, never a silent fallback."""
    if field not in (ledger or {}):
        other = [k for layer, keys in M7_CARRIERS.items() if layer != "pattern"
                 for k in keys if k in (ledger or {})]
        raise GateRefusal("M7 carrier violation at %s: %s (Pattern layer) is absent while %s "
                          "are present -- Evidence-layer event counts and Artifact-layer "
                          "adherence_rate are different carriers and may not substitute for it"
                          % (node_id, field, other),
                          node=node_id, exit_code=2, gap_id="M7_CARRIER_MISMATCH")
    return ledger[field]


def _module(name):
    try:
        return importlib.import_module(name)
    except ImportError:
        return None


def _model_proposal(ctx, dim, node_id):
    """Stage 0's four [LLM] diagnoses consume a RECORDED proposal (M1-M4 have proposal rights
    only). Nothing here calls a model, and a model answer never reaches Stage 1."""
    c = ctx["candidate"]
    store = c.get("model_diagnoses")
    if store is None:
        step = _module("kd_model_step")
        hint = ("kd_model_step is present but returned no recorded %s proposal" % dim
                if step else "kd_model_step (S17, M1-M4) is not on disk")
        raise NotLandedYet(hint, "contracts.model_steps M1/M2/M2b", node=node_id)
    if dim not in store:
        raise GateRefusal("diagnosis %s was never run, so 'all eight missed' cannot be claimed "
                          "at %s -- Stage 0 may not be skipped" % (dim, node_id),
                          node=node_id, exit_code=2, gap_id="STAGE0_DIAGNOSIS_NOT_RUN")
    rec = store[dim]
    if rec.get("produced_by") == "model" and rec.get("adjudication", False):
        raise GateRefusal("%s: a model proposal may not carry adjudication power" % node_id,
                          node=node_id, exit_code=2, gap_id="MODEL_NO_ADJUDICATION")
    ctx["llm_calls"] = ctx.get("llm_calls", 0) + 1
    return rec


def _coverage_hits(ctx):
    c = ctx["candidate"]
    cov = c.get("known_coverage") or []
    hits = [e for e in cov if e.get("identity_hit") and e.get("scope_predicate_hit")
            and e.get("trigger_overlap")]
    return hits


# --------------------------------------------------------------------------- evaluators
def _ev_n00(ctx):
    request = ctx["candidate"].get("lifecycle_request")
    if request is not None:
        if not isinstance(request, dict) or set(request) != {"action", "artifact_id"} \
                or request["action"] not in ("ARCHIVE", "RESTORE") \
                or request["artifact_id"] != ctx["candidate"].get("artifact_id"):
            raise GateRefusal("N00: malformed lifecycle request", node="N00", gap_id="LIFECYCLE_REQUEST_INVALID")
        ctx["disposition"] = request["action"]
        return "lifecycle_requested"  # S12 proves resident/history identity; all admission gates still run.
    hits = _coverage_hits(ctx)
    ctx["coverage_hits"] = hits
    ctx["n00_basis"] = ("no coverage index supplied: the three conditions cannot all hold, so "
                        "'already covered' is not established" if not hits else
                        "%d covered entr%s hit all three conditions" % (len(hits), "y" if len(hits) == 1 else "ies"))
    if hits:
        ctx["stage0_forbidden"] = "ADD NEW RULE"      # 06 2: entering D1..D8 forbids ADD
    return "already_covered" if hits else "not_covered"


def _hit_field(ctx, name, truthy):
    for e in ctx["coverage_hits"]:
        if name not in e:
            raise GateRefusal("D-%s: coverage entry %r does not carry %r, so the diagnosis is "
                              "undecidable rather than negative"
                              % (name, e.get("rule_id", "?"), name),
                              node=ctx["node"], exit_code=2, gap_id="SIGNAL_NOT_EVIDENCED")
        if truthy(e[name]):
            ctx["hit_entry"] = e
            return True
    return False


def _ev_n01(ctx):
    return "hit" if _hit_field(ctx, "ever_loaded", lambda v: v is False) else "miss"


def _ev_n02(ctx):
    return "hit" if _hit_field(ctx, "periodicity_only", lambda v: v is True) else "miss"


def _ev_n03(ctx):
    if not _hit_field(ctx, "scope_matches_failure_sample", lambda v: v is False):
        return "miss"
    e = ctx["hit_entry"]
    if e.get("predicate_selfcheck_ok") is not True:
        return "hit_predicate_selfcheck_failed"     # may not MOVE before the predicate is fixed
    return "hit_and_predicate_ok"


def _ev_n04(ctx):
    return "hit" if _hit_field(ctx, "bound_to", lambda v: not v) else "miss"


def _ev_n05(ctx):
    # deterministic prescreen first: >=2 active entries under one identity key, or the trigger
    # words were eaten by the description window
    active = ctx["candidate"].get("active_entries_under_same_key", 0)
    truncated = any(e.get("trigger_truncated") for e in _coverage_hits(ctx))
    if active < 2 and not truncated:
        ctx["prescreen"] = "no >=2 active entries and no truncated trigger: D5 cannot hit"
        return "miss"
    return "hit" if _model_proposal(ctx, "D5", "N05").get("hit") else "miss"


def _ev_n05a(ctx):
    return "reword_resolves" if _model_proposal(ctx, "D5a", "N05a").get("resolves_by_reword") \
        else "needs_identity_call"


def _ev_n05b(ctx):
    rec = _model_proposal(ctx, "D5b", "N05b")
    if rec.get("same_item"):
        target = ctx["candidate"].get("absorbed_into")
        if not target:
            raise GateRefusal("MERGE must carry absorbed_into = the surviving name (06 2 hard "
                              "ban, S12 refuses its absence)", node="N05b", exit_code=2,
                              gap_id="ABSORBED_INTO_MISSING")
        return "same_item"
    return "unresolved_ambiguity"


def _ev_n06(ctx):
    return "conflict" if _model_proposal(ctx, "D6", "N06").get("conflict") else "no_conflict"


def _ev_n06a(ctx):
    e = ctx["coverage_hits"][0]
    separable = bool(e.get("declared_scope")) and bool(e.get("trigger_anchors"))
    return "separable" if separable else "inseparable"


def _ev_n06b(ctx):
    j = ctx["candidate"].get("judge_decision")
    if j is None:
        raise NotLandedYet("kd_model_step (M3 judge)", "contracts.model_steps M3", node="N06b")
    return "authority_decidable" if j.get("authority") else "unresolved_conflict"


def _ev_n07(ctx):
    # presence side is decidable and reads ONLY the Evidence-layer carriers (M7). Violation side
    # has no mechanical implementation this round, so the diagnosis itself is [LLM].
    present = [e for e in ctx["coverage_hits"]
               if (e.get("use_count", 0) + e.get("view_count", 0)) > 0]
    if not present:
        ctx["prescreen"] = ("use==0 and view==0: the rule was never in the room, so 'ignored' "
                            "cannot be claimed -- that is D1/D3 territory")
        return "miss"
    return "ignored" if _model_proposal(ctx, "D7", "N07").get("violated_while_present") else "miss"


def _ev_n07a(ctx):
    e = ctx.get("hit_entry") or ctx["coverage_hits"][0]
    return "enforceable" if e.get("bound_to") else "not_enforceable"


def _ev_n08(ctx):
    return "hit" if _model_proposal(ctx, "D8", "N08").get("outdated") else "miss"


def _ev_n08a(ctx):
    e = ctx.get("hit_entry") or ctx["coverage_hits"][0]
    if not e.get("authority_is_machine_artifact"):
        raise GateRefusal("N08a: the authority is not a machine artifact, so only a human may "
                          "choose UPDATE / SUPERSEDE / DELETE -- the three-way is not this "
                          "node's to take", node="N08a", exit_code=2,
                          gap_id="HUMAN_TRIPLE_DECISION_REQUIRED")
    return "reverify_pass" if e.get("reverify_ok") else "reverify_fail"


def _ev_n09(ctx):
    declared = ctx["candidate"].get("declared_diagnoses_hit") or []
    routed = ctx.get("routed_diagnoses") or []
    if declared and set(declared) - set(routed):
        return "diagnosis_unrouted"      # a hit that produced no route: Stage 0 was skipped
    return "all_diagnoses_miss"


def _ev_n09b(ctx):
    p = ctx["candidate"].get("add_preconditions") or {}
    identity = ctx["candidate"].get("identity") or {}
    cond_c = bool(identity.get("l0_digest")) and bool(p.get("content_hash_differs"))
    if p.get("born_as_umbrella") and not p.get("preference_order_landed_on_create") and cond_c:
        ctx["disposition"] = "ADD"
        return "add_preconditions_hold"
    return "add_preconditions_fail"


def _ev_n10(ctx):
    scope = ctx["candidate"].get("scope") or {}
    missing = [k for k in ("workspace", "project", "layer") if not scope.get(k)]
    if missing or scope.get("layer") not in LAYERS:
        ctx["reject_reason"] = "scope incomplete %s or layer %r outside %s" % (
            missing, scope.get("layer"), list(LAYERS))
        return "scope_reject"
    ctx["scope"] = scope
    return "scope_ok"


def _ev_n11(ctx):
    ident = ctx["candidate"].get("identity") or {}
    digest = ident.get("l0_digest")
    if not digest:
        return "key_unresolvable"
    if ident.get("produced_by") == "model":
        ctx["reject_reason"] = "identity key was model-produced (06 3 forbids continuing on it)"
        return "key_unresolvable"
    if ident.get("produced_by") not in (None, "deterministic", "kd_identity_key"):
        raise GateRefusal("N11: identity digest came from %r" % ident.get("produced_by"),
                          node="N11", exit_code=2, gap_id="IDENTITY_ORIGIN_UNKNOWN")
    return "key_resolvable"


def _ev_n12(ctx):
    refs = ctx["candidate"].get("refs") or {}
    return "refs_dangling" if refs.get("dangling") else "refs_clean"


def _ev_n13(ctx):
    refs = ctx["candidate"].get("refs") or {}
    if refs.get("unresolved"):
        return "no_runner_pass"
    ev = ctx["candidate"].get("evidence") or []

    # SC01 owns forensic status; verification[] belongs to SC04 artifacts. A
    # captured UNVERIFIED observation is not a runner pass, and adding an
    # Artifact-shaped PASS label must not make it one. S12 independently
    # authenticates the complete observations through its source-host binding.
    import kd_validate as validate

    def runner_verified(e):
        if not isinstance(e, dict) or not validate.validate_artifact("evidence", e)["valid"] \
                or not prov.is_independent(e):
            return False
        status = e["evidence"]
        basis = status.get("status_basis")
        return status.get("status") == "VERIFIED" \
            and isinstance(basis, str) and bool(basis.strip())

    runner_pass = [e for e in ev if runner_verified(e)]
    return "runner_pass_present" if runner_pass else "no_runner_pass"


def _assert_not_rekeyed(ctx):
    """ESC-W2-01 (ROUND2_REOPEN_REQUIRED): a rekeyed Pattern is NOT promotable and the tree takes
    neither of the two candidate policies -- no carry-over, no reset."""
    ident = ctx["candidate"].get("identity") or {}
    rk = ident.get("rekey")
    if not rk:
        return
    before, after = rk.get("digest_before"), rk.get("digest_after")
    if not (before and after) or before == after:
        raise GateRefusal("N14: a rekey claim without both digests is not auditable (got %r/%r)"
                          % (before, after), node="N14", exit_code=2,
                          gap_id="ESC-W2-01/DIGESTS_NOT_RECORDED")
    ctx["rekey"] = {"digest_before": before, "digest_after": after,
                    "support_count_at_refusal": (ctx["candidate"].get("ledger") or {}).get(
                        "support_count"),
                    "escalation": "ESC-W2-01", "status": "ROUND2_REOPEN_REQUIRED",
                    "carry_over_chosen": False, "reset_chosen": False,
                    "note": "Round 2 never decided what happens to support_count when the Stage-3 "
                            "naming step changes the identity digest; the tree stops here instead "
                            "of picking one"}
    raise GateRefusal("N14: identity digest changed (%s -> %s) while support_count is attached to "
                      "the old digest; ESC-W2-01 is undecided, so this Pattern cannot promote"
                      % (before, after), node="N14", exit_code=2,
                      gap_id="ESC-W2-01/REKEY_PENDING_ADJUDICATION")


def _ev_n14(ctx):
    _assert_not_rekeyed(ctx)
    ledger = ctx["candidate"].get("ledger") or {}
    support = read_pattern_carrier(ledger, "support_count", "N14")
    minimum = threshold_for("N14", ctx["cfg"], "min_distinct_evidence")
    last = int(ledger.get("last_attempted_count", 0))
    ctx["counts_seen"] = {"support_count": support, "min": minimum,
                          "last_attempted_count": last}
    return "support_met" if support >= minimum and support > last else "support_below"


def _ev_n15(ctx):
    ledger = ctx["candidate"].get("ledger") or {}
    distinct = read_pattern_carrier(ledger, "distinct_occurrence_count", "N15")
    minimum = threshold_for("N15", ctx["cfg"], "min_independent_cohorts")
    ctx["counts_seen"]["distinct_occurrence_count"] = distinct
    return "occurrences_met" if distinct >= minimum else "occurrences_below"


def _ev_n16(ctx):
    counts = ctx["candidate"].get("counts") or {}
    tasks = threshold_for("N16", ctx["cfg"], "min_distinct_tasks")
    not_this = threshold_for("N16", ctx["cfg"], "min_tasks_not_this_session")
    if "distinct_tasks" not in counts or "tasks_not_this_session" not in counts:
        raise GateRefusal("N16 cannot decide: the candidate carries no task-span counts (%s)"
                          % sorted(counts), node="N16", exit_code=2,
                          gap_id="COUNTER_NOT_SUPPLIED")
    ok = counts["distinct_tasks"] >= tasks and counts["tasks_not_this_session"] >= not_this
    return "span_met" if ok else "span_below"


def _ev_n17(ctx):
    interval = threshold_for("N17", ctx["cfg"], "min_interval_hours")
    dig = ctx["candidate"].get("digest") or {}
    if "input_digest" not in dig or "hours_since_last_attempt" not in dig:
        raise GateRefusal("N17 cannot decide: no input digest / elapsed hours supplied",
                          node="N17", exit_code=2, gap_id="COUNTER_NOT_SUPPLIED")
    unchanged = dig.get("last_input_digest") == dig["input_digest"]
    due = (not unchanged) and dig["hours_since_last_attempt"] >= interval
    return "due" if due else "not_due"


def _ev_n18(ctx):
    form = ctx["candidate"].get("mechanical_form")
    if form not in CLASS_BY_MECHANICAL_FORM:
        raise GateRefusal("N18: mechanical_form %r is outside the three adjudicated classes"
                          % form, node="N18", exit_code=2, gap_id="FORM_NOT_DECLARED")
    ctx["landing_class"] = CLASS_BY_MECHANICAL_FORM[form]
    if form == "ci_evaluable":
        ctx["enforce_form"] = ctx["candidate"].get("enforce_form") or "test"
        if ctx["enforce_form"] not in CLASS_BY_ENFORCE_FORM:
            raise GateRefusal("N18: unknown enforce_form", node="N18", exit_code=2,
                              gap_id="FORM_NOT_DECLARED")
        ctx["landing_class"] = CLASS_BY_ENFORCE_FORM[ctx["enforce_form"]]
    if ctx.get("disposition") == "ARCHIVE":
        ctx["landing_class"] = "retire"
    return form


def _ev_n19(ctx):
    p = ctx["candidate"].get("pending") or {}
    if "draft" not in p or "sha256" not in p:
        raise GateRefusal("N19: the inert candidate carries no draft+sha256 pair (five elements "
                          "1+2)", node="N19", exit_code=2, gap_id="PENDING_INCOMPLETE")
    recomputed = prov.content_hash({"draft": p["draft"]})
    return "digest_intact" if recomputed == p["sha256"] else "digest_mismatch"


def _ev_n20(ctx):
    p = ctx["candidate"].get("pending") or {}
    taken = ctx["candidate"].get("pending_targets") or []
    return "pending_conflict" if p.get("target") in taken else "target_free"


def _ev_n21(ctx):
    p = ctx["candidate"].get("pending") or {}
    ttl = threshold_for("N21", ctx["cfg"], "pending_ttl_hours")
    watermark = p.get("watermark")
    if watermark is None or watermark <= (ctx["candidate"].get("ledger") or {}).get(
            "last_seen_watermark", -1):
        return "replay_or_expired"
    if p.get("age_hours", 0) >= ttl:
        return "replay_or_expired"
    ctx["watermark"] = watermark
    return "watermark_fresh"


def _ev_n22(ctx):
    p = ctx["candidate"].get("pending") or {}
    rej = p.get("prior_rejection")
    if not rej:
        return "admissible"
    support = (ctx["candidate"].get("ledger") or {}).get("support_count")
    if support is None or support <= rej.get("support_count", 0):
        return "rejected_without_new_evidence"   # a human said no; re-proposing needs new evidence
    return "admissible"


def _ev_n22b(ctx):
    draft = ctx["candidate"].get("model_draft")
    if draft is None:
        raise NotLandedYet("kd_model_step (M2 root-cause abstraction)",
                           "contracts.model_steps M2", node="N22b")
    if draft.get("produced_by") != "model":
        raise GateRefusal("N22b is the model's one proposal slot; a non-model draft belongs to a "
                          "deterministic node", node="N22b", exit_code=2,
                          gap_id="WRONG_AUTHOR")
    if draft.get("adjudication"):
        raise GateRefusal("N22b: a model draft may not adjudicate its own tier", node="N22b",
                          exit_code=2, gap_id="MODEL_NO_ADJUDICATION")
    if not draft.get("executable_assertion"):
        raise GateRefusal("N22b refused: the draft is prose for a human to read, not an "
                          "executable-assertion candidate (DD-1 stance B failure mode)",
                          node="N22b", exit_code=2, gap_id="DRAFT_IS_PROSE")
    ctx["draft_size_bytes"] = len(draft.get("body", "").encode("utf-8"))
    ctx["draft_tier_proposal"] = draft.get("tier_proposal")
    return "draft_proposed"


def _ev_n23(ctx):
    target = ctx["candidate"].get("write_target") or {}
    persistent = ctx.get("disposition") in ("ARCHIVE", "RESTORE") or bool(target.get("resident_layer")) or ctx.get("landing_class") in (
        "skill", "rule")
    return "touches_persistent" if persistent else "not_persistent"


def _ev_n24(ctx):
    claim = ctx["candidate"].get("unattended_claim") or {}
    for key in ("mechanically_decidable", "reversible", "idempotent_self_authored"):
        if key not in claim:
            raise GateRefusal("N24: the unattended claim does not state %s" % key, node="N24",
                              exit_code=2, gap_id="CLAIM_INCOMPLETE")
    if claim.get("physical_delete"):
        raise GateRefusal("N24: a physical delete may never take the unattended branch (06 5 "
                          "tightening; archive is the ceiling)", node="N24", exit_code=2,
                          gap_id="PHYSICAL_DELETE_REFUSED")
    all_three = all(claim[k] for k in ("mechanically_decidable", "reversible",
                                       "idempotent_self_authored"))
    if all_three:
        # The R0 branch exists structurally but is not authorised yet: DEF-1 (DD-1-sub01) decides
        # whether R0 may exist at all and DEF-3 (DD-1-sub03) whether the admitted action set may
        # go past 11's T0 six actions, which no available slice enumerates.
        node = NODE_BY_ID["N24"]
        raise GateRefusal("N24: all three conditions hold, but the admitted unattended action set "
                          "is undecided -- %s" % node["deferred"][1], node="N24", exit_code=2,
                          deferred_id=node["deferred"][0], gap_id="IMPLEMENTATION_GAP / DEFERRED")
    return "needs_human"


def _s17_decision(ctx):
    """RH-P0-05: the human decision is a TRUSTED input that reaches S10 only via the
    `approval_context` parameter (G1's output). It is NEVER read off the untrusted candidate -- a
    candidate carrying `human_decision` was stripped at the adjudicate entry and is ignored. No
    approval_context means G1 has not produced a trusted decision, so N25 fails closed rather than
    accepting a self-approval. (S12 kd_write_txn.verify_g1_approvals re-verifies the G1 approval
    rows by digest before any durable byte; that is the authoritative write-time enforcement.)"""
    ac = ctx.get("approval_context")
    if ac is None:
        raise NotLandedYet("kd_human_gate (G1) approval_context", "trusted G1 approval", node="N25")
    if not isinstance(ac, dict):
        raise GateRefusal("N25: approval_context must be a G1 decision object, got %r"
                          % type(ac).__name__, node="N25", exit_code=2,
                          gap_id="APPROVAL_CONTEXT_MALFORMED")
    return ac


def _ev_n25(ctx):
    d = _s17_decision(ctx)
    scope = ctx.get("scope") or ctx["candidate"].get("scope") or {}
    tier = d.get("risk_tier") or ("R2" if ctx.get("disposition") in ("DELETE", "MERGE", "RESTORE") else "R1")
    if ctx.get("disposition") in ("DELETE", "MERGE", "RESTORE") and tier != "R2":
        raise GateRefusal("N25: destructive disposition cannot be downgraded to R1",
                          node="N25", exit_code=2, gap_id="RISK_TIER_DOWNGRADE")
    if d.get("approved") is not True:
        return "refused"
    if tier == "R2" and d.get("confirmation_flag") is not True:
        raise GateRefusal("N25 R2: the confirmation flag is part of the contract, not a courtesy",
                          node="N25", exit_code=2, gap_id="CONFIRMATION_FLAG_MISSING")
    if tier not in ("R1", "R2"):
        raise GateRefusal("N25: risk tier %r is outside R1/R2" % tier, node="N25", exit_code=2,
                          gap_id="RISK_TIER_UNKNOWN")
    if scope.get("layer") == "global":
        second = d.get("second_approver")
        if not second or second == d.get("approver"):
            raise GateRefusal("N25: L-RULE-GLOBAL needs the explicit second human gate by a "
                              "different approver (06 5.1); got approver=%r second=%r"
                              % (d.get("approver"), second), node="N25", exit_code=2,
                              gap_id="SECOND_GATE_MISSING")
        ctx["second_gate"] = {"approver": d.get("approver"), "second_approver": second}
    view = ctx["candidate"].get("approval_view") or {}
    if view:
        if view.get("over_budget") and not view.get("budget_owner"):
            raise GateRefusal("N25: the approval view is over budget with no named budget owner -- "
                              "CM-31 puts the budget with S18 and the view may not bypass it",
                              node="N25", exit_code=2, gap_id="BUDGET_OWNER_MISSING")
        ctx["approval_view_size_bytes"] = len(view.get("rendered", "").encode("utf-8"))
    ctx["human_approved"] = True
    ctx["risk_tier"] = tier
    return "approved"


def _ev_n26(ctx):
    target = ctx["candidate"].get("write_target") or {}
    if target.get("collides_with_human_authored"):
        # DEF-6 (DD-1-sub06) is open: 09's install() override/refuse semantics were never read
        # past the empty-paths raise, so a collision has no decided behaviour and cannot proceed.
        raise GateRefusal("N26: candidate slug collides with a human-authored skill and the "
                          "override/refuse semantics are unresolved (DEF-6, DD-1-sub06: 09's "
                          "install() was only read as the empty-paths raise)",
                          node="N26", exit_code=2, deferred_id="DD-1-sub06",
                          gap_id="IMPLEMENTATION_GAP / DEFERRED")
    if ctx.get("disposition") == "MERGE" and not ctx["candidate"].get("absorbed_into"):
        raise GateRefusal("N26: MERGE without absorbed_into is refused by S12 as well",
                          node="N26", exit_code=2, gap_id="ABSORBED_INTO_MISSING")
    if ctx["candidate"].get("mutation", {}).get("to_state") == "deleted":
        raise GateRefusal("N26: to == 'deleted' is unreachable from the write path", node="N26",
                          exit_code=2, gap_id="DESTRUCTIVE_CEILING")
    ctx["staged_intent"] = build_intent(ctx)
    ctx["score_guard"] = run_score_guard(ctx["staged_intent"], ctx)
    return "write_staged"


def _ev_n27(ctx):
    t = ctx["candidate"].get("transaction") or {}
    approve_row = t.get("approve_event")
    apply_rows = t.get("apply_rows")
    if not approve_row or not apply_rows:
        return "intent_incomplete"  # nothing was submitted; do not claim a rollback
    if len(t.get("ledger_events", [])) != 1:
        raise GateRefusal("N27: one batch op writes exactly one lifecycle_event row (05 2)",
                          node="N27", exit_code=2, gap_id="LEDGER_CARDINALITY")
    ctx["transaction_bundle"] = {"approve_event": approve_row, "apply_rows": list(apply_rows),
                                 "ledger_events": list(t["ledger_events"])}
    return "intent_ready"  # S12 is the only authoritative committer


def _ev_n28(ctx):
    # RH-P0-06: the eval verdict is a TRUSTED input that reaches S10 only via the `eval_verdict`
    # parameter (S16's output), never off the untrusted candidate (candidate.eval_result was
    # stripped at entry). Chain: S15 -> S16 -> trusted EvalVerdict -> S10.
    r = ctx.get("eval_verdict")
    if r is None:
        raise NotLandedYet("kd_eval_freeze / kd_eval_score (S15/S16)",
                           "contracts.scripts S15, S16", node="N28")
    import kd_eval_score as s16
    try:
        s16.assert_verified(r)
    except s16.NotVerified as exc:
        raise GateRefusal("N28: S16 refused the SC09 score document", node="N28",
                          exit_code=2, gap_id="EVAL_NOT_VERIFIED") from exc
    subject = r["subject"]["promoted_from_artifact_id"]
    if subject != (ctx["candidate"].get("artifact_id") or ctx["candidate"]["candidate_id"]):
        raise GateRefusal("N28: eval belongs to a different artifact", node="N28",
                          exit_code=2, gap_id="EVAL_SUBJECT_MISMATCH")
    ctx["eval_status"] = "full"
    return "regression_pass"


def _ev_n29(ctx):
    """The only real consumer of scope.layer: project and global are two different exits."""
    forced = ctx.pop("forced_landing", None)
    if forced:
        return forced
    disposition = ctx.get("disposition", "ADD")
    klass = ctx.get("landing_class") or "rule"
    if klass == "enforceable":
        klass = ctx.get("enforce_form", "test")
    key = (disposition, klass)
    if key not in LANDING_ROUTER:
        raise GateRefusal("N29: no landing for disposition=%s class=%s (06 5.1 does not route it)"
                          % key, node="N29", exit_code=2, gap_id="LANDING_NOT_ROUTED")
    landing = LANDING_ROUTER[key]
    if landing != "RULE_LAYER":
        return landing
    scope = ctx.get("scope") or ctx["candidate"].get("scope") or {}
    layer = scope.get("layer")
    if layer not in RULE_LAYERS:
        raise GateRefusal("scope.layer=%r is not a standing-preference layer, so there is no rule "
                          "landing for it (05 5.3 S3/S4; L-RULE-PROJECT and L-RULE-GLOBAL are the "
                          "only two)" % layer, node="N29", exit_code=2,
                          gap_id="SCOPE_LAYER_NOT_A_RULE_LAYER")
    ctx["layer_consumer"] = {"read": "scope.layer", "value": layer,
                             "decides": "which of the two rule exits"}
    return RULE_LAYERS[layer]


NODE_BY_ID = {n["id"]: n for n in NODE_TABLE}
EDGE_BY_SRC = {}
for _e in EDGE_TABLE:
    EDGE_BY_SRC.setdefault(_e[0], []).append(_e)
#: an edge into N29 that names its landing forces that exit; dispositions name an action
FORCED_LANDING = {(e[0], e[1]): e[3] for e in EDGE_TABLE if len(e) > 3}

EVALUATORS = {
    "N00": _ev_n00, "N01": _ev_n01, "N02": _ev_n02, "N03": _ev_n03, "N04": _ev_n04,
    "N05": _ev_n05, "N05a": _ev_n05a, "N05b": _ev_n05b, "N06": _ev_n06, "N06a": _ev_n06a,
    "N06b": _ev_n06b, "N07": _ev_n07, "N07a": _ev_n07a, "N08": _ev_n08, "N08a": _ev_n08a,
    "N09": _ev_n09, "N09b": _ev_n09b,
    "N10": _ev_n10, "N11": _ev_n11, "N12": _ev_n12, "N13": _ev_n13, "N14": _ev_n14,
    "N15": _ev_n15, "N16": _ev_n16, "N17": _ev_n17, "N18": _ev_n18,
    "N19": _ev_n19, "N20": _ev_n20, "N21": _ev_n21, "N22": _ev_n22, "N22b": _ev_n22b,
    "N23": _ev_n23, "N24": _ev_n24, "N25": _ev_n25, "N26": _ev_n26, "N27": _ev_n27,
    "N28": _ev_n28, "N29": _ev_n29,
}


def _take_edge(node_id, condition):
    for e in EDGE_BY_SRC[node_id]:
        if e[1] == condition:
            return e
    raise GateRefusal("%s returned condition %r which is not one of its declared branches %s"
                      % (node_id, condition, [e[1] for e in EDGE_BY_SRC[node_id]]),
                      node=node_id, exit_code=2, gap_id="UNKNOWN_CONDITION")


# --------------------------------------------------------------------- the two entry points
def adjudicate(candidate, cfg=None, artifact_root="store", *, approval_context=None,
               eval_verdict=None):
    """Walk the tree for ONE candidate and return its per-item verdict plus the decision trace.

    RH-P0-05/06 trust boundary: `candidate` is UNTRUSTED DOMAIN INPUT. The human approval and the
    eval verdict are TRUSTED outputs of G1 and S16 and arrive ONLY as the independent
    `approval_context` / `eval_verdict` parameters -- never as candidate fields. Any trusted-
    decision key the candidate smuggles (human_decision, eval_result, human_approved, ...) is
    stripped on entry and recorded in the verdict's `ignored_untrusted_keys`, so a candidate can
    neither self-approve nor self-eval. S12 re-verifies the G1 approval rows and the S16 verdict
    again before any durable byte; S10's job is to never let the candidate speak for G1/S16.

    Exit codes follow the S10 contract row: 3 = not promoted (a normal terminal state), 2 = the
    thresholds and the policy are not same-source or Stage 0 was skipped/refused.
    """
    if cfg is None:
        import kd_gate
        cfg = kd_gate.load_config()
    if not isinstance(candidate, dict) or not candidate.get("candidate_id"):
        raise GateRefusal("adjudicate takes ONE candidate with a candidate_id -- CM-27: one "
                          "verdict per item, a set is not an input", exit_code=2,
                          gap_id="PER_ITEM_VERDICT_REQUIRED")
    # strip untrusted impersonation of a trusted decision; rebuild the dict so the caller's
    # candidate is never mutated (the old code wrote c["human_decision"] back into it)
    ignored = sorted(k for k in UNTRUSTED_DECISION_KEYS if k in candidate)
    candidate = {k: v for k, v in candidate.items() if k not in UNTRUSTED_DECISION_KEYS}
    ctx = {"candidate": candidate, "cfg": cfg, "artifact_root": artifact_root, "trace": [],
           "hits_found": [], "routed_diagnoses": [], "llm_calls": 0,
           "landing_class": candidate.get("landing_class"),
           "approval_context": approval_context, "eval_verdict": eval_verdict,
           "ignored_untrusted_keys": ignored}
    node = "N00"
    result = None
    while True:
        ctx["node"] = node
        try:
            condition = EVALUATORS[node](ctx)
        except GateRefusal as exc:
            ctx["trace"].append({"node": node, "judge": NODE_BY_ID[node]["judge"],
                                 "outcome": "refusal", "reason": str(exc),
                                 "exit_code": exc.exit_code, "deferred_id": exc.deferred_id,
                                 "gap_id": exc.gap_id})
            result = _finish(ctx, exit_code=exc.exit_code, refusal=exc)
            break
        edge = _take_edge(node, condition)
        ctx["trace"].append({"node": node, "judge": NODE_BY_ID[node]["judge"],
                             "condition": edge[1], "to": edge[2]})
        # bookkeeping Stage 0 needs to prove it did not skip a diagnosis
        if edge[2] in ("N23", "N19"):
            ctx["routed_diagnoses"].append(node)
            if ctx.get("disposition") not in ("ARCHIVE", "RESTORE"):
                ctx["disposition"] = FORCED_LANDING.get((node, condition), "ADD")
        forced = FORCED_LANDING.get((node, condition))
        if forced and edge[2] == "N29" and isinstance(forced, str) and forced.startswith("L-"):
            ctx["forced_landing"] = forced
        node = edge[2]
        if node in LANDINGS:
            result = _finish(ctx, exit_code=exit_code_for(node), landing=node)
            break
        if node in REFUSALS:
            reason = ("REROOT: the canonical L0 identity key is not obtainable, Stage 1 collapses "
                      "and DD-1 must be reopened (06 7)" if node == "R-REROOT" else
                      "Stage 0 declared a diagnosis that was never routed -- the tree refuses "
                      "rather than counting past it")
            result = _finish(ctx, exit_code=2, refusal=GateRefusal(reason, node=node,
                                                                   gap_id=node))
            break
    verdict = build_verdict(ctx, result)
    run_score_guard(verdict, ctx)
    return dict(result, verdict=verdict)


def exit_code_for(landing):
    return 3 if landing in ("L-PATTERN", "L-NOTHING", "L-NOTHING+LEDGER", "L-ARCHIVE") else 0


def _finish(ctx, exit_code, landing=None, refusal=None):
    out = {
        "candidate_id": ctx["candidate"].get("candidate_id"),
        "trace": ctx["trace"],
        "exit_code": exit_code,
        "landing": landing,
        "disposition": ctx.get("disposition"),
        "nodes_visited": [t["node"] for t in ctx["trace"]],
        "stage0_entry": ctx["trace"][0]["node"],
        "llm_diagnosis_inputs_consumed": ctx["llm_calls"],
        "layer_consumer": ctx.get("layer_consumer"),
        "rekey": ctx.get("rekey"),
        "counts_seen": ctx.get("counts_seen"),
        "llm_calls": ctx.get("llm_calls", 0),
        "risk_tier": ctx.get("risk_tier"),
        "second_gate": ctx.get("second_gate"),
        "staged_intent": ctx.get("staged_intent"),
        "transaction_bundle": ctx.get("transaction_bundle"),
        "eval_status": ctx.get("eval_status"),
        # RH-P0-05/06 observability (internal result, NOT part of the SC12 verdict record): the
        # trusted-decision keys the untrusted candidate tried to smuggle and that were stripped.
        "ignored_untrusted_keys": ctx.get("ignored_untrusted_keys") or [],
        "refusal": None if refusal is None else {
            "reason": refusal.reason, "node": refusal.node, "deferred_id": refusal.deferred_id,
            "gap_id": refusal.gap_id},
    }
    return out


ITEM_VERDICT_BY_LANDING = {
    "L-PATTERN": "HOLD_AT_PATTERN", "L-NOTHING": "DROP_SILENT",
    "L-NOTHING+LEDGER": "DROP_WITH_LEDGER", "L-ARCHIVE": "RETIRE_TO_ARCHIVE",
    "L-TEST": "PROMOTE", "L-LINT": "PROMOTE", "L-SCRIPT": "PROMOTE", "L-EVAL": "PROMOTE",
    "L-SKILL": "PROMOTE", "L-RULE-PROJECT": "PROMOTE", "L-RULE-GLOBAL": "PROMOTE",
}


def build_verdict(ctx, result):
    """The SC12 record. One candidate in, one verdict out -- CM-27."""
    landing = result["landing"]
    item_verdict = "REFUSE" if landing is None else ITEM_VERDICT_BY_LANDING[landing]
    return {
        "schema": "kd-verdict/1",
        "candidate_id": result["candidate_id"],
        "item_verdict": item_verdict,
        "terminal_landing": landing,
        "disposition": result["disposition"],
        "exit_code": result["exit_code"],
        "decision_path": result["trace"],
        "scope": ctx["candidate"].get("scope"),
        "identity_digest": (ctx["candidate"].get("identity") or {}).get("l0_digest"),
        "counters": {"carrier": "pattern",
                     "support_count": (result.get("counts_seen") or {}).get("support_count"),
                     "distinct_occurrence_count": (result.get("counts_seen") or {}).get(
                         "distinct_occurrence_count")},
        "human_approved": bool(ctx.get("human_approved")),
        "risk_tier": result["risk_tier"],
        "second_human_gate": result["second_gate"],
        "absorbed_into": ctx["candidate"].get("absorbed_into"),
        "rekey_pending": result["rekey"],
        "refusal": result["refusal"],
        "approval_view_size_bytes": ctx.get("approval_view_size_bytes"),
        "draft_size_bytes": ctx.get("draft_size_bytes"),
        "llm_diagnosis_inputs_consumed": result["llm_calls"],
        "not_promoted_reason": None if landing not in ("L-PATTERN", "L-NOTHING",
                                                       "L-NOTHING+LEDGER") else
        "gate closed at the first unmet condition in decision_path",
    }


def build_intent(ctx):
    """The promotion-shaped payload handed to S12. It is guarded before it is ever returned."""
    return {
        "artifact_id": ctx["candidate"].get("artifact_id") or ctx["candidate"]["candidate_id"],
        "op": ctx.get("disposition", "ADD"),
        "record": {"candidate_id": ctx["candidate"]["candidate_id"],
                   "scope": ctx["candidate"].get("scope"),
                   "landing": ctx.get("landing_class"),
                   "state": "candidate", "produced_by": "deterministic"},
        "mutation": dict(ctx["candidate"].get("mutation") or {},
                         to_state=(ctx["candidate"].get("mutation") or {}).get("to_state", "active")),
        "reason": "gate decision path %s" % "->".join(t["node"] for t in ctx["trace"]),
    }


def run_score_guard(payload, ctx):
    """S07's Tier-3 proxy score may never enter a promotion record. Wired here, not shipped dead.

    The import is lazy on purpose: kd_proxy_candidates imports kd_gate, which imports this module.
    """
    import kd_proxy_candidates as proxy
    scores = ctx["candidate"].get("proxy_scores") or ()
    proxy.assert_not_promotion_payload(payload, scores=scores)
    return {"guard": "kd_proxy_candidates.assert_not_promotion_payload", "called_on": True,
            "scores_supplied": len(list(scores))}


def assert_per_item_verdict(records):
    """CM-27 guard: refuse a batch-shaped verdict, accept only one verdict per candidate."""
    if isinstance(records, dict):
        records = [records]
    seen = set()
    for rec in records:
        if not isinstance(rec, dict):
            raise PerItemVerdictViolation("a verdict must be an object per candidate, got %r" % rec)
        bad = [k for k in BATCH_FORBIDDEN_KEYS if k in rec]
        if bad:
            raise PerItemVerdictViolation("CM-27: batch-level keys %s in a verdict -- one verdict "
                                          "per candidate, never one verdict for a set" % bad)
        word = str(rec.get("item_verdict", "")).lower()
        if word in BATCH_FORBIDDEN_WORDS:
            raise PerItemVerdictViolation("CM-27: item_verdict %r is a batch pass/fail word" % word)
        if rec.get("item_verdict") not in ITEM_VERDICTS:
            raise PerItemVerdictViolation("item_verdict %r is outside %s"
                                          % (rec.get("item_verdict"), ITEM_VERDICTS))
        cid = rec.get("candidate_id")
        if not cid:
            raise PerItemVerdictViolation("a verdict without candidate_id cannot be per-item")
        if cid in seen:
            raise PerItemVerdictViolation("two verdicts for one candidate %s" % cid)
        seen.add(cid)
    return len(records)


# ------------------------------------------------------------------ Stage 1's counting subset
def evaluate_counting(evidence, cfg, artifact_root="store"):
    """The Wave 0 kernel surface: Stage 1's two counting nodes (N14, N15), same keys, same maths.

    Deliberately NOT a promotion decision: it never reaches N16/N17, whose thresholds the single
    constants file does not carry, and it does not run Stage 0. `adjudicate` is the authoritative
    S10 surface; this exists because kd_write_txn re-runs `kd_gate.evaluate_promotion` on the
    evidence it is handed and the frozen kernel's decision keys must keep their meaning.
    """
    support = prov.independent_support(evidence or [], artifact_root)
    required_items = threshold_for("N14", cfg, "min_distinct_evidence")
    required_cohorts = threshold_for("N15", cfg, "min_independent_cohorts")
    promotable = (support["independent_cohort_count"] >= required_cohorts
                  and support["distinct_evidence_count"] >= required_items)
    return {
        "support": support,
        "required_independent_cohorts": required_cohorts,
        "required_distinct_evidence": required_items,
        "promotable": promotable,
        "reason": None if promotable else (
            f"independent cohorts {support['independent_cohort_count']}<{required_cohorts} or "
            f"distinct evidence {support['distinct_evidence_count']}<{required_items}"),
        "tree_nodes": ["N14", "N15"],
        "tree_stage": STAGE_NAMES[1],
        "full_adjudication": False,
    }


def structure_json():
    """Machine-readable shape of the tree, for reports and for the node-coverage test."""
    return {"counts": count_structure(), "problems": validate_structure(),
            "nodes": [{"id": n["id"], "stage": n["stage"], "judge": n["judge"],
                       "branches": len(EDGE_BY_SRC[n["id"]]),
                       "threshold_keys": list(n.get("threshold_keys", ())),
                       "deferred_id": (n.get("deferred") or (None,))[0]} for n in NODE_TABLE]}


def main(argv=None):
    import argparse
    import json
    ap = argparse.ArgumentParser(description="S10 promotion decision tree structure.")
    ap.add_argument("--structure", action="store_true", help="print node/branch counts from data")
    ap.add_argument("--adjudicate", metavar="CANDIDATE_JSON",
                    help="adjudicate one candidate file and print the verdict")
    ap.add_argument("--policy", metavar="FILE",
                    help="explicit admitted runtime policy required for --adjudicate; no default")
    ap.add_argument("--approval-context", metavar="FILE",
                    help="trusted G1 approval decision (RH-P0-05); a candidate field is ignored")
    ap.add_argument("--eval-verdict", metavar="FILE",
                    help="trusted S16 eval verdict (RH-P0-06); a candidate field is ignored")
    args = ap.parse_args(argv)
    if args.adjudicate:
        if not args.policy:
            ap.error("--adjudicate requires an explicit --policy")
        import kd_gate
        import kd_provenance as prov
        try:
            cfg = kd_gate.load_runtime_policy(args.policy)
        except prov.SchemaError as exc:
            print(json.dumps({"status": "REFUSED", "reason": str(exc)}, ensure_ascii=False))
            return 2
        def strict_json(path):
            import math

            def unique(pairs):
                result = {}
                for key, value in pairs:
                    if key in result:
                        raise ValueError("duplicate input JSON key")
                    result[key] = value
                return result

            def nonfinite(_value):
                raise ValueError("nonfinite JSON constant")

            def finite_float(value):
                parsed = float(value)
                if not math.isfinite(parsed):
                    raise ValueError("nonfinite JSON float")
                return parsed

            with open(path, encoding="utf-8") as fh:
                return json.load(fh, object_pairs_hook=unique,
                                 parse_constant=nonfinite, parse_float=finite_float)

        try:
            try:
                candidate = strict_json(args.adjudicate)
                approval_context = (strict_json(args.approval_context)
                                    if args.approval_context else None)
                eval_verdict = (strict_json(args.eval_verdict)
                                if args.eval_verdict else None)
            except (OSError, UnicodeError, ValueError, RecursionError, OverflowError) as exc:
                raise GateRefusal("S10_INPUT_INVALID: candidate, approval or Eval JSON is "
                                  "unreadable or malformed", gap_id="S10_INPUT_INVALID") from exc
            res = adjudicate(candidate, cfg=cfg, approval_context=approval_context,
                             eval_verdict=eval_verdict)
        except GateRefusal as exc:
            print(json.dumps({"status": "REFUSED", "reason": exc.reason,
                              "node": exc.node, "gap_id": exc.gap_id,
                              "deferred_id": exc.deferred_id,
                              "exit_code": exc.exit_code}, ensure_ascii=False))
            return exc.exit_code
        print(json.dumps(res["verdict"], ensure_ascii=False, indent=2))
        return res["exit_code"]
    if args.policy:
        ap.error("--policy requires --adjudicate")
    print(json.dumps(structure_json(), ensure_ascii=False, indent=2))
    return 0 if not validate_structure() else 1


if __name__ == "__main__":
    raise SystemExit(main())
