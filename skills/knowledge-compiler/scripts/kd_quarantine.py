#!/usr/bin/env python3
"""S11 kd_quarantine -- Stage 2's INERT candidate area (Round 3 Wave 2, contract S11).

Contract (`.distill/round-3/wave-2/_dispatch/w2c.json`, row S11; `12-SKILL-DESIGN-BRIEF.md:119`)
    inputs   : Stage 2 候选文件
    outputs  : 惰性候选区读写（**不在宿主 skills 根**）+ `pending_count`
    exit     : 0；`pending_count<=0` 时 hint 必须为空串
    clusters : CM-32 (inert-candidate-quarantine, CORE, stage=promotion-gate)
    schemas  : SC08 `candidate-quarantine.schema.json` <- `06` §4, writer S11, validators S09/S10

Round 2 basis, `06-PROMOTION-POLICY.md` §4. The five implementation requirements are quoted at
`06:177` (`15` 的五要素: pending storage + artifact hash + 冲突拒绝 + approve/apply 同事务 +
Rejected 与 Failed 分离记账) and the section says verbatim that dropping any one of them
degenerates C into B or A -- a 假门. Node-by-node mapping (each one is a code path below, and
each one has a test that fails when the path is removed):

  (1) pending storage   -- `06:180` N19: 写候选文件到 inert store `_pending/<id>.md`
                           (`stage_candidate`, PENDING_DIR).
  (2) artifact hash     -- `06:180` N19: `+ sha256 + artifact hash`; `06:185-186`: a hand-edit
                           that breaks the digest must fail closed and be refused at apply, and
                           must write a failed row. Two digests are recorded: the raw byte digest
                           and a digest over the canonical artifact triple (`verify_candidate`).
  (3) conflict refusal  -- `06:187` N20: 同 target 已有 pending → 拒绝新建, and `06:189`: the
                           known side effect (blocking a legitimate follow-up correction) is
                           handled by recording `suppressed_by_pending`, NOT by overwriting.
  (4) approve/apply in
      one transaction   -- `06:177` element 4, spelled out at `06:247` N27: 任一步失败则整批不落.
                           Mechanically here: `apply_bundle` is a PURE function that emits one
                           bundle keyed by one transaction id and writes nothing; a refused or
                           absent approval therefore cannot leave a half-record behind, because
                           quarantine holds no approve state of its own at all.
  (5) Rejected and Failed
      kept apart        -- `06:195-200` N22: two separate append-only carriers (REJECTED_REL /
                           FAILED_REL), 被拒留痕 (反沉默); `06:200`: rejected is a human decision
                           and 无新证据不得再提, failed is retryable. `06:193` additionally
                           requires that a later failure never overwrite a more informative
                           earlier sample -- hence append + `at` + `seq`, never a rewrite.

Also in §4 and implemented here, though not one of the five: `06:190-194` N21 (幂等与水位:
per-item replay watermark + an expiry channel, so the queue cannot accumulate without bound)
and `06:202-204` N22b (the only model intervention point: draft + suggested tier + size, with
P-1 no write rights -- quarantine holds these as *reported* fields and never lets them decide).

WHY THIS AREA IS INERT AND HOW THAT IS MECHANICAL
  * It cannot be loaded. A host reads skills/rules out of a skills-shaped root; a candidate that
    lands there stops being inert and becomes an active instruction. Every entry point funnels
    through `check_placement`, which REFUSES a target inside a host-loaded surface
    (`SKILLS_ROOT_TARGET`), inside a declared store (`STORE_ROOT_TARGET`), inside the read-only
    corpus (`CORPUS_ROOT_TARGET`) or inside a frozen round (`FROZEN_ROUND_TARGET`). The check runs
    on the real, symlink-resolved path, so `../` and a symlink cannot dodge it.
  * It is not a second authority. Nothing here is registered with S08 (`kd_store_layout`), and
    `check_placement` refuses a root under any store layout, so the store's own stray-file and
    write-journal checks stay the referee. Quarantine state is recomputed from the filesystem on
    every call: `pending_count` is derived, never stored, and the SC08 report is a rendering --
    deleting it changes nothing about the count (05-DATA-MODEL.md:21 红线 1/2, CM-11/CM-13).
  * It is outside the single durable write path. This module never calls `kd_write_txn.commit_batch`
    and never authorises a store path; it reuses S12's `atomic_write` primitive and the Wave-0
    kernel's sanctioned `append_ledger` channel so that no second write mechanism exists in the
    package (12:721 item 1). `kd_write_txn --audit` therefore stays green with this module present.

Exit codes are the package-wide convention of `12-SKILL-DESIGN-BRIEF.md:97-103`, never a private
set: 0 success or legal empty result, 2 fail-closed (an unverifiable predicate: the tamper case
of `06:186`), 3 gate refusal (a deterministic non-promotion -- a conflict, a replay, a
no-new-evidence re-propose -- which is a normal terminal state and must never be retried into
green), 64 usage or schema error. argparse's built-in exit code 2 is overridden for exactly that
reason: a typo must not impersonate a fail-closed verdict.

python3 stdlib only; no pytest on this host.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import kd_provenance as prov      # noqa: E402  wave 0 kernel: canonical hash + append-only ledger
import kd_store_layout as layout  # noqa: E402  S08: who owns which store path
import kd_validate as validate    # noqa: E402  S09: the sole schema witness
import kd_write_txn as txn        # noqa: E402  S12: the package's atomic write primitive

# --------------------------------------------------------------------------- exit codes (12:97-103)
EXIT_OK = 0
EXIT_FAIL_CLOSED = 2
EXIT_GATE_REFUSAL = 3
EXIT_USAGE = 64

# --------------------------------------------------------------------------- the area's shape
SCHEMA_KIND = "candidate-quarantine"     # -> schemas/candidate-quarantine.schema.json (SC08)
QUARANTINE_VERSION = "1"
PENDING_DIR = "_pending"                 # literal of `06:180`
RECORDS_DIR = "_records"
LEDGER_DIR = "_ledger"
REJECTED_REL = LEDGER_DIR + "/rejected.jsonl"    # element 5, carrier A (`06:195`)
FAILED_REL = LEDGER_DIR + "/failed.jsonl"        # element 5, carrier B (`06:195`, `06:193`)
SUPPRESSED_REL = LEDGER_DIR + "/suppressed.jsonl"  # `06:189` suppressed_by_pending

#: the three kinds of quarantine-local ledger row. `rejected` and `failed` share no file, no
#: row shape and no decision: 06:200 makes the difference decisional.
FAILED_KINDS = ("sha256_mismatch", "artifact_hash_mismatch", "pending_file_missing",
                "unreadable_record", "apply_refused")
#: `06:200`: rejected = 人的决定. A model may propose a draft (N22b) but may not reject, so the
#: actor vocabulary of a rejection is closed to the human members of SC07's attribution enum
#: (05-DATA-MODEL.md §4 M1) rather than a free string.
HUMAN_DECISION_ACTORS = ("human", "user")
STATES = ("pending", "rejected", "failed", "consumed", "expired")

# --------------------------------------------------------------------------- `hint` (contract S11)
# The contract pins only the coupling, not the wording, and Round 2 nowhere adjudicates a string.
# `# IMPLEMENTATION_GAP: the exact hint wording for a non-empty Stage 2 queue is not decided in
# # round 2 (no DEFERRED-PARAMETERS.yaml entry covers it either); the plainest possible string is
# # emitted, with no emoji, no severity and no count, and the id is registered as a newly surfaced
# # gap in .distill/round-3/wave-2/W2-C-REPORT.md. / DEFERRED id none registered (newly surfaced)`
HINT_EMPTY = ""
HINT_PENDING = "candidate files are quarantined and awaiting the promotion gate"


def hint_for(pending_count: int) -> str:
    """THE only producer of a hint, and a pure function of the count.

    Contract: `pending_count<=0` 时 hint 必须为空串; the reverse branch is what stops the value
    being a decoration. Because the hint is always re-derived here and never read back from disk,
    a stale hint cannot survive an empty queue -- that is 05-DATA-MODEL.md §5.4's consumer-closure
    condition (3): 默认值/无值状态不得被渲染成真实数据.
    """
    return HINT_EMPTY if pending_count <= 0 else HINT_PENDING


# --------------------------------------------------------------------------- placement (inertness)
#: Directory names a host actually loads instructions from, taken from the corpora Round 1
#: catalogued (`02-FINAL-MECHANISMS.md:250` CM-32 anchors: memsearch `skills_root`, hermes-agent
#: `evolution/` quarantine OUTSIDE `skills/`) and from the harness surfaces those repos ship
#: (`skills/`, `optional-skills/`, `commands/`, `agents/`, `rules/`, `instructions/`, `hooks/`
#: under a dot-directory such as `.claude/`, `.codex/`, `.qoder/`). Being a superset of the
#: surfaces any single host reads is deliberate: a false refusal costs the operator one flag,
#: a false acceptance silently installs an instruction.
#:
#: `# IMPLEMENTATION_GAP: the exact membership of the host-loaded surface vocabulary is not
#: # adjudicated in round 2 -- CM-61 (multi-host projection) was downgraded to SUPPORTING, so no
#: # per-host table exists to copy. The list is conservative-superset, and the reason code names
#: # the segment that tripped it so an operator can see the refusal rather than guess.
#: # / DEFERRED id none registered (newly surfaced; recorded in W2-C-REPORT.md)`
HOST_LOADED_SEGMENTS = frozenset({
    "skills", "optional-skills", "commands", "agents", "rules", "instructions", "hooks",
    "prompts", ".claude", ".codex", ".qoder", ".qoder-cn", ".cursor", ".github",
})
#: the read-only evidence corpus (task-level red line: nothing here may be written), and the two
#: frozen rounds of `.distill/` which are tagged IMMUTABLE.
CORPUS_SEGMENT = "repos"
FROZEN_ROUND_SEGMENTS = frozenset({"round-1", "round-2", "round-3"})


class PlacementRefusal(Exception):
    """The requested quarantine root would be load-bearing. Carries the named reasons."""

    def __init__(self, report: dict):
        super().__init__("; ".join(report["details"]) or ",".join(report["reason_codes"]))
        self.report = report


class QuarantineRefusal(Exception):
    """A deterministic gate refusal (exit 3): conflict, replay or no-new-evidence."""

    def __init__(self, code: str, message: str, detail: dict = None):
        super().__init__(message)
        self.code, self.message, self.detail = code, message, (detail or {})


class FailClosed(Exception):
    """An unverifiable predicate (exit 2): the bytes disagree with the record, or the record is
    unreadable. Nothing durable may be written on top of it (06:185-186)."""


def _real(path: str) -> str:
    """Absolute + symlink-resolved: the placement check must not be dodgeable by `..` or by a
    link that points into a skills root."""
    return os.path.realpath(os.path.abspath(path))


def _segments(path: str) -> list:
    return [c for c in path.split(os.sep) if c]


def discover_store_anchors(path: str) -> list:
    """Every ancestor that S08 would call a store root (it is the one holding `store-layout.json`).
    Read-only, and the answer comes from S08's own manifest name, never from a copy of it here."""
    anchors, current = [], os.path.abspath(path)
    while True:
        if os.path.lexists(os.path.join(current, layout.MANIFEST_NAME)):
            anchors.append(os.path.realpath(current))
        parent = os.path.dirname(current)
        if parent == current:
            return anchors
        current = parent


