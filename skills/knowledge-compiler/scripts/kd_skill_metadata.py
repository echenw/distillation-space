"""Shared Skill frontmatter subset: strings and a metadata string mapping."""
from __future__ import annotations

import json
import re

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def is_skill_name(value: object) -> bool:
    return type(value) is str and len(value) <= 64 and bool(NAME.fullmatch(value))


class MetadataError(ValueError):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


def require(ok: bool, code: str) -> None:
    if not ok:
        raise MetadataError(code)


def mapping_entry(line: str) -> tuple[str, str]:
    match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):(?:[ \t]+(.*))?", line)
    require(match is not None, "METADATA_SYNTAX")
    return match.group(1), match.group(2) or ""


def string_scalar(raw: str) -> str:
    """Parse nonempty, printable single-line strings; never resolve YAML objects."""
    raw = raw.strip()
    if raw.startswith('"'):
        quoted = re.fullmatch(r'("(?:\\.|[^"\\])*")(?:[ \t]+#.*)?', raw)
        require(quoted is not None, "METADATA_INVALID")
        try:
            value = json.loads(quoted.group(1))
        except ValueError as exc:
            raise MetadataError("METADATA_INVALID") from exc
    elif raw.startswith("'"):
        quoted = re.fullmatch(r"'((?:[^']|'')*)'(?:[ \t]+#.*)?", raw)
        require(quoted is not None, "METADATA_INVALID")
        value = quoted.group(1).replace("''", "'")
    else:
        value = re.split(r"[ \t]+#", raw, maxsplit=1)[0].strip()
        require(bool(value) and value[0].isalpha() and
                not re.search(r":[ \t]|:$", value) and
                value.lower() not in {"null", "~", "true", "false", "yes", "no", "on", "off"},
                "METADATA_INVALID")
    require(type(value) is str and bool(value.strip()) and value.isprintable(),
            "METADATA_INVALID")
    return value


def frontmatter_end(lines: list[str]) -> int:
    """Return the first standalone closing delimiter after the opening line."""
    require(bool(lines) and lines[0] == "---", "FRONTMATTER")
    try:
        return lines.index("---", 1)
    except ValueError as exc:
        raise MetadataError("FRONTMATTER") from exc


def parse_frontmatter(body: str) -> dict[str, str | dict[str, str]]:
    lines = body.splitlines()
    end = frontmatter_end(lines)
    fields: dict[str, str | dict[str, str]] = {}
    metadata_map = None
    metadata_indent = None
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[0].isspace():
            require(metadata_map is not None and "\t" not in line[:len(line) - len(line.lstrip())],
                    "METADATA_SYNTAX")
            indent = len(line) - len(line.lstrip(" "))
            if metadata_indent is None:
                metadata_indent = indent
            require(indent == metadata_indent, "METADATA_SYNTAX")
            key, value = mapping_entry(line[indent:])
            require(key not in metadata_map, "METADATA_INVALID")
            metadata_map[key] = string_scalar(value)
            continue
        if metadata_map is not None:
            require(bool(metadata_map), "METADATA_INVALID")
        metadata_map = None
        metadata_indent = None
        key, value = mapping_entry(line)
        require(key not in fields, "METADATA_INVALID")
        if key == "metadata" and (not value.strip() or value.lstrip().startswith("#")):
            metadata_map = {}
            fields[key] = metadata_map
        else:
            fields[key] = string_scalar(value)
    if metadata_map is not None:
        require(bool(metadata_map), "METADATA_INVALID")
    require({"name", "description"} <= fields.keys(), "METADATA_MISSING")
    require(is_skill_name(fields["name"]), "NAME_INVALID")
    return fields
