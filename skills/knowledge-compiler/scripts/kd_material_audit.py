#!/usr/bin/env python3
"""Read-only R06 material batch attachment preflight.

Checks explicit local Markdown links only, never claim provenance, factual
truth or approval. Untrusted link text is excluded from all diagnostics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import re
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

MAX_BATCH_BYTES = 2 * 1024 * 1024
INLINE_LINK = re.compile(
    r"""!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)\n]+)(?:\s+(?:"[^"\n]*"|'[^'\n]*'|\([^)\n]*\)))?\s*\)"""
)
INLINE_CODE = re.compile(r"(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)", re.S)


def visible_markdown_lines(body: str):
    """Exclude real Markdown code, including fenced blocks nested in quotes.

    Keep original character offsets for R09 external claim anchors and R06
    attachment line numbers. Both consumers must see the same prose.
    """
    active = None  # (fence_character, min_length, quote_depth)
    offset = 0
    for line in body.splitlines(keepends=True):
        start = offset
        offset += len(line)
        content, depth = line, 0
        while True:
            prefix = re.match(r"^ {0,3}>[ \t]?", content)
            if prefix is None:
                break
            content = content[prefix.end():]
            depth += 1
        marker = re.match(r"^ {0,3}(" + chr(96) + r"{3,}|~{3,})", content)
        if active is not None:
            # A nonempty line outside the quote ends that quoted fence;
            # follow-on prose must still be checked for real dependencies.
            if depth < active[2] and content.strip():
                active = None
            else:
                if (marker and depth == active[2] and
                        marker.group(1)[0] == active[0] and
                        len(marker.group(1)) >= active[1] and
                        not content[marker.end():].strip()):
                    active = None
                continue
        if marker:
            token = marker.group(1)
            # CommonMark backtick fences cannot contain backticks in their
            # opening info string. An invalid opener is ordinary prose, and
            # must not hide following real links or claim markers until EOF.
            if token[0] != "`" or "`" not in content[marker.end():]:
                active = (token[0], len(token), depth)
                continue
        if content.startswith(("    ", "\t")):
            continue
        yield line, start


def markdown_links_prose(text: str) -> str:
    """Mask escaped punctuation and inline code before parsing link definitions.

    Preserve newlines so multiline code spans cannot create fake definitions.
    Only the documented link subset is recognized; never treat samples as
    authoritative cross-file dependencies.
    """
    escaped = list(text)
    punctuation = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    i = 0
    while i + 1 < len(text):
        if text[i] == "\\" and text[i + 1] in punctuation:
            escaped[i] = " "
            escaped[i + 1] = " "
            i += 2
        else:
            i += 1
    masked = "".join(escaped)
    return INLINE_CODE.sub(
        lambda match: "".join("\n" if char == "\n" else " "
                              for char in match.group(0)), masked)


def _digest(path: Path, root: Path) -> tuple[str, int]:
    """Hash only through the already selected local directory tree.

    Resolve every directory component with O_NOFOLLOW. A replacement between
    link checking and hashing must refuse, never read an outside attachment.
    """
    relative = path.relative_to(root)
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for part in root.absolute().parts[1:] + relative.parts[:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        source = os.open(relative.parts[-1], os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=fd)
        digest, count = hashlib.sha256(), 0
        with os.fdopen(source, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise OSError("attachment is not a regular file")
            for block in iter(lambda: stream.read(1048576), b""):
                digest.update(block)
                count += len(block)
        return digest.hexdigest(), count
    finally:
        os.close(fd)


def _error(code: str, number: int = 0, line: int = 0) -> dict:
    return {"code": code, "link": number, "line": line}


def _target(root: Path, raw: str) -> tuple[str, Path | None]:
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]
    if not raw or raw.startswith("#"):
        return "anchor", None
    if "\\" in raw or "\x00" in raw:
        return "unsafe", None
    try:
        parsed = urlsplit(raw)
    except ValueError:
        return "unsafe", None
    if parsed.scheme in {"http", "https"} and parsed.netloc:
        return "external", None
    if parsed.scheme or parsed.netloc or parsed.query:
        return "unsafe", None
    decoded = unquote(parsed.path)
    if not decoded or "\x00" in decoded or "\\" in decoded or "%" in decoded:
        return "unsafe", None
    rel = PurePosixPath(decoded)
    if rel.is_absolute() or not rel.parts or ".." in rel.parts:
        return "unsafe", None
    dest = root.joinpath(*rel.parts)
    cursor = root
    for part in rel.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            return "symlink", None
    try:
        resolved = dest.resolve(strict=True)
        if root.resolve(strict=True) not in resolved.parents:
            return "unsafe", None
        if not resolved.is_file():
            return "not_file", None
    except (OSError, ValueError):
        return "missing", None
    return "local", resolved


def audit(batch: Path) -> dict:
    """Return stable JSON diagnostics without reading outside the batch."""
    report = {
        "status": "FAIL", "batch_sha256": None, "links_seen": 0,
        "local_files": [], "external_links": 0, "errors": [],
        "limits": {"batch_bytes": MAX_BATCH_BYTES},
        "note": "Attachment integrity only; not factual, licensing or approval verification",
    }
    if batch.is_symlink():
        report["errors"].append(_error("batch_symlink"))
        return report
    try:
        with batch.open("rb") as stream:
            raw = stream.read(MAX_BATCH_BYTES + 1)
        if len(raw) > MAX_BATCH_BYTES:
            report["errors"].append(_error("batch_too_large"))
            return report
        text = raw.decode("utf-8")
        report["batch_sha256"] = hashlib.sha256(raw).hexdigest()
    except (OSError, UnicodeError):
        report["errors"].append(_error("batch_unreadable"))
        return report

    root, seen = batch.parent, set()
    # Filter fenced/indented code once, then mask escaped punctuation and
    # multiline inline code on the WHOLE remaining text (R09's same parser).
    # The mask preserves character widths and physical line boundaries, so
    # each line can still be traced to its untrusted input without echoing it.
    visible = list(visible_markdown_lines(text))
    prose = markdown_links_prose("".join(line for line, _ in visible))
    previous_start, line_num, offset = 0, 1, 0
    for line, start in visible:
        # splitlines agrees with visible_markdown_lines on LF/CRLF/CR and
        # other supported line separators; counting only "\\n" did not.
        line_num += len(text[previous_start:start].splitlines())
        previous_start = start
        clean_line = prose[offset:offset + len(line)]
        offset += len(line)
        for match in INLINE_LINK.finditer(clean_line):
            report["links_seen"] += 1
            number = report["links_seen"]
            status, dest = _target(root, match.group(1))
            if status == "external":
                report["external_links"] += 1
            elif status in {"anchor", "local"}:
                if dest is None or dest in seen:
                    continue
                seen.add(dest)
                try:
                    digest, size = _digest(dest, root.resolve())
                    report["local_files"].append({
                        "link": number, "line": line_num,
                        "sha256": digest, "bytes": size
                    })
                except (OSError, ValueError):
                    report["errors"].append(_error("attachment_unreadable", number, line_num))
            else:
                report["errors"].append(_error(status, number, line_num))
    report["status"] = "PASS" if not report["errors"] else "FAIL"
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read-only R06 batch preflight")
    parser.add_argument("--batch", required=True, help="Path to a material batch.md")
    args = parser.parse_args(argv)
    result = audit(Path(args.batch))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
