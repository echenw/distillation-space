#!/usr/bin/env python3
"""R09 read-only quality checks: material claims, generated Skill, paired task evidence.

This is NOT a model, a knowledge writer, an approval authority, or a trusted
host observer. It checks bytes and declared observations; semantic truth and
agent invocation require independent verification.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, unquote

import kd_material_ops as normalization
import kd_skill_metadata as metadata
from kd_material_audit import markdown_links_prose, visible_markdown_lines

MAX_TEXT = normalization.LIMIT  # share the normalized-unit input ceiling with R03
MAX_MANIFEST = 2 * 1024 * 1024
MAX_TOTAL = 32 * 1024 * 1024
ID = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,63}$")
REF = re.compile(r"(?<![\w./])(?:references|scripts|assets|templates)/[A-Za-z0-9._/-]+")
SHA256 = re.compile(r"^[a-f0-9]{64}$")
MD_LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+[^)]*)?\)")
MD_REF_DEF = re.compile(r"^ {0,3}\[([^\]\n]+)\]:[ \t]*(<[^>\n]+>|[^\s<>\n]+)")
MD_REF_USE = re.compile(r"!?\[([^\]\n]+)\]\[([^\]\n]*)\]")
MD_BRACKET = re.compile(r"!?\[([^\]\n]+)\]")
ARMS = {"none", "baseline", "candidate"}
KINDS = {"positive", "negative", "boundary", "safety"}


class Invalid(Exception):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def require(ok: bool, code: str) -> None:
    if not ok:
        raise Invalid(code)


def obj(v, code: str) -> dict:
    require(type(v) is dict, code)
    return v


def items(v, code: str) -> list:
    require(type(v) is list, code)
    return v


def safe_id(v) -> str:
    require(type(v) is str and ID.fullmatch(v) is not None, "INVALID_ID")
    return v


def read_data(path: Path, limit: int = MAX_MANIFEST) -> bytes:
    require(not path.is_symlink() and path.is_file(), "INPUT_UNREADABLE")
    require(path.stat().st_size <= limit, "INPUT_TOO_LARGE")
    with path.open("rb") as stream:
        raw = stream.read(limit + 1)
    require(len(raw) <= limit, "INPUT_TOO_LARGE")
    return raw


def parse_json(raw: bytes):
    def no_duplicate_pairs(pairs):
        data = {}
        for key, value in pairs:
            require(key not in data, "DUPLICATE_JSON_KEY")
            data[key] = value
        return data
    try:
        parsed = json.loads(
            raw.decode("utf-8"), object_pairs_hook=no_duplicate_pairs,
            parse_constant=normalization.reject_nonstandard_json_constant,
            parse_float=normalization.parse_finite_json_float)
        normalization.require_json_utf8(parsed)
        return parsed
    except (UnicodeError, ValueError, RecursionError) as exc:
        # A byte-size limit does not bound JSON nesting. Normalize parser
        # recursion failures to the same stable invalid-input error.
        raise Invalid("INVALID_JSON") from exc


def read_json(path: Path):
    return parse_json(read_data(path))


def local(root: Path, rel: str, *, existing: bool = True) -> Path:
    """Resolve strict relative paths without traversing *any* symlink."""
    require(type(rel) is str and rel and not rel.startswith("/") and "\\" not in rel and
            "\x00" not in rel, "UNSAFE_PATH")
    parts = PurePosixPath(rel).parts
    require(parts and all(p not in {"..", ".", ""} for p in parts), "UNSAFE_PATH")
    cur = root
    for part in parts:
        cur = cur / part
        require(not cur.is_symlink(), "SYMLINK_PATH")
    if existing:
        require(cur.is_file(), "FILE_MISSING")
    require(root.resolve() == cur.resolve() or root.resolve() in cur.resolve().parents,
            "PATH_ESCAPE")
    return cur


def skill_digest(skill: Path) -> str:
    """Hash the entire Skill tree, including scripts and references."""
    require(skill.is_dir() and not skill.is_symlink(), "SKILL_DIR_INVALID")
    digest = hashlib.sha256()
    total, count = 0, 0
    for base, dirs, names in normalization.walk_source_tree(skill):
        dirs.sort()
        for name in dirs + names:
            require(not (Path(base) / name).is_symlink(), "SKILL_SYMLINK")
        for name in sorted(names):
            path = Path(base) / name
            require(path.is_file(), "SKILL_NON_FILE")
            raw = read_data(path, MAX_TEXT)
            total += len(raw)
            count += 1
            require(total <= MAX_TOTAL and count <= 500, "SKILL_TREE_TOO_LARGE")
            rel = path.relative_to(skill).as_posix().encode("utf-8")
            digest.update(len(rel).to_bytes(4, "big"))
            digest.update(rel)
            digest.update(bytes.fromhex(sha(raw)))
    return digest.hexdigest()





def source_links(skill: Path, path: Path, content: str) -> set[str]:
    """Check live inline and reference-style links, excluding Markdown code."""
    checked: set[str] = set()
    # A single tokenization pass must precede both definition collection and
    # link uses. Otherwise multiline inline-code text can lend false authority
    # to a later reference label.
    raw_lines = []
    definitions: dict[str, str] = {}

    def label_key(value: str) -> str:
        return " ".join(value.split()).casefold()

    for line, _offset in visible_markdown_lines(content):
        while True:
            quote = re.match(r"^ {0,3}>[ \t]?", line)
            if quote is None:
                break
            line = line[quote.end():]
        raw_lines.append(line)
    prose = "".join(raw_lines)
    clean = markdown_links_prose(prose)
    link_lines = []
    for line in clean.splitlines(keepends=True):
        definition = MD_REF_DEF.match(line)
        if definition:
            # Unused definitions impose no dependency; the first real
            # definition is authoritative if a label is repeated.
            definitions.setdefault(label_key(definition.group(1)), definition.group(2))
        else:
            link_lines.append(line)
    links = "".join(link_lines)

    def check_target(raw: str) -> None:
        raw = raw.strip("<>")
        if raw.startswith("#"):
            return
        parsed = urlsplit(raw)
        if parsed.scheme in {"https", "http"} and parsed.netloc:
            return
        require(not parsed.scheme and not parsed.netloc and not parsed.query and
                "%" not in raw and "\\" not in raw, "UNSAFE_REFERENCE")
        dest = (path.parent / unquote(parsed.path)).resolve(strict=False)
        try:
            rel = dest.relative_to(skill.resolve())
        except ValueError as exc:
            raise Invalid("REFERENCE_ESCAPE") from exc
        local(skill, rel.as_posix())
        checked.add(rel.as_posix())

    # Plain file-like words in References often document upstream examples,
    # not dependencies. Only the entrypoint promises bare root-relative paths.
    if path.name == "SKILL.md":
        for match in REF.finditer(prose):
            rel = match.group(0).rstrip(".,;:)")
            local(skill, rel)
            checked.add(rel)
    # The entrypoint's bare scripts/ references above remain real promises,
    # including paths shown in inline code; nested Markdown uses the filtered
    # text for linked dependencies.
    inline = list(MD_LINK.finditer(links))
    for match in inline:
        check_target(match.group(1))
    full = list(MD_REF_USE.finditer(links))
    for match in full:
        key = label_key(match.group(2) or match.group(1))
        require(key in definitions, "REFERENCE_LABEL_MISSING")
        check_target(definitions[key])
    # [name] is a shortcut reference only when a matching definition exists.
    # Do not count the brackets inside a full/collapsed/inline link twice.
    occupied = [match.span() for match in inline + full]
    for match in MD_BRACKET.finditer(links):
        if any(start < match.end() and match.start() < end for start, end in occupied):
            continue
        key = label_key(match.group(1))
        if key in definitions:
            check_target(definitions[key])
    return checked


def result(kind: str, work) -> dict:
    try:
        return work()
    except (Invalid, OSError, ValueError, UnicodeError, SyntaxError) as exc:
        # Code only; never print exception text or source/claim contents.
        code = exc.code if isinstance(exc, Invalid) else "IO_OR_ENCODING_ERROR"
        return {"check": kind, "status": "FAIL", "errors": [code]}


def claim_prose(body: str) -> str:
    """Mask code while preserving offsets for external dossier anchors."""
    parts = []
    end = 0
    for line, offset in visible_markdown_lines(body):
        parts.extend((" " * (offset - end), line))
        end = offset + len(line)
    parts.append(" " * (len(body) - end))
    prose = markdown_links_prose("".join(parts))
    return re.sub(r"<!--.*?-->", lambda match: " " * len(match.group(0)), prose,
                  flags=re.S)


def final_provenance_errors(root: Path) -> list[str]:
    """Recognize explicit intermediate records, not arbitrary literary attribution.

    Names, quotations and disguised citations still need R18's semantic review.
    This is used for generated final artifacts, not the compiler's own manual.
    """
    errors = set()
    for base, dirs, names in normalization.walk_source_tree(root):
        for name in dirs + names:
            require(not (Path(base) / name).is_symlink(), "SKILL_SYMLINK")
        for name in names:
            path = Path(base) / name
            if path.stem.casefold() in {"source-index", "source_index", "bibliography",
                                       "dossier", "来源索引", "书目"}:
                errors.add("FINAL_SOURCE_RECORD_FORBIDDEN")
            if b"R13-CLAIM:" in read_data(path, MAX_TEXT):
                errors.add("FINAL_CLAIM_MARKER_FORBIDDEN")
    return sorted(errors)


def validate_json_source_anchor(anchor: str) -> None:
    """Check the declared R03 chat locator format, not the source's authenticity."""
    # R03 partitions an oversized text into exact, ordered fragments. A suffix
    # must not allow a malformed JSON/chat identity to masquerade as valid.
    try:
        anchor = normalization.source_anchor_base(anchor)
    except normalization.Invalid as exc:
        raise Invalid("SOURCE_ANCHOR_FORMAT_INVALID") from exc
    if anchor == "json:root":
        return
    prefix = "chat:v1:"
    require(anchor.startswith(prefix), "SOURCE_ANCHOR_FORMAT_INVALID")
    try:
        parts = json.loads(anchor[len(prefix):])
    except (json.JSONDecodeError, UnicodeError, RecursionError) as exc:
        # The 4096-character bound still permits JSON deeper than Python's
        # parser limit. Malformed source metadata must return a stable FAIL.
        raise Invalid("SOURCE_ANCHOR_FORMAT_INVALID") from exc
    require(type(parts) is list and len(parts) == 2 and
            all(type(p) is list and len(p) == 2 and
                type(p[0]) is str and type(p[1]) is str
                for p in parts), "SOURCE_ANCHOR_FORMAT_INVALID")
    conversation, message = parts
    require(conversation[0] in {"id", "index"} and
            message[0] in {"id", "index", "node"},
            "SOURCE_ANCHOR_FORMAT_INVALID")
    for label, value in parts:
        if label == "id":
            require(bool(value.strip()), "SOURCE_ANCHOR_FORMAT_INVALID")
        elif label == "index":
            require(re.fullmatch(r"0|[1-9][0-9]*", value) is not None,
                    "SOURCE_ANCHOR_FORMAT_INVALID")
        # Check decoded identifiers, not the JSON-escaped locator. R03 owns
        # this exact private-ID policy; translate its domain exception to the
        # R09 error envelope without echoing untrusted identifier contents.
        try:
            normalization.require_nonprivate_chat_identity(value)
        except normalization.Invalid as exc:
            raise Invalid(exc.code) from exc
    # R03's single encoder is the owner of wire-format serialization; do not
    # accept whitespace, alternate escaping, or legacy colon-joined locators.
    require(normalization.chat_anchor(conversation, message) == anchor,
            "SOURCE_ANCHOR_FORMAT_INVALID")


