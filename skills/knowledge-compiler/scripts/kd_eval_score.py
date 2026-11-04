#!/usr/bin/env python3
"""S16 `kd_eval_score` -- adjudicate a frozen eval bundle and emit the five-tuple audit record.

Contract row (12-SKILL-DESIGN-BRIEF.md:124; .distill/round-3/wave-3/_dispatch/w3c.json):
    inputs   冻结 holdout + before/after 产物 + 量具 id
    outputs  verdict + 五元组审计记录
    exit     2 = 裁决量具 id 与循环内 metric id 相同；变差即 FAILED（不得只标黄）
    clusters CM-48 regression-eval-for-promoted-rule (CORE, MUST) + CM-50 verify-before-persist
             (CORE, MUST; 12:140 -- CM-50 gets no separate script and is enforced jointly by
             S10 写前门 + S16 写前证据 + S12 唯一写者)
    pipeline 步 20 / 行 13

Two refusals this script is the only owner of:

1. SELF-GRADING (exit 2, 08:42 prerequisite (a) + 08:92 P-01). The instrument that adjudicates
   must not be the metric the optimisation loop maximises. Reference defect, read back this round
   by Round 2: `evolve_skill.py:157,170` passes `metric=skill_fitness_metric` to the optimiser and
   `:217,221` compares `baseline_score`/`evolved_score` computed with the SAME function
   (08:118 step 3). A set-disjointness check does not catch that -- the sets are the same
   instrument -- so this compares ids, and it is an assertion executed on every call
   (`assert_not_self_grading`), not a convention written down.

2. REGRESSION MUST BE RED (08:44 prerequisite (c) '且变差即 FAILED / 阻断（不允许「只警告不阻断」）',
   08:93 P-02). `score_bundle` returns `FAILED` for any drop of the after-mean below the
   before-mean, and for any single holdout sample that got strictly worse even when the mean
   improved (an average can hide one regression; P-02's non-blocking "any positive gain is
   accepted" path at `evolve_skill.py:287` is the shape being refused here). There is no warning / review /
   yellow member in the verdict vocabulary -- SC09's `verdict.status` enum is
   [NOT_RUN, PASSED, FAILED, UNVERIFIED] and `test_verdict_vocabulary_has_no_soft_member` reads
   the enum on disk so a future edit that adds one fails.

`verified` is COMPUTED here, never accepted: 08:65 defines it as
`Tier-0 ∧ (Tier-1 若样本可复现 ∨ Tier-2 若为可泛化文本资产)` and 08:67 requires every verified
record to carry the five-tuple (量具 id, 样本/数据集 id, 阈值, 运行结果, 该量具是否同时被用于优化).
`_verified_claim` implements that formula over this document's own fields; a bundle that stored
`verified: true` is ignored (S15 never stores it, and 08:97 P-07 forbids an unwired claim reading
as a pass).

CM-50 hook (for W3-A's S10 gate and S12's writer, both landing in parallel):
    `verification_evidence(score_doc, artifact_sha)` -> an SC04 `verification[]` row
    `assert_verified(score_doc)`                     -> raises NotVerified unless verified is true
    `evidence_before_write(score_doc, artifact_sha)` -> the envelope a write path must carry
S10 N28 and S12 verify_eval_verdict call assert_verified on the complete SC09 score document.
S12 has a conditional recoverable file-transaction interface requiring separate host receipts.
Recorded scores and these checks do not authenticate those receipts or prove an actual rerun.

Exit codes
    0  PASSED and, where the tier arithmetic allows it, `verified` derived true
    2  self-grading: the adjudicating instrument id is one of the loop's metric ids [contract]
    3  FAILED verdict (regression, per-sample regression, below min improvement, repeats short,
       answer material visible at score time, bundle digest drift) -- always blocking
    4  UNVERIFIED: nothing failed, but no tier may certify it; promotion forbidden (08:55-08:59)
    5  refused input: unreadable/unparseable bundle, wrong stage, unusable run results,
       instrument id does not match the frozen instrument, answer file missing

Stdlib only; no model, no network, no spawned child process. This script never executes the
corpus: it adjudicates RECORDED before/after run results, because who produces those scores (the
Tier-1 re-run runner / M4 题面) is a separate, unlanded owner (IMPLEMENTATION_GAP below).
"""
from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import kd_eval_freeze as freeze          # noqa: E402  S15: the isolation scan + digest rules
import kd_validate                       # noqa: E402  S09, the sole schema witness (12:171)
import kd_store_layout as layout         # noqa: E402

EXIT_OK = 0
EXIT_SELF_GRADING = 2                    # contract: 2 = 裁决量具 id 与循环内 metric id 相同
EXIT_FAILED = 3
EXIT_UNVERIFIED = 4
EXIT_REFUSED = 5

KIND = "eval-bundle"
CONTRACT_ROW = "12-SKILL-DESIGN-BRIEF.md:124 (S16) / :185 (SC09) / :140 (CM-50 三处共同强制)"
INSTRUMENT = "kd_eval_score/1"

