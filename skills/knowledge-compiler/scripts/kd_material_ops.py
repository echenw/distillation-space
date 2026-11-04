#!/usr/bin/env python3
"""R03 read-only source normalization, privacy triage and relevance coverage.

All artifacts are stdout-only. An authorized host may separately persist reports
in the existing material round; this module has no writer, model or network.
"""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
import hashlib
import json
import math
import os
import stat
from decimal import Decimal, InvalidOperation
from pathlib import Path, PurePosixPath
import re
import sys
import shutil
import subprocess
import zipfile
from xml.etree import ElementTree as ET

LIMIT = 8 * 1024 * 1024
EXTRACTED_LIMIT = 12 * 1024 * 1024
PDF_TIMEOUT_SECONDS = 20
PDF_DIAGNOSTIC_LIMIT = 8192
BAD = {"unread", "unavailable"}
TAGS = {"relevant", "irrelevant", "unread", "unavailable"}
NORMALIZER_VERSION = "kd-material-ops/9"
EXTRACTORS = {"text": "utf8_text", "json": "json_chat_export",
              "html": "html_parser", "docx": "docx_document_xml",
              "pdf": "pdftotext"}
MAX_SOURCE_ANCHOR = 4096
# Every fragment contains at least one original byte. Its ordinal/count cannot
# exceed the extraction byte bound; appended identity does not consume base-ID space.
MAX_SOURCE_LOCATOR = MAX_SOURCE_ANCHOR + len(f":part:{EXTRACTED_LIMIT}-of-{EXTRACTED_LIMIT}")
TOKEN = re.compile(
    r"(?i)(?:\b(?:api[_-]?key|access[_-]?token|password|secret)\s*[:=]\s*"
    r"['\"]?[A-Za-z0-9_./+=-]{8,}|(?:sk-|ghp_|gho_|github_pat_)[A-Za-z0-9_-]{12,}"
    r"|\bAKIA[A-Z0-9]{16}\b)")
BEARER = re.compile(
    r"(?i)\bauthorization[ \t]*:[ \t]*bearer[ \t]+[A-Za-z0-9._~+/=-]+")
DB_USERINFO = re.compile(
    r"""(?i)\b(?:postgres|mongodb(?:\+srv)?|mysql)://[^\s/@"'<>]+@""")
PRIVATE_KEY = re.compile(
    r"-----BEGIN ((?:RSA |OPENSSH )?PRIVATE KEY)-----.*?-----END \1-----",
    re.DOTALL)
CREDENTIAL_PATTERNS = (TOKEN, BEARER, DB_USERINFO, PRIVATE_KEY)
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
LICENSE = re.compile(r"(?i)\b(?:SPDX-License-Identifier|All rights reserved|copyright|license)\b")


class Invalid(Exception):
    def __init__(self, code):
        self.code = code
        super().__init__(code)


def require(ok, code):
    if not ok:
        raise Invalid(code)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def reject_nonstandard_json_constant(literal):
    """Never accept Python's NaN/Infinity extensions to standard JSON."""
    raise ValueError("NONSTANDARD_JSON_CONSTANT")


def parse_finite_json_float(literal):
    """Preserve JSON decimal meaning when representing it as a Python float.

    R03 is the shared input owner for S09 and material normalization. Refuse
    tokens that would silently round or underflow: downstream consumers work
    with ordinary floats, not with a second Decimal JSON data model.
    """
    number = float(literal)
    if not math.isfinite(number):
        raise ValueError("NONFINITE_JSON_NUMBER")
    try:
        if Decimal(literal) != Decimal(str(number)):
            raise ValueError("LOSSY_JSON_NUMBER")
    except InvalidOperation as exc:
        raise ValueError("LOSSY_JSON_NUMBER") from exc
    return number


def require_json_utf8(value):
    """Reject escaped lone surrogates across JSON keys and values.

    R09 also calls this after its own duplicate-key-preserving JSON decoder,
    so one shared input owner decides whether decoded strings are encodable.
    """
    if isinstance(value, str):
        value.encode("utf-8")
    elif isinstance(value, dict):
        for key, item in value.items():
            key.encode("utf-8")
            require_json_utf8(item)
    elif isinstance(value, list):
        for item in value:
            require_json_utf8(item)


def strict_json(raw):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "DUPLICATE_JSON_FIELD")
            result[key] = value
        return result

    try:
        document = json.loads(raw.decode("utf-8"), object_pairs_hook=unique,
                              parse_constant=reject_nonstandard_json_constant,
                              parse_float=parse_finite_json_float)
        require_json_utf8(document)
        return document
    except (UnicodeError, ValueError, RecursionError) as exc:
        # Deeply nested but otherwise valid JSON must fail at this input
        # boundary, not bypass the CLI's machine-readable error protocol.
        raise Invalid("INVALID_JSON") from exc


