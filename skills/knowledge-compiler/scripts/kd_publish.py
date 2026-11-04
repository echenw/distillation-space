"""Deterministic, derived Markdown publication (Plan 33/35/P2/P3).

Callers create an empty projection directory and explicitly admit a publication policy.
They consume current.json, then generations/<generation>/manifest.json; no host loader is
installed here. Records stay authoritative. A failed/incomplete generation or pointer
temporary is retained, and later publication refuses until the caller explicitly inspects
and recovers its OWN projection directory. This module never deletes files or writes a store.

Lock order is S12 locked_snapshot LOCK_SH, then nonblocking projection LOCK_EX. The lease covers
planning, generation creation, integrity checks, and the pointer CAS. Generations contain
unchanged UTF-8 record.body bytes, not a second model result. Frontmatter supports only flat,
single-line string scalars: complex YAML is a visible refusal, never silently rewritten.

publication_policy requires status='admitted', decision_id, budget_config (SC10), and explicit
object_classes={rule: rule_body, skill: skill_task}.
No inherited index or Skill line-size ceiling is imposed by default. Optional
caller-provided class-specific caps remain enforceable. Optional protected_roots extends the path
boundary for other caller-owned roots; it is path input, not a second knowledge/schema registry.
S12's authenticated snapshot supplies all committed external source roots automatically.
"""
from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import stat
import unicodedata
import uuid
from contextlib import contextmanager

import kd_budget as budget
import kd_store_layout as layout
import kd_validate as validator
import kd_write_txn as txn
import kd_skill_metadata as metadata

GENERATOR = "kd_publish"
VERSION = "1"
MARKER = ".kd-projection.json"
LOCK = ".kd-publish.lock"
CURRENT = "current.json"
MANIFEST = "manifest.json"
_HEX = re.compile(r"[0-9a-f]{64}\Z")
_AID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")
_DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW


class PublishError(Exception):
    """A visible refusal; code and generation disclose no knowledge body or credentials."""

    def __init__(self, code: str, detail: str, *, generation=None):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.generation = generation


def _refuse(code, detail):
    raise PublishError(code, detail)


def _json_bytes(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False,
                       separators=(",", ":")) + "\n").encode("utf-8")


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def _copy_json(value):
    try:
        return json.loads(_json_bytes(value))
    except (TypeError, ValueError, UnicodeError):
        _refuse("INVALID_INPUT", "inputs must be finite UTF-8 JSON values")


def _fold(value):
    return unicodedata.normalize("NFC", value).casefold()


def _absolute(value):
    try:
        path = os.fspath(value)
    except TypeError:
        _refuse("UNSAFE_PATH", "roots must be explicit absolute directory paths")
    if not isinstance(path, str) or not os.path.isabs(path) or "\0" in path \
            or path != os.path.normpath(path) or path == os.path.sep:
        _refuse("UNSAFE_PATH", "root must be a normalized absolute directory path")
    return path


def _overlap(left, right):
    a, b = _fold(left.rstrip(os.sep)), _fold(right.rstrip(os.sep))
    return a == b or a.startswith(b + os.sep) or b.startswith(a + os.sep)


def _forbidden(path):
    parts = [_fold(p) for p in path.split(os.sep)]
    if any(p in {".git", ".distill", "repos", "round-1", "round-2", "round-3"} for p in parts):
        _refuse("PROTECTED_PATH", "repository metadata, source mirrors and frozen roots are forbidden")
    if any(a == ".codex" and b == "skills" for a, b in zip(parts, parts[1:])):
        _refuse("PROTECTED_PATH", "publication does not install personal host skills")
    package = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _overlap(path, package):
        _refuse("PROTECTED_PATH", "the distributed package tree is not a publication/store root")


def _names(fd):
    names = os.listdir(fd)
    if len({_fold(n) for n in names}) != len(names):
        _refuse("CASE_ALIAS", "directory contains ambiguous case/Unicode aliases")
    return set(names)


def _exact(fd, name):
    matches = [n for n in _names(fd) if _fold(n) == _fold(name)]
    if matches and matches != [name]:
        _refuse("CASE_ALIAS", "a path component differs from its on-disk spelling")


def _directory(fd, name):
    _exact(fd, name)
    return os.open(name, _DIR_FLAGS, dir_fd=fd)  # KD-WRITE-EXEMPT: read-only derived/path-boundary directory descriptor, no record write capability


