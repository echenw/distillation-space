"""Safety kernel: provenance identity, source classification, self-generated exclusion,
cohort identity, independent-support semantics, schema validation, append-only ledger.

Wave 0 scope only. Stdlib, deterministic, no model client import.

Contract: S02 (source identity) / S03 (provenance) / S04 (schema validation) /
S19-support semantics. Round 2 CORE clusters: CM-01 CM-04 CM-08 CM-11 CM-24 CM-25 CM-32
CM-47 CM-49 CM-50 (partial, contractual representation in CORE-IMPLEMENTATION-MAP.md).

Generated output is never independent evidence (12-SKILL-DESIGN-BRIEF.md sec 30).
"""
from __future__ import annotations

import hashlib
import json
import os
import re

SCHEMA_VERSION = "1"

# ------------------------------------------------------------------ source classes
EXTERNAL_EVENT = "external_event"          # a real bug, failing test, review, command failure
HUMAN_INPUT = "human_input"                # explicit human correction / instruction
COMPILER_ARTIFACT = "compiler_artifact"  # our own rule / skill / pattern summary
MODEL_OUTPUT = "model_output"              # M1-M4 proposals and summaries
RESTATED_KNOWLEDGE = "restated_knowledge"  # re-presentation of an existing active artifact

INDEPENDENT_CLASSES = frozenset({EXTERNAL_EVENT, HUMAN_INPUT})
DERIVED_CLASSES = frozenset({COMPILER_ARTIFACT, MODEL_OUTPUT, RESTATED_KNOWLEDGE})

ARTIFACT_RECORD_TYPES = frozenset({
    "rule", "skill", "eval", "test", "lint", "script",
    "proposal", "pattern_summary", "artifact_restatement", "candidate",
})


class SchemaError(Exception):
    pass


class AmbiguousOrigin(Exception):
    """Raised when a record cannot be classified. Fail closed: unknown origin is never
    treated as independent support (10-PROVENANCE-MODEL.md: unverified != verified)."""


# ------------------------------------------------------------------ canonical form & identity
def canonical_bytes(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def content_hash(payload: dict) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def cohort_key(scope: dict) -> str:
    """Deterministic cohort identity. Round 2 flagged `02` for computing cohort_key and
    never consuming it; here every consumer of support counts goes through this function,
    and cross-cohort aggregation is explicit (S19 mutation target #2)."""
    for k in ("workspace", "project"):
        if not isinstance(scope.get(k), str) or not scope[k].strip():
            raise AmbiguousOrigin(f"cohort scope missing {k!r}: {scope}")
    path = scope.get("path", "")
    return f"{scope['workspace']}::{scope['project']}::{path}"


# ------------------------------------------------------------------ schema validation (S04)
REQUIRED_EVIDENCE = ("evidence_id", "source_class", "locator", "cohort", "content", "produced_by")
EVIDENCE_ENUMS = {"source_class": set(INDEPENDENT_CLASSES | DERIVED_CLASSES)}


def validate_evidence(rec: dict) -> list:
    """Return a list of violations. Empty list means the record is well-formed."""
    v = []
    for f in REQUIRED_EVIDENCE:
        if f not in rec:
            v.append(f"missing required field {f!r}")
    for f, allowed in EVIDENCE_ENUMS.items():
        if f in rec and rec[f] not in allowed:
            v.append(f"field {f}={rec[f]!r} not in enum {sorted(allowed)}")
    if rec.get("schema_version", SCHEMA_VERSION) != SCHEMA_VERSION:
        v.append(f"unsupported schema_version {rec.get('schema_version')!r}")
    loc = rec.get("locator")
    if isinstance(loc, str) and not re.match(r"^[a-z][a-z0-9+.-]*:", loc) and not os.path.sep in loc:
        v.append(f"locator not resolvable: {loc!r}")
    return v


# ------------------------------------------------------------------ self-generated exclusion
# THE guard. S19's mutation harness flips exactly this constant off to prove the test bites.
SELF_GENERATED_EXCLUSION_ENABLED = True

ARTIFACT_STORE_MARKER = "store/"


def is_self_generated(rec: dict, artifact_root: str = "store") -> bool:
    """True when this record originates from the compiler's own outputs or from a model,
    rather than from a new external event or explicit human input.

    Four exclusion checks; any match excludes the record. Source classes outside
    the independent allowlist are also excluded by default (fail closed).
    This defence in depth follows 11-FAILURE-MODES RT-02/RT-05/RT-13.
    """
    if not SELF_GENERATED_EXCLUSION_ENABLED:
        return False  # MUTATION SWITCH -- see .distill/round-3/wave-0/

    # Exclusion check 1: derived source class
    cls = rec.get("source_class")
    if cls in DERIVED_CLASSES:
        return True

    # Exclusion check 2: only known external observation producers can support
    # independent evidence. An unknown or prior-version producer must not bypass
    # the self-generated filter after the compiler identity changes.
    produced = rec.get("produced_by") or {}
    independent_producers = {"external_event", "external_system", "human", "worker", "ci", "runner"}
    if produced.get("kind") not in independent_producers:
        return True

    # Exclusion check 3: locator is inside the authoritative artifact store
    loc = str(rec.get("locator", ""))
    store_prefix = artifact_root.rstrip("/") + "/"
    if loc.startswith(store_prefix) or ARTIFACT_STORE_MARKER.rstrip("/") in loc.split("/"):
        return True

    # Exclusion check 4: explicitly identified as an artifact record
    if rec.get("record_type") in ARTIFACT_RECORD_TYPES:
        return True

    return cls not in INDEPENDENT_CLASSES


def is_independent(rec: dict, artifact_root: str = "store") -> bool:
    """Independent support requires ALL of: external/human class, a resolvable locator,
    a complete cohort, not self-generated, and a clean schema."""
    if validate_evidence(rec):
        return False
    if is_self_generated(rec, artifact_root):
        return False
    if not str(rec.get("locator", "")).strip():
        return False
    try:
        cohort_key(rec.get("cohort") or {})
    except AmbiguousOrigin:
        return False
    return True


# ------------------------------------------------------------------ independent-support semantics
def independent_support(evidence: list, artifact_root: str = "store") -> dict:
    """Count DISTINCT cohorts and DISTINCT content hashes among independent evidence only.

    Deliberately NOT a raw event count: repeats of the same external event must not inflate
    support (dedup by content_hash), and self-generated items must never enter either number.
    """
    cohorts, hashes, excluded = set(), set(), []
    for rec in evidence:
        if is_independent(rec, artifact_root):
            cohorts.add(cohort_key(rec["cohort"]))
            hashes.add(rec.get("content_hash") or content_hash(rec.get("content", {})))
        else:
            excluded.append({
                "evidence_id": rec.get("evidence_id"),
                "reason": "self_generated" if is_self_generated(rec, artifact_root)
                          else "schema_or_provenance_invalid",
            })
    return {
        "independent_cohorts": sorted(cohorts),
        "independent_cohort_count": len(cohorts),
        "distinct_evidence_count": len(hashes),
        "excluded": excluded,
    }


# ------------------------------------------------------------------ ledger (append-only)
def append_ledger(path: str, event: dict) -> None:
    """The ledger is append-only and records exclusions too, so a silent drop of self-generated
    evidence is auditable rather than invisible (06:run-account-anti-silence)."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"content_hash": content_hash(event), **event},
                            ensure_ascii=False, sort_keys=True) + "\n")
