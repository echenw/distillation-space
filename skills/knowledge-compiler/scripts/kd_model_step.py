#!/usr/bin/env python3
"""M1-M4 model-step envelope -- contract, bounded context, deterministic output validation.

This module is the boundary where Knowledge Compiler stops being deterministic. It
holds a *contract*, not a runtime: it imports no network or model client, calls no client,
and writes nothing. The model is a callable the HOST injects (`responder`), and everything
that callable returns is treated as untrusted input until the deterministic checks below
pass (Round 2 `04` §1 I-2/I-3, `.distill/round-2/04-DETERMINISTIC-VS-LLM.md:16-19`).

What it enforces, and where each rule comes from:

  I-2  模型无写权: 只有只读/提案通道 (`04:17`). Every successful answer becomes a
       PROPOSAL object carrying `produced_by.kind == "model"` and `rights ==
       "proposal-only"`. This module exposes no write function at all -- it does not even
       import `kd_write_txn`, so there is no alternative route to reach (the only durable
       write path stays `S12 kd_write_txn.commit_batch`, and `kd_gate.apply_mutation`
       refuses a `produced_by == "model"` payload without `human_approved`).
  I-1  模型产出的任何标识符，未经代码 canonicalize + 内容寻址派生，不得进入任何计数器或门
       (`04:16`). Model-supplied identifiers are kept in `payload` (raw) and only the
       S05-derived block in `canonicalized` is what a downstream gate may read.
  I-3  失败保留原输出并如实标失败 (`04:18`); the ONE bounded repair retry is `04:77` C1
       (`maxRetries=1`, re-run through the SAME deterministic gate), never a second schema.
  row 5 (`04:51`)  M1 judges only inside S07's candidate set; candidate generation itself
       stays in the deterministic layer.
  row 7 / row 9 / row 12 (`04:53`, `04:55`, `04:58`)  M2 / M3 / M4 contracts.
  row 16 (`04:63`)  provenance verification is deterministic and primary; the model is
       never used to prove a citation, so every cited ref is re-checked by S14 here.

Zero-LLM posture (`04:113-129`): with no injected callable -- or when a step's own
precondition is not met (empty candidate set, no conflict alert, count gate not cleared,
S15 corpus absent) -- the step returns an explicit `NO_PROPOSAL` naming the missing input.
Never an empty success, never a fabricated answer, never an exception the deterministic
chain would have to catch.

Stdlib only. Read-only by construction: no `open(..., "w")`, no rename/replace/fsync, no
`kd_write_txn` import. `python3 kd_write_txn.py --audit` stays exit 0 because of that.
"""
from __future__ import annotations

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import kd_identity_key as ident              # noqa: E402  S05: canonical identity
import kd_provenance as prov                 # noqa: E402  wave 0 kernel (frozen, imported)
import kd_provenance_stamp as stamp          # noqa: E402  S13: write-time provenance stamp
import kd_proxy_candidates as proxy          # noqa: E402  S07: tier-3 containment guard
import kd_refs_audit as refs                 # noqa: E402  S14: evidence ref integrity

# --------------------------------------------------------------------- statuses
PROPOSAL = "PROPOSAL"
NO_PROPOSAL = "NO_PROPOSAL"
REFUSED = "REFUSED_MODEL_OUTPUT"

#: Round 2's only human position; a model payload may never set it (`12:137`).
HUMAN_APPROVAL_FIELD = "human_approved"

#: The envelope's own answer when nothing was injected -- a named status, not an error.
ZERO_LLM_EXITS = {
    "M1": "保留双条目 + possible_duplicate 标记，永不自动合并（`12:133`、`04:122`）",
    "M2": "落 `04` 最低层阶梯（注释/引用/文档），不泛化（`12:134`、`04:123`）",
    "M2b": "无模型即不命名：Pattern 保留 S05 派生的确定性 key（`pat-<pattern_id>`），不猜人类可读名、"
           "不泛化（`04:119`、`04:52` C3）",
    "M3": "记 unresolved_conflict，交人类批处理（`12:135`、`04:124`）",
    "M4": "只跑结构断言与确定性打分，标 eval_status: partial（`12:136`、`04:125`）",
}

#: `04` §5 records that this environment cannot pin which model answered.
MODEL_IDENTITY_STANCE = {
    "execution_model_controlled": False,
    "meaning": "the host, not this package, decides which model answers; nothing here "
               "selects, pins or claims a model",
    "model_id_source": "host-supplied kd_provenance_stamp.RuntimeFacts.model_id, recorded "
                       "verbatim or left None on the zero-LLM path",
    "host_must_supply": ("a callable matching the responder contract below",
                         "RuntimeFacts (round_id, pass_id, compiler_version, config_sha, "
                         "actor) for the S13 stamp",
                         "a kd_refs_audit.RootRegistry if cited refs must be re-resolved"),
}


class StepContractError(Exception):
    """Programmer error: an unknown step id or a malformed context bundle. Raised, because
    silently answering a step that does not exist would mint a fifth model position
    (`12:129` 'Round 3 不得增加第五个')."""


class EnvelopeRefusal(Exception):
    """A model answer that failed the deterministic checks. Never escapes `run_model_step`:
    it is converted into a REFUSED result that carries the original output verbatim (I-3).
    """

    def __init__(self, code, message, detail=None):
        Exception.__init__(self, message)
        self.code, self.message, self.detail = code, message, (detail or {})


# --------------------------------------------------------------------- step contracts
#: `06` §5.1 landing points (`06:256-271`) that a PROPOSAL may name. `L-ARCHIVE` and the
#: destructive routes are deliberately absent: M2 proposes, it does not retire anything.
M2_LANDING_TIERS = ("L-PATTERN", "L-NOTHING", "L-NOTHING+账", "L-SCRIPT", "L-LINT",
                    "L-TEST", "L-EVAL", "L-SKILL", "L-RULE-PROJECT", "L-RULE-GLOBAL")

#: Keys no step may ever carry in its payload: write authority, approval, gate verdicts.
FORBIDDEN_UNIVERSAL = ("human_approved", "approved", "approved_by", "promotable",
                       "write", "write_now", "commit", "delete", "removed",
                       "provenance", "generation", "actor", "stamp_digest")