#: verdict vocabulary. Deliberately closed: no WARNING / REVIEW / YELLOW / NEEDS_ATTENTION.
STATUS_PASSED, STATUS_FAILED, STATUS_UNVERIFIED = "PASSED", "FAILED", "UNVERIFIED"

#: reasons that force FAILED -- 08:44 "且变差即 FAILED / 阻断（不允许「只警告不阻断」）" and 08:93
#: P-02. Membership here is what makes a regression red: none of these can produce a warning.
BLOCKING_REASONS = frozenset({
    "regression_vs_baseline", "per_sample_regression", "below_min_improvement",
    "repeats_below_declared", "answer_material_breach", "bundle_digest_mismatch",
    "original_failure_not_identified", "self_grading_collision",
})

EXIT_FOR_STATUS = {STATUS_PASSED: EXIT_OK, STATUS_FAILED: EXIT_FAILED,
                   STATUS_UNVERIFIED: EXIT_UNVERIFIED}


class NotVerified(Exception):
    """CM-50: a durable write may not proceed on an unverified eval claim."""


class SelfGrading(Exception):
    """08:42 (a) / 08:92 P-01: the adjudicating instrument is the in-loop metric."""


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime())


# --------------------------------------------------------------------- inputs
def read_json(path: str):
    with open(path, encoding="utf-8") as fh:            # read-only
        return json.load(fh)


def read_run_results(path: str) -> dict:
    """A before/after product: JSONL rows {sample_id, score[, repeat]}. Scores are the recorded
    per-sample outcomes; this script neither re-runs the corpus nor judges text (08 §1.4 keeps an
    LLM judge out of Round 3's acceptance path, 12:261)."""
    rows = freeze.read_jsonl(path)
    out = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("run result rows must be objects")
        if "sample_id" not in row or "score" not in row:
            raise ValueError(f"{path}: every run row needs sample_id and score")
        score = row["score"]
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise ValueError(f"{path}: sample {row['sample_id']!r} score must be a number")
        if not 0.0 <= float(score) <= 1.0:
            raise ValueError(f"{path}: sample {row['sample_id']!r} score {score} is outside "
                             "[0, 1] -- an out-of-range score is a producer bug, not a data point")
        repeat = row.get("repeat", 1)
        if type(repeat) is not int or repeat < 1 or not isinstance(row["sample_id"], str) or not row["sample_id"]:
            raise ValueError("sample_id must be a string and repeat a positive integer")
        out.append({"sample_id": row["sample_id"], "score": float(score), "repeat": repeat})
    if not out:
        raise ValueError(f"{path}: empty run result -- a before/after with no rows proves "
                         "nothing (08:101 P-10)")
    validate_runs({"rows": out})
    return {"rows": out}


def validate_runs(run: dict, holdout=None) -> None:
    if not isinstance(run, dict) or not isinstance(run.get("rows"), list) or not run["rows"]:
        raise ValueError("run results need nonempty rows")
    seen = set()
    for row in run["rows"]:
        if not isinstance(row, dict) or not isinstance(row.get("sample_id"), str) \
                or not row["sample_id"] or type(row.get("repeat")) is not int or row["repeat"] < 1 \
                or type(row.get("score")) not in (int, float) or not 0 <= row["score"] <= 1:
            raise ValueError("malformed run row")
        key = (row["sample_id"], row["repeat"])
        if key in seen:
            raise ValueError("duplicate sample/repeat observation")
        seen.add(key)
    if holdout is not None and set(holdout) - {sample for sample, _ in seen}:
        raise ValueError("run does not cover every frozen holdout sample")


def mean(rows: list, holdout: set) -> float:
    # Each sample has equal weight, regardless of how many repeats its producer emits.
    selected = [sum(row["score"] for row in rows if row["sample_id"] == sample) /
                sum(1 for row in rows if row["sample_id"] == sample) for sample in sorted(holdout)]
    return sum(selected) / len(selected)


def by_sample(rows: list) -> dict:
    """Per sample, the worst observed score across repeats: a repeat that regressed must not be
    averaged away by a better one."""
    worst = {}
    for row in rows:
        current = worst.get(row["sample_id"])
        if current is None or row["score"] < current:
            worst[row["sample_id"]] = row["score"]
    return worst


def distinct_repeats(rows: list) -> int:
    return len({row["repeat"] for row in rows})


# --------------------------------------------------------------------- the two refusals
def assert_not_self_grading(instrument_id: str, loop_metric_ids: list) -> dict:
    """Five-tuple slot 5, as an executed assertion (08:42 (a) '写成断言而非约定').
    Equality is compared on the normalised id string so a rename that preserves the metric cannot
    slip past, and an empty loop list is itself a refusal: prerequisite (a) cannot be asserted
    against nothing."""
    normalised = {str(item).strip().casefold() for item in loop_metric_ids if str(item).strip()}
    if not normalised:
        raise SelfGrading("the optimisation loop declares no metric id, so the instrument-"
                          "separation assertion has no second term (08:42)")
    collided = sorted({str(item).strip().casefold() for item in loop_metric_ids
                       if str(item).strip()}.intersection({instrument_id.strip().casefold()}))
    audit = {"loop_metric_ids": sorted(str(item) for item in loop_metric_ids if str(item).strip()),
             "collision": bool(collided), "checked_by": "kd_eval_score"}
    if collided:
        raise SelfGrading(f"the adjudicating instrument id {instrument_id!r} is also an "
                          f"optimisation-loop metric id ({audit['loop_metric_ids']}) -- "
                          "self-grading, refused (P-01, 08:92)")
    return audit