def validate_lineage(row: dict, material_sha: str) -> bool:
    """Require a declared direct origin or one exact R03 unit; never authenticate origin.

    Returns True when the external extractor's version cannot be established.
    A curated/transformed source cannot silently inherit the identity of its
    derived UTF-8 bytes; the upstream host must still verify the source claim.
    """
    lineage = row.get("lineage")
    require(type(lineage) is dict, "SOURCE_LINEAGE_MISSING")
    kind = lineage.get("kind")
    require(kind in ("direct", "normalized"), "SOURCE_LINEAGE_KIND_INVALID")
    if kind == "direct":
        require(set(lineage) == {"kind"}, "SOURCE_DIRECT_LINEAGE_INVALID")
        return False
    required = ("source_sha256", "normalizer_version", "extractor", "extractor_version",
                "extracted_text_sha256", "source_anchor", "unit_sha256", "output_sha256",
                "redacted")
    require(all(field in lineage for field in required), "SOURCE_LINEAGE_INCOMPLETE")
    require(all(type(lineage[field]) is str and SHA256.fullmatch(lineage[field])
                for field in ("source_sha256", "extracted_text_sha256", "unit_sha256",
                              "output_sha256")), "SOURCE_LINEAGE_DIGEST_INVALID")
    require(lineage["normalizer_version"] == normalization.NORMALIZER_VERSION and
            lineage["extractor"] in normalization.EXTRACTORS.values(),
            "SOURCE_NORMALIZER_UNSUPPORTED")
    anchor = lineage["source_anchor"]
    try:
        normalization.source_anchor_base(anchor)
    except normalization.Invalid as exc:
        raise Invalid("SOURCE_ANCHOR_INVALID") from exc
    if lineage["extractor"] == normalization.EXTRACTORS["json"]:
        validate_json_source_anchor(anchor)
    require(type(lineage["redacted"]) is bool, "SOURCE_REDACTION_INVALID")
    require(lineage["output_sha256"] == material_sha and
            (lineage["redacted"] or lineage["unit_sha256"] == material_sha),
            "SOURCE_LINEAGE_OUTPUT_MISMATCH")
    version = lineage["extractor_version"]
    require(version is None or (type(version) is str and bool(version.strip()) and
            len(version) <= 160), "SOURCE_EXTRACTOR_VERSION_INVALID")
    return version is None


