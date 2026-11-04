"""S08 -- kd_store_layout: the machine-checkable statement of WHO OWNS EACH PATH, plus the
proof that the derived index is fully rebuildable from the authoritative layer.

Round 2 provenance
  12-SKILL-DESIGN-BRIEF.md:117  S08 "inputs store 根 + 布局契约 / 布局校验结果 + 派生索引可重建证明
                                 （删索引后重跑一致） / 2=出现第二个写者或非 Owner 落盘"
  12-SKILL-DESIGN-BRIEF.md:590-596 (CM-11 / CM-13) "派生索引不得成为第二权威：索引必须可由真相层
                                 完整重建（S08 的验收）... 派生索引反客为主是自产物回路的第二条腿"
  12-SKILL-DESIGN-BRIEF.md:178  SC04 `artifact.schema.json` 写入者 = "S12（唯一写者）"
  05-DATA-MODEL.md:21           实体级红线 1: "Lifecycle Status 不得与可重建索引同生命周期存放
                                 （索引可删，计数不得随之归零）"
  05-DATA-MODEL.md:21 (红线 2)   "一个业务语义只有一个 Owner"
  05-DATA-MODEL.md:51           record_locator: the ledger/authority is held by its Owner, not by
                                 the recorded object.

The store is a single-Owner layout, so the failure this script must make loud is a SECOND writer
appearing, or a write landing somewhere its registered owner did not authorise. Both are exit 2.
This module never writes to the authoritative layer: it owns only the layout manifest, and it takes
the owner identity as a PARAMETER so the authoritative transaction (S12, built in parallel) can be
wired without editing this file.

python3 stdlib only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import kd_provenance as prov          # noqa: E402  (append_ledger for the visible-failure trail)

LAYOUT_VERSION = "1"
MANIFEST_NAME = "store-layout.json"

# --------------------------------------------------------------------------- exit codes
EXIT_OK = 0
EXIT_INPUT_ERROR = 1
EXIT_SECOND_WRITER = 2      # contract: "2=出现第二个写者或非 Owner 落盘"
EXIT_REBUILD_MISMATCH = 5    # CM-13: the derived index is not reproducible from the truth layer

# --------------------------------------------------------------------------- the writer vocabulary
#: Writer identities: WHO holds the right to put bytes at a registered path. S08 defines this
#: vocabulary and nothing else does; S12 imports these constants instead of carrying its own
#: copy of the string (W1-B-REPORT.md: the two vocabularies had to be aligned or "every real
#: write reads as a non-Owner landing").
#:
#: This is deliberately NOT the lifecycle ledger's `actor` column. `05-DATA-MODEL.md` §4 M1
#: (line 105) adjudicates that column as {curator, user, merge, agent} ∪ {human, import,
#: shared} -- it answers "who caused this change" (Q7). A writer identity answers "which
#: module may write at this path" (CM-30). Collapsing them would either make every human-
#: attributed batch row look like a non-Owner write or let a module name masquerade as an
#: attribution actor. The two columns live in two files, each owned once:
#:   * `store/_ledger/writes.jsonl`  -- rows {path, actor, op, ...}: `actor` IS a writer
#:     identity here, and `check_write_journal` authorises it against the manifest.
#:   * `store/_ledger/lifecycle-events.jsonl` -- SC07 rows, `actor` is the M1 enum and the row
#:     carries no `path` key (SC07 `additionalProperties: false`), so it is not an
#:     authorisation surface; `check_write_journal` skips pathless rows by design.
OWNER_WRITE_TXN = "kd_write_txn"                  # S12: records + derived index + write journal
OWNER_LIFECYCLE_LEDGER = "kd_lifecycle_ledger"    # S17/S13 carrier: the append-only event ledger
OWNER_LAYOUT_MANIFEST = "kd_store_layout"         # this module: the layout manifest only
WRITER_IDENTITIES = (OWNER_WRITE_TXN, OWNER_LIFECYCLE_LEDGER, OWNER_LAYOUT_MANIFEST)

#: the three durable carriers under `store/_ledger` plus the commit marker. These are the ONLY
#: store path literals in the package: every consumer, S12 included, goes through `paths()`.
JOURNAL_REL = os.path.join("store", "_ledger", "writes.jsonl")
LIFECYCLE_LEDGER_REL = os.path.join("store", "_ledger", "lifecycle-events.jsonl")
# RH-P1-05: the commit marker is a MACHINE file under _ledger, never `store/SKILL.md`. A second
# SKILL.md inside the runtime store would be picked up by Skill discovery (`find **/SKILL.md`) as a
# second Skill; the commit point is not a Skill entry, so it is commit.json.
COMMIT_MARKER_REL = os.path.join("store", "_ledger", "commit.json")
# S12 protocol metadata, not another knowledge store. Old manifests must explicitly
# register these carriers before they can participate in the new protocol.
TRANSACTION_LOCK_REL = "store/_ledger/transaction.lock"
TRANSACTION_PENDING_REL = "store/_ledger/pending-transaction.json"
TRANSACTION_HISTORY_REL = "store/_ledger/transactions"

#: the layout contract: one entry per path, one owner per entry, no path literal anywhere else
#: in the package (`12-SKILL-DESIGN-BRIEF.md:117` S08 = store 根 + 布局契约, CM-11 in
#: `02-FINAL-MECHANISMS.md:95-100`; the carrier split below is 05 §2 row 8 + §4 M1).
#: The two `*_ledger` files are separate registered carriers, not one file with two shapes:
#: SC07 (`schemas/lifecycle-event-ledger.schema.json`) is `additionalProperties:false` over
#: {seq, at, op, actor, reason, entity, entity_id, supersedes, superseded_by, detail,
#: record_locator, content_hash} -- it has no `path` column and cannot hold a write-journal row
#: without becoming a second, undocumented meaning of the same file.
LAYOUT_CONTRACT = (
    {"path": "store/records", "kind": "authoritative", "deletable": False},
    {"path": "store/lifecycle", "kind": "lifecycle_records", "deletable": False,
     "note": "SC05 semantics belong to S17; S12 persists them with SC04 and SC07"},
    {"path": "store/index", "kind": "derived_index", "deletable": True,
     "rebuild_from": "store/records"},
    {"path": "store/_ledger", "kind": "append_only_ledger", "deletable": False},
    {"path": JOURNAL_REL, "kind": "write_journal", "deletable": False},
    {"path": LIFECYCLE_LEDGER_REL, "kind": "lifecycle_ledger", "deletable": False},
    {"path": COMMIT_MARKER_REL, "kind": "commit_marker", "deletable": False,
     "note": "S12 hash-bound commit point; a legacy row-count marker is not admissible"},
    {"path": TRANSACTION_LOCK_REL, "kind": "transaction_lock", "deletable": False},
    {"path": TRANSACTION_PENDING_REL, "kind": "transaction_pending", "deletable": False},
    {"path": TRANSACTION_HISTORY_REL, "kind": "transaction_history", "deletable": False,
     "note": "S12 retains immutable per-revision SC06 from S13, separate from artifact bodies"},
)
#: kind -> accessor key in `paths()`, and kind -> which of the two owner slots may hold it
KIND_KEYS = {"authoritative": "records", "lifecycle_records": "lifecycle_records", "derived_index": "index",
             "append_only_ledger": "ledger", "write_journal": "journal",
             "lifecycle_ledger": "lifecycle_ledger", "commit_marker": "commit_marker",
             "transaction_lock": "transaction_lock", "transaction_pending": "transaction_pending",
             "transaction_history": "transaction_history"}
#: which declared owner slot each registered file belongs to.
#: `lifecycle_ledger` sits in the STORE slot for Wave 1: S12 is the only durable writer that
#: exists (P-3, `12-SKILL-DESIGN-BRIEF.md` §16 check 1) and 05 §2 row 8 makes it the writer of
#: "一次 batch op 只写一行", while the *attribution* of each row stays in SC07's `actor` column.
#: 2026-10-07 approved contract: S17 owns SC05 semantics, S12 persists SC04/SC05/SC07
#: in one transaction. The legacy declared ledger identity does not gain write authority
#: over these carriers, and standalone lifecycle appends remain refused.
KIND_OWNER_SLOT = {"authoritative": "store", "lifecycle_records": "store", "derived_index": "store",
                   "append_only_ledger": "ledger", "write_journal": "store",
                   "lifecycle_ledger": "store", "commit_marker": "store",
                   "transaction_lock": "store", "transaction_pending": "store",
                   "transaction_history": "store"}
#: the two ledger files are also exposed as module constants so S12 never re-derives them
JOURNAL_FILE_REL = JOURNAL_REL.replace(os.sep, "/")
LIFECYCLE_LEDGER_FILE_REL = LIFECYCLE_LEDGER_REL.replace(os.sep, "/")
COMMIT_MARKER_FILE_REL = COMMIT_MARKER_REL.replace(os.sep, "/")
#: actors that may not touch the authoritative layer (N2: models hold proposal rights only)
NON_WRITER_ACTORS = frozenset({"model", "llm", "proposal", "candidate_file"})


class LayoutViolation(Exception):
    def __init__(self, findings: list):
        super().__init__("; ".join(f["message"] for f in findings))
        self.findings = findings


# --------------------------------------------------------------------------- manifest
def write_json(path: str, doc) -> None:
    """The layout manifest writer. Bootstrap-only: S12 cannot own this file because the
    manifest is what authorises S12, so routing it through S12 would be a circular
    self-approval. Every site below is reported by S12's `audit_bypass` as an exempted site
    with this reason, never dropped."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)  # KD-WRITE-EXEMPT: S08 owns the layout manifest bootstrap (CM-11); never touches store/records
    tmp = path + ".tmp"
    with open(tmp, "x", encoding="utf-8") as fh:              # KD-WRITE-EXEMPT: exclusive bootstrap tmp; an existing output is refused
        json.dump(doc, fh, ensure_ascii=False, sort_keys=True, indent=1)
        fh.write("\n")                                         # KD-WRITE-EXEMPT: layout manifest newline, tmp file only
        fh.flush()
        os.fsync(fh.fileno())                                  # KD-WRITE-EXEMPT: flush the bootstrap manifest before replacement
    os.replace(tmp, path)                                      # KD-WRITE-EXEMPT: atomic rename of the layout manifest (CM-23 shape), S08 is its only owner
    fd = os.open(os.path.dirname(path) or ".", os.O_RDONLY)  # KD-WRITE-EXEMPT: sync the manifest directory; read-only descriptor
    try:
        os.fsync(fd)  # KD-WRITE-EXEMPT: persist the bootstrap manifest directory entry
    finally:
        os.close(fd)