def source_file(path: Path) -> bytes:
    require(path.is_file() and not path.is_symlink(), "SOURCE_UNAVAILABLE")
    fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW)
    with os.fdopen(fd, "rb") as stream:
        info = os.fstat(stream.fileno())
        require(stat.S_ISREG(info.st_mode), "SOURCE_UNAVAILABLE")
        require(info.st_size <= LIMIT, "SOURCE_TOO_LARGE")
        raw = stream.read(LIMIT + 1)
    require(len(raw) <= LIMIT, "SOURCE_TOO_LARGE")
    return raw


def walk_source_tree(root):
    """Enumerate a complete read-only tree, or propagate an I/O refusal.

    os.walk and Path.rglob otherwise suppress directory permission errors,
    which can turn a partial inventory into a false coverage/hash certificate.
    Consumers retain their own symlink, format and byte-budget contracts.
    """
    def refuse(error):
        raise error
    yield from os.walk(root, onerror=refuse, followlinks=False)


def text_from_html(data):
    class Extractor(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.skip = 0
            self.parts = []
        def handle_starttag(self, tag, attrs):
            if tag in {"script", "style", "svg"}:
                self.skip += 1
            elif not self.skip and tag in {"p", "br", "li", "h1", "h2", "h3", "tr"}:
                self.parts.append("\n")
        def handle_endtag(self, tag):
            if tag in {"script", "style", "svg"} and self.skip:
                self.skip -= 1
            elif not self.skip and tag in {"p", "li", "h1", "h2", "h3", "tr"}:
                self.parts.append("\n")
        def handle_data(self, data):
            if not self.skip:
                self.parts.append(data)
    extractor = Extractor()
    extractor.feed(data.decode("utf-8"))
    return "\n".join(p.strip() for p in "".join(extractor.parts).splitlines()
                     if p.strip())


def text_from_docx(raw):
    try:
        from io import BytesIO
        with zipfile.ZipFile(BytesIO(raw)) as archive:
            require(len(archive.infolist()) <= 1000, "DOCX_TOO_MANY_MEMBERS")
            meta = archive.getinfo("word/document.xml")
            require(meta.file_size <= EXTRACTED_LIMIT, "DOCX_DOCUMENT_TOO_LARGE")
            xml = archive.read("word/document.xml")
        root = ET.fromstring(xml)
    except (KeyError, zipfile.BadZipFile, ET.ParseError, RuntimeError,
            NotImplementedError) as exc:
        raise Invalid("INVALID_DOCX") from exc
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    paragraphs = []
    for paragraph in root.findall(".//w:p", ns):
        parts = []
        for item in paragraph.iter():
            if item.tag.endswith("}t") and item.text:
                parts.append(item.text)
            elif item.tag.endswith("}tab"):
                parts.append("\t")
            elif item.tag.endswith("}br"):
                parts.append("\n")
        if parts:
            paragraphs.append("".join(parts))
    return "\n".join(paragraphs)


def _run_pdf_tool(executable, source, *, version=False):
    """Feed one immutable source snapshot and capture bounded separate streams.

    The trusted local converter receives no source pathname to reopen. Its
    process group, elapsed time and both output streams remain bounded even
    for a broken converter or a highly compressed document.
    """
    import selectors
    import signal
    import time

    argv = ([executable, "-v"] if version else
            [executable, "-enc", "UTF-8", "-layout", "-", "-"])
    limits = {"stdout": PDF_DIAGNOSTIC_LIMIT if version else EXTRACTED_LIMIT,
              "stderr": PDF_DIAGNOSTIC_LIMIT}
    deadline = time.monotonic() + (5 if version else PDF_TIMEOUT_SECONDS)
    try:
        proc = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, bufsize=0, start_new_session=True)
    except OSError:
        raise Invalid("PDF_EXTRACTION_FAILED") from None
    chunks = {"stdout": [], "stderr": []}
    sizes = {"stdout": 0, "stderr": 0}
    offset = 0
    try:
        with selectors.DefaultSelector() as selector:
            for stream, label in ((proc.stdout, "stdout"), (proc.stderr, "stderr")):
                os.set_blocking(stream.fileno(), False)
                selector.register(stream, selectors.EVENT_READ, label)
            if source:
                os.set_blocking(proc.stdin.fileno(), False)
                selector.register(proc.stdin, selectors.EVENT_WRITE, "stdin")
            else:
                proc.stdin.close()
            while True:
                remaining = deadline - time.monotonic()
                require(remaining > 0, "PDF_EXTRACTION_TIMEOUT")
                for key, _ in selector.select(timeout=min(remaining, 0.2)):
                    stream, label = key.fileobj, key.data
                    try:
                        if label == "stdin":
                            written = os.write(proc.stdin.fileno(), source[offset:offset + 65536])
                            require(written > 0, "PDF_EXTRACTION_FAILED")
                            offset += written
                            if offset == len(source):
                                selector.unregister(stream)
                                stream.close()
                        else:
                            chunk = os.read(stream.fileno(), min(65536, limits[label] + 1 - sizes[label]))
                            if chunk:
                                sizes[label] += len(chunk)
                                require(sizes[label] <= limits[label], "PDF_OUTPUT_LIMIT")
                                chunks[label].append(chunk)
                            else:
                                selector.unregister(stream)
                                stream.close()
                    except BlockingIOError:
                        continue
                if not selector.get_map():
                    try:
                        proc.wait(timeout=min(0.2, max(0.001, deadline - time.monotonic())))
                        break
                    except subprocess.TimeoutExpired:
                        continue
        return subprocess.CompletedProcess(argv, proc.returncode,
            stdout=b"".join(chunks["stdout"]), stderr=b"".join(chunks["stderr"]))
    except (OSError, ValueError, subprocess.TimeoutExpired):
        raise Invalid("PDF_EXTRACTION_FAILED") from None
    finally:
        failed = False
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        except OSError:
            failed = True
        try:
            proc.wait(timeout=2)
        except (OSError, subprocess.TimeoutExpired):
            failed = True
        for stream in (proc.stdin, proc.stdout, proc.stderr):
            if stream is not None and not stream.closed:
                try:
                    stream.close()
                except OSError:
                    failed = True
        require(not failed, "PDF_CLEANUP_FAILED")