STEP_CONTRACTS = {
    "M1": {
        # IMPLEMENTATION_GAP: the verdict LABELS below are this envelope's naming. Round 2
        # adjudicated the semantic (`04:51` "Already Covered 含不同措辞" is a semantic judgment question)
        # but never a label set, and D6-a leaves the canonical field/hash choice open, so M1
        # stays advisory-only: no merge, ever（`12:133`）.
        # / DEFERRED id DD-6-sub45 (`04` §9 D6-a) with DD-2-sub16 (自动合并未启用)
        "title": "语义判重",
        "pipeline_step": "#11",
        "matrix_row": "`04` 行 5 判定层（`04:51`）",
        "required_context": ("candidate_pairs", "scope"),
        "precondition": "S07 produced a non-empty candidate set（`12:115` exit 0=空集⇒下游跳过 M1）",
        "payload_required": ("step", "pair_verdicts"),
        "enums": {"pair_verdicts.verdict": ("same_principle", "not_same_principle",
                                            "already_covered_paraphrase", "undecided")},
        "extra_forbidden": ("merged", "merge_into", "canonical_winner", "merged_ids"),
        "effect": "advisory_only: possible_duplicate marker, never a merge（`12:133`）",
        "advisory_only": True,
    },
    "M2": {
        "title": "根因抽象与写作",
        "pipeline_step": "#12",
        "matrix_row": "`04` 行 7 主力 + 行 6 ◐ 命名（`04:53`、`04:52`、C3/C4 `04:79-80`）",
        "required_context": ("grouped_pattern", "count_gate", "scope"),
        "precondition": "必须排在 #13 计数门之后（`12:134`）",
        "payload_required": ("step", "pattern_id", "abstract_statement",
                             "candidate_rule_body", "landing_tier", "evidence_ids", "claims"),
        "enums": {"landing_tier": M2_LANDING_TIERS},
        "extra_forbidden": ("merged_ids", "supersede_now", "state"),
        "effect": "proposal text only; the pattern name is a PROPOSAL and exists only after "
                  "S05 canonicalizes it（`04:52` C3、`12:239` item 3）",
        "advisory_only": False,
    },
    "M2b": {
        # Round 2's authoritative contract set has FIVE model steps (contracts.json
        # `model_steps`, `12:241`): M2b is the Pattern-naming half-cell (matrix 行 6 的 ◐) that
        # Round 3 left unimplemented (SKILL.md §9.2). Implementing it in Round 4 COMPLETES the
        # contract; it is not a new position -- `12:129` bars ADDING a step beyond the contract
        # set, and M2b is inside it. M2 (行 7) writes the abstraction; M2b (行 6 ◐) proposes
        # exactly ONE human-readable name for a pattern the identity pipeline already minted.
        "title": "Pattern 命名",
        "pipeline_step": "#12b",
        "matrix_row": "`04` 行 6 的 ◐ 命名（`04:52` C3、`12:241`）",
        "required_context": ("grouped_pattern", "scope"),
        "precondition": "只为一个已由确定性 identity 管线（S05）产生 pattern_id 的 grouped_pattern "
                        "命名；名字是提案，必须被 S05 canonicalize 后才存在（`04:52` C3、`12:239` item 3）",
        "payload_required": ("step", "pattern_id", "proposed_pattern_name"),
        "enums": {},
        # ESC-W2-01 (stable pattern_id + model naming separation): a naming step may propose a
        # human-readable name and NOTHING carrying identity or count authority. `pattern_id` is
        # required only to say WHICH pattern is named; the authoritative value is read from the
        # deterministic bundle, never from the payload. support/count/lineage/split/merge/state
        # are refused wherever they nest -- a rename never migrates a counter.
        "extra_forbidden": ("support_count", "support", "count", "distinct_occurrence_count",
                            "new_pattern_id", "pattern_id_new", "lineage", "predecessors",
                            "split", "merge", "merged_ids", "migrate", "migration",
                            "state", "to_state", "from_state", "supersede_now"),
        "effect": "propose ONE human-readable name; S05 canonicalizes it into pattern_key. "
                  "pattern_id is unchanged and support is never carried by this step "
                  "(ESC-W2-01: 模型不得拥有 identity authority)",
        "advisory_only": True,
    },
    "M3": {
        # IMPLEMENTATION_GAP: which conflict classes may stay with the small model and which
        # must escalate to a judge/human has NO quantified门槛 in Round 2（`04:193` D6-b）. The
        # conservative reading is implemented: only an alert the deterministic layer raised ever
        # reaches M3, and an answer of `unresolved_conflict` is handed to G1 rather than
        # self-resolved.
        # / DEFERRED id DD-6-sub45 (`04` §9 D6-b)
        "title": "Judge 高风险分歧",
        "pipeline_step": "#14",
        "matrix_row": "`04` 行 7、9 的 judge 列（`04:53`、`04:55`）",
        "required_context": ("conflict_alert", "scope"),
        "precondition": "仅由报警触发、常态 0 次（`12:135`、`04:97`）",
        "payload_required": ("step", "alert_id", "verdict", "reconciliation"),
        "enums": {"verdict": ("reconciled_by_action_priority", "unresolved_conflict")},
        "extra_forbidden": ("resolved_now", "superseded", "deleted_target"),
        "no_scorer": True,
        "effect": "记 unresolved_conflict 交人类批处理（`12:135`）；不引入评分器（`04:80` C4）",
        "advisory_only": True,
    },
    "M4": {
        # IMPLEMENTATION_GAP: whether a judge is ever admitted into acceptance scoring is
        # undecided（`04:59` row 13 judge 列 DEFERRED、`04:194` D6-c）, so `assertions.kind` holds
        # only the two deterministic-checkable kinds and the proposal keeps
        # `eval_status: partial`. Prose-quality rubrics are not admitted here.
        # / DEFERRED id DD-6-sub45 (`04` §9 D6-c) with DD-3-sub20
        "title": "晋升规则的 eval 题面",
        "pipeline_step": "#19",
        "matrix_row": "`04` 行 12 的 ◐（`04:58`）",
        "required_context": ("promoted_artifact", "s15_corpus", "scope"),
        "precondition": "语料与 split 由 S15 持有，每次晋升一次（`12:136`、`04:85` C9）",
        "payload_required": ("step", "artifact_id", "question_stem", "assertions"),
        "enums": {"assertions.kind": ("structure", "deterministic")},
        "extra_forbidden": ("expected_answer", "solution", "held_out", "answer_key"),
        "exam_isolation": True,
        "effect": "只产题面；打分归确定性侧，如实标 eval_status: partial（`04:125`）",
        "advisory_only": False,
    },
}

#: Names a not-yet-landed sibling module is referred to by, so the gap is visible rather
#: than quietly satisfied by a local copy.
NOT_LANDED_YET = {
    "S15": "S15 kd_eval_freeze (W3-C) owns the frozen corpus and split. W3-E does not import a "
           "file another agent owns, so M4 takes the corpus as a context field: S15's freeze "
           "answer {corpus_digest, split} satisfies it directly. Until the integrator wires "
           "that, M4 returns NO_PROPOSAL rather than inventing a corpus",
    "S10": "S10 kd_gate / kd_gate_tree (W3-A) owns the count-gate and promotion verdict. W3-E "
           "does not import it: M2 reads the count-gate answer the host hands in, because a "
           "second gate inside the envelope would be a second authority",
}