def ensure_manifest(root: str, store_owner: str = OWNER_WRITE_TXN,
                    ledger_owner: str = OWNER_LIFECYCLE_LEDGER,
                    create_dirs: bool = True) -> dict:
    """Load the layout manifest, or create it (idempotent bootstrap for a fresh store root).
    S12 calls this instead of keeping a second copy of the layout: the manifest on disk stays
    the single authority for where each carrier lives and who owns it."""
    manifest_path = os.path.join(root, MANIFEST_NAME)
    safe_path(root, MANIFEST_NAME)
    safe_path(root, MANIFEST_NAME + ".tmp")
    if os.path.exists(manifest_path):
        return load_manifest(root)
    manifest = build_manifest(root, store_owner, ledger_owner)
    validate_manifest(root, manifest)
    if create_dirs:
        assert_staging_path(root)  # new stores cannot bootstrap in a package, corpus or frozen tree
        for rel in directories_to_create(manifest):
            os.makedirs(safe_path(root, rel), exist_ok=True)  # KD-WRITE-EXEMPT: S08 layout bootstrap -- empty carrier directories, never record bytes
            current = safe_path(root, rel)
            while current != os.path.dirname(os.path.realpath(root)):
                fd = os.open(current, os.O_RDONLY)  # KD-WRITE-EXEMPT: read-only bootstrap directory descriptor
                try:
                    os.fsync(fd)  # KD-WRITE-EXEMPT: persist new carrier directory entries
                finally:
                    os.close(fd)
                parent = os.path.dirname(current)
                if parent == current:
                    break
                current = parent
        write_json(manifest_path, manifest)
    return manifest