def recheck_isolation(bundle: dict) -> list:
    """Re-run S15's scan at score time: a skills root gains documents between freeze and score,
    and answer bytes can be edited. Returns breach rows ([] when clean)."""
    paths = [entry["path"] for entry in bundle["answer_material"]["files"]]
    on_disk = []
    for entry in bundle["answer_material"]["files"]:
        if not os.path.isfile(entry["path"]):
            raise ValueError("answer material is missing at score time")
        current = freeze.sha256_file(entry["path"])
        if current != entry["sha256"]:
            on_disk.append({"kind": "answer-text-in-loadable-document",
                            "surface": "answer-material-drift", "document": entry["path"],
                            "sample_id": os.path.basename(entry["path"]).split(".")[0],
                            "excerpt_chars": os.path.getsize(entry["path"])})
    surfaces = {row["name"]: row["root"] for row in bundle["isolation"]["surfaces"]}
    if not surfaces or any(not os.path.isdir(root) for root in surfaces.values()):
        raise ValueError("a declared model-visible surface is missing")
    live = {name: root for name, root in surfaces.items() if os.path.isdir(root)}
    answer_texts = {}
    for entry in bundle["answer_material"]["files"]:
        if os.path.isfile(entry["path"]):
            try:
                doc = read_json(entry["path"])
            except ValueError as exc:
                raise ValueError("answer material is unreadable") from exc
            if not isinstance(doc, dict):
                raise ValueError("answer material must be an object")
            answer_texts[doc.get("sample_id") or os.path.basename(entry["path"]).split(".")[0]] = \
                freeze.norm(doc.get("gold_answer", ""))
    scan = freeze.scan_isolation(answer_texts, [{"path": path, "bytes": 0,
                                                 "owner_sample_id": "n/a"} for path in paths],
                                live) if live else {"breaches": [], "status": "unscanned"}
    if scan["status"] == "unscanned":
        raise ValueError("isolation was not established for every declared surface")
    return sorted(on_disk + scan["breaches"],
                  key=lambda b: (b["kind"], b["document"], b["sample_id"]))


# --------------------------------------------------------------------- 08 §1.6 verified
def _tier0(bundle: dict, recomputed_digest: str, isolation_breaches: list) -> dict:
    """Tier-0 is a BLOCKING gate and never grants verified (08:20-08:24): here it is the bundle's
    own integrity facts -- SC09 shape, digest recomputation, isolation recheck."""
    checks = {
        "bundle_stage_is_freeze": bundle.get("stage") == "freeze",
        "digest_matches": recomputed_digest == bundle["bundle_digest"],
        "isolation_still_clean": not isolation_breaches
        and bundle["isolation"]["status"] == "proven-clean",
    }
    return {"status": "satisfied" if all(checks.values()) else "unsatisfied",
            "checks": checks,
            "grants_verified": False}


def _tier1(bundle: dict, before: dict, after: dict) -> dict:
    """Tier-1, the default standard (08:27-08:36): re-run the sample that first failed and it
    turns green, AND the test bites. Bite here is not a metaphor: the before-run must show that
    sample failing (score 0.0) and the after-run must show it passing (1.0). An eval whose
    original-failure sample already passed before the change cannot fail on the old behaviour, so
    it is decorative (CM-48, 06:266 '必须能识别原缺陷')."""
    subject = bundle["subject"]
    original = subject["original_failure_sample_id"]
    before_row, after_row = by_sample(before["rows"]), by_sample(after["rows"])
    holdout = set(bundle["splits"]["holdout"])
    facts = {
        "original_failure_in_holdout": original in holdout,
        "before_scored_zero": before_row.get(original) == 0.0,
        "after_scored_one": after_row.get(original) == 1.0,
        "rerun_claimed_reproducible": subject.get("reproducible_rerun_claimed") is True,
        "kind_is_reproducible_execution": subject.get("sample_kind") == "reproducible-execution",
    }
    satisfied = all(facts.values())
    reason = ("re-ran the original failing sample inside the adjudicating holdout: 0.0 -> 1.0, "
              "and the operator declared it reproducible (08:29)" if satisfied else
              "; ".join(f"{key}={value!r}" for key, value in facts.items() if not value)
              + " -- Tier-1 not satisfied (08:27-08:36)")
    return {"status": "satisfied" if satisfied else "unsatisfied", "facts": facts,
            "reason": reason, "grants_verified": satisfied}