#: which upstream owner a missing context field belongs to, so a gap names a module
_OWNER_BY_CONTEXT_FIELD = {"s15_corpus": "S15", "count_gate": "S10"}


# --------------------------------------------------------------------- bounded context
def _digest(obj) -> str:
    """Content address of anything the deterministic layer handed out, computed by the frozen
    kernel -- not by a local hash recipe (`kd_provenance.content_hash`)."""
    return prov.content_hash(obj)


def _require_scope(scope):
    if not isinstance(scope, dict):
        raise StepContractError("context.scope must be an object resolved by S04/S05")
    for key in ("workspace", "project", "layer"):
        if not isinstance(scope.get(key), str) or not scope[key].strip():
            raise StepContractError(f"context.scope.{key} is empty: an unresolved scope cannot "
                                    "be stamped (S13) nor gated (S05), and 05 §5.3 S1 forbids "
                                    "defaulting a missing layer")
    if scope["layer"] not in ("project", "global", "cohort"):
        raise StepContractError("context.scope.layer is outside SC11")
    return dict(scope)


def build_context(step, *, scope, candidate_pairs=None, grouped_pattern=None, count_gate=None,
                  conflict_alert=None, promoted_artifact=None, s15_corpus=None,
                  allowed_evidence_ids=None, allowed_refs=None, proxy_scores=None,
                  held_out_literals=None, notes=None) -> dict:
    """Assemble the bounded context a responder may see. Everything in it comes from the
    deterministic stages; nothing in it comes from a model.

    `held_out_literals` is the M4 answer corpus. It is stored under a leading-underscore key
    so `_responder_view` strips it (exam isolation, `04:85` C9: 语料与 split 若由模型掌握，
    模型能看见答案，eval 失效) and only the validator reads it.
    """
    contract = _contract(step)
    bundle = {
        "schema": "model-context/1",
        "step": step,
        "scope": _require_scope(scope),
        "candidate_pairs": copy_view(candidate_pairs),
        "grouped_pattern": copy_view(grouped_pattern),
        "count_gate": copy_view(count_gate),
        "conflict_alert": copy_view(conflict_alert),
        "promoted_artifact": copy_view(promoted_artifact),
        "s15_corpus": copy_view(s15_corpus),
        "allowed_evidence_ids": sorted({str(e) for e in (allowed_evidence_ids or []) if str(e)}),
        "allowed_refs": sorted_ref_set(allowed_refs or []),
        "proxy_scores": sorted({float(s) for s in (proxy_scores or [])}),
        "_held_out_literals": sorted({str(h) for h in (held_out_literals or []) if str(h)}),
        "notes": str(notes or ""),
        "model_step_rights": "proposal only, never a write (`04:17` I-2)",
        "zero_llm_exit": ZERO_LLM_EXITS[step],
    }
    bundle["context_digest"] = _digest(
        {k: v for k, v in bundle.items() if not k.startswith("_")})
    missing = [name for name in contract["required_context"]
               if not bundle.get(name) and name != "scope"]
    if missing:
        # the bundle itself says which deterministic input is absent, so a step can never be
        # run on an under-specified context and blame the model for the result
        bundle["incomplete_for"] = missing
    return bundle


def copy_view(value):
    return copy.deepcopy(value)


def sorted_ref_set(raw_refs):
    """Normalise the deterministic layer's allowed refs through S14's own parser, so a
    brace/glob shorthand never enters a bundle (S14 exit 2, `12` S14 row)."""
    out = []
    for item in raw_refs:
        text = item.get("path") if isinstance(item, dict) else item
        parsed = refs.parse_ref(text, project=(item.get("project") if isinstance(item, dict)
                                               else "") or "")
        if isinstance(item, dict) and item.get("line_start") is not None:
            parsed["line_start"] = int(item["line_start"])
            parsed["line_end"] = int(item.get("line_end") or item["line_start"])
        out.append(parsed)
    return sorted(out, key=lambda r: (r["path"], r.get("line_start") or 0))


def _responder_view(bundle: dict) -> dict:
    """The redacted bundle handed to the injected callable: no leading-underscore key, ever."""
    view = copy.deepcopy({k: v for k, v in bundle.items() if not k.startswith("_")})
    # S15's full document contains the adjudicator-side file locators. M4 sees only
    # the question side, never paths/digests enabling access to the answer side.
    corpus = view.get("s15_corpus")
    if isinstance(corpus, dict):
        view["s15_corpus"] = {k: copy.deepcopy(corpus[k]) for k in
                             ("corpus_digest", "bundle_digest", "dataset_id", "splits")
                             if k in corpus}
        if isinstance(corpus.get("samples"), list):
            view["s15_corpus"]["samples"] = [
                {k: row[k] for k in ("sample_id", "split", "task_input") if k in row}
                for row in corpus["samples"] if isinstance(row, dict)]
    return view


def _contract(step: str) -> dict:
    if step not in STEP_CONTRACTS:
        raise StepContractError(f"unknown model step {step!r}: the authoritative model steps are "
                                f"{sorted(STEP_CONTRACTS)} (contracts.json `model_steps`, "
                                "`12:241`); no step beyond this contract set is admitted -- "
                                "`12:129` bars ADDING a new model position, and M2b is inside "
                                "the Round 2 contract, not a fifth insertion point invented here")
    return STEP_CONTRACTS[step]


