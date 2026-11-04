#!/usr/bin/env python3
"""S15 `kd_eval_freeze` -- freeze an eval corpus and PROVE exam isolation.

Contract row (12-SKILL-DESIGN-BRIEF.md:123; .distill/round-3/wave-3/_dispatch/w3c.json):
    inputs   候选语料 + split 契约
    outputs  冻结语料 + fixture + exam isolation 结果
    exit     2 = 隔离被破坏（模型可见答案）
    clusters CM-48 regression-eval-for-promoted-rule (CORE, MUST) + CM-46 (non-core SUPPORTING)
    pipeline 步 18 / 行 12

Why this script exists: 12:244 -- "M4 晋升规则的 eval 题面 ... 语料与 split 由 S15 持有（否则模型
能看见答案，eval 失效）". If the model under evaluation can read the answer, every number
downstream is meaningless (08-EVAL-STRATEGY.md:45 prerequisite (d)). Round 2's only reference for
the guard, `11:exam-isolation-gate`, is UNVERIFIED and has no breach assertion of its own
(08:159 / DEFERRED id DD-3-sub22), so the gate below is written as code that demonstrably fails.

Isolation model -- what counts as "model-visible", resolved as code, not asserted as a claim:
  (1) realpath containment -- an answer file whose RESOLVED path is inside (or equal to) a
      declared surface root is visible however the caller spelled it (`../`, symlinks);
  (2) host-loadable document shapes -- instruction files (SKILL.md / AGENTS.md / CLAUDE.md /
      GEMINI.md / .cursorrules / copilot-instructions.md / *.instructions.md / *.mdc /
      *.agent.md / .waza.yaml / mcp.json / plugin.json) plus every file under a skills-shaped
      path segment (skills/ rules/ commands/ agents/ hooks/ references/ schemas/ .claude/
      .qoder/ .qoder-cn/ .cursor/ .github/ .waza/) or under any directory containing a SKILL.md
      -- bundled assets are loaded when a skill references them
      (repos/awesome-copilot/AGENTS.md "Agent Skills (skills/*/SKILL.md) ... can include bundled
      assets"; repos/pskoett-ai-skills/AGENTS.md "scripts/ references/ assets/" inside the skill
      folder; repos/hermes-agent/skills/AGENTS.md same shape);
  (3) verbatim answer text -- each answer's WHOLE normalised string (NFKC + casefold + whitespace
      collapse) is searched inside every document found by (2). The reference gate compares only
      `content[:60]` and its own registered risk is "只查前缀 60 字符的连续原文，改写/截半的泄漏
      查不到" (round-1/worker-11.md, `11:exam-isolation-gate`), so the prefix blind spot is gone
      here; a paraphrase is still invisible and is registered as an IMPLEMENTATION_GAP below;
  (4) a sample's own answer appearing in its own task_input -- the question carries the answer.
  Dead man: a surface with zero loadable documents is `unscanned`, not clean, and exits 3; an
  empty surface set is refused before any artifact exists. Round 2's audit caught two guards that
  could never fail (a disjunction whose second arm is a constant, and a regex that matched
  nothing), which is why "nothing was read" is a refusal in code AND why SC09 gives
  `$defs/surface.loadable_documents_read` `"minimum": 1`.

Exit codes
    0  bundle + answer side + fixture published, isolation proven clean, SC09 validated
    2  isolation broken -- answer material is model-visible (contract code; nothing is published)
    3  refused input -- missing argument, no surface declared, surface unusable / unscannable,
       unusable corpus or contract, output placement itself model-visible, CM-48 tie absent,
       prerequisite (a) unassessable, SC09 refused the emitted document
    5  filesystem failure

IMPLEMENTATION_GAP: a paraphrased / translated / truncated copy of an answer in a model-visible
    document is undetectable by verbatim comparison / DEFERRED id DD-3-sub22 (08:159 -- (d)
    becomes a MUST gate only once a breach-asserting isolation gate is reused by >=2 projects;
    this file supplies the breach assertion but one implementation is not two projects).
IMPLEMENTATION_GAP: prerequisite (c)'s min_improvement / repeats / tolerance are read from the
    split contract and never defaulted here; Round 2 left them undecided / DEFERRED id DD-3-sub20
    (08:44, 08:93 P-02 -- defaulting min_improvement to 0 IS the non-falsifiable threshold the
    ban names: 「禁止把 improvement 大于零当阈值」).
IMPLEMENTATION_GAP: whether a Round 3 candidate is a reproducible execution sample or a pure
    prompt asset is undetermined, and that choice decides which tier may grant `verified`
    / DEFERRED id DD-3-sub24 (08:151, 08:169 D08-3); `subject.sample_kind` accepts "undecided"
    and kd_eval_score refuses to derive `verified` from it.

Stdlib only. No model, no network, no spawned child process: the zero-LLM static import-closure
scan (.distill/round-3/wave-1/run_wave1_spine.py:313-368) ast-walks this file's closure and
text-scans it, so this module stays clear of every token that scan flags.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import kd_validate  # noqa: E402  S09, the sole schema witness (12:171) -- read-only reuse
import kd_store_layout as layout  # noqa: E402  protected-output boundary

EXIT_OK = 0
EXIT_ISOLATION_BROKEN = 2                # contract: 2 = 隔离被破坏（模型可见答案）
EXIT_REFUSED_INPUT = 3
EXIT_FS = 5

KIND = "eval-bundle"
CONTRACT_ROW = "12-SKILL-DESIGN-BRIEF.md:123 (S15) / :185 (SC09) / :244 (语料与 split 由 S15 持有)"
SPLITS = ("train", "val", "holdout")

#: path segments a host treats as its own instruction surface. `scripts/`, `references/`,
#: `assets/` and `templates/` are included because a skill is a FOLDER whose bundled assets are
#: loaded when the SKILL.md references them (repos/pskoett-ai-skills/AGENTS.md "Structure:
#: SKILL.md / scripts/ / references/ / assets/"; repos/hermes-agent/skills/AGENTS.md rule 6
#: "scripts/, references/, templates." -- "ship a helper script and reference it by
#: skill-relative path"), so an answer parked in any of those directories is model-visible.
SKILLS_SHAPED_SEGMENTS = frozenset({
    "skills", "rules", "commands", "agents", "hooks", "references", "schemas",
    "scripts", "assets", "templates",
    ".claude", ".qoder", ".qoder-cn", ".cursor", ".github", ".waza",
})
INSTRUCTION_NAMES = frozenset({
    "SKILL.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md", ".cursorrules",
    "copilot-instructions.md", ".waza.yaml", "mcp.json", "plugin.json",
})
INSTRUCTION_SUFFIXES = (".instructions.md", ".mdc", ".agent.md")
SKIP_DIR_NAMES = frozenset({".git", "__pycache__", "node_modules", ".mypy_cache"})


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime())


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: str) -> str:
    with open(path, "rb") as fh:                        # read-only: hashing is not a write
        return sha256_bytes(fh.read())


def norm(text: str) -> str:
    """Comparison form for leak detection: NFKC + casefold + whitespace collapse."""
    return " ".join(unicodedata.normalize("NFKC", str(text)).casefold().split())


# --------------------------------------------------------------------- model-visible surface
def is_skills_shaped(path: str) -> bool:
    """Name-level shape test used to refuse S15's OWN output placement: a frozen bundle written
    into a skills-shaped path is a decoy a host will load (same vocabulary S11 uses for
    quarantine placement, 06 §4)."""
    parts = [p.casefold() for p in os.path.abspath(path).replace(os.sep, "/").split("/")]
    return any(p in SKILLS_SHAPED_SEGMENTS for p in parts)


def is_instruction_file(name: str) -> bool:
    return name in INSTRUCTION_NAMES or any(name.endswith(s) for s in INSTRUCTION_SUFFIXES)


def iter_loadable_documents(root: str) -> list:
    """Every file under `root` a host could load into a model's context. Deterministic order."""
    docs = []
    root = os.path.realpath(root)
    if not os.path.isdir(root):
        return docs
    def unreadable(error):
        raise error
    for dirpath, dirnames, filenames in os.walk(root, onerror=unreadable):
        if any(os.path.islink(os.path.join(dirpath, d)) for d in dirnames):
            raise ValueError("isolation scan cannot prove a symlinked subtree clean")
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIR_NAMES)
        segments = [p.casefold() for p in dirpath.replace(os.sep, "/").split("/")]
        shaped = (any(p in SKILLS_SHAPED_SEGMENTS for p in segments)
                  or os.path.exists(os.path.join(dirpath, "SKILL.md")))
        for name in sorted(filenames):
            if shaped or is_instruction_file(name):
                docs.append(os.path.join(dirpath, name))
    return docs