def _tier2(bundle: dict) -> dict:
    """Tier-2 = the frozen independent holdout, valid only with ALL four prerequisites (08:41)."""
    prereqs = bundle["prerequisites"]
    unsatisfied = sorted(key for key, value in prereqs.items() if value.get("status") != "satisfied")
    if bundle["subject"].get("sample_kind") != "generalisable-text-asset":
        unsatisfied.append("subject_is_not_generalisable_text_asset")
    return {"status": "satisfied" if not unsatisfied else "unsatisfied",
            "unsatisfied": unsatisfied,
            "reason": ("all four of §1.3 (a)(b)(c)(d) satisfied over a frozen adjudicator-only "
                       "holdout" if not unsatisfied
                       else "prerequisite(s) unsatisfied: %s -- Tier-2 invalid, fall back to "
                            "Tier-1 or Tier-4 (08:41)" % ", ".join(unsatisfied)),
            "grants_verified": not unsatisfied}


def _verified_claim(tier0: dict, tier1: dict, tier2: dict, certification_ok: bool) -> dict:
    """verified := Tier-0 ∧ (Tier-1 ∨ Tier-2)  (08:65, 12:458). Tier-0 is required but never
    sufficient (08:24). `certification_ok` is S16's own arithmetic-and-blocking decision: no tier
    grants verified over a regression, and Tier-2 needs its (c) triple to exist."""
    granted = tier0["status"] == "satisfied" and certification_ok and (
        tier1["status"] == "satisfied" or tier2["status"] == "satisfied")
    return {
        "value": bool(granted),
        "formula": "verified := Tier-0 ∧ (Tier-1 若样本可复现 ∨ Tier-2 若为可泛化文本资产) "
                   "[08-EVAL-STRATEGY.md:64-68]",
        "tier0": tier0, "tier1": tier1, "tier2": tier2, "certification_ok": bool(certification_ok),
        "five_tuple_complete": True,
    }