# --------------------------------------------------------------------- preconditions
def precondition_gap(step: str, bundle: dict):
    """Return (code, reason) when this step must NOT call a model at all, else None.

    These are `04` §5's cost gates, checked before the responder is invoked: a step that is
    not supposed to fire stays at zero calls even on a host that injected a callable.
    """
    contract = _contract(step)
    if step == "M1":
        pairs = bundle.get("candidate_pairs") or []
        rows = pairs.get("pairs") if isinstance(pairs, dict) else pairs
        if not rows:
            return ("M1_EMPTY_CANDIDATE_SET",
                    "S07 exit 0=空集⇒下游跳过 M1（`12:115`）：无 candidate 即无语义判重可做")
    if step == "M2":
        gate = bundle.get("count_gate") or {}
        if not gate.get("cleared"):
            return ("M2_COUNT_GATE_NOT_CLEARED",
                    "M2 必须排在 #13 计数门之后（`12:134`）：计数未达标时抽象提案本身就是 "
                    "`07` §3.1 要防的过早泛化")
    if step == "M2b":
        grouped = bundle.get("grouped_pattern") or {}
        pid = grouped.get("pattern_id") if isinstance(grouped, dict) else None
        if not str(pid or "").strip():
            return ("M2B_NO_PATTERN_TO_NAME",
                    "M2b names an existing deterministic pattern_id (S05); the bundle carries no "
                    "grouped_pattern.pattern_id, so there is nothing to name -- a name is never "
                    "minted before the identity pipeline produced the pattern (ESC-W2-01: 模型不得"
                    "拥有 identity authority)")
    if step == "M3":
        if not (bundle.get("conflict_alert") or {}).get("alerts"):
            return ("M3_NO_ALERT",
                    "M3 仅由报警触发、常态 0 次（`04:97`、`12:135`）：无冲突告警即不消费 judge")
    if step == "M4":
        corpus = bundle.get("s15_corpus")
        if not isinstance(corpus, dict) or not (corpus.get("bundle_digest") or corpus.get("corpus_digest")):
            return ("M4_NO_FROZEN_CORPUS",
                    "M4 has no frozen corpus or split to work against (NOT_LANDED_YET): "
                    + NOT_LANDED_YET["S15"])
    incomplete = bundle.get("incomplete_for")
    if incomplete:
        owner = _OWNER_BY_CONTEXT_FIELD.get(incomplete[0])
        detail = NOT_LANDED_YET.get(owner, "the upstream stage did not hand this input")
        return ("CONTEXT_INCOMPLETE",
                f"deterministic input missing for {step}: {sorted(incomplete)} -- {detail}")
    return None


# --------------------------------------------------------------------- validation (deterministic)
def _all_keys(payload, prefix=""):
    """Every key path in a payload tree, so a forbidden field cannot hide inside a nest."""
    keys = []
    if isinstance(payload, dict):
        for key, value in payload.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            keys.append((path, value))
            keys.extend(_all_keys(value, path))
    elif isinstance(payload, list):
        for index, value in enumerate(payload):
            keys.extend(_all_keys(value, f"{prefix}[{index}]"))
    return keys


def _find_forbidden(step: str, payload: dict) -> list:
    contract = STEP_CONTRACTS[step]
    banned = {name.lower() for name in FORBIDDEN_UNIVERSAL} | \
             {name.lower() for name in contract["extra_forbidden"]}
    hits, seen = [], set()
    for path, _value in _all_keys(payload):
        leaf = path.split(".")[-1].split("[")[0].lower()
        if leaf in banned and path not in seen:
            seen.add(path)
            hits.append({"code": "RIGHTS_ESCALATION", "field": path,
                         "message": f"{step} payload carries {path!r}: a model holds proposal "
                                    "rights only (`04:17` I-2), and approval / write authority "
                                    "/ gate verdicts are never model-supplied fields -- wherever "
                                    "they nest they are refused"})
    return hits


def _find_scorer(step: str, payload: dict) -> list:
    """M3's 不引入评分器 (`04:80` C4): no score-shaped field name and no float in a judge
    answer. An action-priority ordering is a permutation of ids, not a number."""
    if not STEP_CONTRACTS[step].get("no_scorer"):
        return []
    hits = []
    score_named = ("score", "confidence", "rating", "weight", "rank", "severity")
    for path, value in _all_keys(payload):
        leaf = path.split(".")[-1].split("[")[0].lower()
        if any(token in leaf for token in score_named):
            hits.append({"code": "SCORING_ARTIFACT_REJECTED", "field": path,
                         "message": f"{step} carries a scored field {path!r}; `04` C4 (`04:80`) "
                                    "adopts action priority + same-round reconcile and forbids "
                                    "a scorer"})
        if isinstance(value, float):
            hits.append({"code": "SCORING_ARTIFACT_REJECTED", "field": path,
                         "message": f"{step} carries a numeric value at {path!r}: a judge answer "
                                    "is a verdict plus an ordering of existing ids, never a "
                                    "number to be averaged into a gate"})
    return hits


def check_shape(step: str, raw) -> list:
    """Deterministic schema check BEFORE anything can become a proposal.

    Free-form text is refused, not interpreted: `04` §7.2 (`04:150-154`)判 REJECT 的形态正是
    「解析失败后换一套 schema 重解释同一份输出」。
    """
    contract = _contract(step)
    if not isinstance(raw, dict):
        return [{"code": "FREE_FORM_OUTPUT_REJECTED", "field": "$",
                 "message": f"{step} requires a structured proposal object, got "
                            f"{type(raw).__name__}; prose is not a proposal（`12` N22b：draft 必须"
                            "是可执行断言的候选，不得只是给人读的散文，`06:202-203`）"}]
    try:
        json.dumps(raw, allow_nan=False)
    except (TypeError, ValueError):
        return [{"code": "SHAPE_MISMATCH", "field": "$", "message": "model output must be finite JSON data"}]
    violations = []
    if raw.get("step") != step:
        violations.append({"code": "STEP_MISMATCH", "field": "step",
                           "message": "model output does not answer the requested step"})
    for field in contract["payload_required"]:
        if field not in raw:
            violations.append({"code": "MISSING_FIELD", "field": field,
                               "message": f"{step} payload declares no {field!r}"})
    if any(v["code"] == "MISSING_FIELD" for v in violations):
        return violations
    list_fields = {"M1": ("pair_verdicts",), "M2": ("evidence_ids", "claims"),
                   "M4": ("assertions",)}.get(step, ())
    list_fields += ("evidence_refs",) if "evidence_refs" in raw else ()
    list_fields = tuple(set(list_fields) | {k for k in ("pair_verdicts", "claims", "assertions")
                                          if k in raw})
    if any(not isinstance(raw.get(k), list) for k in list_fields):
        return violations + [{"code": "SHAPE_MISMATCH", "field": k,
                              "message": f"{step}.{k} must be an array"}
                             for k in list_fields if not isinstance(raw.get(k), list)]
    if any(not isinstance(row, dict) for k in ("pair_verdicts", "claims", "assertions")
           for row in raw.get(k, [])):
        return violations + [{"code": "SHAPE_MISMATCH", "field": "$",
                              "message": "verdicts/claims/assertions must contain objects"}]
    for dotted, allowed in contract["enums"].items():
        bad = _enum_violations(raw, dotted, allowed, step)
        violations.extend(bad)
    violations.extend(_find_forbidden(step, raw))
    violations.extend(_find_scorer(step, raw))
    violations.extend(_step_specific(step, raw))
    return violations


