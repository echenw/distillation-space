#!/usr/bin/env python3
"""Read-only candidate scaffold, change preview, maintenance diagnostics."""
from __future__ import annotations
import argparse
from collections import defaultdict
import difflib
import hashlib
import json
import re
from pathlib import Path

import kd_task_brief as intake
import kd_material_quality as quality
import kd_material_ops as normalization

MAX_FILES = 300
MAX_BYTES = 24 * 1024 * 1024
RULE_WORDS = re.compile(r"(?i)\b(?:must|should|always|never|do not|require)\b|必须|应该|应当|一律|禁止|不得|务必|先执行|应优先")
CODE_FILES = {".py", ".sh", ".js", ".ts", ".bash", ".zsh", ".exe"}


class Invalid(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def require(ok, code):
    if not ok:
        raise Invalid(code)


def read(path):
    require(path.is_file() and not path.is_symlink(), "INPUT_MISSING")
    require(path.stat().st_size <= MAX_BYTES, "INPUT_TOO_LARGE")
    with path.open("rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
    require(len(raw) <= MAX_BYTES, "INPUT_TOO_LARGE")
    return raw


def read_brief(path):
    doc = intake.parse(read(path))
    report = intake.validate(doc)
    return doc, report


def index(root):
    require(root.is_dir() and not root.is_symlink(), "TARGET_ROOT_INVALID")
    output = {}
    total = 0
    for base, dirs, names in normalization.walk_source_tree(root):
        for name in dirs + names:
            require(not (Path(base) / name).is_symlink(), "TARGET_SYMLINK")
        for name in sorted(names):
            item = Path(base) / name
            require(item.is_file(), "TARGET_NONFILE")
            rel = item.relative_to(root).as_posix()
            blob = read(item)
            total += len(blob)
            require(total <= MAX_BYTES and len(output) < MAX_FILES, "TARGET_TOO_LARGE")
            output[rel] = blob
    return output


def tree_digest(indexed):
    value = hashlib.sha256()
    for name, content in sorted(indexed.items()):
        encoded = name.encode("utf-8")
        value.update(len(encoded).to_bytes(4, "big"))
        value.update(encoded)
        value.update(hashlib.sha256(content).digest())
    return value.hexdigest()


def scaffold(brief, deliverable_id):
    doc, report = read_brief(brief)
    matched = [d for d in doc["plan"].get("deliverables", [])
               if d["id"] == deliverable_id]
    require(len(matched) == 1, "DELIVERABLE_NOT_FOUND")
    target = matched[0]
    name = re.sub("[^a-z0-9-]+", "-", deliverable_id.lower()).strip("-")
    require(bool(name), "INVALID_ARTIFACT_NAME")
    description = target["purpose"].replace("\n", " ").replace(":", " - ")
    if target["kind"] == "skill":
        trigger = target.get("trigger", "Trigger awaits confirmation")
        expected = target.get("expected_result", "Result awaits confirmation")
        body = ("---\nname: " + name + "\ndescription: " + description +
                " Use when " + trigger.replace("\n", " ") + "\n---\n\n# " +
                name + "\n\n## Trigger\n" + trigger + "\n\n## Expected result\n" +
                expected + "\n\n## Instructions\n\n"
                "## Boundaries\nUse only authorized materials. Do not run untrusted code.\n")
        file_name = "SKILL.md"
    else:
        body = ("# Proposed rule: " + name + "\n\n"
                "Purpose: " + description + "\n\n"
                "<!-- Await evidence-backed rule text and explicit target-specific approval. -->\n")
        file_name = (Path(target["target"].get("destination") or "proposed-rule.md").name
                     or "proposed-rule.md")
    return {"check": "scaffold", "status": "PROPOSAL_ONLY", "artifact_id": deliverable_id,
            "file": file_name, "content": body,
            "text_sha256": quality.sha(body.encode("utf-8")),
            "task_plan_sha256": report["plan_sha256"],
            "model_generation": "NOT_RUN", "host_file_written": False}


def new_normative_lines(old, new):
    """Flag new rules for external evidence review; inline markers cannot attest it."""
    before = old.decode("utf-8").splitlines() if old else []
    after = new.decode("utf-8").splitlines()
    matcher = difflib.SequenceMatcher(a=before, b=after, autojunk=False)
    flagged = []
    for tag, _start, _end, start, end in matcher.get_opcodes():
        if tag not in {"replace", "insert"}:
            continue
        for i in range(start, end):
            line = after[i].strip()
            if not RULE_WORDS.search(line) or line.startswith(("#", "<!--", "|", chr(96)*3)):
                continue
            flagged.append(i+1)
    return flagged


def review(before, after, kind="skill", expected_before=None, expected_after=None):
    require(kind in {"skill", "rule"}, "INVALID_CANDIDATE_KIND")
    old = index(before) if before is not None else {}
    new = index(after)
    old_hash = tree_digest(old)
    new_hash = tree_digest(new)
    require(expected_before is None or expected_before == old_hash, "TARGET_BEFORE_CHANGED")
    require(expected_after is None or expected_after == new_hash, "CANDIDATE_AFTER_CHANGED")
    changed = sorted(k for k in old.keys() | new.keys() if old.get(k) != new.get(k))
    require(changed, "NO_CANDIDATE_CHANGE")
    untraced, executable, removed = {}, [], []
    for rel in changed:
        if rel not in new:
            removed.append(rel)
            continue
        if Path(rel).suffix.lower() in CODE_FILES:
            executable.append(rel)
        if Path(rel).suffix.lower() in {".md", ".markdown"}:
            found = new_normative_lines(old.get(rel, b""), new[rel])
            if found:
                untraced[rel] = found
    structural = (quality.result("skill", lambda: quality.skill_audit(after, "generic"))
                  if kind == "skill" else None)
    final_errors = quality.final_provenance_errors(after)
    needs_review = bool(untraced or executable or removed or final_errors or
                        (structural is not None and structural["status"] != "PASS"))
    return {"check": "review",
            "status": "NEEDS_REVIEW" if needs_review else "STATIC_REVIEW_READY",
            "candidate_kind": kind, "before_tree_sha256": old_hash,
            "after_tree_sha256": new_hash,
            "changed_files": changed, "deleted_files": removed,
            "new_or_changed_executables": executable,
            "untraced_normative_line_numbers": untraced,
            "final_artifact_errors": final_errors,
            "static_skill_check": structural,
            "human_approval": "NOT_GRANTED", "semantic_quality": "NOT_PROVEN",
            "host_effect": "NOT_RUN", "apply_changes": False}


def maintenance(root):
    files = index(root)
    paragraphs = defaultdict(list)
    suspicious = []
    for name, raw in files.items():
        if not name.endswith(".md"):
            continue
        try:
            content = raw.decode("utf-8")
        except UnicodeError as exc:
            raise Invalid("INVALID_MARKDOWN_ENCODING") from exc
        for number, text in enumerate(content.splitlines(), 1):
            text = text.strip()
            if len(text) > 55 and not text.startswith(("#", ">", "|", chr(96)*3)):
                paragraphs[text].append({"file": name, "line": number})
            if re.search(r"\bTODO\b|FIXME|待核实|暂时兼容", text, re.I):
                suspicious.append({"file": name, "line": number})
    duplicated = [refs for refs in paragraphs.values()
                  if len({row["file"] for row in refs}) > 1]
    structural = quality.result("skill", lambda: quality.skill_audit(root, "generic"))
    final_errors = quality.final_provenance_errors(root)
    status = ("NEEDS_REVIEW" if duplicated or suspicious or final_errors or
              structural["status"] != "PASS" else "STATIC_REVIEW_READY")
    return {"check": "maintenance", "status": status,
            "duplicate_normative_candidates": duplicated,
            "staleness_markers": suspicious[:100], "static_skill_check": structural,
            "final_artifact_errors": final_errors,
            "auto_retirement": False, "usage_verified": False}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Read-only candidate scaffold/review/maintenance")
    sub = ap.add_subparsers(dest="action", required=True)
    s = sub.add_parser("scaffold")
    s.add_argument("--brief", required=True)
    s.add_argument("--id", required=True)
    r = sub.add_parser("review")
    r.add_argument("--before")
    r.add_argument("--after", required=True)
    r.add_argument("--kind", choices=("skill", "rule"), default="skill")
    r.add_argument("--before-sha256")
    r.add_argument("--after-sha256")
    m = sub.add_parser("maintenance")
    m.add_argument("--skill", required=True)
    args = ap.parse_args(argv)
    try:
        result = (scaffold(Path(args.brief), args.id) if args.action == "scaffold"
                  else review(Path(args.before) if args.before else None,
                              Path(args.after), args.kind, args.before_sha256,
                              args.after_sha256) if args.action == "review"
                  else maintenance(Path(args.skill)))
        print(json.dumps(result, sort_keys=True, ensure_ascii=False))
        return 0 if result["status"] in {"STATIC_REVIEW_READY", "PROPOSAL_ONLY"} else 2
    except (Invalid, intake.Invalid, quality.Invalid, OSError, UnicodeError, ValueError) as exc:
        code = exc.code if isinstance(exc, (Invalid, intake.Invalid, quality.Invalid)) else "INPUT_ERROR"
        print(json.dumps({"check": args.action, "status": "FAIL", "error": code}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