def event_text(message):
    require(type(message) is dict, "CHAT_MESSAGE_INVALID")
    author = message.get("author", {})
    require(author is None or type(author) is dict, "CHAT_AUTHOR_INVALID")
    candidates = (author.get("role") if type(author) is dict else None,
                  message.get("role"), message.get("sender"))
    require(all(value is None or
                (type(value) is str and (not value or value.strip()))
                for value in candidates), "CHAT_ROLE_INVALID")
    # Preserve the exported role, but compare known exporter aliases before
    # deciding whether contradictory fields describe the same actor.
    roles = [value for value in candidates if value]
    canonical = lambda value: {"human": "user", "function": "tool"}.get(value, value)
    require(len({canonical(value) for value in roles}) <= 1,
            "CHAT_ROLE_CONFLICT")
    role = roles[0] if roles else "unknown"
    actor = canonical(role)
    target = message.get("recipient")
    require(target is None or type(target) is str, "CHAT_RECIPIENT_INVALID")
    content = message.get("content", message.get("text", ""))
    if type(content) is dict:
        content = content.get("parts", content.get("text", ""))
    if type(content) is list:
        content = " ".join(str(v) if type(v) is str else
                           str(v["text"]) if type(v) is dict and
                           type(v.get("text")) is str else
                           json.dumps(v, ensure_ascii=False) for v in content)
    if type(content) not in {str, int, float, bool}:
        content = json.dumps(content, ensure_ascii=False)
    message_type = message.get("type")
    require(message_type is None or type(message_type) is str, "CHAT_TYPE_INVALID")
    # The source's type label cannot promote an assistant's own claim to a
    # tool-return event. Host execution authenticity remains a separate gate.
    calling = target not in {None, "all"} or message_type == "tool_use"
    require(not (message_type == "tool_result" and actor != "tool") and
            not (message_type == "tool_use" and actor != "assistant") and
            not (calling and actor not in {"assistant", "tool"}),
            "CHAT_EVENT_ROLE_CONFLICT")
    kind = ("tool_result" if actor == "tool" else
            "tool_call" if calling else "message")
    return role, kind, str(content)


def require_nonprivate_chat_identity(value: str) -> None:
    """Reject private source identifiers before JSON escaping changes their text.

    The public anchor is a lossless encoding of the source ID, not a safe
    redaction. Never expose a sensitive ID even when --redact is requested.
    """
    risk = risk_scan(value)
    require(not any(risk[k] for k in ("credential", "email", "phone")),
            "SENSITIVE_SOURCE_METADATA")


def chat_identifier(values, fallback, code, fallback_kind="index"):
    """Retain real IDs; tag missing-ID locations in a separate identity domain."""
    for value in values:
        if value is None or value == "":
            continue
        require(type(value) is str and bool(value.strip()), code)
        require_nonprivate_chat_identity(value)
        return ("id", value)
    require_nonprivate_chat_identity(fallback)
    return (fallback_kind, fallback)


def chat_anchor(conversation, message):
    """Encode two typed identity components without ambiguous ID concatenation.

    Raw IDs may contain ':' or resemble positional/node fallbacks; the
    tagged JSON pair keeps both the source domain and original value.
    """
    return "chat:v1:" + json.dumps(
        [conversation, message], ensure_ascii=False, separators=(",", ":"))


