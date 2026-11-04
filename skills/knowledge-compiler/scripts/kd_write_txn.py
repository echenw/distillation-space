#!/usr/bin/env python3
"""S12: single-writer, hash-bound file transactions with explicit crash recovery.

Readers and writers coordinate on one permanent OS lock inode. A fsynced undo/redo journal
precedes every record/ledger change; commit.json is the last authoritative write. Recovery
only restores recognized, uncommitted bytes, never repairs an unknown/legacy store by guess.
G1, independent Eval and source-observation authentication require separate trusted HOST
callbacks, not JSON flags, imported user code or generated secrets. Provisional policy cannot commit.
These are source-level protocol claims; release qualification requires execution evidence.

Contract (.distill/round-3/wave-1/_dispatch/w1c.json):
    inputs  : 通过门的提案 + 当前 store 状态
    outputs : 原子落盘（tmp+rename+fsync），`store/_ledger/commit.json` written LAST as the commit point
    exit    : 2=存在第二条写路径；`absorbed_into` 缺失即拒
    clusters: CM-11 (canonical store layout + owner), CM-23->CM-11, CM-28 (supersede never
              destroy), CM-30 (write ownership boundary)

Round 2 basis (pack-c.md and the docs it quotes):
  * `12-SKILL-DESIGN-BRIEF.md:721` item 1 -- 写路径唯一（P-3）：对全仓 grep 落盘调用
    （write / rename / os.replace / fsync / git commit），断言每一处都在 S12 之内或有显式
    允许清单豁免注释；存在第二条 durable 写路径 ⇒ 整树失效。`audit_bypass` is that assertion,
    as an AST scan, executed at call time.
  * `12-SKILL-DESIGN-BRIEF.md:140` -- CM-50 verify-before-persist 由 S10（写前门）+ S16 +
    S12 三处共同强制: S12 therefore *re-runs* kd_gate.evaluate_promotion (same single
    authority, same inputs) instead of trusting a handed-in decision, then applies the
    mutation through kd_gate.apply_mutation -- the only authoritative mutation boundary
    (so a model payload keeps proposal rights only, and `to == "deleted"` stays unreachable).
  * `07-LIFECYCLE-POLICY.md` §3.4 / A2 -- MERGE 必须带 absorbed_into 且 promoter fail-closed
    （目标伞形不存在 → 整条 intent 拒绝）.
  * `07-LIFECYCLE-POLICY.md` §3.1 -- 可逆 archive 是破坏性上限；本模块不提供任何 delete 通道。
  * `05-DATA-MODEL.md:44,52` -- evidence_refs 由 resolver 校验，解析失败即拒绝入库;
    `refs_integrity` 是每轮重算的结果位.
  * `05-DATA-MODEL.md:49` -- lifecycle_event 账本 append-only，一次 batch op 只写一行，
    detail 不作权威.

No script may replace this boundary with a second durable writer. Atomic single-file helpers
also serve inert staging artifacts; importing them does not grant store-write authority.

Stdlib only.
"""
from __future__ import annotations

import argparse
import ast
import fcntl
import hashlib
import io
import json
import os
import re
import stat
import sys
import time
import tokenize
from contextlib import contextmanager

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import kd_gate                          # noqa: E402  Wave 0: gate + unique mutation boundary
import kd_provenance as prov            # noqa: E402  Wave 0: identity, ledger, classification
import kd_provenance_stamp as stamp     # noqa: E402  S13
import kd_refs_audit as refs            # noqa: E402  S14
import kd_store_layout as layout        # noqa: E402  S08: the ONLY owner of store layout
import kd_human_gate as g1              # noqa: E402  G1: S12 verifies the approval that gates it

EXIT_OK = 0
EXIT_SECOND_WRITE_PATH = 2        # contractual: a second write path exists / self-declared
                                  # provenance reached the gate / refs or CM-65 binding failed
EXIT_WRITE_REJECTED = 3           # policy refusal: gate closed, absorbed_into missing,
                                  # illegal transition, delete requested, stale revision
EXIT_SCAN_INCOMPLETE = 4          # bypass audit could not cover the expected module set
EXIT_STORE_ERROR = 5              # filesystem failure / uncertain outcome; inspect before retry

# Original policy: 8 actions. The 2026-10-07 user-approved RESTORE is an explicit
# committed-history inverse, not automatic resurrection. MOVE/AUTOMATE remain absent.
LIFECYCLE_ACTIONS = ("ADD", "MERGE", "UPDATE", "SUPERSEDE", "DELETE",
                     "REINFORCE", "DECAY", "ARCHIVE", "RESTORE")
# DELETE is a ledger vocabulary term (the human-only gc channel of 07 §A5). It is never a
# write this module performs: archive is the ceiling and kd_gate already raises on
# to == "deleted".
DESTRUCTIVE_CEILING = "archived"

# RH-P0-09 / §14-15: fields the SYSTEM owns. A proposal (untrusted domain input) carrying any of
# these is REFUSED fail-closed, never trusted-then-stamped. `provenance`/`generation`/`actor`/
# `stamp_digest`/`verification`/`status_basis`/`refs_integrity` are already refused upstream by
# kd_provenance_stamp.find_self_declared; this list covers the remaining system-owned fields --
# the ledger pointer, the writer identity, transaction bookkeeping, and the SC05-owned lifecycle
# counters (RH-P1-02: removed from SC04, S17 kd_lifecycle is their only writer). `state`/`revision`
# are handled separately below: a proposal may present only the pre-write initial values.
SYSTEM_OWNED_FIELDS = ("record_locator", "written_by", "decision_digest", "lifecycle_record_id",
                       "use_count", "view_count", "layer_request_count", "opportunity_anchor",
                       "first_seen_at", "pinned", "referenced_by_external", "patch_count",
                       "verification", "refs_integrity")

AUDIT_MARKER = "# KD-WRITE-EXEMPT:"
OWNER_MODULES = frozenset({"kd_write_txn.py"})

# Reviewed derived/layout/projection writes, pinned by the AST of the precise
# annotated calls (owner function + operation + arguments), not by comments
# that an arbitrary new module or new call can add itself. Line/whitespace and
# annotation prose changes do not invalidate a legitimate approved write.
# A change to any approved call requires explicit review of this table; this
# is an audit inventory, not a signature authenticating the package author.
APPROVED_EXEMPT_SITES = {
    "kd_eval_freeze.py": (5, "7960ae74a3ad98e19f9209065808a9d00fa10aa7f2f3619b9ac5fe01d48605f9"),
    "kd_eval_score.py": (5, "7960ae74a3ad98e19f9209065808a9d00fa10aa7f2f3619b9ac5fe01d48605f9"),
    "kd_ingest.py": (5, "29d5c70b9a373abe6a6ad2663dd470b914139ee923ee0b396e9e6a3f24bf8a20"),
    "kd_inventory.py": (5, "29d5c70b9a373abe6a6ad2663dd470b914139ee923ee0b396e9e6a3f24bf8a20"),
    "kd_publish.py": (14, "abc52a2347f8895dd568dc67067d2aab573060895772b9a72e3c36952481e590"),
    # Independently reviewed: two O_RDONLY|O_DIRECTORY|O_NOFOLLOW descriptor opens
    # in the read-only round fingerprint scan; no creation, rename, or writes.
    "kd_round_output.py": (2, "f8ef70ffe28286cdc47d18cf0e15e82956f6324ca3b8a75e086d3af5122bae4e"),
    "kd_scope_resolve.py": (5, "29d5c70b9a373abe6a6ad2663dd470b914139ee923ee0b396e9e6a3f24bf8a20"),
    "kd_selfsource_filter.py": (5, "29d5c70b9a373abe6a6ad2663dd470b914139ee923ee0b396e9e6a3f24bf8a20"),
    "kd_store_layout.py": (19, "4d2b9a60e9ad9157e9dedb1c4951e00335318ca2331c9879deaa1941e599dc92"),
}

# Every distributed runtime script must be present before the scan can be GREEN.
# This reviewed list is independent of the scanned directory: deriving it from
# existing files would let a missing dependency silently disappear from the audit.
# Explicit expected= overrides remain available to isolated scanner unit tests.
EXPECTED_MODULES = (
    "kd_gate.py", "kd_provenance.py",                      # wave 0 kernel
    "kd_write_txn.py", "kd_provenance_stamp.py", "kd_refs_audit.py",  # S12/S13/S14
    "kd_ingest.py", "kd_inventory.py", "kd_selfsource_filter.py",
    "kd_scope_resolve.py", "kd_identity_key.py", "kd_dedup_exact.py",
    "kd_store_layout.py", "kd_validate.py", "kd_gate_tree.py", "kd_human_gate.py",
    "kd_model_step.py", "kd_proxy_candidates.py", "kd_quarantine.py", "kd_eval_freeze.py",
    "kd_eval_score.py", "kd_lifecycle.py", "kd_budget.py", "kd_publish.py",
    "kd_candidate_review.py", "kd_execution_review.py", "kd_incremental.py",
    "kd_material_audit.py", "kd_material_ops.py", "kd_material_quality.py",
    "kd_delivery_preflight.py",  # R18 read-only consumer delivery check, included in S12 scan
    "kd_artifact_quality.py",
    "kd_task_brief.py", "kd_round_output.py", "kd_workspace_audit.py",
    "kd_skill_metadata.py",
)

# Direct durable-write primitives, collected from the Round 2 grep list (write / rename /
# os.replace / fsync / git commit) plus the pathlib and shutil equivalents.
WRITE_PRIMITIVES = {
    "tempfile.mkstemp": "tempfile.mkstemp",
    "tempfile.mkdtemp": "tempfile.mkdtemp",
    "tempfile.NamedTemporaryFile": "tempfile.NamedTemporaryFile",
    "tempfile.TemporaryFile": "tempfile.TemporaryFile",
    "tempfile.TemporaryDirectory": "tempfile.TemporaryDirectory",
    "tempfile.SpooledTemporaryFile": "tempfile.SpooledTemporaryFile",
    "os.replace": "os.replace",
    "os.rename": "os.rename",
    "os.remove": "os.remove",
    "os.unlink": "os.unlink",
    "os.fsync": "os.fsync",
    "os.mkdir": "os.mkdir",
    "os.makedirs": "os.makedirs",
    "os.truncate": "os.truncate",
    "os.ftruncate": "os.ftruncate",
    # These APIs can redirect an existing (approved pipe) file descriptor.
    # os.dup itself only clones an fd and is legitimately used by S06.
    "os.dup2": "os.dup2",
    "os.dup3": "os.dup3",
    "os.open": "os.open",
    "os.write": "os.write",
    # A writable fd can arrive from a caller; these do not need os.open here.
    # Availability is platform dependent but their source callsites must still
    # be classified even when the audit runs on another supported OS.
    "os.pwrite": "os.pwrite",
    "os.writev": "os.writev",
    "os.pwritev": "os.pwritev",
    "os.sendfile": "os.sendfile",
    "os.copy_file_range": "os.copy_file_range",
    "os.splice": "os.splice",
    "os.link": "os.link",
    "os.symlink": "os.symlink",
    "shutil.move": "shutil.move",
    "shutil.copy": "shutil.copy",
    "shutil.copy2": "shutil.copy2",
    "shutil.copyfile": "shutil.copyfile",
    # Copies into an existing destination stream supplied by an upstream owner.
    "shutil.copyfileobj": "shutil.copyfileobj",
    "shutil.copytree": "shutil.copytree",
    "shutil.rmtree": "shutil.rmtree",
}
# Constructors default to read mode; unrecognized, w/x/a/+ modes create
# or mutate an archive, even without an explicit open("w") in this module.
ARCHIVE_CONSTRUCTORS = frozenset({"zipfile.ZipFile", "zipfile.PyZipFile"})
# stream/path methods, matched on the attribute so `fh.write(...)` and `p.write_text(...)`
# are both caught; `sys.stdout.write` is excluded because stdout is not a store file.
WRITE_ATTRS = {"write", "writelines", "write_text", "write_bytes", "writestr",
               "truncate", "touch",
               "mkdir", "unlink", "rmdir", "symlink_to", "hardlink_to", "link_to",
               "chmod", "lchmod"}
# Path.replace/rename accept one target, while str.replace requires two arguments.
# Check their call shapes to avoid mistaking ordinary string normalization for a writer.
PATH_MOVE_ATTRS = {"replace", "rename"}
STD_STREAMS = ("sys.stdout", "sys.stderr")
# Treat every process launch as a potential indirect durable writer. Restrict
# existing read-only invocations using reviewed, exact AST site fingerprints,
# never the child program's name (a non-git shell can also write files).
EXTERNAL_EXEC_NODES = {
    "subprocess.run", "subprocess.call", "subprocess.check_call",
    "subprocess.check_output", "subprocess.Popen", "subprocess.getoutput",
    "subprocess.getstatusoutput", "os.system", "os.popen",
    "os.spawnl", "os.spawnle", "os.spawnlp", "os.spawnlpe",
    "os.spawnv", "os.spawnve", "os.spawnvp", "os.spawnvpe",
    "os.execl", "os.execle", "os.execlp", "os.execlpe",
    "os.execv", "os.execve", "os.execvp", "os.execvpe",
    "os.posix_spawn", "os.posix_spawnp",
    "asyncio.create_subprocess_exec", "asyncio.create_subprocess_shell",
}
# Unbounded wildcard imports are not verifiable name bindings; never GREEN.
UNBOUNDED_STAR_IMPORTS = frozenset({
    "os", "subprocess", "asyncio", "shutil", "tempfile", "io",
    "builtins", "pathlib", "zipfile",
})
# Match publishable Python files under scripts/, while ignoring build trash.
# New nested Python modules are scanned, not implicitly approved or skipped.
SCAN_EXCLUDED_DIRS = frozenset({
    "__MACOSX", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", ".distill", "tests", "test", "repos", ".git",
    ".hg", ".svn", ".idea", ".vscode", "node_modules", ".tmp",
})
MAX_SCAN_SCRIPT_BYTES = 4 * 1024 * 1024
MAX_SCAN_TOTAL_BYTES = 64 * 1024 * 1024
MAX_SCAN_PYTHON_FILES = 512
# Native extension/binary modules are executable but cannot be verified with
# Python AST. Publishing must refuse them, and S12 independently fails closed.
NATIVE_EXECUTABLE_SUFFIXES = (".so", ".dylib", ".dll", ".bundle", ".pyd", ".exe")
# A zipapp, wheel or zipimport archive contains Python that is not visible
# to this scanner's ordinary .py walk. Reject instead of claiming GREEN.
EXECUTABLE_ARCHIVE_SUFFIXES = (".pyz", ".pyzw", ".zip", ".egg", ".whl", ".pex")


def _native_executable_name(name: str) -> bool:
    name = name.lower()
    return name.endswith(NATIVE_EXECUTABLE_SUFFIXES) or ".so." in name


def _executable_archive_name(name: str) -> bool:
    return name.lower().endswith(EXECUTABLE_ARCHIVE_SUFFIXES)


# Wave 0's kernel ledger is a named, non-authoritative append-only channel.
# Keep the historical exception, but pin its exact reviewed AST calls and
# cardinality just like APPROVED_EXEMPT_SITES: an extra write in the SAME
# function with the SAME primitive must make this audit RED, not GREEN.
# This inventory is reviewed manually; do not rebuild it from the scanned tree.
SANCTIONED_CHANNELS = {
    ("kd_provenance.py", "append_ledger"): (
        frozenset({"open_writing_mode", "os.makedirs", "method:write"}),
        3,
        "afe990fc2946c9fa66bda7b80a57ba24b477d8e546c7efd1cb5be6814bda7d64",
    ),
}
# Exactly two separately reviewed external-process call sites.
# R03 invokes pdftotext with stdout='-' or -v for local document extraction;
# S14 invokes the caller-selected Round-1 witness for comparison. Their AST
# arguments, enclosing function and cardinality are pinned. This inventory is
# not an assertion that an arbitrary executable is intrinsically trustworthy;
# modifying/adding a process call without review makes the scan RED.
REVIEWED_EXTERNAL_PROCESS_SITES = {
    "kd_material_ops.py": (1, "99a1ccebbfddba8dfb4f460a70d79a44369f8df4701b0b5652ceeb5f766f3de3"),
    "kd_refs_audit.py": (1, "ae2fd899e5c6ccf6729b61060e63afc8f9cbd7125674fa38ef867d7ba846fa51"),
}
# S14's reviewed witness launcher transfers exact SHA-checked bytes through
# the stdin PIPE of its bounded subprocess, not to durable knowledge storage.
# The single os.write call is pinned independently; arbitrary fd writes remain
# second-writer violations.
REVIEWED_WITNESS_PIPE_SITES = {
    "kd_refs_audit.py": (1, "8c8dda7513810eddda07316726def0223c9db30a02fac4705165839fc8c4099d"),
}
# Pin the entire reviewed implementation, not just its two approved calls:
# a new descriptor redirection or a different stdout/pipe source cannot reuse
# an unchanged os.write callsite to inherit its exception.
REVIEWED_WITNESS_FUNCTION_AST = (
    "1cc1b30402056f9cd9135bb0ed13e7deb3d3ed5ca6e854aa8146b82e3ec611c3"
)

