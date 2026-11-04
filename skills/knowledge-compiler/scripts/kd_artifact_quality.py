#!/usr/bin/env python3
"""GQ1–GQ5: read-only evidence-binding preflight for a finished Skill bundle.

Checks frozen requirement/claim IDs, actual shipped implementations, cited
document anchors, cross-Skill interface fields, applicability counterexamples,
and real-task observation files. It cannot judge semantic truth or authenticate
a reviewer or host. Passing this preflight is never an installation or GO grant.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

import kd_material_quality as quality
import kd_skill_metadata as metadata

ID = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,63}$")
SHA = re.compile(r"^[0-9a-f]{64}$")
CASE_KINDS = {"positive", "missing", "conflict", "boundary"}
DECISIONS = {"pass", "fail", "not_proven"}
# Detect candidate entrypoint promises worth independent implementation review.
AUTO_PROMISE = re.compile(
    r"(?:确定性|自动)[^\n]{0,16}(?:引擎|校验|检查)|"
    r"(?:Schema|schema)[^\n]{0,10}(?:校验|验证)|"
    r"指纹[^\n]{0,10}(?:锁定|引擎|校验)"
)


def require(cond: bool, error: str):
    quality.require(cond, error)


def mapping(value, error: str) -> dict:
    return quality.obj(value, error)


def rows(obj: dict, field: str, *, minimum: int = 1) -> dict:
    data = quality.items(obj.get(field), "GQ_" + field.upper() + "_MISSING")
    require(len(data) >= minimum, "GQ_" + field.upper() + "_EMPTY")
    result = {}
    for item in data:
        mapping(item, "GQ_ROW_INVALID")
        value = item.get("id")
        require(type(value) is str and ID.fullmatch(value) and value not in result,
                "GQ_ID_INVALID_OR_DUPLICATE")
        result[value] = item
    return result


def check_text(value, error: str) -> str:
    require(type(value) is str and bool(value.strip()) and len(value) <= 4000, error)
    return value


def check_sha(value, error: str):
    require(type(value) is str and bool(SHA.fullmatch(value)), error)


def check_ids(expected: dict, actual: dict, field: str):
    require(set(expected) == set(actual), "GQ_" + field.upper() + "_COVERAGE_MISMATCH")


def reference(root: Path, value, *, read: bool = True) -> str:
    """Bind a quoted anchor to a real file under one selected Skill root."""
    obj = mapping(value, "GQ_REFERENCE_INVALID")
    path = check_text(obj.get("path"), "GQ_REFERENCE_PATH_INVALID")
    anchor = check_text(obj.get("anchor"), "GQ_REFERENCE_ANCHOR_MISSING")
    file = quality.local(root, path)
    raw = quality.read_data(file, quality.MAX_TEXT)
    if read:
        try:
            decoded = raw.decode("utf-8")
        except UnicodeError as exc:
            raise quality.Invalid("GQ_REFERENCE_ENCODING_INVALID") from exc
        require(anchor in decoded, "GQ_REFERENCE_ANCHOR_NOT_FOUND")
        return decoded
    return ""


def observed_file(root: Path, value):
    """Verify an immutable-looking observation's actual bytes (not its truth)."""
    obj = mapping(value, "GQ_OBSERVATION_MISSING")
    path = check_text(obj.get("path"), "GQ_OBSERVATION_PATH_INVALID")
    digest = obj.get("sha256")
    check_sha(digest, "GQ_OBSERVATION_DIGEST_INVALID")
    file = quality.local(root, path)
    require(quality.sha(quality.read_data(file)) == digest, "GQ_OBSERVATION_DRIFT")


def status(value, report: dict, name: str):
    require(value in DECISIONS and type(value) is str, "GQ_DECISION_INVALID")
    if value == "fail":
        report["blocking"].append(name)
    elif value == "not_proven":
        report["unverified"].append(name)