def verified_mapping_parents(nodes):
    """Check the entire parent graph, including branches not currently selected."""
    require(all(type(key) is str and type(node) is dict for key, node in nodes.items()),
            "CHATGPT_BRANCH_GRAPH_INVALID")
    parents = {key: node.get("parent") for key, node in nodes.items()}
    require(all(parent is None or (type(parent) is str and parent in nodes)
                for parent in parents.values()), "CHATGPT_BRANCH_GRAPH_INVALID")
    checked = set()
    for key in nodes:
        walk = set()
        cursor = key
        while cursor is not None and cursor not in checked:
            require(cursor not in walk, "CHATGPT_BRANCH_GRAPH_INVALID")
            walk.add(cursor)
            cursor = parents[cursor]
        checked.update(walk)
    return parents


def chat_events(data):
    """Read current ChatGPT lineage, never flatten mutually exclusive branches.

    When an export lacks a selected node but visibly forks, retain messages as
    separately marked unresolved data for manual selection, not one transcript.
    """
    if type(data) is list:
        # Ordinary JSON arrays belong to the generic document fallback. Only
        # an actual conversation-shaped item makes the root a chat batch;
        # once selected, all items still have to satisfy the chat contract.
        if not any(type(row) is dict and any(
                key in row for key in ("mapping", "messages", "chat_messages"))
                for row in data):
            return []
        conversations = data
    elif type(data) is dict:
        conversations = data["conversations"] if "conversations" in data else [data]
    else:
        return []  # Generic JSON scalar; the document fallback owns its text.
    require(type(conversations) is list and
            all(type(conversation) is dict for conversation in conversations),
            "CHAT_CONVERSATIONS_INVALID")
    structured_batch = (type(data) is dict and "conversations" in data or
                        type(data) is list and any(
                            any(k in row for k in ("mapping", "messages", "chat_messages"))
                            for row in conversations))
    if structured_batch:
        require(bool(conversations), "CHAT_CONVERSATIONS_EMPTY")
    events = []
    seen_anchors = set()
    for ci, conversation in enumerate(conversations):
        structured = any(k in conversation for k in ("mapping", "messages", "chat_messages"))
        if not structured:
            require(not structured_batch, "CHAT_MESSAGES_INVALID")
            continue  # An ordinary JSON document is not a chat transcript.
        cid = chat_identifier((conversation.get("id"), conversation.get("uuid"),
                               conversation.get("conversation_id")), str(ci),
                              "CHAT_CONVERSATION_ID_INVALID")
        mapping = conversation.get("mapping")
        if "mapping" in conversation:
            require(type(mapping) is dict, "CHAT_MAPPING_INVALID")
        branch_status = "linear"
        excluded_count = 0
        if type(mapping) is dict:
            nodes = mapping
            parents = verified_mapping_parents(nodes)
            current = conversation.get("current_node")
            if current is not None:
                require(type(current) is str and current in nodes,
                        "CHATGPT_CURRENT_NODE_INVALID")
                chain, visited = [], set()
                point = current
                while point is not None:
                    require(point in nodes and point not in visited,
                            "CHATGPT_BRANCH_GRAPH_INVALID")
                    visited.add(point)
                    chain.append((point, nodes[point]))
                    point = parents[point]
                chain.reverse()
                branch_status = "selected"
                excluded_count = sum(type(v.get("message")) is dict
                                     for key, v in nodes.items() if key not in visited)
            else:
                # A true fork with no current-node pointer must not be
                # silently transformed into a seemingly ordered conversation.
                parent_ids = [p for p in parents.values() if p is not None]
                roots = [key for key, parent in parents.items() if parent is None]
                leaves = [key for key in nodes if key not in parent_ids]
                if len(roots) == 1 and len(leaves) == 1 and len(set(parent_ids)) == len(parent_ids):
                    # One connected parent chain with a unique leaf is unambiguous
                    # even without a current_node. Do not sort by untrusted timestamps.
                    chain = []
                    point = leaves[0]
                    while point is not None:
                        chain.append((point, nodes[point]))
                        point = parents[point]
                    chain.reverse()
                    branch_status = "linear"
                else:
                    branch_status = ("unresolved" if len(parent_ids) != len(set(parent_ids))
                                     else "lineage_unverified")
                    chain = sorted(nodes.items(), key=lambda pair: str(
                        (pair[1].get("message") if type(pair[1].get("message")) is dict
                         else {}).get("create_time") or ""))
            messages = []
            for node_key, node in chain:
                message = node.get("message")
                # Real ChatGPT exports may have a message-less synthetic root.
                # Any other missing/malformed selected event is an evidence gap,
                # not an empty entry to silently discard from the transcript.
                if message is None and parents[node_key] is None:
                    continue
                require(type(message) is dict, "CHAT_MESSAGE_INVALID")
                messages.append((node_key, message))
        else:
            raw_messages = conversation.get("messages", conversation.get("chat_messages", []))
            require(type(raw_messages) is list and
                    all(type(message) is dict for message in raw_messages),
                    "CHAT_MESSAGES_INVALID")
            messages = [(str(mi), message) for mi, message in enumerate(raw_messages)]
        require(bool(messages), "CHAT_MESSAGES_EMPTY")
        for node_key, message in messages:
            role, kind, content = event_text(message)
            mid = chat_identifier((message.get("id"), message.get("uuid")),
                                  node_key, "CHAT_MESSAGE_ID_INVALID",
                                  "node" if type(mapping) is dict else "index")
            anchor = chat_anchor(cid, mid)
            require(anchor not in seen_anchors, "CHAT_ANCHOR_DUPLICATE")
            seen_anchors.add(anchor)
            events.append({"anchor": anchor, "role": role, "kind": kind,
                           "text": content, "branch_status": branch_status})
        if messages and type(mapping) is dict:
            # A count is audit metadata, not invented source text.
            events[-len(messages)]["excluded_branch_messages"] = excluded_count
    return events


