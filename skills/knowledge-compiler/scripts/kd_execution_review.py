#!/usr/bin/env python3
"""Independent read-only review of claimed agent/tool/token run events.

Receipts are NOT authenticated. Never starts workers, sends model requests or
executes tool payloads; checks structural consistency against R01 plan only.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re

import kd_task_brief as intake

KINDS = {"agent_start", "agent_end", "model_request", "tool_result"}
STATUSES = {"success", "failed", "cancelled"}


class Invalid(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def require(ok, code):
    if not ok:
        raise Invalid(code)


def number(value, code):
    try:
        v = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        raise Invalid(code)
    require(v.is_finite() and v >= 0, code)
    return v


def count(v):
    require(type(v) is int and v >= 0, "TOKEN_COUNT_INVALID")
    return v


def run(brief_path, evidence_path):
    brief = intake.parse(intake.read_file(brief_path)[1])
    validated = intake.validate(brief)
    require(evidence_path.is_file() and not evidence_path.is_symlink(), "RUN_EVENTS_UNAVAILABLE")
    require(evidence_path.stat().st_size <= 16 * 1024 * 1024, "RUN_EVENTS_TOO_LARGE")
    with evidence_path.open("rb") as stream:
        raw = stream.read(16 * 1024 * 1024 + 1)
    require(len(raw) <= 16 * 1024 * 1024, "RUN_EVENTS_TOO_LARGE")
    data = intake.parse(raw)
    require(type(data.get("version")) is int and data["version"] == 1, "RUN_SCHEMA")
    require(data.get("plan_sha256") == validated["plan_sha256"],
            "RUN_PLAN_DRIFT")
    require(type(data.get("mode")) is str and data["mode"] in {"fixture", "host_reported"},
            "RUN_MODE_INVALID")
    host = data.get("host")
    require(type(host) is str and host.strip(), "RUN_HOST_MISSING")
    events = data.get("events")
    require(type(events) is list and events, "RUN_EVENTS_EMPTY")
    require(len(events) <= 50000, "RUN_EVENTS_TOO_MANY")
    agents = brief["plan"]["agents"]
    allowed = {"lead"}
    work = {}
    lead_units = {x["id"] for x in agents.get("work_units", [])}
    for assignment in agents.get("assignments", []):
        allowed.add(assignment["worker"])
        work[assignment["worker"]] = assignment["work_unit_id"]
        lead_units.discard(assignment["work_unit_id"])
    require(len(allowed) == agents["chosen_agents"], "RUN_AGENT_COUNT_DRIFT")
    unit_ids = {x["id"] for x in agents["work_units"]}
    starts = set()
    ends = {}
    requests = set()
    all_event_ids = set()
    req_count = 0
    tool_count = 0
    elapsed = 0
    tokens = {"input": 0, "cache_read": 0, "output": 0}
    estimates = Decimal("0")
    by_worker = {w: {"requests": 0, "input": 0, "cache_read": 0, "output": 0}
                 for w in sorted(allowed)}
    routing = agents.get("model_routing", {})
    require(type(routing) is dict, "MODEL_ROUTING_INVALID")
    for i, event in enumerate(events):
        require(type(event) is dict, "EVENT_INVALID")
        eid = event.get("id")
        require(type(eid) is str and re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_-]{0,63}", eid)
                and eid not in all_event_ids, "EVENT_ID_DUPLICATE_OR_INVALID")
        all_event_ids.add(eid)
        worker = event.get("worker")
        unit = event.get("work_unit_id")
        require(type(worker) is str and type(unit) is str and
                worker in allowed and unit in unit_ids, "UNPLANNED_AGENT_OR_UNIT")
        require((worker == "lead" and unit in lead_units) or
                (worker != "lead" and work[worker] == unit), "AGENT_UNIT_OWNERSHIP")
        kind = event.get("kind")
        require(type(kind) is str and kind in KINDS, "EVENT_KIND_INVALID")
        duration = event.get("duration_ms", 0)
        require(type(duration) is int and duration >= 0, "DURATION_INVALID")
        elapsed += duration
        key = (worker, unit)
        if kind == "agent_start":
            require(key not in starts and key not in ends, "AGENT_START_DUPLICATED")
            starts.add(key)
        elif kind == "agent_end":
            require(key in starts and key not in ends, "AGENT_END_WITHOUT_START")
            require(type(event.get("status")) is str and event["status"] in STATUSES,
                    "AGENT_EXIT_INVALID")
            ends[key] = event["status"]
        else:
            require(key in starts and key not in ends, "TASK_EVENT_OUTSIDE_AGENT_SPAN")
            if kind == "tool_result":
                tool_count += 1
                require(type(event.get("tool")) is str and event["tool"].strip() and
                        type(event.get("exit_code")) is int, "TOOL_RECEIPT_INCOMPLETE")
                digest = event.get("output_sha256")
                require(type(digest) is str and re.fullmatch(r"[a-f0-9]{64}", digest),
                        "TOOL_OUTPUT_HASH_MISSING")
            else:
                req_count += 1
                req_id = event.get("request_id")
                require(type(req_id) is str and req_id.strip() and
                        req_id not in requests, "MODEL_REQUEST_REPLAY")
                requests.add(req_id)
                model = event.get("model")
                require(type(model) is str and model.strip(), "MODEL_NAME_MISSING")
                cfg = routing.get(worker)
                require(type(cfg) is dict, "MODEL_ROUTING_REQUIRED_FOR_REQUEST")
                require(model == cfg.get("model"), "MODEL_ROUTING_DRIFT")
                require(cfg.get("max_context_tokens") is not None,
                        "MODEL_CONTEXT_CAP_REQUIRED_FOR_REQUEST")
                it = count(event.get("input_tokens"))
                cache = count(event.get("cached_input_tokens"))
                ot = count(event.get("output_tokens"))
                require(cache <= it, "CACHE_TOKENS_EXCEED_INPUT")
                cap = count(cfg["max_context_tokens"])
                # Cached input is a subset of input, not an extra charge
                # against the window. Output still occupies context.
                require(it + ot <= cap, "MODEL_CONTEXT_BUDGET_EXCEEDED")
                rates = event.get("usd_per_million", {})
                require(type(rates) is dict and all(
                    key in rates for key in ("input", "cached_input", "output")),
                    "MODEL_PRICE_INCOMPLETE")
                price = ((number(rates["input"], "MODEL_PRICE_INVALID") * (it-cache) +
                          number(rates["cached_input"], "MODEL_PRICE_INVALID") * cache +
                          number(rates["output"], "MODEL_PRICE_INVALID") * ot) /
                         Decimal(1000000))
                estimates += price
                tokens["input"] += it
                tokens["cache_read"] += cache
                tokens["output"] += ot
                by_worker[worker]["requests"] += 1
                by_worker[worker]["input"] += it
                by_worker[worker]["cache_read"] += cache
                by_worker[worker]["output"] += ot
    complete = all((w, unit) in ends and ends[(w, unit)] == "success"
                   for w, unit in starts) and bool(starts) and (
        {unit for w, unit in ends if ends[(w, unit)] == "success"} == unit_ids)
    budget = brief["plan"].get("max_cost_usd")
    if budget is not None:
        require(estimates <= number(budget, "COST_BUDGET_INVALID"),
                "COST_BUDGET_EXCEEDED")
    return {
        "check": "execution", "status": "STRUCTURAL_PASS" if complete else "NOT_PROVEN",
        "verdict": ("SIMULATION_ONLY" if data["mode"] == "fixture" else
                    "HOST_REPORTED_UNAUTHENTICATED"),
        "requests": req_count, "tool_receipts": tool_count,
        "tokens": tokens, "estimated_cost_usd": str(estimates),
        "agent_breakdown": by_worker,
        "total_reported_duration_ms": elapsed, "units": len(unit_ids),
        "completed_units": len({u for w, u in ends if ends[(w, u)] == "success"}),
        "host_receipts_authenticated": False, "model_actions_executed_by_validator": False,
        "trusted_model_costs": "NOT_VERIFIED",
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check claimed host run and token evidence")
    ap.add_argument("--brief", required=True)
    ap.add_argument("--events", required=True)
    args = ap.parse_args(argv)
    try:
        report = run(Path(args.brief), Path(args.events))
        print(json.dumps(report, sort_keys=True))
        return 0 if report["status"] == "STRUCTURAL_PASS" else 2
    except (Invalid, intake.Invalid, OSError, UnicodeError, ValueError) as exc:
        code = (exc.code if isinstance(exc, (Invalid, intake.Invalid)) else "INVALID_INPUT")
        print(json.dumps({"check": "execution", "status": "FAIL", "error": code}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