def inspect(skill: Path, brief_path: Path, review_path: Path,
            evidence_root: Path, peers_root: Path | None = None) -> dict:
    # Reuse existing strict JSON, shared frontmatter subset and whole-tree hashing.
    structure = quality.skill_audit(skill, "generic")
    for record in (brief_path, review_path, evidence_root):
        require(not record.resolve().is_relative_to(skill.resolve()), "GQ_EVIDENCE_IN_SKILL")
    forbidden = quality.final_provenance_errors(skill)
    if forbidden:
        raise quality.Invalid(forbidden[0])
    require(evidence_root.is_dir() and not evidence_root.is_symlink(),
            "GQ_EVIDENCE_ROOT_INVALID")
    brief_raw = quality.read_data(brief_path)
    brief = mapping(quality.parse_json(brief_raw), "GQ_BRIEF_INVALID")
    review = mapping(quality.read_json(review_path), "GQ_REVIEW_INVALID")
    require(type(brief.get("version")) is int and brief["version"] == 1 and
            type(review.get("version")) is int and review["version"] == 1,
            "GQ_VERSION_INVALID")
    require(review.get("brief_sha256") == quality.sha(brief_raw),
            "GQ_BRIEF_CHANGED")
    require(review.get("skill_tree_sha256") == structure["skill_tree_sha256"],
            "GQ_SKILL_CHANGED")

    producer = check_text(review.get("producer"), "GQ_PRODUCER_MISSING")
    reviewer = check_text(review.get("reviewer"), "GQ_REVIEWER_MISSING")
    require(producer != reviewer, "GQ_SELF_REVIEW_DECLARED")
    expected = {}
    actual = {}
    for field, minimum in (("requirements", 1), ("capabilities", 1),
                           ("interfaces", 0), ("applicability", 1), ("cases", 4)):
        expected[field] = rows(brief, field, minimum=minimum)
        actual[field] = rows(review, field, minimum=minimum)
        check_ids(expected[field], actual[field], field)

    semantics = rows(review, "semantics", minimum=1)
    report = {
        "check": "artifact-quality", "status": "EVIDENCE_PREFLIGHT",
        "candidate_tree_sha256": structure["skill_tree_sha256"],
        "brief_sha256": quality.sha(brief_raw),
        "counts": {name: len(items) for name, items in expected.items()},
        "blocking": [], "unverified": [], "machine_checks": "CHECKED",
        "semantic_truth": "NOT_AUTHENTICATED",
        "independent_reviewer_identity": "DECLARED_NOT_AUTHENTICATED",
        "host_attestation": "NOT_AUTHENTICATED", "release_authorization": "NOT_GRANTED",
    }
    if reviewer == "NOT_AVAILABLE":
        report["unverified"].append("GQ2/independent-reviewer-unavailable")
    require({row.get("kind") for row in expected["cases"].values()} >= CASE_KINDS,
            "GQ_CASE_KINDS_INCOMPLETE")

    for rid, source in expected["requirements"].items():
        check_text(source.get("text"), "GQ_REQUIREMENT_TEXT_MISSING")
        row = actual["requirements"][rid]
        status(row.get("status"), report, "GQ1/requirement/" + rid)
        if row.get("status") == "pass":
            reference(skill, row.get("ref"))
        else:
            check_text(row.get("reason"), "GQ_REQUIREMENT_GAP_UNEXPLAINED")

    automation_count = 0
    for cid, source in expected["capabilities"].items():
        check_text(source.get("text"), "GQ_CAPABILITY_TEXT_MISSING")
        mode = source.get("mode")
        require(mode in ("workflow", "automation", "external"),
                "GQ_CAPABILITY_MODE_INVALID")
        row = actual["capabilities"][cid]
        status(row.get("status"), report, "GQ1/capability/" + cid)
        if row.get("status") != "pass":
            check_text(row.get("reason"), "GQ_CAPABILITY_GAP_UNEXPLAINED")
            continue
        reference(skill, row.get("ref"))
        if mode == "automation":
            automation_count += 1
            implementations = quality.items(row.get("implementations"),
                                            "GQ_AUTOMATION_IMPLEMENTATION_MISSING")
            require(implementations, "GQ_AUTOMATION_IMPLEMENTATION_MISSING")
            for item in implementations:
                ref = mapping(item, "GQ_IMPLEMENTATION_INVALID")
                path = check_text(ref.get("path"), "GQ_IMPLEMENTATION_PATH_INVALID")
                # Distribution is established by a safe local file and its
                # bytes, not by the implementation language or filename suffix.
                require(path.startswith(("scripts/", "schemas/")),
                        "GQ_IMPLEMENTATION_NOT_DISTRIBUTED")
                digest = ref.get("sha256")
                check_sha(digest, "GQ_IMPLEMENTATION_SHA_INVALID")
                require(quality.sha(quality.read_data(quality.local(skill, path))) == digest,
                        "GQ_IMPLEMENTATION_CHANGED")
            if "run_ref" not in row:
                report["unverified"].append("GQ1/automation-run/" + cid)
            else:
                observed_file(evidence_root, row["run_ref"])
                require(row.get("exit_code") == 0 and
                        type(row.get("exit_code")) is int,
                        "GQ_AUTOMATION_RUN_FAILED")
        elif mode == "external":
            # Borrowed projects are not installed runtime dependencies by declaration.
            report["unverified"].append("GQ1/external-dependency/" + cid)

    entry = quality.read_data(quality.local(skill, "SKILL.md")).decode("utf-8")
    promises = sorted(set(m.group(0) for m in AUTO_PROMISE.finditer(entry)))
    if promises and automation_count == 0:
        report["unverified"].append("GQ1/undeclared-automation-promise")
    report["automation_promise_samples"] = promises[:5]

    for sid, row in semantics.items():
        status(row.get("status"), report, "GQ2/semantic/" + sid)
        if row.get("status") != "pass":
            check_text(row.get("reason"), "GQ_SEMANTIC_GAP_UNEXPLAINED")
            if row.get("record_ref") is not None:
                observed_file(evidence_root, row["record_ref"])
            continue
        refs = quality.items(row.get("refs"), "GQ_SEMANTIC_REFS_MISSING")
        require(len(refs) >= 2, "GQ_SEMANTIC_CROSS_REF_REQUIRED")
        seen = set()
        for ref in refs:
            reference(skill, ref)
            key = (ref["path"], ref["anchor"])
            require(key not in seen, "GQ_SEMANTIC_DUPLICATE_REFERENCE")
            seen.add(key)
        observed_file(evidence_root, row.get("record_ref"))

    interface_peers = {}
    for iid, source in expected["interfaces"].items():
        provider = check_text(source.get("provider"), "GQ_INTERFACE_PROVIDER_MISSING")
        consumer = check_text(source.get("consumer"), "GQ_INTERFACE_CONSUMER_MISSING")
        fields = quality.items(source.get("fields"), "GQ_INTERFACE_FIELDS_MISSING")
        require(fields and all(type(x) is str and x.strip() for x in fields),
                "GQ_INTERFACE_FIELDS_INVALID")
        row = actual["interfaces"][iid]
        status(row.get("status"), report, "GQ3/interface/" + iid)
        if row.get("status") != "pass":
            check_text(row.get("reason"), "GQ_INTERFACE_GAP_UNEXPLAINED")
            continue
        if peers_root is None:
            report["unverified"].append("GQ3/peer-files-unavailable/" + iid)
            continue
        require(peers_root.is_dir() and not peers_root.is_symlink(),
                "GQ_PEERS_ROOT_INVALID")
        documents = {}
        for role, skill_id in (("provider", provider), ("consumer", consumer)):
            require(metadata.is_skill_name(skill_id), "GQ_PEER_ID_INVALID")
            peer = skill if skill_id == skill.name else peers_root / skill_id
            if not peer.is_dir() or peer.is_symlink():
                report["unverified"].append("GQ3/peer-unavailable/" + iid + "/" + role)
                continue
            peer_struct = quality.skill_audit(peer, "generic")
            digest = peer_struct["skill_tree_sha256"]
            pinned = mapping(row.get("peer_tree_sha256"),
                             "GQ_INTERFACE_PEER_DIGESTS_MISSING")
            check_sha(pinned.get(role), "GQ_INTERFACE_PEER_DIGEST_INVALID")
            require(pinned[role] == digest, "GQ_INTERFACE_PEER_CHANGED")
            interface_peers[skill_id] = digest
            ref = row.get(role + "_ref")
            documents[role] = reference(peer, ref)
            for field in fields:
                if field not in documents[role]:
                    report["blocking"].append("GQ3/interface-field-missing/" + iid + "/" +
                                              role + "/" + field[:60])
        if len(documents) == 2:
            observed_file(evidence_root, row.get("record_ref"))

    report["peer_tree_sha256"] = interface_peers
    # A declared dependency must not disappear merely because the author omitted
    # it from the frozen brief. This is an advisory name-based candidate check;
    # prose can also reference peers as examples, so use NOT_PROVEN, never GO.
    if peers_root is not None:
        require(peers_root.is_dir() and not peers_root.is_symlink(),
                "GQ_PEERS_ROOT_INVALID")
        declared = set()
        for item in expected["interfaces"].values():
            declared.update((item["provider"], item["consumer"]))
        for peer in peers_root.iterdir():
            if (peer.name == skill.name or not metadata.is_skill_name(peer.name)
                    or peer.is_symlink() or not peer.is_dir()):
                continue
            if (re.search(r"(?<![A-Za-z0-9-])" + re.escape(peer.name) +
                          r"(?![A-Za-z0-9-])", entry) and peer.name not in declared):
                report["unverified"].append("GQ3/undeclared-peer-reference/" + peer.name)

    for aid, source in expected["applicability"].items():
        check_text(source.get("text"), "GQ_APPLICABILITY_RULE_MISSING")
        row = actual["applicability"][aid]
        status(row.get("status"), report, "GQ4/applicability/" + aid)
        if row.get("status") != "pass":
            check_text(row.get("reason"), "GQ_APPLICABILITY_GAP_UNEXPLAINED")
            if row.get("record_ref") is not None:
                observed_file(evidence_root, row["record_ref"])
            continue
        for field in ("scope", "counterexample", "limitation"):
            check_text(row.get(field), "GQ_APPLICABILITY_BOUNDARY_MISSING")
        reference(skill, row.get("ref"))
        observed_file(evidence_root, row.get("record_ref"))

    for tid, source in expected["cases"].items():
        require(source.get("kind") in CASE_KINDS | {"negative", "safety"},
                "GQ_CASE_KIND_INVALID")
        check_text(source.get("scenario"), "GQ_CASE_SCENARIO_MISSING")
        row = actual["cases"][tid]
        status(row.get("status"), report, "GQ5/task/" + tid)
        mode = row.get("mode")
        require(mode in ("host", "manual", "synthetic"), "GQ_CASE_MODE_INVALID")
        if row.get("status") == "pass":
            observed_file(evidence_root, row.get("record_ref"))
            if mode != "host":
                report["unverified"].append("GQ5/non-host-test/" + tid)
        else:
            check_text(row.get("reason"), "GQ_CASE_GAP_UNEXPLAINED")
            if row.get("record_ref") is not None:
                observed_file(evidence_root, row["record_ref"])

    if report["blocking"]:
        report["status"], report["exit_code"] = "FAIL", 2
    elif report["unverified"]:
        report["status"], report["exit_code"] = "NOT_PROVEN", 3
    else:
        report["status"], report["exit_code"] = "EVIDENCE_REVIEW_REQUIRED", 0
    report["note"] = ("Evidence bytes/coverage are checked. Even exit 0 is NOT a semantic "
                      "approval, verified independent reviewer, real host attestation, or GO.")
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Read-only GQ1-GQ5 Skill deliverable quality evidence preflight")
    parser.add_argument("--skill", required=True, type=Path)
    parser.add_argument("--brief", required=True, type=Path)
    parser.add_argument("--review", required=True, type=Path)
    parser.add_argument("--evidence-root", required=True, type=Path)
    parser.add_argument("--peers-root", type=Path,
                        help="sibling Skills for provider/consumer interface checks")
    args = parser.parse_args(argv)
    try:
        result = inspect(args.skill, args.brief, args.review,
                         args.evidence_root, args.peers_root)
    except (quality.Invalid, metadata.MetadataError, OSError, UnicodeError, SyntaxError,
            ValueError, TypeError, RecursionError) as exc:
        code = exc.code if isinstance(exc, (quality.Invalid, metadata.MetadataError)) else "GQ_INPUT_UNREADABLE"
        result = {"check": "artifact-quality", "status": "FAIL", "exit_code": 2,
                  "error": code, "host_attestation": "NOT_AUTHENTICATED",
                  "semantic_truth": "NOT_AUTHENTICATED"}
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return result["exit_code"]


if __name__ == "__main__":
    sys.exit(main())