def extract(path: Path, raw: bytes, kind: str):
    observations = {}
    if kind == "auto":
        kind = {".md": "text", ".txt": "text", ".log": "text",
                ".json": "json", ".html": "html", ".htm": "html",
                ".docx": "docx", ".pdf": "pdf"}.get(path.suffix.lower(), "unsupported")
    if kind == "text":
        text = raw.decode("utf-8")
        units = [{"anchor": "lines:1-" + str(len(text.splitlines())), "role": "source",
                  "kind": "document", "text": text}]
    elif kind == "html":
        units = [{"anchor": "html:text", "role": "source", "kind": "document",
                  "text": text_from_html(raw.decode("utf-8").encode("utf-8"))}]
    elif kind == "docx":
        units = [{"anchor": "docx:word/document.xml", "role": "source", "kind": "document",
                  "text": text_from_docx(raw)}]
    elif kind == "pdf":
        executable = shutil.which("pdftotext")
        require(bool(executable), "PDF_EXTRACTOR_UNAVAILABLE")
        completed = _run_pdf_tool(executable, raw)
        require(completed.returncode == 0 and
                len(completed.stdout) <= EXTRACTED_LIMIT, "PDF_EXTRACTION_FAILED")
        stream = completed.stdout.decode("utf-8")
        page_texts = stream.split("\f") if stream else []
        if stream.endswith("\f"):
            page_texts.pop()  # Exactly one terminal delimiter artifact, not a page.
        units, no_text_pages = [], []
        for i, text in enumerate(page_texts, 1):
            anchor = "pdf:page:" + str(i)
            if text.strip():
                units.append({"anchor": anchor, "role": "source",
                              "kind": "document", "text": text})
            else:
                no_text_pages.append({"page": i, "anchor": anchor, "reason": "UNKNOWN"})
        # These are slots observed in this extraction response. They neither
        # attest PDF metadata page totals nor diagnose why a page has no text.
        observations["pdf"] = {"observed_page_slots": len(page_texts),
                               "count_basis": "extraction_stream",
                               "no_text_pages": no_text_pages}
    elif kind == "json":
        data = strict_json(raw)
        units = chat_events(data)
        if not units:
            units = [{"anchor": "json:root", "role": "source",
                      "kind": "document",
                      "text": json.dumps(data, ensure_ascii=False, indent=2)}]
    else:
        raise Invalid("UNSUPPORTED_FORMAT")
    require(units and any(u["text"].strip() for u in units), "EMPTY_EXTRACTION")
    total = sum(len(u["text"].encode("utf-8")) for u in units)
    require(total <= EXTRACTED_LIMIT, "EXTRACTED_TEXT_TOO_LARGE")
    for u in units:
        anchor = u["anchor"]
        require(type(anchor) is str and 0 < len(anchor) <= MAX_SOURCE_ANCHOR and
                not any(ch in anchor for ch in "\r\n\x00"), "SOURCE_ANCHOR_INVALID")
        u["sha256"] = sha(u["text"].encode("utf-8"))
        u["lines"] = len(u["text"].splitlines())
    return units, observations


def credential_spans(text):
    """One owner for complete credential intervals, including multiline bodies.

    Overlapping recognizers describe one credential, not independent fragments.
    These structural alerts also apply to fully shaped synthetic examples.
    """
    spans = sorted((m.start(), m.end())
                   for pattern in CREDENTIAL_PATTERNS for m in pattern.finditer(text))
    merged = []
    for start, finish in spans:
        if merged and start < merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], finish))
        else:
            merged.append((start, finish))
    return merged