# --------------------------------------------------------------------- scoring
def score_bundle(bundle: dict, before: dict, after: dict, instrument_audit: dict) -> dict:
    """The adjudication. Returns the SC09 stage='score' document (verdict + five-tuple).

    No number is invented: `min_improvement` / `repeats` / `tolerance` are read from the frozen
    bundle's prerequisite (c). When they are absent the improvement cannot be certified, which
    yields UNVERIFIED (a legal state, 08:55) rather than a defaulted floor. A regression needs no
    number at all: `after_mean < before_mean` is the drop, and 08:44 requires it to be FAILED."""
    if not kd_validate.validate_artifact(KIND, bundle).get("valid") or bundle.get("stage") != "freeze":
        raise ValueError("S16 requires a valid SC09 freeze document")
    holdout = set(bundle["splits"]["holdout"])
    validate_runs(before, holdout)
    validate_runs(after, holdout)
    assert_not_self_grading(bundle["five_tuple"]["instrument_id"],
                           bundle["five_tuple"]["instrument_also_optimised_against"]["loop_metric_ids"])
    thresholds = (bundle["prerequisites"]["c_min_improvement_repeats_tolerance"]["thresholds"])
    min_improvement, repeats_needed, tolerance = (thresholds.get("min_improvement"),
                                                 thresholds.get("repeats"),
                                                 thresholds.get("tolerance"))
    before_mean, after_mean = mean(before["rows"], holdout), mean(after["rows"], holdout)
    delta = after_mean - before_mean
    floor = tolerance if isinstance(tolerance, (int, float)) else 0.0
    before_worst, after_worst = by_sample(before["rows"]), by_sample(after["rows"])

    reasons: list = []
    regression = delta < -floor
    per_sample_worse = sorted(sample for sample in holdout
                              if after_worst.get(sample, 0.0) < before_worst.get(sample, 0.0)
                              - floor)
    thresholds_missing = any(value is None for value in (min_improvement, repeats_needed,
                                                          tolerance))
    if regression:
        reasons.append("regression_vs_baseline")
    if per_sample_worse:
        reasons.append("per_sample_regression")
    repeats_observed = min(len({row["repeat"] for row in run["rows"] if row["sample_id"] == sample})
                           for run in (before, after) for sample in holdout)
    if isinstance(repeats_needed, int) and repeats_observed < repeats_needed:
        reasons.append("repeats_below_declared")
    if not thresholds_missing and not regression and not per_sample_worse \
            and delta < float(min_improvement) - floor:
        reasons.append("below_min_improvement")
    if thresholds_missing:
        # informative only: it disqualifies the Tier-2 route, it does NOT disqualify Tier-1,
        # which is the default standard and needs no tunable number (08:27 "默认口径")
        reasons.append("thresholds_undecided")
    if not reasons:
        reasons.append("met_threshold")

    isolation_breaches = recheck_isolation(bundle)
    recomputed = freeze.bundle_digest(bundle)
    if isolation_breaches:
        reasons.insert(0, "answer_material_breach")
    if recomputed != bundle["bundle_digest"]:
        reasons.insert(0, "bundle_digest_mismatch")
    if bundle["subject"]["original_failure_sample_id"] not in holdout:
        reasons.append("original_failure_not_identified")

    tier0 = _tier0(bundle, recomputed, isolation_breaches)
    tier1 = _tier1(bundle, before, after)
    tier2 = _tier2(bundle)

    blocking_any = any(item in reasons for item in BLOCKING_REASONS)
    # 08:65 verified := Tier-0 ∧ ( Tier-1（若样本可复现） ∨ Tier-2（若为可泛化文本资产） ).
    # Tier-1's own criterion is the re-run of the original failure with bite, which needs no
    # tunable number; Tier-2 additionally requires the (c) triple to exist and to have been met.
    tier2_certifying = (tier2["status"] == "satisfied" and not thresholds_missing
                        and "met_threshold" in reasons)
    certification_ok = (not blocking_any
                        and (tier1["status"] == "satisfied" or tier2_certifying))
    verified = _verified_claim(tier0, tier1, tier2, certification_ok)

    if blocking_any:
        status = STATUS_FAILED
    elif verified["value"]:
        status = STATUS_PASSED
        if tier1["status"] == "satisfied" and "met_threshold" not in reasons:
            reasons.append("tier1_rerun_green")
    else:
        status = STATUS_UNVERIFIED
        reasons.append("prerequisite_unsatisfied")
    blocking = status != STATUS_PASSED

    five_tuple = {
        "instrument_id": bundle["five_tuple"]["instrument_id"],
        "dataset_id": bundle["five_tuple"]["dataset_id"],
        "threshold": (None if min_improvement is None or repeats_needed is None
                      or tolerance is None else {"min_improvement": min_improvement,
                                                 "repeats": repeats_needed,
                                                 "tolerance": tolerance}),
        "run_result": {
            "before_mean": before_mean, "after_mean": after_mean, "delta": delta,
            "tolerance_applied": floor, "holdout_size": len(holdout),
            "repeats_observed": repeats_observed,
            "per_sample_worse": per_sample_worse,
            "original_failure": {
                "sample_id": bundle["subject"]["original_failure_sample_id"],
                "before_score": before_worst.get(bundle["subject"]["original_failure_sample_id"]),
                "after_score": after_worst.get(bundle["subject"]["original_failure_sample_id"]),
            },
            "produced_by": "recorded before/after run results; kd_eval_score did not execute the "
                           "corpus",
        },
        "instrument_also_optimised_against": bundle["five_tuple"]["instrument_also_optimised_against"],
    }

    doc = dict(bundle)
    doc["stage"] = "score"
    doc["at"] = _now()
    doc["isolation"] = dict(bundle["isolation"],
                            status=("breach" if isolation_breaches else "proven-clean"),
                            breaches=isolation_breaches, checked_at=_now())
    doc["five_tuple"] = five_tuple
    doc["verdict"] = {"status": status, "blocking": blocking, "verified": bool(verified["value"]),
                      "regression_detected": bool(regression or per_sample_worse),
                      "reasons": sorted(set(reasons)) or ["met_threshold"]}
    doc["provenance"] = {"produced_by": "S16 kd_eval_score", "script": "kd_eval_score.py",
                        "model_id": "none", "contract_row": CONTRACT_ROW}
    doc["notes"] = dict(bundle["notes"], IMPLEMENTATION_GAPS=sorted(set(
        list(bundle["notes"]["IMPLEMENTATION_GAPS"]) + [
            "IMPLEMENTATION_GAP: who produces per-sample before/after scores (Tier-1 re-run "
            "runner / M4 题面, 12:136) is not S16's owner and is not landed / DEFERRED id "
            "DD-3-sub20",
            "IMPLEMENTATION_GAP: the exact condition under which a stored `verified` may be "
            "granted to a pure-prompt asset is undecided, so _tier1 requires an explicit "
            "reproducible-execution kind and refuses otherwise / DEFERRED id DD-3-sub24",
            "IMPLEMENTATION_GAP: LLM-as-judge stays out of the acceptance path this round, so "
            "slot 4 holds recorded deterministic scores only / DEFERRED id DD-3-sub21 (12:261)",
        ])))
    # the derived-only extras a reader needs, kept OUTSIDE the closed SC09 field set: they ride
    # on the stdout envelope, never inside the witnessed document
    return {"document": doc, "verified_detail": verified,
            "isolation_breaches": isolation_breaches, "recomputed_digest": recomputed}


# --------------------------------------------------------------------- CM-50 hook
def verification_evidence(score_doc: dict, artifact_sha: str) -> dict:
    """The row S12 appends to an SC04 artifact's `verification[]` (05 §2 row 7: appended by the
    eval runner; the body may never edit an existing verdict). Shape is SC04's own required set:
    eval_id / verdict / run_at / run_evidence_hash / artifact_sha.

    `artifact_sha` is supplied by the writer that owns the record, never read off the bundle: a
    verdict expires against a different artifact_sha, which is what stops a stale PASSED from
    authorising a later body (08:97 P-07 -- an `Implemented`-style claim must have a call site)."""
    if not isinstance(artifact_sha, str) or not re.fullmatch(r"[0-9a-f]{64}", artifact_sha):
        raise ValueError("verification_evidence needs the artifact's 64-hex content_hash from the "
                         "write path (S10/S12's job); refusing to mint a row that SC04 would "
                         "reject")
    payload = json.dumps({"five_tuple": score_doc["five_tuple"], "verdict": score_doc["verdict"],
                          "bundle_digest": score_doc["bundle_digest"],
                          "dataset_id": score_doc["dataset_id"]},
                         sort_keys=True, ensure_ascii=False)
    return {
        "eval_id": "%s@%s" % (score_doc["five_tuple"]["instrument_id"],
                              score_doc["bundle_digest"][:12]),
        "verdict": score_doc["verdict"]["status"],
        "run_at": score_doc["at"],
        "run_evidence_hash": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
        "artifact_sha": artifact_sha,
    }