def material_audit(root: Path, dossier: Path, skill: Path) -> dict:
    """Verify declared coverage and exact quotation bytes, NOT semantic support."""
    require(skill.is_dir() and not skill.is_symlink(), "SKILL_DIR_INVALID")
    require(not dossier.resolve().is_relative_to(skill.resolve()), "DOSSIER_IN_SKILL")
    data = obj(read_json(dossier), "DOSSIER_NOT_OBJECT")
    require(type(data.get("version")) is int, "DOSSIER_VERSION")
    require(data.get("version") != 1, "DOSSIER_V1_LINEAGE_NOT_PROVEN")
    require(data.get("version") == 2, "DOSSIER_VERSION")
    require(root.is_dir() and not root.is_symlink(), "MATERIAL_ROOT_INVALID")
    source_rows = items(data.get("sources"), "SOURCES_MISSING")
    windows = items(data.get("windows"), "WINDOWS_MISSING")
    claims = items(data.get("claims"), "CLAIMS_MISSING")
    conflicts = items(data.get("conflicts", []), "CONFLICTS_INVALID")
    require(source_rows and claims and windows, "EMPTY_DOSSIER")
    all_files: set[str] = set()
    for base, dirs, files in normalization.walk_source_tree(root):
        for name in dirs + files:
            p = Path(base) / name
            require(not p.is_symlink(), "SOURCE_SYMLINK")
        for name in files:
            p = Path(base) / name
            if p.resolve() == dossier.resolve():
                continue
            all_files.add(p.relative_to(root).as_posix())
    sources: dict[str, dict] = {}
    source_paths: set[str] = set()
    normalized_units: set[tuple[str, str]] = set()
    lineage_version_gaps: list[str] = []
    total = 0
    for source in source_rows:
        source = obj(source, "SOURCE_INVALID")
        sid = safe_id(source.get("id"))
        require(sid not in sources, "SOURCE_ID_DUPLICATE")
        if "material_id" in source:
            safe_id(source["material_id"])  # kd_incremental.py verifies the frozen R01 snapshot binding.
        rel = source.get("path")
        f = local(root, rel)
        require(rel not in source_paths, "SOURCE_PATH_DUPLICATE")
        require(f.stat().st_size <= MAX_TEXT, "SOURCE_TOO_LARGE")
        raw = read_data(f, MAX_TEXT)
        total += len(raw)
        require(total <= MAX_TOTAL, "MATERIAL_TOTAL_TOO_LARGE")
        actual_sha = sha(raw)
        require(actual_sha == source.get("sha256"), "SOURCE_CHANGED")
        if validate_lineage(source, actual_sha):
            lineage_version_gaps.append(sid)
        lineage = source["lineage"]
        if lineage["kind"] == "normalized":
            # Paths and source IDs are dossier-local aliases, not independent
            # evidence identities. One R03 unit can appear only once even if
            # it is copied into multiple files or output redaction variants.
            unit_key = (lineage["source_sha256"], lineage["source_anchor"])
            require(unit_key not in normalized_units, "SOURCE_UNIT_DUPLICATE")
            normalized_units.add(unit_key)
        text = raw.decode("utf-8")
        lines = text.splitlines(keepends=True)
        require(type(source.get("lines")) is int and source["lines"] == len(lines), "SOURCE_LINE_COUNT")
        sources[sid] = {"path": rel, "lines": lines, "covered": set()}
        source_paths.add(rel)
    require(source_paths == all_files, "SOURCE_INVENTORY_INCOMPLETE")
    for window in windows:
        window = obj(window, "WINDOW_INVALID")
        sid = safe_id(window.get("source_id"))
        require(sid in sources, "WINDOW_SOURCE_MISSING")
        entry = sources[sid]
        start, end = window.get("start"), window.get("end")
        require(type(start) is int and type(end) is int and
                1 <= start <= end <= len(entry["lines"]), "WINDOW_BOUNDS")
        excerpt = "".join(entry["lines"][start - 1:end]).encode("utf-8")
        require(sha(excerpt) == window.get("sha256"), "WINDOW_HASH_MISMATCH")
        entry["covered"].update(range(start, end + 1))
    rules: set[str] = set()
    forbidden = final_provenance_errors(skill)
    if forbidden:
        raise Invalid(forbidden[0])
    targets: set[tuple[str, str]] = set()
    local(skill, "SKILL.md")
    for claim in claims:
        claim = obj(claim, "CLAIM_INVALID")
        rid = safe_id(claim.get("id"))
        require(rid not in rules, "CLAIM_DUPLICATE")
        rules.add(rid)
        for key in ("assertion", "applicability", "limitations", "skill_anchor"):
            require(type(claim.get(key)) is str and claim[key].strip(), "CLAIM_FIELD_MISSING")
        target = claim.get("skill_path", "SKILL.md")
        file_path = local(skill, target)
        target = file_path.relative_to(skill).as_posix()
        body = read_data(file_path, MAX_TEXT).decode("utf-8")
        anchor, assertion = claim["skill_anchor"], claim["assertion"]
        require(anchor in body, "SKILL_RULE_ANCHOR_MISSING")
        require(body.find(anchor, body.index(anchor) + 1) == -1, "SKILL_RULE_ANCHOR_AMBIGUOUS")
        require(assertion in anchor, "CLAIM_TEXT_NOT_IN_SKILL")
        start = body.index(anchor) + anchor.index(assertion)
        require(re.search(r"[^\W_]", claim_prose(body)[start:start + len(assertion)]) is not None,
                "SKILL_RULE_ANCHOR_NOT_PROSE")
        require((target, anchor) not in targets, "CLAIM_TARGET_DUPLICATE")
        targets.add((target, anchor))
        evidences = items(claim.get("evidence"), "CLAIM_EVIDENCE_MISSING")
        require(evidences, "CLAIM_EVIDENCE_MISSING")
        for ref in evidences:
            ref = obj(ref, "CLAIM_REF_INVALID")
            sid = safe_id(ref.get("source_id"))
            require(sid in sources, "CLAIM_SOURCE_MISSING")
            entry = sources[sid]
            start, end = ref.get("start"), ref.get("end")
            require(type(start) is int and type(end) is int and
                    1 <= start <= end <= len(entry["lines"]), "CLAIM_LINE_BOUNDS")
            require(set(range(start, end + 1)) <= entry["covered"], "CLAIM_UNREAD_WINDOW")
            quotation = ref.get("quote")
            require(type(quotation) is str and quotation.strip(), "CLAIM_QUOTE_MISSING")
            source_slice = "".join(entry["lines"][start - 1:end])
            require(quotation in source_slice and sha(quotation.encode("utf-8")) ==
                    ref.get("quote_sha256"), "CLAIM_QUOTE_UNSUPPORTED")
    unresolved = 0
    for conflict in conflicts:
        conflict = obj(conflict, "CONFLICT_INVALID")
        ids = conflict.get("source_ids")
        require(type(ids) is list and len(ids) >= 2 and
                all(type(sid) is str and ID.fullmatch(sid) is not None and
                    sid in sources for sid in ids) and
                len(set(ids)) >= 2, "CONFLICT_SOURCES")
        status = conflict.get("status")
        require(type(status) is str and
                status in {"UNRESOLVED", "RESOLVED", "VERSIONED"},
                "CONFLICT_STATUS")
        require(type(conflict.get("reason")) is str and conflict["reason"].strip(),
                "CONFLICT_REASON")
        unresolved += status == "UNRESOLVED"
    covered = sum(len(e["covered"]) for e in sources.values())
    line_total = sum(len(e["lines"]) for e in sources.values())
    full = covered == line_total and line_total > 0
    complete = full and not unresolved and not lineage_version_gaps
    verdict = "STRUCTURE_VALID_SEMANTICS_UNPROVEN" if complete else "NOT_PROVEN"
    return {
        "check": "material", "status": "PASS" if complete else "FAIL",
        "verdict": verdict, "sources": len(sources), "claims": len(rules),
        "covered_lines": covered, "total_lines": line_total,
        "uncovered_lines": line_total - covered, "unresolved_conflicts": unresolved,
        "unknown_extractor_version_sources": sorted(lineage_version_gaps),
        "original_source_attestation": "NOT_AVAILABLE",
        "semantic_validation": "NOT_RUN", "host_read_attestation": "NOT_AVAILABLE",
        "note": "Declared source-window bytes checked; neither actual host reading nor inference correctness proven",
    }