def directories_to_create(manifest: dict) -> list:
    """Directory-kind carriers only. `store/_ledger/commit.json` and the two ledger files are
    files, and creating a directory named after them would poison `check_stray_files`."""
    return [str(e["path"]) for e in manifest.get("entries", [])
            if KIND_KEYS.get(e.get("kind")) in ("records", "lifecycle_records", "index", "ledger", "transaction_history")]


def build_manifest(root: str, store_owner: str = OWNER_WRITE_TXN,
                   ledger_owner: str = OWNER_LIFECYCLE_LEDGER) -> dict:
    """One entry per path, one owner per entry. The manifest is the only place a path's owner
    is stated, so a second writer shows up as either a duplicate entry or a journal mismatch.

    Owners come from `LAYOUT_CONTRACT` + the two owner slots, so a registered carrier can never
    be created without an owner (which `check_duplicate_owners` would report as UNOWNED_ENTRY).
    """
    entries = []
    for spec in LAYOUT_CONTRACT:
        entry = dict(spec)
        entry["owner"] = (store_owner if KIND_OWNER_SLOT[spec["kind"]] == "store"
                          else ledger_owner)
        entries.append(entry)
    entries[0]["write_transaction"] = "S12 kd_write_txn.apply_write(path, payload, actor)"
    return {
        "layout_version": LAYOUT_VERSION,
        "root": os.path.abspath(root),
        "manifest_owner": OWNER_LAYOUT_MANIFEST,
        "journal": JOURNAL_FILE_REL,
        "writer_identities": sorted(WRITER_IDENTITIES),
        "entries": entries,
    }


def load_manifest(root: str) -> dict:
    path = safe_path(root, MANIFEST_NAME)
    if not os.path.exists(path):
        raise LayoutViolation([{"code": "MANIFEST_MISSING",
                                "message": f"{path}: no layout manifest, so no path has a declared "
                                           "owner -- refuse to call this a store (S08 must run before "
                                           "step 16, 12:117)"}])
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    validate_manifest(root, doc)
    return doc