def assert_verified(score_doc: dict) -> None:
    """CM-50's write-before-evidence predicate: a durable write may not proceed on a claim that
    this function cannot recompute from the document's own fields."""
    valid = kd_validate.validate_artifact(KIND, score_doc).get("valid")
    verdict = score_doc.get("verdict") if isinstance(score_doc, dict) else None
    verdict = verdict if isinstance(verdict, dict) else {}
    if not valid or score_doc.get("stage") != "score" or verdict.get("verified") is not True \
            or verdict.get("status") != STATUS_PASSED or verdict.get("blocking") is not False \
            or verdict.get("regression_detected") is not False:
        # This boundary receives untrusted score documents. Neither the
        # caller's status nor its reasons may be echoed into host logs.
        raise NotVerified("SC09 score invalid or unverified: promotion must not be written")
    try:
        if freeze.bundle_digest(score_doc) != score_doc["bundle_digest"] or recheck_isolation(score_doc):
            raise ValueError("frozen inputs or isolation changed")
        five = score_doc["five_tuple"]
        audit = five["instrument_also_optimised_against"]
        assert_not_self_grading(five["instrument_id"], audit["loop_metric_ids"])
        result, subject = five["run_result"], score_doc["subject"]
        if not isinstance(result, dict) or result.get("per_sample_worse") != []:
            raise ValueError("missing or regressing run evidence")
        for key in ("before_mean", "after_mean", "delta", "tolerance_applied"):
            if type(result.get(key)) not in (int, float):
                raise ValueError("run evidence requires numeric measurements")
        if result["delta"] != result["after_mean"] - result["before_mean"] \
                or not 0 <= result["before_mean"] <= 1 or not 0 <= result["after_mean"] <= 1 \
                or result["tolerance_applied"] < 0 \
                or type(result.get("repeats_observed")) is not int or result["repeats_observed"] < 1 \
                or result.get("holdout_size") != len(score_doc["splits"]["holdout"]) \
                or five["dataset_id"] != score_doc["dataset_id"] \
                or subject["original_failure_sample_id"] not in score_doc["splits"]["holdout"]:
            raise ValueError("inconsistent measurement identity/arithmetic")
        tier1 = (subject["sample_kind"] == "reproducible-execution"
                 and subject["reproducible_rerun_claimed"] is True
                 and result.get("original_failure", {}).get("sample_id") == subject["original_failure_sample_id"]
                 and type(result["original_failure"].get("before_score")) in (int, float)
                 and type(result["original_failure"].get("after_score")) in (int, float)
                 and result["original_failure"].get("before_score") == 0.0
                 and result["original_failure"].get("after_score") == 1.0)
        triple = five["threshold"]
        if isinstance(triple, dict) and (result["repeats_observed"] < triple["repeats"]
                                        or result["delta"] < triple["min_improvement"] - triple["tolerance"]):
            raise ValueError("declared repeat/improvement requirements not met")
        tier2 = (_tier2(score_doc)["status"] == "satisfied" and isinstance(triple, dict)
                 and result.get("repeats_observed", 0) >= triple["repeats"]
                 and result.get("delta", -1) >= triple["min_improvement"] - triple["tolerance"])
        if not (tier1 or tier2) or any(reason in BLOCKING_REASONS for reason in verdict["reasons"]):
            raise ValueError("no eligible verification tier")
        if type(result.get("delta")) not in (int, float) or result["delta"] < -result.get("tolerance_applied", 0):
            raise ValueError("invalid or regressing aggregate evidence")
    except (OSError, ValueError, KeyError, TypeError, AttributeError, SelfGrading) as exc:
        raise NotVerified("S16 could not re-establish the verification predicates") from exc


def evidence_before_write(score_doc: dict, artifact_sha: str) -> dict:
    """The envelope S10 checks before admitting, and S12 re-checks before committing. It carries
    the five-tuple plus the SC04 row, so there is exactly one object whose presence and shape the
    write path can require."""
    assert_verified(score_doc)
    return {"eval_id": None, "row": verification_evidence(score_doc, artifact_sha),
            "five_tuple": score_doc["five_tuple"],
            "verified": True, "instrument": INSTRUMENT}