def yaml_mapping_entry(line: str, code: str) -> tuple[str, str]:
    try:
        return metadata.mapping_entry(line)
    except metadata.MetadataError as exc:
        raise Invalid(code) from exc


def yaml_string_scalar(raw: str, code: str) -> str:
    try:
        return metadata.string_scalar(raw)
    except metadata.MetadataError as exc:
        raise Invalid(code) from exc


def chatgpt_interface_labels(text: str) -> dict[str, str]:
    """Read required scalar labels from a block-style UI mapping, not comments.

    The distributed validator has no YAML dependency. Reject unsupported label
    shapes instead of mistaking a keyword in a comment for real host metadata.
    Other root mappings (e.g. policy) do not grant or change these labels.
    """
    section = None
    interface_lines: list[tuple[int, str]] = []
    found = False
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        require("\t" not in line[:len(line) - len(line.lstrip())],
                "SKILL_HOST_METADATA_INVALID")
        indentation = len(line) - len(line.lstrip(" "))
        if indentation == 0:
            section, raw = yaml_mapping_entry(line, "SKILL_HOST_METADATA_INVALID")
            if section == "interface":
                require(not found and (not raw.strip() or
                        raw.lstrip().startswith("#")), "SKILL_HOST_METADATA_INVALID")
                found = True
        elif section == "interface":
            interface_lines.append((indentation, line[indentation:]))
    require(found and interface_lines, "SKILL_HOST_METADATA_INVALID")
    level = min(indent for indent, _ in interface_lines)
    labels: dict[str, str] = {}
    for indent, line in interface_lines:
        if indent != level:
            continue
        key, raw = yaml_mapping_entry(line, "SKILL_HOST_METADATA_INVALID")
        require(key not in labels, "SKILL_HOST_METADATA_INVALID")
        if key not in {"display_name", "short_description"}:
            continue
        labels[key] = yaml_string_scalar(raw, "SKILL_HOST_METADATA_INVALID")
    require(set(labels) == {"display_name", "short_description"},
            "SKILL_HOST_METADATA_INVALID")
    return labels