def _enum_violations(raw: dict, dotted: str, allowed, step: str) -> list:
    """`landing_tier` and `pair_verdicts.verdict` style enum checks (list-aware)."""
    head, _, tail = dotted.partition(".")
    if tail == "":
        value = raw.get(head)
        if value not in allowed:
            return [{"code": "ENUM_OUT_OF_RANGE", "field": head,
                     "message": f"{step}.{head}={value!r} is not one of {list(allowed)} "
                                "（`12` S09 exit 2=枚举越界）"}]
        return []
    out = []
    for index, item in enumerate(raw.get(head) or []):
        if not isinstance(item, dict):
            out.append({"code": "SHAPE_MISMATCH", "field": f"{head}[{index}]",
                        "message": f"{step}.{head}[{index}] must be an object"})
            continue
        value = item.get(tail)
        if value not in allowed:
            out.append({"code": "ENUM_OUT_OF_RANGE", "field": f"{head}[{index}].{tail}",
                        "message": f"{step}.{head}[{index}].{tail}={value!r} is not one of "
                                   f"{list(allowed)}"})
    return out


def _find_tier3_leak(step: str, raw: dict) -> list:
    """S07's tier-3 ranking signal must not ride an M-step into anything a gate reads
    (`12:115` 分数永不进晋升记录). S07's own name pattern is reused, not restated, and the
    final check on the emitted proposal is `contain_scores` below."""
    if step not in ("M1", "M2"):
        return []
    hits = []
    for path, value in _all_keys(raw):
        leaf = path.split(".")[-1].split("[")[0]
        if proxy.SCORE_NAME_RE.search(leaf):
            hits.append({"code": "TIER3_SIGNAL_LEAK", "field": path,
                         "message": f"{step} payload carries {leaf!r}: the proxy score is a "
                                    "ranking signal for candidate generation only（`04:51` 行 5 判定层"
                                    "不产出分数），it is refused here and `contain_scores` runs "
                                    "S07's guard on the finished proposal"})
        del value
    return hits


def _step_specific(step: str, raw: dict) -> list:
    out = _find_tier3_leak(step, raw)
    if step == "M1":
        rows = raw.get("pair_verdicts") or []
        for index, item in enumerate(rows):
            if not isinstance(item, dict) or "pair_id" not in item:
                out.append({"code": "SHAPE_MISMATCH", "field": f"pair_verdicts[{index}]",
                            "message": "M1 verdicts must name the candidate pair they answer; "
                                       "an unanchored judgement cannot be audited"})
                continue
            if item.get("verdict") == "same_principle" and not str(item.get("rationale") or ""):
                out.append({"code": "UNSUBSTANTIATED_VERDICT",
                            "field": f"pair_verdicts[{index}].rationale",
                            "message": "M1 asserts two entries are one principle but gives no "
                                       "rationale: the marker is advisory, so an empty reason is "
                                       "not evidence for anyone"})
        return out
    if step == "M2":
        if not str(raw.get("abstract_statement") or "").strip():
            out.append({"code": "EMPTY_ABSTRACTION", "field": "abstract_statement",
                        "message": "M2 produced no statement to abstract"})
        if not raw.get("evidence_ids"):
            out.append({"code": "EVIDENCE_FREE_ABSTRACTION", "field": "evidence_ids",
                        "message": "M2 generalises without binding to any of the evidence the "
                                   "deterministic stage handed it -- exactly the "
                                   "over-generalisation `04:53` puts under the judge column"})
        return out
    if step == "M2b":
        name = raw.get("proposed_pattern_name")
        if not isinstance(name, str) or not name.strip():
            out.append({"code": "EMPTY_PATTERN_NAME", "field": "proposed_pattern_name",
                        "message": "M2b must propose exactly one non-empty human-readable name; "
                                   "an empty name is not a naming proposal（`04:52` C3）"})
        if not str(raw.get("pattern_id") or "").strip():
            out.append({"code": "UNANCHORED_NAME", "field": "pattern_id",
                        "message": "M2b must say WHICH deterministic pattern_id it names; an "
                                   "unanchored name cannot be canonicalized against an identity "
                                   "(ESC-W2-01)"})
        return out
    if step == "M4":
        assertions = raw.get("assertions") or []
        if not assertions:
            return [{"code": "NO_ASSERTIONS", "field": "assertions",
                     "message": "M4 must yield structurally checkable assertions, not only a "
                                "question stem（`04:58` 只跑结构断言与确定性打分）"}]
        return []
    return []


def exam_isolation_violations(step: str, raw: dict, bundle: dict) -> list:
    """M4's corpus and split belong to S15 (`12:136`). A stem or assertion that repeats a
    held-out answer means the model saw the answer, which voids the eval outright
    (`04:85` C9: 语料与 split 若由模型掌握，模型能看见答案，eval 失效).
    """
    if not STEP_CONTRACTS[step].get("exam_isolation"):
        return []
    literals = [str(x) for x in (bundle.get("_held_out_literals") or []) if str(x).strip()]
    texts = [str(raw.get("question_stem") or "")]
    for assertion in (raw.get("assertions") or []):
        if isinstance(assertion, dict):
            texts.append(str(assertion.get("predicate") or ""))
            texts.append(str(assertion.get("expect") or ""))
    hits = []
    for literal in literals:
        for text in texts:
            if literal in text:
                hits.append({"code": "EXAM_ISOLATION_BROKEN", "field": "question_stem",
                             "message": f"M4 output repeats held-out material {literal!r}: the "
                                        "answer corpus is S15's, never a model input, and a stem "
                                        "that contains it grades nothing（`04:58`、`04:85`）"})
                break
    return hits



