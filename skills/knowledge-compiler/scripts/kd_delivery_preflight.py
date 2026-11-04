#!/usr/bin/env python3
"""Read-only preflight for a standalone Skill's templates and final-artifact isolation.

Only syntactic evidence is checked. This tool never executes the candidate,
authenticates a literary interpretation, or attests host/model quality.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from kd_material_quality import Invalid as SkillInvalid, final_provenance_errors, skill_digest
from kd_round_output import SnapshotError, fingerprint as round_fingerprint
from kd_workspace_audit import checklist_fields_unique


class Invalid(Exception):
    pass


def strict_pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise Invalid("SPEC_DUPLICATE_KEY")
        result[key] = value
    return result


def read_spec(path):
    try:
        if not path.is_file() or path.stat().st_size > 128_000:
            raise Invalid("SPEC_INVALID")
        spec = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=strict_pairs)
    except (OSError, UnicodeError, ValueError, RecursionError):
        raise Invalid("SPEC_INVALID") from None
    if not isinstance(spec, dict) or type(spec.get("version")) is not int or spec["version"] != 1:
        raise Invalid("SPEC_VERSION")
    if not isinstance(spec.get("templates"), list):
        raise Invalid("TEMPLATES_INVALID")
    if "source_index" in spec:
        raise Invalid("SOURCE_INDEX_FORBIDDEN")
    if not spec["templates"] and spec.get("round_closure") is None:
        raise Invalid("SPEC_EMPTY")
    return spec


def relative_file(root, raw):
    if not isinstance(raw, str) or not raw or "\\" in raw or "\x00" in raw:
        raise Invalid("PACKAGE_PATH_UNSAFE")
    path = Path(raw)
    if path.is_absolute() or any(part in ("..", ".") for part in path.parts):
        raise Invalid("PACKAGE_PATH_UNSAFE")
    target = root / path
    if not target.is_file() or target.is_symlink():
        raise Invalid("PACKAGE_FILE_MISSING")
    try:
        if target.stat().st_size > 1_000_000:
            raise Invalid("PACKAGE_FILE_TOO_LARGE")
        target.resolve().relative_to(root.resolve())
        text = target.read_text(encoding="utf-8")
    except (OSError, UnicodeError, ValueError):
        raise Invalid("PACKAGE_FILE_UNREADABLE") from None
    return text


def unique_ids(raw, code):
    if not isinstance(raw, list) or not raw or any(
        not isinstance(i, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", i)
        for i in raw
    ) or len(set(raw)) != len(raw):
        raise Invalid(code)
    return raw



def pipe_cells(line):
    """Conservative GFM row parser: optional outer pipes; skip escaped/code pipes."""
    raw = line.strip()
    if not raw:
        return None
    if raw.startswith("|"):
        raw = raw[1:]
    cells, cell, i, fence = [], [], 0, 0
    while i < len(raw):
        char = raw[i]
        if char == chr(96):
            j = i
            while j < len(raw) and raw[j] == chr(96):
                j += 1
            run = j - i
            if fence == 0:
                fence = run
            elif fence == run:
                fence = 0
            cell.append(raw[i:j])
            i = j
            continue
        if char == "|":
            escaped = 0
            j = i - 1
            while j >= 0 and raw[j] == chr(92):
                escaped += 1
                j -= 1
            if fence == 0 and escaped % 2 == 0:
                cells.append("".join(cell).strip())
                cell = []
                i += 1
                continue
        cell.append(char)
        i += 1
    cells.append("".join(cell).strip())
    # A trailing unescaped, non-code pipe creates an empty terminal cell.
    if raw.endswith("|") and cells[-1] == "" and len(cells) > 1:
        cells.pop()
    return cells if len(cells) >= 2 else None


def _markdown_table_blocks(text):
    """Only adjacent pipe rows outside common fenced code; no markup rendering."""
    block = []
    fence = None
    for line in text.splitlines() + [""]:
        striped = line.lstrip(" ")
        indent = len(line) - len(striped)
        mark = re.match(r"^([~]{3,}|[" + chr(96) + r"]{3,})(.*)$", striped) if indent <= 3 else None
        if mark:
            ch, size = mark.group(1)[0], len(mark.group(1))
            if fence is None:
                fence = (ch, size)
            elif ch == fence[0] and size >= fence[1] and not mark.group(2).strip():
                fence = None
            if block:
                yield block
                block = []
            continue
        parsed = pipe_cells(line) if fence is None else None
        if parsed is None:
            if block:
                yield block
                block = []
        else:
            block.append(parsed)


def rows(text):
    """Return table-looking rows for field/source identity checks.

    Malformed tables are additionally caught by check_markdown_tables.
    """
    for block in _markdown_table_blocks(text):
        for row in block:
            if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in row):
                yield row


def check_markdown_tables(root, errors):
    # A single isolated line beginning/ending with pipes might be prose;
    # two or more adjacent pipe rows represent an attempted GFM table.
    for path in root.rglob("*.md"):
        if path.is_symlink() or not path.is_file():
            errors.append("PACKAGE_FILE_MISSING")
            continue
        try:
            if path.stat().st_size > 1_000_000:
                raise Invalid("PACKAGE_FILE_TOO_LARGE")
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append("PACKAGE_FILE_UNREADABLE")
            continue
        for block in _markdown_table_blocks(text):
            if len(block) < 2:
                continue
            header_count = len(block[0])
            sep = block[1]
            if len(sep) != header_count or not all(re.fullmatch(r":?-{3,}:?", cell) for cell in sep):
                errors.append("MARKDOWN_TABLE_HEADER_SEPARATOR_MISSING")
                continue
            if any(len(row) != header_count for row in block[2:]):
                errors.append("MARKDOWN_TABLE_COLUMN_COUNT_MISMATCH")

def _schema_field(schema, pointer):
    """Resolve an explicit editable JSON Schema property without running $ref."""
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise Invalid("TEMPLATE_SCHEMA_POINTER_INVALID")
    parts = pointer.split("/")[1:]
    if len(parts) < 2 or len(parts) % 2:
        raise Invalid("TEMPLATE_SCHEMA_POINTER_INVALID")
    target = schema
    for i in range(0, len(parts), 2):
        if parts[i] != "properties" or not parts[i + 1]:
            raise Invalid("TEMPLATE_SCHEMA_POINTER_INVALID")
        key = parts[i + 1]
        if re.search(r"~(?![01])", key):
            raise Invalid("TEMPLATE_SCHEMA_POINTER_INVALID")
        key = key.replace("~1", "/").replace("~0", "~")
        if not isinstance(target, dict) or not isinstance(target.get("properties"), dict):
            return None
        target = target["properties"].get(key)
        if target is None:
            return None
    return target


def check_templates(root, specs, errors):
    for entry in specs:
        if not isinstance(entry, dict):
            raise Invalid("TEMPLATE_SPEC_INVALID")
        ids = unique_ids(entry.get("field_ids"), "TEMPLATE_FIELD_IDS_INVALID")
        raw_path = entry.get("path")
        text = relative_file(root, raw_path)
        fmt = entry.get("format", "json-schema" if str(raw_path).endswith(".json") else "markdown-table")
        if fmt == "json-schema":
            try:
                schema = json.loads(text, object_pairs_hook=strict_pairs)
            except (ValueError, Invalid, RecursionError):
                errors.append("TEMPLATE_SCHEMA_INVALID")
                continue
            if not isinstance(schema, dict) or not isinstance(schema.get("properties"), dict):
                errors.append("TEMPLATE_SCHEMA_INVALID")
                continue
            paths = entry.get("field_paths")
            if paths is None:
                paths = {field: "/properties/" + field.replace("~", "~0").replace("/", "~1")
                         for field in ids}
            if (not isinstance(paths, dict) or set(paths) != set(ids)
                    or any(not isinstance(v, str) for v in paths.values())
                    or len(set(paths.values())) != len(paths)):
                raise Invalid("TEMPLATE_SCHEMA_FIELD_PATHS_INVALID")
            for field in ids:
                item = _schema_field(schema, paths[field])
                if item is None:
                    errors.append("TEMPLATE_SCHEMA_FIELD_MISSING")
                elif not isinstance(item, dict) or item.get("readOnly") is True or "const" in item:
                    errors.append("TEMPLATE_SCHEMA_FIELD_NOT_EDITABLE")
        elif fmt == "markdown-table":
            first = [cells[0] for cells in rows(text)]
            for field in ids:
                n = first.count(field)
                if n == 0:
                    errors.append("TEMPLATE_FIELD_ROW_MISSING")
                elif n > 1:
                    errors.append("TEMPLATE_FIELD_ROW_DUPLICATE")
            # Each requirement needs its own first-column row, not a combined row.
            for field in ids:
                if any(field in cell and cell != field for cell in first):
                    errors.append("TEMPLATE_FIELD_NOT_INDIVIDUAL")
        else:
            raise Invalid("TEMPLATE_FORMAT_UNSUPPORTED")


def check_external_notes(root, errors):
    for f in root.rglob("*.md"):
        if f.is_symlink() or not f.is_file():
            errors.append("PACKAGE_FILE_MISSING")
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append("PACKAGE_FILE_UNREADABLE")
            continue
        fenced = False
        for line in text.splitlines():
            s = line.strip()
            if s.startswith(("```", "~~~")):
                fenced = not fenced
                continue
            if fenced or "notes/" not in line:
                continue
            # Explicit negative examples are not external runtime dependencies.
            if re.search(r"不依赖|不要依赖|不得依赖|不要求访问|不能依赖|无需读取", line):
                continue
            if re.search(r"(?:\bnotes/|\.\./notes/)[A-Za-z0-9_.-]+", line):
                errors.append("EXTERNAL_NOTES_REFERENCE")



def check_round_closure(root, round_root, closure_spec, errors):
    """Optional static receipt check, aligned to R01's single Round status owner."""
    if round_root is None:
        errors.append("ROUND_ROOT_REQUIRED")
        return
    if not round_root.is_dir() or round_root.is_symlink():
        errors.append("ROUND_ROOT_INVALID")
        return
    if (not isinstance(closure_spec, dict) or any(
        not isinstance(closure_spec.get(k), str) for k in ("checklist", "log", "record")
    )):
        errors.append("ROUND_SPEC_INVALID")
        return
    if closure_spec["checklist"] != "checklist.md" or closure_spec["log"] != "log.md":
        # R01's lifecycle controls live in the round root. A notes copy must
        # never substitute for the actual checklist or append-only log.
        errors.append("ROUND_RECEIPT_INVALID")
        return
    if root.resolve().parent != (round_root / "output").resolve():
        errors.append("ROUND_SKILL_NOT_IN_OUTPUT")
        return
    try:
        checklist = relative_file(round_root, closure_spec["checklist"])
        log = relative_file(round_root, closure_spec["log"])
        checklist_fields_unique(checklist)
        record_raw = relative_file(round_root, closure_spec["record"])
        record = json.loads(record_raw, object_pairs_hook=strict_pairs)
    except (Invalid, ValueError, RecursionError):
        errors.append("ROUND_RECEIPT_INVALID")
        return
    # R01 is authoritative: only '- 状态：已完成' is a terminal success state.
    if not re.search(r"(?m)^[ \t]*-[ \t]*状态[ \t]*[：:][ \t]*已完成[ \t]*\r?$", checklist):
        errors.append("ROUND_CHECKLIST_NOT_FINAL")
    if not re.search(r"(?m)^[ \t]*-[ \t]*验收范围[ \t]*[：:][ \t]*静态交付[ \t]*\r?$", checklist):
        errors.append("ROUND_STATIC_SCOPE_MISSING")
    if (not isinstance(record, dict) or type(record.get("version")) is not int
            or record["version"] != 1 or record.get("status") != "STATIC_DELIVERED"):
        errors.append("ROUND_RECEIPT_INVALID")
        return
    try:
        digest = skill_digest(root)
    except (SkillInvalid, OSError, UnicodeError):
        errors.append("ROUND_SKILL_DIGEST_INVALID")
        return
    try:
        output_digest = round_fingerprint(round_root / "output")["tree_sha256"]
    except (SnapshotError, OSError, ValueError):
        errors.append("ROUND_OUTPUT_SNAPSHOT_INVALID")
        return
    if record.get("skill_tree_sha256") != digest:
        errors.append("ROUND_TREE_SHA_MISMATCH")
    if record.get("output_tree_sha256") != output_digest:
        errors.append("ROUND_OUTPUT_TREE_SHA_MISMATCH")
    if not re.search(r"(?m)^[ \t]*状态[ \t]*[：:][ \t]*已完成(?:[ \t]*[；;]|[ \t]*$)", log):
        errors.append("ROUND_LOG_NOT_FINAL")
    if "静态交付" not in log:
        errors.append("ROUND_LOG_STATIC_SCOPE_MISSING")
    if digest not in log:
        errors.append("ROUND_LOG_TREE_SHA_MISSING")
    if output_digest not in log:
        errors.append("ROUND_LOG_OUTPUT_SHA_MISSING")
    checks = record.get("checks")
    if not isinstance(checks, list) or not checks:
        errors.append("ROUND_CHECKS_EMPTY")
        return
    seen = set()
    for entry in checks:
        if not isinstance(entry, dict) or any(
            not isinstance(entry.get(k), str) for k in ("id", "path", "sha256", "status")
        ) or type(entry.get("required")) is not bool:
            errors.append("ROUND_CHECK_INVALID")
            continue
        if entry["id"] in seen:
            errors.append("ROUND_CHECK_DUPLICATE")
        seen.add(entry["id"])
        if not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            errors.append("ROUND_RECEIPT_SHA_INVALID")
            continue
        try:
            actual_path = round_root / entry["path"]
            raw = relative_file(round_root, entry["path"])
            observed = json.loads(raw, object_pairs_hook=strict_pairs)
        except (Invalid, ValueError, RecursionError):
            errors.append("ROUND_CHECK_RECEIPT_INVALID")
            continue
        if hashlib.sha256(actual_path.read_bytes()).hexdigest() != entry["sha256"]:
            errors.append("ROUND_CHECK_RECEIPT_SHA_MISMATCH")
        if not isinstance(observed, dict) or observed.get("status") != entry["status"]:
            errors.append("ROUND_CHECK_RECEIPT_STATUS_MISMATCH")
        if entry["status"] == "FAIL" or (entry.get("required") is True and entry["status"] != "PASS"):
            errors.append("ROUND_REQUIRED_CHECK_FAILED")
    # Records are not authenticated independent host or model attestations.
    if (type(record.get("live_task")) is not str or
            record["live_task"] not in {"NOT_RUN", "OBSERVED"}):
        errors.append("ROUND_REAL_TASK_STATUS_INVALID")
    if (type(record.get("independent_review")) is not str or
            record["independent_review"] not in {"NOT_PROVEN", "OBSERVED"}):
        errors.append("ROUND_INDEPENDENT_REVIEW_STATUS_INVALID")