# PDF conversion feeds the exact source snapshot through a bounded local pipe.
# The helper and descriptor write are reviewed as one fixed implementation.
REVIEWED_PDF_PIPE_SITES = {"kd_material_ops.py": (1, "ba8c8297a35f51366579b917edc4a59e01ab0361cbe4664a20c063588cf3cfa1")}
REVIEWED_PDF_FUNCTION_AST = "35fcced65bd47aaf5492efacc0e688c36f61ac307da5037a56fad6533b7a15ba"


class WriteRejection(Exception):
    """Policy refusal to write. Maps to exit 3."""


class SecondWritePath(Exception):
    """The write path uniqueness / provenance / evidence invariants were violated. Exit 2."""


class StoreError(Exception):
    """Filesystem/integrity failure. Exit 5; inspect recovery before retrying."""


# --------------------------------------------------------------------- store layout (S08's, not ours)
class StorePaths:
    """Every store path, read from S08's layout manifest at call time.

    S08 `kd_store_layout` is the single Owner of the store layout (CM-11, the Round 2裁决 that
    keeps CM-11 "where/what shape", CM-13 "which copy is trusted" and CM-30 "who may write"
    three orthogonal clauses -- `02-FINAL-MECHANISMS.md:95-111`). This class therefore holds no
    path literal of its own: `records`, `index`, `journal`, `lifecycle_ledger` and
    `commit_marker` all come from `kd_store_layout.paths(root, manifest)`, and the actor that
    authorises a write is `kd_store_layout.OWNER_WRITE_TXN`, not a string copied from here.

    Protocol carriers also come from S08; old manifests are not silently migrated.
    """

    def __init__(self, root: str, manifest: dict | None = None):
        self.root = os.path.realpath(root)
        self.manifest = manifest if manifest is not None else layout.load_manifest(self.root)
        resolved = layout.paths(self.root, self.manifest)
        self.records = resolved["records"]
        self.lifecycle_records = resolved.get("lifecycle_records")
        self.index = resolved["index"]
        self.ledger_dir = resolved["ledger"]
        self.journal = resolved["journal"]
        self.lifecycle_ledger = resolved["lifecycle_ledger"]
        self.commit_point = resolved["commit_marker"]
        self.lock = resolved.get("transaction_lock")
        self.pending = resolved.get("transaction_pending")
        self.history = resolved.get("transaction_history")
        #: the writer identity S12 holds in the manifest: the ONE vocabulary S08 authorises with
        self.writer = layout.OWNER_WRITE_TXN

    def rel(self, path: str) -> str:
        """Manifest-relative posix path: what a journal row and `authorize_write` name."""
        return os.path.relpath(path, self.root).replace(os.sep, "/")

    def record(self, artifact_id: str) -> str:
        if not isinstance(artifact_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", artifact_id):
            raise WriteRejection(f"unsafe artifact_id for a store path: {artifact_id!r}")
        return layout.safe_path(self.root, self.rel(os.path.join(self.records, f"{artifact_id}.json")))

    def lifecycle_record(self, artifact_id: str) -> str:
        self.record(artifact_id)  # same safe ID vocabulary, not another path Owner
        if not self.lifecycle_records:
            raise WriteRejection("PROTOCOL_LAYOUT_MISSING: SC05 carrier needs explicit migration")
        return layout.safe_path(self.root, self.rel(os.path.join(self.lifecycle_records, f"{artifact_id}.json")))

    def authorize(self, path: str) -> None:
        """Fail-closed: an unregistered path or an actor that holds no owner slot is refused
        (S08 `authorize_write`), and this is on the commit path, not an optional check."""
        try:
            layout.authorize_write(self.manifest, self.rel(path), self.writer)
        except layout.LayoutViolation as exc:
            raise SecondWritePath("store ownership refused the transaction target") from exc


def resolve_paths(store_dir: str, *, bootstrap: bool = False) -> StorePaths:
    """Bind the transaction to S08's layout. A store root with no `store-layout.json` yet is
    bootstrapped by S08 itself (`ensure_manifest`) when `bootstrap=True`, i.e. only on the
    commit path; a read-only entry point keeps the in-memory canonical default and never
    creates a store."""
    root = os.path.abspath(store_dir)
    if bootstrap:
        try:
            manifest = layout.ensure_manifest(root, layout.OWNER_WRITE_TXN,
                                             layout.OWNER_LIFECYCLE_LEDGER)
        except layout.LayoutViolation as exc:
            # a root whose manifest is corrupt or of another layout version is not a store this
            # transaction may write into: refuse (exit 3), never borrow exit 2 (S08's code for a
            # second writer / non-Owner landing) and never write over it
            raise WriteRejection(f"{root} is not a declared store for this layout: {exc}") from exc
        except OSError as exc:
            raise StoreError(f"cannot bootstrap the store layout in {root}: {exc}") from exc
    else:
        try:
            manifest = (layout.load_manifest(root) if os.path.lexists(os.path.join(root, layout.MANIFEST_NAME))
                        else layout.build_manifest(root, layout.OWNER_WRITE_TXN, layout.OWNER_LIFECYCLE_LEDGER))
        except (layout.LayoutViolation, ValueError) as exc:
            raise WriteRejection("invalid declared store layout") from exc
    try:
        return StorePaths(root, manifest)
    except layout.LayoutViolation as exc:
        raise WriteRejection("invalid declared store paths") from exc


# --------------------------------------------------------------------- atomic writer
def _fsync_dir(path: str) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _mkdir_durable(directory):
    missing, current = [], directory
    while not os.path.exists(current):
        missing.append(current)
        current = os.path.dirname(current)
    os.makedirs(directory, exist_ok=True)
    for created in missing:
        _fsync_dir(created)
        _fsync_dir(os.path.dirname(created))


def atomic_write(path: str, text: str) -> None:
    """tmp + fsync + os.replace: a crash never leaves a half-written record.

    This primitive does not grant transaction authority. Records/ledgers/commit points are
    owned by S12's protocol; derived writers may use it only for their declared staging paths.
    """
    directory = os.path.dirname(path) or "."
    _mkdir_durable(directory)
    tmp = os.path.join(directory, f".tmp-{os.path.basename(path)}-{os.getpid()}-{time.time_ns()}")
    try:
        with open(tmp, "x", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)
        _fsync_dir(directory)
    except OSError as exc:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise StoreError(f"atomic write failed for {path}: {exc}") from exc


def write_json(path: str, doc) -> None:
    atomic_write(path, json.dumps(doc, ensure_ascii=False, sort_keys=True, indent=1) + "\n")


# --------------------------------------------------------------------- bypass audit (S12 exit 2)
def _dotted_name(node, aliases: dict | None = None) -> str:
    """Normalize bounded builtins.getattr references and explicit import aliases."""
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = _dotted_name(node.value, aliases)
        return base + "." + node.attr if base else ""
    if isinstance(node, ast.Call) and len(node.args) in (2, 3):
        target = _resolve_audit_name(_dotted_name(node.func, aliases), aliases or {})
        if target not in ("getattr", "builtins.getattr"):
            return ""
        base = _dotted_name(node.args[0], aliases)
        if not base:
            return ""
        attr = node.args[1]
        if isinstance(attr, ast.Constant) and type(attr.value) is str:
            return base + "." + attr.value
        return base + ".<dynamic>"
    return ""


def _function_owners(tree) -> dict:
    """id(call node) -> name of the innermost enclosing function ("<module>" at top level)."""
    owner = {}
    for fn in ast.walk(tree):
        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for inner in ast.walk(fn):
                if inner is not fn:
                    owner[id(inner)] = fn.name
    return owner


def _open_mode(call: ast.Call, *, method: bool = False) -> str:
    """Resolve a file open mode; unknown modes are potential writes.

    Builtin/io.open use positional slot 1 (after the path), whereas
    Path.open uses slot 0 (the receiver is the path).
    """
    slot = 0 if method else 1
    mode = call.args[slot] if len(call.args) > slot else None
    if mode is None:
        for kw in call.keywords:
            if kw.arg == "mode":
                mode = kw.value
                break
        else:
            return "r"
    if mode is None:
        return "r"
    if isinstance(mode, ast.Constant) and isinstance(mode.value, str):
        return mode.value
    return "NON_LITERAL"


def _resolve_audit_name(name: str, aliases: dict) -> str:
    head, sep, rest = name.partition(".")
    return aliases.get(head, head) + (sep + rest if sep else "")


def _read_only_os_flags(node, aliases=None) -> bool:
    """Accept only explicit known read-only os.open flags, including import aliases.

    O_RDONLY is zero; an unrecognized flag or OR with O_CREAT is always a
    potential write, even if a different term says O_RDONLY.
    """
    aliases = aliases or {}
    if isinstance(node, ast.Constant):
        return type(node.value) is int and node.value == 0
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        return (_read_only_os_flags(node.left, aliases)
                and _read_only_os_flags(node.right, aliases))
    return _resolve_audit_name(_dotted_name(node), aliases) in {
        "os.O_RDONLY", "os.O_NOFOLLOW", "os.O_NONBLOCK", "os.O_DIRECTORY",
        "os.O_CLOEXEC", "os.O_NOCTTY", "os.O_NDELAY", "os.O_LARGEFILE",
    }

def is_writing_mode(mode: str) -> bool:
    """Any mode that can durably change bytes on disk, including append: an append to a
    store record is as destructive as a truncation."""
    if mode == "NON_LITERAL":
        return True
    return any(c in mode for c in "wxa+")


def _open_aliases(tree) -> dict:
    """Resolve direct stdlib imports and simple aliases of known write APIs.

    An aliased os.replace or shutil.copyfile must remain the *same* audited
    primitive as its qualified call. This is bounded static resolution, not
    general execution or dynamic alias inference.
    """
    modules = {"io", "builtins", "pathlib", "os", "shutil",
               "tempfile", "subprocess", "asyncio", "zipfile"}
    flags = {"O_RDONLY", "O_NOFOLLOW", "O_NONBLOCK", "O_DIRECTORY",
             "O_CLOEXEC", "O_NOCTTY", "O_NDELAY", "O_LARGEFILE"}
    aliases = {"open": "builtins.open", "getattr": "builtins.getattr"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for item in node.names:
                if item.name in modules:
                    aliases[item.asname or item.name] = item.name
        elif isinstance(node, ast.ImportFrom) and node.module in modules:
            for item in node.names:
                qualified = f"{node.module}.{item.name}"
                if (qualified in WRITE_PRIMITIVES or qualified in EXTERNAL_EXEC_NODES
                        or qualified in ARCHIVE_CONSTRUCTORS
                        or qualified in ("io.open", "builtins.open", "builtins.getattr")
                        or (node.module == "os" and item.name in flags)):
                    aliases[item.asname or item.name] = qualified
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            resolved = _resolve_audit_name(_dotted_name(node.value, aliases), aliases)
            if (resolved in WRITE_PRIMITIVES or resolved in EXTERNAL_EXEC_NODES
                    or resolved in ARCHIVE_CONSTRUCTORS
                    or resolved in ("builtins.open", "io.open", "builtins.getattr")):
                aliases[node.targets[0].id] = resolved
    return aliases


def _classify(call: ast.Call, aliases: dict | None = None) -> str | None:
    aliases = aliases or {}
    name = _dotted_name(call.func, aliases)
    if name in {stream + ".write" for stream in STD_STREAMS} | {
            stream + ".writelines" for stream in STD_STREAMS}:
        return None                     # stdout is not a store file
    # A retrieved write callable can escape into a variable/collection and
    # later be invoked without another recognizable standard-library call.
    # Even a bare unsafe/dynamic getattr is a potential second-write path.
    if (_resolve_audit_name(_dotted_name(call.func, aliases), aliases)
            in ("getattr", "builtins.getattr") and len(call.args) >= 2):
        retrieved = _resolve_audit_name(_dotted_name(call, aliases), aliases)
        if (retrieved in WRITE_PRIMITIVES or retrieved in EXTERNAL_EXEC_NODES
                or (".<dynamic>" in retrieved and
                    retrieved.split(".", 1)[0] in UNBOUNDED_STAR_IMPORTS)):
            return "indirect_dynamic_dispatch"
    resolved = _resolve_audit_name(name, aliases)
    if (".<dynamic>" in resolved and
            resolved.split(".", 1)[0] in UNBOUNDED_STAR_IMPORTS):
        return "indirect_dynamic_dispatch"
    if resolved in ("builtins.open", "io.open"):
        return "open_writing_mode" if is_writing_mode(_open_mode(call)) else None
    if resolved in ARCHIVE_CONSTRUCTORS:
        return "archive_writing_mode" if is_writing_mode(_open_mode(call)) else None
    if resolved == "os.open":
        flags = call.args[1] if len(call.args) > 1 else next(
            (kw.value for kw in call.keywords if kw.arg == "flags"), None)
        return None if _read_only_os_flags(flags, aliases) else WRITE_PRIMITIVES[resolved]
    if resolved in WRITE_PRIMITIVES:
        return WRITE_PRIMITIVES[resolved]
    if isinstance(call.func, ast.Attribute) and call.func.attr == "open":
        # A receiver may be Path(path), a Path variable, or an unresolved file API.
        # A non-literal mode is never presumed read-only.
        return "open_writing_mode" if is_writing_mode(_open_mode(call, method=True)) else None
    if isinstance(call.func, ast.Attribute):
        attr = call.func.attr           # catches `Path(p).write_text(...)` and `fh.write(...)`
    else:
        attr = name.rsplit(".", 1)[-1] if name else ""
    if attr in WRITE_ATTRS:
        return f"method:{attr}"
    if attr in PATH_MOVE_ATTRS and (
            len(call.args) == 1 or any(kw.arg == "target" for kw in call.keywords)):
        return f"method:{attr}"
    if resolved in EXTERNAL_EXEC_NODES:
        return "external_process"
    return None


def _site_ast_text(node) -> str:
    """Interpreter-independent AST text behind every reviewed-site digest.

    `ast.dump()` is a debugging aid, not a stable serialisation: 3.12 added an
    empty `type_params` to function/class definitions and 3.13 stopped printing
    empty lists. The reviewed inventories above were pinned against the 3.9
    form, so that form is written out here instead of inherited from whichever
    interpreter runs the audit. A non-empty `type_params` is still serialised:
    such source was not expressible when the pins were reviewed and must drift.
    """
    if isinstance(node, ast.AST):
        cls, fields = type(node), []
        for name in node._fields:
            try:
                value = getattr(node, name)
            except AttributeError:
                continue
            if value is None and getattr(cls, name, ...) is None:
                continue                    # unset optional field
            if name == "type_params" and value == []:
                continue
            fields.append("%s=%s" % (name, _site_ast_text(value)))
        return "%s(%s)" % (cls.__name__, ", ".join(fields))
    if isinstance(node, list):
        return "[%s]" % ", ".join(_site_ast_text(item) for item in node)
    return repr(node)


def _scan_file(path: str, file_label: str | None = None) -> dict:
    label = file_label or os.path.basename(path)
    try:
        # A bounded binary read is essential before AST/tokenizer allocation.
        # Non-UTF-8 bytes cannot be silently skipped or treated as a clean scan.
        with open(path, "rb") as fh:                                # read-only
            raw = fh.read(MAX_SCAN_SCRIPT_BYTES + 1)
        if len(raw) > MAX_SCAN_SCRIPT_BYTES:
            return {"file": label, "unparsable": "script exceeds scan byte limit",
                    "sites": []}
        source = raw.decode("utf-8")
    except (OSError, UnicodeError) as exc:
        return {"file": label,
                "unparsable": f"unreadable source ({type(exc).__name__})", "sites": []}
    try:
        tree = ast.parse(source, filename=path)
    except (SyntaxError, RecursionError) as exc:
        return {"file": label, "unparsable": f"invalid syntax ({type(exc).__name__})",
                "sites": []}
    owners = _function_owners(tree)
    aliases = _open_aliases(tree)
    lines = source.splitlines()
    try:
        exemption_lines = {token.start[0] for token in tokenize.generate_tokens(
            io.StringIO(source).readline)
            if token.type == tokenize.COMMENT and AUDIT_MARKER in token.string}
    except (tokenize.TokenError, UnicodeError) as exc:
        return {"file": label,
                "unparsable": f"invalid tokens ({type(exc).__name__})", "sites": []}
    sites = []
    # Imports can themselves make resolution unbounded. Record an explicit
    # violation rather than silently treating every unknown bare call as safe.
    for node in ast.walk(tree):
        if not (isinstance(node, ast.ImportFrom) and node.module in UNBOUNDED_STAR_IMPORTS
                and any(alias.name == "*" for alias in node.names)):
            continue
        primitive = f"wildcard_import:{node.module}"
        owner = owners.get(id(node), "<module>")
        site_digest = hashlib.sha256((owner + "|" + primitive + "|" +
                                      _site_ast_text(node)).encode("utf-8")).hexdigest()
        sites.append({"file": label, "line": node.lineno,
                      "function": owner, "primitive": primitive,
                      "text": lines[node.lineno - 1].strip()[:120],
                      "site_digest": site_digest, "exempt": False})
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        primitive = _classify(node, aliases)
        if primitive is None:
            continue
        raw_line = lines[node.lineno - 1] if 0 < node.lineno <= len(lines) else ""
        owner = owners.get(id(node), "<module>")
        # AST shape pins each reviewed write while remaining stable across
        # comment edits and unrelated line moves.
        site_digest = hashlib.sha256((owner + "|" + primitive + "|" +
                                      _site_ast_text(node)).encode("utf-8")).hexdigest()
        sites.append({"file": label, "line": node.lineno,
                      "function": owner, "primitive": primitive,
                      "text": raw_line.strip()[:120], "site_digest": site_digest,
                      "exempt": any(line in exemption_lines
                                    for line in range(node.lineno, node.end_lineno + 1))})
    reviewed_function_digest = None
    if label == "kd_refs_audit.py":
        matching = [node for node in tree.body
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and node.name == "_run_bounded_witness"]
        if len(matching) == 1:
            reviewed_function_digest = hashlib.sha256(
                _site_ast_text(matching[0]).encode("utf-8")
            ).hexdigest()
    pdf_digest = None
    if label == "kd_material_ops.py":
        matching = [node for node in tree.body
                    if isinstance(node, ast.FunctionDef) and node.name == "_run_pdf_tool"]
        if len(matching) == 1:
            pdf_digest = hashlib.sha256(
                _site_ast_text(matching[0]).encode("utf-8")).hexdigest()
    return {"file": label, "unparsable": None, "sites": sites,
            "reviewed_witness_function_digest": reviewed_function_digest,
            "reviewed_pdf_function_digest": pdf_digest}


def _channel_exempt(site) -> bool:
    contract = SANCTIONED_CHANNELS.get((site["file"], site["function"]))
    return contract is not None and site["primitive"] in contract[0]


def _scan_inventory(scripts_dir: str) -> tuple[list[str], list[str]]:
    """Recursively collect publishable Python files, never following linked paths.

    The package builder walks nested directories. A directory error, symlink,
    or incomplete listing must not silently certify a partial scan as GREEN.
    """
    files, errors = [], []
    try:
        if os.path.islink(scripts_dir) or not os.path.isdir(scripts_dir):
            return [], ["script root is missing or linked"]
        os.listdir(scripts_dir)       # distinguish an unreadable directory from an empty one

        def on_error(exc):
            errors.append(f"directory unreadable ({type(exc).__name__})")

        for current, dirs, names in os.walk(scripts_dir, onerror=on_error,
                                            followlinks=False):
            for entry in dirs + names:
                if os.path.islink(os.path.join(current, entry)):
                    errors.append("script tree contains a symlink")
            dirs[:] = sorted(d for d in dirs if d not in SCAN_EXCLUDED_DIRS
                             and not d.startswith("._")
                             and not os.path.islink(os.path.join(current, d)))
            for name in names:
                # AppleDouble "._*" files are not published by the packager.
                if name.startswith("._"):
                    continue
                if _native_executable_name(name) or _executable_archive_name(name):
                    errors.append("unaudited executable payload in scripts")
                if name.endswith(".py") and not os.path.islink(os.path.join(current, name)):
                    rel = os.path.relpath(os.path.join(current, name), scripts_dir)
                    files.append(rel.replace(os.sep, "/"))
    except OSError as exc:
        errors.append(f"script directory inaccessible ({type(exc).__name__})")
    return sorted(files), errors


def audit_bypass(scripts_dir: str = HERE, expected=EXPECTED_MODULES,
                  owner=OWNER_MODULES) -> dict:
    """Mechanically enforce "S12 is the only write path" (12:721 item 1).

    Scan all publishable Python subtrees, with stable bounded-resource errors.
    Returns GREEN / SCANNED_SET_INCOMPLETE / RED; incomplete is never GREEN.
    """
    py_files, collection_errors = _scan_inventory(scripts_dir)
    missing = [m for m in expected if m not in py_files]
    reports, cumulative = [], 0
    if len(py_files) > MAX_SCAN_PYTHON_FILES:
        collection_errors.append("too many Python files to audit")
    for file in py_files[:MAX_SCAN_PYTHON_FILES]:
        full = os.path.join(scripts_dir, *file.split("/"))
        try:
            details = os.stat(full, follow_symlinks=False)
            if not stat.S_ISREG(details.st_mode):
                collection_errors.append("source is not a regular file")
                continue
            if details.st_size + cumulative > MAX_SCAN_TOTAL_BYTES:
                collection_errors.append("Python scan exceeds total byte limit")
                break
            cumulative += details.st_size
        except OSError as exc:
            collection_errors.append(f"source stat failed ({type(exc).__name__})")
            continue
        reports.append(_scan_file(full, file_label=file))
    unparsable = [{"file": r["file"], "detail": r["unparsable"]}
                  for r in reports if r["unparsable"]]

    violations, exempted, owner_sites, sanctioned = [], [], [], []
    reviewed_external, reviewed_pipe, reviewed_pdf_pipe = [], [], []
    pdf_drifted = set()
    drifted, sanctioned_drifted, external_drifted, pipe_drifted = set(), set(), set(), set()
    for report in reports:
        file = report["file"]
        if file in APPROVED_EXEMPT_SITES:
            marked = [site["site_digest"] for site in report["sites"] if site["exempt"]]
            digest = hashlib.sha256("".join(sorted(marked)).encode("ascii")).hexdigest()
            if (len(marked), digest) != APPROVED_EXEMPT_SITES[file]:
                drifted.add(file)
                violations.append({"file": file, "line": 0, "function": "<audit>",
                                   "primitive": "approved-site-set", "kind": "EXEMPTION_DRIFT"})
        for (channel_file, channel_function), (primitives, count, approved) in SANCTIONED_CHANNELS.items():
            if channel_file != file:
                continue
            channel_calls = [
                site["site_digest"] for site in report["sites"]
                if site["function"] == channel_function
                and site["primitive"] in primitives and not site["exempt"]
            ]
            digest = hashlib.sha256("".join(sorted(channel_calls)).encode("ascii")).hexdigest()
            if (len(channel_calls), digest) != (count, approved):
                sanctioned_drifted.add((channel_file, channel_function))
                violations.append({"file": file, "line": 0, "function": channel_function,
                                   "primitive": "sanctioned-channel-set",
                                   "kind": "SANCTIONED_CHANNEL_DRIFT"})
        if file in REVIEWED_EXTERNAL_PROCESS_SITES and not report["unparsable"]:
            external_calls = [site["site_digest"] for site in report["sites"]
                              if site["primitive"] == "external_process"]
            digest = hashlib.sha256("".join(sorted(external_calls)).encode("ascii")).hexdigest()
            if (len(external_calls), digest) != REVIEWED_EXTERNAL_PROCESS_SITES[file]:
                external_drifted.add(file)
                violations.append({"file": file, "line": 0, "function": "<audit>",
                                   "primitive": "reviewed-external-process-set",
                                   "kind": "EXTERNAL_PROCESS_DRIFT"})
        if file in REVIEWED_WITNESS_PIPE_SITES and not report["unparsable"]:
            if (report.get("reviewed_witness_function_digest")
                    != REVIEWED_WITNESS_FUNCTION_AST):
                pipe_drifted.add(file)
                violations.append({"file": file, "line": 0,
                                   "function": "_run_bounded_witness",
                                   "primitive": "reviewed-witness-function-ast",
                                   "kind": "WITNESS_FUNCTION_DRIFT"})
            pipe_calls = [site["site_digest"] for site in report["sites"]
                          if site["primitive"] == "os.write"
                          and site["function"] == "_run_bounded_witness"]
            digest = hashlib.sha256("".join(sorted(pipe_calls)).encode("ascii")).hexdigest()
            if (len(pipe_calls), digest) != REVIEWED_WITNESS_PIPE_SITES[file]:
                pipe_drifted.add(file)
                violations.append({"file": file, "line": 0, "function": "<audit>",
                                   "primitive": "reviewed-witness-pipe-set",
                                   "kind": "WITNESS_PIPE_DRIFT"})
        if file in REVIEWED_PDF_PIPE_SITES and not report["unparsable"]:
            pipe_calls = [site["site_digest"] for site in report["sites"]
                          if site["primitive"] == "os.write"
                          and site["function"] == "_run_pdf_tool"]
            digest = hashlib.sha256("".join(sorted(pipe_calls)).encode("ascii")).hexdigest()
            if (report.get("reviewed_pdf_function_digest") != REVIEWED_PDF_FUNCTION_AST
                    or (len(pipe_calls), digest) != REVIEWED_PDF_PIPE_SITES[file]):
                pdf_drifted.add(file)
                violations.append({"file": file, "line": 0, "function": "_run_pdf_tool",
                                   "primitive": "reviewed-pdf-function-ast",
                                   "kind": "PDF_FUNCTION_DRIFT"})
        for site in report["sites"]:
            if site["file"] in owner:
                owner_sites.append(site)
            elif site["exempt"] and file in APPROVED_EXEMPT_SITES and file not in drifted:
                exempted.append(site)
            elif (_channel_exempt(site) and not site["exempt"] and
                  (site["file"], site["function"]) not in sanctioned_drifted):
                sanctioned.append(dict(site, channel="append_ledger (wave 0 kernel)"))
            elif (site["primitive"] == "external_process" and
                  file in REVIEWED_EXTERNAL_PROCESS_SITES and
                  file not in external_drifted and not site["exempt"]):
                reviewed_external.append(dict(site, channel="reviewed_external_process"))
            elif (site["primitive"] == "os.write" and
                  site["function"] == "_run_bounded_witness" and
                  file in REVIEWED_WITNESS_PIPE_SITES and
                  file not in pipe_drifted and not site["exempt"]):
                reviewed_pipe.append(dict(site, channel="reviewed_witness_stdin_pipe"))
            elif (site["primitive"] == "os.write"
                  and site["function"] == "_run_pdf_tool"
                  and file in REVIEWED_PDF_PIPE_SITES
                  and file not in pdf_drifted and not site["exempt"]):
                reviewed_pdf_pipe.append(dict(site, channel="reviewed_pdf_stdin_pipe"))
            else:
                violations.append(site)

    if violations:
        # a found second writer outranks an incomplete scan: incompleteness must never mask a
        # positive detection, and an incomplete-but-clean scan still cannot report GREEN
        status = "RED"
    elif not reports or unparsable or missing or collection_errors:
        status = "SCANNED_SET_INCOMPLETE"
    else:
        status = "GREEN"
    return {
        "schema": "write_path_audit/1",
        "status": status,
        "scripts_dir": os.path.abspath(scripts_dir),
        "scanned_files": [r["file"] for r in reports],
        "scanned_count": len(reports),
        "collection_errors": collection_errors,
        "expected_module_count": len(expected),
        "missing_expected_modules": missing,
        "unparsable_files": unparsable,
        "violations": violations,
        "exempted_sites": exempted,
        "sanctioned_channel_sites": sanctioned,
        "reviewed_external_process_sites": reviewed_external,
        "reviewed_witness_pipe_sites": reviewed_pipe,
        "reviewed_pdf_pipe_sites": reviewed_pdf_pipe,
        "owner_sites_count": len(owner_sites),
        "owner_sites": owner_sites[:12],
        "second_write_path": bool(violations),
    }


def audit_exit_code(status: str) -> int:
    if status == "RED":
        return EXIT_SECOND_WRITE_PATH
    if status == "SCANNED_SET_INCOMPLETE":
        return EXIT_SCAN_INCOMPLETE
    return EXIT_OK


# --------------------------------------------------------------------- preflight (pure)
def _load_records(paths: StorePaths) -> dict:
    """Current store state: {artifact_id: record}. Read-only; a missing directory is an
    empty store, a corrupt record is a failure (never silently skipped)."""
    store = {}
    if not os.path.isdir(paths.records):
        return store
    seen = set()
    for name in sorted(os.listdir(paths.records)):
        if name.startswith(".tmp-"):
            continue  # not a published record; no reader consumes an atomic-write temp
        if not name.endswith(".json"):
            raise StoreError("unrecognized file in the authoritative record directory")
        if name.casefold() in seen:
            raise StoreError("case-alias record collision")
        seen.add(name.casefold())
        try:
            raw = _read_text(paths.record(name[:-5]))
            if raw is None:
                raise StoreError("record disappeared during snapshot inspection")
            doc = json.loads(raw)
        except (OSError, ValueError) as exc:
            raise StoreError(f"store record {name} is unreadable: {exc}") from exc
        if not isinstance(doc, dict) or doc.get("artifact_id") != name[:-5]:
            raise StoreError(f"store record {name} disagrees with its own artifact_id")
        store[doc["artifact_id"]] = doc
    return store


def load_store(paths: StorePaths) -> dict:
    """Public reader: never exposes a half-batch or certifies a legacy marker."""
    return read_snapshot(paths.root)["records"]


def _load_lifecycle_records(paths):
    records, seen = {}, set()
    if not paths.lifecycle_records or not os.path.isdir(paths.lifecycle_records):
        return records
    for name in sorted(os.listdir(paths.lifecycle_records)):
        if name.startswith(".tmp-"):
            continue
        if not name.endswith(".json") or name.casefold() in seen:
            raise StoreError("unrecognized/case-alias SC05 record")
        seen.add(name.casefold())
        try:
            records[name[:-5]] = json.loads(_read_text(paths.lifecycle_record(name[:-5])))
        except (OSError, ValueError, TypeError) as exc:
            raise StoreError("unreadable SC05 record") from exc
    return records


def _validate_lifecycle_records(records, lifecycle_records):
    import kd_validate as s09
    if set(records) != set(lifecycle_records):
        raise WriteRejection("SC04_SC05_IDENTITY_MISMATCH: one lifecycle record per artifact required")
    for aid, lifecycle_record in lifecycle_records.items():
        if not s09.validate_artifact("lifecycle-record", lifecycle_record)["valid"] \
                or lifecycle_record["lifecycle_state"] != records[aid]["state"] \
                or lifecycle_record["absorbed_into"] != records[aid].get("absorbed_into"):
            raise WriteRejection("SC04_SC05_STATE_MISMATCH: SC04 must project the SC05 state")


def _ledger_seq(paths: StorePaths) -> int:
    """Rows already in the append-only lifecycle ledger (SC07 carrier, S08-registered path)."""
    raw = _read_text(paths.lifecycle_ledger)
    return 0 if raw is None else sum(1 for line in raw.splitlines() if line.strip())


def preflight_intent(intent: dict, store: dict, *, facts,
                     registry: refs.RootRegistry, batch_ids=()) -> list:
    """All refusals happen here, before a single byte is written. Raises on refusal."""
    aid = intent.get("artifact_id")
    op = intent.get("op")
    if not isinstance(aid, str) or not aid:
        raise WriteRejection("intent without artifact_id")
    if op not in LIFECYCLE_ACTIONS:
        raise WriteRejection(f"intent op {op!r} is not a supported lifecycle transaction action "
                             f"{LIFECYCLE_ACTIONS}")
    if op == "DELETE":
        raise WriteRejection("DELETE is not reachable through the write transaction: reversible "
                             "archive is the destructive ceiling (07 §3.1) and kd_gate refuses "
                             "to == 'deleted'; deletion eligibility is a revocable state bit "
                             "(tombstoned_at), never an action taken here")

    record = intent.get("record")
    if not isinstance(record, dict):
        raise WriteRejection(f"intent {aid} carries no record body")
    if record.get("artifact_id") != aid:
        raise WriteRejection("intent and record artifact_id must match")
    if not isinstance(record.get("body"), str) or hashlib.sha256(record["body"].encode("utf-8")).hexdigest() != record.get("content_hash"):
        raise WriteRejection(f"{aid}: content_hash does not bind the actual body bytes")
    mutation = intent.get("mutation") or {}
    if not isinstance(mutation, dict) or mutation.get("artifact_id", aid) != aid:
        raise WriteRejection("mutation and intent artifact_id must match")
    actual_from = (store.get(aid) or {}).get("state", "candidate")
    if mutation.get("from_state", actual_from) != actual_from:
        raise WriteRejection(f"{aid}: mutation lies about the stored from_state")
    import kd_lifecycle as lifecycle
    try:
        lifecycle.assert_transition(actual_from, mutation.get("to_state") or "active", op)
    except lifecycle.LifecycleRefusal as exc:
        raise WriteRejection(f"{aid}: {exc}") from exc

    # --- RH-P0-09: system-owned fields may not ride in on a proposal (REFUSE, not trust-then-stamp)
    forged = [k for k in SYSTEM_OWNED_FIELDS if k in record]
    if forged:
        raise WriteRejection(
            f"{aid}: proposal carries system-owned field(s) {forged}; these are allocated by S12 / "
            "S17 / the ledger owner after authorisation, never chosen by the recorded object "
            "(RH-P0-09, §14-15). A forged record_locator / counter must not become the final value.")
    if record.get("state") not in (None, "candidate"):
        raise WriteRejection(
            f"{aid}: proposal self-declares state={record.get('state')!r}; only S12 (through "
            "kd_gate.apply_mutation) sets the stored state and a proposal may only arrive as "
            "'candidate' (RH-P0-09 T4: Proposal.state=active must not self-promote)")
    if record.get("revision") is not None and (type(record["revision"]) is not int or record["revision"] != 0):
        raise WriteRejection(
            f"{aid}: proposal self-declares revision={record.get('revision')!r}; revision is "
            "incremented only by kd_gate.apply_mutation (RH-P0-09)")

    # --- provenance must have been produced here, not by the recorded object (S13 exit 2)
    ok, why = stamp.verify(record)
    if not ok:
        raise SecondWritePath(f"{aid}: provenance is not a system stamp: {why}")
    body = {k: v for k, v in record.items() if k not in stamp.SELF_DECLARED_KEYS}
    hits = stamp.find_self_declared(body)
    if hits:
        raise SecondWritePath(f"{aid}: self-declared provenance is nested inside the payload "
                              f"({hits}); the recorded object may not fill in its own 出处 "
                              "(05-DATA-MODEL.md:46-47)")
    try:
        # This is a NEW revision, not an in-place change to the old stamped entry.
        # S12 verifies the committed base and retains its immutable history before
        # advancing the current record. S13's existing= guard remains applicable to
        # re-stamping the SAME entry, not to UPDATE/RESTORE's new revision.
        expected = stamp.stamp(body, facts)
    except stamp.ProvenanceViolation as exc:
        raise SecondWritePath(f"{aid}: {exc}") from exc
    if expected["provenance"]["stamp_digest"] != record["provenance"]["stamp_digest"]:
        raise SecondWritePath(
            f"{aid}: the record's provenance block does not match a stamp re-derived from this "
            "run's runtime facts -- it was filled in by the recorded object, or edited after "
            "stamping")

    # --- stale-write guard on the transaction's own revision counter
    prior = store.get(aid)
    if prior is not None:
        expected_rev = intent.get("expected_revision")
        if type(expected_rev) is not int or expected_rev != prior.get("revision", 0):
            raise WriteRejection(f"{aid}: stale write guard, expected_revision={expected_rev} "
                                 f"but store holds {prior.get('revision')}")
        if op == "ADD":
            raise WriteRejection(f"{aid}: ADD cannot overwrite an existing artifact")
    elif op != "ADD" or type(intent.get("expected_revision", 0)) is not int or intent.get("expected_revision", 0) != 0:
        raise WriteRejection(f"{aid}: a missing artifact requires ADD at revision zero")

    # --- evidence refs must resolve, and CM-65 claims must be grounded (S14 exit 2)
    evidence_refs = record.get("evidence_refs") or []
    parsed, shorthand = [], []
    for item in evidence_refs:
        raw = item.get("path") if isinstance(item, dict) else item
        try:
            ref = refs.parse_ref(raw, project=(item.get("project") if isinstance(item, dict)
                                               else None) or "", origin="evidence_refs")
            if isinstance(item, dict) and isinstance(item.get("lines"), dict):
                ref["line_start"] = int(item["lines"]["start"])
                ref["line_end"] = int(item["lines"]["end"])
            parsed.append(ref)
        except refs.RefSyntaxError as exc:
            shorthand.append(str(exc))
    audit = refs.audit_refs(parsed, registry)
    if not evidence_refs:
        # an empty ref set is never a green answer (SC04 requires >=1 evidence ref per
        # artifact; CM-65 makes the body re-checkable only when refs exist)
        raise WriteRejection(f"{aid}: artifact carries no evidence_refs -- refusing to write an "
                             "ungrounded body (05 §2.1 D2); EMPTY_REF_SET is a visible refusal, "
                             "not a pass")
    for ref, out in zip(parsed, audit["findings"]):
        if out["kind"] == "OK":
            ref["resolved_path"] = out["resolved_path"]
    findings = []
    if shorthand:
        findings.append({"kind": "SHORTHAND", "detail": shorthand})
    elif audit["total_refs"] and audit["status"] != refs.STATUS_PASS:
        findings.append({"kind": audit["status"],
                         "detail": [f"{f['ref']['path']}: {f['kind']}"
                                    for f in audit["findings"] if f["kind"] != "OK"][:10]})
    stray = refs.check_claim_binding(record.get("claims") or [], parsed)
    if stray:
        findings.append({"kind": "STRAY_IDENTIFIER", "detail": stray})
    if findings:
        raise SecondWritePath(f"{aid}: evidence binding failed -- " +
                              "; ".join(f"{f['kind']}({f['detail']})" for f in findings))
    # the caller's proposal is never mutated: the result bit is returned and attached to the
    # record copy in commit_batch, so a refused batch leaves retryable input behind
    integrity = refs.refs_integrity_bit(audit)

    # --- absorbed_into: missing means reject the whole intent (07 §3.4)
    siblings = intent.get("absorbed_siblings") or []
    if op == "MERGE" or siblings:
        target = intent.get("absorbed_into", None)
        if target is None:
            raise WriteRejection(f"{aid}: MERGE intent is missing 'absorbed_into' -- refused "
                                 "fail-closed (07 §3.4); 不允许先删了再说")
        if not isinstance(target, str) or not target.strip():
            raise WriteRejection(f"{aid}: absorbed_into={target!r} is empty; an absorb without a "
                                 "verifiable forward reference is undetectable (#29912)")
        # 07 A2: destinations must really exist, or be created by this same batch -- a name
        # the proposal merely asserts is not a destination.
        if target not in store and target not in tuple(batch_ids):
            raise WriteRejection(f"{aid}: absorbed_into target {target!r} does not exist in the "
                                 "store and is not an artifact of this batch")
        if target == aid or record.get("absorbed_into") != target:
            raise WriteRejection(f"{aid}: absorbed_into must match the persisted forward reference and cannot point to self")
    return integrity


# --------------------------------------------------------------------- G1 approval verification
#: Map an adjudicated landing (S10, `06` §5.1) onto the G1 action class (`06:212-270`) so the
#: durable write is gated by the SAME tier rule G1 owns -- S12 classifies by asking G1, never by
#: re-deriving a tier of its own (that would be a second authority for the same decision).
LANDING_TO_G1_ACTION = {
    "L-PATTERN": "pattern-count-only", "L-NOTHING": "nothing-silent",
    "L-NOTHING+LEDGER": "nothing-with-ledger", "L-NOTHING+账": "nothing-with-ledger",
    "L-ARCHIVE": "archive-superseded-entry", "L-SCRIPT": "write-script", "L-LINT": "write-lint",
    "L-TEST": "write-test", "L-EVAL": "write-eval", "L-SKILL": "write-skill",
    "L-RULE-PROJECT": "write-rule-project", "L-RULE-GLOBAL": "write-rule-global",
}
_TIER_RANK = {g1.TIER_R0: 0, g1.TIER_R1: 1, g1.TIER_R2: 2}


def _require_g1_intent_shape(intent) -> None:
    """Validate container shapes before permission/risk checks read nested fields.

    This is not a second SC04 validator: field semantics and state transitions
    remain with preflight_intent/S09. It only prevents untrusted inputs from
    bypassing S12's stable WriteRejection protocol before that preflight.
    """
    if not isinstance(intent, dict) or not isinstance(intent.get("record"), dict):
        raise WriteRejection("G1_INTENT_MALFORMED: intent and record must be objects")
    record = intent["record"]
    if record.get("scope") is not None and not isinstance(record["scope"], dict):
        raise WriteRejection("G1_SCOPE_MALFORMED: record scope must be an object")
    if intent.get("mutation") is not None and not isinstance(intent["mutation"], dict):
        raise WriteRejection("G1_MUTATION_MALFORMED: mutation must be an object")


def _g1_action_for(intent: dict) -> str:
    """Derive risk from the actual resident kind/Scope and content-destroying operation.

    Caller action labels can only agree with that result, never override or lower its tier.
    A deterministic implementation does not turn a resident Rule into a human-free R0 write.
    """
    _require_g1_intent_shape(intent)
    record = intent["record"]
    if intent.get("op") in ("ARCHIVE", "RESTORE"):
        base = "archive-resident" if intent["op"] == "ARCHIVE" else "restore-committed"
        action = base + ("-global" if (record.get("scope") or {}).get("layer") == "global" else "-entry")
    elif intent.get("op") == "MERGE":
        action = "merge-destroying-content" + (
            "-global" if (record.get("scope") or {}).get("layer") == "global" else "")
    elif record.get("kind") == "rule":
        layer = (record.get("scope") or {}).get("layer")
        if layer not in ("project", "global"):
            raise WriteRejection("resident rule needs project/global scope")
        action = "write-rule-" + layer
    elif record.get("kind") in ("skill", "doc", "script", "lint", "test", "eval"):
        action = "write-" + record["kind"]
    else:
        raise WriteRejection("unknown resident artifact kind; refusing risk classification")
    if intent.get("action") is not None and intent["action"] != action:
        raise WriteRejection("action class cannot override the actual resident mutation")
    return action


def _normalize_approval(approval):
    """Accept the shapes G1 emits -- an `approve_and_apply` bundle, a `record_batch_approval`
    result, or a bare list of rows -- and return (rows, txn_id), or None when no approval rode."""
    if approval is None:
        return None
    if isinstance(approval, dict):
        rows, txn_id = approval.get("approve_rows") or approval.get("rows"), approval.get("txn_id")
    elif isinstance(approval, (list, tuple)):
        rows, txn_id = list(approval), None
    else:
        raise WriteRejection("approval must be a G1 bundle / rows, got %r" % type(approval).__name__)
    if not isinstance(rows, list) or not rows or any(not isinstance(row, dict) for row in rows):
        raise WriteRejection("approval carries no G1 approval rows")
    if any(not isinstance(row.get("classification"), dict)
           or type(row["classification"].get("tier")) is not str
           or row["classification"]["tier"] not in _TIER_RANK for row in rows):
        raise WriteRejection("G1_CLASSIFICATION_MALFORMED: approval tier must be R0, R1 or R2")
    row_txns = {row.get("txn_id") for row in rows if isinstance(row.get("txn_id"), str)}
    if len(row_txns) != 1 or any(not isinstance(row.get("txn_id"), str) or not row["txn_id"].strip()
                                 for row in rows):
        raise WriteRejection("approval rows need one nonempty transaction id")
    row_txn = next(iter(row_txns))
    if txn_id is not None and txn_id != row_txn:
        raise WriteRejection("approval bundle and rows name different transactions")
    txn_id = row_txn
    return rows, txn_id


def verify_g1_approvals(intents, approval, human_approved_flag):
    """S12 verifies the G1 approval that gates each intent instead of trusting a bare flag.

    SKILL.md §9.1: `--human-approved` was 'set by the assembly layer and not self-verified by
    S12'. Here a gated intent (tier R1/R2 by G1's own rule, or model-produced) must carry a
    human-labelled, digest-pinned approval row at an adequate tier and in the same transaction;
    anything less refuses fail-closed and writes nothing (`06:186`、`06:247` N27). Returns
    {artifact_id: effective_human_approved} for `kd_gate.apply_mutation`. These are consistency
    checks, NOT cryptographic signatures or authentication of the approval's producer.
    """
    normalized = _normalize_approval(approval)
    rows, txn_id = normalized if normalized else ([], None)
    effective = {}
    for intent in intents:
        _require_g1_intent_shape(intent)
        aid = intent.get("artifact_id")
        mutation = intent.get("mutation") or {}
        produced = mutation.get("produced_by")
        if produced is None:
            produced = (intent.get("record") or {}).get("produced_by")
        kind = produced.get("kind") if isinstance(produced, dict) else produced
        is_model = str(kind or "").lower() == "model"
        action = _g1_action_for(intent)
        classification = g1.classify_action(action, target=intent.get("target", ""))
        tier = classification["tier"]
        if not (classification["requires_human"] or is_model):
            effective[aid] = False            # R0 deterministic path: no human, still only S12 writes
            continue
        digest = g1.approved_digest(intent["record"])
        matches = [r for r in rows
                   if r.get("proposal_digest") == digest and r.get("human_approved") is True
                   and r.get("gate") == "G1" and r.get("per_item_verdict") == "approve"
                   and str(r.get("approved_by", "")).lower() in g1.HUMAN_ACTORS]
        if not matches:
            if rows:
                raise WriteRejection(
                    f"{aid}: DIGEST_MISMATCH -- no G1 approval pins digest {digest[:16]}... for the "
                    f"exact bytes of this {tier} intent; refusing to write, and writing nothing as "
                    f"if it had (`06:186` 失配 → fail-closed 拒绝 apply)")
            if classification["requires_human"] or human_approved_flag:
                raise WriteRejection(
                    f"{aid}: APPROVAL_MISSING -- action {action!r} is tier {tier} / model-produced "
                    f"(requires_human) but no verified G1 approval row pins this digest; the bare "
                    f"--human-approved flag is not evidence S12 trusts (SKILL.md §9.1)")
            effective[aid] = False            # no flag, no bundle: apply_mutation refuses a model intent
            continue
        if len(matches) != 1:
            raise WriteRejection(f"{aid}: ambiguous duplicate approval rows")
        row = matches[0]
        row_tier = row["classification"]["tier"]
        if _TIER_RANK[row_tier] < _TIER_RANK[tier]:
            raise WriteRejection(
                f"{aid}: TIER_NOT_SATISFIED -- action {action!r} requires {tier} but the approval "
                f"was recorded at {row_tier}; a weaker approval cannot authorise a stronger write "
                f"(`06:226` R2 人审 + 确认 flag 是契约本身")
        if classification.get("requires_confirmation_flag") and row.get("confirmation_flag") is not True:
            raise WriteRejection("R2 requires an explicit boolean confirmation")
        if classification.get("requires_second_approver") and (
                row.get("second_approver") not in g1.HUMAN_ACTORS
                or row["second_approver"] == row["approved_by"]):
            raise WriteRejection("global rule requires a different second human approver")
        # §12 / RH-P0-08: the approval must bind THIS write target, not just the record bytes. G1
        # stamped intent_digest(record_digest, target) at approval; recompute it from the intent at
        # hand so a post-approval change to the mutation target is a hard mismatch, not a silent pass.
        expected_intent = g1.intent_digest(digest, intent.get("target", ""))
        if row.get("intent_digest") != expected_intent:
            raise WriteRejection(
                f"{aid}: AUTHORIZATION_DIGEST_MISMATCH -- the G1 approval pins intent/target "
                f"{str(row.get('intent_digest'))[:16]}... but this write intent binds "
                f"{expected_intent[:16]}...; the mutation target changed after approval, so nothing "
                "is written (§12: any bound object changed by one byte => NO WRITE)")
        if txn_id and str(row.get("txn_id") or "").strip() != str(txn_id).strip():
            raise WriteRejection(
                f"{aid}: APPROVE_APPLY_SPLIT -- approval txn {row.get('txn_id')!r} != batch txn "
                f"{txn_id!r}; approve and apply must be one transaction (`06:247` N27)")
        effective[aid] = True
    return effective


def verify_eval_verdict(eval_verdict, intents=None):
    """CM-50 verify-before-persist (`12:140`: S10 写前门 + S16 写前证据 + S12 唯一写者, jointly).

    S12 is the last of the three and the one that actually persists, so it re-checks the S16 eval
    verdict before a single byte is durable -- using S16's OWN closed vocabulary (kd_eval_score is
    resolved at call time; this writer never forks the enum, one Owner for the verdict status).
    The full tree already consumes eval at N28 (`kd_gate_tree.py:239` regression_pass/fail); the
    counting shortcut `evaluate_promotion` deliberately does not, so the durable re-check lands
    here, on the unique write path.

    Every resident intent requires a complete, version-bound SC09 score document (stage='score'),
    separately for each artifact; None or a detached `verdict` block is not sufficient. Anything not
    not PASSED + verified + non-blocking refuses fail-closed and writes NOTHING: FAILED (a
    regression), UNVERIFIED (no tier certifies it) and NOT_RUN all block, and SC09 has no
    WARNING / YELLOW / SOFT-PASS member to slip through (`08:44` 变差即 FAILED / 阻断，不允许「只警告
    不阻断」; `08:57` 禁止晋升).
    """
    if isinstance(eval_verdict, list):
        if not intents or len(eval_verdict) != len(intents):
            raise WriteRejection("EVAL_COVERAGE_MISMATCH: one complete score per artifact required")
        docs = {}
        for doc in eval_verdict:
            source = doc.get("subject") if isinstance(doc, dict) else None
            if not isinstance(source, dict):
                raise WriteRejection("EVAL_DUPLICATE_OR_MISSING_SUBJECT")
            subject = source.get("promoted_from_artifact_id")
            if not isinstance(subject, str) or not subject or subject in docs:
                raise WriteRejection("EVAL_DUPLICATE_OR_MISSING_SUBJECT")
            docs[subject] = doc
        if set(docs) != {i["artifact_id"] for i in intents}:
            raise WriteRejection("EVAL_SUBJECT_MISMATCH")
        return {"required": True, "by_artifact": {
            i["artifact_id"]: verify_eval_verdict(docs[i["artifact_id"]], [i]) for i in intents}}
    if eval_verdict is None:
        raise WriteRejection("EVAL_MISSING: resident writes require the complete S16 score document")
    import kd_eval_score as s16        # noqa: WPS433  the verdict-vocabulary Owner, at call time
    if not isinstance(eval_verdict, dict):
        raise WriteRejection("EVAL_MALFORMED: score document must be an object")
    verdict = (eval_verdict.get("verdict")
               if isinstance(eval_verdict.get("verdict"), dict) else eval_verdict)
    if not isinstance(verdict, dict) or "status" not in verdict:
        raise WriteRejection("EVAL_MALFORMED: eval_verdict carries no SC09 verdict.status -- S12 "
                             "will not guess a verdict shape (the vocabulary is closed, 08:44). "
                             "Pass the complete S16 SC09 score document, not a verdict block.")
    status, blocking, verified = (verdict.get("status"), verdict.get("blocking"),
                                  verdict.get("verified"))
    closed_enum = (s16.STATUS_PASSED, s16.STATUS_FAILED, s16.STATUS_UNVERIFIED, "NOT_RUN")
    if status not in closed_enum:
        raise WriteRejection("EVAL_MALFORMED: verdict status is outside the closed SC09 enum")
    if status != s16.STATUS_PASSED or blocking is not False or verified is not True \
            or verdict.get("regression_detected") is not False:
        # Only the closed status enum is safe to display. reasons and other
        # caller-supplied fields may contain private source or model text.
        raise WriteRejection(
            f"EVAL_BLOCKED: S16 verdict status={status}; a verified, non-regressing "
            "PASSED score is required before any S12 write")
    try:
        s16.assert_verified(eval_verdict)       # full SC09, not a self-declared verdict flag
    except s16.NotVerified as exc:
        raise WriteRejection("EVAL_BLOCKED: S16 score verification predicates failed") from exc
    if intents is not None and any(intent["artifact_id"] != eval_verdict["subject"]["promoted_from_artifact_id"]
                                   for intent in intents):
        raise WriteRejection("EVAL_SUBJECT_MISMATCH: this score does not cover every written artifact")
    return {"required": True, "status": status, "blocking": bool(blocking),
            "verified": bool(verified),
            "regression_detected": bool(verdict.get("regression_detected")),
            "reasons": verdict.get("reasons"), "checked_by": "kd_write_txn+S16"}


def verify_adjudication(intents, adjudication):
    """Complete PROMOTE or explicit ARCHIVE paths; failed Eval is never writable."""
    import kd_gate_tree as tree
    import kd_validate as validator
    docs = adjudication if isinstance(adjudication, list) else [adjudication]
    verdicts = {}
    for doc in docs:
        verdict = doc.get("verdict", doc) if isinstance(doc, dict) else None
        if not validator.validate_artifact("verdict", verdict).get("valid"):
            raise WriteRejection("S10_MISSING_OR_INVALID: complete per-item SC12 verdict required")
        cid = verdict["candidate_id"]
        if cid in verdicts:
            raise WriteRejection("S10_DUPLICATE_CANDIDATE")
        permitted = (verdict["item_verdict"] == "PROMOTE" and verdict["exit_code"] == 0) or (
            verdict["disposition"] == "ARCHIVE" and verdict["item_verdict"] == "RETIRE_TO_ARCHIVE"
            and verdict["exit_code"] == 3 and verdict["terminal_landing"] == "L-ARCHIVE")
        if not permitted or verdict.get("refusal") is not None or verdict.get("human_approved") is not True:
            raise WriteRejection("S10_BLOCKED: non-promotion/deferred verdict cannot authorize a write")
        trace = verdict["decision_path"]
        if trace[0]["node"] != "N00" or not {"N25", "N26", "N27", "N28", "N29"} <= {r["node"] for r in trace}:
            raise WriteRejection("S10_INCOMPLETE_PATH")
        for index, row in enumerate(trace):
            node = row["node"]
            if node not in tree.NODE_BY_ID or row["judge"] != tree.NODE_BY_ID[node]["judge"] \
                    or (node, row.get("condition"), row.get("to")) not in {e[:3] for e in tree.EDGE_TABLE}:
                raise WriteRejection("S10_INVALID_PATH_EDGE")
            expected = trace[index + 1]["node"] if index + 1 < len(trace) else verdict["terminal_landing"]
            if row.get("to") != expected:
                raise WriteRejection("S10_DISCONTINUOUS_PATH")
        verdicts[cid] = verdict
    for intent in intents:
        cid = intent.get("candidate_id") or intent["artifact_id"]
        verdict = verdicts.get(cid)
        record = intent["record"]
        if verdict is None or verdict.get("scope") != record.get("scope") \
                or verdict.get("identity_digest") != (record.get("identity") or {}).get("canonical_key") \
                or not verdict.get("identity_digest") or verdict.get("disposition") != intent["op"]:
            raise WriteRejection("S10_BINDING_MISMATCH: candidate/scope/identity/action changed")
        landing = verdict["terminal_landing"]
        action = LANDING_TO_G1_ACTION.get(landing)
        if intent["op"] == "ARCHIVE":
            if landing != "L-ARCHIVE":
                raise WriteRejection("S10_LANDING_MISMATCH")
        elif intent["op"] == "RESTORE":
            kind = record.get("kind")
            expected = "L-RULE-" + record["scope"]["layer"].upper() if kind == "rule" else "L-" + str(kind).upper()
            if landing != expected:
                raise WriteRejection("S10_LANDING_MISMATCH")
        elif intent["op"] != "MERGE" and action != _g1_action_for(intent):
            raise WriteRejection("S10_LANDING_MISMATCH")
    if len(verdicts) != len(intents):
        raise WriteRejection("S10_UNRELATED_VERDICT")
    return verdicts


# --------------------------------------------------------------------- transaction protocol
PROTOCOL = "kd-file-transaction/3"


def _json_text(doc) -> str:
    return json.dumps(doc, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"


def _hash_text(value: str | None):
    return None if value is None else hashlib.sha256(value.encode("utf-8")).hexdigest()


def _read_bytes(path: str) -> bytes | None:
    if not os.path.lexists(path):
        return None
    flags = (os.O_RDONLY | os.O_NONBLOCK | getattr(os, "O_NOFOLLOW", 0)
             | getattr(os, "O_CLOEXEC", 0))
    fd = os.open(path, flags)
    with os.fdopen(fd, "rb") as fh:
        info = os.fstat(fh.fileno())
        named = os.stat(path, follow_symlinks=False)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 \
                or (named.st_dev, named.st_ino) != (info.st_dev, info.st_ino):
            raise StoreError("owned carrier is not a regular, unaliased file")
        data = fh.read()
        after = os.fstat(fh.fileno())
        named = os.stat(path, follow_symlinks=False)
        if (info.st_size, info.st_mtime_ns, info.st_ctime_ns) != \
                (after.st_size, after.st_mtime_ns, after.st_ctime_ns) \
                or (named.st_dev, named.st_ino) != (info.st_dev, info.st_ino) \
                or named.st_nlink != 1:
            raise StoreError("owned carrier changed during inspection")
        return data


def _read_text(path: str) -> str | None:
    raw = _read_bytes(path)
    try:
        return None if raw is None else raw.decode("utf-8")
    except UnicodeError as exc:
        raise StoreError("owned carrier contains incomplete/non-UTF-8 bytes") from exc


def _require_protocol_layout(paths):
    for path in (paths.lock, paths.pending, paths.history, paths.lifecycle_records, paths.commit_point,
                 paths.journal, paths.lifecycle_ledger):
        if path is None:
            raise WriteRejection("PROTOCOL_LAYOUT_MISSING: old manifests require explicit migration")
        paths.authorize(path)
    if os.path.dirname(paths.lock) != paths.ledger_dir or os.path.dirname(paths.pending) != paths.ledger_dir:
        raise WriteRejection("protocol lock and journal must live in the declared ledger")


@contextmanager
def _store_lock(paths, *, exclusive: bool, create: bool = False):
    """Nonblocking POSIX lock. Never unlink it: unlink would split the locking identity."""
    _require_protocol_layout(paths)
    paths.lock = layout.safe_path(paths.root, paths.rel(paths.lock))
    if create:
        _mkdir_durable(paths.ledger_dir)
    if not os.path.lexists(paths.lock) and not create:
        raise StoreError("transaction lock missing; a populated legacy store is not certified")
    flags = os.O_RDWR if exclusive else os.O_RDONLY
    if create:
        flags |= os.O_CREAT
    flags |= os.O_NONBLOCK | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_CLOEXEC", 0)
    fd = os.open(paths.lock, flags, 0o600)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise StoreError("transaction lock must be a regular, unaliased inode")
        try:
            fcntl.flock(fd, (fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH) | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise WriteRejection("STORE_BUSY: another reader/writer owns the transaction lock") from exc
        named = os.stat(paths.lock, follow_symlinks=False)
        if (named.st_dev, named.st_ino) != (info.st_dev, info.st_ino) or named.st_nlink != 1:
            raise StoreError("transaction lock identity changed")
        if create:
            os.fsync(fd)
            _fsync_dir(paths.ledger_dir)
        yield
    finally:
        os.close(fd)  # process exit/crash also releases flock; the file itself stays


def _file_state(paths) -> dict:
    state = {}
    for aid in _load_records(paths):
        path = paths.record(aid)
        raw = _read_bytes(path)
        if raw is None:
            raise StoreError("record disappeared during snapshot inspection")
        state[paths.rel(path)] = hashlib.sha256(raw).hexdigest()
    for aid in _load_lifecycle_records(paths):
        path = paths.lifecycle_record(aid)
        raw = _read_bytes(path)
        if raw is None:
            raise StoreError("SC05 disappeared during snapshot inspection")
        state[paths.rel(path)] = hashlib.sha256(raw).hexdigest()
    for path in (paths.lifecycle_ledger, paths.journal):
        raw = _read_bytes(path)
        if raw is not None:
            state[paths.rel(path)] = hashlib.sha256(raw).hexdigest()
    return state


def _snapshot_locked(paths, *, allow_pending: bool = False) -> dict:
    if not allow_pending and paths.pending and os.path.lexists(paths.pending):
        raise StoreError("RECOVERY_REQUIRED: an interrupted transaction must be inspected/recovered")
    text = _read_text(paths.commit_point)
    records = _load_records(paths)
    lifecycle_records = _load_lifecycle_records(paths)
    files = _file_state(paths)
    if text is None:
        if files:
            raise StoreError("UNCERTAIN_BATCH: records or ledger exist without a hash-bound commit")
        return {"state": "EMPTY", "records": {}, "lifecycle_records": {}, "provenance_records": {}, "marker": None, "snapshot_digest": None,
                "source_roots": []}
    try:
        marker = json.loads(text)
        if marker["protocol"] != PROTOCOL or marker["files"] != files \
                or marker["layout_digest"] != g1.binding_digest(paths.manifest) \
                or type(marker["generation"]) is not int or marker["generation"] < 1 \
                or marker["kd-ledger-rows"] != _ledger_seq(paths) \
                or not isinstance(marker["committed_transactions"], dict) \
                or marker["committed_transactions"].get(marker["txn_id"]) != marker["batch_digest"]:
            raise ValueError("marker does not bind all current carriers")
        history_path = layout.safe_path(paths.root, paths.rel(paths.history) + "/" + marker["txn_id"] + ".json")
        journal = _load_transaction(paths, history_path)
        if journal["digest"] != marker["batch_digest"] or journal["after_marker"] != marker:
            raise ValueError("committed transaction history differs from its commit point")
        source_roots, provenance_records, provenance_revisions = set(), {}, {}
        for transaction_id, digest in marker["committed_transactions"].items():
            history = layout.safe_path(paths.root, paths.rel(paths.history) + "/" + transaction_id + ".json")
            transaction = journal if transaction_id == marker["txn_id"] else _load_transaction(paths, history)
            if transaction["digest"] != digest or transaction["request"]["txn_id"] != transaction_id:
                raise ValueError("retained transaction differs from the committed history index")
            source_roots.update(source["root"] for source in transaction["request"]["sources"])
            for aid, provenance_record in transaction["provenance_records"].items():
                revision = transaction["snapshot_records"][aid]["revision"]
                if revision == provenance_revisions.get(aid) and provenance_records[aid] != provenance_record:
                    raise ValueError("conflicting provenance for one artifact revision")
                if revision > provenance_revisions.get(aid, 0):
                    provenance_revisions[aid], provenance_records[aid] = revision, provenance_record
        if set(provenance_records) != set(records) or any(
                provenance_revisions[aid] != record["revision"] for aid, record in records.items()):
            raise ValueError("current artifact revision lacks immutable SC06")
        if any(not isinstance(root, str) or not os.path.isabs(root) for root in source_roots):
            raise ValueError("retained source root is not an explicit absolute path")
        _validate_final_artifacts(records)
        _validate_lifecycle_records(records, lifecycle_records)
    except (ValueError, KeyError, TypeError, AttributeError, layout.LayoutViolation, WriteRejection) as exc:
        raise StoreError("UNCERTAIN_BATCH: invalid/mismatched hash-bound commit point") from exc
    return {"state": "COMMITTED", "records": records, "lifecycle_records": lifecycle_records,
            "provenance_records": provenance_records, "marker": marker,
            "snapshot_digest": _hash_text(text), "source_roots": sorted(source_roots)}


def read_snapshot(store_dir: str) -> dict:
    """One verified, mutually consistent committed snapshot. A derived reader uses this API."""
    paths = resolve_paths(store_dir)
    if not os.path.lexists(paths.commit_point) and not _file_state(paths) \
            and not (paths.pending and os.path.lexists(paths.pending)) \
            and not (paths.lock and os.path.lexists(paths.lock)):
        return {"state": "EMPTY", "records": {}, "lifecycle_records": {}, "provenance_records": {}, "marker": None, "snapshot_digest": None,
                "source_roots": []}
    with _store_lock(paths, exclusive=False):
        return _snapshot_locked(paths)


@contextmanager
def locked_snapshot(store_dir: str):
    """Public, read-only lease used by a projector while publishing one fixed generation.

    It holds the shared lock through the caller's context, preventing a stale switch. It
    does not expose any authority to mutate records or to change the commit point.
    """
    paths = resolve_paths(store_dir)
    with _store_lock(paths, exclusive=False):
        yield _snapshot_locked(paths)


def _committed_revision(paths, snapshot, transaction_id, artifact_id):
    if not isinstance(transaction_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", transaction_id):
        raise WriteRejection("RESTORE_SOURCE_INVALID: unsafe transaction ID")
    paths.record(artifact_id)
    digest = (snapshot["marker"] or {}).get("committed_transactions", {}).get(transaction_id)
    if not digest:
        raise WriteRejection("RESTORE_SOURCE_NOT_COMMITTED: no indexed committed history")
    path = layout.safe_path(paths.root, paths.rel(paths.history) + "/" + transaction_id + ".json")
    history = _load_transaction(paths, path)
    if history["digest"] != digest or artifact_id not in history["snapshot_records"]:
        raise WriteRejection("RESTORE_SOURCE_INVALID: history does not bind this artifact")
    record = history["snapshot_records"][artifact_id]
    source = {"txn_id": transaction_id, "generation": history["after_marker"]["generation"],
              "batch_digest": digest, "record_digest": g1.binding_digest(record)}
    return {"source": source, "record": record}


def read_committed_revision(store_dir, transaction_id, artifact_id):
    """Read-only public rollback source, from verified indexed history under a shared lease.

    Returning old content grants no write authority. Applying it requires a new full
    Eval, G1 confirmation and three fresh bound receipts through commit_batch.
    """
    paths = resolve_paths(store_dir)
    with _store_lock(paths, exclusive=False):
        return _committed_revision(paths, _snapshot_locked(paths), transaction_id, artifact_id)


def read_provenance(store_dir, artifact_id, *, transaction_id=None):
    """Read current SC06, or the exact SC06 issued by one indexed committed transaction.

    The same public shared lease and history validation protect both body and provenance.
    Uncommitted history, a missing version or unknown protocol never yields trusted facts.
    """
    paths = resolve_paths(store_dir)
    paths.record(artifact_id)
    with _store_lock(paths, exclusive=False):
        snapshot = _snapshot_locked(paths)
        if transaction_id is None:
            rows = snapshot["provenance_records"]
        else:
            _committed_revision(paths, snapshot, transaction_id, artifact_id)
            path = layout.safe_path(paths.root, paths.rel(paths.history) + "/" + transaction_id + ".json")
            rows = _load_transaction(paths, path)["provenance_records"]
        if artifact_id not in rows:
            raise WriteRejection("PROVENANCE_VERSION_MISSING: no SC06 issued for this artifact/version")
        return rows[artifact_id]


_CONTENT_FIELDS = ("kind", "body", "content_hash", "identity", "scope", "claims", "evidence_refs",
                   "produced_by", "absorbed_into")


def _verify_lifecycle_source(paths, snapshot, intent):
    aid, op, record = intent["artifact_id"], intent["op"], intent["record"]
    if op not in ("ARCHIVE", "RESTORE"):
        if "restore_source" in intent:
            raise WriteRejection("RESTORE_SOURCE_UNEXPECTED")
        return
    prior = snapshot["records"].get(aid)
    if prior is None:
        raise WriteRejection("LIFECYCLE_RESIDENT_MISSING")
    if op == "ARCHIVE":
        if "restore_source" in intent or any(record.get(key) != prior.get(key) for key in _CONTENT_FIELDS):
            raise WriteRejection("ARCHIVE_CONTENT_CHANGED: archive may only retire the current body")
        return
    source = intent.get("restore_source")
    if not isinstance(source, dict):
        raise WriteRejection("RESTORE_SOURCE_MISSING")
    historical = _committed_revision(paths, snapshot, source.get("txn_id"), aid)
    old = historical["record"]
    if source != historical["source"] or old["state"] != "active" \
            or old["revision"] >= prior["revision"] \
            or any(old.get(key) != prior.get(key) for key in ("kind", "identity", "scope")) \
            or any(record.get(key) != old.get(key) for key in _CONTENT_FIELDS):
        raise WriteRejection("RESTORE_SOURCE_MISMATCH: same identity/Scope and exact older active content required")
    if prior["state"] == "active" and record["content_hash"] == prior["content_hash"]:
        raise WriteRejection("RESTORE_NO_CHANGE: current active content is already the selected revision")


def _policy_thresholds(policy, facts):
    try:
        cfg = kd_gate.runtime_thresholds(policy)
    except prov.SchemaError as exc:
        raise WriteRejection(str(exc)) from exc
    if not isinstance(facts, stamp.RuntimeFacts) or facts.config_sha != g1.binding_digest(policy):
        raise WriteRejection("CONFIG_BINDING_MISMATCH: runtime facts must bind the policy actually used")
    return cfg


def _eval_documents(eval_verdict, intents):
    verify_eval_verdict(eval_verdict, intents)
    docs = eval_verdict if isinstance(eval_verdict, list) else [eval_verdict]
    return {d["subject"]["promoted_from_artifact_id"]: d for d in docs}


def _source_bindings(intents, registry):
    bindings = []
    for intent in intents:
        for item in intent["record"].get("evidence_refs", []):
            ref = refs.parse_ref(item["path"], project=item["project"], origin="evidence_refs")
            ref.update(line_start=item["lines"]["start"], line_end=item["lines"]["end"])
            resolved = refs.resolve_one(ref, registry)
            if resolved["kind"] != "OK":
                raise WriteRejection("SOURCE_BINDING_UNRESOLVED")
            with open(resolved["resolved_path"], "rb") as fh:
                digest = hashlib.sha256(fh.read()).hexdigest()
            bindings.append({"artifact_id": intent["artifact_id"], "ref": item,
                             "root": registry.roots[resolved["root"]], "file_digest": digest})
    return bindings


def _replay_adjudication(intents, candidates, verdicts, eval_docs, approval, cfg, evidence):
    """S10 is the one Owner. A fabricated trace must not bypass a currently deferred gate."""
    import kd_gate_tree as tree
    if not isinstance(candidates, list) or len(candidates) != len(intents) \
            or any(not isinstance(c, dict) for c in candidates):
        raise WriteRejection("S10_INPUTS_MISSING: complete per-item candidates required for replay")
    by_id = {c.get("candidate_id"): c for c in candidates if isinstance(c.get("candidate_id"), str)}
    if len(by_id) != len(candidates):
        raise WriteRejection("S10_DUPLICATE_OR_MISSING_CANDIDATE")
    normalized = _normalize_approval(approval)
    if normalized is None:
        raise WriteRejection("S10_REPLAY_APPROVAL_MISSING")
    approve_rows, _ = normalized
    for intent in intents:
        aid, rec = intent["artifact_id"], intent["record"]
        cid = intent.get("candidate_id") or aid
        candidate = by_id.get(cid)
        if not candidate or candidate.get("artifact_id", cid) != aid \
                or candidate.get("scope") != rec.get("scope") \
                or (candidate.get("identity") or {}).get("l0_digest") != rec["identity"]["canonical_key"]:
            raise WriteRejection("S10_INPUT_BINDING_MISMATCH")
        scoped = _scoped_evidence(evidence, rec["scope"])
        counts = kd_gate.evaluate_promotion(scoped, cfg=cfg)
        ledger = candidate.get("ledger") or {}
        if ledger.get("support_count") != counts["support"]["distinct_evidence_count"] \
                or ledger.get("distinct_occurrence_count") != counts["support"]["independent_cohort_count"] \
                or g1.binding_digest(candidate.get("evidence")) != g1.binding_digest(scoped):
            raise WriteRejection("S10_EVIDENCE_BINDING_MISMATCH: no caller-supplied inflated support")
        row = next((r for r in approve_rows
                    if r["proposal_digest"] == g1.approved_digest(rec)), None)
        if row is None:
            raise WriteRejection("S10_REPLAY_APPROVAL_BINDING_MISMATCH: no G1 row pins this record")
        context = {"approved": True, "approver": row["approved_by"],
                   "second_approver": row.get("second_approver"),
                   "risk_tier": row["classification"]["tier"],
                   "confirmation_flag": row.get("confirmation_flag") is True}
        replay = tree.adjudicate(candidate, cfg=cfg, approval_context=context, eval_verdict=eval_docs[aid])
        if replay["verdict"] != verdicts[cid]:
            raise WriteRejection("S10_REPLAY_MISMATCH: supplied verdict is not the current full-tree result")


def _scoped_evidence(evidence, scope):
    return [row for row in evidence if isinstance(row, dict) and row.get("scope") == scope
            and isinstance(row.get("cohort"), dict)
            and row["cohort"].get("workspace") == scope.get("workspace")
            and row["cohort"].get("project") == scope.get("project")]


def _compiler_digest():
    """Bind installed runtime bytes, not a caller's claimed version string."""
    package = os.path.dirname(HERE)
    digests = {}
    def unreadable(error):
        raise WriteRejection("COMPILER_SCAN_INCOMPLETE: " + type(error).__name__)
    for directory in ("scripts", "schemas", "references"):
        base = os.path.join(package, directory)
        for current, dirs, names in os.walk(base, followlinks=False, onerror=unreadable):
            dirs[:] = sorted(d for d in dirs if d != "__pycache__")
            if any(os.path.islink(os.path.join(current, d)) for d in dirs):
                raise WriteRejection("compiler package contains a linked directory")
            for name in sorted(names):
                if name.endswith((".pyc", ".pyo")) or name == ".DS_Store":
                    continue
                path = os.path.join(current, name)
                if os.path.islink(path):
                    raise WriteRejection("compiler package contains a linked file")
                with open(path, "rb") as fh:
                    digests[os.path.relpath(path, package)] = hashlib.sha256(fh.read()).hexdigest()
    return g1.binding_digest(digests)


def _assemble(paths, snapshot, intents, evidence, facts, registry, approval, adjudication, eval_verdict,
              candidates, policy):
    store = snapshot["records"]
    cfg = _policy_thresholds(policy, facts)
    verdicts = verify_adjudication(intents, adjudication)
    eval_docs = _eval_documents(eval_verdict, intents)
    effective = verify_g1_approvals(intents, approval, False)
    _replay_adjudication(intents, candidates, verdicts, eval_docs, approval, cfg, evidence)
    import kd_validate as validator
    committed, lifecycle_records, events, provenance_records = {}, {}, [], {}
    seq = (snapshot["marker"] or {}).get("kd-ledger-rows", 0)
    for intent in intents:
        aid = intent["artifact_id"]
        _verify_lifecycle_source(paths, snapshot, intent)
        if intent["op"] == "ADD" and any(
                prior.get("scope") == intent["record"].get("scope")
                and (prior.get("identity") or {}).get("canonical_key")
                    == (intent["record"].get("identity") or {}).get("canonical_key")
                and prior.get("state") == "active" for prior in dict(store, **committed).values()):
            raise WriteRejection("DUPLICATE_KNOWLEDGE: existing active identity requires Stage-0 disposition")
        if intent.get("target") != paths.rel(paths.record(aid)):
            raise WriteRejection("WRITE_TARGET_MISMATCH: approved target must be the actual resolved record path")
        integrity = preflight_intent(intent, store, facts=facts, registry=registry,
                                     batch_ids=[i["artifact_id"] for i in intents])
        mutation = dict(intent.get("mutation") or {})
        mutation.update(artifact_id=aid)
        mutation.setdefault("from_state", (store.get(aid) or {}).get("state", "candidate"))
        produced = intent["record"].get("produced_by")
        mutation.setdefault("produced_by", produced.get("kind") if isinstance(produced, dict) else produced)
        mutation["to_state"] = mutation.get("to_state") or "active"
        decision = kd_gate.evaluate_promotion(_scoped_evidence(evidence, intent["record"]["scope"]), cfg=cfg)
        try:
            projected = dict(store, **committed)
            row = kd_gate.apply_mutation(projected, mutation, dict(decision, human_approved=effective[aid]))
        except kd_gate.WritePathViolation as exc:
            raise WriteRejection(f"{aid}: {exc}") from exc
        import kd_lifecycle as lifecycle
        producer = intent["record"].get("produced_by") or {}
        if not isinstance(producer, dict):
            raise WriteRejection("artifact producer must be a typed object")
        try:
            lifecycle_records[aid] = lifecycle.committed_record(
                snapshot["lifecycle_records"].get(aid), action=intent["op"], to_state=row["state"],
                created_by=producer.get("name") or producer.get("kind"), at=facts.created_at,
                absorbed_into=intent.get("absorbed_into"), evaluation_verified=True)
        except lifecycle.LifecycleRefusal as exc:
            raise WriteRejection(f"{aid}: {exc.code}: {exc}") from exc
        record = dict(intent["record"], state=lifecycle_records[aid]["lifecycle_state"], revision=row["revision"],
                      refs_integrity=integrity, written_by=paths.writer)
        import kd_eval_score as scorer
        score = eval_docs[aid]
        new_verification = scorer.verification_evidence(score, record["content_hash"])
        prior_verification = (store.get(aid) or {}).get("verification", [])
        if any(row["run_evidence_hash"] == new_verification["run_evidence_hash"] for row in prior_verification):
            raise WriteRejection("FRESH_EVAL_REQUIRED: a committed score cannot authorize a new revision")
        record["verification"] = list(prior_verification) + [new_verification]
        committed[aid] = record
        actor = "agent" if facts.actor.startswith("agent:") else facts.actor
        event = lifecycle.make_event(intent["op"], "artifact", aid, actor=actor,
                                     reason=intent.get("reason") or _reason_for(intent["op"]),
                                     at=facts.created_at, supersedes=intent.get("supersedes"),
                                     superseded_by=intent.get("superseded_by"))
        seq += 1
        event.update(seq=seq, record_locator={"ledger": paths.rel(paths.lifecycle_ledger), "seq": seq})
        event["content_hash"] = prov.content_hash(event)
        if not validator.validate_artifact("lifecycle-event-ledger", event).get("valid"):
            raise WriteRejection("SC07_INVALID: no durable transaction has started")
        try:
            provenance_records[aid] = stamp.provenance_record(record, _scoped_evidence(evidence, record["scope"]), event)
        except stamp.InvalidFacts as exc:
            raise WriteRejection(f"SC06_INVALID: {exc}") from exc
        events.append(event)
    _validate_final_artifacts(committed)
    _validate_lifecycle_records(committed, lifecycle_records)
    return committed, lifecycle_records, events, provenance_records


def _input_digest(intents, evidence, facts, approval, adjudication, eval_verdict, candidates, policy):
    rows, txn_id = _normalize_approval(approval)
    return g1.binding_digest({"txn_id": txn_id, "intents": intents, "evidence": evidence,
                              "facts": {"generation": facts.generation(), "actor": facts.actor},
                              "rows": rows, "adjudication": adjudication, "eval": eval_verdict,
                              "candidates": candidates, "policy": policy})


def _request(paths, snapshot, intents, evidence, facts, registry, approval, adjudication,
             eval_verdict, candidates, policy):
    rows, txn_id = _normalize_approval(approval)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", txn_id):
        raise WriteRejection("unsafe transaction id")
    items = []
    for intent in intents:
        classification = g1.classify_action(_g1_action_for(intent), target=intent["target"])
        items.append({"artifact_id": intent["artifact_id"], "target": intent["target"],
                      "op": intent["op"], "mutation": intent.get("mutation"),
                      "expected_revision": intent.get("expected_revision", 0),
                      "restore_source": intent.get("restore_source"),
                      "record_digest": g1.binding_digest(intent["record"]),
                      "required_approvers": 2 if classification["requires_second_approver"] else 1})
    return {"schema": "kd-commit-authorization/1", "store_root": paths.root,
            "layout_digest": g1.binding_digest(paths.manifest), "txn_id": txn_id,
            "base_snapshot": snapshot["snapshot_digest"], "items": items,
            "policy_digest": g1.binding_digest(policy), "compiler_digest": _compiler_digest(),
            "input_digest": _input_digest(intents, evidence, facts, approval, adjudication,
                                          eval_verdict, candidates, policy),
            "sources": _source_bindings(intents, registry)}


def _eval_binding(request, eval_verdict):
    return {"schema": "kd-evaluation-binding/1", "items": request["items"],
            "scores_digest": g1.binding_digest(eval_verdict),
            "sources": request["sources"],
            "policy_digest": request["policy_digest"], "compiler_digest": request["compiler_digest"]}


def _evidence_binding(request, evidence, candidates):
    """Source-fact attestation is separate from consent and evaluation, not a new core schema.

    S10 consumes task spans, retry timing, prior rejection and pending watermarks from its
    candidate input. Replaying S10 cannot establish that those observations are genuine.
    The trusted source host must attest to the evidence and all candidate observations for
    these exact artifact/source/policy/compiler versions before a transaction may start.
    """
    return {"schema": "kd-observation-binding/1", "items": request["items"],
            "evidence_digest": g1.binding_digest(evidence), "observations": candidates,
            "sources": request["sources"], "policy_digest": request["policy_digest"],
            "compiler_digest": request["compiler_digest"]}


def _verify_observations(proof, binding, verifier):
    if not callable(verifier):
        raise WriteRejection("TRUSTED_OBSERVATIONS_SOURCE_MISSING: the source host must attest measured facts")
    try:
        # Finite JSON copies prevent a verifier from changing the durable-phase inputs.
        result = verifier(json.loads(_json_text(proof)), json.loads(_json_text(binding)))
    except Exception as exc:
        raise WriteRejection("OBSERVATIONS_AUTHENTICATION_FAILED: source host verification failed") from exc
    if not isinstance(result, dict) or result.get("verified") is not True \
            or result.get("measured") is not True \
            or result.get("binding_digest") != g1.binding_digest(binding) \
            or result.get("observations_digest") != g1.binding_digest(binding["observations"]) \
            or not isinstance(result.get("observer_id"), str) or not result["observer_id"].strip() \
            or result["observer_id"] != result["observer_id"].strip():
        raise WriteRejection("OBSERVATIONS_AUTHENTICATION_FAILED: candidate assertions are not source measurements")
    return {"binding_digest": g1.binding_digest(binding),
            "observations_digest": result["observations_digest"], "observer_id": result["observer_id"]}


def prepare_commit(store_dir, intents, *, evidence, facts, registry, approval, adjudication,
                   eval_verdict, candidates, policy):
    """Read-only three-channel request builder. Never creates a lock, manifest or store."""
    _require_loaded_module_origins()
    if not isinstance(intents, list) or not intents:
        raise WriteRejection("prepare_commit requires a nonempty batch of record intents")
    for intent in intents:
        _require_g1_intent_shape(intent)
    aids = [i.get("artifact_id") for i in intents]
    if any(not isinstance(aid, str) or not aid for aid in aids) \
            or len({aid.casefold() for aid in aids}) != len(aids):
        raise WriteRejection("batch artifact IDs must be nonempty and distinct")
    verify_adjudication(intents, adjudication)
    verify_eval_verdict(eval_verdict, intents)
    _policy_thresholds(policy, facts)
    normalized = _normalize_approval(approval)
    if not isinstance(approval, dict) or normalized is None or len(normalized[0]) != len(intents):
        raise WriteRejection("G1_COVERAGE_MISMATCH")
    if not isinstance(evidence, list) or not isinstance(registry, refs.RootRegistry):
        raise WriteRejection("explicit evidence and source-root registry required")
    paths = resolve_paths(store_dir)
    _require_protocol_layout(paths)
    snapshot = read_snapshot(store_dir)
    _assemble(paths, snapshot, intents, evidence, facts, registry, approval,
              adjudication, eval_verdict, candidates, policy)
    request = _request(paths, snapshot, intents, evidence, facts, registry, approval,
                       adjudication, eval_verdict, candidates, policy)
    return {"approval_binding": request, "evaluation_binding": _eval_binding(request, eval_verdict),
            "evidence_binding": _evidence_binding(request, evidence, candidates)}


def _load_transaction(paths, path):
    """Validate ALL journal targets and payloads before recovery can mutate anything."""
    try:
        doc = json.loads(_read_text(path))
        body = {k: v for k, v in doc.items() if k not in ("digest", "after_marker")}
        if doc["protocol"] != PROTOCOL or doc["digest"] != g1.binding_digest(body) \
                or doc["root"] != paths.root or doc["layout_digest"] != g1.binding_digest(paths.manifest) \
                or doc["after_marker"]["batch_digest"] != doc["digest"] \
                or doc["after_marker"]["txn_id"] != doc["request"]["txn_id"]:
            raise ValueError("journal identity mismatch")
        if not isinstance(doc["request"].get("txn_id"), str) \
                or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", doc["request"]["txn_id"]):
            raise ValueError("unsafe journal transaction id")
        files = doc["files"]
        if not isinstance(files, dict) or not files:
            raise ValueError("empty journal")
        allowed = {paths.rel(paths.journal), paths.rel(paths.lifecycle_ledger)}
        for rel, change in files.items():
            target = layout.safe_path(paths.root, rel)
            if rel not in allowed:
                aid = os.path.basename(target)[:-5]
                expected_path = (paths.record(aid) if os.path.dirname(target) == paths.records else
                                 paths.lifecycle_record(aid) if os.path.dirname(target) == paths.lifecycle_records else None)
                if target != expected_path:
                    raise ValueError("journal contains a non-transaction target")
            paths.authorize(target)
            if not isinstance(change, dict) or set(change) != {"before", "after"} \
                    or any(value is not None and not isinstance(value, str) for value in change.values()) \
                    or change["after"] is None:
                raise ValueError("malformed file images")
            if rel in allowed and not change["after"].startswith(change["before"] or ""):
                raise ValueError("journal would truncate committed ledger bytes")
        before = doc["before_marker"]
        if before is not None and (not isinstance(before, dict) or before.get("protocol") != PROTOCOL):
            raise ValueError("legacy marker cannot be an undo baseline")
        expected = dict((before or {}).get("files", {}))
        for rel, change in files.items():
            if expected.get(rel) != _hash_text(change["before"]):
                raise ValueError("undo image is not bound to the previous commit")
            expected[rel] = _hash_text(change["after"])
        if doc["after_marker"]["files"] != expected \
                or doc["after_marker"]["generation"] != (before or {}).get("generation", 0) + 1:
            raise ValueError("after marker does not cover these file images")
        after = doc["after_marker"]
        transactions = dict((before or {}).get("committed_transactions", {}))
        transactions[doc["request"]["txn_id"]] = doc["digest"]
        if after.get("protocol") != PROTOCOL or after.get("layout_digest") != doc["layout_digest"] \
                or after.get("committed_transactions") != transactions:
            raise ValueError("transaction continuity mismatch")
        records = doc["snapshot_records"]
        if not isinstance(records, dict) or any(rec.get("artifact_id") != aid for aid, rec in records.items()):
            raise ValueError("snapshot record identity mismatch")
        record_hashes = {paths.rel(paths.record(aid)): _hash_text(_json_text(rec)) for aid, rec in records.items()}
        expected_record_hashes = {rel: sha for rel, sha in after["files"].items()
                                  if os.path.dirname(layout.safe_path(paths.root, rel)) == paths.records}
        if record_hashes != expected_record_hashes:
            raise ValueError("historical snapshot is not bound to its committed record bytes")
        lifecycle_records = doc["snapshot_lifecycle_records"]
        lifecycle_hashes = {paths.rel(paths.lifecycle_record(aid)): _hash_text(_json_text(rec))
                            for aid, rec in lifecycle_records.items()}
        expected_lifecycle_hashes = {rel: sha for rel, sha in after["files"].items()
                                    if os.path.dirname(layout.safe_path(paths.root, rel)) == paths.lifecycle_records}
        if lifecycle_hashes != expected_lifecycle_hashes:
            raise ValueError("historical SC05 is not bound to its committed bytes")
        _validate_final_artifacts(records)
        _validate_lifecycle_records(records, lifecycle_records)
        _validate_transaction_provenance(paths, doc)
    except (ValueError, KeyError, TypeError, AttributeError, layout.LayoutViolation,
            WriteRejection, SecondWritePath, stamp.InvalidFacts, StopIteration) as exc:
        raise StoreError("UNCERTAIN_BATCH: unrecognized/corrupt transaction journal") from exc
    return doc


def _restore_text(path, text):
    if text is None:
        if os.path.lexists(path):
            os.unlink(path)
            _fsync_dir(os.path.dirname(path))
    else:
        atomic_write(path, text)


def _recover_locked(paths, *, repair):
    if not os.path.lexists(paths.pending):
        return _snapshot_locked(paths)
    doc = _load_transaction(paths, paths.pending)
    marker_text = _read_text(paths.commit_point)
    before_text = None if doc["before_marker"] is None else _json_text(doc["before_marker"])
    after_text = _json_text(doc["after_marker"])
    if marker_text not in (before_text, after_text):
        raise StoreError("UNCERTAIN_BATCH: commit point is neither recognized journal endpoint")
    complete = marker_text == after_text
    observed = _file_state(paths)
    untouched = {rel: sha for rel, sha in (doc["before_marker"] or {}).get("files", {}).items()
                 if rel not in doc["files"]}
    if {rel: sha for rel, sha in observed.items() if rel not in doc["files"]} != untouched:
        raise StoreError("UNCERTAIN_BATCH: untouched committed carriers changed; recovery refused")
    for rel, change in doc["files"].items():
        current = _read_bytes(layout.safe_path(paths.root, rel))
        before = None if change["before"] is None else change["before"].encode("utf-8")
        after = change["after"].encode("utf-8")
        recognized = current in (before, after)
        if rel in (paths.rel(paths.journal), paths.rel(paths.lifecycle_ledger)) and current is not None:
            recognized = current.startswith(before or b"") and after.startswith(current)
        if not recognized or (complete and current != after):
            raise StoreError("UNCERTAIN_BATCH: journal target contains unknown bytes; refusing recovery")
    if not repair:
        raise StoreError("RECOVERY_REQUIRED: recognized committed cleanup" if complete
                         else "RECOVERY_REQUIRED: recognized uncommitted batch")
    if not complete:
        for rel, change in doc["files"].items():
            target = layout.safe_path(paths.root, rel)
            paths.authorize(target)
            _restore_text(target, change["before"])
        # The old commit point is never replaced/truncated during rollback.
    # Validate the endpoint AND make its commit-point rename durable before discarding
    # the only recovery witness. Incomplete ledger UTF-8 has already been restored above.
    snapshot = _snapshot_locked(paths, allow_pending=True)
    _fsync_dir(os.path.dirname(paths.commit_point))
    os.unlink(paths.pending)
    _fsync_dir(paths.ledger_dir)
    return dict(snapshot, recovery="FINALIZED_COMMIT" if complete else "ROLLED_BACK")


def _append_image(path, change):
    if _read_text(path) != change["before"]:
        raise StoreError("ledger changed after transaction preflight")
    suffix = change["after"][len(change["before"] or ""):]
    flags = os.O_RDWR | os.O_APPEND | os.O_NOFOLLOW | os.O_NONBLOCK
    if change["before"] is None:
        flags |= os.O_CREAT | os.O_EXCL
    fd = os.open(path, flags, 0o600)
    with os.fdopen(fd, "r+b") as fh:
        info, named = os.fstat(fh.fileno()), os.stat(path, follow_symlinks=False)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 \
                or (info.st_dev, info.st_ino) != (named.st_dev, named.st_ino) \
                or fh.read() != (change["before"] or "").encode("utf-8"):
            raise StoreError("ledger inode/bytes changed before append")
        fh.write(suffix.encode("utf-8"))
        fh.flush()
        os.fsync(fh.fileno())
    _fsync_dir(os.path.dirname(path))


def _validate_transaction_provenance(paths, doc):
    """Reconstruct SC06 from hash-bound observed inputs, final records and exact SC07 rows."""
    aids = [item["artifact_id"] for item in doc["request"]["items"]]
    if len(set(aids)) != len(aids) or set(doc["provenance_records"]) != set(aids):
        raise ValueError("SC06 coverage differs from the committed batch")
    change = doc["files"][paths.rel(paths.lifecycle_ledger)]
    rows = [json.loads(line) for line in change["after"][len(change["before"] or ""):].splitlines() if line]
    if len(rows) != len(aids) or [row["entity_id"] for row in rows] != aids:
        raise ValueError("SC06 event order/coverage differs from the committed batch")
    start = (doc["before_marker"] or {}).get("kd-ledger-rows", 0) + 1
    if [row["seq"] for row in rows] != list(range(start, start + len(aids))):
        raise ValueError("SC06 event sequence is discontinuous")
    observations = doc["evidence_binding"]["observations"]
    for item, event in zip(doc["request"]["items"], rows):
        aid = item["artifact_id"]
        if event["op"] != item["op"] or event["content_hash"] != prov.content_hash(
                {key: value for key, value in event.items() if key != "content_hash"}):
            raise ValueError("SC06 event action/hash differs from the transaction")
        candidate = next(c for c in observations if c.get("artifact_id", c.get("candidate_id")) == aid)
        expected = stamp.provenance_record(doc["snapshot_records"][aid], candidate["evidence"], event)
        if doc["provenance_records"][aid] != expected:
            raise ValueError("SC06 differs from its observed inputs, run or allocated ledger row")


def _persist_batch(paths, snapshot, committed, lifecycle_records, events, provenance_records, request, evaluation_binding, evidence_binding,
                   authentication, facts):
    import kd_validate as validator
    files = {paths.rel(paths.record(aid)): {"before": _read_text(paths.record(aid)), "after": _json_text(rec)}
             for aid, rec in committed.items()}
    files.update({paths.rel(paths.lifecycle_record(aid)): {"before": _read_text(paths.lifecycle_record(aid)),
                                                         "after": _json_text(rec)}
                  for aid, rec in lifecycle_records.items()})
    previous = _read_text(paths.lifecycle_ledger)
    rows = events
    seq = _ledger_seq(paths)
    if [row["seq"] for row in rows] != list(range(seq + 1, seq + 1 + len(rows))) \
            or any(not validator.validate_artifact("lifecycle-event-ledger", row).get("valid") for row in rows):
        raise WriteRejection("SC07_INVALID: final allocated sequence changed")
    seq += len(rows)
    files[paths.rel(paths.lifecycle_ledger)] = {"before": previous,
                                               "after": (previous or "") + "".join(_json_text(row) for row in rows)}
    old_journal = _read_text(paths.journal)
    journal_rows = [{"path": rel, "actor": paths.writer, "op": "WRITE", "txn_id": request["txn_id"],
                     "content_hash": _hash_text(change["after"])} for rel, change in sorted(files.items())]
    files[paths.rel(paths.journal)] = {"before": old_journal,
                                      "after": (old_journal or "") + "".join(_json_text(row) for row in journal_rows)}
    for rel in files:
        paths.authorize(layout.safe_path(paths.root, rel))
    before_marker = snapshot["marker"]
    body = {"protocol": PROTOCOL, "root": paths.root, "layout_digest": g1.binding_digest(paths.manifest),
            "request": request, "evaluation_binding": evaluation_binding,
            "evidence_binding": evidence_binding, "authentication": authentication,
            "provenance_records": provenance_records,
            "before_marker": before_marker, "files": files,
            "snapshot_records": dict(snapshot["records"], **committed),
            "snapshot_lifecycle_records": dict(snapshot["lifecycle_records"], **lifecycle_records)}
    digest = g1.binding_digest(body)
    expected = dict((before_marker or {}).get("files", {}))
    expected.update({rel: _hash_text(change["after"]) for rel, change in files.items()})
    txns = dict((before_marker or {}).get("committed_transactions", {}))
    txns[request["txn_id"]] = digest
    marker = {"protocol": PROTOCOL, "txn_id": request["txn_id"], "batch_digest": digest,
              "layout_digest": body["layout_digest"], "generation": (before_marker or {}).get("generation", 0) + 1,
              "files": expected, "kd-ledger-rows": seq, "committed_transactions": txns,
              "at": facts.created_at}
    doc = dict(body, digest=digest, after_marker=marker)
    history = layout.safe_path(paths.root, paths.rel(paths.history) + "/" + request["txn_id"] + ".json")
    paths.authorize(history)
    existing = _read_text(history)
    if existing is not None and existing != _json_text(doc):
        raise WriteRejection("TRANSACTION_ID_REUSED: retained history pins a different batch")
    if existing is None:
        atomic_write(history, _json_text(doc))
    atomic_write(paths.pending, _json_text(doc))  # undo images durable BEFORE the first authority byte
    _load_transaction(paths, paths.pending)
    try:
        for aid in sorted(committed):
            atomic_write(paths.record(aid), files[paths.rel(paths.record(aid))]["after"])
            atomic_write(paths.lifecycle_record(aid), files[paths.rel(paths.lifecycle_record(aid))]["after"])
        _append_image(paths.lifecycle_ledger, files[paths.rel(paths.lifecycle_ledger)])
        _append_image(paths.journal, files[paths.rel(paths.journal)])
        if _file_state(paths) != marker["files"]:
            raise StoreError("file state differs before commit point")
        atomic_write(paths.commit_point, _json_text(marker))  # LAST authoritative write
    except (OSError, StoreError) as exc:
        # Rename may have happened before a failed directory fsync. Only a recognized old
        # marker may be rolled back; an after-marker is a possibly committed outcome.
        if _read_text(paths.commit_point) != _json_text(marker):
            try:
                _recover_locked(paths, repair=True)
            except (OSError, StoreError) as recovery_error:
                raise StoreError("RECOVERY_REQUIRED: interrupted batch retained; do not blindly retry") from recovery_error
        raise StoreError("COMMIT_OUTCOME_UNCERTAIN: inspect/recover before retry" if _read_text(paths.commit_point) == _json_text(marker)
                         else "ROLLED_BACK: no authoritative changes committed") from exc
    # Cleanup failure does not turn a committed batch into a falsely reported rollback.
    _snapshot_locked(paths, allow_pending=True)
    _fsync_dir(os.path.dirname(paths.commit_point))
    try:
        os.unlink(paths.pending)
        _fsync_dir(paths.ledger_dir)
    except OSError:
        return dict(_receipt(doc, replayed=False), cleanup_required=True)
    _snapshot_locked(paths)
    return _receipt(doc, replayed=False)


def _receipt(doc, *, replayed):
    marker = doc["after_marker"]
    return {"status": "COMMITTED", "exit_code": EXIT_OK, "txn_id": marker["txn_id"],
            "generation": marker["generation"], "batch_digest": doc["digest"],
            "snapshot_digest": _hash_text(_json_text(marker)), "replayed": replayed,
            "written": sorted(i["artifact_id"] for i in doc["request"]["items"]),
            "revisions": {i["artifact_id"]: doc["snapshot_records"][i["artifact_id"]]["revision"]
                          for i in doc["request"]["items"]},
            "ledger_rows": marker["kd-ledger-rows"]}


# --------------------------------------------------------------------- commit
def _require_loaded_module_origins() -> None:
    """Reject a mixed installation with cached kd_* dependencies from another tree.

    Python import caching can bypass sys.path insertion; auditing HERE proves
    nothing about a same-named module already loaded from elsewhere. These
    origin checks are in addition to scanning and hash-binding the disk tree.
    """
    # Verify the actual objects S12 uses, not only the mutable import cache.
    bound_modules = {
        "kd_gate": kd_gate, "kd_provenance": prov,
        "kd_provenance_stamp": stamp, "kd_refs_audit": refs,
        "kd_store_layout": layout, "kd_human_gate": g1,
    }
    for name, bound in bound_modules.items():
        if sys.modules.get(name) is not bound:
            raise WriteRejection("RUNTIME_MODULE_OBJECT_MISMATCH: " + name)
    for filename in EXPECTED_MODULES:
        name = filename[:-3]
        module = sys.modules.get(name)
        if module is None:
            continue
        expected_path = os.path.realpath(os.path.join(HERE, filename))
        actual_file = getattr(module, "__file__", None)
        if not isinstance(actual_file, str) or os.path.realpath(actual_file) != expected_path:
            raise WriteRejection("RUNTIME_MODULE_SOURCE_MISMATCH: " + name)
        spec = getattr(module, "__spec__", None)
        origin = getattr(spec, "origin", None)
        if origin and os.path.realpath(origin) != expected_path:
            raise WriteRejection("RUNTIME_MODULE_SOURCE_MISMATCH: " + name)


def _validate_final_artifacts(committed: dict) -> None:
    """RH-P0-04: validate every fully-assembled SC04 artifact BEFORE the first authoritative byte.

    This is CM-50 verify-before-persist on the unique write path. The system-owned fields have
    already been injected, so each record is now in its final persisted shape. If ANY record is not
    SC04-valid the whole batch is refused and NOTHING is written -- no record, no lifecycle-ledger
    append, no commit marker, no write journal -- because `commit()` returning success is NOT the
    same as the artifact being valid. S09 (kd_validate) owns schema resolution; this writer never
    forks the schema, it calls the one gate.
    """
    import kd_validate as s09           # noqa: WPS433  S09 owns the schema gate, resolved at call time
    for aid, record in committed.items():
        result = s09.validate_artifact("artifact", record)
        if not result.get("valid"):
            detail = "; ".join("%s@%s: %s" % (v.get("code"), v.get("path"), v.get("message"))
                               for v in result.get("violations", [])[:6])
            raise WriteRejection(
                f"{aid}: final artifact failed SC04 BEFORE the first authoritative write -- {detail} "
                "(RH-P0-04: SC04 failure must precede any durable byte; nothing was written)")


def commit_batch(store_dir: str, intents: list, *, evidence: list, facts: stamp.RuntimeFacts,
                 registry: refs.RootRegistry | None = None, human_approved: bool = False,
                 approval=None, adjudication=None, eval_verdict=None,
                 scripts_dir: str = HERE, candidates=None, policy=None,
                 approval_verifier=None, evaluation_proof=None, evaluation_verifier=None,
                 evidence_proof=None, evidence_verifier=None) -> dict:
    """Commit only a complete, host-authenticated batch under the single S12 file lock.

    The verifiers are trusted in-process host capabilities, NOT fields in an untrusted
    request. Consent, independent evaluation and measured source observations stay separate.
    Missing capabilities/policy refuse before store creation. No key or credential is created.
    `human_approved` is retained as an inert CLI compatibility input, not authorization.
    """
    # Validate the executable dependency boundary before even the first Schema
    # or policy call; those calls themselves consume cached kd_* modules.
    _require_loaded_module_origins()
    if not isinstance(intents, list) or not intents:
        raise WriteRejection("commit_batch called with no intents -- an empty batch is a "
                             "visible refusal, not a no-op success")
    if not isinstance(evidence, list):
        raise WriteRejection("evidence must be a list of input records")
    for intent in intents:
        _require_g1_intent_shape(intent)
    batch_ids = [i.get("artifact_id") for i in intents]
    if any(not isinstance(aid, str) or not aid for aid in batch_ids) \
            or len({aid.casefold() for aid in batch_ids}) != len(batch_ids):
        raise WriteRejection("batch artifact IDs must be nonempty and distinct")
    verify_adjudication(intents, adjudication)
    verify_eval_verdict(eval_verdict, intents)
    _policy_thresholds(policy, facts)
    if not isinstance(approval, dict):
        raise WriteRejection("AUTHORIZATION_BUNDLE_MISSING: G1 rows and host proof must share one bundle")
    normalized = _normalize_approval(approval)
    if normalized is None or len(normalized[0]) != len(intents):
        raise WriteRejection("G1_COVERAGE_MISMATCH: one approval row per intended artifact required")
    if not callable(approval_verifier) or not callable(evaluation_verifier) or not callable(evidence_verifier):
        raise WriteRejection("TRUSTED_HOST_CAPABILITIES_MISSING: approval/Eval/source-observation channel required")
    # Freeze caller-owned data once. A verifier receives copies, so it cannot change what
    # the durable phase writes by mutating the same Python dictionaries.
    try:
        frozen = json.loads(_json_text({"intents": intents, "evidence": evidence, "approval": approval,
                                        "adjudication": adjudication, "eval": eval_verdict,
                                        "candidates": candidates, "policy": policy,
                                        "evaluation_proof": evaluation_proof, "evidence_proof": evidence_proof}))
    except (TypeError, ValueError) as exc:
        raise WriteRejection("batch inputs must be finite JSON") from exc
    intents, evidence, approval = frozen["intents"], frozen["evidence"], frozen["approval"]
    adjudication, eval_verdict = frozen["adjudication"], frozen["eval"]
    candidates, policy, evaluation_proof = frozen["candidates"], frozen["policy"], frozen["evaluation_proof"]
    evidence_proof = frozen["evidence_proof"]
    facts = stamp.RuntimeFacts(**facts.generation(), actor=facts.actor)
    paths = resolve_paths(store_dir)
    registry = registry or refs.RootRegistry([])
    registry = refs.RootRegistry([name + "=" + path for name, path in registry.roots.items()])
    _require_protocol_layout(paths)

    # The caller may supply an *additional* tree for migration/test inspection,
    # but must never substitute it for this process's executable dependencies.
    audited_roots = [HERE]
    if os.path.realpath(scripts_dir) != os.path.realpath(HERE):
        audited_roots.append(scripts_dir)
    for audited_root in audited_roots:
        audit = audit_bypass(audited_root)
        if audit["second_write_path"] or audit["status"] != "GREEN":
            # An incomplete scan cannot authenticate source code either.
            raise SecondWritePath("second write path present, batch refused: " +
                                  json.dumps({"status": audit["status"],
                                              "violations": audit["violations"],
                                              "missing_expected_modules":
                                                  audit["missing_expected_modules"]},
                                             ensure_ascii=False))

    rows, txn_id = _normalize_approval(approval)
    input_digest = _input_digest(intents, evidence, facts, approval, adjudication, eval_verdict, candidates, policy)

    def authenticate(request, eval_binding, evidence_binding):
        try:
            human = g1.verify_host_approval(approval.get("authorization"), request, approval_verifier)
            runner = g1.verify_host_evaluation(evaluation_proof, eval_binding, evaluation_verifier)
        except g1.GateRefusal as exc:
            raise WriteRejection(f"{exc.code}: {exc.message}") from exc
        if any(runner["runner_id"] in ids for ids in human["approvers"].values()):
            raise WriteRejection("EVAL_NOT_INDEPENDENT: runner and human approval identities overlap")
        observed = _verify_observations(evidence_proof, evidence_binding, evidence_verifier)
        return {"approval": human, "evaluation": runner, "observations": observed}

    def replay(snapshot):
        digest = (snapshot["marker"] or {}).get("committed_transactions", {}).get(txn_id)
        if digest is None:
            return None
        history_path = layout.safe_path(paths.root, paths.rel(paths.history) + "/" + txn_id + ".json")
        doc = _load_transaction(paths, history_path)
        if doc["digest"] != digest or doc["request"]["input_digest"] != input_digest:
            raise WriteRejection("TRANSACTION_ID_REUSED: committed transaction pins different inputs")
        if doc["request"]["sources"] != _source_bindings(intents, registry) \
                or doc["request"]["compiler_digest"] != _compiler_digest():
            raise WriteRejection("REPLAY_INPUTS_CHANGED: source/compiler bytes differ from the committed batch")
        if doc["evidence_binding"] != _evidence_binding(doc["request"], evidence, candidates):
            raise WriteRejection("REPLAY_OBSERVATIONS_CHANGED")
        authenticate(doc["request"], doc["evaluation_binding"], doc["evidence_binding"])
        return _receipt(doc, replayed=True)

    snapshot = read_snapshot(paths.root)
    replayed = replay(snapshot)
    if replayed is not None:
        return replayed
    committed, lifecycle_records, events, provenance_records = _assemble(paths, snapshot, intents, evidence, facts, registry, approval,
                                  adjudication, eval_verdict, candidates, policy)
    request = _request(paths, snapshot, intents, evidence, facts, registry, approval, adjudication,
                       eval_verdict, candidates, policy)
    eval_binding = _eval_binding(request, eval_verdict)
    evidence_binding = _evidence_binding(request, evidence, candidates)
    authenticate(request, eval_binding, evidence_binding)  # all refusals precede even bootstrap metadata
    if not os.path.lexists(os.path.join(paths.root, layout.MANIFEST_NAME)):
        layout.assert_staging_path(paths.root)
    with _store_lock(paths, exclusive=True, create=True):
        bound = resolve_paths(paths.root, bootstrap=True)
        if g1.binding_digest(bound.manifest) != request["layout_digest"]:
            raise WriteRejection("LAYOUT_CHANGED_AFTER_APPROVAL")
        current = _snapshot_locked(bound)
        replayed = replay(current)
        if replayed is not None:
            return replayed
        if current["snapshot_digest"] != request["base_snapshot"]:
            raise WriteRejection("STALE_SNAPSHOT: store changed after approval; no re-signing on retry")
        committed, lifecycle_records, events, provenance_records = _assemble(bound, current, intents, evidence, facts, registry, approval,
                                      adjudication, eval_verdict, candidates, policy)
        if _request(bound, current, intents, evidence, facts, registry, approval, adjudication,
                    eval_verdict, candidates, policy) != request:
            raise WriteRejection("INPUT_CHANGED_AFTER_APPROVAL")
        authentication = authenticate(request, eval_binding, evidence_binding)
        return _persist_batch(bound, current, committed, lifecycle_records, events, provenance_records, request, eval_binding, evidence_binding,
                              authentication, facts)



def _reason_for(op: str):
    """`reason` is a closed enum per 05 §4 M1: {decay-sweep, archive, absorbed, reactivated,
    tombstone}. Actions without an adjudicated reason are written as
    null rather than being handed a plausible-sounding one.

    # IMPLEMENTATION_GAP: Round 2 closed the reason enum only for the archive/merge/decay
    # family; ADD / UPDATE / SUPERSEDE / REINFORCE have no adjudicated reason value, and
    # RESTORE maps the existing "reactivated" reason under the 2026-10-07 extension.
    # Other unmapped actions keep null instead of inventing a value.
    # No entry in .distill/round-3/DEFERRED-PARAMETERS.yaml covers this; it is a newly
    # surfaced gap, registered in W1-C-REPORT.md rather than decided here.
    """
    return {"DECAY": "decay-sweep", "ARCHIVE": "archive", "MERGE": "absorbed", "RESTORE": "reactivated"}.get(op)


# --------------------------------------------------------------------- recovery report
def recover(store_dir: str, *, repair: bool = False) -> dict:
    """Read-only by default. Explicit repair only rolls back a recognized interrupted batch.

    Unknown bytes, legacy markers and undeclared protocol carriers are NEVER rewritten.
    A committed transaction is finalized, not rolled back. Repeating recovery is idempotent.
    """
    try:
        paths = resolve_paths(store_dir)
        if not (paths.pending and os.path.lexists(paths.pending)):
            snapshot = read_snapshot(store_dir)
        else:
            with _store_lock(paths, exclusive=repair):
                snapshot = _recover_locked(paths, repair=repair)
    except (StoreError, WriteRejection, SecondWritePath, OSError, ValueError) as exc:
        return {"store": os.path.realpath(store_dir),
                "state": "RECOVERY_REQUIRED" if str(exc).startswith("RECOVERY_REQUIRED") else "UNCERTAIN_BATCH",
                "transaction_verified": False, "repaired": False,
                "note": str(exc), "records": [], "ledger_rows": None, "commit_point_rows": None}
    marker = snapshot["marker"] or {}
    return {"store": paths.root, "state": snapshot["state"], "records": sorted(snapshot["records"]),
            "ledger_rows": marker.get("kd-ledger-rows", 0),
            "commit_point_rows": marker.get("kd-ledger-rows"),
            "transaction_verified": snapshot["state"] == "COMMITTED",
            "repaired": "recovery" in snapshot, "recovery": snapshot.get("recovery"),
            "snapshot_digest": snapshot["snapshot_digest"], "generation": marker.get("generation", 0)}


# --------------------------------------------------------------------- CLI
def _load(path: str):
    if path == "-":
        return json.load(sys.stdin)
    with open(path, encoding="utf-8") as fh:               # read-only
        return json.load(fh)



class UsageError(Exception):
    """A CLI usage error. argparse exits with code 2 by design, and 2 is a contract code in
    this package (second write path / self-declared provenance / unresolved ref), so usage
    errors must never be able to impersonate one."""


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        print(f"invalid input: {message}", file=sys.stderr)
        raise UsageError(message)

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    ap = ArgumentParser(
        prog="kd_write_txn.py",
        description="S12: host-authenticated file transactions, read-only recovery inspection "
                    "and the mechanical second-write-path audit. CLI JSON alone cannot authenticate consent.")
    ap.add_argument("--audit", action="store_true",
                    help="run the bypass audit over the scripts dir and exit "
                         "(0 green / 2 second write path / 4 scanned set incomplete)")
    ap.add_argument("--scripts-dir", default=HERE)
    ap.add_argument("--recover", metavar="STORE", help="inspect a hash-bound committed snapshot / interrupted batch")
    ap.add_argument("--repair", action="store_true", help="with --recover only: restore recognized uncommitted bytes")
    ap.add_argument("--store", metavar="DIR", help="store root for --commit")
    ap.add_argument("--batch", metavar="FILE or -", help="JSON list of intents")
    ap.add_argument("--prepare", action="store_true", help="print read-only host approval/Eval/observation bindings; does not commit")
    ap.add_argument("--candidates", metavar="FILE", help="complete S10 candidate input(s) for deterministic replay")
    ap.add_argument("--policy", metavar="FILE", help="explicit runtime-reviewed policy, not provisional defaults")
    ap.add_argument("--evidence", metavar="FILE or -", help="evidence set re-run through kd_gate")
    ap.add_argument("--root", action="append", default=[], metavar="NAME=PATH",
                    help="evidence root registry handed to S14 (repeatable)")
    ap.add_argument("--human-approved", action="store_true",
                    help="no longer trusted as sole evidence: S12 verifies a real G1 approval row "
                         "(--approval); a gated write carrying only this flag is refused (§9.1)")
    ap.add_argument("--approval", metavar="FILE or -",
                    help="G1 approval bundle/rows JSON (record_batch_approval / approve_and_apply "
                         "output); the commit API also requires trusted approval/Eval/observation verifiers")
    ap.add_argument("--eval-verdict", metavar="FILE or -",
                    help="complete S16 SC09 score document; a verdict that is not "
                         "PASSED+verified blocks the whole batch (CM-50 verify-before-persist)")
    ap.add_argument("--adjudication", metavar="FILE or -", help="complete per-item S10 SC12 verdict(s)")
    for flag in ("--round-id", "--pass-id", "--compiler-version", "--config-sha", "--actor",
                 "--created-at"):
        ap.add_argument(flag)
    ap.add_argument("--model-id", default=None)
    try:
        args = ap.parse_args(argv)
    except UsageError:
        return EXIT_WRITE_REJECTED

    if args.audit:
        report = audit_bypass(args.scripts_dir)
        print(json.dumps(report, ensure_ascii=False, indent=1))
        return audit_exit_code(report["status"])
    if args.recover:
        report = recover(args.recover, repair=args.repair)
        print(json.dumps(report, ensure_ascii=False, indent=1))
        return EXIT_STORE_ERROR if report["state"] in ("UNCERTAIN_BATCH", "RECOVERY_REQUIRED") else EXIT_OK
    if args.repair:
        print("invalid input: --repair requires --recover", file=sys.stderr)
        return EXIT_WRITE_REJECTED
    if not args.store or not args.batch:
        ap.print_usage(sys.stderr)
        print("invalid input: a commit needs --store and --batch (or use --audit/--recover)",
              file=sys.stderr)
        return EXIT_WRITE_REJECTED
    try:
        intents = _load(args.batch)
        evidence = _load(args.evidence) if args.evidence else []
        approval = _load(args.approval) if args.approval else None
        eval_verdict = _load(args.eval_verdict) if args.eval_verdict else None
        adjudication = _load(args.adjudication) if args.adjudication else None
        candidates = _load(args.candidates) if args.candidates else None
        policy = kd_gate.read_runtime_policy(args.policy) if args.policy else None
        if isinstance(intents, dict):
            intents = intents.get("intents", [])
        elif not isinstance(intents, list):
            raise ValueError("batch must be an intent list or an object with intents")
        facts = stamp.RuntimeFacts(round_id=args.round_id, pass_id=args.pass_id,
                                   compiler_version=args.compiler_version,
                                   config_sha=args.config_sha, actor=args.actor,
                                   model_id=args.model_id, created_at=args.created_at)
    except (OSError, ValueError, stamp.InvalidFacts, prov.SchemaError) as exc:
        print(f"invalid input: {exc}", file=sys.stderr)
        return EXIT_WRITE_REJECTED

    try:
        if args.prepare:
            request = prepare_commit(args.store, intents, evidence=evidence, facts=facts,
                                     registry=refs.RootRegistry(args.root), approval=approval,
                                     adjudication=adjudication, eval_verdict=eval_verdict,
                                     candidates=candidates, policy=policy)
            print(json.dumps(request, ensure_ascii=False, indent=1))
            return EXIT_OK
        receipt = commit_batch(args.store, intents, evidence=evidence, facts=facts,
                               registry=refs.RootRegistry(args.root),
                               human_approved=args.human_approved, approval=approval,
                               adjudication=adjudication, eval_verdict=eval_verdict, scripts_dir=args.scripts_dir,
                               candidates=candidates, policy=policy)
    except SecondWritePath as exc:
        print(f"SECOND_WRITE_PATH: {exc}", file=sys.stderr)
        return EXIT_SECOND_WRITE_PATH
    except WriteRejection as exc:
        print(f"WRITE_REJECTED: {exc}", file=sys.stderr)
        return EXIT_WRITE_REJECTED
    except (StoreError, OSError) as exc:
        print(f"STORE_ERROR: {exc}", file=sys.stderr)
        return EXIT_STORE_ERROR
    print(json.dumps(receipt, ensure_ascii=False, indent=1))
    return receipt["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