# --------------------------------------------------------------------- hallucinated-evidence defence
def check_evidence(step: str, raw: dict, bundle: dict, registry=None) -> dict:
    """S14 is the witness, not the model's own citation list (`04:63` row 16: exact set
    equality + 拒批外引用; `04:88` C12: 「不得用来证明读过」).

    Two independent refusals:
      * a cited evidence id the deterministic stage never handed over -> HALLUCINATED_EVIDENCE;
      * a cited path outside the allowed ref set, or one S14 cannot resolve on disk, or one
        carrying brace/glob shorthand -> refused with S14's own vocabulary.
    A claim whose strong identifiers do not appear in the cited line range is refused by S14's
    `check_claim_binding` (CM-65), called rather than re-implemented.
    """
    allowed_ids = set(bundle.get("allowed_evidence_ids") or [])
    cited_ids = {str(x) for x in (raw.get("evidence_ids") or [])}
    for row in (raw.get("pair_verdicts") or []):
        if isinstance(row, dict):
            cited_ids |= {str(x) for x in (row.get("cites_evidence") or [])}
    invented = sorted(cited_ids - allowed_ids) if allowed_ids else sorted(cited_ids)
    findings = [{"code": "HALLUCINATED_EVIDENCE", "field": "evidence_ids",
                 "message": f"{step} cites {item!r}, which no deterministic stage handed to it "
                            f"(allowed set has {len(allowed_ids)} ids). Refusing the proposal, "
                            "not the citation（`04:63`）"} for item in invented]

    allowed_paths = {r["path"] for r in (bundle.get("allowed_refs") or [])}
    cited_refs = []
    for item in (raw.get("evidence_refs") or []):
        text = item.get("path") if isinstance(item, dict) else item
        try:
            parsed = refs.parse_ref(str(text),
                                   project=(item.get("project") if isinstance(item, dict)
                                            else "") or "")
        except refs.RefSyntaxError as exc:
            findings.append({"code": "REF_SHORTHAND", "field": "evidence_refs",
                             "message": f"{step} cited {text!r} which S14 refuses to parse "
                                        f"({exc}); no expansion, no guessing（S14 exit 2）"})
            continue
        if parsed["path"] not in allowed_paths:
            findings.append({"code": "HALLUCINATED_EVIDENCE", "field": "evidence_refs",
                             "message": f"{step} cites {parsed['path']!r} which is outside the "
                                        f"{len(allowed_paths)} refs the deterministic stage "
                                        "handed it"})
            continue
        cited_refs.append(parsed)

    integrity = {"status": refs.STATUS_EMPTY_REF_SET if not cited_refs else refs.STATUS_PASS,
                 "basis": "kd_model_step.check_evidence via kd_refs_audit"}
    resolved_refs = []
    if registry is not None and cited_refs:
        audit = refs.audit_refs(cited_refs, registry)
        integrity = refs.refs_integrity_bit(audit)
        if audit["status"] != refs.STATUS_PASS:
            findings.append({"code": "REF_UNRESOLVED", "field": "evidence_refs",
                             "message": f"S14 recomputed the cited refs and they do not all "
                                        f"resolve: status={audit['status']} "
                                        f"counts={audit['counts']}"})
        resolved_refs = [dict(f["ref"], resolved_path=f["resolved_path"])
                         for f in audit["findings"] if f["kind"] == "OK"]
    claims = _claims_of(raw, step)
    if claims:
        if not resolved_refs:
            findings.append({"code": "CLAIM_NOT_VERIFIED", "field": "claims",
                             "message": f"{step} asserts strong identifiers but no registered "
                                        "root was supplied, so S14 could not re-read the cited "
                                        "lines: an unverified claim is not a verified one "
                                        "（`04:63` row 16 —— 模型从不用于证明）"})
        else:
            for index, row in enumerate(refs.check_claim_binding(claims, resolved_refs)):
                findings.append({"code": "CM65_STRAY_IDENTIFIER", "field": f"claims[{index}]",
                                 "message": f"claim {row['claim_id']} names {row['identifiers']} "
                                            "which do not appear in the cited line range "
                                            "(CM-65 / S14 check_claim_binding)"})

    if not cited_ids and step in ("M2",):
        findings.append({"code": "EMPTY_REF_SET", "field": "evidence_ids",
                         "message": "an empty citation set is not a clean answer (S14's "
                                    "anti-vacuity rule): M2 must bind to the evidence it "
                                    "abstracted from"})
    return {"findings": findings, "refs_audit": integrity,
            "cited_evidence_ids": sorted(cited_ids),
            "unused_evidence": sorted(allowed_ids - cited_ids) if allowed_ids else []}


def _claims_of(raw: dict, step: str) -> list:
    out = []
    for index, claim in enumerate(raw.get("claims") or []):
        if not isinstance(claim, dict):
            continue
        out.append({"claim_id": claim.get("claim_id", f"{step}-claim-{index}"),
                    "text": claim.get("text", ""),
                    "strong_identifiers": claim.get("strong_identifiers") or [],
                    "evidence_ref_index": claim.get("evidence_ref_index")})
    return out


# --------------------------------------------------------------------- identity canonicalisation
def canonicalize(step: str, raw: dict, bundle: dict) -> dict:
    """I-1 (`04:16`): no model string reaches a counter or a gate until code derived it.

    The key is built from ids and fields the DETERMINISTIC stage owns; a model-supplied name
    only ever enters as `pattern_key`, and only after S05's normaliser pipeline folded it
    (`04:52` C3 -- 只准提案名字，必须被代码 canonicalize 后才存在).
    """
    scope = bundle["scope"]
    records = []
    if step == "M1":
        for row in (raw.get("pair_verdicts") or []):
            pair_id = str(row.get("pair_id"))
            records.append({"pair_id": pair_id,
                            "identity_record": {"pattern_key": f"m1-{pair_id}",
                                                "origin": {"problem": row.get("verdict", "")},
                                                "scope": scope}})
    elif step == "M2":
        name = str(raw.get("proposed_pattern_name") or "")
        records.append({"pattern_id": str(raw.get("pattern_id")),
                        "model_supplied_name": name or None,
                        "canonical_name": ident.normalize_token(name) if name else None,
                        "identity_record": {"pattern_key": ident.normalize_token(name) if name
                                            else f"m2-{raw.get('pattern_id')}",
                                            "origin": {"problem": raw.get("abstract_statement",
                                                                          "")},
                                            "scope": scope}})
    elif step == "M2b":
        grouped = bundle.get("grouped_pattern") or {}
        deterministic_pid = str(grouped.get("pattern_id") or "")
        name = str(raw.get("proposed_pattern_name") or "")
        canonical_name = ident.normalize_token(name) if name.strip() else None
        records.append({
            # ESC-W2-01: pattern_id is the DETERMINISTIC one from the bundle, never the
            # payload's -- a naming step holds no identity authority and cannot re-key.
            "pattern_id": deterministic_pid,
            "model_supplied_name": name or None,
            "canonical_name": canonical_name,
            "pattern_id_source": "deterministic S05 grouped_pattern (model naming cannot change "
                                 "it; ESC-W2-01)",
            "support_count_carried": False,
            "identity_record": {"pattern_key": canonical_name or f"pat-{deterministic_pid}",
                                "origin": {"problem": str(grouped.get("problem") or name or "")},
                                "scope": scope}})
    elif step == "M3":
        records.append({"alert_id": str(raw.get("alert_id")),
                        "identity_record": {"pattern_key": f"m3-{raw.get('alert_id')}",
                                            "origin": {"problem": str(raw.get("verdict", ""))},
                                            "scope": scope}})
    elif step == "M4":
        records.append({"artifact_id": str(raw.get("artifact_id")),
                        "identity_record": {"pattern_key": f"m4-{raw.get('artifact_id')}",
                                            "origin": {"problem": str(raw.get("question_stem",
                                                                              ""))[:200]},
                                            "scope": scope}})
    for record in records:
        inner = record.get("identity_record")
        if not inner:
            continue
        try:
            record["derived"] = ident.checked_derive(inner)
        except ident.IdentityGuardViolation as exc:
            record["derivation_refused"] = str(exc)
    return {"normalizer_set": ident.NORMALIZER_SET, "records": records,
            "rule": "model strings are inputs to S05, never keys themselves (`04:16` I-1)"}


