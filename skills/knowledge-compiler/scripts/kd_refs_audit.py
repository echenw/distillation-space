#!/usr/bin/env python3
"""S14 kd_refs_audit -- evidence reference integrity (Round 3 Wave 1, contract S14).

Contract (.distill/round-3/wave-1/_dispatch/w1c.json):
    inputs  : `evidence_refs[]` + 仓库根注册表
    outputs : `refs_integrity` 结果位（每轮重算）
    exit    : 2=路径不可解析或使用 brace/通配简写

Round 2 basis (quoted in _dispatch/pack-c.md):
  * `05-DATA-MODEL.md:44` -- evidence_refs[].path 必须为规范仓库相对路径，禁 brace/通配
    简写；"Worker 填，resolver 校验，解析失败即拒绝入库"。
  * `10-PROVENANCE-MODEL.md` SR-1/SR-2/SR-3 -- round-1 measured defect classes:
    paths missing the `repos/` prefix, brace shorthand, only a fraction directly resolvable.
  * SR-4 -- "not found 不允许自动映射": this tool never guesses a target. A ref either
    resolves under a registered root or it fails.
  * SR-6 -- "门存在但无调用点 = 未接线 = 视同不存在": every number this tool reports is
    recomputed from disk on every run; nothing is accepted from a prior report.
  * `10-PROVENANCE-MODEL.md` L4 (产物强标识符) -- `check_claim_binding` implements the
    verbatim set-difference check required by CM-65; S12 calls it before any write.

Anti-vacuity rules (this module's whole point):
  * an empty ref set is NOT success -- it is `EMPTY_REF_SET`, a distinct visible result;
  * a scan that found no corpus file, or a corpus file that failed to parse, is
    `SCANNED_SET_INCOMPLETE` -- never a green audit;
  * a ref that resolves only because a glob/brace was expanded is a failure, not a hit.

Stdlib only. Normal reference checks are read-only. The explicit historical
comparison mode executes an operator-digest-pinned Python auditor and must be
run only with trusted executable content and appropriately restricted OS rights;
a SHA check is not a sandbox. S12 alone owns authoritative store writes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys

EXIT_OK = 0
EXIT_INTEGRITY_FAILED = 2          # contractual: unresolvable path or brace/glob shorthand
EXIT_EMPTY_REF_SET = 3             # distinct visible result, deliberately not success
EXIT_SCANNED_SET_INCOMPLETE = 4    # nothing/only-unparseable was scanned -> never green
EXIT_INVALID_INPUTS = 5            # CLI usage error: kept off code 2, which is contractual

STATUS_PASS = "PASS"
STATUS_FAIL_UNRESOLVED = "FAIL_UNRESOLVED"
STATUS_FAIL_SHORTHAND = "FAIL_SHORTHAND"
STATUS_EMPTY_REF_SET = "EMPTY_REF_SET"
STATUS_INCOMPLETE = "SCANNED_SET_INCOMPLETE"

# characters that make a path a *shorthand* rather than a single openable string
BRACE_CHARS = ("{", "}")
GLOB_CHARS = ("*", "?", "[", "]")
TRUNCATION_MARKS = ("…", "...", "etc.", "其余省略")
PLACEHOLDER_MARKS = ("<", ">", "TBD", "path/to")

LINE_SUFFIX_RE = re.compile(r"^(?P<path>[^:]+?):(?P<start>\d+)(?:-(?P<end>\d+))?$")

MAX_FAILURE_ROWS = 60

def reference_root_specs(workspace: str) -> list:
    """`NAME=PATH` spec registering one EXPLICITLY named workspace as the default root.

    RH-P1-06 / §6: S14 is a GENERIC reference-integrity auditor. It registers only roots the
    caller names -- `--root NAME=PATH` (repeatable), or this single-workspace convenience. It no
    longer hardcodes Repo-A's Round-1 bootstrap repo set (the 15 reference repositories) nor
    its monorepo sub-layout (`.distill` / `packages` / `repos`): those are build-time/CI concerns,
    not shipped-runtime knowledge, and an installed Skill compiling a NEW target has no use for
    them. A build-time audit that must resolve a Round-1 citation passes an explicit
    `--root <name>=<ws>/repos/<name>` per repo -- the same generic mechanism, no baked-in list.

    No cwd fallback (SR-4): the operator names the workspace, because a silently different
    workspace would change which paths resolve and make the audit non-reproducible.
    """
    ws = os.path.realpath(os.path.abspath(os.path.expanduser(workspace)))
    if not os.path.isdir(ws):
        raise RootRegistrationError(f"--reference-roots {workspace}", ws)
    return [f"ws={ws}"]


# --------------------------------------------------------------------- ref normalisation
class RefSyntaxError(Exception):
    """The ref string is not a single openable path -- shorthand, truncation, placeholder."""


def classify_shorthand(raw: str) -> str | None:
    """Return the shorthand class of a raw ref string, or None when it is a plain path."""
    text = str(raw)
    if any(c in text for c in BRACE_CHARS):
        return "BRACE"
    if any(c in text for c in GLOB_CHARS):
        return "GLOB"
    if any(m in text for m in TRUNCATION_MARKS):
        return "TRUNCATED"
    if any(m in text for m in PLACEHOLDER_MARKS):
        return "PLACEHOLDER"
    return None


def split_annotation(raw: str) -> tuple[str, str]:
    """Drop a trailing parenthetical annotation (`...(注：…)` / `…（说明）`).

    Round 1 evidence strings carry free-text notes after the path; the note is kept as
    diagnostic text only, it never participates in resolution.
    """
    text = str(raw).strip()
    for opener, closer in (("（", "）"), ("(", ")")):
        idx = text.find(opener)
        if idx > 0 and text.rstrip().endswith(closer):
            return text[:idx].strip(), text[idx:].strip()
    return text, ""


def parse_ref(raw: str, *, project: str = "", origin: str = "") -> dict:
    """Normalise one raw evidence reference into a structured ref.

    Raises RefSyntaxError for shorthand/truncated forms -- the caller records those as
    contractual exit-2 failures instead of guessing a target (SR-4).
    """
    head, annotation = split_annotation(raw)
    bad = classify_shorthand(head)
    if bad is not None:
        raise RefSyntaxError(f"{bad} shorthand in ref: {raw!r}")
    if not head:
        raise RefSyntaxError(f"empty ref: {raw!r}")

    symbol = ""
    body = head
    if "#" in body:
        body, _, symbol = body.partition("#")

    line_start = line_end = None
    m = LINE_SUFFIX_RE.match(body.strip())
    if m:
        body = m.group("path")
        line_start = int(m.group("start"))
        line_end = int(m.group("end")) if m.group("end") else line_start
        if line_end < line_start:
            raise RefSyntaxError(f"inverted line range in ref: {raw!r}")
    elif ":" in body.split("/")[0]:
        raise RefSyntaxError(f"unparseable line suffix in ref: {raw!r}")

    path = body.strip().strip("`'\"")
    if path.startswith("/") or path.startswith("\\"):
        raise RefSyntaxError(f"absolute ref (must be repo-relative): {raw!r}")
    parts = [p for p in path.replace("\\", "/").split("/") if p]
    if any(p == ".." for p in parts):
        raise RefSyntaxError(f"ref escapes its root: {raw!r}")
    if not parts:
        raise RefSyntaxError(f"empty path component: {raw!r}")

    return {
        "project": project or None,
        "path": "/".join(parts),
        "symbol": symbol.strip() or None,
        "line_start": line_start,
        "line_end": line_end,
        "raw": str(raw),
        "annotation": annotation or None,
        "origin": origin or None,
    }


# --------------------------------------------------------------------- root registry
class RootRegistrationError(Exception):
    """A root named on the command line does not exist.

    Registered by a dispatcher typo (`--reference-roots WORKSPACE`, the metavar passed
    instead of a path): every ref then fails to resolve, and the cross-check reported
    `S14_WEAKER` -- a wrong verdict instead of a wrong input. SR-4 fail-closed applies to
    the registration itself, not only to the refs."""

    def __init__(self, spec: str, path: str):
        Exception.__init__(self, f"registered root does not exist: {spec!r} -> {path}")
        self.spec, self.path = spec, path


class RootRegistry:
    """`仓库根注册表`: project name -> absolute directory. No implicit roots.

    SR-4: a missing root is a *failure* (`NO_REGISTERED_ROOT`), never a silent skip and
    never a fallback to the current directory. A ref may only resolve under a root that was
    named on the command line; `readonly` records which registered roots are reference
    repositories (resolution targets, never outputs).
    """

    def __init__(self, entries=None, readonly_entries=None):
        self.roots: dict[str, str] = {}
        self.readonly: set[str] = set()
        self.absent: list = []
        self.default: str | None = None
        for spec in entries or []:
            self.add(spec, require_exists=True)
        for spec in readonly_entries or []:
            name = self.add(spec, require_exists=False)
            if name:
                self.readonly.add(name)

    def add(self, spec: str, require_exists: bool = True):
        """Operator-named roots must exist (a typo would silently resolve nothing).

        A root of the frozen Round 1 reference set may legitimately be absent on another
        machine, so it is recorded in `self.absent` and reported rather than raised --
        but never counted as coverage the audit had.
        """
        if "=" in spec.split(os.sep)[0]:
            name, _, raw = spec.partition("=")
        else:
            raw, name = spec, os.path.basename(os.path.normpath(spec))
        path = os.path.realpath(os.path.abspath(os.path.expanduser(raw)))
        if not os.path.isdir(path):
            if require_exists:
                raise RootRegistrationError(spec, path)
            self.absent.append(name)
            return None
        self.roots[name] = path
        if self.default is None:
            self.default = path
        return name

    def for_project(self, project: str | None) -> tuple[str | None, str | None]:
        if project and project in self.roots:
            return project, self.roots[project]
        return None, None

    def candidate_names(self, project: str | None) -> list:
        """Explicit projects only search their registered project/head roots. A missing file
        never falls back to another project. Unscoped refs use the explicit default, or all
        registered roots with ambiguity detection; there is no cwd or inferred repo mapping.
        """
        ordered = []
        if project:
            head = str(project).split("/")[0]
            if project not in self.roots and head not in self.roots:
                # a ref that names a project NO registered root covers fails closed
                # (NO_REGISTERED_ROOT): an unrelated root must never be searched for it
                # (SR-4, and `test_refs_pass_only_when_every_ref_resolves_with_its_range`).
                return []
            for name in (project, head):
                if name in self.roots and name not in ordered:
                    ordered.append(name)
            return ordered   # a missing file in project A must not resolve in project B
        if self.default is not None and not project:
            for name, path in self.roots.items():
                if path == self.default and name not in ordered:
                    ordered.append(name)
        for name in self.roots:
            if name not in ordered:
                ordered.append(name)
        return ordered


def count_lines(path: str) -> int:
    n = 0
    with open(path, "rb") as fh:            # read-only: S14 never writes
        for _ in fh:
            n += 1
    return n


# --------------------------------------------------------------------- resolution
def resolve_one(ref: dict, registry: RootRegistry) -> dict:
    """Resolve a single parsed ref against the REGISTERED roots only.

    Resolution is a `stat` of the exact cited path under each candidate root: no directory is
    walked, no glob is expanded, no name is fuzzy-matched. Returns kind=OK plus the root that
    held it, or the failure kind (`UNRESOLVED`, `NOT_A_FILE`, `AMBIGUOUS_ROOT`, `ESCAPES_ROOT`,
    `NO_LINE_RANGE`, `LINE_RANGE_OUT_OF_FILE`, `UNREADABLE`, `NO_REGISTERED_ROOT`).
    """
    names = registry.candidate_names(ref.get("project"))
    if not names:
        return _fail(ref, "NO_REGISTERED_ROOT",
                     f"no root registered for project {ref.get('project')!r}")

    hits, dir_hits, escapes = [], [], []
    for name in names:
        root = registry.roots[name]
        candidate = os.path.realpath(os.path.join(root, ref["path"]))
        if not (candidate == root or candidate.startswith(root + os.sep)):
            escapes.append(name)
            continue
        if os.path.isdir(candidate):
            dir_hits.append(name)
            continue
        if os.path.isfile(candidate):
            if (candidate, ) not in [(h[1], ) for h in hits]:
                hits.append((name, candidate))
    if not hits:
        if dir_hits:
            return _fail(ref, "NOT_A_FILE", f"{ref['path']} is a directory under "
                                            f"{dir_hits}, not a file")
        if escapes:
            return _fail(ref, "ESCAPES_ROOT", f"{ref['path']} escapes registered roots "
                                              f"{escapes}")
        return _fail(ref, "UNRESOLVED",
                     f"no such file under any registered root "
                     f"({len(names)} roots tried, project={ref.get('project')!r}): {ref['path']}")

    distinct = {path for _, path in hits}
    if len(distinct) > 1:
        return _fail(ref, "AMBIGUOUS_ROOT",
                     f"{ref['path']} exists under {[n for n, _ in hits]} -- refusing to pick a "
                     "root (SR-4: not found must not become an automatic mapping)")
    root_name, resolved = hits[0]

    if ref["line_start"] is None:
        return _fail(ref, "NO_LINE_RANGE",
                     f"ref resolves to {ref['path']} but carries no line range; "
                     "S14 requires file + line range inside it")
    try:
        total = count_lines(resolved)
    except OSError as exc:                      # unreadable file is a visible failure
        return _fail(ref, "UNREADABLE", str(exc))
    if not (1 <= ref["line_start"] <= ref["line_end"] <= total):
        return _fail(ref, "LINE_RANGE_OUT_OF_FILE",
                     f"{ref['path']}: {ref['line_start']}-{ref['line_end']} not inside "
                     f"a {total}-line file")

    project = ref.get("project")
    declared = project if project and project in registry.roots else \
        (str(project).split("/")[0] if project and str(project).split("/")[0] in registry.roots
         else None)
    return {"kind": "OK", "ref": ref, "resolved_path": resolved,
            "root": root_name, "file_lines": total,
            # visible signal for Round 1's measured defect class (worker-10's 132 paths omit
            # the `repos/` prefix, so they resolve only under a root OTHER than their own
            # project root): the citation is not silently treated as clean.
            "resolved_via_declared_root": declared is None or root_name == declared,
            "readonly_root": root_name in registry.readonly}


def _fail(ref: dict, kind: str, detail: str) -> dict:
    return {"kind": kind, "ref": ref, "detail": detail}


def audit_refs(refs: list[dict], registry: RootRegistry) -> dict:
    """Pure audit over already-parsed refs. Empty input is a distinct visible result."""
    findings = []
    for ref in refs:
        findings.append(resolve_one(ref, registry))
    counts: dict[str, int] = {}
    for f in findings:
        counts[f["kind"]] = counts.get(f["kind"], 0) + 1
    resolved = counts.get("OK", 0)
    total = len(refs)

    if total == 0:
        status = STATUS_EMPTY_REF_SET
    elif resolved == total:
        status = STATUS_PASS
    else:
        # shorthand forms never reach `refs` (parse_ref refuses them) -- run() upgrades the
        # status to FAIL_SHORTHAND when it has collected them
        status = STATUS_FAIL_UNRESOLVED
    return {
        "status": status,
        "total_refs": total,
        "resolved": resolved,
        "unresolved": total - resolved,
        "counts": dict(sorted(counts.items())),
        "findings": findings,
    }


def status_exit_code(status: str, incomplete: bool) -> int:
    # a positive integrity failure outranks an incomplete scan; incompleteness alone is still
    # never a pass (a previous auditor's check could pass vacuously -- this one cannot)
    code = status_exit_code_for(status)
    if code == EXIT_OK and incomplete:
        return EXIT_SCANNED_SET_INCOMPLETE
    return code


def status_exit_code_for(status: str) -> int:
    if status == STATUS_PASS:
        return EXIT_OK
    if status == STATUS_EMPTY_REF_SET:
        return EXIT_EMPTY_REF_SET
    if status == STATUS_INCOMPLETE:
        return EXIT_SCANNED_SET_INCOMPLETE
    return EXIT_INTEGRITY_FAILED


def refs_integrity_bit(result: dict) -> dict:
    """The `refs_integrity` 结果位 written into a record (recomputed every round)."""
    return {
        "status": result["status"],
        "total_refs": result["total_refs"],
        "resolved": result["resolved"],
        "unresolved": result["unresolved"],
        "basis": f"kd_refs_audit@{os.path.relpath(os.path.abspath(__file__))}",
    }


# --------------------------------------------------------------------- CM-65 claim binding
def check_claim_binding(claims: list[dict], evidence_refs: list[dict]) -> list[dict]:
    """CM-65 / 10 §1.4 (L4): every strong identifier in an assertion must appear verbatim
    inside the line range of the evidence it cites. Stray identifiers -> refuse the write.

    `claims[] = {claim_id, text, strong_identifiers[], evidence_ref_index}`.
    Only refs that actually resolved are usable; a claim bound to an unresolved ref fails.
    """
    stray = []
    for claim in claims or []:
        ids = [str(x) for x in claim.get("strong_identifiers") or []]
        idx = claim.get("evidence_ref_index")
        if not ids:
            continue
        if not isinstance(idx, int) or not (0 <= idx < len(evidence_refs)):
            stray.append({"claim_id": claim.get("claim_id"), "reason": "NOT_BOUND",
                          "identifiers": ids})
            continue
        ref = evidence_refs[idx]
        resolved = ref.get("resolved_path")
        if not resolved or not os.path.isfile(resolved):
            stray.append({"claim_id": claim.get("claim_id"), "reason": "REF_UNRESOLVED",
                          "identifiers": ids})
            continue
        window = _line_window(resolved, ref.get("line_start"), ref.get("line_end"))
        missing = [i for i in ids if i not in window]
        if missing:
            stray.append({"claim_id": claim.get("claim_id"), "reason": "STRAY_IDENTIFIER",
                          "identifiers": missing})
    return stray


def _line_window(path: str, start, end) -> str:
    with open(path, encoding="utf-8", errors="replace") as fh:   # read-only
        lines = fh.readlines()
    if start is None:
        return "".join(lines)
    lo = max(1, int(start))
    hi = min(len(lines), int(end or start))
    return "".join(lines[lo - 1:hi])


# --------------------------------------------------------------------- corpus harvesting
WORKER_JSON_FIELDS = (
    ("mechanisms", "evidence", "path"),      # evidence_refs[] proper
    ("implementation_evidence", None, None),  # free strings with inline ranges
)


def harvest_corpus(doc: dict, source: str) -> tuple[list[dict], list[dict]]:
    """Extract raw ref strings from a Round 1 worker document.

    Returns (refs, syntax_failures). A string that cannot be parsed is *not* dropped: it
    becomes a visible shorthand failure, which is exactly the SR-2 defect class.
    """
    refs, failures = [], []
    project = doc.get("project") or ""

    def emit(raw, origin):
        try:
            refs.append(parse_ref(raw, project=project, origin=origin))
        except RefSyntaxError as exc:
            failures.append({"kind": "SHORTHAND", "detail": str(exc), "raw": str(raw),
                             "ref": {"raw": str(raw), "path": str(raw), "project": project,
                                     "origin": origin, "line_start": None, "line_end": None}})

    for mech in doc.get("mechanisms") or []:
        for ev in mech.get("evidence") or []:
            if isinstance(ev, dict) and ev.get("path"):
                raw = ev["path"]
                if ev.get("symbol") and ":" not in raw:
                    raw = f"{raw}#{ev['symbol']}" if "\n" not in str(ev["symbol"]) else raw
                emit(raw, f"mechanisms[{mech.get('id')}].evidence.path")
        reuse = mech.get("code_reuse")
        if isinstance(reuse, dict) and reuse.get("file"):
            emit(reuse["file"], f"mechanisms[{mech.get('id')}].code_reuse.file")
    for raw in doc.get("implementation_evidence") or []:
        if isinstance(raw, str):
            emit(raw, "implementation_evidence")
    return dedupe(refs), dedupe_failures(failures)


def dedupe(refs: list[dict]) -> list[dict]:
    seen, out = set(), []
    for r in refs:
        key = (r["path"], r["line_start"], r["line_end"], r["origin"])
        if key not in seen:
            seen.add(key)
            out.append(r)
    return out


def dedupe_failures(failures: list[dict]) -> list[dict]:
    seen, out = set(), []
    for f in failures:
        key = f["raw"]
        if key not in seen:
            seen.add(key)
            out.append(f)
    return out


def harvest_evidence_paths(doc: dict) -> list:
    """The Round 1 auditor's universe, exactly: every `mechanisms[].evidence[].path` string,
    in document order, NOT deduplicated (`.distill/round-1/audit_round1.py` builds `ev` the
    same way and counts 1293). S14's normal corpus harvest is a wider set (it also reads
    `code_reuse.file` and the free-text `implementation_evidence` lines), so a cross-check
    against Round 1's numbers has to be able to state the narrower universe, or the two sides
    are not comparable and the comparison would be meaningless.
    """
    out = []
    for mech in doc.get("mechanisms") or []:
        for ev in mech.get("evidence") or []:
            if isinstance(ev, dict) and ev.get("path"):
                out.append(ev["path"])
    return out


# --------------------------------------------------------------------- Round 1 cross-check
ROUND1_CHECK_KEYS = ("refs_total", "resolved", "unresolved", "shorthand", "line_range_violations")


def stem_probe(raw: str, project: str, registry: RootRegistry):
    """Classify a REFUSED citation by stat-ing its literal file part.

    This is not a resolution path and expands nothing: it takes the citation exactly as
    written, strips a trailing `#symbol` and a `:<digits...>` suffix (the same textual split
    `parse_ref` already performs for a legal single range), and asks whether THAT literal stem
    exists. Brace/glob stems are never probed -- probing would be expansion, which SR-4 and the
    exit-2 contract forbid. It exists so a refusal can be named honestly: "you cited a
    directory" and "your range syntax is not a single range, but the file is there" are not the
    same fact as "no registered root holds this path".
    """
    stem = str(raw).split("#")[0].split(" (line")[0].strip()
    m = re.search(r":\d", stem)
    if m:
        stem = stem[:m.start()]
    stem = stem.strip().strip("`'\"")
    if not stem or classify_shorthand(stem):
        return "NOT_PROBED_SHORTHAND"
    probe = {"path": stem, "project": project or None, "line_start": None, "line_end": None,
             "raw": str(raw), "symbol": None, "annotation": None, "origin": "stem-probe"}
    kind = resolve_one(probe, registry)["kind"]
    if kind == "NO_LINE_RANGE":                    # the resolver found the FILE
        return "FILE_EXISTS"
    return {"NOT_A_FILE": "CITED_DIRECTORY", "UNRESOLVED": "NO_SUCH_FILE"}.get(kind, kind)


def round1_universe(registry: RootRegistry, corpus_files: list) -> dict:
    """Resolve the Round 1 evidence-path universe with S14's own code, no dedupe, no expansion.

    Every number here is recomputed from disk on this run (SR-6): nothing is taken from a
    previous report, including Round 1's own.
    """
    parsed, shorthand, unresolved, no_range, out_of_range = [], [], [], [], []
    buckets = {"cited_directory": 0, "refused_citation_file_exists": 0, "truly_missing": 0}
    rows = {"cited_directory": [], "refused_citation_file_exists": [], "truly_missing": []}
    for path in corpus_files:
        try:
            with open(path, encoding="utf-8") as fh:      # read-only
                doc = json.load(fh)
        except (OSError, ValueError):
            continue                                      # reported by the main scan, not here
        if not isinstance(doc, dict):
            continue
        project = doc.get("project") or ""
        for raw in harvest_evidence_paths(doc):
            try:
                parsed.append(parse_ref(raw, project=project, origin="evidence.path"))
            except RefSyntaxError as exc:
                shorthand.append({"raw": raw, "detail": str(exc), "project": project,
                                  "shorthand": classify_shorthand(str(raw))})
    for ref in parsed:
        finding = resolve_one(ref, registry)
        kind = finding["kind"]
        if kind == "OK":
            continue
        if kind == "NO_LINE_RANGE":
            no_range.append(finding)
            continue
        if kind == "LINE_RANGE_OUT_OF_FILE":
            out_of_range.append(finding)
            continue
        # a refused citation: name WHY it was refused, using the literal stem only
        probe = stem_probe(ref["raw"], ref.get("project") or "", registry)
        if kind == "NOT_A_FILE" or probe == "CITED_DIRECTORY":
            buckets["cited_directory"] += 1
            rows["cited_directory"].append({"path": ref["path"], "kind": kind})
        elif probe == "FILE_EXISTS":
            buckets["refused_citation_file_exists"] += 1
            rows["refused_citation_file_exists"].append({"path": ref["path"], "kind": kind})
        else:
            buckets["truly_missing"] += 1
            rows["truly_missing"].append({"path": ref["path"], "project": ref.get("project"),
                                          "kind": kind, "detail": finding["detail"]})
    return {
        "refs_total": len(parsed) + len(shorthand),
        # `path_exists` = the cited path is a readable FILE under a registered root (a line
        # range may or may not follow); `resolved` is S14's full contract answer (file AND a
        # line range inside it). Round 1's auditor only ever asked the first question.
        "path_exists": len(parsed) - buckets["cited_directory"] - buckets["truly_missing"],
        "resolved": len(parsed) - len(no_range) - len(out_of_range)
            - buckets["cited_directory"] - buckets["refused_citation_file_exists"]
            - buckets["truly_missing"],
        # refusals that are NOT "no line range" (that count is reported on its own row)
        "unresolved": (len(out_of_range) + buckets["cited_directory"]
                       + buckets["refused_citation_file_exists"] + buckets["truly_missing"]),
        "covered": (len(parsed) - buckets["cited_directory"] - buckets["truly_missing"]
                    + buckets["cited_directory"] + len(shorthand)),
        "shorthand": len(shorthand),
        "shorthand_file_exists": sum(1 for s in shorthand
                                     if stem_probe(s["raw"], s.get("project") or "",
                                                   registry) == "FILE_EXISTS"),
        "line_range_violations": len(out_of_range),
        "no_line_range": len(no_range),
        "cited_directory": buckets["cited_directory"],
        "refused_citation_file_exists": buckets["refused_citation_file_exists"],
        "truly_missing": buckets["truly_missing"],
        "rows_cited_directory": rows["cited_directory"][:12],
        "rows_refused_citation": rows["refused_citation_file_exists"][:12],
        "rows_truly_missing": rows["truly_missing"][:12],
        "shorthand_rows": shorthand[:12],
    }


MAX_WITNESS_BYTES = 4 * 1024 * 1024
MAX_WITNESS_OUTPUT_BYTES = 256 * 1024
MAX_WITNESS_SECONDS = 20
# Interpreter executes verified bytes received via stdin, NEVER reopening the
# mutable original Python path. __file__ and argv retain the historical values.
_WITNESS_BOOTSTRAP = (
    "import os,sys\n"
    "_path=sys.argv[1]\n"
    "sys.argv=[_path]\n"
    "sys.path.insert(0,os.path.dirname(_path))\n"
    "_source=sys.stdin.buffer.read()\n"
    "__file__=_path\n"
    "__package__=None\n"
    "exec(compile(_source,_path,'exec'),globals(),globals())\n"
)


class WitnessRefused(Exception):
    """The caller has not authenticated the executable historical witness."""


def _authenticate_witness(path: str, expected_sha256: str | None) -> tuple[str, bytes]:
    """Require a trusted, independently reviewed fingerprint before execution.

    An expected digest must come from a trusted historical manifest or operator;
    computing it from an untrusted path grants no assurance. This is an
    execution authorization boundary, not a read-only Python sandbox.
    """
    if not isinstance(expected_sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", expected_sha256):
        raise WitnessRefused("trusted historical auditor SHA-256 is required")
    auditor = os.path.abspath(path)
    try:
        if os.path.islink(auditor):
            raise WitnessRefused("linked auditor file is not trusted")
        info = os.stat(auditor, follow_symlinks=False)
        if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_WITNESS_BYTES:
            raise WitnessRefused("auditor must be a bounded regular file")
        with open(auditor, "rb") as fh:
            raw = fh.read(MAX_WITNESS_BYTES + 1)
        after = os.stat(auditor, follow_symlinks=False)
        if (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns) != (
                after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            raise WitnessRefused("historical auditor changed during verification")
    except OSError:
        raise WitnessRefused("historical auditor is not accessible") from None
    if len(raw) > MAX_WITNESS_BYTES or hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise WitnessRefused("historical auditor SHA-256 mismatch")
    # The executable is the verified immutable byte snapshot, not this path:
    # another process can replace the path after the hash check completes.
    return auditor, raw


def _run_bounded_witness(auditor: str, source: bytes):
    """Execute only the verified bytes; bound both runtime and captured output.

    POSIX selector pumps a private stdin pipe and reads stdout with a hard cap.
    No temporary script or store file is created by the comparison process.
    """
    import selectors
    import signal
    import subprocess
    import time

    argv = [sys.executable, "-c", _WITNESS_BOOTSTRAP, auditor]
    try:
        proc = subprocess.Popen(
            argv, cwd=os.path.dirname(auditor), stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0,
            start_new_session=True)  # dedicated POSIX process group for descendants
    except OSError:
        raise WitnessRefused("historical witness process could not start") from None

    chunks, size, offset = [], 0, 0
    deadline = time.monotonic() + MAX_WITNESS_SECONDS
    try:
        with selectors.DefaultSelector() as sel:
            os.set_blocking(proc.stdout.fileno(), False)
            sel.register(proc.stdout, selectors.EVENT_READ)
            if source:
                os.set_blocking(proc.stdin.fileno(), False)
                sel.register(proc.stdin, selectors.EVENT_WRITE)
            else:
                proc.stdin.close()

            while True:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise WitnessRefused("historical witness execution timed out")
                for key, _ in sel.select(timeout=min(remaining, 0.2)):
                    if key.fileobj is proc.stdout:
                        # Read just enough to detect a single byte beyond cap.
                        limit = min(65536, MAX_WITNESS_OUTPUT_BYTES + 1 - size)
                        chunk = os.read(proc.stdout.fileno(), limit)
                        if chunk:
                            size += len(chunk)
                            if size > MAX_WITNESS_OUTPUT_BYTES:
                                raise WitnessRefused("historical witness output exceeded limit")
                            chunks.append(chunk)
                        else:
                            sel.unregister(proc.stdout)
                            proc.stdout.close()
                    else:
                        written = os.write(proc.stdin.fileno(), source[offset:offset + 65536])
                        if written <= 0:
                            raise WitnessRefused("historical witness stdin unavailable")
                        offset += written
                        if offset == len(source):
                            sel.unregister(proc.stdin)
                            proc.stdin.close()
                if not sel.get_map():
                    try:
                        proc.wait(timeout=min(0.2, max(0.001, deadline - time.monotonic())))
                        break
                    except subprocess.TimeoutExpired:
                        continue
        if proc.returncode is None:
            raise WitnessRefused("historical witness process did not exit")
        return subprocess.CompletedProcess(
            argv, proc.returncode, stdout=b"".join(chunks).decode("utf-8", "replace"),
            stderr="")
    except (OSError, ValueError, subprocess.TimeoutExpired):
        raise WitnessRefused("historical witness subprocess I/O failed") from None
    finally:
        # A direct proc.kill() cannot stop grandchildren that inherited the
        # stdout pipe or continue running after their parent exits. Kill the
        # dedicated session's group even on a nominally successful return.
        cleanup_failed = False
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass                     # the group exited without descendants
        except OSError:
            cleanup_failed = True    # never silently treat a failed cleanup as PASS
        try:
            proc.wait(timeout=2)
        except (OSError, subprocess.TimeoutExpired):
            cleanup_failed = True
        for stream in (proc.stdin, proc.stdout):
            if stream is not None and not stream.closed:
                try:
                    stream.close()
                except OSError:
                    cleanup_failed = True
        if cleanup_failed:
            raise WitnessRefused("historical witness process-group cleanup failed")


def round1_auditor_witness(auditor_path: str, *, expected_sha256: str | None = None) -> dict:
    """Run Round 1's own frozen auditor and read its three evidence checks out of its output.

    It is a digest-pinned, explicitly authorized executable WITNESS, not a
    read-only sandbox. The numbers are parsed from the checks
    that auditor actually prints (`.distill/round-1/audit_round1.py` [C2]), and a check that
    cannot be parsed is an error that fails the comparison, never a silent zero. It is
    allowed only when a trusted operator supplies the expected historical script hash.
    """
    auditor, source = _authenticate_witness(auditor_path, expected_sha256)
    proc = _run_bounded_witness(auditor, source)
    text = proc.stdout + proc.stderr
    patterns = {
        "refs_total": r"evidence path count == \d+ \(got (\d+)\)",
        "unresolved": r"all (\d+) evidence paths resolve on disk \(failures=(\d+)\)",
        "line_range_violations": r"evidence line ranges within file length \(failures=(\d+)\)",
    }
    out = {"exit_code": proc.returncode, "missing_checks": []}
    m = re.search(patterns["refs_total"], text)
    out["refs_total"] = int(m.group(1)) if m else None
    m = re.search(patterns["unresolved"], text)
    if m:
        out["paths_checked"], out["unresolved"] = int(m.group(1)), int(m.group(2))
    else:
        out["paths_checked"], out["unresolved"] = None, None
        out["missing_checks"].append("evidence path existence check")
    m = re.search(patterns["line_range_violations"], text)
    out["line_range_violations"] = int(m.group(1)) if m else None
    if out["missing_checks"]:
        out["missing_checks"].append("line-range check") if out["line_range_violations"] is None \
            else None
    # The frozen auditor counts a brace-shorthand ref as resolvable because it expands the
    # braces; it prints no shorthand number, so the shorthand column is derived from the same
    # evidence strings Round 1 counted (a property of the citation text, of both sides).
    out["resolved"] = (out["refs_total"] - out["unresolved"]
                       if out["refs_total"] is not None and out["unresolved"] is not None else None)
    return out


def compare_with_round1_auditor(registry: RootRegistry, corpus_files: list,
                               auditor_path: str, *,
                               auditor_sha256: str | None = None) -> dict:
    """Per-count table, plus the weakness gate this round exists for."""
    s14 = round1_universe(registry, corpus_files)
    witness = round1_auditor_witness(auditor_path, expected_sha256=auditor_sha256)
    rows = []
    verdict = "MATCH"
    if witness.get("exit_code") != 0:
        return {"verdict": "WITNESS_FAILED", "s14": s14, "round1_auditor": witness,
                "table": rows, "roots_claimed": len(registry.roots),
                "detail": "historical witness process did not exit successfully"}
    if any(witness.get(k) is None for k in ("refs_total", "unresolved", "line_range_violations")):
        return {"verdict": "WITNESS_UNREADABLE", "s14": s14, "round1_auditor": witness,
                "table": rows, "roots_claimed": len(registry.roots),
                "detail": "Round 1's auditor printed no parseable evidence counts; the "
                          "comparison is refused rather than compared against zeros."}
    # Round 1 counts a brace-shorthand path as resolvable-by-expansion; S14 refuses to expand
    # (contract: exit 2 SHORTHAND). The comparable figure is therefore refs the path really
    # exists for, on both sides.
    auditor_resolvable = witness["refs_total"] - witness["unresolved"]
    s14_covered = s14["covered"]
    table = [
        {"count": "refs total (evidence paths, no dedupe)", "s14": s14["refs_total"],
         "round1_auditor": witness["refs_total"],
         "delta": s14["refs_total"] - witness["refs_total"]},
        {"count": "resolved (file + line range inside it)", "s14": s14["resolved"],
         "round1_auditor": "not checked", "delta": "n/a",
         "note": f"S14 additionally requires a line range: {s14['no_line_range']} refs point at "
                 "a real file and cite no range, which Round 1's auditor never asked for"},
        {"count": "cited path is a readable file", "s14": s14["path_exists"],
         "round1_auditor": auditor_resolvable,
         "delta": s14["path_exists"] - auditor_resolvable},
        {"count": "located by S14 in any form (file+dir+shorthand)", "s14": s14["covered"],
         "round1_auditor": auditor_resolvable, "delta": s14["covered"] - auditor_resolvable,
         "note": "the weakness gate is on THIS row: a path Round 1 could locate must be "
                 "locatable here too, whatever S14 then refuses it for"},
        {"count": "unresolved / refused", "s14": s14["unresolved"] + s14["shorthand"],
         "round1_auditor": witness["unresolved"],
         "delta": s14["unresolved"] + s14["shorthand"] - witness["unresolved"]},
        {"count": "  of which: brace/glob shorthand (exit 2 by contract)",
         "s14": s14["shorthand"], "round1_auditor": "counted as resolvable via expansion",
         "delta": "n/a",
         "note": f"{s14['shorthand_file_exists']} of them have a real file behind the stem; "
                 "S14 refuses to expand a brace, so they stay refusals (SR-2, SR-4)"},
        {"count": "  of which: cited a directory", "s14": s14["cited_directory"],
         "round1_auditor": "counted as resolvable by os.path.exists", "delta": "n/a",
         "note": "a directory cannot be opened for a line range, so S14 refuses it"},
        {"count": "  of which: citation form refused, file exists",
         "s14": s14["refused_citation_file_exists"], "round1_auditor": "counted as resolvable",
         "delta": "n/a", "note": "multi-range forms like `file.ts:91-121,280-282` are not a "
                                 "single file+range; the stem is stat-ed and reported, never "
                                 "silently accepted"},
        {"count": "  of which: NO registered root holds the path",
         "s14": s14["truly_missing"], "round1_auditor": witness["unresolved"],
         "delta": s14["truly_missing"] - witness["unresolved"],
         "note": "THIS is the column a weaker audit would hide in"},
        {"count": "line-range violations", "s14": s14["line_range_violations"],
         "round1_auditor": witness["line_range_violations"],
         "delta": s14["line_range_violations"] - witness["line_range_violations"]},
    ]
    if s14["refs_total"] != witness["refs_total"]:
        verdict = "COUNTS_DIVERGE"
    elif s14["truly_missing"] > witness["unresolved"] or s14_covered < auditor_resolvable:
        verdict = "S14_WEAKER"
        table[-2]["note"] = ("S14 could not find files that Round 1's auditor could, under the "
                             "same root set -- a silently weaker audit, the failure mode this "
                             "round exists to catch")
    elif s14["cited_directory"] or s14["refused_citation_file_exists"] or s14["shorthand"] \
            or s14["line_range_violations"]:
        verdict = "S14_STRICTER_REFUSALS"
    else:
        verdict = "MATCH"
    return {"verdict": verdict, "s14": s14, "round1_auditor": witness, "table": table,
            "roots_claimed": len(registry.roots)}


# --------------------------------------------------------------------- CLI
def _iter_corpus_files(paths: list[str], scan_dir: str | None):
    # Keep explicitly requested missing files so run() reports incomplete coverage.
    files = list(dict.fromkeys(paths))
    if scan_dir:
        for name in sorted(os.listdir(scan_dir)):
            if name.endswith(".json"):
                full = os.path.join(scan_dir, name)
                if os.path.isfile(full) and full not in files:
                    files.append(full)
    return files


def run(argv: list[str]) -> int:
    ap = ArgumentParser(
        prog="kd_refs_audit.py",
        description="S14: recompute evidence reference integrity from disk. "
                    "No globs, no brace expansion, no implicit roots; an empty ref set is "
                    "never reported as success.")
    ap.add_argument("--root", action="append", default=[], metavar="NAME=PATH or PATH",
                    help="registered repository root (repeatable); the first bare root is "
                         "also the default for refs that name no project")
    ap.add_argument("--reference-roots", metavar="WORKSPACE",
                    help="register one EXPLICIT workspace path as the default read-only root "
                         "(RH-P1-06: generic; no bootstrap repo list or monorepo sub-layout is "
                         "baked in -- pass --root NAME=PATH per additional root). No contents are "
                         "walked: each cited path is stat-ed under each registered root.")
    ap.add_argument("--against-round1-auditor", metavar="AUDIT_PY",
                    help="high-trust comparison: execute an explicitly digest-pinned historical "
                         "Python auditor; not sandboxed or automatically read-only")
    ap.add_argument("--auditor-sha256", metavar="EXPECTED_SHA256",
                    help="operator-reviewed SHA-256 required before any historical auditor executes")
    ap.add_argument("--corpus", action="append", default=[], metavar="FILE.json",
                    help="worker/round-1 JSON whose evidence strings are audited (repeatable)")
    ap.add_argument("--refs", action="append", default=[], metavar="FILE.json",
                    help="SC04/SC06-shaped document carrying evidence_refs[] (repeatable)")
    ap.add_argument("--scan-dir", metavar="DIR",
                    help="audit every *.json in DIR as a worker corpus")
    ap.add_argument("--ref", dest="inline", action="append", default=[], metavar="PATH[:N-M]",
                    help="audit a single ref string (repeatable)")
    ap.add_argument("--project", default="", help="project for --ref strings")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON only")
    try:
        args = ap.parse_args(argv)
    except UsageError:
        return EXIT_INVALID_INPUTS

    if not args.root and not args.reference_roots:
        print("SCANNED_SET_INCOMPLETE: no registered root (--root NAME=PATH or "
              "--reference-roots WORKSPACE); refusing to guess a repository root (SR-4).",
              file=sys.stderr)
        return EXIT_SCANNED_SET_INCOMPLETE
    try:
        readonly_specs = reference_root_specs(args.reference_roots) if args.reference_roots else []
        registry = RootRegistry(args.root, readonly_entries=readonly_specs)
    except RootRegistrationError as exc:
        print(f"SCANNED_SET_INCOMPLETE: {exc}. A root that does not exist cannot hold any "
              f"ref, and a scan over it would report weakness rather than misconfiguration.",
              file=sys.stderr)
        return EXIT_SCANNED_SET_INCOMPLETE
    if registry.absent:
        print(f"NOTE: {len(registry.absent)} declared reference root(s) are absent on this "
              f"machine and provide no coverage: {sorted(registry.absent)}", file=sys.stderr)

    if args.auditor_sha256 and not args.against_round1_auditor:
        print("invalid inputs: --auditor-sha256 requires --against-round1-auditor",
              file=sys.stderr)
        return EXIT_INVALID_INPUTS
    if args.against_round1_auditor:
        if not isinstance(args.auditor_sha256, str) or not re.fullmatch(
                r"[0-9a-f]{64}", args.auditor_sha256):
            print("invalid inputs: trusted --auditor-sha256 is mandatory",
                  file=sys.stderr)
            return EXIT_INVALID_INPUTS
        witness_files = _iter_corpus_files(args.corpus, args.scan_dir)
        if not witness_files:
            print("SCANNED_SET_INCOMPLETE: --against-round1-auditor needs a corpus "
                  "(--scan-dir DIR or --corpus FILE); comparing against an empty universe is "
                  "not an audit.", file=sys.stderr)
            return EXIT_SCANNED_SET_INCOMPLETE
        try:
            comparison = compare_with_round1_auditor(
                registry, witness_files, args.against_round1_auditor,
                auditor_sha256=args.auditor_sha256)
        except WitnessRefused as exc:
            print(f"SCANNED_SET_INCOMPLETE: {exc}", file=sys.stderr)
            return EXIT_SCANNED_SET_INCOMPLETE
        comparison["roots_readonly"] = sorted(registry.readonly)
        comparison["roots_absent"] = sorted(registry.absent)
        if args.json:
            print(json.dumps(comparison, ensure_ascii=False, indent=1, default=str))
        else:
            print(f"round-1 cross-check: verdict={comparison['verdict']} "
                  f"roots_claimed={comparison['roots_claimed']}")
            print(f"{'count':52s} {'S14':>7s} {'round-1 auditor':>16s} {'delta':>7s}")
            for row in comparison["table"]:
                print(f"{row['count']:52s} {str(row['s14']):>7s} {str(row['round1_auditor']):>16s}"
                      f" {str(row['delta']):>7s}"
                      + (f"   [{row['note']}]" if row.get("note") else ""))
            for label, rows in (("missing", comparison["s14"]["rows_truly_missing"]),
                                ("dir", comparison["s14"]["rows_cited_directory"]),
                                ("form", comparison["s14"]["rows_refused_citation"]),
                                ("shorthand", comparison["s14"]["shorthand_rows"])):
                for row in rows[:6]:
                    print(f"  {label:9s} {str(row.get('path') or row.get('raw'))[:72]:72s} "
                          f"{row.get('detail') or row.get('shorthand') or row.get('kind') or ''}")
        verdict = comparison["verdict"]
        s14 = comparison["s14"]
        if verdict in ("S14_WEAKER", "COUNTS_DIVERGE", "WITNESS_UNREADABLE", "WITNESS_FAILED"):
            return EXIT_INTEGRITY_FAILED
        if s14["unresolved"] or s14["line_range_violations"] or s14["shorthand"]:
            # the refusals are the contractual finding: shorthand stays exit 2 (SR-2)
            return EXIT_INTEGRITY_FAILED
        return EXIT_OK

    if not args.scan_dir and not args.corpus and not args.refs and not args.inline:
        # one-shot convenience: the first registered root doubles as the corpus directory
        args = argparse.Namespace(**vars(args))
        args.scan_dir = next(iter(registry.roots.values()))

    refs: list[dict] = []
    shortfail: list[dict] = []
    parsed_files: list[str] = []
    unreadable: list[str] = []

    for raw in args.inline:
        try:
            refs.append(parse_ref(raw, project=args.project))
        except RefSyntaxError as exc:
            shortfail.append({"kind": "SHORTHAND", "detail": str(exc), "raw": raw,
                              "ref": {"raw": raw, "path": raw, "project": args.project,
                                      "origin": "--ref", "line_start": None, "line_end": None}})

    for path in _iter_corpus_files(args.corpus, args.scan_dir) + list(args.refs):
        try:
            with open(path, encoding="utf-8") as fh:
                doc = json.load(fh)
        except (OSError, ValueError) as exc:
            unreadable.append(f"{path}: {exc}")
            continue
        parsed_files.append(path)
        if isinstance(doc, dict) and ("mechanisms" in doc or "implementation_evidence" in doc):
            got, bad = harvest_corpus(doc, path)
            refs.extend(got)
            shortfail.extend(bad)
        if isinstance(doc, dict) and isinstance(doc.get("evidence_refs"), list):
            for item in doc["evidence_refs"]:
                raw = item.get("path") if isinstance(item, dict) else item
                origin = "evidence_refs"
                try:
                    ref = parse_ref(raw, project=(item.get("project") if isinstance(item, dict)
                                                  else args.project) or "", origin=origin)
                    if isinstance(item, dict) and item.get("lines"):
                        ref["line_start"] = int(item["lines"]["start"])
                        ref["line_end"] = int(item["lines"]["end"])
                    refs.append(ref)
                except RefSyntaxError as exc:
                    shortfail.append({"kind": "SHORTHAND", "detail": str(exc), "raw": str(raw),
                                      "ref": {"raw": str(raw), "path": str(raw),
                                              "project": args.project, "origin": origin,
                                              "line_start": None, "line_end": None}})

    nothing_scanned = bool(unreadable) or (not parsed_files and not args.inline)
    result = audit_refs(refs, registry)
    status = result["status"]
    if shortfail:
        # brace/glob shorthand is the harder defect class (SR-2): report it as such even
        # when unresolved paths were also found
        status = STATUS_FAIL_SHORTHAND
    elif nothing_scanned:
        # "no corpus read" is not the same answer as "a corpus with zero refs", and neither
        # one is a pass
        status = STATUS_INCOMPLETE
    incomplete = nothing_scanned
    failures = shortfail + [f for f in result["findings"] if f["kind"] != "OK"]
    counts = dict(result["counts"])
    if shortfail:
        counts["SHORTHAND"] = len(shortfail)

    payload = {
        "schema": "refs_integrity/1",
        "status": status,
        "exit_code": status_exit_code(status, incomplete),
        "roots": {k: v for k, v in sorted(registry.roots.items())},
        "scanned": {"corpus_files": len(parsed_files), "files": sorted(parsed_files)[:20],
                    "unreadable_files": unreadable},
        "counts": {"total_refs": result["total_refs"] + len(shortfail),
                   "resolved": result["resolved"],
                   "unresolved": result["unresolved"] + len(shortfail),
                   "shorthand": len(shortfail),
                   "per_kind": counts},
        "resolution_rate": f"{result['resolved']}/"
                           f"{result['total_refs'] + len(shortfail)}",
        "failures": [{"kind": f.get("kind"),
                      "raw": (f.get("ref") or {}).get("raw"),
                      "path": (f.get("ref") or {}).get("path"),
                      "origin": (f.get("ref") or {}).get("origin"),
                      "detail": f.get("detail")} for f in failures[:MAX_FAILURE_ROWS]],
        "failures_omitted": max(0, len(failures) - MAX_FAILURE_ROWS),
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=1))
    else:
        print(f"status={payload['status']} exit={payload['exit_code']} "
              f"resolution={payload['resolution_rate']} "
              f"(total={payload['counts']['total_refs']} resolved={payload['counts']['resolved']} "
              f"unresolved={payload['counts']['unresolved']} shorthand={payload['counts']['shorthand']})")
        print(f"roots={payload['roots']} corpus_files={payload['scanned']['corpus_files']}"
              + (f" unreadable={payload['scanned']['unreadable_files']}"
                 if payload["scanned"]["unreadable_files"] else ""))
        print(f"per_kind={payload['counts']['per_kind']}")
        for row in payload["failures"][:12]:
            print(f"  {row['kind']:22s} {str(row['path'])[:78]:78s} {row['origin'] or ''}")
        if payload["failures_omitted"]:
            print(f"  ... {payload['failures_omitted']} further failures suppressed "
                  "(use --json for the full list)")
    return payload["exit_code"]



class UsageError(Exception):
    """A CLI usage error. argparse exits with code 2 by design, and 2 is a contract code in
    this package (second write path / self-declared provenance / unresolved ref), so usage
    errors must never be able to impersonate one."""


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        print(f"invalid input: {message}", file=sys.stderr)
        raise UsageError(message)

def main(argv: list[str] | None = None) -> int:
    return run(list(sys.argv[1:] if argv is None else argv))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