def skill_audit(skill: Path, host: str) -> dict:
    require(skill.is_dir() and not skill.is_symlink(), "SKILL_DIR_INVALID")
    files: list[Path] = []
    for base, dirs, names in normalization.walk_source_tree(skill):
        for name in dirs + names:
            require(not (Path(base) / name).is_symlink(), "SKILL_SYMLINK")
            require(name not in {".git", ".DS_Store", "__pycache__", ".venv", ".env"} and
                    not name.endswith((".pyc", ".pyo", ".key")), "SKILL_JUNK_OR_SECRET_FILE")
        for name in names:
            files.append(Path(base) / name)
    require(files and len(files) <= 500, "SKILL_FILE_COUNT")
    entry = read_data(local(skill, "SKILL.md"), MAX_TEXT).decode("utf-8")
    try:
        fields = metadata.parse_frontmatter(entry)
    except metadata.MetadataError as exc:
        raise Invalid("SKILL_" + exc.code) from exc
    require(fields["name"] == skill.name, "SKILL_NAME_INVALID")
    if host == "chatgpt":
        meta = read_data(local(skill, "agents/openai.yaml"), MAX_TEXT).decode("utf-8")
        chatgpt_interface_labels(meta)
    lines = entry.splitlines()
    require(any(line.strip() for line in lines[metadata.frontmatter_end(lines) + 1:]),
            "SKILL_BODY_EMPTY")
    checked: set[str] = set()
    for f in files:
        if f.suffix == ".md":
            checked.update(source_links(skill, f, read_data(f, MAX_TEXT).decode("utf-8")))
    compiled = 0
    for f in files:
        if f.suffix == ".py":
            require(f.stat().st_size <= MAX_TEXT, "SKILL_SCRIPT_TOO_LARGE")
            compile(read_data(f, MAX_TEXT), f.name, "exec")
            compiled += 1
    return {
        "check": "skill", "status": "PASS", "verdict": "STATIC_STRUCTURE_VALID",
        "files": len(files), "references_checked": len(checked),
        "python_scripts_compiled": compiled, "host": host,
        "skill_tree_sha256": skill_digest(skill),
        "host_task_execution": "NOT_RUN", "note": "No script executed; no Skill selection or effect observed",
    }