@contextmanager
def _absolute_dir(path):
    """Open every component without following links, including ancestor case aliases."""
    fd = os.open(os.path.sep, _DIR_FLAGS)  # KD-WRITE-EXEMPT: read-only ancestor descriptor used to reject aliases; never a write target
    try:
        for part in path.split(os.sep)[1:]:
            child = _directory(fd, part)
            os.close(fd)
            fd = child
        yield fd
    finally:
        os.close(fd)


def _read(fd, name):
    _exact(fd, name)
    handle = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                     dir_fd=fd)  # KD-WRITE-EXEMPT: read-only projection/control file, no authoritative writes
    try:
        before = os.fstat(handle)
        named = os.stat(name, dir_fd=fd, follow_symlinks=False)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            _refuse("UNSAFE_PATH", "files must be regular, singly linked and owned at their exact path")
        if (before.st_dev, before.st_ino) != (named.st_dev, named.st_ino):
            _refuse("MANUAL_TAMPER", "file was replaced during integrity inspection")
        chunks = []
        while True:
            chunk = os.read(handle, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(handle)
        named = os.stat(name, dir_fd=fd, follow_symlinks=False)
        if (before.st_size, before.st_mtime_ns, before.st_ctime_ns) != \
                (after.st_size, after.st_mtime_ns, after.st_ctime_ns) \
                or (before.st_dev, before.st_ino) != (named.st_dev, named.st_ino) \
                or named.st_nlink != 1:
            _refuse("MANUAL_TAMPER", "file changed during integrity inspection")
        return b"".join(chunks)
    finally:
        os.close(handle)


def _document(data):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError("duplicate JSON key")
            out[key] = value
        return out

    try:
        doc = json.loads(data.decode("utf-8"), object_pairs_hook=unique)
        if not isinstance(doc, dict) or _json_bytes(doc) != data:
            raise ValueError("not canonical object bytes")
        return doc
    except (ValueError, TypeError, UnicodeError):
        _refuse("MANUAL_TAMPER", "derived metadata is invalid or differs from generator bytes")


def _safe_aid(value):
    if not isinstance(value, str) or not _AID.fullmatch(value) or value.endswith("."):
        _refuse("UNSAFE_PATH", "artifact_id cannot be mapped to a safe Markdown filename")
    return value


def _skill_name(body):
    try:
        return metadata.parse_frontmatter(body)["name"]
    except metadata.MetadataError as exc:
        code = ("INVALID_FRONTMATTER" if exc.code in
                {"FRONTMATTER", "NAME_INVALID", "METADATA_MISSING"}
                else "UNSUPPORTED_FRONTMATTER")
        _refuse(code, "Skill frontmatter does not satisfy the shared string/metadata-map contract")


def _budget_verdict(cfg, body, object_class):
    try:
        verdict = budget.check_write(cfg, body, object_class)
    except (budget.BudgetConfigError, KeyError, TypeError, ValueError):
        _refuse("BUDGET_REFUSED", "S18 could not decide the complete artifact budget")
    # Successful S18 verdicts also call the enforcement disposition 'hard_refusal'; the
    # boolean and exit, not that policy label, distinguish an actual refusal.
    if verdict.get("cannot_decide") or verdict.get("exit") != 0 or verdict.get("hard_refusal"):
        _refuse("BUDGET_REFUSED", "S18 refused or could not decide the complete artifact budget")


def _policy(policy):
    policy = _copy_json(policy)
    if not isinstance(policy, dict) or policy.get("status") != "admitted" \
            or not isinstance(policy.get("decision_id"), str) or not policy["decision_id"].strip():
        _refuse("POLICY_NOT_ADMITTED", "caller must explicitly admit publication and identify its decision")
    cfg, classes = policy.get("budget_config"), policy.get("object_classes")
    if not isinstance(cfg, dict) or not isinstance(classes, dict) or set(classes) != {"rule", "skill"}:
        _refuse("POLICY_NOT_ADMITTED", "explicit SC10 budget config and rule/skill classes are required")
    try:
        budget.validate_shape(cfg, "publication_policy.budget_config")
    except (budget.BudgetConfigError, KeyError, TypeError, ValueError, AttributeError):
        _refuse("BUDGET_REFUSED", "S18 rejected budget_config shape")
    if not validator.validate_artifact("budget-config", cfg)["valid"]:
        _refuse("BUDGET_REFUSED", "budget_config does not satisfy its existing SC10 schema")
    for kind in ("rule", "skill"):
        object_class = classes[kind]
        if (kind == "rule" and object_class != "rule_body") or \
                (kind == "skill" and object_class != "skill_task"):
            _refuse("BUDGET_REFUSED", "rule_body and skill_task are the only approved whole-artifact classes; an index budget cannot limit a Rule body")
        _budget_verdict(cfg, "", object_class)
    roots = policy.get("protected_roots", [])
    if not isinstance(roots, list):
        _refuse("UNSAFE_PATH", "protected_roots must be an explicit list of absolute source roots")
    for root in roots:
        _absolute(root)
    return policy


def plan_projection(snapshot, *, scope, publication_policy):
    """Pure deterministic plan. Pass a snapshot from S12 read_snapshot/locked_snapshot.

    This helper does NOT authenticate a caller-supplied dict or authorize switching. publish
    always obtains its own S12 lease. Mixed active rule/skill Scopes are refused as a batch;
    inactive records and other artifact kinds never become Markdown output.
    """
    policy, scope = _policy(publication_policy), _copy_json(scope)
    if not validator.validate_artifact("scope-tuple", scope)["valid"]:
        _refuse("SCOPE_MISMATCH", "caller must declare one valid exact SC11 Scope")
    if not isinstance(snapshot, dict) or snapshot.get("state") != "COMMITTED" \
            or not isinstance(snapshot.get("marker"), dict) or not snapshot["marker"] \
            or not isinstance(snapshot.get("snapshot_digest"), str) \
            or not _HEX.fullmatch(snapshot["snapshot_digest"]) \
            or not isinstance(snapshot.get("records"), dict):
        _refuse("UNCOMMITTED", "only a complete S12 committed snapshot is publishable")
    digest, files, entries = snapshot["snapshot_digest"], {}, []
    used = set()
    for aid, record in sorted(snapshot["records"].items()):
        if not isinstance(record, dict):
            _refuse("INCOMPLETE_RECORD", "committed record is not an artifact object")
        if record.get("state") != "active" or record.get("kind") not in {"rule", "skill"}:
            continue
        if record.get("scope") != scope:
            _refuse("SCOPE_MISMATCH", "active rule/skill does not belong to the caller's exact Scope")
        if record.get("artifact_id") != aid or not validator.validate_artifact("artifact", record)["valid"] \
                or type(record.get("revision")) is not int or record["revision"] < 1:
            _refuse("INCOMPLETE_RECORD", "active artifact identity/revision/SC04 is incomplete")
        safeaid, body, kind = _safe_aid(aid), record["body"], record["kind"]
        try:
            data = body.encode("utf-8")
        except UnicodeError:
            _refuse("INCOMPLETE_RECORD", "body is not representable as unchanged UTF-8 bytes")
        _budget_verdict(policy["budget_config"], body, policy["object_classes"][kind])
        path = f"rules/{safeaid}.md" if kind == "rule" else f"skills/{_skill_name(body)}/SKILL.md"
        if _fold(path) in used:
            _refuse("PATH_COLLISION", "two active artifacts map to the same Markdown/Skill path")
        used.add(_fold(path))
        files[path] = data
        entries.append({"artifact_id": aid, "revision": record["revision"], "kind": kind,
                        "path": path, "hash": _sha(data), "record_content_hash": record["content_hash"],
                        "source_snapshot": digest, "generator": GENERATOR, "version": VERSION})
    base = {"source_snapshot": digest, "publication_policy_hash": _sha(_json_bytes(policy)),
            "publication_decision": policy["decision_id"], "scope": scope,
            "generator": GENERATOR, "version": VERSION, "entries": entries}
    generation = _sha(_json_bytes(base))
    manifest = _json_bytes(dict(base, generation=generation))
    return {"generation": generation, "source_snapshot": digest, "files": files,
            "manifest": manifest, "manifest_hash": _sha(manifest)}


def _protected_paths(store, policy):
    paths = txn.resolve_paths(store)  # public, read-only; never bootstrap a store
    roots = [os.path.join(store, e["path"].replace("/", os.sep)) for e in paths.manifest["entries"]]
    roots.append(os.path.join(store, layout.MANIFEST_NAME))
    carrier_parent = os.path.commonpath((paths.records, paths.ledger_dir))
    if carrier_parent != store:
        roots.append(carrier_parent)
    # Plan 11's non-projection carriers are outside S08's record/ledger layout.
    roots.extend(os.path.join(store, n) for n in ("evidence", "candidates", "evals", "distillation"))
    roots.extend(policy.get("protected_roots", []))
    # Resolve protected boundaries too: an externally registered evidence-root alias must
    # not allow writing through its other spelling. No evidence content is read here.
    return roots + [os.path.realpath(path) for path in roots]


def _check_location(store, root, policy, source_roots=()):
    _forbidden(store)
    _forbidden(root)
    if root == store or any(_overlap(root, path) for path in _protected_paths(store, policy)):
        _refuse("PROTECTED_PATH", "projection root overlaps store, ledger, evidence or other protected carriers")
    if any(_overlap(root, source) or _overlap(root, os.path.realpath(source)) for source in source_roots):
        _refuse("PROTECTED_PATH", "projection root overlaps an S12-bound external source root")


def _write(fd, name, data):
    """Exclusive new derived file. No existing file is overwritten by this primitive."""
    _exact(fd, name)
    handle = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                     0o600, dir_fd=fd)  # KD-WRITE-EXEMPT: exclusive creation inside the owned projection root only; never records/ledger/evidence
    try:
        view = memoryview(data)
        while view:
            size = os.write(handle, view)  # KD-WRITE-EXEMPT: unchanged derived Markdown/manifest/control bytes only, no record write authority
            if size <= 0:
                raise OSError("derived file write made no progress")
            view = view[size:]
        os.fchmod(handle, 0o444)  # KD-WRITE-EXEMPT: seal this newly created derived file, never chmod a store file
        os.fsync(handle)  # KD-WRITE-EXEMPT: persist only this new derived projection file
    finally:
        os.close(handle)
    os.fsync(fd)  # KD-WRITE-EXEMPT: persist the owned projection directory's new file entry only


