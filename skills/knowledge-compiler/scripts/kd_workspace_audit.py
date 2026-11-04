#!/usr/bin/env python3
"""Read-only workspace lifecycle and results-integrity preflight.

Advisory filesystem checks. This cannot authenticate user authorization,
prove agent reasoning, freeze files, or infer how many rounds the user intended.
No external YAML dependencies and no writes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat

from kd_round_output import SnapshotError, fingerprint
from kd_skill_metadata import string_scalar

SHA = re.compile(r"^[0-9a-f]{64}$")
ROUND = re.compile(r"^round-[0-9]{2,}-[0-9]{4}-[0-9]{2}-[0-9]{2}$")
INPUT_REV = re.compile(r"^manifest-v([0-9]{2,})\.yaml$")
STATUS = re.compile(r"^\s*-\s*状态\s*[：:]\s*(.+)\s*$", re.M)
TREE = re.compile(r"^\s*-\s*整树 SHA-256\s*[：:]\s*([0-9a-f]{64})\s*$", re.M)
LATEST = re.compile(r"^\s*-\s*本轮最新有效输入清单\s*[：:]\s*(\S+)", re.M)
LATEST_SHA = re.compile(r"^\s*-\s*最新清单 SHA-256\s*[：:]\s*([0-9a-f]{64})", re.M)
REQUIREMENTS_SHA = re.compile(r"^\s*-\s*总需求副本 SHA-256\s*[：:]\s*([0-9a-f]{64})", re.M)
FLOW = re.compile(r"^[ \t]*-[ \t]*流程[ \t]*[：:][ \t]*([^\r\n]+?)[ \t]*\r?$", re.M)
CANCELLATION = re.compile(r"^[ \t]*-[ \t]*取消依据[ \t]*[：:][ \t]*(\S[^\r\n]*)\r?$", re.M)
ACTIVE = frozenset(("调查中", "已确认", "进行中", "等待用户"))
STATES = ACTIVE | {"已完成", "已取消"}
CHECKLIST_FIELDS = ("状态", "流程", "取消依据", "验收范围", "整树 SHA-256",
                    "本轮最新有效输入清单", "最新清单 SHA-256", "总需求副本 SHA-256")
MAX_TEXT = 1024 * 1024


def _text(path: Path) -> str:
    """Reject non-files and replacements while reading small control files."""
    before = path.lstat()
    if not stat.S_ISREG(before.st_mode) or before.st_size > MAX_TEXT:
        raise ValueError("CONTROL_FILE_UNSAFE")
    fd = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        st = os.fstat(fd)
        if (st.st_dev, st.st_ino) != (before.st_dev, before.st_ino):
            raise ValueError("CONTROL_FILE_CHANGED")
        with os.fdopen(os.dup(fd), "rb") as stream:
            data = stream.read(MAX_TEXT + 1)
        after = os.fstat(fd)
        if (len(data) > MAX_TEXT or
                (st.st_size, st.st_mtime_ns, st.st_ctime_ns) !=
                (after.st_size, after.st_mtime_ns, after.st_ctime_ns)):
            raise ValueError("CONTROL_FILE_CHANGED")
        return data.decode("utf-8")
    finally:
        os.close(fd)


def _hash(path: Path) -> str:
    """Never follow symlinks, and do not trust a file changing under our feet."""
    before = path.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise ValueError("ARTIFACT_NOT_REGULAR")
    h = hashlib.sha256()
    fd = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        st = os.fstat(fd)
        if (st.st_dev, st.st_ino) != (before.st_dev, before.st_ino):
            raise ValueError("ARTIFACT_CHANGED")
        while True:
            data = os.read(fd, 1024 * 1024)
            if not data:
                break
            h.update(data)
        after = os.fstat(fd)
        if (st.st_size, st.st_mtime_ns, st.st_ctime_ns) != (
                after.st_size, after.st_mtime_ns, after.st_ctime_ns):
            raise ValueError("ARTIFACT_CHANGED")
        return h.hexdigest()
    finally:
        os.close(fd)


def _scalar(value: str) -> str:
    value = value.strip()
    if value.startswith(('"', "'")):
        # Parse the closing quote before its optional comment. Removing a
        # comment first would corrupt a quoted value containing " #".
        return string_scalar(value)
    return re.split(r"[ \t]+#", value, maxsplit=1)[0].strip()


def _field(text: str, name: str) -> str | None:
    matches = list(re.finditer(r"^" + re.escape(name) + r":[ \t]*(.*?)[ \t]*$", text, re.M))
    if len(matches) > 1:
        raise ValueError("CONTROL_FIELD_DUPLICATE: " + name)
    return _scalar(matches[0][1]) if matches else None


def checklist_fields_unique(text: str) -> None:
    """A lifecycle control has one value, including when a duplicate is invalid."""
    for name in CHECKLIST_FIELDS:
        pattern = r"^[ \t]*-[ \t]*" + re.escape(name) + r"[ \t]*[：:][^\r\n]*\r?$"
        if len(re.findall(pattern, text, re.M)) > 1:
            raise ValueError("CONTROL_FIELD_DUPLICATE: " + name)


def audit(workspace: Path, expected_rounds: int | None = None) -> dict:
    findings: list[dict] = []
    records: list[dict] = []

    def report(code: str, location: str, detail: str):
        findings.append({"code": code, "location": location, "detail": detail})

    try:
        st = workspace.lstat()
        if not stat.S_ISDIR(st.st_mode):
            raise ValueError("WORKSPACE_NOT_DIRECTORY")
    except (OSError, ValueError) as exc:
        return {"status": "FAIL", "exit_code": 2, "rounds_total": 0,
                "findings": [{"code": "WORKSPACE_UNREADABLE", "detail": str(exc)}]}

    rounds = workspace / "rounds"
    if rounds.exists() or rounds.is_symlink():
        try:
            if not stat.S_ISDIR(rounds.lstat().st_mode):
                raise ValueError("ROUNDS_DIR_UNSAFE")
            entries = sorted(rounds.iterdir())
        except (OSError, ValueError) as exc:
            report("ROUNDS_DIR_UNSAFE", "rounds", str(exc))
            entries = []
        for entry in entries:
            name = entry.name
            if not ROUND.fullmatch(name):
                if entry.is_dir() or entry.is_symlink():
                    report("ROUND_NAME_UNEXPECTED", "rounds/" + name,
                           "round directories must use round-NN-YYYY-MM-DD")
                # README and Finder metadata are not additional rounds.
                continue
            try:
                if not stat.S_ISDIR(entry.lstat().st_mode):
                    raise ValueError("ROUND_NOT_DIRECTORY")
                checklist = _text(entry / "checklist.md")
                checklist_fields_unique(checklist)
                match = STATUS.search(checklist)
                if match is None:
                    report("ROUND_STATUS_MISSING", name, "checklist has no top-level - 状态：")
                    state = "UNKNOWN"
                else:
                    state = re.split(r"[（(\s]", match[1], maxsplit=1)[0]
                    if state not in STATES:
                        report("ROUND_STATUS_UNKNOWN", name, state)
                records.append({"name": name, "status": state})
                if state == "已取消":
                    basis = CANCELLATION.search(checklist)
                    if basis is None or basis[1].strip().startswith("<"):
                        report("CANCELLATION_BASIS_MISSING", name,
                               "cancelled rounds need the actual user stop-message reference")
                    # Cancellation is not acceptance and requires no completed
                    # output. Preserve any partial work without adopting it.
                    continue
                if state != "已完成":
                    checked = re.findall(r"^\s*-\s*\[x\]\s+", checklist, re.M)
                    unchecked = re.findall(r"^\s*-\s*\[ \]\s+", checklist, re.M)
                    work_output = entry / "output"
                    has_output = (work_output.is_dir() and
                                  any(child.is_file() for child in work_output.rglob("*")))
                    if state in ACTIVE and (
                            re.search(r"^\s*-\s*\[x\]\s*检查与交付\s*$", checklist, re.M)
                            or checked and not unchecked and has_output):
                        report("ROUND_STATUS_STALE", name,
                               "acceptance is checked while status is not 已完成")
                    continue

                flows = FLOW.findall(checklist)
                if len(flows) > 1 or flows and flows[0] not in ("标准", "轻量短笔记"):
                    report("ROUND_FLOW_INVALID", name, "use one standard or lightweight flow field")
                    continue
                lightweight = flows == ["轻量短笔记"]
                try:
                    result = fingerprint(entry / "output")
                except (SnapshotError, OSError, ValueError) as exc:
                    report("COMPLETED_OUTPUT_INVALID", name, str(exc))
                    continue
                if lightweight and any(Path(item["path"]).name in ("SKILL.md", "AGENTS.md")
                                       for item in result["files"]):
                    report("LIGHTWEIGHT_ARTIFACT_INVALID", name,
                           "Skill or executable Rule entrypoints cannot use the short-note exemption")
                if not lightweight:
                    expected = TREE.search(checklist)
                    if not expected:
                        report("COMPLETED_FREEZE_DIGEST_MISSING", name,
                               "completed standard round lacks output tree SHA-256")
                    elif result["tree_sha256"] != expected[1]:
                        report("COMPLETED_FREEZE_DRIFT", name,
                               "frozen output SHA-256 disagrees with actual files")

                    inp = entry / "inputs"
                    initial = inp / "manifest.yaml"
                    old_sha = None
                    try:
                        old_sha = _hash(initial)
                        requirements = inp / "requirements.md"
                        expected_req = REQUIREMENTS_SHA.search(checklist)
                        if not expected_req or _hash(requirements) != expected_req[1]:
                            report("REQUIREMENTS_SNAPSHOT_UNVERIFIED", name,
                                   "initial requirements SHA missing or mismatched")
                    except (OSError, ValueError) as exc:
                        report("INPUT_SNAPSHOT_MISSING", name, str(exc))
                    revised = inp / "revisions"
                    versions = []
                    if revised.exists() or revised.is_symlink():
                        if not stat.S_ISDIR(revised.lstat().st_mode):
                            report("INPUT_REVISIONS_UNSAFE", name, "not a real directory")
                        else:
                            for file in revised.iterdir():
                                match = INPUT_REV.fullmatch(file.name)
                                if match:
                                    versions.append((int(match[1]), file))
                            versions.sort()
                            for expected_version, (rev, file) in enumerate(versions, 2):
                                try:
                                    body = _text(file)
                                    previous = _field(body, "previous_manifest_sha256")
                                    declared_rev = _field(body, "revision")
                                    if (rev != expected_version or
                                            declared_rev != str(rev) or
                                            previous != old_sha):
                                        report("INPUT_VERSION_CHAIN_INVALID", name,
                                               file.name + " lacks sequential version or prior SHA")
                                    old_sha = _hash(file)
                                except (OSError, ValueError) as exc:
                                    report("INPUT_VERSION_UNREADABLE", name,
                                           file.name + ": " + str(exc))
                                    old_sha = None
                    latest = LATEST.search(checklist)
                    latest_hash = LATEST_SHA.search(checklist)
                    latest_rel = ("inputs/revisions/" + versions[-1][1].name
                                  if versions else "inputs/manifest.yaml")
                    if (latest is None or latest_hash is None or
                            latest[1] != latest_rel or latest_hash[1] != old_sha):
                        report("LATEST_INPUT_UNVERIFIED", name,
                               "checklist latest input reference/SHA does not match the final input version")
            except (OSError, UnicodeError, ValueError) as exc:
                report("ROUND_CONTROL_INVALID", name, str(exc))

    active = [r["name"] for r in records if r["status"] in ACTIVE]
    cancelled = sum(r["status"] == "已取消" for r in records)
    counted_rounds = len(records) - cancelled
    if len(active) > 1:
        report("MULTIPLE_ACTIVE_ROUNDS", "rounds",
               "multiple unfinished rounds: " + ", ".join(active[:20]))
    if expected_rounds is not None and counted_rounds != expected_rounds:
        report("ROUND_COUNT_MISMATCH", "rounds",
               f"expected {expected_rounds} non-cancelled delivery rounds, found {counted_rounds}")

    results = workspace / "results"
    if results.exists() or results.is_symlink():
        try:
            if not stat.S_ISDIR(results.lstat().st_mode):
                raise ValueError("RESULTS_DIR_UNSAFE")
            has_artifacts = False
            for entry in sorted(results.iterdir()):
                mode = entry.lstat().st_mode
                if entry.name == "manifest.yaml":
                    continue  # The control-file reader below checks its type.
                if entry.name in ("skills", "rules"):
                    has_artifacts = True
                    continue
                if entry.name in ("README.md", ".DS_Store") and stat.S_ISREG(mode):
                    continue  # Optional index and Finder metadata, not adopted artifacts.
                has_artifacts = True
                if entry.name in ("AGENTS.md", "SKILL.md"):
                    report("RESULTS_ROOT_ARTIFACT_MIXED", "results/" + entry.name,
                           "Skill and Rule outputs belong under skills/ or rules/")
                else:
                    report("RESULTS_ROOT_ENTRY_UNCLASSIFIED", "results/" + entry.name,
                           "entry is outside the standard layout; inspect its purpose and authorized placement")
            manifest = results / "manifest.yaml"
            if manifest.exists() or manifest.is_symlink():
                content = _text(manifest)
                rev = _field(content, "revision")
                prev = _field(content, "previous_manifest_sha256")
                if not rev or not rev.isdigit() or int(rev) < 1:
                    report("RESULTS_REVISION_MISSING", "results/manifest.yaml",
                           "revision must be a positive integer")
                previous_valid = (prev == "null" if rev == "1" else
                                  bool(rev and rev.isdigit() and int(rev) > 1 and
                                       prev is not None and SHA.fullmatch(prev)))
                if not previous_valid:
                    report("RESULTS_PREVIOUS_SHA_INVALID", "results/manifest.yaml",
                           "initial revision must use null; later revisions need previous manifest SHA")
                if not re.search(r"^accepted_rounds:\s*$", content, re.M):
                    report("RESULTS_ACCEPTED_ROUNDS_MISSING", "results/manifest.yaml",
                           "missing accepted_rounds source list")
                artifacts = []
                collecting = False
                for line in content.splitlines():
                    if line == "artifacts:":
                        collecting = True
                        continue
                    if collecting and line and not line[0].isspace():
                        collecting = False
                    if not collecting:
                        continue
                    match = re.match(r"^\s+- path:\s*(.+?)\s*$", line)
                    if match:
                        artifacts.append({"path": _scalar(match[1])})
                    else:
                        match = re.match(r"^\s+(sha256|source_round|decision_ref):\s*(.*?)\s*$", line)
                        if match and artifacts:
                            if match[1] in artifacts[-1]:
                                raise ValueError("CONTROL_FIELD_DUPLICATE: " + match[1])
                            artifacts[-1][match[1]] = _scalar(match[2])
                if not artifacts:
                    report("RESULTS_ARTIFACTS_MISSING", "results/manifest.yaml",
                           "each delivered Skill/Rule file needs its own path and SHA-256")
                actual_files = set()
                for category in ("skills", "rules"):
                    folder = results / category
                    if not folder.exists() and not folder.is_symlink():
                        continue
                    if not stat.S_ISDIR(folder.lstat().st_mode):
                        report("RESULTS_CATEGORY_UNSAFE", "results/" + category,
                               "category is not a directory")
                        continue
                    for item in folder.rglob("*"):
                        rel = item.relative_to(results).as_posix()
                        mode = item.lstat().st_mode
                        if stat.S_ISREG(mode):
                            actual_files.add(rel)
                        elif not stat.S_ISDIR(mode):
                            report("RESULTS_FILE_UNSAFE", "results/" + rel,
                                   "symlink or special file")
                listed = set()
                for item in artifacts:
                    rel = item.get("path", "")
                    parts = Path(rel).parts
                    if (not isinstance(rel, str) or not parts or
                            parts[0] not in ("skills", "rules") or
                            any(part in ("..", ".") for part in parts) or
                            rel.startswith("/") or "\\" in rel or "<" in rel or ">" in rel):
                        report("RESULTS_ARTIFACT_PATH_INVALID", "results/manifest.yaml", repr(rel))
                        continue
                    if rel in listed:
                        report("RESULTS_ARTIFACT_DUPLICATE", "results/manifest.yaml", rel)
                    listed.add(rel)
                    digest = item.get("sha256", "")
                    if not isinstance(digest, str) or not SHA.fullmatch(digest):
                        report("RESULTS_ARTIFACT_SHA_MISSING", "results/" + rel,
                               "must have actual 64-character SHA-256")
                    else:
                        try:
                            if _hash(results / rel) != digest:
                                report("RESULTS_ARTIFACT_DRIFT", "results/" + rel,
                                       "actual bytes do not match manifest")
                        except (OSError, ValueError) as exc:
                            report("RESULTS_ARTIFACT_UNREADABLE", "results/" + rel, str(exc))
                    if not item.get("source_round") or not item.get("decision_ref"):
                        report("RESULTS_DECISION_PROVENANCE_MISSING", "results/" + rel,
                               "source_round and decision_ref are mandatory")
                for extra in sorted(actual_files - listed):
                    report("RESULTS_FILE_NOT_INDEXED", "results/" + extra,
                           "current artifact missing from manifest")
            elif has_artifacts:
                report("RESULTS_MANIFEST_MISSING", "results",
                       "adopted artifacts exist without a manifest")
        except (OSError, UnicodeError, ValueError, TypeError) as exc:
            report("RESULTS_CONTROL_INVALID", "results", str(exc))

    return {"status": "PASS" if not findings else "FAIL",
            "exit_code": 0 if not findings else 2,
            "rounds_total": len(records), "rounds_active": len(active),
            "rounds_cancelled": cancelled, "rounds_counted": counted_rounds,
            "rounds_completed": sum(r["status"] == "已完成" for r in records),
            "rounds": records, "findings": findings,
            "limits": "advisory static check; does not verify actual human approval or task quality"}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Read-only review of a distillation workspace; never rewrites historical rounds")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--expect-rounds", type=int, default=None,
                        help="user-established independent delivery rounds, excluding cancelled rounds")
    args = parser.parse_args(argv)
    if args.expect_rounds is not None and args.expect_rounds < 0:
        parser.error("--expect-rounds must be a nonnegative integer")
    report = audit(args.workspace, args.expect_rounds)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
    return report["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
