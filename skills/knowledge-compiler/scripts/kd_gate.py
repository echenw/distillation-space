"""Safety kernel: provisional promotion evaluation and the UNIQUE mutation path.

Wave 0 scope only for the mutation boundary. Wave 3 (S10) extended this file without touching its
public API: the counting arithmetic now lives in `kd_gate_tree` (the 38-node / 86-branch
adjudicated tree of 06-PROMOTION-POLICY.md), so there is one source for the numbers and one for
the decision shape. `evaluate_promotion` keeps returning the same keys with the same meaning,
because `kd_write_txn.commit_batch` re-runs it and Wave 0's mutation proof depends on it.

The numeric threshold here is a PROVISIONAL default carried in an
external config file, because the promotion-threshold subparameters are among the 52
DEFERRED entries in .distill/round-3/DEFERRED-PARAMETERS.yaml (DD-1 group).

Two surfaces, and the difference is stated rather than hidden:
  * `evaluate_promotion(evidence, cfg, artifact_root)` -- Stage 1's counting nodes N14/N15 only,
    which is NOT a whole-tree decision (`full_adjudication: false` says so on the record);
  * `adjudicate(candidate, cfg, artifact_root)` -- the whole tree for ONE candidate (CM-27), which
    refuses at N16/N17 while their thresholds are undecided and calls S07's
    `assert_not_promotion_payload` on every promotion-shaped payload it emits.

Nothing in this module may be cited as an evidence-backed constant.
"""
from __future__ import annotations

import json
import math
import os

import kd_provenance as prov

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(HERE, os.pardir, "references", "promotion-config.json")
MAX_POLICY_BYTES = 256 * 1024  # resource bound for a small explicit policy document


def load_config(path: str = CONFIG_PATH) -> dict:
    with open(path, encoding="utf-8") as fh:
        cfg = json.load(fh)
    if cfg.get("status") != "provisional":
        raise prov.SchemaError("promotion config must be marked status=provisional in Wave 0")
    return cfg["thresholds"]


def runtime_thresholds(policy: dict) -> dict:
    """Single shape contract for explicit admitted runtime policy; grants no approval."""
    if not isinstance(policy, dict) or policy.get("status") != "admitted" \
            or not isinstance(policy.get("decision_id"), str) or not policy["decision_id"].strip():
        raise prov.SchemaError("POLICY_NOT_ADMITTED")
    cfg = policy.get("thresholds")
    minimums = {"min_independent_cohorts": 1, "min_distinct_evidence": 1,
                "min_distinct_tasks": 1, "min_tasks_not_this_session": 0}
    if not isinstance(cfg, dict) or any(type(cfg.get(k)) is not int or cfg[k] < v
                                       for k, v in minimums.items()):
        raise prov.SchemaError("POLICY_MALFORMED")
    for key, minimum in (("min_interval_hours", 0), ("pending_ttl_hours", 0)):
        value = cfg.get(key)
        if type(value) not in (int, float) or (type(value) is float and not math.isfinite(value)) or value < minimum \
                or (key == "pending_ttl_hours" and value == 0):
            raise prov.SchemaError("POLICY_MALFORMED")
    return cfg


def read_runtime_policy(path: str) -> dict:
    """Read a caller-selected policy. A policy label is not a trusted G1/S12 receipt."""
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise prov.SchemaError("POLICY_MALFORMED")
            result[key] = value
        return result

    def invalid_constant(value):
        raise prov.SchemaError("POLICY_MALFORMED")

    def finite_float(value):
        parsed = float(value)
        if not math.isfinite(parsed):
            raise prov.SchemaError("POLICY_MALFORMED")
        return parsed

    try:
        with open(path, "rb") as handle:
            raw = handle.read(MAX_POLICY_BYTES + 1)
        if len(raw) > MAX_POLICY_BYTES:
            raise prov.SchemaError("POLICY_INPUT_TOO_LARGE")
        policy = json.loads(raw.decode("utf-8"), object_pairs_hook=unique,
                            parse_constant=invalid_constant, parse_float=finite_float)
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        raise prov.SchemaError("POLICY_UNREADABLE_OR_INVALID") from exc
    runtime_thresholds(policy)
    return policy