def _mkdir(fd, name):
    _exact(fd, name)
    os.mkdir(name, 0o700, dir_fd=fd)  # KD-WRITE-EXEMPT: exclusive derived generation directory in the owned projection root; no store bootstrap
    os.fsync(fd)  # KD-WRITE-EXEMPT: persist only the derived directory entry


def _tree(fd, *, immutable=False, prefix=""):
    files, dirs = {}, set()
    for name in sorted(_names(fd)):
        meta = os.stat(name, dir_fd=fd, follow_symlinks=False)
        rel = prefix + name
        if immutable and meta.st_mode & 0o222:
            _refuse("MANUAL_TAMPER", "an immutable generation was made writable")
        if stat.S_ISDIR(meta.st_mode):
            child = _directory(fd, name)
            try:
                subfiles, subdirs = _tree(child, immutable=immutable, prefix=rel + "/")
                files.update(subfiles)
                dirs.update(subdirs)
                dirs.add(rel)
            finally:
                os.close(child)
        elif stat.S_ISREG(meta.st_mode):
            files[rel] = _read(fd, name)
        else:
            _refuse("UNSAFE_PATH", "projection contains a symlink or special file")
    return files, dirs


def _generation(fd, generation):
    if not _HEX.fullmatch(generation):
        _refuse("UNKNOWN_FILE", "generation directory name is not a generator digest")
    child = _directory(fd, generation)
    try:
        if os.fstat(child).st_mode & 0o222:
            _refuse("RECOVERY_REQUIRED", "generation is incomplete or has been made writable")
        files, dirs = _tree(child, immutable=True)
    finally:
        os.close(child)
    if MANIFEST not in files:
        _refuse("RECOVERY_REQUIRED", "incomplete generation retained; explicit inspection/recovery required")
    raw = files.pop(MANIFEST)
    doc = _document(raw)
    keys = {"generation", "source_snapshot", "publication_policy_hash", "publication_decision",
            "scope", "generator", "version", "entries"}
    if set(doc) != keys or doc["generation"] != generation or doc["generator"] != GENERATOR \
            or doc["version"] != VERSION \
            or not isinstance(doc["source_snapshot"], str) or not _HEX.fullmatch(doc["source_snapshot"]) \
            or not isinstance(doc["publication_policy_hash"], str) or not _HEX.fullmatch(doc["publication_policy_hash"]) \
            or not isinstance(doc["publication_decision"], str) or not doc["publication_decision"].strip() \
            or not isinstance(doc["entries"], list) \
            or not validator.validate_artifact("scope-tuple", doc["scope"])["valid"] \
            or _sha(_json_bytes({k: v for k, v in doc.items() if k != "generation"})) != generation:
        _refuse("MANUAL_TAMPER", "manifest no longer binds its immutable generation")
    expected, expected_dirs, aids = {}, {"rules", "skills"}, set()
    for entry in doc["entries"]:
        entry_keys = {"artifact_id", "revision", "kind", "path", "hash", "record_content_hash",
                      "source_snapshot", "generator", "version"}
        if not isinstance(entry, dict) or set(entry) != entry_keys:
            _refuse("MANUAL_TAMPER", "manifest entry is incomplete")
        aid, path = _safe_aid(entry["artifact_id"]), entry["path"]
        if not isinstance(path, str) or type(entry["revision"]) is not int or entry["revision"] < 1 \
                or not isinstance(entry["hash"], str) or not _HEX.fullmatch(entry["hash"]) \
                or not isinstance(entry["record_content_hash"], str) or not _HEX.fullmatch(entry["record_content_hash"]) \
                or entry["hash"] != entry["record_content_hash"] \
                or entry["source_snapshot"] != doc["source_snapshot"] \
                or entry["generator"] != doc["generator"] or entry["version"] != doc["version"]:
            _refuse("MANUAL_TAMPER", "manifest entry lost its source/revision/hash binding")
        if entry["kind"] == "rule":
            valid = path == f"rules/{aid}.md"
        elif entry["kind"] == "skill":
            bits = path.split("/")
            valid = len(bits) == 3 and bits[0] == "skills" and bits[2] == "SKILL.md" \
                and metadata.is_skill_name(bits[1])
            if valid:
                expected_dirs.add("skills/" + bits[1])
        else:
            valid = False
        if not valid or _fold(path) in {_fold(p) for p in expected} or _fold(aid) in aids:
            _refuse("MANUAL_TAMPER", "manifest has unsafe, repeated or colliding artifact paths")
        expected[path] = entry["hash"]
        aids.add(_fold(aid))
    if set(files) != set(expected) or dirs != expected_dirs:
        _refuse("UNKNOWN_FILE", "generation has unknown or missing files/directories; differences are preserved")
    if any(_sha(data) != expected[path] for path, data in files.items()):
        _refuse("MANUAL_TAMPER", "generated Markdown differs from its manifest; manual bytes are preserved")
    return {"generation": generation, "source_snapshot": doc["source_snapshot"],
            "manifest_hash": _sha(raw), "generator": doc["generator"], "version": doc["version"]}