def default_surfaces() -> dict:
    """This package's own model-visible trees -- what a host loads when the generated skill
    ships. Resolved from HERE at call time so moving the package moves the surface."""
    pkg = os.path.abspath(os.path.join(HERE, os.pardir))
    out = {}
    for name, rel in (("pkg-references", "references"), ("pkg-schemas", "schemas"),
                      ("pkg-scripts", "scripts")):
        path = os.path.join(pkg, rel)
        if os.path.isdir(path):
            out[name] = path
    return out


def parse_surfaces(pairs) -> dict:
    surfaces = {}
    for item in pairs:
        if "=" not in item:
            raise ValueError(f"--surface wants NAME=PATH, got {item!r}")
        name, path = (part.strip() for part in item.split("=", 1))
        if not name or not path:
            raise ValueError(f"--surface wants NAME=PATH, got {item!r}")
        surfaces[name] = os.path.realpath(os.path.abspath(os.path.expanduser(path)))
    return surfaces


# --------------------------------------------------------------------- inputs
def read_jsonl(path: str) -> list:
    rows = []
    with open(path, encoding="utf-8") as fh:            # read-only
        for number, line in enumerate(fh, 1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                rows.append(json.loads(stripped))
            except ValueError as exc:
                raise ValueError(f"{path}:{number}: malformed JSONL line: {exc}") from exc
    return rows


def load_corpus(path: str) -> list:
    """Corpus rows carry `07:rubric-based-eval-split-contract`'s five fields (08:46: task_input /
    expected_behavior / difficulty / category / source) plus sample_id, split and gold_answer.
    An empty rubric is refused (CM-46's own builder discards empty-criterion examples) and so is
    a row without an answer, which could not be adjudicated."""
    rows = read_jsonl(path)
    if not rows:
        raise ValueError(f"{path}: empty corpus -- a frozen eval with no samples is P-10's "
                         "'.evals/cases/ 为空' shape (08:101); refused, not recorded")
    required = ("sample_id", "split", "task_input", "expected_behavior", "gold_answer")
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("corpus rows must be objects")
        for key in required:
            value = row.get(key)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{path}: sample {row.get('sample_id')!r} needs a non-empty "
                                 f"string field {key!r}")
        if row["sample_id"] in (".", "..") or any(c in row["sample_id"] for c in ("/", "\\", "\x00")):
            raise ValueError("sample_id must be a single safe filename component")
        if "is_original_failure" in row and type(row["is_original_failure"]) is not bool:
            raise ValueError("is_original_failure must be a boolean")
        if row["split"] not in SPLITS:
            raise ValueError(f"{path}: sample {row['sample_id']!r} has split {row['split']!r}; "
                             "the CM-46 contract defines train/val/holdout only")
        if row.get("source") is not None and row["source"] not in ("golden", "sessiondb",
                                                                   "synthetic"):
            raise ValueError(f"{path}: sample {row['sample_id']!r} has unknown source "
                             f"{row['source']!r}")
    ids = [row["sample_id"] for row in rows]
    if len(set(ids)) != len(ids):
        raise ValueError(f"{path}: duplicate sample_id values -- a split is set membership, not "
                         "a bag (08:46 split contract)")
    return rows