def load_runtime_policy(path: str) -> dict:
    return read_runtime_policy(path)["thresholds"]


def evaluate_promotion(evidence: list, cfg: dict = None, artifact_root: str = "store") -> dict:
    """Decide whether an accumulated candidate set clears the gate.

    Consumption rule (Round 2 RT-05: cohort was 'modelled but not consumed'): the gate
    reads ONLY independent cohorts, and cohort identity is mandatory -- an evidence item
    with an incomplete cohort is rejected, never silently aggregated into a global bucket.

    Delegates to kd_gate_tree.evaluate_counting -- nodes N14 and N15 reading their thresholds out
    of the single constants file. The five Wave 0 keys keep their names, types and meaning.
    """
    import kd_gate_tree as tree
    return tree.evaluate_counting(evidence, load_config() if cfg is None else cfg, artifact_root)


def adjudicate(candidate: dict, cfg: dict = None, artifact_root: str = "store", *,
               approval_context: dict = None, eval_verdict: dict = None) -> dict:
    """THE S10 surface: walk the full tree for ONE candidate and return its per-item verdict.

    RH-P0-05/06: `approval_context` (G1) and `eval_verdict` (S16) are the ONLY trusted channels
    for the human decision and the eval; the untrusted `candidate` cannot supply them (any such
    field it carries is stripped and ignored by kd_gate_tree.adjudicate).

    Exit codes follow S10's contract row: 3 = not promoted (a normal terminal state), 2 = the
    thresholds and the policy are not same-source, or Stage 0 was skipped / refused.
    """
    import kd_gate_tree as tree
    return tree.adjudicate(candidate, load_config() if cfg is None else cfg, artifact_root,
                           approval_context=approval_context, eval_verdict=eval_verdict)


# ----------------------------------------------------------------- unique mutation path
class WritePathViolation(Exception):
    """Any attempt to change authoritative state outside the single boundary."""


def legal_transitions() -> dict:
    """Legal state edges belong to S17 (`07-LIFECYCLE-POLICY.md` §1), not to this module.

    Wave 0 carried its own copy here and it drifted: it materialised `stale`, which `07:32`
    §1.1 rules to be a read-only derived view that must never become authoritative, it allowed
    `superseded -> active` and `superseded -> archived`, neither of which `07` adjudicates, and
    it had no `failed` state although `07:26` requires failed and rejected to stay separate.
    Consulting the Owner removes the second authority; a missing Owner fails closed rather
    than falling back to a permissive table.
    """
    import kd_lifecycle as lifecycle        # noqa: WPS433 (the Owner is resolved at call time)
    allowed: dict = {}
    for frm, to in lifecycle.TRANSITIONS:
        allowed.setdefault(frm, set()).add(to)
    return allowed


def apply_mutation(store: dict, mutation: dict, decision: dict) -> dict:
    """THE authoritative mutation boundary. Everything else produces proposals.

    Wave 0 enforces the two properties S19 depends on:
      1. a durable write requires decision.promotable == True (gate sits on this path);
      2. a model/proposal payload has no write authority of its own.
    """
    if mutation.get("produced_by") == "model" and not decision.get("human_approved"):
        raise WritePathViolation("model output has proposal rights only, never write rights")
    if not decision.get("promotable"):
        raise WritePathViolation(f"gate closed: {decision.get('reason')}")

    to = mutation["to_state"]
    frm = mutation.get("from_state", "candidate")
    # checked first so the ceiling stays the named reason even though `deleted` is also not a
    # legal state: an archive-or-nothing ceiling must never be reported as a generic typo
    if to in ("deleted", "hard-deleted", "purged"):
        raise WritePathViolation(
            f"physical delete is not reachable from this path: {to!r} is not a storage state, "
            f"archive is the destructive ceiling (07-LIFECYCLE-POLICY.md)")
    if to not in legal_transitions().get(frm, set()):
        raise WritePathViolation(f"illegal transition {frm} -> {to}")

    aid = mutation["artifact_id"]
    prev = store.get(aid)
    store[aid] = {
        "artifact_id": aid,
        "state": to,
        "revision": (prev or {}).get("revision", 0) + 1,
        "decision_digest": decision.get("digest", ""),
        "support": decision.get("support", {}).get("independent_cohorts", []),
    }
    return store[aid]
