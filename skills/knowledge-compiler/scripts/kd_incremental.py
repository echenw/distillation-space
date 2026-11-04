#!/usr/bin/env python3
"""Read-only material/target delta planner, not an automatic rewriter."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

import kd_task_brief as intake
import kd_material_quality as quality


class Invalid(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def require(ok, code):
    if not ok:
        raise Invalid(code)


def plan(path):
    doc = intake.parse(intake.read_file(path)[1])
    meta = intake.validate(doc)
    return doc["plan"], meta


def items_by_id(items):
    return {obj["id"]: obj for obj in items}


def delta(before_path, after_path, dossier_path=None):
    before, b = plan(before_path)
    after, a = plan(after_path)
    left = items_by_id(before["materials"])
    right = items_by_id(after["materials"])
    additions = sorted(right.keys() - left.keys())
    removals = sorted(left.keys() - right.keys())
    changed = sorted(key for key in left.keys() & right.keys()
                     if left[key]["snapshot_sha256"] != right[key]["snapshot_sha256"]
                     or left[key]["locator"] != right[key]["locator"])
    unchanged = sorted(left.keys() & right.keys() - set(changed))
    prior_products = items_by_id(before.get("deliverables", []))
    next_products = items_by_id(after.get("deliverables", []))
    changed_outputs = sorted(id_ for id_ in prior_products.keys() | next_products.keys()
                             if prior_products.get(id_) != next_products.get(id_))
    affected = set(additions + removals + changed)
    prior_units = items_by_id(before["agents"].get("work_units", []))
    current_units = items_by_id(after["agents"].get("work_units", []))
    # A deleted source can only be referenced by the OLD plan. Checking just
    # current units silently loses the work and evidence that must be retired.
    affected_prior = {uid for uid, unit in prior_units.items()
                      if affected.intersection(unit["material_ids"])}
    affected_current = {uid for uid, unit in current_units.items()
                        if affected.intersection(unit["material_ids"])}
    changed_units = {uid for uid in prior_units.keys() | current_units.keys()
                     if prior_units.get(uid) != current_units.get(uid)}
    affected_units = affected_prior | affected_current | changed_units
    # Material invalidation and work-unit lifecycle are independent changes.
    # Retire a removed unit even if all its material snapshots were unchanged.
    retired_units = prior_units.keys() - current_units.keys()
    detached_units = {
        uid for uid, old in prior_units.items()
        if uid not in current_units or
        bool(set(old["material_ids"]) - set(current_units[uid]["material_ids"]))
    }
    claim_refs = []
    affected_source_ids = set()
    if dossier_path is not None:
        # R09 owns the dossier's 2 MiB manifest boundary and duplicate-key
        # parser. R01's 256 KiB task-brief limit must not truncate R09 inputs.
        try:
            doc = quality.read_json(dossier_path)
        except quality.Invalid as exc:
            raise Invalid(exc.code) from exc
        require(type(doc) is dict and type(doc.get("version")) is int and doc["version"] == 2,
                "DOSSIER_VERSION_REQUIRED")
        sources = doc.get("sources")
        require(type(sources) is list and sources, "DOSSIER_SOURCES_INVALID")
        require(type(doc.get("claims")) is list, "DOSSIER_CLAIMS_INVALID")
        source_materials = {}
        for source in sources:
            require(type(source) is dict and type(source.get("id")) is str and
                    source["id"] and source["id"] not in source_materials,
                    "DOSSIER_SOURCE_ID_INVALID")
            # R09 source IDs are batch-local; R01 material IDs belong to the
            # frozen task plan. They are intentionally different namespaces.
            mid = source.get("material_id")
            require(type(mid) is str and mid in left, "DOSSIER_MATERIAL_BINDING_MISSING")
            lineage = source.get("lineage")
            require(type(lineage) is dict and type(lineage.get("kind")) is str and
                    lineage["kind"] in {"direct", "normalized"},
                    "DOSSIER_LINEAGE_INVALID")
            origin_digest = (source.get("sha256") if lineage["kind"] == "direct"
                             else lineage.get("source_sha256"))
            require(type(origin_digest) is str and
                    left[mid]["snapshot_sha256"] is not None and
                    origin_digest == left[mid]["snapshot_sha256"],
                    "DOSSIER_MATERIAL_SNAPSHOT_MISMATCH")
            source_materials[source["id"]] = mid
            if mid in affected:
                affected_source_ids.add(source["id"])
        claim_ids = set()
        for claim in doc["claims"]:
            require(type(claim) is dict and type(claim.get("id")) is str and
                    claim["id"] and claim["id"] not in claim_ids,
                    "DOSSIER_CLAIM_INVALID")
            claim_ids.add(claim["id"])
            evidence = claim.get("evidence")
            require(type(evidence) is list and evidence, "DOSSIER_CLAIM_EVIDENCE_INVALID")
            refs = []
            for reference in evidence:
                sid = reference.get("source_id") if type(reference) is dict else None
                require(type(sid) is str and sid in source_materials,
                        "DOSSIER_CLAIM_SOURCE_UNKNOWN")
                refs.append(source_materials[sid])
            if affected.intersection(refs):
                claim_refs.append(claim["id"])
    objective_drift = b["plan_sha256"] != a["plan_sha256"]
    return {"check": "incremental", "status": "DELTA_DETECTED" if
            affected or changed_outputs or objective_drift else "NO_CHANGES",
            "added_materials": additions, "changed_materials": changed,
            "removed_materials": removals, "unchanged_materials": unchanged,
            "changed_deliverables": changed_outputs,
            "affected_work_units": sorted(affected_units),
            "affected_current_work_units": sorted(affected_current),
            "affected_prior_work_units": sorted(affected_prior),
            "retired_work_units": sorted(retired_units),
            "detached_prior_dependencies": sorted(detached_units),
            "changed_work_units": sorted(changed_units),
            "affected_claims": sorted(set(claim_refs)),
            "affected_dossier_sources": sorted(affected_source_ids),
            "dossier_material_bindings_checked": dossier_path is not None,
            "old_plan_sha256": b["plan_sha256"],
            "new_plan_sha256": a["plan_sha256"],
            "reconfirmation_needed": objective_drift,
            "unchanged_sources_may_be_reused_only_if_sha_matches": True,
            "did_rewrite_target": False, "did_resume_host_agent": False}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Compare frozen R01 task-material snapshots")
    ap.add_argument("--previous", required=True)
    ap.add_argument("--current", required=True)
    ap.add_argument("--dossier")
    args = ap.parse_args(argv)
    try:
        report = delta(Path(args.previous), Path(args.current),
                       Path(args.dossier) if args.dossier else None)
        print(json.dumps(report, sort_keys=True, ensure_ascii=False))
        return 0
    except (Invalid, intake.Invalid, OSError, ValueError, UnicodeError) as exc:
        code = exc.code if isinstance(exc, (Invalid, intake.Invalid)) else "INVALID_INPUT"
        print(json.dumps({"check": "incremental", "status": "FAIL", "error": code}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