def load_contract(path: str) -> dict:
    """The split contract: dataset_id, splits, answer_visibility, optimisation_loop.metric_ids,
    verdict_thresholds, floor_ceiling, attribution, sample_kind, reproducible_rerun_claimed.
    Nothing is defaulted: an absent threshold stays None, which records prerequisite (c) as
    unsatisfied instead of inventing a number."""
    with open(path, encoding="utf-8") as fh:            # read-only
        doc = json.load(fh)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: split contract must be a JSON object")
    for key in ("dataset_id", "splits", "answer_visibility", "optimisation_loop"):
        if key not in doc:
            raise ValueError(f"{path}: split contract is missing required key {key!r}")
    if not isinstance(doc["dataset_id"], str) or not doc["dataset_id"].strip():
        raise ValueError(f"{path}: dataset_id must be a non-empty string")
    if not isinstance(doc["splits"], list) or any(not isinstance(s, str) for s in doc["splits"]):
        raise ValueError("splits must be an array of split names")
    declared = set(doc["splits"])
    unknown = declared - set(SPLITS)
    if unknown:
        raise ValueError(f"{path}: contract declares splits {sorted(unknown)} the CM-46 "
                         "three-split contract does not define")
    if not isinstance(doc["answer_visibility"], dict):
        raise ValueError(f"{path}: answer_visibility must be an object of split -> audience")
    if any(doc["answer_visibility"].get(split) not in ("model", "agent", "all", "any", "adjudicator-only")
           for split in declared):
        raise ValueError("every declared split needs an explicit, known answer audience")
    loop = doc["optimisation_loop"]
    if not isinstance(loop, dict) or not isinstance(loop.get("metric_ids"), list):
        raise ValueError(f"{path}: optimisation_loop.metric_ids must be a list of the loop's "
                         "own metric ids -- prerequisite (a) has nothing to be distinct from "
                         "otherwise (08:42)")
    return doc