def check_placement(root: str, extra_store_roots=()) -> dict:
    """The inertness gate. Returns a report; `ok` False means this module will not touch `root`.

    Reasons are NAMED so a refusal is actionable (a bare 'no' would be its own failure mode):
      SKILLS_ROOT_TARGET   a host would load it (`06:183-184`, contract "**不在宿主 skills 根**")
      STORE_ROOT_TARGET    it would sit inside S08's layout and read as a NON_OWNER_WRITE, i.e.
                           quarantine would have become a second authority (05 红线 1/2)
      CORPUS_ROOT_TARGET   the read-only evidence corpus
      FROZEN_ROUND_TARGET  `.distill/round-1` / `round-2` / `round-3`, tagged IMMUTABLE
    """
    resolved = _real(root)
    segs = _segments(resolved)
    codes, details, hits = [], [], sorted(s for s in segs if s in HOST_LOADED_SEGMENTS)
    if hits:
        codes.append("SKILLS_ROOT_TARGET")
        details.append(f"SKILLS_ROOT_TARGET: path segment(s) {hits} are a host-loaded "
                       "skills/rules surface, so a candidate placed here would be read by the "
                       "host and stop being inert")
    if CORPUS_SEGMENT in segs:
        codes.append("CORPUS_ROOT_TARGET")
        details.append(f"CORPUS_ROOT_TARGET: {resolved} is inside the read-only evidence corpus "
                       f"({CORPUS_SEGMENT}/)")
    for i, seg in enumerate(segs):
        if seg == ".distill" and i + 1 < len(segs) and segs[i + 1] in FROZEN_ROUND_SEGMENTS:
            codes.append("FROZEN_ROUND_TARGET")
            details.append(f"FROZEN_ROUND_TARGET: .distill/{segs[i + 1]} is frozen and immutable")
            break
    anchors = sorted(set(map(os.path.realpath, extra_store_roots)) | set(discover_store_anchors(resolved)))
    inside = [a for a in anchors if resolved == a or resolved.startswith(a + os.sep)]
    if inside:
        codes.append("STORE_ROOT_TARGET")
        details.append(f"STORE_ROOT_TARGET: {resolved} is inside the declared store root(s) "
                       f"{inside}; the store layout belongs to S08 and its writes to S12, so "
                       "quarantine bytes there would be a non-Owner landing instead of an inert "
                       "holding area")
    try:
        layout.assert_staging_path(resolved)
    except layout.LayoutViolation:
        if not codes:
            codes.append("PROTECTED_OUTPUT_TARGET")
            details.append("PROTECTED_OUTPUT_TARGET: quarantine cannot write into the package or a protected tree")
    return {
        "placement_check_ran": True,
        "requested_root": os.path.abspath(root),
        "resolved_root": resolved,
        "host_skills_root": bool(hits),
        "inside_store_root": bool(inside),
        "corpus_root": CORPUS_SEGMENT in segs,
        "frozen_round": "FROZEN_ROUND_TARGET" in codes,
        "reason_codes": codes,
        "details": details,
        "ok": not codes,
    }


