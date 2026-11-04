#!/usr/bin/env python3
"""Read-only fingerprint and drift check for one completed round's output tree.

This is an integrity aid, not an immutable storage system, authorization token or
proof that a human actually approved the contents.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat

SHA256 = re.compile(r"^[0-9a-f]{64}$")


class SnapshotError(Exception):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _identity(st):
    return (st.st_dev, st.st_ino, st.st_mode & stat.S_IFMT(st.st_mode))


def _unchanged_file(before, after):
    return _identity(before) == _identity(after) and (
        before.st_size, before.st_mtime_ns, before.st_ctime_ns) == (
        after.st_size, after.st_mtime_ns, after.st_ctime_ns)


def fingerprint(root: Path) -> dict:
    """Fingerprint a stable tree via no-follow directory/file descriptors.

    Reject replacement or mutation observed while scanning. Filesystem snapshots
    are not atomic: callers still need a quiescent workspace or trusted snapshot.
    """
    try:
        root_stat = root.lstat()
    except OSError as exc:
        raise SnapshotError("OUTPUT_ROOT_UNREADABLE") from exc
    if not stat.S_ISDIR(root_stat.st_mode):
        raise SnapshotError("OUTPUT_ROOT_NOT_DIRECTORY")

    records = []
    flags_dir = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    try:
        top_fd = os.open(root, flags_dir)  # KD-WRITE-EXEMPT: read-only nofollow root descriptor; never writes store or files
        try:
            if _identity(os.fstat(top_fd)) != _identity(root_stat):
                raise SnapshotError("OUTPUT_CHANGED_DURING_SCAN")

            def walk(dir_fd, prefix):
                before_dir = os.fstat(dir_fd)
                names = os.listdir(dir_fd)
                if len(names) != len(set(names)):
                    raise SnapshotError("OUTPUT_PATH_NOT_CANONICAL")
                for name in names:
                    if not name or any(c in name for c in ("\t", "\r", "\n")):
                        raise SnapshotError("OUTPUT_PATH_NOT_CANONICAL")
                    name.encode("utf-8", "strict")
                    rel = prefix + name
                    before = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
                    if stat.S_ISLNK(before.st_mode):
                        raise SnapshotError("OUTPUT_SYMLINK_REFUSED")
                    if stat.S_ISDIR(before.st_mode):
                        child_fd = os.open(name, flags_dir, dir_fd=dir_fd)  # KD-WRITE-EXEMPT: read-only child descriptor
                        try:
                            if _identity(os.fstat(child_fd)) != _identity(before):
                                raise SnapshotError("OUTPUT_CHANGED_DURING_SCAN")
                            walk(child_fd, rel + "/")
                            after = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
                            if not _unchanged_file(before, after):
                                raise SnapshotError("OUTPUT_CHANGED_DURING_SCAN")
                        finally:
                            os.close(child_fd)
                    elif stat.S_ISREG(before.st_mode):
                        if before.st_nlink != 1:
                            raise SnapshotError("OUTPUT_HARDLINK_REFUSED")
                        fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,  # KD-WRITE-EXEMPT: read-only regular file descriptor
                                     dir_fd=dir_fd)
                        try:
                            if not _unchanged_file(before, os.fstat(fd)):
                                raise SnapshotError("OUTPUT_CHANGED_DURING_SCAN")
                            digest = hashlib.sha256()
                            while True:
                                chunk = os.read(fd, 1024 * 1024)
                                if not chunk:
                                    break
                                digest.update(chunk)
                            after_fd = os.fstat(fd)
                            after_path = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
                            if not _unchanged_file(before, after_fd) or (
                                    not _unchanged_file(before, after_path)):
                                raise SnapshotError("OUTPUT_CHANGED_DURING_SCAN")
                            records.append({"path": rel, "sha256": digest.hexdigest()})
                        finally:
                            os.close(fd)
                    else:
                        raise SnapshotError("OUTPUT_SPECIAL_FILE_REFUSED")
                if set(os.listdir(dir_fd)) != set(names):
                    raise SnapshotError("OUTPUT_CHANGED_DURING_SCAN")
                after_dir = os.fstat(dir_fd)
                if not _unchanged_file(before_dir, after_dir):
                    raise SnapshotError("OUTPUT_CHANGED_DURING_SCAN")

            walk(top_fd, "")
            end_root = root.lstat()
            if not _identity(root_stat) == _identity(end_root):
                raise SnapshotError("OUTPUT_CHANGED_DURING_SCAN")
        finally:
            os.close(top_fd)
    except (OSError, UnicodeError) as exc:
        raise SnapshotError("OUTPUT_READ_FAILED") from exc
    if not records:
        raise SnapshotError("OUTPUT_EMPTY")
    records.sort(key=lambda entry: entry["path"].encode("utf-8"))
    raw = "".join(entry["path"] + "\t" + entry["sha256"] + "\n"
                  for entry in records).encode("utf-8")
    return {"files": records, "file_count": len(records),
            "tree_sha256": sha256(raw), "consistency": "STABLE_SCAN_NOT_ATOMIC"}



def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read-only fingerprint or verify a completed round output")
    parser.add_argument("--root", required=True, help="Round output/ directory")
    parser.add_argument("--expected", help="Expected lowercase tree SHA-256; mismatches fail")
    args = parser.parse_args(argv)
    if args.expected is not None and not SHA256.fullmatch(args.expected):
        print(json.dumps({"status": "FAIL", "error": "EXPECTED_DIGEST_INVALID"}))
        return 2
    try:
        result = fingerprint(Path(args.root))
    except SnapshotError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}))
        return 2
    match = args.expected is None or result["tree_sha256"] == args.expected
    print(json.dumps({"status": "PASS" if match else "FAIL",
                      "verified_against_expected": args.expected is not None,
                      **result}, ensure_ascii=False))
    return 0 if match else 2


if __name__ == "__main__":
    raise SystemExit(main())