# --------------------------------------------------------------------- the isolation check
def scan_isolation(answer_texts: dict, answer_files: list, surfaces: dict) -> dict:
    """`answer_texts`: sample_id -> normalised answer, PRE-FILTERED by the contract's
    answer_visibility (an answer the contract declares model-visible is not a leak).
    `answer_files`: [{path, bytes, owner_sample_id}] as they exist on disk.
    `surfaces`: name -> realpath root.
    Returns the SC09 `isolation` block. status == 'breach' on any detection, 'unscanned' when no
    declared surface contained a single host-loadable document, else 'proven-clean'."""
    method = ("realpath containment against declared surface roots + host-loadable document "
              "shape enumeration + verbatim whole-normalised-answer substring test; a paraphrased "
              "or translated copy is NOT detected (IMPLEMENTATION_GAP, DEFERRED id DD-3-sub22)")
    breaches, surface_rows = [], []
    for name, root in sorted(surfaces.items()):
        docs = iter_loadable_documents(root)
        inside = 0
        for entry in answer_files:
            real = os.path.realpath(entry["path"])
            if real == root or real.startswith(root + os.sep):
                inside += 1
                breaches.append({"kind": "answer-file-inside-surface", "surface": name,
                                 "document": real, "sample_id": entry["owner_sample_id"],
                                 "excerpt_chars": entry["bytes"]})
        for doc_path in docs:
            try:
                with open(doc_path, encoding="utf-8", errors="replace") as fh:   # read-only
                    text = norm(fh.read())
            except OSError as exc:
                raise ValueError("isolation scan could not read a declared document") from exc
            for sample_id in sorted(answer_texts):
                needle = answer_texts[sample_id]
                if needle and needle in text:
                    breaches.append({"kind": "answer-text-in-loadable-document", "surface": name,
                                     "document": os.path.realpath(doc_path),
                                     "sample_id": sample_id, "excerpt_chars": len(needle)})
        surface_rows.append({"name": name, "root": root, "loadable_documents_read": len(docs),
                             "answer_files_inside": inside})
    if breaches:
        status = "breach"
    elif not surface_rows or any(row["loadable_documents_read"] == 0 for row in surface_rows):
        # strict per surface: a declared root that yields nothing loadable was not scanned, so
        # the whole result is 'unscanned'. SC09 gives each surface row
        # `"loadable_documents_read": {"minimum": 1}` for exactly this reason -- a row that could
        # be 0 would be a guard with nothing behind it.
        status = "unscanned"
    else:
        status = "proven-clean"
    return {"status": status, "method": method, "surfaces": surface_rows,
            "breaches": sorted(breaches, key=lambda b: (b["kind"], b["document"], b["sample_id"])),
            "checked_at": _now()}


def self_leaks(rows: list, visible: set) -> list:
    """A sample whose own answer appears in its own task_input (defect `11:exam-isolation-gate`
    was written for). `visible` = split names whose answers the contract allows the model to see;
    an answer that is legitimately model-visible cannot be a leak."""
    out = []
    for row in rows:
        if row["split"] in visible:
            continue
        needle = norm(row["gold_answer"])
        if needle and needle in norm(row["task_input"]):
            out.append({"kind": "question-carries-own-answer", "surface": "corpus",
                        "document": f"<task_input of {row['sample_id']}>",
                        "sample_id": row["sample_id"], "excerpt_chars": len(needle)})
    return out


# --------------------------------------------------------------------- 08 §1.3 four prerequisites
def prerequisites(contract: dict, rows: list, isolation: dict, instrument_id: str,
                  loop_metric_ids: list) -> dict:
    """One field per prerequisite with a reason. Tier-2 validity is the AND of the four (08:41
    '缺一即 Tier-2 无效，退回 Tier-1 或 Tier-4'), and S16 reads exactly this."""
    collision = instrument_id in loop_metric_ids
    prereq_a = {
        "status": "satisfied" if not collision else "unsatisfied",
        "reason": ("instrument %r vs optimisation-loop metric ids %r: %s"
                   % (instrument_id, loop_metric_ids,
                      "distinct -- but S16 still re-asserts this, it is not a convention"
                      if not collision else
                      "COLLISION -- the adjudicating instrument IS the in-loop metric (P-01, "
                      "08:92); S16 refuses with exit 2")),
        "judge_instrument_id": instrument_id,
        "loop_metric_ids": sorted(loop_metric_ids),
        "asserted_not_conventional": True,
    }

    floor_ceiling = contract.get("floor_ceiling") or {}
    floor, oracle = floor_ceiling.get("baseline_noop"), floor_ceiling.get("oracle")
    prereq_b = {
        "status": "satisfied" if (floor is not None and oracle is not None) else "unsatisfied",
        "reason": ("baseline-noop and oracle both supplied by the contract (08:43)"
                   if (floor is not None and oracle is not None) else
                   "one or both of baseline_noop / oracle absent; 08 §7 item 4 makes (b) a hard "
                   "constraint only once 01's bench solvers reproduce 0/3->3/3, so it is recorded "
                   "unsatisfied rather than synthesized (DEFERRED id DD-3-sub23)"),
        "baseline_noop": floor,
        "oracle": oracle,
    }

    thresholds = contract.get("verdict_thresholds") or {}
    triple = {key: thresholds.get(key) for key in ("min_improvement", "repeats", "tolerance")}
    missing = [key for key, value in triple.items() if value is None]
    prereq_c = {
        "status": "satisfied" if not missing else "unsatisfied",
        "reason": ("min_improvement / repeats / tolerance all supplied by the contract (08:44)"
                   if not missing else
                   "undecided in the split contract: %s; kd_eval_freeze and kd_eval_score refuse "
                   "to default them (08:44, 08:93 P-02)" % ", ".join(missing)),
        "thresholds": {**triple,
                       "values_from": str(thresholds.get("values_from", "split contract"))},
    }

    attribution = contract.get("attribution") or {}
    corrections_in_train = attribution.get("new_corrections_in_train")
    holdout_audience = str(contract["answer_visibility"].get("holdout", "")).casefold()
    answers_model_visible = holdout_audience in {"model", "agent", "all", "any"}
    reasons = []
    if isolation["status"] != "proven-clean":
        reasons.append(f"isolation status is {isolation['status']!r}")
    if answers_model_visible:
        reasons.append("the contract itself declares holdout answers model-visible "
                       f"(answer_visibility.holdout={contract['answer_visibility'].get('holdout')!r})")
    if corrections_in_train is not False:
        reasons.append(f"attribution.new_corrections_in_train={corrections_in_train!r} -- 08:45 "
                       "requires that a new correction not go only into train")
    prereq_d = {
        "status": "satisfied" if not reasons else "unsatisfied",
        "reason": ("isolation proven clean, holdout answers adjudicator-only, and no new "
                   "correction routed into train (08:45)" if not reasons
                   else "; ".join(reasons)),
        "new_corrections_kept_out_of_train": corrections_in_train is False,
        "acceptance_criteria_immutable": isolation["status"] == "proven-clean",
    }
    return {"a_instrument_separation": prereq_a, "b_floor_ceiling": prereq_b,
            "c_min_improvement_repeats_tolerance": prereq_c,
            "d_leakage_and_attribution": prereq_d}