def redact_text(text):
    parts, offset = [], 0
    for start, finish in credential_spans(text):
        parts.extend((text[offset:start], "[REDACTED]"))
        offset = finish
    parts.append(text[offset:])
    text = "".join(parts)
    for pattern in (EMAIL, PHONE):
        text = pattern.sub("[REDACTED]", text)
    return text


def source_anchor_base(anchor):
    require(type(anchor) is str and 0 < len(anchor) <= MAX_SOURCE_LOCATOR and
            not any(ch in anchor for ch in "\r\n\x00"), "SOURCE_ANCHOR_INVALID")
    part = re.search(r":part:([1-9][0-9]*)-of-([1-9][0-9]*)$", anchor)
    base = anchor
    if part is not None:
        width = len(str(EXTRACTED_LIMIT))
        require(len(part[1]) <= width and len(part[2]) <= width, "SOURCE_ANCHOR_INVALID")
        index, total = int(part[1]), int(part[2])
        require(2 <= total <= EXTRACTED_LIMIT and 1 <= index <= total, "SOURCE_ANCHOR_INVALID")
        base = anchor[:part.start()]
    require(0 < len(base) <= MAX_SOURCE_ANCHOR, "SOURCE_ANCHOR_INVALID")
    return base


def split_units_for_validation(units, *, redact=False):
    """Partition oversized extracted units without losing bytes or source identity.

    The quality checker verifies at most LIMIT bytes per normalized text file.
    Splits prefer a newline; otherwise they preserve UTF-8 codepoint boundaries.
    Both original and final redacted bytes must fit the per-file resource bound.
    A :part:N-of-M suffix identifies the exact fragment of the original anchor.
    """
    result = []
    for unit in units:
        data = unit["text"].encode("utf-8")
        if len(data) <= LIMIT and (not redact or
                len(redact_text(unit["text"]).encode("utf-8")) <= LIMIT):
            result.append(unit)
            continue
        # A sensitive token may straddle an otherwise valid UTF-8 split.
        # Protect complete tokens before selecting byte boundaries so redaction
        # cannot lose half a credential or silently change the risk counts.
        intervals = sorted(credential_spans(unit["text"]) +
                           [(m.start(), m.end())
                            for pattern in (EMAIL, PHONE, LICENSE)
                            for m in pattern.finditer(unit["text"])])
        merged = []
        for start, finish in intervals:
            if merged and start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], finish))
            else:
                merged.append((start, finish))
        protected = []
        char_pos = byte_pos = 0
        for start, finish in merged:
            first = byte_pos + len(unit["text"][char_pos:start].encode("utf-8"))
            last = first + len(unit["text"][start:finish].encode("utf-8"))
            require(last - first <= LIMIT, "SENSITIVE_UNIT_UNSPLITTABLE")
            protected.append((first, last))
            char_pos, byte_pos = finish, last
        pieces = []
        offset = 0
        def safe_end(proposed):
            if proposed < len(data):
                while proposed > offset and (data[proposed] & 0xC0) == 0x80:
                    proposed -= 1
                newline = data.rfind(b"\n", offset + (proposed - offset) // 2, proposed)
                if newline >= 0:
                    proposed = newline + 1
                for first, last in protected:
                    if first < proposed < last:
                        proposed = first if first > offset else last
                        break
            return proposed

        while offset < len(data):
            end = safe_end(min(offset + LIMIT, len(data)))
            # Preserve original byte ranges and complete sensitive matches;
            # shortening a fragment never chops a credential or its redaction.
            while redact and len(redact_text(data[offset:end].decode("utf-8")).encode("utf-8")) > LIMIT:
                shortened = safe_end(offset + (end - offset) // 2)
                require(offset < shortened < end, "EXTRACTED_UNIT_UNSPLITTABLE")
                end = shortened
            require(end > offset and end - offset <= LIMIT, "EXTRACTED_UNIT_UNSPLITTABLE")
            require(not any(first < end < last for first, last in protected),
                    "SENSITIVE_SPLIT_BOUNDARY")
            pieces.append(data[offset:end].decode("utf-8"))
            offset = end
        require("".join(pieces).encode("utf-8") == data, "EXTRACTED_UNIT_UNSPLITTABLE")
        for index, piece in enumerate(pieces, 1):
            row = dict(unit)
            row["anchor"] = f'{unit["anchor"]}:part:{index}-of-{len(pieces)}'
            source_anchor_base(row["anchor"])
            row["text"] = piece
            row["sha256"] = sha(piece.encode("utf-8"))
            row["lines"] = len(piece.splitlines())
            result.append(row)
    return result


def risk_scan(text):
    matches = {"credential": credential_spans(text),
               "email": list(EMAIL.finditer(text)),
               "phone": list(PHONE.finditer(text)),
               "licensing": list(LICENSE.finditer(text))}
    return {kind: len(items) for kind, items in matches.items()}


def normalize(path, kind="auto", include_text=False, redact=False):
    raw = source_file(path)
    units, observations = extract(path, raw, kind)
    # The original extraction digest is independent of later validation-sized partitions.
    original_text = "\n".join(u["text"] for u in units)
    extracted_digest = sha(original_text.encode("utf-8"))
    excluded_branch_messages = sum(u.get("excluded_branch_messages", 0) for u in units)
    units = split_units_for_validation(units, redact=redact)
    # Anchors and roles are exported even without --include-text and appear
    # unchanged inside R09 lineage. Never disguise a private identifier by
    # redacting its display value while claiming the original source anchor.
    metadata = "\n".join(u["anchor"] + "\n" + u["role"] for u in units)
    metadata_risk = risk_scan(metadata)
    require(not any(metadata_risk[k] for k in ("credential", "email", "phone")),
            "SENSITIVE_SOURCE_METADATA")
    # Risk counts belong to the original text. Fragment boundaries are checked
    # against its protected match intervals by the splitter; synthetic separators
    # would create new regex word boundaries and falsely reject valid inputs.
    risk = risk_scan(original_text)
    private = any(risk[k] for k in ("credential", "email", "phone"))
    if include_text and private and not redact:
        raise Invalid("SENSITIVE_TEXT_REQUIRES_REDACTION")
    fmt = kind if kind != "auto" else path.suffix.lower().lstrip(".")
    if fmt in {"md", "txt", "log"}:
        fmt = "text"
    if fmt == "htm":
        fmt = "html"
    extractor = EXTRACTORS[fmt]
    version = "python-stdlib-" + ".".join(map(str, sys.version_info[:3]))
    if fmt == "pdf":
        executable = shutil.which("pdftotext")
        version = None
        if executable:
            check = _run_pdf_tool(executable, b"", version=True)
            if check.returncode == 0:
                lines = (check.stderr + check.stdout).decode("utf-8", errors="replace").splitlines()
                version = lines[0][:160] if lines else None
    # Every normalized unit carries the exact lineage descriptor consumed by
    # R09's dossier. This is declared source metadata, not original-host proof.
    source_digest = sha(raw)
    result = []
    for unit in units:
        body = unit["text"]
        if redact:
            body = redact_text(body)
        require(len(body.encode("utf-8")) <= LIMIT, "OUTPUT_UNIT_TOO_LARGE")
        output_digest = sha(body.encode("utf-8"))
        out = {k: v for k, v in unit.items() if k != "text"}
        out["lines"] = len(body.splitlines())
        out["output_sha256"] = output_digest
        out["lineage"] = {"kind": "normalized", "source_sha256": source_digest,
                          "normalizer_version": NORMALIZER_VERSION,
                          "extractor": extractor, "extractor_version": version,
                          "extracted_text_sha256": extracted_digest,
                          "source_anchor": unit["anchor"], "unit_sha256": unit["sha256"],
                          "output_sha256": output_digest, "redacted": bool(redact)}
        if include_text:
            out["text"] = body
        result.append(out)
    branch_review = any(u.get("branch_status") in {"unresolved", "lineage_unverified"}
                        for u in units)
    pdf_gaps = bool(observations.get("pdf", {}).get("no_text_pages"))
    return {"check": "normalize",
            "status": "NEEDS_REVIEW" if private or risk["licensing"] or branch_review or pdf_gaps else "PASS",
            "source_sha256": source_digest, "source_bytes": len(raw),
            "normalizer_version": NORMALIZER_VERSION,
            "extractor": extractor, "extractor_version": version,
            "extracted_text_sha256": extracted_digest,
            "excluded_branch_messages": excluded_branch_messages,
            "branch_selection_unresolved": branch_review,
            "units": result, "risk_counts": risk,
            "extraction_observations": observations,
            "license_verified": False, "model_read_attested": False,
            "original_text_exposed": include_text and not redact}


def coverage(root, manifest):
    data = strict_json(source_file(manifest))
    require(type(data) is dict and type(data.get("version")) is int and data["version"] == 1 and
            type(data.get("sources")) is list and data["sources"], "COVERAGE_MANIFEST_INVALID")
    require(root.is_dir() and not root.is_symlink(), "COVERAGE_ROOT_INVALID")
    counters = {s: 0 for s in TAGS}
    totals = 0
    paths = set()
    unavailable_paths = set()
    for entry in data["sources"]:
        require(type(entry) is dict, "COVERAGE_SOURCE_INVALID")
        rel = entry.get("path")
        require(type(rel) is str and rel and "\\" not in rel and "\x00" not in rel and
                not PurePosixPath(rel).is_absolute() and
                ".." not in PurePosixPath(rel).parts, "COVERAGE_SOURCE_UNSAFE")
        require(rel not in paths, "COVERAGE_DUPLICATE_SOURCE")
        paths.add(rel)
        cur = root
        for part in PurePosixPath(rel).parts:
            cur = cur / part
            require(not cur.is_symlink(), "COVERAGE_SOURCE_SYMLINK")
        require(root.resolve() in cur.resolve().parents, "COVERAGE_PATH_ESCAPE")
        availability = entry.get("availability", "available")
        require(type(availability) is str and
                availability in {"available", "unavailable"},
                "COVERAGE_AVAILABILITY_INVALID")
        spans = entry.get("spans", [])
        require(type(spans) is list, "COVERAGE_SPAN_INVALID")
        if availability == "unavailable":
            # A missing source is an explicit gap, never a fictional zero-line
            # source. It cannot carry copied or fabricated readable line spans.
            require(not cur.exists(), "COVERAGE_AVAILABLE_SOURCE_MISLABELED")
            require(type(entry.get("reason")) is str and entry["reason"].strip(),
                    "COVERAGE_REASON_REQUIRED")
            require(not spans, "COVERAGE_UNAVAILABLE_HAS_SPANS")
            old_digest = entry.get("sha256")
            require(old_digest is None or
                    (type(old_digest) is str and re.fullmatch(r"[a-f0-9]{64}", old_digest)),
                    "COVERAGE_UNAVAILABLE_DIGEST_INVALID")
            unavailable_paths.add(rel)
            counters["unavailable"] += 1  # one missing-source sentinel, not lines
            continue
        raw = source_file(cur)
        require(sha(raw) == entry.get("sha256"), "COVERAGE_SOURCE_CHANGED")
        lines = raw.decode("utf-8").splitlines(keepends=True)
        labels = [None] * len(lines)
        for span in spans:
            require(type(span) is dict, "COVERAGE_SPAN_INVALID")
            lo, hi, tag = span.get("start"), span.get("end"), span.get("label")
            require(type(lo) is int and type(hi) is int and
                    1 <= lo <= hi <= len(lines) and
                    type(tag) is str and tag in TAGS, "COVERAGE_SPAN_INVALID")
            require(sha("".join(lines[lo - 1:hi]).encode()) == span.get("sha256"),
                    "COVERAGE_SPAN_CHANGED")
            require(type(span.get("reason")) is str and span["reason"].strip(),
                    "COVERAGE_REASON_REQUIRED")
            for index in range(lo - 1, hi):
                require(labels[index] is None, "COVERAGE_OVERLAP")
                labels[index] = tag
        totals += len(lines)
        for tag in labels:
            counters[tag or "unread"] += 1
    require(totals > 0 or unavailable_paths, "COVERAGE_EMPTY")
    observed = set()
    for base, dirs, names in walk_source_tree(root):
        for name in dirs + names:
            candidate = Path(base) / name
            require(not candidate.is_symlink(), "COVERAGE_SOURCE_SYMLINK")
            if candidate.is_file() and candidate.resolve() != manifest.resolve():
                observed.add(candidate.relative_to(root).as_posix())
    require(paths == observed | unavailable_paths, "COVERAGE_SOURCE_INVENTORY_INCOMPLETE")
    complete = counters["unread"] == 0 and counters["unavailable"] == 0
    return {"check": "coverage", "status": "PASS" if complete else "NOT_PROVEN",
            "coverage_lines": totals, "line_classes": counters,
            "unavailable_sources": sorted(unavailable_paths),
            "unavailable_line_counts": "UNKNOWN" if unavailable_paths else 0,
            "model_read_attested": False,
            "note": "Relevance is declared, not semantic truth or observed model reading"}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Read-only source normalization and coverage")
    sub = ap.add_subparsers(dest="action", required=True)
    n = sub.add_parser("normalize")
    n.add_argument("--input", required=True)
    n.add_argument("--kind", choices=("auto", "text", "html", "docx", "pdf", "json"),
                   default="auto")
    n.add_argument("--include-text", action="store_true")
    n.add_argument("--redact", action="store_true")
    c = sub.add_parser("coverage")
    c.add_argument("--root", required=True)
    c.add_argument("--manifest", required=True)
    args = ap.parse_args(argv)
    try:
        out = (normalize(Path(args.input), args.kind, args.include_text, args.redact)
               if args.action == "normalize" else
               coverage(Path(args.root), Path(args.manifest)))
        print(json.dumps(out, ensure_ascii=False, sort_keys=True))
        return 0 if out["status"] == "PASS" else 2
    except (Invalid, OSError, UnicodeError, ValueError, subprocess.TimeoutExpired,
            zipfile.BadZipFile, ET.ParseError) as exc:
        code = exc.code if isinstance(exc, Invalid) else "IO_OR_PARSE_ERROR"
        print(json.dumps({"check": args.action, "status": "FAIL",
                          "error": code}, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