# --------------------------------------------------------------------------- the area
_ID_BYTES = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-")


def _safe_id(candidate_id: str) -> str:
    cid = str(candidate_id or "")
    if not cid or cid[0] in "._-" or any(c not in _ID_BYTES for c in cid) or len(cid) > 64:
        raise QuarantineRefusal("BAD_CANDIDATE_ID",
                                f"candidate_id {candidate_id!r} is not a safe file name "
                                "(letters, digits, '.', '_', '-' only, max 64)")
    return cid


def _target_key(target: str) -> str:
    t = str(target or "").strip()
    if not t:
        raise QuarantineRefusal("BAD_TARGET", "a candidate must name the target it would become; "
                                             "conflict refusal is per-target (`06:187`)")
    return t


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _epoch(stamp):
    """Parse an ISO instant for the expiry channel only; an unparseable stamp is an explicit
    failure, never a silent 'not expired'."""
    if not stamp:
        return None
    try:
        instant = datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))
        if instant.tzinfo is None:
            raise ValueError("timestamp needs an explicit timezone")
        return instant
    except ValueError as exc:
        raise FailClosed(f"unreadable timestamp {stamp!r}: {exc}") from exc


class Quarantine:
    """One inert candidate area. Construction IS the placement gate: no instance exists for a
    root a host would load."""

    def __init__(self, root: str, store_roots=(), at: str = None):
        self.placement = check_placement(root, store_roots)
        if not self.placement["ok"]:
            raise PlacementRefusal(self.placement)
        self.root = self.placement["resolved_root"]
        self.at = at or _now_iso()

    # -- paths (relative to the area only; the store's paths come from S08, never from here)
    def at_path(self, rel: str) -> str:
        try:
            return layout.safe_path(self.root, rel)
        except layout.LayoutViolation as exc:
            raise QuarantineRefusal("UNSAFE_QUARANTINE_PATH", str(exc)) from exc

    def pending_path(self, cid: str) -> str:
        return self.at_path(f"{PENDING_DIR}/{_safe_id(cid)}.md")

    def record_path(self, cid: str) -> str:
        return self.at_path(f"{RECORDS_DIR}/{_safe_id(cid)}.json")

    # -- writes. Both go through an existing sanctioned durable channel, never a new mechanism:
    #    S12's atomic tmp+rename+fsync primitive, and the Wave-0 append-only ledger writer.
    def _write(self, path: str, text: str) -> None:
        txn.atomic_write(path, text)

    def _write_json(self, path: str, doc) -> None:
        txn.atomic_write(path, json.dumps(doc, ensure_ascii=False, sort_keys=True, indent=1) + "\n")

    def _append(self, rel: str, row: dict) -> None:
        prov.append_ledger(self.at_path(rel), row)

    # -- reads (derived on every call, never cached)
    def load_records(self) -> dict:
        out = {}
        directory = self.at_path(RECORDS_DIR)
        if not os.path.isdir(directory):
            return out
        for name in sorted(os.listdir(directory)):
            if not name.endswith(".json"):
                continue
            cid = name[:-5]
            try:
                with open(os.path.join(directory, name), encoding="utf-8") as fh:
                    doc = json.load(fh)
            except (OSError, ValueError) as exc:
                # an unreadable quarantine record is a visible failure: `06:186` fail-closed
                raise FailClosed(f"quarantine record {name} is unreadable: {exc}") from exc
            if not isinstance(doc, dict) or doc.get("candidate_id") != cid:
                raise FailClosed(f"quarantine record {name} disagrees with its own candidate_id")
            out[cid] = doc
        return out

    def ledger_rows(self, rel: str) -> list:
        path = self.at_path(rel)
        if not os.path.isfile(path):
            return []
        rows = []
        with open(path, encoding="utf-8") as fh:            # read-only
            for line in fh:
                if line.strip():
                    try:
                        rows.append(json.loads(line))
                    except ValueError as exc:
                        raise FailClosed(f"{rel}: append-only row is unparseable: {exc}") from exc
        return rows


# --------------------------------------------------------------------------- the two digests (element 2)
def digests(draft: bytes, target: str, landing, size_bytes: int) -> dict:
    """`06:180` names TWO digests, and they answer different questions:
       * `sha256`         -- these exact bytes at `_pending/<id>.md`, so a hand edit is visible
                             (`06:185-186` requires the mismatch to fail closed);
       * `artifact_hash`  -- the candidate AS AN ARTIFACT (target + suggested landing point +
                             size + byte digest), so the same draft aimed at a different target
                             is not read as the same proposal.
    """
    sha = hashlib.sha256(draft).hexdigest()
    payload = {"target": target, "landing": landing, "size_bytes": int(size_bytes),
               "pending_sha256": sha}
    return {"sha256": sha, "artifact_hash": prov.content_hash(payload)}


