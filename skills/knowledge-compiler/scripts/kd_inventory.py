#!/usr/bin/env python3
"""S02 kd_inventory -- bounded, enumerable input inventory with a digest.

Contract (12-SKILL-DESIGN-BRIEF.md line 43 / w1a.json S02):
  inputs  : working root + previous round's input digest
  outputs : a bounded, enumerable `inventory.json` (with digest)
  exit    : 2 = the input set is not enumerable or is unbounded
  clusters: CM-04 evidence-inventory-and-ingest (MUST)

Stdlib only. Reuses the frozen Wave 0 kernel for canonical hashing; never re-implements it.
`repos/` is never enumerated (task-level read prohibition, and it is a foreign corpus, not ours).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import kd_provenance as prov  # reuse only -- NEVER edit the kernel
import kd_store_layout as layout

EXIT_OK = 0
EXIT_UNENUMERABLE = 2

INVENTORY_SCHEMA = "kd-inventory/1"

# repos/ is excluded unconditionally and un-configurably (hard constraint + CM-09 hygiene).
NEVER_ENUMERATE = ("repos",)

# IMPLEMENTATION_GAP: the ceiling that makes an input set "bounded" is not decided in Round 2.
#   04 §3 row 17 (line 63) adjudicates the *mechanism* (spool 不丢 / 硬编码模式 / 长度锚定) and
#   `12` line 19 (CM-64) adjudicates "审计产物一律带上界", but no number is fixed for the
#   evidence inventory window. DEFERRED id DD-6-sub42 (the only round-1 size-threshold item:
#   "若 05 的体积阈值被写成可执行断言…") -- left deferred. This value is a conservative
#   operational cap that *fails loudly* (exit 2) rather than truncating; it is not a policy
#   threshold and must not be cited as one.
MAX_ENTRIES_DEFAULT = 5000

# IMPLEMENTATION_GAP: per-file byte ceiling for hashing is likewise undecided (same DEFERRED id
#   DD-6-sub42). Oversized files are reported, not silently skipped: they are listed in
#   `skipped` and still contribute their path+size to the digest.
MAX_HASH_BYTES_DEFAULT = 4 * 1024 * 1024


def sha256_file(path: str, cap: int) -> tuple:
    """Return (hex_digest_or_None, size, truncated_flag). Deterministic; no mtime involved."""
    size = os.path.getsize(path)
    if size > cap:
        return None, size, True
    digest = hashlib.sha256()
    remaining = cap
    truncated = False
    with open(path, "rb") as fh:
        while True:
            block = fh.read(65536)
            if not block:
                break
            if remaining <= 0:
                truncated = True
                break
            chunk = block[:remaining]
            digest.update(chunk)
            remaining -= len(chunk)
            if len(block) > len(chunk):
                truncated = True
    if truncated:
        return None, size, True
    return digest.hexdigest(), size, False


def build_inventory(root: str, max_entries: int, max_hash_bytes: int, extra_excludes):
    """Walk `root` and return (entries, failures, meta). Raises InventoryError when the set is
    not enumerable or not bounded -- the caller maps that to exit 2 (never a silent truncate)."""
    excludes = set(NEVER_ENUMERATE) | set(extra_excludes)
    entries, skipped = [], []
    root_abs = os.path.realpath(root)
    if not os.path.isdir(root_abs) or "repos" in root_abs.split(os.sep):
        raise InventoryError("input root is missing or inside the excluded corpus")
    if type(max_entries) is not int or max_entries < 1 or type(max_hash_bytes) is not int or max_hash_bytes < 1:
        raise InventoryError("inventory bounds must be positive integers")
    def unreadable(error):
        raise InventoryError("input tree cannot be fully enumerated") from error

    for dirpath, dirnames, filenames in os.walk(root_abs, followlinks=False, onerror=unreadable):
        # Sort for determinism: os.walk order is filesystem-dependent.
        dirnames.sort()
        filenames.sort()
        rel_dir = os.path.relpath(dirpath, root_abs).replace(os.sep, "/")
        prune = []
        for name in dirnames:
            if name in excludes or name == ".git" or name == "__pycache__":
                prune.append(name)
                continue
            full = os.path.join(dirpath, name)
            if os.path.islink(full):
                # A symlinked directory makes the walk's closure unbounded by our own policy
                # (we never follow links), so the input set is not enumerable -> fail loudly.
                raise InventoryError(
                    "symlinked directory inside input set (unbounded without a link policy): "
                    + os.path.join(rel_dir, name))
        dirnames[:] = [d for d in dirnames if d not in prune]
        for name in prune:
            skipped.append({"path": _rel(rel_dir, name), "reason": "excluded_root"})

        for name in filenames:
            full = os.path.join(dirpath, name)
            rel = _rel(rel_dir, name)
            if os.path.islink(full):
                skipped.append({"path": rel, "reason": "symlink_not_followed"})
                continue
            if not os.path.isfile(full):
                skipped.append({"path": rel, "reason": "not_a_regular_file"})
                continue
            if len(entries) >= max_entries:
                raise InventoryError(
                    "input set exceeds the bounded window (max_entries=%d) -- refusing to "
                    "truncate silently (CM-01 visible failure, 12 line 551)" % max_entries)
            try:
                sha, size, trunc = sha256_file(full, max_hash_bytes)
            except OSError as exc:
                raise InventoryError("unreadable entry, set not enumerable: %s (%s)" % (rel, exc))
            if trunc:
                skipped.append({"path": rel, "reason": "over_size_cap_no_hash"})
                entries.append({"path": rel, "size": size, "sha256": None})
            else:
                entries.append({"path": rel, "size": size, "sha256": sha})
    entries.sort(key=lambda e: e["path"])
    return entries, skipped, {"root": root_abs, "excluded_roots": sorted(excludes)}


def _rel(reldir: str, name: str) -> str:
    return name if reldir == "." else "%s/%s" % (reldir, name)


class InventoryError(Exception):
    """Input set is not enumerable or not bounded -> exit 2."""


def inventory_digest(entries) -> str:
    """Digest over canonical bytes of the entry list only. Timestamps are deliberately outside
    the digest so `unchanged` is a real comparison and not a wall-clock artifact."""
    return hashlib.sha256(prov.canonical_bytes(entries)).hexdigest()


def load_prev_digest(path: str):
    if not path:
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
    except (OSError, ValueError) as exc:
        raise InventoryError("previous input digest unreadable/malformed: %s (%s)" % (path, exc))
    if isinstance(doc, dict):
        return doc.get("digest")
    if isinstance(doc, str):
        return doc.strip()
    raise InventoryError("previous input digest has no digest field: %s" % path)


def atomic_write(path: str, text: str) -> None:
    layout.assert_staging_path(path)
    layout.assert_staging_path(path + ".tmp")
    if os.path.lexists(path + ".tmp"):
        raise InventoryError("refusing an existing temporary output")
    tmp = path + ".tmp"
    with open(tmp, "x", encoding="utf-8") as fh:  # KD-WRITE-EXEMPT: S02 inventory tmp -- half of the write-once rename; the artifact is rebuilt from --scan-root every round and is not the authoritative store
        fh.write(text)  # KD-WRITE-EXEMPT: derived S02 inventory body -- a listing keyed by content hash, regenerated each round, read by no counter or gate
        fh.flush()
        os.fsync(fh.fileno())  # KD-WRITE-EXEMPT: durability of the derived S02 tmp only; a fsynced projection stays a projection (CM-13)
    os.replace(tmp, path)  # KD-WRITE-EXEMPT: rename publishes the derived S02 artifact into the CLI-chosen --out-dir, never into the store, so S12 remains the unique writer


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="kd_inventory.py",
        description="S02: emit a bounded, enumerable inventory.json with an input digest.")
    parser.add_argument("--root", default=".", help="working root to enumerate")
    parser.add_argument("--out", required=True,
                        help="path of inventory.json to write")
    parser.add_argument("--prev-digest", default=None,
                        help="previous round's inventory.json (or a bare digest file) -- input digest gate")
    parser.add_argument("--max-entries", type=int, default=MAX_ENTRIES_DEFAULT)
    parser.add_argument("--max-hash-bytes", type=int, default=MAX_HASH_BYTES_DEFAULT)
    parser.add_argument("--exclude", action="append", default=[],
                        help="additional directory name to prune (repeatable). repos/ cannot be excluded "
                             "because it is pruned unconditionally.")
    args = parser.parse_args(argv)

    if os.path.basename(os.path.normpath(args.root)) in set(NEVER_ENUMERATE):
        print("S02 REFUSING: repos/ may never be enumerated as an input root", file=sys.stderr)
        return EXIT_UNENUMERABLE
    if not os.path.isdir(args.root):
        print("S02 exit 2: working root is not a directory: %s" % args.root, file=sys.stderr)
        return EXIT_UNENUMERABLE

    try:
        entries, skipped, meta = build_inventory(
            args.root, args.max_entries, args.max_hash_bytes, args.exclude)
        prev = load_prev_digest(args.prev_digest)
    except InventoryError as exc:
        print("S02 exit 2 (input set not enumerable or unbounded): %s" % exc, file=sys.stderr)
        return EXIT_UNENUMERABLE

    digest = inventory_digest(entries)
    doc = {
        "schema": INVENTORY_SCHEMA,
        "root": meta["root"],
        "excluded_roots": meta["excluded_roots"],
        "entry_count": len(entries),
        "max_entries": args.max_entries,
        "bounded": True,
        "digest": digest,
        "previous_input_digest": prev,
        # `unchanged` is a fact about two digests, not a decision. The expiry gate that would
        # zero model calls on unchanged input belongs to S17/S18 (`12` line 685, 步 15/21),
        # so nothing downstream is assumed here.
        "input_unchanged": (prev == digest and all(e["sha256"] is not None for e in entries)) if prev else False,
        "entries": entries,
        "skipped": skipped,
    }
    out_dir = os.path.dirname(os.path.abspath(args.out))
    try:
        layout.assert_staging_path(args.out)
        os.makedirs(out_dir, exist_ok=True)  # KD-WRITE-EXEMPT: explicit staging output only
        atomic_write(args.out, json.dumps(doc, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    except (OSError, InventoryError, layout.LayoutViolation) as exc:
        print(f"S02 output refused: {exc}", file=sys.stderr)
        return EXIT_UNENUMERABLE
    print("S02 ok: %d entries, digest=%s, unchanged=%s"
          % (len(entries), digest[:12], doc["input_unchanged"]))
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