# --------------------------------------------------------------------- build / digest
def adjudicator_only_rows(rows: list, contract: dict) -> list:
    visible = {split for split, audience in contract["answer_visibility"].items()
               if str(audience).casefold() in {"model", "agent", "all", "any"} and split in SPLITS}
    return [row for row in rows if row["split"] not in visible]


def question_side_of(bundle_samples: list, dataset_id: str, splits: dict) -> str:
    return json.dumps({"dataset_id": dataset_id, "splits": splits, "samples": bundle_samples},
                      sort_keys=True, ensure_ascii=False)


def digest_of(dataset_id: str, splits: dict, bundle_samples: list, answer_files: list) -> str:
    """The frozen bundle's identity: question side + every answer file digest. S16 recomputes it
    and refuses on mismatch -- that is the mechanism behind P-11 (08:102 'DO UPDATE SET expected'
    silently rewriting the acceptance criteria)."""
    answer_digest = sha256_bytes(json.dumps(
        sorted((entry["path"], entry["sha256"]) for entry in answer_files), sort_keys=True,
        ensure_ascii=False).encode("utf-8"))
    question_digest = sha256_bytes(question_side_of(bundle_samples, dataset_id,
                                                    splits).encode("utf-8"))
    return sha256_bytes((question_digest + answer_digest).encode("utf-8"))


def bundle_digest(doc: dict) -> str:
    # Freeze the decision inputs as well as question/answer bytes. Scoring changes only
    # verdict, run_result and scan observations, never subject, thresholds or instrument.
    frozen = {key: doc[key] for key in ("schema_version", "dataset_id", "subject", "splits",
                                      "samples", "answer_material", "prerequisites")}
    frozen["instrument"] = {key: doc["five_tuple"][key] for key in (
        "instrument_id", "dataset_id", "threshold", "instrument_also_optimised_against")}
    frozen["surfaces"] = [{"name": row["name"], "root": row["root"]}
                          for row in doc["isolation"]["surfaces"]]
    return sha256_bytes(json.dumps(frozen, sort_keys=True, ensure_ascii=False,
                                  allow_nan=False).encode("utf-8"))