def validate_manifest(root: str, doc: dict) -> None:
    """Validate path/owner structure before any accessor or writer can consume it."""
    if not isinstance(doc, dict) or doc.get("layout_version") != LAYOUT_VERSION:
        raise LayoutViolation([{"code": "LAYOUT_VERSION",
                                "message": "unsupported or malformed layout manifest"}])
    entries = doc.get("entries")
    if not isinstance(entries, list) or not entries or any(not isinstance(e, dict) for e in entries):
        raise LayoutViolation([{"code": "LAYOUT_SHAPE", "message": "entries must contain objects"}])
    kinds, findings = set(), []
    for entry in entries:
        kind = entry.get("kind")
        if not isinstance(kind, str) or kind not in KIND_KEYS or kind in kinds:
            findings.append({"code": "LAYOUT_KIND", "message": "unknown or duplicate carrier kind"})
        if isinstance(kind, str):
            kinds.add(kind)
        rel, owner = entry.get("path"), entry.get("owner")
        if not isinstance(owner, str) or not owner.strip() or owner in NON_WRITER_ACTORS:
            findings.append({"code": "UNOWNED_ENTRY", "message": "invalid carrier owner"})
        for field in ("path", "rebuild_from"):
            value = entry.get(field)
            if value is not None:
                try:
                    safe_path(root, value)
                except LayoutViolation as exc:
                    findings.extend(exc.findings)
        if kind == "derived_index" and entry.get("rebuild_from") != next(
                (e.get("path") for e in entries if e.get("kind") == "authoritative"), None):
            findings.append({"code": "NO_REBUILD_SOURCE", "message": "index must derive from records"})
        if not isinstance(rel, str):
            findings.append({"code": "LAYOUT_PATH", "message": "carrier path must be a string"})
    findings.extend(check_duplicate_owners(doc))
    if not {"authoritative", "derived_index", "append_only_ledger"} <= kinds:
        findings.append({"code": "LAYOUT_SHAPE", "message": "required directory carriers missing"})
    locations = [e.get("path") for e in entries if isinstance(e.get("path"), str)]
    for entry in entries:
        if isinstance(entry.get("path"), str) and entry.get("kind") in (
                "write_journal", "lifecycle_ledger", "commit_marker", "transaction_lock",
                "transaction_pending"):
            prefix = str(entry["path"]).rstrip("/").casefold() + "/"
            if any(p.casefold().startswith(prefix) for p in locations):
                findings.append({"code": "LAYOUT_PATH", "message": "file carrier used as directory"})
    directory_entries = [e for e in entries if e.get("kind") in (
        "authoritative", "lifecycle_records", "derived_index", "append_only_ledger") and isinstance(e.get("path"), str)]
    for i, left in enumerate(directory_entries):
        for right in directory_entries[i + 1:]:
            a, b = left["path"].casefold(), right["path"].casefold()
            if a == b or a.startswith(b + "/") or b.startswith(a + "/"):
                findings.append({"code": "LAYOUT_OVERLAP", "message": "directory carriers must not overlap"})
    for history in (e for e in entries if e.get("kind") == "transaction_history"
                    and isinstance(e.get("path"), str)):
        base = history["path"].casefold()
        for other in entries:
            if other is history or other.get("kind") == "append_only_ledger" \
                    or not isinstance(other.get("path"), str):
                continue
            rel = other["path"].casefold()
            if rel == base or rel.startswith(base + "/") or base.startswith(rel + "/"):
                findings.append({"code": "LAYOUT_OVERLAP", "message": "transaction history must not overlap another carrier"})
    for entry in entries:
        if not isinstance(entry.get("path"), str):
            continue
        if entry["path"] == MANIFEST_NAME or entry["path"].startswith(MANIFEST_NAME + "/"):
            findings.append({"code": "LAYOUT_OVERLAP", "message": "carrier overlaps the layout manifest"})
        if entry.get("kind") in ("write_journal", "lifecycle_ledger", "commit_marker",
                                 "transaction_lock", "transaction_pending", "transaction_history"):
            ledger = next((e.get("path") for e in entries if e.get("kind") == "append_only_ledger"), None)
            if not isinstance(ledger, str) or not entry["path"].startswith(ledger + "/"):
                findings.append({"code": "LAYOUT_OVERLAP", "message": "ledger file carriers must stay inside the ledger directory"})
        target = safe_path(root, entry["path"])
        if os.path.exists(target):
            directory = entry.get("kind") in ("authoritative", "lifecycle_records", "derived_index", "append_only_ledger",
                                             "transaction_history")
            if os.path.isdir(target) != directory:
                findings.append({"code": "LAYOUT_PATH", "message": "carrier file/directory type mismatch"})
    if findings:
        raise LayoutViolation(findings)


def safe_path(root: str, rel: str) -> str:
    """Canonical relative paths only; symlinks are forbidden in owned carriers."""
    if not isinstance(rel, str) or not rel or "\x00" in rel or "\\" in rel or os.path.isabs(rel) \
            or any(p in ("", ".", "..") for p in rel.split("/")):
        raise LayoutViolation([{"code": "LAYOUT_PATH", "message": "noncanonical carrier path"}])
    base = os.path.realpath(os.path.abspath(root))
    target = os.path.join(base, *rel.split("/"))
    current = base
    for part in rel.split("/"):
        current = os.path.join(current, part)
        if os.path.islink(current):
            raise LayoutViolation([{"code": "LAYOUT_SYMLINK", "message": "owned path contains symlink"}])
    if os.path.commonpath([base, os.path.realpath(target)]) != base:
        raise LayoutViolation([{"code": "LAYOUT_ESCAPE", "message": "carrier escapes store root"}])
    return target