# --------------------------------------------------------------------- proposal assembly
def assemble_proposal(step: str, raw: dict, bundle: dict, facts, registry=None) -> dict:
    """The only shape this module can produce: a PROPOSAL with provenance stamped by S13.

    It is not written anywhere. `kd_gate.apply_mutation` raises `WritePathViolation` on it
    until a human approval is present, and there is no other route from here to disk.
    """
    if step == "M1":
        pairs = bundle.get("candidate_pairs") or []
        pairs = pairs.get("pairs", []) if isinstance(pairs, dict) else pairs
        allowed = {row["pair_id"] for row in pairs if isinstance(row, dict)
                   and isinstance(row.get("pair_id"), str) and row["pair_id"].strip()}
        selected = [row.get("pair_id") for row in raw["pair_verdicts"]]
        if any(not isinstance(pair_id, str) or not pair_id.strip() for pair_id in selected):
            raise EnvelopeRefusal("IDENTITY_TAMPER", "M1 pair IDs must be nonempty strings")
        if not selected or len(set(selected)) != len(selected) or set(selected) - allowed:
            raise EnvelopeRefusal("IDENTITY_TAMPER", "M1 must answer distinct supplied pairs")
    if step in ("M2", "M3", "M4"):
        key, context = {"M2": ("pattern_id", "grouped_pattern"),
                        "M3": ("alert_id", "conflict_alert"),
                        "M4": ("artifact_id", "promoted_artifact")}[step]
        owner = bundle.get(context) or {}
        if not isinstance(owner, dict):
            raise EnvelopeRefusal("CONTEXT_MALFORMED", f"{context} must be an object")
        allowed = {str(owner[key])} if isinstance(owner, dict) and owner.get(key) else set()
        if step == "M3":
            allowed.update(str(row["alert_id"]) for row in owner.get("alerts", [])
                           if isinstance(row, dict) and row.get("alert_id"))
        if str(raw.get(key) or "") not in allowed:
            raise EnvelopeRefusal("IDENTITY_TAMPER", f"{step}.{key} is not a supplied identity")
    evidence = check_evidence(step, raw, bundle, registry=registry)
    violations = evidence["findings"]
    if violations:
        raise EnvelopeRefusal(violations[0]["code"], violations[0]["message"],
                              {"violations": violations})

    if step == "M2b":
        # ESC-W2-01 identity continuity: the model names WHICH pattern; it may not re-key it.
        # The authoritative pattern_id is the deterministic one in the bundle, so a payload
        # declaring a different id is an identity-tamper attempt -- refused, never canonicalized,
        # and support is never migrated by a rename.
        grouped = bundle.get("grouped_pattern") or {}
        det_pid = str(grouped.get("pattern_id") or "")
        claimed_pid = str(raw.get("pattern_id") or "")
        if det_pid and claimed_pid and claimed_pid != det_pid:
            message = (
                f"M2b declared pattern_id {claimed_pid!r} but the deterministic identity pipeline "
                f"(S05) produced {det_pid!r}: a naming step proposes a human-readable name only, "
                "it holds no identity authority and may not re-key a pattern or migrate its "
                "support (ESC-W2-01). Refused, not canonicalized.")
            raise EnvelopeRefusal(
                "IDENTITY_TAMPER", message,
                {"violations": [{"code": "IDENTITY_TAMPER", "field": "pattern_id",
                                 "message": message}],
                 "declared_pattern_id": claimed_pid, "deterministic_pattern_id": det_pid})

    canonicalized = canonicalize(step, raw, bundle)
    if any("derivation_refused" in row for row in canonicalized["records"]):
        raise EnvelopeRefusal("IDENTITY_DERIVATION_REFUSED", "S05 refused the proposed identity")
    body = {
        "step": step,
        "pipeline_step": STEP_CONTRACTS[step]["pipeline_step"],
        "record_type": "proposal",
        "source_class": prov.MODEL_OUTPUT,
        "produced_by": {"kind": "model", "step": step},
        "rights": "proposal-only",
        "write_authority": False,
        HUMAN_APPROVAL_FIELD: False,
        "advisory_only": bool(STEP_CONTRACTS[step]["advisory_only"]),
        "effect": STEP_CONTRACTS[step]["effect"],
        "scope": dict(bundle["scope"]),
        "context_digest": bundle["context_digest"],
        "payload": copy.deepcopy(raw),
        "canonicalized": canonicalized,
        "evidence": evidence,
        "model_identity": dict(MODEL_IDENTITY_STANCE),
        "eval_status": "partial" if step == "M4" else None,
    }
    if step == "M1":
        body["advisory_marker"] = {"kind": "possible_duplicate", "merge_executed": False,
                                   "never_auto_merges": True}
    if step == "M2":
        body["count_gate"] = dict(bundle.get("count_gate") or {})
    if step == "M2b":
        body["identity_continuity"] = {
            "pattern_id_authority": "deterministic (S05), unchanged by naming",
            "support_count_carried": False,
            "rule": "ESC-W2-01: 普通改名保持 pattern_id 不变、绝不迁移 support_count；真正的 "
                    "split/merge 只能出提案，确定性系统批准后才 mint 新 pattern_id + lineage 并"
                    "从 Evidence 重算 support（禁止 new.support_count = old.support_count）",
        }
    if step == "M3":
        body["batch_handoff"] = {"to": "G1 human batch", "reason": "unresolved_conflict"}
    if step == "M4":
        # `12:136` 每次晋升一次，不随语料规模放大 -- declared here, enforced upstream
        body["cost_rule"] = {
            "model_calls_per_promotion": 1,
            "wording": "每次晋升一次，不随语料规模放大（`12:136`、`04:58`）",
            "repeat_suppression_owner": "S18 kd_budget (W3-D) plus S02's input-digest 到期门 "
                                        "（`04:54`）；本模块只声明该规则，不实现第二个预算",
        }
    if facts is None:
        raise EnvelopeRefusal("RUNTIME_FACTS_MISSING",
                              "no kd_provenance_stamp.RuntimeFacts were supplied, so this "
                              "proposal could not be attributed: refused rather than stamped "
                              "with a placeholder（S13 exit 3）")
    try:
        stamped = stamp.stamp(body, facts)
    except stamp.ProvenanceViolation as exc:
        raise EnvelopeRefusal("SELF_DECLARED_PROVENANCE", str(exc), {}) from exc
    except stamp.InvalidFacts as exc:
        raise EnvelopeRefusal("UNSTAMPABLE", str(exc), {}) from exc
    contain_scores(bundle, stamped)
    return stamped