def build_bundle(contract: dict, rows: list, answer_files: list, isolation: dict,
                 prereqs: dict, instrument_id: str, loop_metric_ids: list, subject: dict) -> dict:
    """The SC09 stage='freeze' document. `verified` is structurally false at freeze: Tier-0 and
    the freezing act produce no verified record (08:24, 08:65)."""
    splits = {key: [row["sample_id"] for row in rows if row["split"] == key] for key in SPLITS}
    samples = [{
        "sample_id": row["sample_id"], "split": row["split"], "task_input": row["task_input"],
        "expected_behavior": row["expected_behavior"],
        "difficulty": row.get("difficulty", "medium"),
        "category": row.get("category", "general"),
        "source": row.get("source", "synthetic"),
        "gold_sha256": sha256_bytes(row["gold_answer"].encode("utf-8")),
        "is_original_failure": bool(row.get("is_original_failure", False)),
    } for row in rows]
    threshold_slots = ("min_improvement", "repeats", "tolerance")
    prereq_c = prereqs["c_min_improvement_repeats_tolerance"]
    doc = {
        "schema_version": "1", "stage": "freeze", "at": _now(),
        "dataset_id": contract["dataset_id"],
        "bundle_digest": digest_of(contract["dataset_id"], splits, samples, answer_files),
        "subject": subject, "splits": splits, "samples": samples,
        "answer_material": {"visibility": "adjudicator-only",
                            "files": [{"path": entry["path"], "sha256": entry["sha256"],
                                       "bytes": entry["bytes"]} for entry in answer_files]},
        "isolation": isolation,
        "prerequisites": prereqs,
        "five_tuple": {
            "instrument_id": instrument_id, "dataset_id": contract["dataset_id"],
            "threshold": (None if prereq_c["status"] == "unsatisfied"
                          else {key: prereq_c["thresholds"][key] for key in threshold_slots}),
            "run_result": None,
            "instrument_also_optimised_against": {
                "loop_metric_ids": sorted(loop_metric_ids),
                "collision": instrument_id in loop_metric_ids,
                "checked_by": "kd_eval_score"},
        },
        "verdict": {"status": "NOT_RUN", "blocking": False, "verified": False,
                    "regression_detected": False, "reasons": ["not_run_frozen_only"]},
        "provenance": {"produced_by": "S15 kd_eval_freeze", "script": "kd_eval_freeze.py",
                       "model_id": "none", "contract_row": CONTRACT_ROW},
        "notes": {"IMPLEMENTATION_GAPS": [
            "IMPLEMENTATION_GAP: paraphrased / truncated answer copies are undetectable by "
            "verbatim comparison / DEFERRED id DD-3-sub22",
            "IMPLEMENTATION_GAP: min_improvement / repeats / tolerance are undecided and never "
            "defaulted / DEFERRED id DD-3-sub20",
            "IMPLEMENTATION_GAP: candidate kind (reproducible execution sample vs pure prompt "
            "asset) undecided, so which tier may grant verified is unresolved "
            "/ DEFERRED id DD-3-sub24",
            "IMPLEMENTATION_GAP: `verified` is derived by S16 from this document, never stored as "
            "a claim here / 08:64-68, 12:458",
            "IMPLEMENTATION_GAP: who produces per-sample before/after scores (the Tier-1 re-run "
            "runner / M4 题面) is outside S15 and S16 / DEFERRED id DD-3-sub20 -- S16 adjudicates "
            "recorded run results, it does not execute the corpus",
        ]},
    }
    doc["bundle_digest"] = bundle_digest(doc)
    return doc


# --------------------------------------------------------------------- writes
def atomic_write_text(path: str, text: str) -> None:
    """One write mechanism, tmp-then-rename, for S15's derived artifacts at the operator-named
    --out-dir / --report. No store path is ever touched here, so S12's commit_batch does not own
    it and `kd_write_txn.py --audit` lists every site below as exempted, not hidden."""
    layout.assert_staging_path(path)
    layout.assert_staging_path(path + ".tmp")
    if os.path.lexists(path + ".tmp"):
        raise ValueError("refusing an existing temporary output")
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)   # KD-WRITE-EXEMPT: parent dir of an operator-named S15 derived artifact (answer side / bundle / fixture / report), never a store path
    tmp = path + ".tmp"
    with open(tmp, "x", encoding="utf-8") as fh:   # KD-WRITE-EXEMPT: tmp half of one write-once rename for a derived S15 artifact
        fh.write(text)                      # KD-WRITE-EXEMPT: the derived S15 artifact body (bundle / answer side / fixture / report), written once by this single emit path
        fh.flush()
        os.fsync(fh.fileno())               # KD-WRITE-EXEMPT: durability of the derived tmp only; a fsynced projection confers no authority
    os.replace(tmp, path)                   # KD-WRITE-EXEMPT: atomic publish of the derived S15 artifact at the operator-named path


def atomic_write_json(path: str, doc) -> None:
    atomic_write_text(path, json.dumps(doc, ensure_ascii=False, indent=1) + "\n")


class UsageError(Exception):
    """A CLI usage error. argparse's own exit code is 2, which is a CONTRACT code here meaning
    'isolation broken', so usage mistakes must never reach it: they exit 3."""


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise UsageError(message)


def emit(args, payload) -> bool:
    text = json.dumps(payload, ensure_ascii=False, indent=1)
    if args.report:
        try:
            atomic_write_text(args.report, text + "\n")
        except (OSError, ValueError, layout.LayoutViolation) as exc:
            print(f"kd_eval_freeze: could not write --report {args.report}: {exc}",
                  file=sys.stderr)
            return False
    print(text)
    return True


def refuse(args, code: str, detail: str, **extra) -> int:
    emit(args, dict({"status": "refused", "code": code, "detail": detail}, **extra))
    return EXIT_REFUSED_INPUT


def payload_without_status(base: dict) -> dict:
    """The summary block reused by a refusal path, minus its own `status` key so `refuse()`
    stays the single place a refusal's status is set."""
    return {key: value for key, value in base.items() if key != "status"}