# --------------------------------------------------------------------------- pending_count / hint
def live_pending(q: "Quarantine", records: dict, now: str = None) -> list:
    """The ONLY definition of `pending_count`: derived from disk at call time.

    A candidate is live while (a) its record says `pending`, (b) its `_pending/<id>.md` bytes are
    still there, and (c) its expiry channel has not been pulled. `now` must be supplied for an
    expiry to fire: no clock, no automatic drop (`06:190-194` demands the channel, never an
    invented TTL value -- a default here would be exactly the 默认值 rendered as real data that
    05-DATA-MODEL.md §5.4 (3) forbids). Rejected and Failed candidates are excluded by the state
    check, which is where element 5 becomes observable in a number.
    """
    cutoff = _epoch(now)
    out = []
    for cid in sorted(records):
        doc = records[cid]
        if doc.get("state") != "pending":
            continue
        if not os.path.isfile(q.pending_path(cid)):
            continue
        expires = _epoch(doc.get("expires_at"))
        if expires is not None and cutoff is not None and expires <= cutoff:
            continue
        out.append(cid)
    return out


def build_report(q: "Quarantine", now: str = None, records: dict = None) -> dict:
    """The SC08 document. A rendering, never an authority: everything in it is re-read here, and
    deleting the file changes no count (proved by `test_the_report_is_a_rendering_...`)."""
    recs = q.load_records() if records is None else records
    live = live_pending(q, recs, now)
    pending_dir = q.at_path(PENDING_DIR)
    on_disk = sorted(n[:-3] for n in os.listdir(pending_dir)
                     if n.endswith(".md") and os.path.isdir(pending_dir)) if os.path.isdir(pending_dir) else []
    orphan_bytes = [cid for cid in on_disk if cid not in recs]
    missing_bytes = [cid for cid in sorted(recs) if not os.path.isfile(q.pending_path(cid))]
    count = len(live)
    return {
        "schema_version": QUARANTINE_VERSION,
        "at": q.at,
        "root": q.root,
        "inertness": {k: q.placement[k] for k in
                      ("placement_check_ran", "requested_root", "resolved_root", "host_skills_root",
                       "inside_store_root", "corpus_root", "frozen_round", "reason_codes", "ok")},
        "pending_count": count,
        # always re-derived, never read back: this line is the whole hint contract
        "hint": hint_for(count),
        "candidates": [recs[cid] for cid in sorted(recs)],
        "conflicts": q.ledger_rows(SUPPRESSED_REL),
        "rejected": {"ledger": REJECTED_REL, "rows": q.ledger_rows(REJECTED_REL)},
        "failed": {"ledger": FAILED_REL, "rows": q.ledger_rows(FAILED_REL)},
        "integrity": {"record_without_bytes": missing_bytes,
                      "bytes_without_record": orphan_bytes},
        "live_pending": live,
    }


class SchemaViolation(Exception):
    """The emitted document does not satisfy SC08 on disk: a usage/schema error (exit 64)."""

    def __init__(self, result: dict):
        super().__init__("; ".join(v["message"] for v in result["violations"]))
        self.result = result


def self_witness(report: dict, schemas_dir: str = validate.DEFAULT_SCHEMAS_DIR) -> dict:
    """Hand the report to S09, the package's only schema witness (`12:171`).

    The SC08 file carries the `pending_count<=0 => hint == ""` coupling as an if/then/else, so
    this call is what turns the contract's exit clause into a checked property on EVERY code
    path, not only in tests. The path is resolved by S09 at call time, so editing the schema
    changes the verdict on the next run instead of being shadowed by a Python copy.
    """
    result = validate.validate_artifact(SCHEMA_KIND, report, schemas_dir=schemas_dir)
    if not result["valid"]:
        raise SchemaViolation(result)
    return result


# --------------------------------------------------------------------------- element 5: the two ledgers
def note_failure(q: "Quarantine", cid: str, kind: str, target: str = "", artifact_hash: str = "",
                 flip_state: bool = True) -> dict:
    """`06:193` demands that a later failure never overwrite a more informative earlier sample:
    append-only rows with their own `at`, in a file `rejected.jsonl` never shares."""
    if kind not in FAILED_KINDS:
        raise FailClosed(f"failure kind {kind!r} is not one of the named kinds {FAILED_KINDS}")
    rows = q.ledger_rows(FAILED_REL)
    row = {"seq": len(rows) + 1, "at": q.at, "kind": kind, "candidate_id": _safe_id(cid),
           "target": str(target or ""), "artifact_hash": str(artifact_hash or "")}
    q._append(FAILED_REL, row)
    if flip_state:
        records = q.load_records()
        if cid in records and records[cid].get("state") in ("pending",):
            q._write_json(q.record_path(cid), dict(records[cid], state="failed", updated_at=q.at))
    return row


def note_suppression(q: "Quarantine", cid: str, target: str, artifact_hash: str) -> dict:
    """Element 3's non-silence clause (`06:189`): the refusal to create a second pending
    candidate for one target is recorded as `suppressed_by_pending` so a human can read it.

    The same clause asks for a `lifecycle_event`. That ledger is S08-registered and S12/S17-owned
    (`05-DATA-MODEL.md` §2 row 8), so writing it from here would be a non-Owner landing inside the
    store -- which `kd_store_layout` correctly reports as exit 2. Therefore S11 records the
    suppression in its OWN inert area and hands the caller an explicit intent to forward; the
    caller passes it to the ledger's Owner, and this module never writes outside its root.
    """
    rows = q.ledger_rows(SUPPRESSED_REL)
    row = {"seq": len(rows) + 1, "at": q.at, "action": "suppressed_by_pending",
           "candidate_id": _safe_id(cid), "target": str(target or ""),
           "artifact_hash": str(artifact_hash or "")}
    q._append(SUPPRESSED_REL, row)
    return row


def note_rejection(q: "Quarantine", cid: str, target: str, artifact_hash: str, by: str) -> dict:
    """Element 5, rejected side. `06:200`: rejected is 人的决定, so only a human actor may
    produce one; a model that could write this row would be able to launder its own proposal
    history into a 0-count queue."""
    if by not in HUMAN_DECISION_ACTORS:
        raise QuarantineRefusal(
            "NOT_A_HUMAN_DECISION",
            f"rejection actor {by!r} is not one of {HUMAN_DECISION_ACTORS}: 'rejected' is a human "
            "decision (06:200) and a model holds proposal rights only (N22b / P-1)")
    rows = q.ledger_rows(REJECTED_REL)
    row = {"seq": len(rows) + 1, "at": q.at, "candidate_id": _safe_id(cid), "target": str(target),
           "artifact_hash": str(artifact_hash), "by": by}
    q._append(REJECTED_REL, row)
    return row