def contain_scores(bundle: dict, proposal: dict) -> None:
    """S07's guard is called on everything this envelope emits, so a tier-3 ranking score can
    never ride a proposal into a promotion record（`12:115` 分数永不进晋升记录、
    `W2-B` expected consumers = S10/S12）. Raises EnvelopeRefusal on a leak."""
    try:
        proxy.assert_not_promotion_payload(proposal, scores=bundle.get("proxy_scores"))
    except proxy.PromotionLeakRefusal as exc:
        raise EnvelopeRefusal("PROMOTION_LEAK", str(exc),
                              {"guard": "kd_proxy_candidates.assert_not_promotion_payload"}) \
            from exc


# --------------------------------------------------------------------- the envelope
def no_proposal(step: str, code: str, reason: str, bundle: dict = None, **extra) -> dict:
    """Zero-LLM degradation: an explicit named status naming the missing input (`04:119`)."""
    out = {"step": step, "status": NO_PROPOSAL, "code": code, "reason": reason,
            "proposal": None, "missing_input": extra.get("missing_input") or code,
            "zero_llm_exit": ZERO_LLM_EXITS[step],
            "halts_deterministic_chain": False}
    out.update(extra)
    if bundle is not None:
        out["context_digest"] = bundle.get("context_digest")
    return out


def refused(step: str, code: str, reason: str, preserved, bundle=None, **extra) -> dict:
    """I-3 (`04:18`): the failing answer is kept verbatim and labelled a failure. No second
    schema re-reads it, and nothing downstream may treat it as a proposal."""
    out = {"step": step, "status": REFUSED, "code": code, "reason": reason,
           "proposal": None, "preserved_output": preserved, "retried": bool(extra.get("retried")),
           "halts_deterministic_chain": False}
    if bundle is not None:
        out["context_digest"] = bundle.get("context_digest")
    out.update(extra)
    return out


def run_model_step(step: str, bundle: dict, responder=None, *, facts=None, registry=None,
                   max_repairs=1) -> dict:
    """THE envelope call. Deterministic before and after, opaque in the middle.

    `responder` is the model the host injects: `responder(context_view) -> payload`. When it
    is None -- or when the step's own precondition is unmet -- no model is contacted at all.
    """
    _contract(step)                                    # unknown step id is a programmer error
    if type(max_repairs) is not int or max_repairs not in (0, 1):
        raise StepContractError("max_repairs must be 0 or 1 (one bounded repair)")
    bundle = copy.deepcopy(bundle)
    try:
        _require_scope(bundle.get("scope"))
        gap = precondition_gap(step, bundle)
    except (StepContractError, TypeError, AttributeError) as exc:
        return no_proposal(step, "CONTEXT_MALFORMED", type(exc).__name__, bundle)
    if gap:
        return no_proposal(step, gap[0], gap[1], bundle, missing_input=step)
    if responder is None or not callable(responder):
        return no_proposal(step, "RESPONDER_NOT_INJECTED",
                           f"the host injected no model callable for {step} "
                           f"({STEP_CONTRACTS[step]['title']}): no proposal is produced, the "
                           "deterministic spine continues unchanged",
                           bundle, missing_input="responder")

    attempt = 0
    first_violations = None
    first_raw = None
    while True:
        view = _responder_view(bundle)
        if attempt:
            view["repair"] = {"of_attempt": 0, "violations": copy.deepcopy(first_violations),
                              "previous_output": copy.deepcopy(first_raw),
                              "note": "one bounded repair retry, then the SAME deterministic "
                                      "gate (`04:77` C1); a different schema would be I-3"}
        try:
            raw = copy.deepcopy(responder(view))
        except Exception as exc:
            # Do not log provider text: it can contain private context or credentials.
            return refused(step, "RESPONDER_FAILED", type(exc).__name__, None, bundle,
                           retried=bool(attempt), model_calls=1 + attempt)
        violations = check_shape(step, raw) + exam_isolation_violations(step, raw, bundle)
        if attempt == 0:
            first_violations, first_raw = violations, raw
        if not violations:
            try:
                proposal = assemble_proposal(step, raw, bundle, facts, registry=registry)
            except EnvelopeRefusal as exc:
                return refused(step, exc.code, exc.message, raw, bundle,
                               violations=exc.detail.get("violations", [exc.message]),
                               retried=bool(attempt))
            return {"step": step, "status": PROPOSAL, "proposal": proposal,
                    "rights": "proposal-only", "write_authority": False,
                    "human_approved": False, "retried": bool(attempt),
                    "model_calls": 1 + attempt, "context_digest": bundle["context_digest"],
                    "next_gate": "S15/S16 independent Eval -> G1 kd_human_gate (approval) -> S10 N28 -> S12 kd_write_txn.commit_batch"}
        if attempt >= max_repairs:
            if first_violations is None:
                first_violations = violations
                first_raw = raw
            codes = sorted({v["code"] for v in violations})
            return refused(step, codes[0],
                           f"{step} answer failed the deterministic schema gate after "
                           f"{attempt} repair attempt(s): {codes}. Original output preserved; "
                           "no second schema reinterprets it（`04:18` I-3、`04:150-154`）",
                           raw, bundle, violations=violations, retried=bool(attempt),
                           first_violations=first_violations, first_output=first_raw)
        attempt += 1


def describe_steps() -> dict:
    """Machine-readable restatement of the five contracts (M1, M2, M2b, M3, M4), for the report
    and for hosts."""
    return {step: {"title": c["title"], "pipeline_step": c["pipeline_step"],
                   "matrix_row": c["matrix_row"], "required_context": c["required_context"],
                   "precondition": c["precondition"], "payload_required": c["payload_required"],
                   "enums": c["enums"], "advisory_only": c["advisory_only"],
                   "zero_llm_exit": ZERO_LLM_EXITS[step]}
            for step, c in STEP_CONTRACTS.items()}


def write_surface() -> tuple:
    """Names this module exports that could write durable state. It is empty by construction,
    and `test_w3e_model_human.py` proves it with an AST scan plus `kd_write_txn --audit`."""
    return ()
