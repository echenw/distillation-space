"""S07 -- kd_proxy_candidates: the CHEAP stage that only PROPOSES what M1 may look at.

Round 2 provenance (contract row, verbatim from 12-SKILL-DESIGN-BRIEF.md:115, mirrored in
.distill/round-3/SCRIPTS-CONTRACT-MAP.md:21 and .distill/round-3/wave-2/_dispatch/w2b.json)
  inputs  分组后的条目集 + 阈值
  outputs candidate_pairs.json（Tier-3 排序信号）
  exit    0=空集⇒下游跳过 M1；分数**永不进晋升记录**
  clusters （支撑 CM-42 分界；簇 CM-17/CM-41 SUPPORTING）        pipeline 步 9 / 行 5
  04-DETERMINISTIC-VS-LLM.md:51 (row 5) 候选生成层唯一负责：Jaccard / keyword overlap 便宜 proxy，
  阈值可测，把 O(n²) 压到常数级；命中为空即跳过语义判定 | 判定层：只在 candidate 内判「是否同一条」
  04-DETERMINISTIC-VS-LLM.md:103-105     step 9 近似 proxy 产 candidate pairs (det) -> step 11
  语义判重 (llm). CM-42 carries the deterministic/LLM split; CM-17/CM-41 are SUPPORTING, so S07
  mines a cheap overlap signal and proposes -- it never decides, never merges, never counts.

The one defence in this file: 「分数永不进晋升记录」 (the proxy-metric leak).
Round 1 caught the shape once (a `times_applied` counter with no writer still drove sorting,
sampling, eval weights and display); Round 2 made it a rule (05-DATA-MODEL.md §5.4). Documenting
it is not enough, so containment here is mechanical:
  * every emitted score is labelled `score_semantics = tier_3_ranking_only_not_evidence_of_recurrence`
    and the document states what it must NOT be read as (`must_not_be_read_as`);
  * `assert_not_promotion_payload(payload, scores=...)` refuses (non-zero exit, named reasons) any
    payload that puts a proxy score -- by field name, by value, or as a literal / proxy citation
    inside prose -- into a promotion-shaped record. The promotion-shaped field set is read from
    schemas/artifact.schema.json, schemas/learning.schema.json and schemas/pattern.schema.json at
    call time (no hand-copied second authority), plus the gate-verdict keys S10 emits
    (`kd_gate.evaluate_promotion` -> promotable / required_* / decision_digest) and the Pattern and
    Artifact counter names (05 §6). S10 and S12 are meant to call it before building a promotion
    record; S07 already calls it on its own output before writing (containment.guarded_by_this_run).
  * a guard that cannot fail is worse than none: a previous draft used `... or True`. The refusal is
    therefore a positive detection over a real field set, and
    tests/knowledge-compiler/test_w2b_proxy.py carries a mutation control that removes the refusal
    (and one that reinstates the tautological form) in a TEMP COPY of this module, proving the
    leaking payload passes there -- the negative control goes red-without-the-guard, not green
    either way.

Threshold is data, never a number baked in here. Round 2 deferred the numeric thresholds
(DEFERRED-PARAMETERS.yaml: DD-6-sub43 「0.7 Jaccard 类 ... 必须先有度量」, DD-2-sub16 (τ for
auto-merge), DD-2-sub18 (T0 equality vs Jaccard threshold consistency), DD-4-sub31 (any float
score criterion needs one Owner + offline calibration)). S07 reads the single-source config the
gate reads -- `references/promotion-config.json`, through `kd_gate.load_config`, whose `status`
must stay `provisional` -- and that file carries only `min_independent_cohorts` /
`min_distinct_evidence`. Neither is a similarity cut, so S07 does not invent one: it takes the cut
from the operator at run time (`--min-score`) and records its provenance, or refuses with exit 4
naming the DEFERRED ids. Nothing here edits that file, adds a key to it, or reads it as `adopted`.

CM-41 / CM-17 SUPPORTING: S07 is the cheap pre-filter for an expensive model stage. It has NO
durable write path -- no store, no journal, no ledger, no promotion record. Its only write is the
derived CLI artifact at --out, rebuilt from the grouping document on every run.

Input shape is consumed through `load_grouping()`, which names every field S07 needs (W2-A is
changing which fields S05/S06 *require* but was told not to change this document shape), so a
shape change is a loud exit 2, never a silent empty candidate set.

python3 stdlib only. kd_gate / kd_provenance are imported, never edited.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import kd_gate                     # noqa: E402  the ONE reader of the promotion config
import kd_provenance as prov       # noqa: E402  Wave 0 kernel; only its error type is reused here

SCHEMA = "kd_proxy_candidates/candidate_pairs/1"
SIGNAL_TIER = "tier-3-ranking-signal"
SCORE_SEMANTICS = "tier_3_ranking_only_not_evidence_of_recurrence"

# --------------------------------------------------------------------------- exit codes
EXIT_OK = 0                    # contract: 0 also on an EMPTY candidate set => downstream skips M1
EXIT_INPUT_ERROR = 1           # unreadable / malformed input, out-of-range --min-score
EXIT_GROUPING_SHAPE = 2        # the S06 document lacks a field S07 names (fail loud, not vacuous)
EXIT_CONFIG_UNUSABLE = 3       # the single-source config is no longer status=provisional, or unreadable
EXIT_THRESHOLD_UNDECIDED = 4   # no similarity threshold in the config and none supplied -- refuse
EXIT_PROMOTION_LEAK = 5        # assert_not_promotion_payload fired (分数永不进晋升记录)

DEFERRED_THRESHOLD_IDS = ("DD-6-sub43", "DD-2-sub16", "DD-2-sub18", "DD-4-sub31")

#: keys the config WOULD have to carry for S07 to source the cut itself. It carries none today,
#: which is why the operator supplies the value per run (and why exit 4 exists).
SIMILARITY_CONFIG_KEYS = ("min_proxy_score", "min_candidate_pair_score", "min_jaccard")

# --------------------------------------------------------------------------- containment
PACKAGE_ROOT = os.path.abspath(os.path.join(HERE, os.pardir))
SCHEMA_FILES = ("schemas/artifact.schema.json",     # SC04 -- the durable record S12 writes
                "schemas/learning.schema.json",     # SC02 -- Learning
                "schemas/pattern.schema.json")      # SC03 -- Pattern, home of the counters
#: the verdict S10 emits: kd_gate.evaluate_promotion keys + what kd_gate.apply_mutation reads
GATE_VERDICT_KEYS = ("promotable", "decision_digest", "human_approved",
                    "required_independent_cohorts", "required_distinct_evidence", "support")
#: one of these alone makes a record a decision carrier (05 §6 counters, §5.4 admission)
SOLO_DECISION_KEYS = ("promotable", "decision_digest", "human_approved", "state", "written_by",
                      "revision", "absorbed_into", "verification", "claims", "evidence_refs",
                      "support_count", "distinct_occurrence_count", "contradiction_count",
                      "near_duplicate_count", "last_attempted_count", "use_count", "view_count",
                      "patch_count", "pattern_id", "pattern_ref", "artifact_id", "learning_id",
                      "validation_state", "decay_type", "pinned")
#: a field name that says "this number ranks or weights something"
SCORE_NAME_RE = re.compile(r"score|rank|weight|similarity|confidence|tier[_-]?3|proxy", re.I)
#: prose that cites the cheap signal as a reason -- the laundering path
SCORE_PROSE_RE = re.compile(r"tier[ _-]?3|proxy[ _-]?score|candidate_pairs|排序信号", re.I)


class PromotionLeakRefusal(Exception):
    """A proxy score reached (or was aliased / laundered into) a promotion-shaped record."""

    def __init__(self, findings: list):
        super().__init__("; ".join(f["message"] for f in findings))
        self.findings = findings


class GroupingShapeError(Exception):
    """The grouping document does not carry a field S07 names."""

    def __init__(self, findings: list):
        super().__init__("; ".join(f["message"] for f in findings))
        self.findings = findings


class ConfigUnusable(Exception):
    """The single-source promotion config cannot be read as provisional data."""


class UndecidedThreshold(Exception):
    """The similarity cut is neither in the single-source config nor supplied -- exit 4."""


def promotion_field_set() -> set:
    """The promotion-shaped field set, read from the schemas themselves (no hand copy)."""
    keys: set = set()
    for rel in SCHEMA_FILES:
        with open(os.path.join(PACKAGE_ROOT, rel), encoding="utf-8") as fh:   # read-only
            doc = json.load(fh)
        keys |= set(doc.get("properties", {}))
    keys |= set(GATE_VERDICT_KEYS)
    return keys


def _is_promotion_shaped(rec: dict, fields: set) -> bool:
    own = set(rec)
    return len(own & fields) >= 2 or bool(own & set(SOLO_DECISION_KEYS))


def _walk_dicts(node, path: str = "$"):
    if isinstance(node, dict):
        yield path, node
        for key, value in node.items():
            yield from _walk_dicts(value, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from _walk_dicts(value, f"{path}[{index}]")


def _score_literals(score_values: set) -> list:
    """Text forms a score can hide behind in prose: the rounded value and its short reprs."""
    out = []
    for value in score_values:
        out.append(f"{value:.6f}".rstrip("0"))
        out.append(repr(round(value, 6)))
        out.append(str(round(value, 2)))
    return sorted({t for t in out if len(t) >= 4})


def assert_not_promotion_payload(payload, scores=None) -> None:
    """THE refusal. Call it with any payload about to become a promotion record.

    Wiring note for the integrator: S10 calls it on the verdict it hands S12, and S12 calls it on
    every record before the atomic write (passing the round's score set from
    candidate_pairs.json for value-alias detection, or `scores=None` for the name/prose-only
    check). CLI form for pre-commit use: `kd_proxy_candidates.py --guard-payload FILE
    [--guard-scores 0.83,0.5]` -> exit 5 with named findings.
    Containment limits, stated rather than overclaimed: this checks field placement, value aliasing
    and prose citation in a payload tree; it does not prove that a score already summarized into an
    opaque free-text `body` without any numeric or tier wording is absent.

    Raises PromotionLeakRefusal (-> exit 5) carrying named findings; returns None when clean.
    """
    fields = promotion_field_set()
    score_values = set()
    for candidate in (scores or ()):
        try:
            score_values.add(round(float(candidate), 6))
        except (TypeError, ValueError):
            continue
    literals = _score_literals(score_values)
    findings = []
    for path, rec in _walk_dicts(payload):
        if not _is_promotion_shaped(rec, fields):
            continue
        for key, value in rec.items():
            name = str(key)
            if SCORE_NAME_RE.search(name):
                findings.append({"code": "SCORE_FIELD_IN_PROMOTION_RECORD", "path": path,
                                 "field": name,
                                 "message": f"{path}.{name} puts a ranking score into a "
                                            "promotion-shaped record -- 分数永不进晋升记录 (S07 exit)"})
            if isinstance(value, (int, float)) and not isinstance(value, bool) \
                    and round(float(value), 6) in score_values:
                findings.append({"code": "SCORE_VALUE_ALIAS_IN_PROMOTION_RECORD", "path": path,
                                 "field": name,
                                 "message": f"{path}.{name}={value} equals a proxy score: copying "
                                            "or renaming the number is the same leak"})
            if isinstance(value, str) and value.strip():
                if SCORE_PROSE_RE.search(value):
                    findings.append({"code": "PROXY_SIGNAL_CITED_AS_PROMOTION_BASIS", "path": path,
                                     "field": name,
                                     "message": f"{path}.{name} cites the tier-3 proxy as a reason "
                                                "or basis; a ranking signal is not evidence of "
                                                "recurrence"})
                elif any(lit in value for lit in literals):
                    findings.append({"code": "SCORE_LITERAL_IN_PROMOTION_PROSE", "path": path,
                                     "field": name,
                                     "message": f"{path}.{name} carries a proxy score as a literal "
                                                "inside prose -- the field name moved, the leak did not"})
    if findings:
        raise PromotionLeakRefusal(findings)


# --------------------------------------------------------------------------- S06 shape (read-only)
REQUIRED_TOP = ("schema_version", "support_semantics", "groups", "verdicts", "result_digest")
REQUIRED_GROUP = ("identity_digest", "canonical_evidence_id", "canonical_locator",
                  "content_hashes", "member_count", "support", "possible_duplicate")
REQUIRED_SUPPORT = ("independent_cohorts", "independent_cohort_count")


def load_grouping(path: str) -> dict:
    """Name every field S07 consumes, so a shape change shows up as exit 2 instead of zero pairs."""
    try:
        with open(path, encoding="utf-8") as fh:                               # read-only
            doc = json.load(fh)
    except OSError as exc:
        raise GroupingShapeError([{"code": "GROUPING_UNREADABLE",
                                   "message": f"{path}: {exc}"}]) from exc
    except ValueError as exc:
        raise GroupingShapeError([{"code": "GROUPING_NOT_JSON",
                                   "message": f"{path}: {exc}"}]) from exc
    if not isinstance(doc, dict):
        raise GroupingShapeError([{"code": "GROUPING_NOT_AN_OBJECT",
                                   "message": f"{path}: expected an object"}])
    findings = []
    missing = [k for k in REQUIRED_TOP if k not in doc]
    if missing:
        findings.append({"code": "GROUPING_MISSING_TOP_FIELD", "fields": missing,
                         "message": f"{path}: the grouping document lacks {missing}; S07 consumes "
                                    "groups/verdicts/result_digest by name and refuses to read a "
                                    "shape change as an empty candidate set"})
    groups = doc.get("groups")
    if isinstance(groups, list):
        for index, grp in enumerate(groups):
            if not isinstance(grp, dict):
                findings.append({"code": "GROUP_NOT_AN_OBJECT", "index": index,
                                 "message": f"{path}: groups[{index}] is not an object"})
                continue
            g_missing = [k for k in REQUIRED_GROUP if k not in grp]
            if g_missing:
                findings.append({"code": "GROUP_MISSING_FIELD", "index": index,
                                 "fields": g_missing,
                                 "message": f"{path}: groups[{index}] lacks {g_missing}"})
                continue
            support = grp["support"]
            if not isinstance(support, dict):
                findings.append({"code": "GROUP_SUPPORT_UNSHAPED", "index": index,
                                 "message": f"{path}: groups[{index}].support is not an object"})
                continue
            s_missing = [k for k in REQUIRED_SUPPORT if k not in support]
            if s_missing:
                findings.append({"code": "GROUP_SUPPORT_MISSING_FIELD", "index": index,
                                 "fields": s_missing,
                                 "message": f"{path}: groups[{index}].support lacks {s_missing} -- "
                                            "S07 blocks pairs on cohort identity and cannot do so "
                                            "without independent_cohorts"})
            elif not isinstance(support["independent_cohorts"], list):
                findings.append({"code": "GROUP_SUPPORT_UNSHAPED", "index": index,
                                 "message": f"{path}: groups[{index}].support.independent_cohorts "
                                            "is not a list -- treating a scalar cohort set as "
                                            "character-by-character cohorts would invent pairs"})
    else:
        findings.append({"code": "GROUPS_NOT_A_LIST",
                         "message": f"{path}: groups is not a list"})
    verdicts = doc.get("verdicts")
    if isinstance(verdicts, list):
        for index, verdict in enumerate(verdicts):
            if not isinstance(verdict, dict) or "evidence_id" not in verdict \
                    or "verdict" not in verdict:
                findings.append({"code": "VERDICT_UNSHAPED", "index": index,
                                 "message": f"{path}: verdicts[{index}] needs evidence_id + verdict "
                                            "(CM-27 per-item verdict)"})
    else:
        findings.append({"code": "VERDICTS_NOT_A_LIST", "message": f"{path}: verdicts is not a list"})
    if findings:
        raise GroupingShapeError(findings)
    return doc


def load_intents(path: str | None) -> set:
    """S06's pending-removal intents (jsonl). A group whose canonical member is already pending
    removal is not offered to M1 -- S07 reads the intent, it never commits one (S12 alone may)."""
    ids = set()
    if not path:
        return ids
    with open(path, encoding="utf-8") as fh:                                    # read-only
        for line in fh:
            if not line.strip():
                continue
            rec = json.loads(line)
            if isinstance(rec, dict) and rec.get("evidence_id"):
                ids.add(str(rec["evidence_id"]))
    return ids


def build_evidence_index(path: str | None) -> dict:
    """Optional: the evidence stream S06 consumed, so the cheap proxy can read canonical CONTENT
    text instead of only the locator. Records are indexed, never mutated."""
    index: dict = {}
    if not path:
        return index
    with open(path, encoding="utf-8") as fh:                                    # read-only
        for line in fh:
            if not line.strip():
                continue
            rec = json.loads(line)
            if isinstance(rec, dict) and rec.get("evidence_id"):
                index[str(rec["evidence_id"])] = rec
    return index


# --------------------------------------------------------------------------- the cheap proxy
_TOKEN_RE = re.compile(r"[0-9a-z_\u4e00-\u9fff]+", re.I)
_CJK_RE = re.compile(r"[一-鿿]{2,}")


def token_set(text: str) -> frozenset:
    """Deterministic keyword-overlap tokens (04 row 5: Jaccard / keyword overlap).

    ASCII/word tokens plus CJK bigrams: without the bigrams a Chinese phrase collapses to a single
    token and shows zero overlap against a reordered copy, which would make the cheap stage
    silently under-propose to the model stage.
    """
    tokens = {t.lower() for t in _TOKEN_RE.findall(text or "")}
    for run in _CJK_RE.findall(text or ""):
        tokens.update(run[i:i + 2] for i in range(len(run) - 1))
    return frozenset(tokens)


def proxy_score(left: frozenset, right: frozenset) -> float:
    union = left | right
    if not union:
        return 0.0
    return round(len(left & right) / len(union), 6)


def canonical_text(group: dict, evidence_index: dict) -> tuple:
    """What the proxy actually measured -- recorded, because a cheap signal with no stated basis
    cannot be audited."""
    evidence_id = str(group["canonical_evidence_id"])
    rec = evidence_index.get(evidence_id)
    if rec is not None:
        return (json.dumps(rec.get("content", {}), sort_keys=True, ensure_ascii=False),
                "canonical_content_tokens", evidence_id)
    identity = group.get("identity") if isinstance(group.get("identity"), dict) else {}
    parts = [group.get("canonical_locator"), identity.get("pattern_key"),
             identity.get("canonical_fields")]
    text = " ".join(str(p) for p in parts if p)
    return (text, "canonical_locator_and_identity_tokens (no --evidence stream, or the canonical "
                  "evidence id is absent from it)", evidence_id)


def scope_of_cohort(cohort_key: str) -> str:
    """`kd_provenance.cohort_key` is `workspace::project::path`; blocking uses the first two
    components, i.e. the scope pair. The path is deliberately dropped: independent support REQUIRES
    distinct cohorts (so distinct paths), and blocking on the full key would refuse to pair any two
    groups that ever qualified, collapsing the cheap stage to a permanent empty set. Cross-scope
    pairing is what 12:66 (N4) forbids, so it stays impossible here."""
    parts = str(cohort_key).split("::")
    return "::".join(parts[:2]) if len(parts) >= 2 else str(cohort_key)


def pair_candidates(doc: dict, pending: set, evidence_index: dict, min_score: float) -> list:
    """O(n²) reduced by blocking, not by a magic cap: a pair forms only between groups that share at
    least one independent cohort's scope, so a cross-project candidate cannot exist here (12:66 N4).

    # IMPLEMENTATION_GAP: no cap on the number of pairs emitted per group / per run. A capacity
    # knob would be a second, coupled effect (a numeric cut here both ranks and limits), and Round
    # 2 deferred exactly that shape. / DEFERRED id DD-4-sub31 (float score criteria: one Owner,
    # offline-calibrated coefficients, capacity knob decoupled)
    """
    verdicts = {(str(v["evidence_id"]), str(v["identity_digest"])): str(v["verdict"])
                for v in doc["verdicts"] if "identity_digest" in v}
    live = []
    for grp in sorted(doc["groups"], key=lambda g: str(g["identity_digest"])):
        canonical = grp["canonical_evidence_id"]
        if canonical is None or str(canonical) in pending:
            continue                      # nothing live, or a removal intent is already pending
        verdict = verdicts.get((str(canonical), str(grp["identity_digest"])))
        if verdict is not None and verdict != "canonical":
            continue                      # CM-27: a per-item verdict that is not canonical is not a candidate
        cohorts = {scope_of_cohort(c) for c in grp["support"]["independent_cohorts"]}
        if not cohorts:
            continue                      # no independent cohort -> nothing to propose against
        text, basis, evidence_id = canonical_text(grp, evidence_index)
        live.append({"digest": str(grp["identity_digest"]), "cohorts": cohorts,
                    "tokens": token_set(text), "basis": basis, "evidence_id": evidence_id,
                    "hashes": set(grp["content_hashes"])})

    pairs = []
    for i in range(len(live)):
        for j in range(i + 1, len(live)):
            left, right = live[i], live[j]
            shared = sorted(left["cohorts"] & right["cohorts"])
            if not shared:
                continue                  # different scope -> never a candidate pair (N4)
            score = proxy_score(left["tokens"], right["tokens"])
            if score < min_score:
                continue
            pair_id = f"{min(left['digest'], right['digest'])[:16]}-{max(left['digest'], right['digest'])[:16]}"
            pairs.append({"pair_id": pair_id,
                          "left_identity_digest": left["digest"],
                          "right_identity_digest": right["digest"],
                          "left_canonical_evidence_id": left["evidence_id"],
                          "right_canonical_evidence_id": right["evidence_id"],
                          "shared_scopes": shared,
                          "shared_content_hash": sorted(left["hashes"] & right["hashes"]),
                          "overlap_token_count": len(left["tokens"] & right["tokens"]),
                          "score": score,
                          "score_semantics": SCORE_SEMANTICS,
                          "proxy_basis": {"left": left["basis"], "right": right["basis"]},
                          "candidate_for": "M1_semantic_dedup_advisory_only"})
    return sorted(pairs, key=lambda p: (-p["score"], p["pair_id"]))


# --------------------------------------------------------------------------- threshold sourcing
def read_threshold(config_path: str, cli_value):
    """The cut comes from the single-source config if it carries a similarity key, else from the
    operator. Never from a number written into this file."""
    try:
        thresholds = kd_gate.load_config(config_path)     # enforces status == provisional
    except prov.SchemaError as exc:
        raise ConfigUnusable(f"{config_path}: status={_status_of(config_path)!r} -- S07 reads "
                             f"thresholds only from the provisional single source (kd_gate.load_config "
                             f"refused: {exc})")
    except OSError as exc:
        raise ConfigUnusable(f"{config_path}: unreadable ({exc})")
    present = sorted(thresholds)
    key = next((k for k in SIMILARITY_CONFIG_KEYS if k in thresholds), None)
    if key is not None:
        return (float(thresholds[key]), key,
                "promotion-config.json threshold key (the same single source the gate reads; the "
                "value is still provisional, not adopted policy)",
                present, _status_of(config_path))
    if cli_value is None:
        raise UndecidedThreshold(
            f"{config_path} carries {present}; none of them is a similarity cut, and Round 2 "
            f"deferred the proxy threshold ({', '.join(DEFERRED_THRESHOLD_IDS)}). Supply "
            "--min-score at run time, or add a similarity key to that config with the evidence "
            "DD-6-sub43 demands -- kd_proxy_candidates.py refuses to invent a number.")
    value = float(cli_value)
    if not 0.0 <= value <= 1.0:
        raise ValueError("--min-score must be within [0,1]: the proxy is a Jaccard ratio")
    return (value, "--min-score",
            f"operator-supplied at run time; NOT a decided constant (deferred "
            f"{', '.join(DEFERRED_THRESHOLD_IDS)})", present, _status_of(config_path))


def _status_of(config_path: str) -> str:
    """Diagnostic only; the authority on the status stays kd_gate.load_config."""
    try:
        with open(config_path, encoding="utf-8") as fh:                         # read-only
            return str(json.load(fh).get("status"))
    except (OSError, ValueError):
        return "UNREADABLE"


# --------------------------------------------------------------------------- output document
def build_payload(pairs: list, doc: dict, threshold: dict, args) -> dict:
    empty = not pairs
    return {
        "schema": SCHEMA,
        "signal_tier": SIGNAL_TIER,
        "authority": ("RANKING ONLY. Proposes which pairs the expensive model step "
                      "(M1 / #11 语义判重) may look at. Not evidence of recurrence, not a promotion "
                      "input, not a counter, not an automatic merge."),
        "must_not_be_read_as": ["evidence of recurrence", "promotion decision input",
                               "support_count / distinct_occurrence_count / contradiction_count",
                               "an automatic merge", "a decided threshold"],
        "threshold": threshold,
        "grouping_source": {"path": os.path.abspath(args.grouping),
                           "schema_version": doc["schema_version"],
                           "support_semantics": doc["support_semantics"],
                           "result_digest": doc["result_digest"],
                           "group_count": len(doc["groups"]),
                           "evidence_stream": os.path.abspath(args.evidence) if args.evidence else None,
                           "pending_removal_source":
                               os.path.abspath(args.intents) if args.intents else None},
        "pairs": pairs,
        "pair_count": len(pairs),
        "empty_candidate_set": empty,
        "downstream": {
            "m1_semantic_dedup": {
                "action": "SKIP" if empty else "MAY_RUN",
                "because": ("contract S07 exit 0=空集⇒下游跳过 M1: the cheap stage proposed no "
                            "candidate, so the model step has nothing to adjudicate") if empty else
                           ("candidate set is non-empty; M1 judges only inside this set "
                            "(04 row 5 判定层, CM-42)"),
                "consumer_status": ("PENDING_CONSUMER: M1 (#11 语义判重) and S10 land in Wave 3, so "
                                    "no reader of this flag exists in the repo yet; it is recorded, "
                                    "not claimed as wired"),
            },
            "promotion_pipeline": "NOT AN INPUT (分数永不进晋升记录)",
        },
        "containment": {
            "rule": "分数永不进晋升记录",
            "guard": "kd_proxy_candidates.assert_not_promotion_payload",
            "guarded_by_this_run": "this document and every score in it passed the guard before the write",
            "expected_consumers": ("PENDING_CONSUMER: S10 (verdict) and S12 (pre-write) are asked to "
                                   "call the guard; see W2-B-REPORT.md"),
            "durable_write_path": "none: S07 writes only this derived CLI artifact, never the store",
        },
    }


def score_set(pairs: list) -> list:
    return sorted({p["score"] for p in pairs})


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _refusal(name: str, code: int, detail: dict) -> str:
    body = {"refusal": name, "exit": code, "rule": "分数永不进晋升记录"
            if code == EXIT_PROMOTION_LEAK else "S07 contract", "detail": detail}
    return json.dumps(body, ensure_ascii=False, indent=1)


# --------------------------------------------------------------------------- CLI
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="kd_proxy_candidates.py",
        description="S07 cheap proxy candidate generation: score keyword/Jaccard overlap between "
                    "S06 identity groups and emit candidate_pairs.json as a Tier-3 RANKING signal "
                    "only. An empty candidate set is a normal result (exit 0) and tells downstream "
                    "to skip M1. A score never enters a promotion record: "
                    "assert_not_promotion_payload() refuses with exit 5, and --guard-payload runs "
                    "the same check on a file.")
    ap.add_argument("--grouping", help="S06 grouping document (groups/verdicts/result_digest)")
    ap.add_argument("--evidence", help="optional evidence stream (jsonl) so the proxy reads canonical content")
    ap.add_argument("--intents", help="optional S06 pending-removal intents (jsonl); those groups are not proposed")
    ap.add_argument("--min-score", help="similarity cut in [0,1]; required unless the provisional "
                                        "config carries a similarity key (S07 never defaults one)")
    ap.add_argument("--config", default=kd_gate.CONFIG_PATH,
                    help="the single-source promotion config the gate reads "
                         "(default: references/promotion-config.json)")
    ap.add_argument("--out", help="write candidate_pairs.json here (derived artifact; parent dir must exist)")
    ap.add_argument("--dry-run", action="store_true", help="compute and print only; writes nothing")
    ap.add_argument("--guard-payload", help="check a payload file for a proxy-score leak into a "
                                           "promotion-shaped record and exit (0 clean / 5 refused)")
    ap.add_argument("--guard-scores", default="",
                    help="comma-separated score values for --guard-payload value-alias detection")
    ap.add_argument("--quiet", action="store_true", help="do not print the payload")
    args = ap.parse_args(argv)

    if args.guard_payload:
        try:
            with open(args.guard_payload, encoding="utf-8") as fh:              # read-only
                payload = json.load(fh)
        except (OSError, ValueError) as exc:
            print(f"input error: {exc}", file=sys.stderr)
            return EXIT_INPUT_ERROR
        scores = [s for s in (x.strip() for x in args.guard_scores.split(",")) if s]
        try:
            assert_not_promotion_payload(payload, scores)
        except PromotionLeakRefusal as exc:
            print(_refusal("PROMOTION_LEAK_REFUSED", EXIT_PROMOTION_LEAK,
                           {"findings": exc.findings}), file=sys.stderr)
            return EXIT_PROMOTION_LEAK
        print(json.dumps({"guard": "PROMOTION_PAYLOAD_CLEAN", "exit": EXIT_OK,
                          "note": "clean for THIS payload: no score-named field, no "
                                  "decision-carrier key, no proxy prose"}, ensure_ascii=False))
        return EXIT_OK

    if not args.grouping:
        print("usage error: --grouping is required", file=sys.stderr)
        return EXIT_INPUT_ERROR

    try:
        doc = load_grouping(args.grouping)
    except GroupingShapeError as exc:
        print(_refusal("GROUPING_SHAPE", EXIT_GROUPING_SHAPE, {"findings": exc.findings}),
              file=sys.stderr)
        return EXIT_GROUPING_SHAPE

    try:
        min_score, source, provenance, config_keys, config_status = read_threshold(
            args.config, args.min_score)
    except UndecidedThreshold as exc:
        print(_refusal("THRESHOLD_UNDECIDED", EXIT_THRESHOLD_UNDECIDED, {
            "deferred_ids": list(DEFERRED_THRESHOLD_IDS),
            "similarity_keys_looked_for": list(SIMILARITY_CONFIG_KEYS),
            "message": str(exc)}), file=sys.stderr)
        return EXIT_THRESHOLD_UNDECIDED
    except ConfigUnusable as exc:
        print(_refusal("CONFIG_UNUSABLE", EXIT_CONFIG_UNUSABLE,
                       {"message": str(exc), "config": os.path.abspath(args.config)}),
              file=sys.stderr)
        return EXIT_CONFIG_UNUSABLE
    except (TypeError, ValueError) as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR

    try:
        pending = load_intents(args.intents)
        evidence_index = build_evidence_index(args.evidence)
    except (OSError, ValueError) as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR

    pairs = pair_candidates(doc, pending, evidence_index, min_score)
    payload = build_payload(pairs, doc, {
        "min_score": min_score, "source": source, "provenance": provenance,
        "config_path": os.path.abspath(args.config), "config_status": config_status,
        "config_threshold_keys": config_keys,
        "deferred_ids": list(DEFERRED_THRESHOLD_IDS),
        "note": "the cut is data, not policy: read from the operator or a config key, never baked "
                "into kd_proxy_candidates.py",
    }, args)
    payload["result_digest"] = _digest(json.dumps(
        {"pairs": payload["pairs"], "min_score": min_score,
         "empty": payload["empty_candidate_set"]}, sort_keys=True, ensure_ascii=False))

    # containment runs on the document S07 is about to emit, every run
    try:
        assert_not_promotion_payload(payload, score_set(pairs))
    except PromotionLeakRefusal as exc:
        print(_refusal("PROMOTION_LEAK_REFUSED", EXIT_PROMOTION_LEAK,
                       {"findings": exc.findings}), file=sys.stderr)
        return EXIT_PROMOTION_LEAK

    text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    if not args.dry_run and args.out:
        import kd_store_layout as layout
        try:
            layout.assert_staging_path(args.out)
        except layout.LayoutViolation as exc:
            print(f"output refused: {exc}", file=sys.stderr)
            return EXIT_INPUT_ERROR
        parent = os.path.dirname(os.path.abspath(args.out))
        if not os.path.isdir(parent):
            print(f"input error: {parent} does not exist (S07 never creates directories)",
                  file=sys.stderr)
            return EXIT_INPUT_ERROR
        try:
            layout.write_staging_text(args.out, text + "\n")
        except (OSError, layout.LayoutViolation) as exc:
            print(f"output refused: {type(exc).__name__}", file=sys.stderr)
            return EXIT_INPUT_ERROR
    if not args.quiet:
        print(text)
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