# --------------------------------------------------------------------------- element 2: verification
def digest_check(q: "Quarantine", rec: dict) -> tuple:
    """Pure recomputation of both digests. Returns `(draft_bytes, mismatch_kind_or_None)`; it
    never writes, so it is safe on a read-only path and inside `apply_bundle`."""
    cid = _safe_id(rec["candidate_id"])
    path = q.pending_path(cid)
    if not os.path.isfile(path):
        return None, "pending_file_missing"
    try:
        with open(path, "rb") as fh:                            # read-only
            draft = fh.read()
    except OSError as exc:
        raise FailClosed(f"{cid}: pending bytes unreadable: {exc}") from exc
    fresh = digests(draft, rec.get("target"), rec.get("landing"), len(draft))
    if fresh["sha256"] != rec.get("sha256"):
        return draft, "sha256_mismatch"
    if fresh["artifact_hash"] != rec.get("artifact_hash"):
        return draft, "artifact_hash_mismatch"
    return draft, None


def verify_candidate(q: "Quarantine", candidate_id: str, records: dict = None) -> dict:
    """`06:185-186`: the sha256-mismatch path is 未闭合 in the reference implementation, and this
    tree's requirement is explicit -- 失配 → fail-closed 拒绝 apply + 写 failed 账. The account is
    written here; the refusal of apply is `apply_bundle` calling the same check."""
    cid = _safe_id(candidate_id)
    recs = q.load_records() if records is None else records
    if cid not in recs:
        raise QuarantineRefusal("NO_SUCH_CANDIDATE", f"{cid}: no quarantined candidate to verify")
    rec = recs[cid]
    _, kind = digest_check(q, rec)
    if kind:
        row = note_failure(q, cid, kind, rec.get("target"), rec.get("artifact_hash"))
        return {"candidate_id": cid, "ok": False, "kind": kind, "failed_row": row}
    return {"candidate_id": cid, "ok": True, "sha256": rec["sha256"],
            "artifact_hash": rec["artifact_hash"]}


# --------------------------------------------------------------------------- element 1 (+3, +5 guards)
def stage_candidate(q: "Quarantine", *, candidate_id: str, target: str, draft, landing=None,
                    expires_at=None, records: dict = None) -> dict:
    """Write one candidate into the inert area (`06:180` N19, 五要素 1+2).

    Refusals, in the order they are decided, each with the clause that puts it here:
      * replay       -- `06:190` N21 per-item watermark: the same (id, target, artifact) already
                        pending is a replay, not a second copy;
      * conflict     -- `06:187` N20 同 target 已有 pending → 拒绝新建, and `06:189` explicitly
                        refuses the "just overwrite it" fix;
      * no-new-proof -- `06:200` rejected 无新证据不得再提: the same artifact hash for a rejected
                        target stays refused, while a different hash (new evidence) is admitted,
                        and a `failed` target is always retryable. That asymmetry is the only
                        place element 5 changes a decision, so it is also the test that proves
                        rejected and failed are not one bucket.
    """
    cid = _safe_id(candidate_id)
    tgt = _target_key(target)
    if isinstance(draft, str):
        draft = draft.encode("utf-8")
    if not isinstance(draft, (bytes, bytearray)):
        raise QuarantineRefusal("BAD_DRAFT", "the draft must be bytes or text: N22b hands "
                                             "quarantine a draft, not a reference")
    # IMPLEMENTATION_GAP: N22b (`06:203`) requires the model's draft to be 可执行断言的候选 rather
    # than prose, but "is this text an executable assertion" is not a deterministic predicate and
    # no Round 2 clause makes it one, so quarantine checks only that a draft exists and reports
    # its size; the judgement belongs to the Stage 3 landing decision (N18), not here.
    # / DEFERRED id none registered (newly surfaced; recorded in W2-C-REPORT.md)
    if not draft:
        raise QuarantineRefusal("EMPTY_DRAFT", "an empty draft proves nothing was produced; "
                                              "refused rather than stored as a placeholder")
    recs = q.load_records() if records is None else records
    hashes = digests(draft, tgt, landing, len(draft))
    _epoch(expires_at)      # validate the shape now, not at the next sweep
    rejected_rows = [r for r in q.ledger_rows(REJECTED_REL) if r.get("target") == tgt]

    prior = recs.get(cid)
    if prior is not None and prior.get("state") == "pending" \
            and prior.get("target") == tgt \
            and prior.get("artifact_hash") == hashes["artifact_hash"]:
        return {"action": "replay", "candidate_id": cid, "target": tgt,
                "reason": "per-item watermark: this exact candidate is already pending "
                          "(`06:190` N21 防重放)", "record": prior}

    if rejected_rows and any(r.get("artifact_hash") == hashes["artifact_hash"]
                             for r in rejected_rows):
        raise QuarantineRefusal(
            "REJECTED_WITHOUT_NEW_EVIDENCE",
            f"{tgt}: artifact_hash {hashes['artifact_hash'][:12]}... was already rejected; 无新证据"
            "不得再提 (`06:200`) -- refusing a repeat submission rather than faking progress",
            {"candidate_id": cid, "rejected_rows": len(rejected_rows)})

    for other_id in sorted(recs):
        other = recs[other_id]
        if other.get("state") == "pending" and other.get("target") == tgt and other_id != cid:
            note_suppression(q, cid, tgt, hashes["artifact_hash"])
            raise QuarantineRefusal(
                "CONFLICT_TARGET_PENDING",
                f"target {tgt!r} already has pending candidate {other_id!r}: 同 target 已有 "
                "pending → 拒绝新建 (`06:187`); the fix is NOT to overwrite (`06:189`), the "
                "suppression is recorded and readable",
                {"candidate_id": other_id,
                 "lifecycle_event_intent": {"entity": "quarantine_candidate",
                                            "entity_id": cid,
                                            "op": "ADD",
                                            "reason": None,
                                            "detail": "suppressed_by_pending"}})
    if prior is not None and prior.get("state") == "pending":
        # same id, different bytes: replacing a live pending candidate in place is the overwrite
        # the policy refuses, so it goes through the same conflict door
        note_suppression(q, cid, tgt, hashes["artifact_hash"])
        raise QuarantineRefusal(
            "CONFLICT_TARGET_PENDING",
            f"{cid} is already pending with a different artifact; replacing pending bytes is the "
            "overwrite `06:189` refuses (reject or consume the pending one first)",
            {"prior_artifact_hash": prior.get("artifact_hash")})

    record = {
        "schema_version": QUARANTINE_VERSION,
        "candidate_id": cid,
        "target": tgt,
        "state": "pending",
        "pending_file": f"{PENDING_DIR}/{cid}.md",
        "sha256": hashes["sha256"],
        "artifact_hash": hashes["artifact_hash"],
        "size_bytes": len(draft),
        "staged_at": q.at,
    }
    if landing is not None:
        record["landing"] = str(landing)
    if expires_at is not None:
        record["expires_at"] = str(expires_at)
    if prior is not None:
        # a re-submission after a failed attempt or a rejection carries the watermark forward, so
        # the per-item history is monotone rather than reset (`06:190` N21)
        record["prior_states"] = [prior.get("state")]
    try:
        text = draft.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise QuarantineRefusal("DRAFT_NOT_TEXT",
                                f"{cid}: the Stage 2 candidate is a Markdown draft, so it must be "
                                f"UTF-8 text; refused rather than lossily re-encoded ({exc})")
    q._write(q.pending_path(cid), text)
    q._write_json(q.record_path(cid), record)
    return {"action": "staged", "candidate_id": cid, "target": tgt, "record": record,
            "replayed_rejection": bool(rejected_rows)}


