"""S05 -- kd_identity_key: deterministic multi-field identity, with a self-audit that makes
"single field + strip()/trim() as identity" mechanically impossible.

Round 2 provenance for the adjudicated shape
  04-DETERMINISTIC-VS-LLM.md:52 row 6  "canonical key 由代码从归一化字段派生（trim / strip `.md` /
                                 lowercase / `_`+空格->`-` / kebab slug / scope 三元组 / hash）"
  04-DETERMINISTIC-VS-LLM.md:133 7.1   the `02` defect: aggregation key was the model's free string
                                 `candidate.workflow_key.trim()` (engine.rs:2927) with NO content hash
                                 in the identity path -- recorded as an anti-pattern, not a template.
  12-SKILL-DESIGN-BRIEF.md:523 gate 3  "键至少含 归一化模式身份 + scope + 来源 worker，
                                 禁止单字段 strip/trim 作身份。 实现: S05"
  05-DATA-MODEL.md:121-124 (5.1) "L0 主判（唯一持有自动计数与写盘权）：
                                 identity = sha256( canonical 字段 NUL-join )[0:40]  ||  显式 Pattern-Key 字段
                                 canonical 字段 = 结构化语义字段精确等值，簿记字段排除"
  12-SKILL-DESIGN-BRIEF.md:725 item 10 "规范化测试向量集（NFKC + 大小写/空白/标点 + kebab slug +
                                 scope + 来源 worker）全通过；grep 确认无单字段 strip()/trim() 作身份"

TWO AXES, NOT ONE CONJUNCTION (ESC-W1-01 re-adjudication, Wave 2 construction constraint 1)
  `05:122` states the identity as `sha256( canonical 字段 NUL-join )[0:40] ‖ 显式 Pattern-Key 字段`:
  a digest over the canonical fields AND a second, explicit Pattern-Key axis. `05:126` (CM-25) says
  that Pattern-Key is 「LLM 命名、确定性校验」-- a model product -- and `contracts.stages` puts the
  naming at Stage 3 step 12 while dedup/identity (S05/S06) is Stage 2 steps 9-11. `12:114` declares
  S06's input as `evidence.filtered.jsonl`, and an Evidence record carries neither a Pattern-Key nor
  a worker attribution (schemas/evidence.schema.json: `produced_by` is {kind, detail} only, and
  `05` §6 line 244 lists no worker column). So a Stage-2 gate may not hard-require a Stage-3
  product: `pattern_key` and `source_worker` are axes that PARTICIPATE WHEN PRESENT (and, when
  present, are validated and must move the digest), while the semantic field and the scope triple
  stay mandatory. That is exactly the shape of the adjudicated constraint, quoted at `05:261`
  (DM-1) and `04:192` (D6-a): 「必须含 scope + 语义字段 + 排除簿记字段」.

Still deferred (NOT decided here): 05-DATA-MODEL.md sec 7 DM-1 leaves the final canonical field list
and the digest truncation length open; DD-2-sub16..sub19 in
.distill/round-3/DEFERRED-PARAMETERS.yaml keep similarity out of the write path. See
IDENTITY_FIELD_SPEC below, which is marked provisional.

python3 stdlib only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

SCHEMA_VERSION = "1"

# --------------------------------------------------------------------------- exit codes (contract)
EXIT_OK = 0
EXIT_INPUT_ERROR = 1        # unreadable / malformed record or spec
EXIT_IDENTITY_GUARD = 2     # contract: "2=出现单字段 strip/trim 作身份"
EXIT_SPEC_INVALID = 5        # the field spec itself is not usable (unknown source path, bad group)
#: a derived report could not be emitted. Deliberately NOT 1/2/5: an unusable output path is
#: neither an input failure nor an identity verdict, and must never be read as one.
EXIT_OUTPUT_ERROR = 4

# --------------------------------------------------------------------------- normalisation
NORMALIZER_SET = "kd-identity-v1"
TRIM_ONLY_OPS = frozenset({"strip", "trim"})
#: the adjudicated pipeline, in order (04:52). Anything outside this set is refused rather
#: than silently applied -- a wider fold is a DEFERRED parameter (DD-2-sub19).
PIPELINE_OPS = ("nfkc", "trim", "strip_md", "lower", "underscore_space_to_hyphen", "kebab_slug")

_MD_SUFFIX = re.compile(r"\.md$", re.IGNORECASE)
_DASHES = re.compile(r"-{2,}")


def _slugify(value: str) -> str:
    """kebab slug: drop punctuation, keep every alphanumeric of EVERY script.

    Deliberately not `[^a-z0-9-]`: a Latin-only class would fold all CJK text to the empty
    string and collapse distinct Chinese patterns into one identity -- 05-DATA-MODEL.md:125
    cites CM-26 `11:exact-duplicate-identity` together with `test_t0_preserves_distinct_text`
    and "8 组中文/语序/标点对抗", i.e. word order and script must survive the narrow fold.
    """
    return "".join(ch if (ch.isalnum() or ch == "-") else "-" for ch in value)

#: 05 sec 5.1 writes the truncation as `[0:40]`; DM-1 defers the final length, so it is a
#: named constant restated per record in `derivation.digest_len` instead of being buried.
# IMPLEMENTATION_GAP: digest truncation length not adjudicated / DEFERRED id DM-1 (05-DATA-MODEL.md sec 7)
DIGEST_LEN = 40

#: separator for the NUL-join of canonical fields (05:121 "canonical 字段 NUL-join")
FIELD_JOIN = "\x00"
#: the `||` in `sha256(...)[0:40] || 显式 Pattern-Key 字段`. kebab_slug removes '#' from every
#: normalized value, so this delimiter cannot be forged by content.
IDENTITY_JOIN = "#"

#: DC-SP-1 gate 3 (12:523) names three groups, and every one of them must be DECLARED by a spec:
#: dropping a group from the spec is a contract reduction, not a simplification.
REQUIRED_GROUPS = ("semantic", "scope", "worker")
#: Of those, the groups whose values the record must actually carry. `worker` is deliberately NOT
#: here: `05` §6 line 244 gives Evidence no worker column and `12:114` makes that stream S06's
#: input, so requiring a value would gate Stage 2 on a Stage 3 product (ESC-W1-01). A worker that
#: IS present still joins, is still validated and is still probed for sensitivity.
PRESENCE_REQUIRED_GROUPS = ("semantic", "scope")

# PROVISIONAL-CANONICAL-FIELD-SET: this list is the adjudicated MINIMUM, not a decision about
# which fields are canonical forever. `05` sec 7 DM-1 / `04` D6-a defer the final field list to a
# divergence measurement over >=50 real candidates; the constraint they do fix is
# 「必须含 scope + 语义字段 + 排除簿记字段」, which is what this spec encodes:
#   * semantic axis  -- the statement carried by the record (Pattern-Key when a model named one,
#                       origin.problem on an Evidence record); >= 1 must be present,
#   * scope axis     -- the typed triple, all three required (05 sec 5.3 S1, fail-closed),
#   * worker axis    -- participates when present (12:523 gate 3, Pattern layer),
#   * bookkeeping    -- EXCLUDED by construction: `canonical_pairings` reads only declared fields,
#                       so generation{..}/created_at, evidence.status/status_basis, record_locator,
#                       refs_integrity and every *_count counter cannot enter the join.
# IMPLEMENTATION_GAP: canonical field list / DEFERRED id DM-1 (05-DATA-MODEL.md sec 7)
# The cohort triple is NOT a canonical field: `cohort.path` is the DISTINCT-COHORT axis of support
# (05 sec 5.4 / kd_provenance.cohort_key), and folding it into the identity would split one
# identity per path and destroy the support rule S06 is built to compute.
DEFAULT_IDENTITY_SPEC = {
    "normalizer_set": NORMALIZER_SET,
    "fields": [
        "pattern_key",            # axis 2 (05:122 `‖ 显式 Pattern-Key 字段`): participates if present
        "origin.problem",         # semantic statement an Evidence record does carry (05 sec 2 line 42)
        "scope.workspace",        # scope triple, S1 fail-closed (05:174)
        "scope.project",
        "scope.layer",
        "source_worker",          # provenance worker (12:523): participates if present
    ],
    #: declared fields that must carry a value on the record; the semantic minimum is enforced by
    #: the group predicate instead of by naming one field, because DM-1 has not chosen the field.
    #: A spec without this key requires every declared field (the Wave 1 behaviour).
    "required_fields": ["scope.workspace", "scope.project", "scope.layer"],
    "groups": {
        "semantic": ["pattern_key", "origin.problem"],
        "scope": ["scope.workspace", "scope.project", "scope.layer"],
        "worker": ["source_worker"],
    },
    "normalizers": list(PIPELINE_OPS),
}


class IdentityGuardViolation(Exception):
    """Raised by the self-audit when a derivation would not be a real identity."""

    def __init__(self, violations: list):
        super().__init__("; ".join(v["message"] for v in violations))
        self.violations = violations


# --------------------------------------------------------------------------- the pipeline
def normalize_token(text, ops=PIPELINE_OPS) -> str:
    """Apply the adjudicated normalisation rules in order. Deterministic and total."""
    if text is None:
        raise ValueError("normalize_token refuses None: an absent identity field is a "
                         "fail-closed case, not an empty string")
    value = text if isinstance(text, str) else json.dumps(text, sort_keys=True, ensure_ascii=False)
    for op in ops:
        if op == "nfkc":
            value = unicodedata.normalize("NFKC", value)
        elif op in ("trim", "strip"):
            value = value.strip()
        elif op == "strip_md":
            value = _MD_SUFFIX.sub("", value)
        elif op == "lower":
            value = value.lower()
        elif op == "underscore_space_to_hyphen":
            value = re.sub(r"[_\s]+", "-", value)
        elif op == "kebab_slug":
            value = _DASHES.sub("-", _slugify(value)).strip("-")
        else:
            raise ValueError(f"unknown normalizer {op!r}; the pipeline is closed at {PIPELINE_OPS} "
                             "and widening it is a DEFERRED parameter (DD-2-sub19)")
    return value


def _lookup(record: dict, dotted: str):
    node = record
    for part in dotted.split("."):
        if isinstance(node, dict):
            if part not in node:
                return None
            node = node[part]
        elif isinstance(node, list) and part.isdigit() and int(part) < len(node):
            node = node[int(part)]
        else:
            return None
    return node


def _field_value(record: dict, dotted: str, ops) -> str | None:
    """Normalized value of one declared canonical field: None when the record does not carry it,
    "" when the narrow fold erases a value that IS there. Both states are audited
    (`audit_derivation`), and neither is silently joined."""
    raw = _lookup(record, dotted)
    return None if raw is None else normalize_token(raw, ops)


def declared_required(spec: dict) -> list:
    """Declared fields that must carry a value. Absent key == every declared field required, which
    is the Wave 1 behaviour, so an older spec file cannot become looser by omission."""
    return list(spec.get("required_fields") if spec.get("required_fields") is not None
                else spec["fields"])


def pairings_for(record: dict, spec: dict):
    """[(field, value)] for the fields that PARTICIPATE, in DECLARED ORDER, plus the declared
    fields this record did not contribute. The declared list order is part of the key contract, so
    a caller cannot reshuffle fields into a different identity."""
    ops = tuple(spec.get("normalizers") or PIPELINE_OPS)
    required = set(declared_required(spec))
    pairs, skipped = [], []
    for name in spec["fields"]:
        value = _field_value(record, name, ops)
        if value is None or value == "":
            if name in required:
                raise ValueError(f"required canonical field {name!r} is absent from this record: an "
                                 "absent identity field is a fail-closed case, not an empty string")
            skipped.append(name)
            continue
        pairs.append((name, value))
    return pairs, skipped


def canonical_pairings(record: dict, spec: dict):
    """The participating (field, value) pairs only -- see `pairings_for`."""
    return pairings_for(record, spec)[0]


def derive_key(record: dict, spec: dict = None) -> dict:
    """Deterministic identity derivation. Returns the canonical key, the sha256 digest and the
    `||`-concatenated identity, plus the re-derivation record required by SC03.identity."""
    spec = spec or DEFAULT_IDENTITY_SPEC
    pairs, skipped = pairings_for(record, spec)
    canonical_key = FIELD_JOIN.join(f"{name}={value}" for name, value in pairs)
    digest = hashlib.sha256(canonical_key.encode("utf-8")).hexdigest()[:DIGEST_LEN]
    pattern_key = next((v for n, v in pairs if n.endswith("pattern_key")), "")
    identity = digest + IDENTITY_JOIN + pattern_key if pattern_key else digest
    groups = spec.get("groups") or {}
    joined = {name for name, _ in pairs}
    #: which axes this record actually contributed -- recorded so an absent optional axis is
    # visible in the artifact instead of being a silent weakening of the predicate
    axes = [g for g, members in groups.items() if any(m in joined for m in members)]
    return {
        "identity": identity,
        "identity_digest": digest,
        "canonical_key": canonical_key,
        "pattern_key": pattern_key,
        "canonical_pairs": [{"field": n, "normalized": v} for n, v in pairs],
        "layer": "L0",
        "derivation": {
            "canonical_fields": [n for n, _ in pairs],
            "absent_optional_fields": skipped,
            "axes_participating": sorted(axes),
            "normalizer_set": spec.get("normalizer_set", NORMALIZER_SET),
            "scope_triple": [str(_lookup(record, f) or "") for f in
                             groups.get("scope", ["scope.workspace", "scope.project", "scope.layer"])],
            "source_worker": str(_lookup(record, "source_worker") or ""),
            "digest_len": DIGEST_LEN,
        },
    }


# --------------------------------------------------------------------------- THE SELF-AUDIT
def _perturbed(record: dict, group: str, fields: list) -> dict:
    """Deterministic probe: change every field of one required group and nothing else."""
    clone = json.loads(json.dumps(record, ensure_ascii=False))
    for dotted in fields:
        parts = dotted.split(".")
        node = clone
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        original = _lookup(clone, dotted)
        marker = "\x01probe"                     # removed by kebab_slug, so it changes nothing
        node[parts[-1]] = (original if isinstance(original, str) else str(original or "")) + marker
    return clone


def audit_derivation(record: dict, spec: dict) -> list:
    """A real predicate over the key derivation, not a style comment.

    Three independent checks; every one of them has produced a finding in a reference project:

    A. declared shape -- a single field normalised only by strip()/trim() is the `02` defect
       (04:133 7.1) and is refused outright.
    B. group coverage -- each mandatory group (semantic / scope / worker) must contribute at
       least one declared field (12:523 gate 3).
    C. sensitivity -- for each mandatory group, mutating that group's values MUST change the
       digest. A group that is present in the record but absent from the join is exactly the
       "computed but never consumed" failure the kernel was built to refuse (RT-05).

    Making `pattern_key` / `source_worker` optional axes does not relax B or C: a group is skipped
    only when the record carries NO value for any of its members, only for the groups that are
    legitimately absent at this layer (see PRESENCE_REQUIRED_GROUPS), and every skip is written
    into the derivation as `absent_optional_fields` / `axes_participating` so it is auditable.
    """
    violations = []
    fields = list(spec.get("fields") or [])
    ops = tuple(spec.get("normalizers") or PIPELINE_OPS)     # ORDERED: the pipeline is positional
    op_set = set(ops)
    groups = spec.get("groups") or {}
    required = declared_required(spec)

    unknown_required = [f for f in required if f not in fields]
    if unknown_required:
        violations.append({"code": "REQUIRED_FIELD_NOT_DECLARED",
                           "message": f"{unknown_required} are marked required but are not declared "
                                      "in `fields`, so no probe can see them"})
    grouped = {m for members in groups.values() for m in members if m}
    ungrouped = [f for f in fields if f not in grouped]
    if ungrouped:
        violations.append({"code": "FIELD_NOT_IN_ANY_GROUP",
                           "message": f"{ungrouped} join the digest but belong to no audited group: "
                                      "coverage and sensitivity cannot be checked for them"})

    if len(fields) == 1 and op_set <= TRIM_ONLY_OPS:
        violations.append({
            "code": "TRIM_ONLY_IDENTITY",
            "message": f"single-field identity {fields[0]!r} normalised only by "
                       f"{sorted(op_set)} is not an identity (04 sec 7.1: `workflow_key.trim()` "
                       "is the recorded anti-pattern)",
        })
    if len(fields) < 2:
        violations.append({"code": "SINGLE_FIELD_IDENTITY",
                           "message": f"identity needs more than one canonical field, got {fields}"})
    if not op_set - TRIM_ONLY_OPS:
        violations.append({"code": "TRIM_ONLY_PIPELINE",
                           "message": f"normaliser set {sorted(op_set)} is whitespace-only; the "
                                      f"adjudicated pipeline is {' + '.join(PIPELINE_OPS)}"})

    #: a declared value that the narrow fold erases cannot move a digest: for a required canonical
    #: field it is a hole, for the explicit Pattern-Key it is the second axis silently lost
    #: (05:126 「LLM 命名、确定性校验」= the naming is free, the validation is not).
    for name in fields:
        raw = _lookup(record, name)
        if raw is None or name not in grouped:
            continue
        try:
            erased = normalize_token(raw, ops) == ""
        except ValueError:
            erased = False
        if erased:
            violations.append({"code": "IDENTITY_FIELD_FOLDS_TO_EMPTY",
                               "message": f"{name} is present on this record but normalises to the "
                                          "empty string, so it contributes nothing to the NUL-join "
                                          "(05 sec 5.3 S1 is fail-closed non-empty)"})

    for group in REQUIRED_GROUPS:
        members = [f for f in groups.get(group, []) if f]
        if not members:
            violations.append({"code": "MISSING_GROUP",
                               "message": f"required identity group {group!r} contributes no field "
                                          "(12 sec 523 gate 3: normalized identity + scope + worker)"})
            continue
        for member in members:
            if member not in fields:
                violations.append({"code": "GROUP_FIELD_NOT_IN_JOIN",
                                   "message": f"{group}.{member} is declared but never NUL-joined "
                                              "into the canonical key"})
        #: presence is a property of the RECORD, not of the join: a member the record carries but
        #: the spec does not join is exactly the "computed but never consumed" shape, and it has to
        #: be caught by the probe below rather than filtered out of it.
        present = [m for m in members if _field_value(record, m, ops)]
        if not present:
            if group in PRESENCE_REQUIRED_GROUPS:
                violations.append({"code": "MISSING_CANONICAL_FIELD",
                                   "message": f"group {group!r} has no value on this record: "
                                              f"members {members} are all absent"})
            continue
        try:
            base = derive_key(record, spec)
            probe = derive_key(_perturbed(record, group, present), spec)
        except ValueError as exc:
            # a required identity field is absent or null: fail closed, never derive a key
            # from a hole in the record (05 sec 5.3 S1 is the same rule for scope)
            violations.append({"code": "MISSING_CANONICAL_FIELD",
                               "message": f"group {group!r} cannot be derived from this record: {exc}"})
            continue
        if base["identity_digest"] == probe["identity_digest"]:
            violations.append({"code": "INSENSITIVE_GROUP",
                               "message": f"digest unchanged when group {group!r} changed -- the "
                                          "group is decorative, so this is a strip-only identity "
                                          "by another name"})
    return violations


def checked_derive(record: dict, spec: dict = None) -> dict:
    """derive_key behind the audit. Raises IdentityGuardViolation instead of returning a key
    that cannot be trusted -- callers that catch nothing get exit 2 by construction."""
    spec = spec or DEFAULT_IDENTITY_SPEC
    violations = audit_derivation(record, spec)
    if violations:
        raise IdentityGuardViolation(violations)
    return derive_key(record, spec)


# --------------------------------------------------------------------------- normalisation vectors
#: 12:725 item 10 demands a normalisation vector set covering NFKC + case/whitespace/punctuation
#: + kebab slug + scope + source worker. Every vector runs the FULL adjudicated pipeline, so the
#: expectation is what a reviewer can recompute by hand from PIPELINE_OPS order.
NORMALIZATION_VECTORS = [
    {"id": "V01-whitespace-trim", "input": "  Retry-Timeouts  ", "expect": "retry-timeouts"},
    {"id": "V02-nfkc-fullwidth", "input": "ＲＥＴＲＹ＿ＴＩＭＥＯＵＴ", "expect": "retry-timeout"},
    {"id": "V03-nfkc-nbsp", "input": "retry\xa0timeouts", "expect": "retry-timeouts"},
    {"id": "V04-strip-md-suffix", "input": "docs/Retry_Timeouts.md", "expect": "docs-retry-timeouts"},
    {"id": "V05-underscore-space-run", "input": "retry__timeouts  slow", "expect": "retry-timeouts-slow"},
    # the parenthesised ".md" is not a suffix, so strip_md leaves it and the slug keeps its letters
    {"id": "V06-punctuation-collapse", "input": "retry(.md)?; timeouts!!", "expect": "retry-md-timeouts"},
    {"id": "V07-case-fold", "input": "ReTrY-TiMeOuTs", "expect": "retry-timeouts"},
    {"id": "V08-cjk-word-order-a", "input": "超时重试", "expect": "超时重试"},
    {"id": "V09-cjk-word-order-b", "input": "重试超时", "expect": "重试超时"},
    {"id": "V10-trailing-md-uppercase", "input": "  Retry.Timeouts.MD ", "expect": "retry-timeouts"},
    {"id": "V11-punctuation-only-is-empty", "input": "---;;;---", "expect": ""},
]

#: what S03 hands to S06 per `12:114`: an Evidence-shaped record, i.e. `05` §6 line 244's columns
#: with the semantic statement and the scope triple present and NEITHER optional axis
EVIDENCE_SHAPED_RECORD = {
    "origin": {"problem": "gateway retries must be capped"},
    "scope": {"workspace": "ws-one", "project": "pj-one", "layer": "project"},
}

#: the key-level half of the same requirement: scope and source worker must be IN the key,
#: and the trim-only shape must be refused. `expect` is a predicate over two derivations.
KEY_VECTORS = [
    {"id": "K01-scope-changes-key", "kind": "differs",
     "a": {"pattern_key": "Retry_Timeouts", "scope": {"workspace": "ws-a", "project": "p1", "layer": "project"},
           "source_worker": "worker-01"},
     "b": {"pattern_key": "Retry_Timeouts", "scope": {"workspace": "ws-b", "project": "p1", "layer": "project"},
           "source_worker": "worker-01"}},
    {"id": "K02-worker-changes-key", "kind": "differs",
     "a": {"pattern_key": "retry-timeouts", "scope": {"workspace": "ws-a", "project": "p1", "layer": "project"},
           "source_worker": "worker-01"},
     "b": {"pattern_key": "retry-timeouts", "scope": {"workspace": "ws-a", "project": "p1", "layer": "project"},
           "source_worker": "worker-02"}},
    {"id": "K03-layer-changes-key", "kind": "differs",
     "a": {"pattern_key": "retry-timeouts", "scope": {"workspace": "ws-a", "project": "p1", "layer": "project"},
           "source_worker": "worker-01"},
     "b": {"pattern_key": "retry-timeouts", "scope": {"workspace": "ws-a", "project": "p1", "layer": "global"},
           "source_worker": "worker-01"}},
    {"id": "K04-noise-does-not-change-key", "kind": "same",
     "a": {"pattern_key": "  Retry.Timeouts  ", "scope": {"workspace": "ws-a", "project": "p1", "layer": "project"},
           "source_worker": "worker-01"},
     "b": {"pattern_key": "RETRY__TIMEOUTS", "scope": {"workspace": "ws-a", "project": "p1", "layer": "project"},
           "source_worker": "worker-01"}},
    {"id": "K05-cjk-word-order-stays-distinct", "kind": "differs",
     "a": {"pattern_key": "超时重试", "scope": {"workspace": "ws-a", "project": "p1", "layer": "project"},
           "source_worker": "worker-01"},
     "b": {"pattern_key": "重试超时", "scope": {"workspace": "ws-a", "project": "p1", "layer": "project"},
           "source_worker": "worker-01"}},
    # ---- ESC-W1-01: the two axes of `05:122`, and the 「簿记字段排除」 half of DM-1
    {"id": "K06-evidence-shaped-record-derives", "kind": "derives",
     "a": dict(EVIDENCE_SHAPED_RECORD)},
    {"id": "K07-explicit-pattern-key-participates", "kind": "differs",
     "a": dict(EVIDENCE_SHAPED_RECORD),
     "b": dict(EVIDENCE_SHAPED_RECORD, pattern_key="gateway-retries-must-be-capped")},
    {"id": "K07b-pattern-key-noise-does-not-split", "kind": "same",
     "a": dict(EVIDENCE_SHAPED_RECORD, pattern_key="Gateway_Retries_Must.Be Capped.md"),
     "b": dict(EVIDENCE_SHAPED_RECORD, pattern_key="  gateway retries must be capped  ")},
    {"id": "K08-bookkeeping-never-changes-identity", "kind": "same",
     "a": dict(EVIDENCE_SHAPED_RECORD, evidence={"status": "UNVERIFIED", "status_basis": None},
               generation={"created_at": "2026-10-06T00:00:00Z", "round_id": "round-3"},
               record_locator="store/_ledger/lifecycle.jsonl#1"),
     "b": dict(EVIDENCE_SHAPED_RECORD, evidence={"status": "VERIFIED",
                                                 "status_basis": "ci://runs/4471"},
               generation={"created_at": "2026-10-07T11:22:33Z", "round_id": "round-4"},
               record_locator="store/_ledger/lifecycle.jsonl#99")},
    # `cohort.path` is the DISTINCT-COHORT axis of support (05 sec 5.4), never an identity field:
    # folding it in would split one identity per path and destroy the support rule S06 computes.
    {"id": "K09-cohort-path-is-not-identity", "kind": "same",
     "a": dict(EVIDENCE_SHAPED_RECORD, cohort={"workspace": "ws-one", "project": "pj-one",
                                               "path": "src/gateway"}),
     "b": dict(EVIDENCE_SHAPED_RECORD, cohort={"workspace": "ws-one", "project": "pj-one",
                                               "path": "tests"})},
]


def _spec_not_joining(*names: str) -> dict:
    """Sabotage used by the guard vectors: the group is still DECLARED (so gate 3's coverage cannot
    be satisfied by deleting it) but the field is removed from the join. If the record carries a
    value there, the sensitivity probe must see it as a decorative axis."""
    spec = json.loads(json.dumps(DEFAULT_IDENTITY_SPEC))
    spec["fields"] = [f for f in spec["fields"] if f not in names]
    spec["required_fields"] = [f for f in spec["required_fields"] if f not in names]
    return spec


#: executable guard rows: `expect` "clean" means the adjudicated predicate must accept the record,
#: a list means every named code must fire.
GUARD_VECTORS = [
    {"id": "G03-evidence-shaped-accepted", "record": dict(EVIDENCE_SHAPED_RECORD),
     "spec": DEFAULT_IDENTITY_SPEC, "expect": "clean"},
    {"id": "G04-no-semantic-field-refused",
     "record": {"scope": {"workspace": "ws-a", "project": "p1", "layer": "project"}},
     "spec": DEFAULT_IDENTITY_SPEC, "expect": ["MISSING_CANONICAL_FIELD"]},
    {"id": "G05-no-scope-refused", "record": {"origin": {"problem": "x"}},
     "spec": DEFAULT_IDENTITY_SPEC, "expect": ["MISSING_CANONICAL_FIELD"]},
    {"id": "G06-worker-present-but-not-joined-refused",
     "record": dict(EVIDENCE_SHAPED_RECORD, source_worker="worker-01"),
     "spec": _spec_not_joining("source_worker"),
     "expect": ["GROUP_FIELD_NOT_IN_JOIN", "INSENSITIVE_GROUP"]},
    {"id": "G07-semantic-present-but-not-joined-refused",
     "record": dict(EVIDENCE_SHAPED_RECORD),
     "spec": _spec_not_joining("origin.problem"),
     "expect": ["GROUP_FIELD_NOT_IN_JOIN", "INSENSITIVE_GROUP"]},
    {"id": "G08-empty-pattern-key-refused",
     "record": dict(EVIDENCE_SHAPED_RECORD, pattern_key="---;;;---"),
     "spec": DEFAULT_IDENTITY_SPEC, "expect": ["IDENTITY_FIELD_FOLDS_TO_EMPTY"]},
]

#: the rejected shape, kept as an executable counter-example (04 sec 7.1 / `02` engine.rs:2927)
TRIM_ONLY_CANDIDATE_SPEC = {
    "normalizer_set": "trim-only-legacy",
    "fields": ["workflow_key"],
    "groups": {"semantic": ["workflow_key"]},
    "normalizers": ["trim"],
}


def run_vectors() -> list:
    """Execute both halves of the vector set and return machine-checkable rows."""
    rows = []
    for vec in NORMALIZATION_VECTORS:
        got = normalize_token(vec["input"])
        rows.append({"id": vec["id"], "layer": "normalisation", "input": vec["input"],
                     "expect": vec["expect"], "got": got, "pass": got == vec["expect"]})
    for vec in KEY_VECTORS:
        da = derive_key(vec["a"])["identity_digest"]
        row = {"id": vec["id"], "layer": "key", "expect": vec["kind"], "digest_a": da}
        if vec["kind"] == "derives":
            axes = derive_key(vec["a"])["derivation"]["axes_participating"]
            row["got"] = "axes=" + ",".join(axes)
            row["pass"] = bool(da) and {"semantic", "scope"} <= set(axes)
        else:
            db = derive_key(vec["b"])["identity_digest"]
            row["digest_b"] = db
            row["pass"] = (da == db) if vec["kind"] == "same" else (da != db)
        rows.append(row)
    for vec in GUARD_VECTORS:
        codes = sorted({v["code"] for v in audit_derivation(vec["record"], vec["spec"])})
        if vec["expect"] == "clean":
            rows.append({"id": vec["id"], "layer": "guard", "expect": "clean",
                         "got": codes, "pass": not codes})
        else:
            missing = [c for c in vec["expect"] if c not in codes]
            rows.append({"id": vec["id"], "layer": "guard", "expect": vec["expect"],
                         "got": codes, "pass": not missing})
    guard = audit_derivation({"workflow_key": "  anything  "}, TRIM_ONLY_CANDIDATE_SPEC)
    rows.append({"id": "G01-trim-only-refused", "layer": "guard", "expect": "violations",
                 "got": [v["code"] for v in guard], "pass": bool(guard)})
    clean = audit_derivation(KEY_VECTORS[0]["a"], DEFAULT_IDENTITY_SPEC)
    rows.append({"id": "G02-adjudicated-spec-accepted", "layer": "guard", "expect": "clean",
                 "got": [v["code"] for v in clean], "pass": not clean})
    return rows


# --------------------------------------------------------------------------- CLI
def _load_json(path: str):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


#: W1-F's spine run reached S06's write line only after ESC-W1-01 stopped gating it, and died with
#: an uncaught FileNotFoundError (exit 1, no artifact) because the harness names `--out` inside a
#: directory nothing had created -- the same "an I/O failure reads as a verdict code" shape W1-F
#: filed against S09. The parent of an operator-named DERIVED-REPORT path is therefore created, and
#: every write is wrapped. `--dry-run` never calls this, so it still writes and creates nothing
#: (05 sec 5.2 "--dry-run 不写不建目录").
def write_derived_report(path: str, text: str) -> None:
    import kd_store_layout as layout
    if text and not text.endswith("\n"):
        text += "\n"
    try:
        layout.write_staging_text(path, text, create_parents=True)
    except layout.LayoutViolation as exc:
        raise OSError("derived report target is protected") from exc


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="kd_identity_key.py",
        description="S05 deterministic multi-field identity key (NFKC + kebab slug + NUL-join + "
                    "sha256) with a self-audit that exits 2 on a single-field strip/trim identity.")
    ap.add_argument("--record", help="candidate record (JSON object) to derive an identity for")
    ap.add_argument("--spec", help="identity field spec; defaults to the adjudicated minimum")
    ap.add_argument("--out", help="write the derivation result JSON here")
    ap.add_argument("--vectors", action="store_true", help="run the normalisation test vector set")
    ap.add_argument("--audit-only", action="store_true",
                    help="run the self-audit and report, without emitting a key")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    if args.vectors:
        rows = run_vectors()
        passed = sum(1 for r in rows if r["pass"])
        payload = {"normalizer_set": NORMALIZER_SET, "pipeline": list(PIPELINE_OPS),
                   "passed": passed, "total": len(rows), "vectors": rows}
        if args.out:
            try:
                write_derived_report(args.out, json.dumps(payload, ensure_ascii=False,
                                                           sort_keys=True, indent=1))
            except OSError as exc:
                print(f"output error: {exc}", file=sys.stderr)
                return EXIT_OUTPUT_ERROR
        if not args.quiet:
            for r in rows:
                detail = r.get("expect", "")
                got = r.get("got", r.get("digest_b", ""))
                if isinstance(got, list):
                    got = ",".join(got)
                print(f"{r['id']:<32} {r['layer']:<14} {'PASS' if r['pass'] else 'FAIL'}  "
                      f"expect={detail!r} got={got!r}")
            print(f"identity vectors: {passed}/{len(rows)} "
                  f"(normalisation {len(NORMALIZATION_VECTORS)} + key/guard "
                  f"{len(rows) - len(NORMALIZATION_VECTORS)})")
        return EXIT_OK if passed == len(rows) else EXIT_INPUT_ERROR

    if not args.record:
        # deliberately not argparse's ap.error(), which exits 2 and would collide with the
        # contractual "2 = trim-only identity" code
        print("usage error: --record is required unless --vectors is given", file=sys.stderr)
        return EXIT_INPUT_ERROR
    try:
        record = _load_json(args.record)
        spec = _load_json(args.spec) if args.spec else DEFAULT_IDENTITY_SPEC
    except OSError as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    except ValueError as exc:
        print(f"input error: malformed JSON: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    if not isinstance(record, dict) or not isinstance(spec, dict) or "fields" not in spec:
        print("input error: record must be an object and spec must declare `fields`", file=sys.stderr)
        return EXIT_SPEC_INVALID

    violations = audit_derivation(record, spec)
    if violations:
        print(json.dumps({"guard": "IDENTITY_GUARD_FAILED", "exit": EXIT_IDENTITY_GUARD,
                          "violations": violations}, ensure_ascii=False, indent=1),
              file=sys.stderr)
        return EXIT_IDENTITY_GUARD
    if args.audit_only:
        result = derive_key(record, spec)
        print(json.dumps({"guard": "IDENTITY_GUARD_PASSED", "groups": REQUIRED_GROUPS,
                          "presence_required_groups": list(PRESENCE_REQUIRED_GROUPS),
                          "fields": spec["fields"], "required_fields": declared_required(spec),
                          "axes_participating": result["derivation"]["axes_participating"],
                          "absent_optional_fields": result["derivation"]["absent_optional_fields"],
                          "identity_digest": result["identity_digest"]},
                         ensure_ascii=False))
        return EXIT_OK

    try:
        result = checked_derive(record, spec)
    except IdentityGuardViolation as exc:      # unreachable while audit_derivation gates first
        print(json.dumps({"guard": "IDENTITY_GUARD_FAILED", "violations": exc.violations},
                         ensure_ascii=False), file=sys.stderr)
        return EXIT_IDENTITY_GUARD
    payload = json.dumps(result, ensure_ascii=False, sort_keys=True)
    if args.out:
        try:
            write_derived_report(args.out, payload)
        except OSError as exc:
            print(f"output error: {exc}", file=sys.stderr)
            return EXIT_OUTPUT_ERROR
    if not args.quiet:
        print(payload)
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