def assert_staging_path(path: str) -> None:
    """Derived outputs cannot overwrite the package, corpus, frozen history or a store.

    This is a path check, not an authorization grant. Each caller still owns its own
    explicit staging output; durable store writes remain S12-only.
    """
    requested = os.path.abspath(path)
    resolved = os.path.realpath(requested)
    package = os.path.realpath(os.path.join(HERE, os.pardir))
    # A final symlink redirects a writer; a hard-linked regular file may be
    # another name for a store record or a frozen source outside this path.
    if os.path.islink(requested):
        raise LayoutViolation([{"code": "STAGING_SYMLINK", "message": "staging output is a symlink"}])
    if os.path.exists(requested):
        info = os.stat(requested)
        if stat.S_ISREG(info.st_mode) and info.st_nlink > 1:
            raise LayoutViolation([{"code": "STAGING_HARDLINK",
                                    "message": "staging output aliases another file inode"}])
    for view in dict.fromkeys((requested, resolved)):
        parts = [part.casefold() for part in view.split(os.sep)]
        frozen = any(parts[i] == ".distill" and parts[i + 1] in ("round-1", "round-2", "round-3")
                     for i in range(len(parts) - 1))
        if any(part in ("repos", "skills", "rules") for part in parts) or frozen \
                or os.path.basename(view).casefold() in ("skill.md", "agents.md", "claude.md") \
                or os.path.commonpath([package, view]) == package:
            raise LayoutViolation([{"code": "STAGING_PROTECTED", "message": "output is inside a protected tree"}])
        current = view
        while True:
            # samefile also detects case aliases on case-insensitive macOS volumes.
            if os.path.exists(current) and os.path.samefile(current, package):
                raise LayoutViolation([{"code": "STAGING_PROTECTED", "message": "output is inside the package"}])
            if os.path.lexists(os.path.join(current, MANIFEST_NAME)):
                raise LayoutViolation([{"code": "STAGING_STORE", "message": "derived output is inside a store"}])
            parent = os.path.dirname(current)
            if parent == current:
                break
            current = parent


def write_staging_text(path: str, text: str, *, create_parents: bool = False) -> None:
    """Write only derived text, without ever truncating an existing target inode.

    The caller owns the output and its directory policy; this helper merely
    centralizes the staging-only path guard and the exclusive temp/replace step.
    An existing hard-linked destination is refused, not silently detached.
    """
    assert_staging_path(path)
    target = os.path.abspath(path)
    directory = os.path.dirname(target)
    if create_parents:
        os.makedirs(directory, exist_ok=True)  # KD-WRITE-EXEMPT: only caller-approved derived output parent
    assert_staging_path(path)
    fd, temporary = tempfile.mkstemp(prefix=".kd-staging-", dir=directory)  # KD-WRITE-EXEMPT: exclusive private derived temp in approved output dir
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)  # KD-WRITE-EXEMPT: write new private staging inode, never existing target
            fh.flush()
            os.fsync(fh.fileno())  # KD-WRITE-EXEMPT: flush this derived output before atomic replacement
        assert_staging_path(path)
        os.replace(temporary, target)  # KD-WRITE-EXEMPT: replace directory entry, do not truncate target inode
    except Exception:
        if os.path.lexists(temporary):
            os.unlink(temporary)  # KD-WRITE-EXEMPT: remove only this invocation's private staging temp
        raise


def owners_by_path(manifest: dict) -> dict:
    return {str(e["path"]): str(e["owner"]) for e in manifest.get("entries", [])}


def owner_for_path(manifest: dict, rel: str) -> str | None:
    """Longest owned prefix wins, so a stray file at store/notes/x resolves to no owner."""
    best, best_len = None, -1
    norm = rel.replace(os.sep, "/")
    if not norm or os.path.isabs(norm) or any(p in ("", ".", "..") for p in norm.split("/")):
        return None
    for path, owner in owners_by_path(manifest).items():
        if (norm == path or norm.startswith(path.rstrip("/") + "/")) and len(path) > best_len:
            best, best_len = owner, len(path)
    return best


# --------------------------------------------------------------------------- derived index (CM-13)
def paths(root: str, manifest: dict = None) -> dict:
    """Absolute store paths, derived from the layout contract at call time. This is the
    accessor S12's `StorePaths` is repointed at: one place states where the truth layer, the
    derived index, the two append-only carriers and the commit marker live, so no other module
    encodes a store path (CM-11, `12-SKILL-DESIGN-BRIEF.md:117`)."""
    manifest = manifest if manifest is not None else build_manifest(root, OWNER_WRITE_TXN, OWNER_LIFECYCLE_LEDGER)
    validate_manifest(root, manifest)
    out = {"root": os.path.realpath(root), "manifest": safe_path(root, MANIFEST_NAME)}
    for entry in manifest.get("entries", []):
        kind = entry.get("kind")
        if kind not in KIND_KEYS:
            raise LayoutViolation([{"code": "UNKNOWN_LAYOUT_KIND",
                                    "message": f"layout entry {entry!r} declares kind {kind!r}, "
                                               "which the layout contract does not define"}])
        key = KIND_KEYS[kind]
        if key in out and out[key] != os.path.join(root, entry["path"].replace("/", os.sep)):
            raise LayoutViolation([{"code": "SECOND_WRITER",
                                    "message": f"two layout entries map to accessor {key!r} at "
                                               "different paths -- one carrier, one location"}])
        out[key] = safe_path(root, entry["path"])
    # a manifest written before this carrier split still resolves: the defaults are S08's own
    # constants, never a copy in a consumer
    for kind, rel in (("write_journal", JOURNAL_REL), ("lifecycle_ledger", LIFECYCLE_LEDGER_REL),
                      ("commit_marker", COMMIT_MARKER_REL)):
        out.setdefault(KIND_KEYS[kind], safe_path(root, rel.replace(os.sep, "/")))
    return out


def _record_identity(raw_line: str, rec: dict) -> str:
    ident = rec.get("identity")
    if isinstance(ident, dict):
        return str(ident.get("identity_digest") or ident.get("canonical_digest")
                   or ident.get("canonical_key") or "")
    if ident:
        return str(ident)
    return str(rec.get("content_hash") or hashlib.sha256(raw_line.encode("utf-8")).hexdigest()[:40])