def _marker(root):
    return {"owner": GENERATOR, "format": VERSION, "projection_root": root}


def read_publication(projection_root, *, expected_generation, expected_snapshot_digest, scope):
    """Read only a pinned intact active generation, under a shared projection lease.

    Unreferenced failed generations/pointer temporaries are preserved and never loaded.
    They still prevent further publication until explicit recovery, but cannot hide an
    intact older active generation. This is a versioned reader, not host installation or
    a lifecycle use-event producer. Every returned byte is bound to the manifest/Scope.
    """
    root, scope = _absolute(projection_root), _copy_json(scope)
    if not isinstance(expected_generation, str) or not _HEX.fullmatch(expected_generation) \
            or not isinstance(expected_snapshot_digest, str) or not _HEX.fullmatch(expected_snapshot_digest):
        _refuse("INVALID_INPUT", "consumer must pin generation and S12 snapshot digests")
    if not validator.validate_artifact("scope-tuple", scope)["valid"]:
        _refuse("SCOPE_MISMATCH", "consumer must declare one exact Scope")
    try:
        with _absolute_dir(root) as fd:
            _exact(fd, LOCK)
            lockfd = os.open(LOCK, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
            try:
                meta = os.fstat(lockfd)
                if not stat.S_ISREG(meta.st_mode) or meta.st_nlink != 1 or meta.st_size:
                    _refuse("UNSAFE_PATH", "consumer lease requires the existing empty singly linked lock")
                try:
                    fcntl.flock(lockfd, fcntl.LOCK_SH | fcntl.LOCK_NB)
                except BlockingIOError:
                    _refuse("PROJECTOR_BUSY", "publication is in progress; no automatic retry")
                _binding(fd, lockfd, root)
                if _document(_read(fd, MARKER)) != _marker(root):
                    _refuse("UNMANAGED_ROOT", "consumer refuses an unowned projection root")
                pointer = _document(_read(fd, CURRENT))
                if pointer.get("generation") != expected_generation:
                    _refuse("STALE_GENERATION", "active generation differs from the pinned version")
                if pointer.get("source_snapshot") != expected_snapshot_digest:
                    _refuse("STALE_SNAPSHOT", "active projection describes a different S12 snapshot")
                genfd = _directory(fd, "generations")
                try:
                    if _generation(genfd, expected_generation) != pointer:
                        _refuse("MANUAL_TAMPER", "pointer does not bind the intact active generation")
                    child = _directory(genfd, expected_generation)
                    try:
                        files, _ = _tree(child, immutable=True)
                    finally:
                        os.close(child)
                    raw = files.pop(MANIFEST)
                    manifest = _document(raw)
                    if manifest["scope"] != scope:
                        _refuse("SCOPE_MISMATCH", "consumer cannot load knowledge from another Scope")
                    if _sha(raw) != pointer["manifest_hash"] or set(files) != {
                            entry["path"] for entry in manifest["entries"]} or any(
                            _sha(files[entry["path"]]) != entry["hash"] for entry in manifest["entries"]):
                        _refuse("MANUAL_TAMPER", "generation changed during the shared read")
                    _binding(fd, lockfd, root)
                    if _document(_read(fd, CURRENT)) != pointer or _generation(genfd, expected_generation) != pointer:
                        _refuse("STALE_GENERATION", "active projection changed during the shared read")
                finally:
                    os.close(genfd)
                return {"status": "READ", "projection_root": root, **pointer,
                        "manifest": manifest, "files": files}
            finally:
                fcntl.flock(lockfd, fcntl.LOCK_UN)
                os.close(lockfd)
    except PublishError:
        raise
    except (OSError, KeyError, ValueError, TypeError) as exc:
        raise PublishError("READ_REFUSED", "active generation is missing, malformed or unreadable; bytes preserved") from exc


def _inspect(fd, root):
    names = _names(fd)
    if not {MARKER, LOCK} <= names or names - {MARKER, LOCK, CURRENT, "generations"}:
        _refuse("RECOVERY_REQUIRED", "unknown/unmanaged files or retained partial publication require explicit inspection")
    if _document(_read(fd, MARKER)) != _marker(root) or _read(fd, LOCK) != b"":
        _refuse("UNMANAGED_ROOT", "directory has no valid projector-owned marker/lock")
    generations = {}
    if "generations" in names:
        genfd = _directory(fd, "generations")
        try:
            for name in sorted(_names(genfd)):
                generations[name] = _generation(genfd, name)
        finally:
            os.close(genfd)
    if CURRENT not in names:
        if generations:
            _refuse("RECOVERY_REQUIRED", "generations exist without a complete current pointer")
        return None
    pointer = _document(_read(fd, CURRENT))
    generation = pointer.get("generation")
    if not isinstance(generation, str) or pointer != generations.get(generation):
        _refuse("MANUAL_TAMPER", "current pointer does not bind an intact owned generation")
    return pointer


@contextmanager
def _projection_lock(fd, root):
    names = _names(fd)
    if names and MARKER not in names and names != {LOCK}:
        _refuse("UNMANAGED_ROOT", "caller must provide an empty directory or a valid owned projection root")
    if names - {MARKER, LOCK, CURRENT, "generations"}:
        _refuse("UNKNOWN_FILE", "unknown user files are preserved; publication refused")
    if MARKER in names and LOCK not in names:
        _refuse("RECOVERY_REQUIRED", "owned marker has lost its lock; do not silently recreate it")
    created = False
    try:
        handle = os.open(LOCK, os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                         0o600, dir_fd=fd)  # KD-WRITE-EXEMPT: projector-owned empty advisory lock only; never a store lock/write
        created = True
    except FileExistsError:
        _exact(fd, LOCK)
        handle = os.open(LOCK, os.O_RDWR | os.O_NOFOLLOW | os.O_NONBLOCK,
                         dir_fd=fd)  # KD-WRITE-EXEMPT: open only the existing projector lock for flock, no knowledge bytes written
    try:
        meta = os.fstat(handle)
        if not stat.S_ISREG(meta.st_mode) or meta.st_nlink != 1 or meta.st_size != 0:
            _refuse("UNSAFE_PATH", "projection lock must be an empty singly linked regular file")
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            _refuse("PROJECTOR_BUSY", "another publisher owns the projection lock; no automatic retry")
        names = _names(fd)
        if created and names == {LOCK}:
            _write(fd, MARKER, _json_bytes(_marker(root)))
        elif MARKER not in names:
            _refuse("RECOVERY_REQUIRED", "unmarked lock retained; explicit root recovery required")
        current = _inspect(fd, root)
        yield current, handle
    finally:
        fcntl.flock(handle, fcntl.LOCK_UN)
        os.close(handle)


def _binding(fd, lockfd, root):
    with _absolute_dir(root) as current:
        a, b = os.fstat(fd), os.fstat(current)
        lock, named = os.fstat(lockfd), os.stat(LOCK, dir_fd=current, follow_symlinks=False)
        if (a.st_dev, a.st_ino) != (b.st_dev, b.st_ino) \
                or (lock.st_dev, lock.st_ino) != (named.st_dev, named.st_ino) or named.st_nlink != 1:
            _refuse("UNSAFE_PATH", "projection directory or advisory lock was replaced during publication")


def _store_binding(fd, store, snapshot):
    """Recheck the public snapshot while its shared lease is still held; no private reads."""
    with _absolute_dir(store) as current:
        old, named = os.fstat(fd), os.fstat(current)
        if (old.st_dev, old.st_ino) != (named.st_dev, named.st_ino):
            _refuse("STALE_SNAPSHOT", "source store directory was replaced during publication")
    if txn.read_snapshot(store) != snapshot:
        _refuse("STALE_SNAPSHOT", "source store changed despite the held snapshot lease")


def _descend(fd, parts):
    child = os.dup(fd)
    try:
        for part in parts:
            nextfd = _directory(child, part)
            os.close(child)
            child = nextfd
        return child
    except BaseException:
        os.close(child)
        raise


def _seal(fd):
    for name in sorted(_names(fd)):
        meta = os.stat(name, dir_fd=fd, follow_symlinks=False)
        if stat.S_ISDIR(meta.st_mode):
            child = _directory(fd, name)
            try:
                _seal(child)
            finally:
                os.close(child)
    os.fchmod(fd, 0o555)  # KD-WRITE-EXEMPT: seal only directories of this newly generated derived generation
    os.fsync(fd)  # KD-WRITE-EXEMPT: persist the complete derived generation's sealed directory


def _create_generation(fd, plan):
    if "generations" not in _names(fd):
        _mkdir(fd, "generations")
    genfd = _directory(fd, "generations")
    try:
        generation = plan["generation"]
        if generation in _names(genfd):
            if _generation(genfd, generation)["manifest_hash"] != plan["manifest_hash"]:
                _refuse("MANUAL_TAMPER", "existing immutable generation differs from the deterministic plan")
            return
        _mkdir(genfd, generation)
        child = _directory(genfd, generation)
        try:
            _mkdir(child, "rules")
            _mkdir(child, "skills")
            names = sorted({path.split("/")[1] for path in plan["files"] if path.startswith("skills/")})
            skillsfd = _directory(child, "skills")
            try:
                for name in names:
                    _mkdir(skillsfd, name)
            finally:
                os.close(skillsfd)
            for path, data in sorted(plan["files"].items()):
                bits = path.split("/")
                target = _descend(child, bits[:-1])
                try:
                    _write(target, bits[-1], data)
                finally:
                    os.close(target)
            _write(child, MANIFEST, plan["manifest"])
            _seal(child)
        finally:
            os.close(child)
        if _generation(genfd, generation)["manifest_hash"] != plan["manifest_hash"]:
            _refuse("MANUAL_TAMPER", "new generation failed its independent file/hash inspection")
        os.fsync(genfd)  # KD-WRITE-EXEMPT: persist only the new immutable derived generation entry
    finally:
        os.close(genfd)


def publish(store_root, projection_root, *, expected_snapshot_digest, expected_generation,
            scope, publication_policy):
    """Publish a leased S12 snapshot by CAS against current.json's expected generation.

    None means there must be no current pointer. Success is PUBLISHED, not host consumption.
    Failure before pointer replacement preserves the old pointer and all old generation bytes.
    A post-replacement fsync refusal reports SWITCHED_NOT_DURABLE, not an unobserved switch.
    No automatic rollback, cleanup, installation, policy admission or record mutation occurs.
    """
    store, root = _absolute(store_root), _absolute(projection_root)
    policy, scope = _policy(publication_policy), _copy_json(scope)
    if not validator.validate_artifact("scope-tuple", scope)["valid"]:
        _refuse("SCOPE_MISMATCH", "caller must declare one valid exact SC11 Scope")
    if not isinstance(expected_snapshot_digest, str) or not _HEX.fullmatch(expected_snapshot_digest):
        _refuse("STALE_SNAPSHOT", "an explicit S12 snapshot digest is required")
    if expected_generation is not None and (not isinstance(expected_generation, str)
                                             or not _HEX.fullmatch(expected_generation)):
        _refuse("STALE_GENERATION", "expected_generation must be null or an exact generation digest")
    plan = None
    try:
        _check_location(store, root, policy)
        with _absolute_dir(store) as storefd, _absolute_dir(root) as fd:
            with txn.locked_snapshot(store) as snapshot:
                if snapshot["snapshot_digest"] != expected_snapshot_digest:
                    _refuse("STALE_SNAPSHOT", "S12 snapshot changed before publication lease was acquired")
                _check_location(store, root, policy, snapshot["source_roots"])
                plan = plan_projection(snapshot, scope=scope, publication_policy=policy)
                with _projection_lock(fd, root) as (old, lockfd):
                    previous = old["generation"] if old else None
                    if previous != expected_generation:
                        _refuse("STALE_GENERATION", "current generation differs from caller's CAS expectation")
                    _store_binding(storefd, store, snapshot)
                    _binding(fd, lockfd, root)
                    _store_binding(storefd, store, snapshot)
                    _create_generation(fd, plan)
                    # Inspect EVERY retained generation, including inactive older ones. Initial
                    # publication has a new complete generation but intentionally no pointer yet.
                    if old is None:
                        genfd = _directory(fd, "generations")
                        try:
                            if _names(genfd) != {plan["generation"]}:
                                _refuse("UNKNOWN_FILE", "initial publication contains an unexpected generation")
                            _generation(genfd, plan["generation"])
                        finally:
                            os.close(genfd)
                        if CURRENT in _names(fd):
                            _refuse("STALE_GENERATION", "a current pointer appeared before initial CAS")
                        if _names(fd) != {MARKER, LOCK, "generations"} \
                                or _document(_read(fd, MARKER)) != _marker(root):
                            _refuse("UNKNOWN_FILE", "projection changed while building its initial generation")
                    elif _inspect(fd, root) != old:
                        _refuse("STALE_GENERATION", "current pointer changed before CAS")
                    _binding(fd, lockfd, root)
                    pointer = {"generation": plan["generation"], "source_snapshot": plan["source_snapshot"],
                               "manifest_hash": plan["manifest_hash"], "generator": GENERATOR, "version": VERSION}
                    durability = "SYNCED"
                    if old != pointer:
                        pending = ".pending-current-" + uuid.uuid4().hex
                        _write(fd, pending, _json_bytes(pointer))
                        _binding(fd, lockfd, root)
                        # Check expected bytes immediately before replacement; projector flock
                        # serializes cooperating writers. An uncooperative edit is a refusal.
                        if (CURRENT in _names(fd)) != (old is not None) \
                                or (old is not None and _document(_read(fd, CURRENT)) != old):
                            _refuse("STALE_GENERATION", "current pointer changed while preparing CAS")
                        _store_binding(storefd, store, snapshot)
                        os.replace(pending, CURRENT, src_dir_fd=fd, dst_dir_fd=fd)  # KD-WRITE-EXEMPT: sole derived current pointer CAS under projection flock and S12 shared lease; never a store commit
                        try:
                            os.fsync(fd)  # KD-WRITE-EXEMPT: persist only the derived current pointer switch
                        except OSError:
                            # replace is the linearization point. A later fsync failure cannot
                            # truthfully be described as "old pointer retained" or retried as if
                            # CAS never happened. Report observed switch with durability unknown.
                            durability = "NOT_PROVEN"
                    return {"status": "PUBLISHED" if durability == "SYNCED" else "SWITCHED_NOT_DURABLE",
                            "durability": durability, "generation": plan["generation"],
                            "previous_generation": previous, "source_snapshot": plan["source_snapshot"],
                            "manifest_hash": plan["manifest_hash"], "projection_root": root,
                            "current": CURRENT, "artifact_count": len(plan["files"])}
    except PublishError:
        raise
    except (txn.StoreError, txn.WriteRejection, layout.LayoutViolation) as exc:
        raise PublishError("SNAPSHOT_REFUSED", "S12/S08 refused the source; use their explicit recovery path") from exc
    except OSError as exc:
        raise PublishError("RECOVERY_REQUIRED", "filesystem refusal; old pointer/partial derived files are retained",
                           generation=plan["generation"] if plan else None) from exc
