#!/usr/bin/env python3
"""S13 kd_provenance_stamp -- write-time provenance stamping, produced by the system.

Contract (.distill/round-3/wave-1/_dispatch/w1c.json):
    inputs  : 提案 + 运行环境事实
    outputs : `generation{round_id,pass_id,compiler_version,model_id,config_sha,created_at}`
              、`actor`
    exit    : 2=由被记录对象自填出处；已有盖戳被覆盖即 2

Round 2 basis (pack-c.md and the two docs it quotes):
  * `05-DATA-MODEL.md:46` -- `provenance.actor` 由写入网关/装配层写，**不由被记录对象自报**；
    缺省 fail-closed；归属变更只有人类 adopt 路径可改。
  * `05-DATA-MODEL.md:47` -- `generation{...}` 由装配层写盘时盖戳，**Worker 不可自填**；
    **不可变**；任何改写产生新条目并由 `lifecycle_event` 链接。
  * `10-PROVENANCE-MODEL.md` §3 -- 出处记录不得放在被记录对象自己手里；provenance 写时一次
    盖戳、不可覆盖（`importOrigin` 证明必须写时盖戳且绝不覆盖，事后补会被派生记录覆盖）。
  * `10-PROVENANCE-MODEL.md` §1.2 -- 归属是声明的，永不从活跃度推断.

This module writes nothing (S12 owns every store write). Its CLI prints the stamped block
on stdout so the caller can hand it to `kd_write_txn`.
The additional pure `provenance_record` API assembles all SC06 fields from S12's
validated source evidence, final Artifact and allocated SC07 event. S12 persists
that full record in immutable transaction history, never in the proposal body.

Stdlib only. Provenance identity helpers come from the Wave 0 kernel `kd_provenance`; they
are called, never copied.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import kd_provenance as prov          # noqa: E402  (Wave 0 kernel, read-only reuse)
import kd_validate as validator       # noqa: E402  SC01/SC06 are the runtime contracts

EXIT_OK = 0
EXIT_SELF_DECLARED_OR_OVERWRITE = 2    # contractual exit 2
EXIT_INVALID_INPUTS = 3
EXIT_UNVERIFIABLE = 4                  # --verify on a record carrying no stamp digest

GENERATION_FIELDS = ("round_id", "pass_id", "compiler_version", "model_id",
                     "config_sha", "created_at")

# Keys whose presence in a *proposal payload* means the recorded object tried to fill in its
# own provenance. `05` §2 rows 5-8 and 11 assign every one of these to a system writer
# (assembly layer / eval runner / auditor), so a payload carrying them is not a gap -- it is
# the exact failure mode.
SELF_DECLARED_KEYS = ("provenance", "generation", "actor", "stamp_digest",
                      "verification", "status_basis", "refs_integrity")

ACTORS = ("human", "curator", "import", "shared")
SCOPE_LAYERS = ("project", "global", "cohort")     # 05 §5.3: layer ∈ {project, global, cohort}
AGENT_ACTOR_RE = re.compile(r"^agent:[A-Za-z0-9._-]+$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")

# Bookkeeping S12 attaches at commit time. The subject digest deliberately excludes them so
# the stamp stays verifiable after the write instead of describing a payload that can never
# be reconstructed (05 §2 row 6: 不可变).
TRANSACTION_FIELDS = ("state", "revision", "decision_digest", "written_by", "refs_integrity")


class ProvenanceViolation(Exception):
    """Mapped to exit 2: the stamp would be self-declared or would overwrite a stamp."""


class InvalidFacts(Exception):
    """Mapped to exit 3: runtime facts or scope are missing/incomplete (fail-closed)."""


# --------------------------------------------------------------------- runtime facts
class RuntimeFacts:
    """Trusted inputs of the stamp, held by the assembly layer, never by the proposal."""

    def __init__(self, *, round_id, pass_id, compiler_version, config_sha, actor,
                 model_id=None, created_at=None):
        self.round_id = _required("round_id", round_id)
        self.pass_id = _required("pass_id", pass_id)
        self.compiler_version = _required("compiler_version", compiler_version)
        self.config_sha = _sha("config_sha", config_sha)
        self.actor = _actor(actor)
        # model_id is legitimately absent on the zero-LLM path (`12` §16 item 6 forbids a
        # guessed value there), so None stays None -- it is never filled with a placeholder.
        self.model_id = model_id if model_id is None else _required("model_id", model_id)
        self.created_at = created_at or datetime.now(timezone.utc).isoformat(timespec="seconds")

    def generation(self) -> dict:
        return {
            "round_id": self.round_id,
            "pass_id": self.pass_id,
            "compiler_version": self.compiler_version,
            "model_id": self.model_id,
            "config_sha": self.config_sha,
            "created_at": self.created_at,
        }


def _required(name, value):
    if not isinstance(value, str) or not value.strip():
        raise InvalidFacts(f"runtime fact {name!r} is missing; the stamp fails closed rather "
                           f"than writing an unattributable record")
    return value.strip()


def _sha(name, value):
    value = _required(name, value)
    if not SHA_RE.match(value):
        raise InvalidFacts(f"{name} must be a 64-hex sha256, got {value!r}")
    return value


def _actor(value):
    value = _required("actor", value)
    if value in ACTORS or AGENT_ACTOR_RE.match(value):
        return value
    raise InvalidFacts(f"actor {value!r} not in {ACTORS} or agent:<name>")


# --------------------------------------------------------------------- self-declaration check
def find_self_declared(payload) -> list:
    """Any provenance-bearing key already present in the payload means the object tried to
    fill in its own 出处. Detected recursively because proposals nest (a `learning` may carry
    `origin`, and a `pattern` may carry child proposals)."""
    hits = []
    if isinstance(payload, dict):
        for key, value in payload.items():
            if key in SELF_DECLARED_KEYS:
                hits.append(key)
            hits.extend(find_self_declared(value))
    elif isinstance(payload, list):
        for item in payload:
            hits.extend(find_self_declared(item))
    return sorted(set(hits))


def _origin_view(proposal: dict) -> dict:
    """Project a proposal onto the kernel's evidence vocabulary so `is_self_generated` -- not
    a re-implementation -- classifies its origin."""
    return {
        "source_class": proposal.get("source_class") or "model_output",
        "produced_by": proposal.get("produced_by") or {},
        "locator": proposal.get("locator") or "",
        "record_type": proposal.get("record_type") or "proposal",
    }


def subject_digest(proposal: dict) -> str:
    """sha256 over the proposal with provenance-bearing and transaction-bookkeeping keys
    stripped. `record_locator` is kept: it is a pointer written by the ledger owner, and
    stripping it would let a re-located record keep an identical digest.
    """
    drop = set(SELF_DECLARED_KEYS) | set(TRANSACTION_FIELDS)
    body = {k: v for k, v in proposal.items() if k not in drop}
    return prov.content_hash(body)


# --------------------------------------------------------------------- the stamp
def stamp(proposal: dict, facts: RuntimeFacts, *, existing: dict | None = None) -> dict:
    """Return a NEW proposal dict carrying a system-produced provenance block.

    Raises ProvenanceViolation (exit 2) when:
      * the payload already carries any provenance-bearing key (self-declared 出处);
      * `existing` already carries a stamp and the new one is not byte-identical (overwrite);
    Raises InvalidFacts (exit 3) when runtime facts or the cohort scope are incomplete.
    """
    if not isinstance(proposal, dict):
        raise InvalidFacts(f"proposal must be an object, got {type(proposal).__name__}")

    hits = find_self_declared(proposal)
    if hits:
        raise ProvenanceViolation(
            f"self-declared provenance: payload already carries {hits}. Provenance is "
            "produced by kd_provenance_stamp from runtime facts and written once by kd_write_txn "
            "(05-DATA-MODEL.md:46-47, 10-PROVENANCE-MODEL.md §3).")

    # scope/cohort fail-closed (05 §5.3 S1) -- cohort identity is *consumed* here, not merely
    # modelled: an artifact with an incomplete cohort cannot be attributed to a round at all.
    scope = proposal.get("scope") or {}
    if scope.get("layer") not in SCOPE_LAYERS:
        raise InvalidFacts(f"proposal scope.layer={scope.get('layer')!r} is not one of "
                           f"{SCOPE_LAYERS}: 05 §5.3 S1 forbids defaulting a missing scope to "
                           "global, so an artifact without a resolved layer cannot be stamped")
    try:
        prov.cohort_key({"workspace": scope.get("workspace"),
                         "project": scope.get("project"),
                         # 05 §5.3 gives an artifact scope {workspace, project, layer}; the
                         # kernel cohort triple is {workspace, project, path}, so the third
                         # discriminator consumed here is the artifact's layer.
                         "path": scope.get("layer")})
    except prov.AmbiguousOrigin as exc:
        raise InvalidFacts(f"proposal scope cohort is incomplete, refusing to stamp: {exc}")

    # attribution laundering guard (10 §1.2, CM-35): a self-generated payload may not be
    # stamped as human-authored. Classification is delegated to the kernel guard.
    if facts.actor == "human" and prov.is_self_generated(_origin_view(proposal)):
        raise ProvenanceViolation(
            "actor=human requested for a self-generated payload: 归属是声明的，永不从活跃度"
            "推断；human attribution requires the adopt path (CM-35).")

    block = {
        "generation": facts.generation(),
        "actor": facts.actor,
        "subject_digest": subject_digest(proposal),
    }
    block["stamp_digest"] = stamp_digest(block)

    if existing is not None:
        prior = (existing.get("provenance") or {})
        if prior.get("generation") or prior.get("stamp_digest"):
            if prior.get("stamp_digest") != block["stamp_digest"]:
                raise ProvenanceViolation(
                    "stamp overwrite refused: the record already carries "
                    f"stamp_digest={prior.get('stamp_digest')!r}; immutability means a new "
                    "entry linked by lifecycle_event, never a rewritten stamp "
                    "(05-DATA-MODEL.md:47).")

    stamped = dict(proposal)
    stamped["provenance"] = block
    return stamped


def stamp_digest(block: dict) -> str:
    """Binding digest over the stamp.

    IMPLEMENTATION_GAP: Round 2 adjudicates *immutability* and *who writes*, not a keyed MAC
    or a key-management design, so this is an integrity binding (detects an after-the-fact
    edit of the body's provenance block), not a cryptographic authority. No secret is
    invented here. / DEFERRED id DD-7-sub49 (provenance trust strength beyond the adjudicated
    ladder) -- the digest must not be read as a signing mechanism.
    """
    body = {k: v for k, v in block.items() if k != "stamp_digest"}
    return prov.content_hash(body)


def verify(record: dict) -> tuple[bool, str]:
    """Recompute the binding digest of an already-stamped record."""
    block = record.get("provenance")
    if not isinstance(block, dict) or not block.get("stamp_digest"):
        return False, "UNVERIFIABLE: record carries no provenance stamp"
    expected = stamp_digest(block)
    if expected != block["stamp_digest"]:
        return False, ("SELF_DECLARED_OR_EDITED: provenance block was filled in or rewritten "
                       f"by someone other than kd_provenance_stamp (stored "
                       f"{block['stamp_digest'][:12]}..., recomputed {expected[:12]}...)")
    missing = [f for f in GENERATION_FIELDS if f not in block.get("generation", {})]
    if missing:
        return False, f"INCOMPLETE_GENERATION: missing {missing}"
    if "actor" not in block:
        return False, "INCOMPLETE_ACTOR: provenance.actor missing (fail-closed)"
    if subject_digest(record) != block.get("subject_digest"):
        return False, ("SELF_DECLARED_OR_EDITED: the subject changed after stamping, so this "
                       "body is not the body the stamp was produced for")
    return True, "OK"


def provenance_record(record: dict, evidence: list, event: dict) -> dict:
    """Pure SC06 producer, held by S12's immutable transaction history, not the body.

    S12 supplies the final artifact, independently observed SC01 rows and the allocated
    SC07 event after replaying all gates. This function does not authenticate inputs or
    grant write authority. A candidate cannot provide or overwrite any part of SC06.
    """
    ok, _ = verify(record)
    if not ok or not isinstance(evidence, list) or not evidence:
        raise InvalidFacts("SC06 requires a system stamp and nonempty observed evidence")
    sources = {}
    for row in evidence:
        if not validator.validate_artifact("evidence", row).get("valid") \
                or row.get("scope") != record.get("scope") or not prov.is_independent(row) \
                or row.get("content_hash") != prov.content_hash(row["content"]):
            raise InvalidFacts("SC06 source must be complete, independent and bound to the exact Scope/content")
        eid = row["evidence_id"]
        if eid in sources and sources[eid] != row:
            raise InvalidFacts("SC06 source ID cannot identify conflicting evidence")
        sources[eid] = row
    origins = [sources[eid]["origin"] for eid in sorted(sources)]
    refs = {prov.content_hash(ref): ref for origin in origins for ref in origin["source_refs"]}
    verification = record.get("verification") or []
    if not verification or verification[-1].get("verdict") != "PASSED" \
            or verification[-1].get("artifact_sha") != record["content_hash"] \
            or (record.get("refs_integrity") or {}).get("status") != "PASS":
        raise InvalidFacts("SC06 requires a fresh body-bound PASSED run and successful S14 audit")
    if not validator.validate_artifact("lifecycle-event-ledger", event).get("valid") \
            or event.get("entity") != "artifact" or event.get("entity_id") != record.get("artifact_id"):
        raise InvalidFacts("SC06 requires the allocated event for this artifact")
    latest = verification[-1]
    block = record["provenance"]
    result = {
        "origin": {"problem": "\n".join(sorted({origin["problem"] for origin in origins})),
                   "why": "\n".join(sorted({origin["why"] for origin in origins})),
                   "source_refs": [copy.deepcopy(refs[key]) for key in sorted(refs)]},
        "evidence_refs": copy.deepcopy(record["evidence_refs"]),
        "evidence": {"status": "VERIFIED", "status_basis": {
            "run_id": latest["eval_id"], "run_at": latest["run_at"], "artifact_sha": latest["artifact_sha"]}},
        "actor": block["actor"], "generation": copy.deepcopy(block["generation"]),
        "verification": copy.deepcopy(verification),
        "lifecycle_event": [{key: event[key] for key in (
            "at", "op", "actor", "reason", "supersedes", "superseded_by")}],
        "derived_from": [{"entity": "evidence", "entity_id": eid} for eid in sorted(sources)],
        "record_locator": copy.deepcopy(event["record_locator"]),
        "refs_integrity": copy.deepcopy(record["refs_integrity"]),
    }
    if not validator.validate_artifact("provenance-record", result).get("valid"):
        raise InvalidFacts("SC06 minimum provenance fields are incomplete or invalid")
    return result


# --------------------------------------------------------------------- CLI
def _load(path: str):
    if path == "-":
        return json.load(sys.stdin)
    with open(path, encoding="utf-8") as fh:                # read-only
        return json.load(fh)



class UsageError(Exception):
    """A CLI usage error. argparse exits with code 2 by design, and 2 is a contract code in
    this package (second write path / self-declared provenance / unresolved ref), so usage
    errors must never be able to impersonate one."""


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        print(f"invalid input: {message}", file=sys.stderr)
        raise UsageError(message)

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    ap = ArgumentParser(
        prog="kd_provenance_stamp.py",
        description="S13: produce the write-time provenance stamp from runtime facts. "
                    "Never writes; the stamped block goes to stdout for kd_write_txn.")
    ap.add_argument("--proposal", metavar="FILE or -",
                    help="proposal JSON to stamp (self-declared provenance -> exit 2)")
    ap.add_argument("--existing", metavar="FILE",
                    help="current stored record; a differing second stamp -> exit 2")
    ap.add_argument("--verify", metavar="FILE",
                    help="verify an already-stamped record instead of stamping")
    ap.add_argument("--round-id")
    ap.add_argument("--pass-id")
    ap.add_argument("--compiler-version")
    ap.add_argument("--config-sha")
    ap.add_argument("--actor", help="human | curator | import | shared | agent:<name>")
    ap.add_argument("--model-id", default=None,
                    help="omit on the zero-LLM path; never guessed")
    ap.add_argument("--created-at", default=None)
    try:
        args = ap.parse_args(argv)
    except UsageError:
        return EXIT_INVALID_INPUTS

    if args.verify:
        try:
            record = _load(args.verify)
        except (OSError, ValueError) as exc:
            print(f"invalid input: {exc}", file=sys.stderr)
            return EXIT_INVALID_INPUTS
        ok, why = verify(record)
        print(why)
        return EXIT_OK if ok else (EXIT_UNVERIFIABLE if why.startswith("UNVERIFIABLE")
                                   else EXIT_SELF_DECLARED_OR_OVERWRITE)

    missing = [n for n, v in (("--round-id", args.round_id), ("--pass-id", args.pass_id),
                             ("--compiler-version", args.compiler_version),
                             ("--config-sha", args.config_sha), ("--actor", args.actor))
               if not v]
    if args.proposal is None or missing:
        ap.print_usage(sys.stderr)
        print("invalid input: " + ("--proposal is required; " if args.proposal is None else "")
              + (f"missing runtime facts: {missing}" if missing else ""), file=sys.stderr)
        return EXIT_INVALID_INPUTS

    try:
        proposal = _load(args.proposal)
        existing = _load(args.existing) if args.existing else None
    except (OSError, ValueError) as exc:
        print(f"invalid input: {exc}", file=sys.stderr)
        return EXIT_INVALID_INPUTS

    try:
        facts = RuntimeFacts(round_id=args.round_id, pass_id=args.pass_id,
                             compiler_version=args.compiler_version,
                             config_sha=args.config_sha, actor=args.actor,
                             model_id=args.model_id, created_at=args.created_at)
        stamped = stamp(proposal, facts, existing=existing)
    except ProvenanceViolation as exc:
        print(f"PROVENANCE_VIOLATION: {exc}", file=sys.stderr)
        return EXIT_SELF_DECLARED_OR_OVERWRITE
    except InvalidFacts as exc:
        print(f"INVALID_INPUTS: {exc}", file=sys.stderr)
        return EXIT_INVALID_INPUTS

    json.dump(stamped, sys.stdout, ensure_ascii=False, sort_keys=True)
    sys.stdout.write("\n")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