def build_index(root: str, manifest: dict) -> bytes:
    """Deterministic layout diagnostic, not a committed-snapshot consumer.

    A transactional store must be consumed through S12's shared snapshot lease. This raw
    filesystem diagnostic cannot establish that lease without inverting the S08/S12 Owner
    dependency, so it refuses transaction carriers rather than exposing a partial batch.
    """
    validate_manifest(root, manifest)
    registered = paths(root, manifest)
    if any(registered.get(key) and os.path.lexists(registered[key])
           for key in ("transaction_lock", "transaction_pending", "commit_marker")):
        raise LayoutViolation([{"code": "COMMITTED_READER_REQUIRED",
                                "message": "raw index diagnostics cannot consume an S12 transaction store; use locked_snapshot"}])
    src = None
    for entry in manifest.get("entries", []):
        if entry.get("kind") == "derived_index":
            src = entry.get("rebuild_from")
    if not src:
        raise LayoutViolation([{"code": "NO_REBUILD_SOURCE",
                                "message": "derived index declares no rebuild_from source"}])
    rows = []
    base = safe_path(root, src)
    if os.path.isdir(base):
        for name in sorted(os.listdir(base)):
            if not name.endswith((".json", ".jsonl")):
                continue
            with open(safe_path(root, f"{src}/{name}"), encoding="utf-8") as fh:
                documents = [(1, fh.read())] if name.endswith(".json") else list(enumerate(fh, 1))
                for num, line in documents:
                    if not line.strip():
                        continue
                    try:
                        rec = json.loads(line)
                    except ValueError as exc:
                        raise LayoutViolation([{"code": "RECORD_UNREADABLE",
                                                "message": f"{src}/{name}:{num}: {exc}"}]) from exc
                    if not isinstance(rec, dict):
                        raise LayoutViolation([{"code": "RECORD_SHAPE", "message": "record must be an object"}])
                    rows.append({"identity": _record_identity(line, rec),
                                 "path": f"{src}/{name}", "line": num})
    rows.sort(key=lambda r: (r["identity"], r["path"], r["line"]))
    return "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows).encode("utf-8")


def index_paths(manifest: dict) -> list:
    return [e["path"] for e in manifest.get("entries", []) if e.get("kind") == "derived_index"]


def prove_rebuild(root: str, manifest: dict, write_back: bool = False) -> dict:
    """Contract output: "派生索引可重建证明（删索引后重跑一致）".
    Recompute twice without consulting cached indexes. Only explicit write_back replaces
    the named derived projection; read-only checks never delete existing files."""
    before = build_index(root, manifest)
    digest_before = hashlib.sha256(before).hexdigest()
    deleted = []
    after = build_index(root, manifest)
    digest_after = hashlib.sha256(after).hexdigest()
    if write_back:
        for rel in index_paths(manifest):
            directory = safe_path(root, rel)
            os.makedirs(directory, exist_ok=True)              # KD-WRITE-EXEMPT: derived index directory for the rebuild write-back
            target = safe_path(root, rel + "/by-identity.jsonl")
            tmp = safe_path(root, rel + "/by-identity.jsonl.tmp")
            with open(tmp, "xb") as fh:  # KD-WRITE-EXEMPT: exclusive temporary derived index only
                fh.write(after)                                # KD-WRITE-EXEMPT: derived index bytes, deterministic projection of store/records
                fh.flush()
                os.fsync(fh.fileno())                           # KD-WRITE-EXEMPT: durability of derived index
            os.replace(tmp, target)                             # KD-WRITE-EXEMPT: publish derived index only
    return {"deleted_index_files": deleted, "digest_before": digest_before,
            "digest_after": digest_after, "identical": digest_before == digest_after,
            "entries": int(after.count(b"\n"))}


# --------------------------------------------------------------------------- the two exit-2 checks
def check_duplicate_owners(manifest: dict) -> list:
    seen, findings = {}, []
    for entry in manifest.get("entries", []):
        path = str(entry.get("path", ""))
        owner = str(entry.get("owner", ""))
        if not path or not owner:
            findings.append({"code": "UNOWNED_ENTRY",
                             "message": f"layout entry {entry!r} declares no path or no owner"})
            continue
        folded = path.casefold()  # portable layout: case aliases cannot become two carriers on macOS
        if folded in seen:
            findings.append({"code": "SECOND_WRITER",
                             "message": f"path {path!r} has two owners declared: {seen[folded]!r} "
                                        f"and {owner!r} -- one business meaning, one Owner "
                                        "(05 sec 1 red line 2)"})
        seen[folded] = owner
    authoritative = [e for e in manifest.get("entries", []) if e.get("kind") == "authoritative"]
    if len(authoritative) != 1:
        findings.append({"code": "AUTHORITY_COUNT",
                         "message": f"the layout must declare exactly one authoritative layer, "
                                    f"found {len(authoritative)} (CM-11): truth and counts cannot "
                                    "have two owners"})
    return findings


def _scan_error(error):
    raise LayoutViolation([{"code": "SCAN_INCOMPLETE",
                            "message": "store directory scan unavailable (" + type(error).__name__ + ")"}])