def compare(oracle_file: Path, manifest_file: Path, outputs_root: Path,
            baseline: Path, candidate: Path, *, operation: str = "update") -> dict:
    oracle_raw = read_data(oracle_file)
    oracle = obj(parse_json(oracle_raw), "ORACLE_INVALID")
    data = obj(read_json(manifest_file), "COMPARISON_INVALID")
    require(type(oracle.get("version")) is int and type(data.get("version")) is int and
            oracle["version"] == data["version"] == 1, "COMPARISON_VERSION")
    require(sha(oracle_raw) == data.get("oracle_sha256"), "ORACLE_DRIFT")
    mode = data.get("mode")
    require(type(mode) is str and mode in {"fixture", "host_reported"},
            "COMPARISON_MODE")
    recorded_operation = data.get("operation", "update")
    require(type(operation) is str and operation in {"create", "update"} and
            type(recorded_operation) is str and recorded_operation == operation,
            "COMPARISON_OPERATION")
    if operation == "create":
        require(baseline is None, "CREATE_BASELINE_NOT_ALLOWED")
        require("baseline_tree_sha256" in data and
                data["baseline_tree_sha256"] is None, "CREATE_BASELINE_INVALID")
        arms = ARMS - {"baseline"}
    else:
        require(baseline is not None, "UPDATE_BASELINE_REQUIRED")
        require((baseline / "SKILL.md").is_file(), "BASELINE_SKILL_MISSING")
        require(data.get("baseline_tree_sha256") == skill_digest(baseline),
                "SKILL_VERSION_DRIFT")
        arms = ARMS
    require((candidate / "SKILL.md").is_file(), "CANDIDATE_SKILL_MISSING")
    require(data.get("candidate_tree_sha256") == skill_digest(candidate),
            "SKILL_VERSION_DRIFT")
    cases: dict[str, dict] = {}
    for case in items(oracle.get("cases"), "ORACLE_CASES"):
        c = obj(case, "ORACLE_CASE_INVALID")
        cid = safe_id(c.get("id"))
        expected_files = c.get("expected_files", [])
        require(type(expected_files) is list, "ORACLE_CASE_INVALID")
        case_kind = c.get("kind")
        require(cid not in cases and type(case_kind) is str and
                case_kind in KINDS and
                type(c.get("should_trigger")) is bool and
                "expected_stdout" in c and
                (type(c["expected_stdout"]) is str or
                 (c["expected_stdout"] is None and bool(expected_files))) and
                type(c.get("expected_exit")) is int, "ORACLE_CASE_INVALID")
        cases[cid] = c
    require(cases and set(c["kind"] for c in cases.values()) >= KINDS,
            "ORACLE_COVERAGE_INCOMPLETE")
    observations: dict[tuple[str, str], bool] = {}
    for run in items(data.get("runs"), "COMPARISON_RUNS"):
        run = obj(run, "RUN_INVALID")
        cid = safe_id(run.get("case_id"))
        arm = run.get("arm")
        require(cid in cases and type(arm) is str and arm in arms,
                "RUN_CASE_OR_ARM")
        key = (cid, arm)
        require(key not in observations, "DUPLICATE_OBSERVATION")
        require(type(run.get("exit_code")) is int and
                type(run.get("skill_invoked")) is bool and
                type(run.get("duration_ms")) is int and run["duration_ms"] >= 0,
                "RUN_METADATA_INVALID")
        require(run.get("environment") == data.get("environment") and
                type(run["environment"]) is dict and bool(run["environment"]),
                "RUN_ENV_DRIFT")
        stdout = read_data(local(outputs_root, run.get("stdout")), MAX_TEXT)
        require(sha(stdout) == run.get("stdout_sha256"), "OBSERVATION_TAMPERED")
        expected = cases[cid]
        triggered = run["skill_invoked"]
        right_trigger = not triggered if arm == "none" else triggered == expected["should_trigger"]
        artifacts_correct = True
        for artifact in expected.get("expected_files", []):
            artifact = obj(artifact, "EXPECTED_FILE_INVALID")
            rel = artifact.get("path")
            digest = artifact.get("sha256")
            require(type(rel) is str and type(digest) is str and
                    bool(re.fullmatch(r"[a-f0-9]{64}", digest)), "EXPECTED_FILE_INVALID")
            folder = run.get("artifact_dir")
            require(type(folder) is str and folder, "ARTIFACT_DIR_MISSING")
            actual = read_data(local(outputs_root, folder + "/" + rel), MAX_TEXT)
            artifacts_correct &= sha(actual) == digest
        correct = ((expected["expected_stdout"] is None or
                    stdout == expected["expected_stdout"].encode("utf-8")) and
                   artifacts_correct and run["exit_code"] == expected["expected_exit"] and
                   right_trigger)
        observations[key] = correct
    require(len(observations) == len(cases) * len(arms) and
            all((cid, arm) in observations for cid in cases for arm in arms),
            "PAIRED_RUNS_INCOMPLETE")
    scores = {arm: sum(observations[(cid, arm)] for cid in cases) for arm in sorted(arms)}
    references = arms - {"candidate"}
    regression_counts = {
        arm: sum(observations[(cid, arm)] and not observations[(cid, "candidate")]
                 for cid in cases) for arm in references}
    regressions = sum(any(observations[(cid, arm)] for arm in references) and
                      not observations[(cid, "candidate")] for cid in cases)
    unsafe = sum(not observations[(cid, "candidate")] for cid, case in cases.items()
                 if case["kind"] in {"negative", "safety"})
    # A weak old Skill must not make a useless or harmful replacement look good.
    # Creation has no old version: compare directly against actual no-Skill runs.
    improvement = all(scores["candidate"] > scores[arm] for arm in references) and \
        regressions == 0 and unsafe == 0
    if data["mode"] == "fixture":
        verdict = "SIMULATION_ONLY"
    else:
        verdict = "HOST_REPORTED_UNAUTHENTICATED"
    return {
        "check": "compare", "status": "PASS" if improvement else "FAIL",
        "verdict": verdict, "operation": operation, "required_arms": sorted(arms),
        "oracle_sha256": sha(oracle_raw), "case_count": len(cases),
        "counts": scores, "regressions": regressions, "unsafe_failures": unsafe,
        "regressions_vs_none": regression_counts["none"],
        "regressions_vs_baseline": regression_counts.get("baseline"),
        "improvement_in_declared_observations": improvement,
        "host_attestation": "NOT_VERIFIED", "approval": "NOT_GRANTED",
        "note": "Deterministic oracle comparison only. Not proof of actual host execution or trusted approval",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="R09 read-only material/Skill/paired-run quality checks")
    subs = parser.add_subparsers(dest="check", required=True)
    m = subs.add_parser("material")
    m.add_argument("--materials", required=True)
    m.add_argument("--dossier", required=True)
    m.add_argument("--skill", required=True)
    sk = subs.add_parser("skill")
    sk.add_argument("--skill", required=True)
    sk.add_argument("--host", choices=("generic", "chatgpt"), default="generic")
    ab = subs.add_parser("compare")
    ab.add_argument("--operation", choices=("create", "update"), default="update")
    ab.add_argument("--baseline")
    for flag in ("oracle", "manifest", "outputs", "candidate"):
        ab.add_argument("--" + flag, required=True)
    args = parser.parse_args(argv)
    if args.check == "material":
        report = result("material", lambda: material_audit(
            Path(args.materials), Path(args.dossier), Path(args.skill)))
    elif args.check == "skill":
        report = result("skill", lambda: skill_audit(Path(args.skill), args.host))
    else:
        report = result("compare", lambda: compare(
            Path(args.oracle), Path(args.manifest), Path(args.outputs),
            Path(args.baseline) if args.baseline is not None else None,
            Path(args.candidate), operation=args.operation))
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