def downstream_hooks() -> dict:
    """Named hand-off rather than a silent assumption: does the write path already require this
    evidence? Probed against the real signatures at call time, so the answer changes when W3-A's
    gate or S12 lands the parameter."""
    out = {}
    for module_name, function_name in (("kd_gate", "evaluate_promotion"),
                                       ("kd_write_txn", "commit_batch")):
        label = "%s.%s" % (module_name, function_name)
        try:
            module = __import__(module_name)
            function = getattr(module, function_name)
        except (ImportError, AttributeError) as exc:
            out[label] = "NOT_LANDED_YET (%s)" % exc
            continue
        names = list(inspect.signature(function).parameters)
        out[label] = ("accepts eval evidence" if any("eval" in name or "verdict" in name
                                                     for name in names)
                      else "NOT_LANDED_YET: signature is %s -- no eval/verdict parameter, so "
                           "kd_eval_score's evidence_before_write has no call site there yet "
                           "(12:140 assigns it to S10 + S16 + S12 jointly)" % names)
    return out


# --------------------------------------------------------------------- CLI
class UsageError(Exception):
    """argparse's exit code 2 is a contract code here (self-grading), so usage errors exit 5."""


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise UsageError(message)


def atomic_write_text(path: str, text: str) -> None:
    layout.assert_staging_path(path)
    layout.assert_staging_path(path + ".tmp")
    if os.path.lexists(path + ".tmp"):
        raise ValueError("refusing an existing temporary output")
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)   # KD-WRITE-EXEMPT: parent dir of S16's derived verdict/envelope output at the operator-named --out, never a store path
    tmp = path + ".tmp"
    with open(tmp, "x", encoding="utf-8") as fh:   # KD-WRITE-EXEMPT: tmp half of one write-once rename for S16's derived verdict document
        fh.write(text)                # KD-WRITE-EXEMPT: the derived verdict body, written once by this single emit path
        fh.flush()
        os.fsync(fh.fileno())               # KD-WRITE-EXEMPT: durability of the derived tmp only; a verdict is evidence, not an authority
    os.replace(tmp, path)                   # KD-WRITE-EXEMPT: publish S16's derived verdict document at the operator-named --out