def main(argv=None) -> int:
    ap = ArgumentParser(
        prog="kd_eval_freeze.py",
        description=("S15: freeze an eval corpus against a split contract, publish the answer "
                     "side separately, and PROVE exam isolation over every model-visible surface "
                     "declared. Contract 12-SKILL-DESIGN-BRIEF.md:123, schema SC09 "
                     "eval-bundle.schema.json, authority 08-EVAL-STRATEGY.md §1.3/§1.6."),
        epilog=("exit codes: 0 frozen + isolation proven clean; 2 isolation broken (model-visible "
                "answers) [contract]; 3 refused input; 5 filesystem failure. No model call, no "
                "network, and no defaulted threshold: prerequisite (c)'s numbers come from the "
                "split contract or (c) is recorded unsatisfied (08:44, 08:93)."))
    ap.add_argument("--corpus", metavar="FILE", required=True,
                    help="JSONL rows: sample_id, split, task_input, expected_behavior, "
                         "gold_answer (+ difficulty / category / source / is_original_failure)")
    ap.add_argument("--contract", metavar="FILE", required=True,
                    help="JSON split contract: dataset_id, splits, answer_visibility, "
                         "optimisation_loop.metric_ids, verdict_thresholds, floor_ceiling, "
                         "attribution, sample_kind, reproducible_rerun_claimed")
    ap.add_argument("--out-dir", metavar="DIR", required=True,
                    help="where to publish eval-bundle.json, fixture.jsonl and answers/ "
                         "(fresh operator-owned staging directory; frozen rounds and host-loaded paths are refused)")
    ap.add_argument("--instrument-id", metavar="ID", required=True,
                    help="five-tuple slot 1: the instrument that will adjudicate this corpus; "
                         "must differ from every optimisation_loop.metric_ids entry")
    ap.add_argument("--promoted-from", metavar="ARTIFACT_ID", required=True,
                    help="CM-48: the SC04 artifact whose promotion this eval adjudicates")
    ap.add_argument("--surface", action="append", default=[], metavar="NAME=PATH",
                    help="a model-visible surface root (repeatable), realpath-resolved before "
                         "containment is judged")
    ap.add_argument("--use-default-surfaces", action="store_true",
                    help="also scan this package's own references/, schemas/ and scripts/ trees")
    ap.add_argument("--report", metavar="FILE", help="also write the emitted JSON document here")
    args = ap.parse_args(argv)

    try:
        rows = load_corpus(args.corpus)
        contract = load_contract(args.contract)
    except (OSError, ValueError) as exc:
        return refuse(args, "UNUSABLE_INPUT", str(exc))

    loop_metric_ids = sorted({str(item).strip() for item in contract["optimisation_loop"]["metric_ids"]
                              if str(item).strip()})
    if not loop_metric_ids:
        return refuse(args, "PREREQ_A_UNASSESSABLE",
                      "optimisation_loop.metric_ids is empty: prerequisite (a) is a hard "
                      "assertion that the adjudicating metric id differs from the loop's metric "
                      "id (08:42), which cannot be stated against an empty set")

    try:
        surfaces = parse_surfaces(args.surface)
    except ValueError as exc:
        return refuse(args, "SURFACE_UNUSABLE", str(exc))
    if args.use_default_surfaces:
        for name, path in default_surfaces().items():
            surfaces.setdefault(name, path)
    if not surfaces:
        return refuse(args, "NO_SURFACE_DECLARED",
                      "isolation cannot be proven over an empty surface set: pass --surface "
                      "NAME=PATH for every model-visible root (or --use-default-surfaces). "
                      "Refusing here IS the dead man -- scanning nothing would otherwise be "
                      "reported as clean")
    for name, path in sorted(surfaces.items()):
        if not os.path.isdir(path):
            return refuse(args, "SURFACE_UNUSABLE",
                          f"surface {name!r} resolves to {path!r}, which is not a directory; a "
                          "missing root is refused rather than treated as clean")

    out_dir = os.path.realpath(os.path.abspath(args.out_dir))
    if is_skills_shaped(out_dir):
        return refuse(args, "PLACEMENT_MODEL_VISIBLE",
                      f"--out-dir {out_dir} sits inside a skills-shaped path, so the frozen "
                      "bundle and its answer side would ship as host-loadable assets")
    try:
        layout.assert_staging_path(out_dir)
    except layout.LayoutViolation as exc:
        return refuse(args, "PLACEMENT_PROTECTED", str(exc))

    failures = [row for row in rows if row.get("is_original_failure")]
    if len(failures) != 1:
        return refuse(args, "CM48_ORIGINAL_FAILURE_UNBOUND",
                      f"exactly one corpus row must carry is_original_failure=true, found "
                      f"{len(failures)}: an eval that cannot name the original defect cannot fail "
                      f"on the old behaviour and is decorative (08:29, CM-48)")
    if failures[0]["split"] != "holdout":
        return refuse(args, "CM48_ORIGINAL_FAILURE_NOT_IN_HOLDOUT",
                      f"the original failure {failures[0]['sample_id']!r} is in split "
                      f"{failures[0]['split']!r}; Tier-1's re-run sample must live in the "
                      "adjudicating set (08:27-08:29)")

    answers_dir = os.path.join(out_dir, "answers")
    guarded = adjudicator_only_rows(rows, contract)
    answer_texts = {row["sample_id"]: norm(row["gold_answer"]) for row in guarded}
    answer_files = [{"path": os.path.realpath(os.path.join(answers_dir, f"{row['sample_id']}.answer.json")),
                     "bytes": 0, "sha256": "", "owner_sample_id": row["sample_id"]}
                    for row in guarded]
    answer_payloads = []
    for entry, row in zip(answer_files, guarded):
        payload = json.dumps({"sample_id": row["sample_id"], "split": row["split"],
                                  "gold_answer": row["gold_answer"],
                                  "expected_behavior": row["expected_behavior"]},
                                 ensure_ascii=False, sort_keys=True) + "\n"
        answer_payloads.append(payload)
        entry["sha256"] = sha256_bytes(payload.encode("utf-8"))
        entry["bytes"] = len(payload.encode("utf-8"))
    if any(row["split"] not in contract["splits"] for row in rows):
        return refuse(args, "SPLIT_UNDECLARED", "corpus uses a split absent from its contract")
    try:
        isolation = scan_isolation(answer_texts, answer_files, surfaces)
    except (OSError, ValueError) as exc:
        return refuse(args, "SURFACE_UNSCANNED", str(exc))
    leaks = self_leaks(rows, {split for split, audience in contract["answer_visibility"].items()
                              if str(audience).casefold() in {"model", "agent", "all", "any"}})
    if leaks:
        isolation["breaches"] = sorted(isolation["breaches"] + leaks,
                                       key=lambda b: (b["kind"], b["document"], b["sample_id"]))
        isolation["status"] = "breach"

    prereqs = prerequisites(contract, rows, isolation, args.instrument_id, loop_metric_ids)
    subject = {"promoted_from_artifact_id": args.promoted_from,
               "original_failure_sample_id": failures[0]["sample_id"],
               "sample_kind": contract.get("sample_kind", "undecided"),
               "reproducible_rerun_claimed": contract.get("reproducible_rerun_claimed")}
    bundle = build_bundle(contract, rows, answer_files, isolation, prereqs, args.instrument_id,
                          loop_metric_ids, subject)
    summary = {"status": isolation["status"], "dataset_id": bundle["dataset_id"],
               "bundle_digest": bundle["bundle_digest"], "instrument_id": args.instrument_id,
               "loop_metric_ids": sorted(loop_metric_ids),
               "collision": args.instrument_id in loop_metric_ids,
               "isolation": isolation, "prerequisites": prereqs,
               "artifacts": {"bundle": None, "fixture": None, "answer_files": []},
               "planned_answer_files": [entry["path"] for entry in answer_files]}

    if isolation["status"] == "breach":
        # contract exit 2. NOTHING that claims a freeze is published: a breach is not a bundle
        # with a note attached. Planned answer files have NOT been written.
        emit(args, dict(summary, code="ISOLATION_BROKEN",
                                     detail="answer material is reachable from a model-visible "
                                            "surface, so any score computed against this corpus "
                                            "would be meaningless (08:45, 12:244)"))
        return EXIT_ISOLATION_BROKEN
    if isolation["status"] == "unscanned":
        return refuse(args, "SURFACE_UNSCANNED",
                      "a declared surface contained no host-loadable document, so cleanliness "
                      "was not established for it; the alternative would be a guard that can "
                      "never fail", **payload_without_status(summary))

    fixture = [{"sample_id": item["sample_id"], "split": item["split"],
                "task_input": item["task_input"]} for item in bundle["samples"]]
    validation = kd_validate.validate_artifact(KIND, bundle)
    summary["schema_validation"] = {"valid": bool(validation.get("valid")),
                                    "code": validation.get("code"),
                                    "violations": list(validation.get("violations", []))[:8]}
    if not validation.get("valid"):
        return refuse(args, "SC09_VALIDATION_FAILED", "invalid freeze refused before publication",
                      **payload_without_status(summary))
    try:
        bundle_path = os.path.join(out_dir, "eval-bundle.json")
        fixture_path = os.path.join(out_dir, "fixture.jsonl")
        targets = [bundle_path, fixture_path] + [entry["path"] for entry in answer_files]
        if any(os.path.lexists(target) for target in targets):
            return refuse(args, "FROZEN_OUTPUT_EXISTS", "freeze outputs are immutable; choose a fresh output directory")
        for entry, payload in zip(answer_files, answer_payloads):
            atomic_write_text(entry["path"], payload)
            summary["artifacts"]["answer_files"].append(entry["path"])
        atomic_write_json(bundle_path, bundle)
        atomic_write_text(fixture_path, "".join(
            json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in fixture))
        summary["artifacts"]["bundle"] = bundle_path
        summary["artifacts"]["fixture"] = fixture_path
    except (OSError, ValueError, layout.LayoutViolation) as exc:
        return refuse(args, "FS_FAILURE", str(exc))
    return EXIT_OK if emit(args, summary) else EXIT_REFUSED_INPUT


if __name__ == "__main__":
    try:
        sys.exit(main())
    except UsageError as exc:
        print(f"kd_eval_freeze: usage error: {exc}", file=sys.stderr)
        sys.exit(EXIT_REFUSED_INPUT)