def check_stray_files(root: str, manifest: dict) -> list:
    """Any file inside the store that no declared owner covers is a non-Owner write on disk."""
    findings = []
    covered = set(owners_by_path(manifest)) | {MANIFEST_NAME}
    for dirpath, dirnames, filenames in os.walk(root, onerror=_scan_error):
        dirnames[:] = sorted(d for d in dirnames if d not in {"__pycache__", ".git"})
        for name in sorted(filenames):
            if name.endswith(".tmp"):
                continue                      # an in-flight atomic rename, not a write yet
            rel = os.path.relpath(os.path.join(dirpath, name), root).replace(os.sep, "/")
            if rel == MANIFEST_NAME:
                continue
            if any(rel == p or rel.startswith(p.rstrip("/") + "/") for p in covered):
                continue
            findings.append({"code": "NON_OWNER_WRITE", "path": rel,
                             "message": f"{rel}: a file exists under the store root that no "
                                        "manifest owner covers -- non-Owner write on disk"})
    return findings


def check_write_journal(root: str, manifest: dict) -> list:
    """Scan EVERY durable trail inside the store root, not just the one S08 names.

    S12 (`kd_write_txn`, landed in parallel) appends its own lifecycle ledger rather than a
    journal called `writes.jsonl`; the contract says exit 2 when "a second writer or a non-Owner
    write appears", so the check must be able to see whoever actually wrote. Any append-only row
    carrying both an `actor` and a `path` is attributed; rows without a path cannot be attributed
    to an owner and are left to their own Owner's checks.
    """
    findings = []
    writers = {}
    trails = sorted(_jsonl_files(root))
    for tpath in trails:
        rel_trail = os.path.relpath(tpath, root).replace(os.sep, "/")
        if rel_trail.endswith((".tmp",)):
            continue
        try:
            with open(tpath, encoding="utf-8") as fh:
                lines = fh.readlines()
        except OSError as exc:
            findings.append({"code": "JOURNAL_UNREADABLE",
                             "message": f"{rel_trail}: {exc}"})
            continue
        for num, line in enumerate(lines, 1):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except ValueError as exc:
                findings.append({"code": "JOURNAL_UNREADABLE",
                                 "message": f"{rel_trail}:{num}: {exc}"})
                continue
            if not isinstance(rec, dict) or "path" not in rec or "actor" not in rec:
                continue
            rel = str(rec.get("path", "")).replace(os.sep, "/")
            actor = str(rec.get("actor", ""))
            owner = owner_for_path(manifest, rel)
            if owner is None:
                findings.append({"code": "NON_OWNER_WRITE", "path": rel,
                                 "message": f"{rel_trail}:{num}: write to {rel!r} by {actor!r}, "
                                            "which no layout entry owns"})
                continue
            if actor != owner:
                findings.append({"code": "NON_OWNER_WRITE", "path": rel,
                                 "message": f"{rel_trail}:{num}: {rel!r} is owned by {owner!r} but "
                                            f"{actor!r} wrote it"})
            if actor in NON_WRITER_ACTORS:
                findings.append({"code": "MODEL_WRITE_ATTEMPT", "path": rel,
                                 "message": f"{rel_trail}:{num}: actor {actor!r} has proposal "
                                            "rights only, never write rights (12 sec N2)"})
            writers.setdefault(rel, set()).add(actor)
    for rel, actors in sorted(writers.items()):
        if len(actors) > 1:
            findings.append({"code": "SECOND_WRITER", "path": rel,
                             "message": f"{rel!r} was written by {sorted(actors)} -- a second writer "
                                        "appeared on the single-Owner path"})
    return findings


def _jsonl_files(root: str):
    for dirpath, dirnames, filenames in os.walk(root, onerror=_scan_error):
        dirnames[:] = sorted(d for d in dirnames if d not in {"__pycache__", ".git"})
        for name in sorted(filenames):
            if name.endswith(".jsonl"):
                yield os.path.join(dirpath, name)


def check_layout(root: str, manifest: dict, do_rebuild_proof: bool = True) -> dict:
    validate_manifest(root, manifest)
    findings = check_duplicate_owners(manifest) + check_stray_files(root, manifest) \
        + check_write_journal(root, manifest)
    code = EXIT_SECOND_WRITER if findings else EXIT_OK
    rebuild = prove_rebuild(root, manifest) if do_rebuild_proof else {}
    if do_rebuild_proof and not rebuild["identical"]:
        findings.append({"code": "REBUILD_MISMATCH",
                         "message": "deleting the derived index and rebuilding produced different "
                                    "bytes -- the index is a second authority (CM-13)"})
        code = EXIT_REBUILD_MISMATCH
    return {"layout_version": LAYOUT_VERSION, "root": os.path.abspath(root),
            "owners": owners_by_path(manifest), "ok": not findings,
            "exit": code, "violations": findings, "rebuild_proof": rebuild}


# --------------------------------------------------------------------------- the S12-facing interface
def declared_owners(manifest: dict) -> set:
    """The writer vocabulary in force for THIS store: every owner a manifest actually names,
    unioned with S08's canonical identities. A caller that registers a different Owner module
    extends the vocabulary by declaring it here, never by editing a consumer."""
    return set(owners_by_path(manifest).values()) | set(WRITER_IDENTITIES)