def main(argv=None) -> int:
    ap = ArgumentParser(
        prog="kd_eval_score.py",
        description=("S16: adjudicate a frozen eval bundle (SC09 stage='freeze') against recorded "
                     "before/after run results, refuse self-grading, make any regression FAILED, "
                     "and emit the verdict plus the five-tuple audit record. Contract "
                     "12-SKILL-DESIGN-BRIEF.md:124, authority 08-EVAL-STRATEGY.md §1.3/§1.6, "
                     "schema SC09. This script does not run the corpus and does not default any "
                     "threshold."),
        epilog=("exit codes: 0 PASSED; 2 self-grading (裁决量具 id == 循环内 metric id) "
                "[contract]; 3 FAILED (变差即 FAILED, never a warning); 4 UNVERIFIED (legal, "
                "no promotion right, 08:55-08:59); 5 refused input."))
    ap.add_argument("--bundle", metavar="FILE", required=True,
                    help="SC09 stage='freeze' document produced by kd_eval_freeze")
    ap.add_argument("--before", metavar="FILE", required=True,
                    help="JSONL run results for the baseline product: sample_id, score[, repeat]")
    ap.add_argument("--after", metavar="FILE", required=True,
                    help="JSONL run results for the candidate product: sample_id, score[, repeat]")
    ap.add_argument("--instrument-id", metavar="ID", required=True,
                    help="five-tuple slot 1; must equal the bundle's frozen instrument id and "
                         "must differ from every optimisation-loop metric id")
    ap.add_argument("--loop-metric-id", action="append", default=[], metavar="ID",
                    help="an optimisation-loop metric id to assert against (repeatable; the "
                         "bundle's frozen list is always included)")
    ap.add_argument("--artifact-sha", metavar="SHA",
                    help="the 64-hex content_hash of the SC04 artifact this verdict will "
                         "authorise; supplied by the write path (S10/S12). Without it the CM-50 "
                         "evidence row is reported as unbindable, and no write may proceed.")
    ap.add_argument("--out", metavar="FILE", help="also write the envelope JSON here")
    ap.add_argument("--emit", choices=("envelope", "document"), default="envelope",
                    help="what to print: the envelope (verdict + five-tuple + CM-50 hook "
                         "availability + downstream probe) or the raw SC09 document")
    args = ap.parse_args(argv)

    try:
        bundle = read_json(args.bundle)
    except (OSError, ValueError) as exc:
        return refused(args, "UNREADABLE_BUNDLE", str(exc))
    if not isinstance(bundle, dict) or bundle.get("stage") != "freeze":
        return refused(args, "NOT_A_FROZEN_BUNDLE",
                       "S16 scores a freeze document; scoring a stage='score' document would "
                       "let yesterday's verdict certify today's artifact")
    if not kd_validate.validate_artifact(KIND, bundle).get("valid"):
        return refused(args, "SC09_VALIDATION_FAILED", "invalid frozen bundle")
    if bundle["five_tuple"]["instrument_id"] != args.instrument_id:
        return refused(args, "INSTRUMENT_ID_MISMATCH",
                       "the bundle froze instrument %r but --instrument-id says %r -- an "
                       "instrument id cannot be swapped at score time (08:42 (a))"
                       % (bundle["five_tuple"]["instrument_id"], args.instrument_id))
    try:
        before, after = read_run_results(args.before), read_run_results(args.after)
    except (OSError, ValueError) as exc:
        return refused(args, "UNUSABLE_RUN_RESULTS", str(exc))
    holdout = set(bundle["splits"]["holdout"])
    for label, run in (("before", before), ("after", after)):
        seen = {row["sample_id"] for row in run["rows"]}
        absent = sorted(holdout - seen)
        if absent:
            return refused(args, "RUN_INCOMPLETE",
                           f"the {label} run result has no row for holdout sample(s) {absent} -- "
                           "a verdict computed over a partial adjudicating set is not the frozen "
                           "measurement (08:67 slot 2)")

    loop_ids = sorted(set(bundle["prerequisites"]["a_instrument_separation"]["loop_metric_ids"])
                      | {item for item in args.loop_metric_id if item.strip()})
    try:
        audit = assert_not_self_grading(args.instrument_id, loop_ids)
    except SelfGrading as exc:
        # contract exit 2. Refused BEFORE any score is computed: a self-graded number must not
        # exist even as an artifact a later reader might cite.
        envelope = {"status": "refused", "code": "SELF_GRADING_COLLISION", "detail": str(exc),
                    "five_tuple": {"instrument_id": args.instrument_id,
                                   "dataset_id": bundle["dataset_id"], "threshold": None,
                                   "run_result": None,
                                   "instrument_also_optimised_against": {
                                       "loop_metric_ids": loop_ids, "collision": True,
                                       "checked_by": "kd_eval_score"}},
                    "verdict": {"status": STATUS_FAILED, "blocking": True, "verified": False,
                                "regression_detected": False,
                                "reasons": ["self_grading_collision"]},
                    "downstream": downstream_hooks()}
        emit(args, envelope)
        return EXIT_SELF_GRADING

    try:
        result = score_bundle(bundle, before, after, audit)
    except (OSError, ValueError, SelfGrading) as exc:
        return refused(args, "UNUSABLE_EVAL_EVIDENCE", str(exc))
    doc = result["document"]
    validation = kd_validate.validate_artifact(KIND, doc)
    envelope = {
        "status": doc["verdict"]["status"],
        "exit_code": EXIT_FOR_STATUS[doc["verdict"]["status"]],
        "code": None,
        "verdict": doc["verdict"], "five_tuple": doc["five_tuple"],
        "verified_derivation": result["verified_detail"],
        "bundle_digest": doc["bundle_digest"], "recomputed_digest": result["recomputed_digest"],
        "isolation_breaches_at_score": result["isolation_breaches"],
        "schema_validation": {"valid": bool(validation.get("valid")), "code": validation.get("code"),
                              "violations": list(validation.get("violations", []))[:8]},
        "cm50_evidence": None, "downstream": downstream_hooks(),
        "blocking": doc["verdict"]["blocking"],
    }
    if not validation.get("valid"):
        # a verdict SC09 cannot witness is not a verdict: refuse loudly instead of returning the
        # status-derived code, which would let a malformed document read as an adjudication
        envelope["status"] = "refused"
        envelope["code"] = "SC09_VALIDATION_FAILED"
        envelope["blocking"] = True
        emit(args, envelope, doc)
        return EXIT_REFUSED
    if args.artifact_sha:
        try:
            envelope["cm50_evidence"] = evidence_before_write(doc, args.artifact_sha)
        except (NotVerified, ValueError) as exc:
            envelope["cm50_evidence"] = {"refused": True, "detail": str(exc)}
    else:
        envelope["cm50_evidence"] = {
            "unbindable": True,
            "detail": "no --artifact-sha given: the SC04 verification[] row needs the content "
                      "hash the write path owns, so S16 reports the hook as unavailable instead "
                      "of inventing one (12:140 -- S10 + S16 + S12 jointly)",
            "row_schema": ["eval_id", "verdict", "run_at", "run_evidence_hash", "artifact_sha"]}
    return envelope["exit_code"] if emit(args, envelope, doc) else EXIT_REFUSED


def emit(args, envelope, score_doc: dict = None) -> bool:
    payload = score_doc if (args.emit == "document" and score_doc is not None) else envelope
    if args.out:
        try:
            atomic_write_text(args.out, json.dumps(envelope, ensure_ascii=False, indent=1) + "\n")
        except (OSError, ValueError, layout.LayoutViolation) as exc:
            print(f"kd_eval_score: could not write --out {args.out}: {exc}", file=sys.stderr)
            return False
    print(json.dumps(payload, ensure_ascii=False, indent=1))
    return True


def refused(args, code: str, detail: str) -> int:
    emit(args, {"status": "refused", "code": code, "detail": detail,
                "downstream": downstream_hooks()})
    return EXIT_REFUSED


if __name__ == "__main__":
    try:
        sys.exit(main())
    except UsageError as exc:
        print(f"kd_eval_score: usage error: {exc}", file=sys.stderr)
        sys.exit(EXIT_REFUSED)