# --------------------------------------------------------------------------- element 4: one transaction
def apply_bundle(q: "Quarantine", candidate_id: str, approval: dict, txn_id: str,
                 records: dict = None) -> dict:
    """五要素 4 (`06:177`), spelled out at `06:247` N27: approve and apply are ONE transaction,
    任一步失败则整批不落，不留 created_by=null 的半记录.

    The mechanical form chosen here: quarantine holds NO approve state of its own. A caller
    supplies the approval it wants applied together with the transaction id both steps share, and
    this function -- which writes nothing on the accepted path -- returns the single bundle the
    durable writer (S12) must commit. There is therefore no "approved yesterday, applied today"
    state to desynchronise, and quarantine cannot become the authority for what was approved
    (CM-32 + CM-30: one Owner per business meaning).
    """
    cid = _safe_id(candidate_id)
    recs = q.load_records() if records is None else records
    if cid not in recs:
        raise QuarantineRefusal("NO_SUCH_CANDIDATE", f"{cid}: nothing quarantined under that id")
    rec = recs[cid]
    if rec.get("state") != "pending":
        raise QuarantineRefusal("NOT_PENDING",
                                f"{cid} is {rec.get('state')!r}, not pending: a rejected, failed, "
                                "expired or consumed candidate is not applicable")
    if not isinstance(approval, dict) or not approval:
        note_failure(q, cid, "apply_refused", rec.get("target"), rec.get("artifact_hash"),
                     flip_state=False)
        raise QuarantineRefusal("APPROVAL_MISSING",
                                "apply refused: no approval accompanied this call, and approve "
                                "must be in the same transaction as apply (`06:247`)")
    if approval.get("approved") is not True:
        raise QuarantineRefusal("NOT_APPROVED",
                                "approval present but not affirmative: a refusal must never be "
                                "read as consent")
    by = approval.get("approved_by")
    if approval.get("candidate_id") != cid or approval.get("artifact_hash") != rec.get("artifact_hash"):
        raise QuarantineRefusal("APPROVAL_BINDING_MISMATCH", "approval does not cover this exact candidate")
    if by not in HUMAN_DECISION_ACTORS:
        raise QuarantineRefusal("NOT_A_HUMAN_DECISION",
                                f"approval actor {by!r} is not human: G1 是仅有的人类门 "
                                "(`12:137`), models and automation cannot approve")
    if not str(txn_id or "").strip() or not str(approval.get("txn_id") or "").strip():
        raise QuarantineRefusal("TXN_ID_MISSING",
                                "approve/apply need one shared transaction id (`06:247`); an "
                                "unnamed transaction cannot be checked against an approval")
    if str(approval.get("txn_id") or "").strip() != str(txn_id).strip():
        note_failure(q, cid, "apply_refused", rec.get("target"), rec.get("artifact_hash"),
                     flip_state=False)
        raise QuarantineRefusal(
            "APPROVE_APPLY_SPLIT",
            f"approval carries txn_id {approval.get('txn_id')!r} but apply was asked for "
            f"{txn_id!r}: two transactions, so the pair is refused (`06:247` 五要素 4)",
            {"approval_txn": approval.get("txn_id"), "apply_txn": txn_id})

    _, kind = digest_check(q, rec)
    if kind:
        # `06:186` exactly: 失配 → fail-closed 拒绝 apply + 写 failed 账
        note_failure(q, cid, kind, rec.get("target"), rec.get("artifact_hash"))
        raise FailClosed(f"{cid}: apply refused fail-closed, {kind} -- the bytes at "
                         "_pending/ do not match the record")
    return {
        "single_transaction": True,
        "txn_id": str(txn_id).strip(),
        "candidate_id": cid,
        "approve_row": {"candidate_id": cid, "target": rec.get("target"), "by": by,
                        "at": approval.get("at") or q.at, "txn_id": str(txn_id).strip()},
        "apply_intent": {"artifact_id": rec.get("target"), "candidate_id": cid,
                         "op": "ADD", "record_sha256": rec.get("sha256"),
                         "artifact_hash": rec.get("artifact_hash")},
        "pending_release": {"candidate_id": cid, "txn_id": str(txn_id).strip()},
        "durable_write_owner": "S12 kd_write_txn.commit_batch",
    }