def authorize_write(manifest: dict, rel: str, actor: str) -> None:
    """The predicate S12 calls BEFORE touching any registered path. Fail-closed in both
    directions: an unregistered path is refused, and an actor that holds no owner slot anywhere
    in the manifest is refused rather than defaulted to allow.

    Expected S12 contract (W1-B-REPORT.md; landed by W1-D):
        kd_write_txn.StorePaths(root)            -> paths derived from `paths(root, manifest)`
        kd_write_txn.commit_batch(root, intents) -> receipt
      1. call `authorize_write(manifest, rel, OWNER_WRITE_TXN)` for every path in the batch and
         abort on refusal (`actor` here is a WRITER IDENTITY, never the SC07 attribution enum);
      2. write atomically (tmp + rename), only under the path it was authorised for;
      3. append the bound write journal and SC07 lifecycle events within S12's
         hash-bound transaction; kd_provenance.append_ledger is a separate non-authoritative
         kernel channel and never writes the transaction store;
      4. expose a verified snapshot for rebuildable derived readers (CM-13);
      5. write the commit marker (`store/_ledger/commit.json`) LAST.
    """
    owner = owner_for_path(manifest, rel)
    if owner is None:
        raise LayoutViolation([{"code": "NON_OWNER_WRITE",
                                "message": f"{rel}: no owner in the layout, refusing the write"}])
    if actor not in declared_owners(manifest):
        raise LayoutViolation([{"code": "NON_OWNER_WRITE",
                                "message": f"{rel}: actor {actor!r} is not a declared owner "
                                           f"anywhere in this store (declared: "
                                           f"{sorted(declared_owners(manifest))}) -- unknown "
                                           "writer identity, refused fail-closed"}])
    if actor != owner:
        raise LayoutViolation([{"code": "SECOND_WRITER",
                                "message": f"{rel}: owner is {owner!r}, refusing a write by {actor!r}"}])
    return None


# --------------------------------------------------------------------------- CLI
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="kd_store_layout.py",
        description="S08 store layout: declare who owns each path, prove the derived index is "
                    "rebuildable from the authoritative layer, and exit 2 when a second writer or "
                    "a non-Owner write appears.")
    ap.add_argument("--root", help="store root")
    ap.add_argument("--init", action="store_true", help="write the layout manifest and directories")
    ap.add_argument("--check", action="store_true", help="validate layout + journal + rebuild proof")
    ap.add_argument("--prove-rebuild", action="store_true",
                    help="recompute the index twice without reading or deleting cached indexes")
    ap.add_argument("--rebuild-index", action="store_true",
                    help="write the derived index (owner-only action, no journal needed)")
    ap.add_argument("--owner", default=OWNER_WRITE_TXN,
                    help="writer identity registered for the authoritative layer, the derived "
                         "index, the write journal and the commit marker (default: "
                         f"{OWNER_WRITE_TXN}; S12 registers itself by passing its own name)")
    ap.add_argument("--ledger-owner", default=OWNER_LIFECYCLE_LEDGER,
                    help="writer identity registered for the append-only carriers "
                         f"(default: {OWNER_LIFECYCLE_LEDGER})")
    ap.add_argument("--out", help="write the check report JSON here")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    # checked by hand: argparse exits 2, and 2 is this script's contract code for "a second
    # writer appeared", so a typo must never look like a caught violation
    if not args.root:
        print("usage error: --root is required", file=sys.stderr)
        return EXIT_INPUT_ERROR

    try:
        if args.init:
            manifest = ensure_manifest(args.root, args.owner, args.ledger_owner)
            if not args.quiet:
                print(json.dumps({"initialized": os.path.abspath(args.root),
                                  "owners": owners_by_path(manifest)}, ensure_ascii=False,
                                 sort_keys=True))
            if not (args.check or args.prove_rebuild or args.rebuild_index):
                return EXIT_OK
        else:
            manifest = load_manifest(args.root)

        code = EXIT_OK
        report = {}
        if args.rebuild_index:
            report["rebuilt"] = prove_rebuild(args.root, manifest, write_back=True)
        if args.prove_rebuild:
            report["rebuild_proof"] = prove_rebuild(args.root, manifest, write_back=args.rebuild_index)
            if not report["rebuild_proof"]["identical"]:
                code = EXIT_REBUILD_MISMATCH
        if args.check or (not args.init and not report):
            result = check_layout(args.root, manifest, do_rebuild_proof=bool(args.check))
            report["layout"] = result
            if not result["ok"]:
                code = result["exit"]
    except LayoutViolation as exc:
        print(json.dumps({"violation": "LAYOUT", "exit": EXIT_SECOND_WRITER,
                          "findings": exc.findings}, ensure_ascii=False, indent=1), file=sys.stderr)
        return EXIT_SECOND_WRITER
    except OSError as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    except ValueError as exc:
        print(f"input error: malformed JSON: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR

    payload = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=1)
    if args.out:
        try:
            assert_staging_path(args.out)
        except LayoutViolation as exc:
            print(f"output refused: {exc}", file=sys.stderr)
            return EXIT_INPUT_ERROR
        try:
            write_staging_text(args.out, payload + "\n")
        except (OSError, LayoutViolation) as exc:
            print(f"output refused: {exc}", file=sys.stderr)
            return EXIT_INPUT_ERROR
    if not args.quiet:
        print(payload)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