def audit(root, spec, round_root=None):
    errors = []
    if not root.is_dir() or root.is_symlink() or not (root / "SKILL.md").is_file():
        raise Invalid("SKILL_ROOT_INVALID")
    check_templates(root, spec["templates"], errors)
    if "source_index" in spec:
        errors.append("SOURCE_INDEX_FORBIDDEN")
    try:
        errors.extend(final_provenance_errors(root))
    except (SkillInvalid, OSError, UnicodeError):
        errors.append("FINAL_ARTIFACT_UNREADABLE")
    check_external_notes(root, errors)
    check_markdown_tables(root, errors)
    if spec.get('round_closure') is not None:
        check_round_closure(root, round_root, spec['round_closure'], errors)
    errors = sorted(set(errors))
    return {"check": "delivery-preflight", "status": "FAIL" if errors else "PASS",
            "errors": errors, "verdict": "STATIC_ONLY_SEMANTICS_NOT_PROVEN"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", required=True)
    parser.add_argument("--spec", required=True, help="External round/notes JSON with required template fields and optional closure")
    parser.add_argument("--round-dir", help="Only when spec.round_closure is supplied; read-only finalization check")
    args = parser.parse_args()
    try:
        result = audit(Path(args.skill), read_spec(Path(args.spec)), Path(args.round_dir) if args.round_dir else None)
    except Invalid as exc:
        result = {"check": "delivery-preflight", "status": "FAIL",
                  "errors": [str(exc)], "verdict": "STATIC_ONLY_SEMANTICS_NOT_PROVEN"}
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