def consume_candidate(q: "Quarantine", candidate_id: str, txn_id: str, approval: dict = None,
                      records: dict = None, *, commit_receipt: dict = None) -> dict:
    """Called by the pipeline only AFTER S12 reported a committed batch: flip the record to
    `consumed` so the queue drains. The bytes stay (no delete channel exists in this module at
    all: 07 §3.1's archive-is-the-ceiling rule, and `09:git-backed-inert-candidate-store`'s
    "未生效即可 diff" only works while the file is there).

    The approval arrives as an argument, exactly as it does for `apply_bundle`: quarantine holds
    no approval state of its own, so a release is authenticated against the same single-transaction
    proof and against the bytes that proof covered (06:247 五要素 4)."""
    cid = _safe_id(candidate_id)
    recs = q.load_records() if records is None else records
    if cid not in recs:
        raise QuarantineRefusal("NO_SUCH_CANDIDATE", f"{cid}: nothing quarantined under that id")
    rec = recs[cid]
    if not isinstance(commit_receipt, dict) or commit_receipt.get("status") != "COMMITTED" \
            or commit_receipt.get("txn_id") != txn_id or rec.get("target") not in commit_receipt.get("written", []):
        raise QuarantineRefusal("COMMIT_RECEIPT_MISSING", "queue release requires the matching S12 commit receipt")
    if not isinstance(approval, dict) or approval.get("candidate_id") != cid \
            or approval.get("artifact_hash") != rec.get("artifact_hash"):
        raise QuarantineRefusal("APPROVAL_BINDING_MISMATCH", "release approval covers a different candidate")
    if rec.get("state") != "pending":
        raise QuarantineRefusal("NOT_PENDING", f"{cid} is {rec.get('state')!r}, not pending")
    if not str(txn_id or "").strip():
        raise QuarantineRefusal("TXN_ID_MISSING",
                                f"{cid}: a release needs the transaction id it belongs to")
    if not isinstance(approval, dict) or not approval \
            or str(approval.get("txn_id") or "").strip() != str(txn_id).strip():
        raise QuarantineRefusal("APPROVE_APPLY_SPLIT",
                                f"{cid}: release refused -- the transaction being reported is not "
                                "the transaction this candidate was approved under, and "
                                "quarantine keeps no approval state to fall back on")
    if approval.get("approved") is not True or approval.get("approved_by") not in HUMAN_DECISION_ACTORS:
        raise QuarantineRefusal("NOT_A_HUMAN_DECISION",
                                f"{cid}: only an affirmative human approval of the same "
                                "transaction may drain the queue (06:200, 12:137 G1)")
    _, kind = digest_check(q, rec)
    if kind:
        note_failure(q, cid, kind, rec.get("target"), rec.get("artifact_hash"))
        raise FailClosed(f"{cid}: release refused fail-closed, {kind}")
    updated = dict(rec, state="consumed", updated_at=q.at)
    q._write_json(q.record_path(cid), updated)
    return {"candidate_id": cid, "state": "consumed", "txn_id": txn_id}


def reject_candidate(q: "Quarantine", candidate_id: str, by: str, records: dict = None) -> dict:
    cid = _safe_id(candidate_id)
    recs = q.load_records() if records is None else records
    if cid not in recs:
        raise QuarantineRefusal("NO_SUCH_CANDIDATE", f"{cid}: nothing quarantined under that id")
    rec = recs[cid]
    row = note_rejection(q, cid, rec.get("target"), rec.get("artifact_hash"), by)
    updated = dict(rec, state="rejected", updated_at=q.at)
    q._write_json(q.record_path(cid), updated)
    return {"candidate_id": cid, "state": "rejected", "rejected_row": row}


def sweep_expiry(q: "Quarantine", now: str, records: dict = None) -> dict:
    """N21's 过期通道, and the reason it needs an explicit `now`: a queue that can only grow is
    the 无界堆积 defect `06:191` names. Expiry is a state flip on the record; the draft bytes are
    retained for the diff, and no default TTL value is invented anywhere."""
    cutoff = _epoch(now)
    if cutoff is None:
        raise QuarantineRefusal("NOW_REQUIRED",
                                "the expiry sweep needs an explicit instant; without a clock "
                                "nothing expires (no invented default is applied)")
    recs = q.load_records() if records is None else records
    flipped = []
    for cid in sorted(recs):
        rec = recs[cid]
        expires = _epoch(rec.get("expires_at"))
        if rec.get("state") != "pending" or expires is None or expires > cutoff:
            continue
        q._write_json(q.record_path(cid), dict(rec, state="expired", updated_at=q.at))
        flipped.append(cid)
    return {"expired": flipped, "at": now}


# --------------------------------------------------------------------------- CLI
class UsageError(Exception):
    """A CLI usage error. argparse exits 2 by design and 2 is this package's fail-closed code,
    so a typo must never be reported as a tamper verdict (same reasoning as S12's parser)."""


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        print(f"invalid input: {message}", file=sys.stderr)
        raise UsageError(message)


ACTIONS = ("stage", "status", "verify", "reject", "fail", "apply-bundle", "consume",
           "sweep-expiry", "placement")


def build_parser() -> ArgumentParser:
    ap = ArgumentParser(
        prog="kd_quarantine.py",
        description="S11: Stage 2's inert candidate area -- pending storage with two digests, "
                    "per-target conflict refusal, one-transaction approve/apply bundles and "
                    "separate rejected/failed accounts, plus a pending_count whose hint is empty "
                    "exactly when the queue is empty. The area is never inside a host "
                    "skills/rules root, never inside the store layout, and never authoritative.",
        epilog="exit codes (12:97-103): 0 success or legal empty queue, 2 fail-closed (digest "
               "mismatch / unreadable record), 3 gate refusal (conflict, replay, "
               "no-new-evidence, approval split -- a normal terminal state, never to be retried "
               "into green), 64 usage or SC08 schema error.")
    ap.add_argument("--root", help="quarantine area root; placement-checked against host "
                                  "skills/rules roots, the store layout, repos/ and the frozen "
                                  "rounds")
    ap.add_argument("--action", choices=ACTIONS, help="what to do (default: status)")
    ap.add_argument("--id", dest="candidate_id", help="candidate id (a safe file name)")
    ap.add_argument("--target", help="what this candidate would become; conflicts are per-target")
    ap.add_argument("--draft-file", help="read the draft bytes from this file (--action stage)")
    ap.add_argument("--draft", help="inline draft text (--action stage)")
    ap.add_argument("--landing", help="N22b's SUGGESTED landing point (advisory; the authority "
                                     "for the value set is SC12 / S10 in Wave 3)")
    ap.add_argument("--expires-at", help="ISO instant after which this candidate stops counting "
                                         "(no default: an unset expiry never fires)")
    ap.add_argument("--now", help="ISO instant used by the expiry sweep and by pending_count")
    ap.add_argument("--at", help="ISO instant stamped on rows and records (taken once)")
    ap.add_argument("--by", help="decision actor for --action reject (human|user only)")
    ap.add_argument("--kind", choices=FAILED_KINDS, help="failure kind for --action fail")
    ap.add_argument("--approval-file", help="JSON approval document (--action apply-bundle), or - "
                                            "for stdin")
    ap.add_argument("--txn", help="transaction id shared by approve and apply")
    ap.add_argument("--commit-receipt-file", help="S12 COMMITTED receipt for --action consume")
    ap.add_argument("--store-root", action="append", default=[], metavar="DIR",
                    help="a store root to refuse placement inside (repeatable); ancestors holding "
                         "store-layout.json are discovered anyway")
    ap.add_argument("--schemas-dir", default=validate.DEFAULT_SCHEMAS_DIR,
                    help="resolved by S09 at call time (default: %(default)s)")
    ap.add_argument("--report", action="store_true",
                    help="emit the whole SC08 report instead of the action receipt")
    ap.add_argument("--out", help="write the emitted document here instead of on stdout")
    return ap


def _load_json(path: str):
    if path == "-":
        return json.load(sys.stdin)
    with open(path, encoding="utf-8") as fh:                    # read-only
        return json.load(fh)


def run(argv=None) -> dict:
    """The whole command surface as a testable function: returns the document to emit, and lets
    the typed exceptions reach `main` so the exit mapping lives in exactly one place."""
    ap = build_parser()
    args = ap.parse_args(list(sys.argv[1:] if argv is None else argv))
    if args.out:
        try:
            layout.assert_staging_path(args.out)
        except layout.LayoutViolation as exc:
            raise UsageError("--out cannot overwrite a protected tree or a store") from exc
    action = args.action or "status"
    if action != "placement" and not args.root:
        raise UsageError("--root is required for --action %s" % action)
    if action == "placement":
        # a read-only question about a path, for installers and for the test that proves the gate
        # bites; it never constructs a writable area
        report = check_placement(args.root or os.getcwd(), args.store_root)
        if not report["ok"]:
            raise PlacementRefusal(report)
        return {"emitted": {"action": "placement", "placement": report}, "out": args.out}

    q = Quarantine(args.root, args.store_root, at=args.at)
    result: dict = {}
    if action == "stage":
        draft = args.draft
        if args.draft_file:
            with open(args.draft_file, "rb") as fh:             # read-only input, not a write
                draft = fh.read()
        if draft is None:
            raise UsageError("--action stage needs --draft or --draft-file")
        result = stage_candidate(q, candidate_id=args.candidate_id, target=args.target,
                                 draft=draft, landing=args.landing, expires_at=args.expires_at)
    elif action == "verify":
        result = verify_candidate(q, args.candidate_id)
        if not result.get("ok"):
            # a reported mismatch is a fail-closed verdict, not a successful inspection
            raise FailClosed(f"{result['candidate_id']}: {result['kind']} "
                             f"(accounted in {FAILED_REL})")
    elif action == "reject":
        result = reject_candidate(q, args.candidate_id, args.by)
    elif action == "fail":
        if not args.kind:
            raise UsageError("--action fail needs --kind: a failure without a named kind cannot "
                             "be read back (`06:193` keeps the informative sample)")
        rec = q.load_records().get(args.candidate_id or "", {})
        result = {"failed_row": note_failure(q, args.candidate_id, args.kind,
                                             rec.get("target"), rec.get("artifact_hash"))}
    elif action == "apply-bundle":
        if not args.approval_file:
            raise UsageError("--action apply-bundle needs --approval-file (approve and apply "
                             "arrive together or not at all)")
        result = apply_bundle(q, args.candidate_id, _load_json(args.approval_file), args.txn)
    elif action == "consume":
        if not args.approval_file or not args.commit_receipt_file:
            raise UsageError("--action consume needs --approval-file and --commit-receipt-file: a release is authenticated "
                             "against the approval of the same transaction, not against state "
                             "quarantine does not keep")
        result = consume_candidate(q, args.candidate_id, args.txn, _load_json(args.approval_file),
                                   commit_receipt=_load_json(args.commit_receipt_file))
    elif action == "sweep-expiry":
        result = sweep_expiry(q, args.now)

    # every action that can move the queue ends in the same derived report, and the report is
    # witnessed by S09 on that path: the hint rule of the contract is checked on every call, not
    # only on --action status
    report = build_report(q, args.now)
    self_witness(report, args.schemas_dir)
    emitted = report if (action == "status" or args.report) else dict(
        result, action=action, pending_count=report["pending_count"], hint=report["hint"])
    return {"emitted": emitted, "out": args.out}


def main(argv=None) -> int:
    try:
        outcome = run(argv)
    except UsageError as exc:
        print(f"invalid input: {exc}", file=sys.stderr)
        return EXIT_USAGE
    except PlacementRefusal as exc:
        print(json.dumps({"refused": "PLACEMENT", "exit": EXIT_FAIL_CLOSED,
                          "placement": exc.report}, ensure_ascii=False, indent=1), file=sys.stderr)
        return EXIT_FAIL_CLOSED
    except QuarantineRefusal as exc:
        out = {"refused": exc.code, "exit": EXIT_GATE_REFUSAL, "message": str(exc)}
        out.update(exc.detail)
        print(json.dumps(out, ensure_ascii=False, indent=1), file=sys.stderr)
        return EXIT_GATE_REFUSAL
    except FailClosed as exc:
        print(f"FAIL_CLOSED: {exc}", file=sys.stderr)
        return EXIT_FAIL_CLOSED
    except SchemaViolation as exc:
        print(json.dumps({"refused": "SCHEMA", "exit": EXIT_USAGE,
                          "violations": exc.result["violations"]}, ensure_ascii=False,
                         indent=1), file=sys.stderr)
        return EXIT_USAGE
    except txn.StoreError as exc:
        print(f"write error: {exc}", file=sys.stderr)
        return EXIT_FAIL_CLOSED
    except (OSError, ValueError) as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return EXIT_USAGE

    payload = json.dumps(outcome["emitted"], ensure_ascii=False, sort_keys=True, indent=1) + "\n"
    if outcome["out"]:
        try:
            layout.assert_staging_path(outcome["out"])
            txn.atomic_write(outcome["out"], payload)
        except (layout.LayoutViolation, txn.StoreError, OSError) as exc:
            print(f"report write refused: {exc}", file=sys.stderr)
            return EXIT_FAIL_CLOSED
    else:
        print(payload, end="")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
