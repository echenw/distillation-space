"""S09 -- kd_validate: the schema validation gate (deterministic, sole witness).

Round 2 provenance for this module
  12-SKILL-DESIGN-BRIEF.md:171  "共 12 条，全部放 `schemas/`，由 S09 `kd_validate` 作唯一发证人"
  04-DETERMINISTIC-VS-LLM.md:77 row C1 "重试上限 1 次（`maxRetries=1` + STRICTER_SUFFIX），
                                 重试后必须再走同一确定性门；仍不合格则保留首次输出并标 `retried:true`"
  12-SKILL-DESIGN-BRIEF.md:115  S09 "2=枚举越界；有界修复重试 ≤1 次后仍走**同一**确定性门"
  05-DATA-MODEL.md:88           每条 schema 必须能指出写入者与校验者；"有列但没有写入者"禁止进判据

Design rules that are load-bearing here (each is false-if-removed):

  * The schemas on disk are the ONLY statement of field sets. Nothing in this module knows
    what fields `learning` or `pattern` have -- if a schema changes on disk, the verdict
    changes with it. Field lists in Python would silently pass stale records, which is the
    exact failure this wave exists to kill.
  * Unknown validation keywords in a foreign schema FAIL CLOSED as
    `UNSUPPORTED_SCHEMA_KEYWORD`. A keyword we cannot interpret is never treated as absent.
  * A schema file that is not there yet (other Wave 1 agents write `evidence.schema.json`,
    `scope-tuple.schema.json`, `artifact.schema.json`, `provenance-record.schema.json`,
    `lifecycle-event-ledger.schema.json` concurrently) yields the explicit result code
    `SCHEMA_MISSING` and a non-zero exit -- not a pass, and not a crash.
  * The repair retry is bounded at exactly one attempt and the retry path calls the SAME
    gate function. A resubmission can never declare itself valid: `valid` is produced only
    inside `_gate()`.

python3 stdlib only.
"""
from __future__ import annotations

import argparse
import copy
from decimal import Decimal
from fractions import Fraction
import json
import os
import re
import sys
from urllib.parse import unquote

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SCHEMAS_DIR = os.path.abspath(os.path.join(HERE, os.pardir, "schemas"))

SCHEMA_VERSION = "1"

# --------------------------------------------------------------------------- exit codes (contract)
EXIT_OK = 0                 # artifact passed the gate (possibly after the ONE bounded retry)
EXIT_FAIL_CLOSED = 1        # violations other than enum overflow; artifact NOT emitted
EXIT_ENUM_OUT_OF_RANGE = 2  # contract: "2=枚举越界"
EXIT_SCHEMA_MISSING = 3     # contract: absent schema is an explicit, non-zero result
EXIT_USAGE = 4              # bad CLI usage / unreadable instance

# --------------------------------------------------------------------------- schema keywords
# `format` is an ANNOTATION in draft 2020-12 unless a deployment opts into assertion, so the
# gate does not assert it; every machine-checkable string constraint in these schemas is
# written as `pattern` instead. Unknown *validation* keywords still fail closed below.
ANNOTATION_KEYWORDS = frozenset({
    "$schema", "$id", "$anchor", "$defs", "$comment", "title", "description",
    "default", "examples", "deprecated", "readOnly", "writeOnly", "format",
})
SUPPORTED_KEYWORDS = frozenset({
    "type", "enum", "const",
    "required", "properties", "patternProperties", "additionalProperties",
    "propertyNames", "minProperties", "maxProperties", "dependencies", "dependentRequired",
    "items", "prefixItems", "additionalItems", "contains", "minItems", "maxItems", "uniqueItems",
    "minLength", "maxLength", "pattern",
    "minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "multipleOf",
    "allOf", "anyOf", "oneOf", "not", "if", "then", "else",
    "$ref", "definitions",
})

# violation code -> what a consumer must do about it
CODE_ENUM = "ENUM_OUT_OF_RANGE"
CODE_MISSING = "MISSING_REQUIRED"
CODE_TYPE = "TYPE_MISMATCH"
CODE_ADDITIONAL = "ADDITIONAL_PROPERTY"
CODE_PATTERN = "PATTERN_MISMATCH"
CODE_BOUND = "BOUND_VIOLATION"
CODE_COUNT = "COUNT_VIOLATION"
CODE_CONST = "CONST_MISMATCH"
CODE_COMBINATOR = "COMBINATOR_FAILURE"
CODE_UNSUPPORTED = "UNSUPPORTED_SCHEMA_KEYWORD"
CODE_BAD_REF = "SCHEMA_REF_UNRESOLVED"
CODE_SCHEMA_MISSING = "SCHEMA_MISSING"
CODE_SCHEMA_UNREADABLE = "SCHEMA_UNREADABLE"
CODE_MALFORMED = "INSTANCE_MALFORMED"


class SchemaProblem(Exception):
    """A schema itself is unusable (missing, unreadable, or containing keywords this
    validator cannot interpret). Never downgraded to 'the instance is fine'."""

    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


class Violation(dict):
    """A single deterministic gate finding: {code, path, message}."""

    @property
    def code(self):
        return self["code"]


def _type_name(value) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):          # bool before int: bool IS an int in Python
        return "boolean"
    if isinstance(value, (int,)):
        return "integer" if not isinstance(value, bool) else "boolean"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def _type_ok(value, want: str) -> bool:
    got = _type_name(value)
    if want == "integer":
        # JSON: 1.0 is a valid integer; Python bools are not integers here
        return got == "integer" or (got == "number" and float(value).is_integer())
    if want == "number":
        return got in ("integer", "number")
    if want == "boolean":
        return got == "boolean"
    return got == want


def _resolve_ref(ref: str, root: dict):
    """Resolve only local RFC 6901 URI-fragment pointers, keeping empty tokens."""
    if ref == "#":
        return root
    if not isinstance(ref, str) or not ref.startswith("#/"):
        raise SchemaProblem(CODE_BAD_REF, "only local #/... JSON pointers are supported")
    if re.search(r"%(?![0-9A-Fa-f]{2})", ref[2:]):
        raise SchemaProblem(CODE_BAD_REF, "invalid percent escape in JSON pointer")
    try:
        # JSON Schema uses URI fragments; percent decoding precedes JSON Pointer
        # ~0/~1 token unescaping and must not erase empty path segments.
        pointer = unquote(ref[2:], encoding="utf-8", errors="strict")
    except UnicodeError as exc:
        raise SchemaProblem(CODE_BAD_REF, "invalid encoded JSON pointer") from exc
    node = root
    for part in pointer.split("/"):
        if re.search(r"~(?![01])", part):
            raise SchemaProblem(CODE_BAD_REF, "invalid JSON pointer escape")
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(node, dict) and part in node:
            node = node[part]
        elif (isinstance(node, list) and re.fullmatch(r"0|[1-9][0-9]*", part)
              and int(part) < len(node)):
            node = node[int(part)]
        else:
            raise SchemaProblem(CODE_BAD_REF, "unresolvable local JSON pointer")
    return node


def _json_value_key(value):
    """Hashable, type-aware JSON equality key shared by enum/const/uniqueItems.

    JSON numbers compare by their mathematical decimal value, including 1/1.0;
    booleans must remain separate from numbers, despite Python's bool == int.
    """
    if value is None:
        return ("null",)
    if type(value) is bool:
        return ("boolean", value)
    if type(value) in (int, float):
        return ("number", Fraction(Decimal(str(value))))
    if isinstance(value, str):
        return ("string", value)
    if isinstance(value, list):
        return ("array", tuple(_json_value_key(item) for item in value))
    if isinstance(value, dict):
        return ("object", tuple(sorted(
            (key, _json_value_key(item)) for key, item in value.items())))
    raise TypeError("non-JSON value")


def _json_equal(a, b) -> bool:
    return _json_value_key(a) == _json_value_key(b)


def _walk(instance, schema, root, path: str, out: list) -> None:
    if isinstance(schema, bool):
        if not schema:
            out.append(Violation(code=CODE_COMBINATOR, path=path,
                                 message="value is forbidden by the false schema"))
        return
    if not isinstance(schema, dict):
        raise SchemaProblem(CODE_UNSUPPORTED,
                            f"non-object schema at {path}: {schema!r}")
    unknown = set(schema) - SUPPORTED_KEYWORDS - ANNOTATION_KEYWORDS
    if unknown:
        # fail closed: an interpreted-later keyword must not read as "no constraint"
        raise SchemaProblem(CODE_UNSUPPORTED,
                            f"{path}: keyword(s) {sorted(unknown)} are not interpretable "
                            "by the deterministic gate")

    def hit(code: str, msg: str) -> None:
        out.append(Violation(code=code, path=path, message=msg))

    if "$ref" in schema:
        _walk(instance, _resolve_ref(schema["$ref"], root), root, path, out)
        # Draft 2020-12 also applies the sibling constraints below.

    if "type" in schema:
        want = schema["type"]
        wants = want if isinstance(want, list) else [want]
        if not any(_type_ok(instance, w) for w in wants):
            hit(CODE_TYPE, f"expected type {wants}, got {_type_name(instance)}")
            return  # further structural checks on a wrong-typed value are noise

    if "enum" in schema:
        allowed = schema["enum"]
        if not any(_json_equal(instance, a) for a in allowed):
            hit(CODE_ENUM, f"value of type {_type_name(instance)} is not in the enum")
    if "const" in schema:
        if not _json_equal(instance, schema["const"]):
            hit(CODE_CONST, "value does not match required constant")

    if isinstance(instance, dict):
        if "required" in schema:
            for key in schema["required"]:
                if key not in instance:
                    hit(CODE_MISSING, f"required property {key!r} is absent")
        props = schema.get("properties", {})
        for key, subschema in props.items():
            if key in instance:
                _walk(instance[key], subschema, root, f"{path}/{key}", out)
        pprops = schema.get("patternProperties", {})
        addl = schema.get("additionalProperties", True)
        for key, val in instance.items():
            matched = key in props
            for pat in pprops:
                if re.search(pat, key):
                    matched = True
                    _walk(val, pprops[pat], root, f"{path}/*", out)
            if matched:
                continue
            if addl is False:
                out.append(Violation(code=CODE_ADDITIONAL, path=f"{path}/*",
                                     message="unexpected property in closed field set"))
            elif isinstance(addl, dict):
                # The property name comes from untrusted input, not the Schema.
                # Diagnostic paths must not expose private source identifiers.
                _walk(val, addl, root, f"{path}/*", out)
        if "propertyNames" in schema:
            for key in instance:
                _walk(key, schema["propertyNames"], root, f"{path}/*#", out)
        if "minProperties" in schema and len(instance) < schema["minProperties"]:
            hit(CODE_COUNT, f"needs >= {schema['minProperties']} properties")
        if "maxProperties" in schema and len(instance) > schema["maxProperties"]:
            hit(CODE_COUNT, f"needs <= {schema['maxProperties']} properties")
        for dep_key, dep in schema.get("dependentRequired", {}).items():
            if dep_key in instance:
                for need in dep:
                    if need not in instance:
                        hit(CODE_MISSING, f"{dep_key!r} present, so {need!r} is required too")
        for dep_key, dep in schema.get("dependencies", {}).items():
            if dep_key not in instance:
                continue
            if isinstance(dep, list):
                for need in dep:
                    if need not in instance:
                        hit(CODE_MISSING, f"dependency {dep_key!r} requires {need!r}")
            else:
                _walk(instance, dep, root, path, out)

    if isinstance(instance, list):
        items = schema.get("items")
        prefix = schema.get("prefixItems")
        if prefix:
            for idx, item in enumerate(instance):
                if idx < len(prefix):
                    _walk(item, prefix[idx], root, f"{path}/{idx}", out)
                elif items is not None and items is not True:
                    _walk(item, items, root, f"{path}/{idx}", out)
                elif idx >= len(prefix) and schema.get("additionalItems", True) is False:
                    hit(CODE_COUNT, f"tuple has no slot {idx}")
        elif isinstance(items, (dict, bool)):
            for idx, item in enumerate(instance):
                _walk(item, items, root, f"{path}/{idx}", out)
        if "minItems" in schema and len(instance) < schema["minItems"]:
            hit(CODE_COUNT, f"needs >= {schema['minItems']} items, got {len(instance)}")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            hit(CODE_COUNT, f"needs <= {schema['maxItems']} items, got {len(instance)}")
        if schema.get("uniqueItems"):
            seen = [_json_value_key(x) for x in instance]
            if len(set(seen)) != len(seen):
                hit(CODE_COUNT, "items must be unique")
        if "contains" in schema:
            if not any(not _collect(item, schema["contains"], root) for item in instance):
                hit(CODE_COMBINATOR, "no item satisfies `contains`")

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            hit(CODE_BOUND, f"string shorter than {schema['minLength']}")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            hit(CODE_BOUND, f"string longer than {schema['maxLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            hit(CODE_PATTERN, "string does not match required pattern")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        # one comparison per keyword: sharing `>=` across `minimum` and `maximum` made every
        # `maximum` bound accept larger values, i.e. an upper limit that never limited
        for key, holds in (("minimum", lambda i, b: i >= b),
                           ("maximum", lambda i, b: i <= b),
                           ("exclusiveMinimum", lambda i, b: i > b),
                           ("exclusiveMaximum", lambda i, b: i < b)):
            if key in schema:
                bound = schema[key]
                if not holds(instance, bound):
                    hit(CODE_BOUND, f"number violates {key} bound")
        if "multipleOf" in schema:
            dividend = Fraction(Decimal(str(instance)))
            divisor = Fraction(Decimal(str(schema["multipleOf"])))
            if dividend % divisor != 0:
                hit(CODE_BOUND, "number is not a multiple of the required factor")

    for combinator in ("allOf", "anyOf", "oneOf", "not"):
        if combinator not in schema:
            continue
        subs = schema[combinator]
        if combinator == "not":
            # `not` takes ONE schema (draft 2020-12); the others take an array of schemas
            if not isinstance(subs, (dict, bool)):
                raise SchemaProblem(CODE_UNSUPPORTED,
                                    f"{path}: `not` needs one schema object, got {_type_name(subs)}")
            if not _collect(instance, subs, root):
                hit(CODE_COMBINATOR, "value must not match `not`")
            continue
        if _type_name(subs) != "array":
            raise SchemaProblem(CODE_UNSUPPORTED,
                                f"{path}: `{combinator}` needs an array of schemas, "
                                f"got {_type_name(subs)}")
        if combinator == "allOf":
            for idx, sub in enumerate(subs):
                _walk(instance, sub, root, f"{path}/allOf/{idx}", out)
            continue
        passes = [not _collect(instance, sub, root) for sub in subs]
        if combinator == "anyOf" and not any(passes):
            hit(CODE_COMBINATOR, "value matches none of `anyOf`")
        elif combinator == "oneOf" and sum(passes) != 1:
            hit(CODE_COMBINATOR, f"`oneOf` matched {sum(passes)} branches, exactly 1 required")

    if "if" in schema:
        branch_ok = not _collect(instance, schema["if"], root)
        arm = "then" if branch_ok else "else"
        if arm in schema:
            _walk(instance, schema[arm], root, f"{path}/{arm}", out)


def _collect(instance, schema, root) -> list:
    out: list = []
    _walk(instance, schema, root, "$", out)
    return out


# --------------------------------------------------------------------------- schema loading
def audit_schema_tree(schema, path: str = "$", root: dict = None, visited=None) -> None:
    """Walk every REACHABLE subschema position and reject any keyword the gate cannot interpret,
    plus any unresolvable local pointer. Run before the first instance is judged, so a peer's
    schema file cannot half-validate: an unreadable contract is a visible failure.

    Only positions that a validator would actually apply are audited -- including `$ref` targets,
    followed transitively. A `$defs` entry nobody references is documentation (peer schemas put
    invariant notes there) and is deliberately not read as a constraint.
    """
    root = root if root is not None else schema
    visited = visited if visited is not None else set()
    if isinstance(schema, bool):
        return
    if not isinstance(schema, dict):
        raise SchemaProblem(CODE_UNSUPPORTED, f"{path}: schema node is {_type_name(schema)}")
    unknown = set(schema) - SUPPORTED_KEYWORDS - ANNOTATION_KEYWORDS
    if unknown:
        raise SchemaProblem(CODE_UNSUPPORTED,
                            f"{path}: keyword(s) {sorted(unknown)} are not interpretable by the "
                            "deterministic gate")

    def malformed(key, expected):
        raise SchemaProblem(CODE_SCHEMA_UNREADABLE,
                            f"{path}/{key}: expected {expected} in Schema contract")

    def string_list(value):
        return isinstance(value, list) and all(type(v) is str for v in value) \
            and len(value) == len(set(value))

    if "type" in schema:
        value = schema["type"]
        valid_types = {"null", "boolean", "object", "array", "string", "number", "integer"}
        types = value if isinstance(value, list) else [value]
        if not types or not string_list(types) or any(v not in valid_types for v in types):
            malformed("type", "supported JSON Schema type(s)")
    if "enum" in schema and (not isinstance(schema["enum"], list) or not schema["enum"]):
        malformed("enum", "nonempty array")
    if "required" in schema and not string_list(schema["required"]):
        malformed("required", "array of unique strings")
    if "uniqueItems" in schema and type(schema["uniqueItems"]) is not bool:
        malformed("uniqueItems", "boolean")
    for key in ("minProperties", "maxProperties", "minItems", "maxItems", "minLength", "maxLength"):
        if key in schema and (type(schema[key]) is not int or schema[key] < 0):
            malformed(key, "nonnegative integer")
    for key in ("minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "multipleOf"):
        if key in schema and (type(schema[key]) not in (int, float)
                              or (key == "multipleOf" and schema[key] <= 0)):
            malformed(key, "valid numeric bound")
    if "pattern" in schema:
        if type(schema["pattern"]) is not str:
            malformed("pattern", "regular expression string")
        try:
            re.compile(schema["pattern"])
        except re.error as exc:
            raise SchemaProblem(CODE_SCHEMA_UNREADABLE, f"{path}/pattern: invalid regex") from exc

    for key in ("items", "additionalItems", "additionalProperties", "contains", "propertyNames",
                "if", "then", "else", "not"):
        if key in schema:
            node = schema[key]
            if not isinstance(node, (dict, bool)):
                malformed(key, "schema object or boolean")
            audit_schema_tree(node, f"{path}/{key}", root, visited)

    for key in ("properties", "patternProperties", "definitions"):
        if key in schema:
            values = schema[key]
            if not isinstance(values, dict) or any(type(name) is not str for name in values):
                malformed(key, "object of subschemas")
            if key == "patternProperties":
                for pattern in values:
                    try:
                        re.compile(pattern)
                    except re.error as exc:
                        raise SchemaProblem(CODE_SCHEMA_UNREADABLE,
                                            f"{path}/{key}: invalid regex") from exc
            if key != "definitions":  # unreferenced definitions are annotations, not constraints
                for name, node in values.items():
                    audit_schema_tree(node, f"{path}/{key}/{name}", root, visited)

    for key in ("allOf", "anyOf", "oneOf", "prefixItems"):
        if key in schema:
            subschemas = schema[key]
            if not isinstance(subschemas, list) or (
                    key != "prefixItems" and not subschemas):
                malformed(key, "array of subschemas")
            for idx, node in enumerate(subschemas):
                audit_schema_tree(node, f"{path}/{key}/{idx}", root, visited)

    for key in ("dependencies", "dependentRequired"):
        if key in schema:
            values = schema[key]
            if not isinstance(values, dict):
                malformed(key, "object")
            for name, node in values.items():
                if key == "dependentRequired" or isinstance(node, list):
                    if not string_list(node):
                        malformed(f"{key}/{name}", "array of unique strings")
                else:
                    audit_schema_tree(node, f"{path}/{key}/{name}", root, visited)

    if "$ref" in schema:
        ref = schema["$ref"]
        if not isinstance(ref, str):
            malformed("$ref", "string")
        node = _resolve_ref(ref, root)
        if ref not in visited:
            visited.add(ref)
            audit_schema_tree(node, f"{path}->({ref})", root, visited)


def schema_path(kind: str, schemas_dir: str = DEFAULT_SCHEMAS_DIR) -> str:
    name = kind if kind.endswith(".schema.json") else f"{kind}.schema.json"
    return os.path.join(schemas_dir, os.path.basename(name))


# Schema contracts are small (the current largest is < 30 KiB); a 4 MiB
# ceiling permits richer external schemas. JSONL may batch many artifacts, so
# it has a separate 32 MiB budget instead of inheriting R03's 8 MiB source cap.
MAX_SCHEMA_BYTES = 4 * 1024 * 1024
MAX_ARTIFACT_BYTES = 32 * 1024 * 1024


def _read_bounded(path: str, limit: int, code: str, label: str) -> bytes:
    """Read at most limit+1 bytes, including when the file grows during read."""
    with open(path, "rb") as fh:
        raw = fh.read(limit + 1)
    if len(raw) > limit:
        raise SchemaProblem(code, f"{label} exceeds {limit} byte limit")
    return raw


def load_schema(kind: str, schemas_dir: str = DEFAULT_SCHEMAS_DIR) -> dict:
    """Resolved at CALL time, never cached: the on-disk schema is the authority, so an edit
    by another agent must take effect on the next validation, not the next process start."""
    path = schema_path(kind, schemas_dir)
    if not os.path.exists(path):
        raise SchemaProblem(CODE_SCHEMA_MISSING,
                            "schema contract is missing; validation cannot certify the artifact")
    import kd_material_ops as json_input
    try:
        doc = json_input.strict_json(_read_bounded(
            path, MAX_SCHEMA_BYTES, CODE_SCHEMA_UNREADABLE, "schema input"))
    except (OSError, json_input.Invalid) as exc:
        raise SchemaProblem(CODE_SCHEMA_UNREADABLE, "schema JSON is unavailable or malformed") from exc
    if not isinstance(doc, dict):
        raise SchemaProblem(CODE_SCHEMA_UNREADABLE, "schema top level is not an object")
    audit_schema_tree(doc)      # whole-file keyword audit, before any instance is judged
    return doc


# --------------------------------------------------------------------------- the gate
MAX_REPAIR_ATTEMPTS = 1   # 04:77 row C1 `maxRetries=1`; raising this violates the contract

GATE_CALLS = 0            # observability: proves the retry went through THIS gate, not another


def _gate(kind: str, artifact, schemas_dir: str) -> dict:
    """THE deterministic gate. The only function in this module allowed to set `valid`."""
    global GATE_CALLS
    GATE_CALLS += 1
    try:
        # A PASS must also be serializable by the same UTF-8 wire format
        # downstream -- json.dumps() alone tolerates unpaired surrogate escapes.
        canonical_bytes(artifact)
    except (TypeError, ValueError, UnicodeError, RecursionError) as exc:
        return {"valid": False, "code": CODE_MALFORMED, "violations": [
            Violation(code=CODE_MALFORMED, path="$", message=type(exc).__name__)]}
    try:
        schema = load_schema(kind, schemas_dir)
    except SchemaProblem as exc:
        return {"valid": False, "code": exc.code, "violations": [
            Violation(code=exc.code, path="$schema", message=exc.detail)]}
    except (KeyError, TypeError, ValueError, RecursionError, re.error) as exc:
        return {"valid": False, "code": CODE_SCHEMA_UNREADABLE, "violations": [
            Violation(code=CODE_SCHEMA_UNREADABLE, path="$schema", message=type(exc).__name__)]}
    try:
        violations = _collect(artifact, schema, schema)
    except SchemaProblem as exc:
        return {"valid": False, "code": exc.code, "violations": [
            Violation(code=exc.code, path="$schema", message=exc.detail)]}
    except (KeyError, TypeError, ValueError, RecursionError, re.error) as exc:
        return {"valid": False, "code": CODE_SCHEMA_UNREADABLE, "violations": [
            Violation(code=CODE_SCHEMA_UNREADABLE, path="$schema", message=type(exc).__name__)]}
    codes = {v["code"] for v in violations}
    return {"valid": not violations, "code": sorted(codes)[0] if violations else "PASS",
            "violations": violations, "schema_violation_codes": sorted(codes)}


def validate_artifact(kind: str, artifact, *, schemas_dir: str = DEFAULT_SCHEMAS_DIR,
                      repair=None, attempts: int = MAX_REPAIR_ATTEMPTS) -> dict:
    """Validate `artifact` against `schemas/<kind>.schema.json`, with AT MOST `attempts`
    bounded repairs, every attempt going through `_gate`.

    `repair(artifact, violations) -> artifact | None` is the caller's retry right (the model
    has proposal rights only, 12:133 M1/M2). It may only produce a replacement artifact;
    it can never influence `valid`.

    Returns {valid, code, violations, retried, attempts, artifact}.
    On failure the FIRST output is kept (04:77 "仍不合格则保留首次输出并标 retried:true").
    """
    if type(attempts) is not int or attempts not in (0, MAX_REPAIR_ATTEMPTS):
        raise ValueError(f"repair attempts are contractually capped at {MAX_REPAIR_ATTEMPTS}")
    try:
        # Check *before* deepcopy: a dict/list subclass can return itself from
        # __deepcopy__ and leave a supposedly certified artifact caller-owned.
        # Only exact JSON container types have trusted copy semantics here.
        _require_json_structure(artifact)
        artifact = copy.deepcopy(artifact)
    except (RecursionError, TypeError, ValueError) as exc:
        refused = {"valid": False, "code": CODE_MALFORMED, "violations": [
            Violation(code=CODE_MALFORMED, path="$", message=type(exc).__name__)]}
        return dict(refused, retried=False, attempts=1, artifact=None)
    first = _gate(kind, artifact, schemas_dir)
    if first["valid"] or repair is None or attempts == 0:
        return dict(first, retried=False, attempts=1, artifact=artifact)

    try:
        proposal = repair(copy.deepcopy(artifact), copy.deepcopy(first["violations"]))
    except Exception:
        # Model/host adapters can time out or raise. Keep the first failure and
        # never expose provider exceptions, which may include private material.
        second = {"valid": False, "code": CODE_MALFORMED, "violations": [
            Violation(code=CODE_MALFORMED, path="$", message="retry callback failed")]}
    else:
        try:
            # Check before deepcopy for the same reason as the first attempt:
            # a hostile JSON-like subclass can defeat deepcopy isolation.
            _require_json_structure(proposal)
            replacement = copy.deepcopy(proposal)
        except (RecursionError, TypeError, ValueError) as exc:
            second = {"valid": False, "code": CODE_MALFORMED, "violations": [
                Violation(code=CODE_MALFORMED, path="$",
                          message=f"retry candidate cannot be copied ({type(exc).__name__})")]}
        else:
            second = _gate(kind, replacement, schemas_dir)  # SAME gate, once
    if second["valid"]:
        return dict(second, retried=True, attempts=2, artifact=replacement)
    # retry did not clear the gate: keep the first output, mark it retried, stay fail-closed
    return dict(first, retried=True, attempts=2, artifact=artifact,
                code=first["code"] or "RETRY_STILL_INVALID",
                violations=first["violations"] + [
                    Violation(code="RETRY_EXHAUSTED", path="$",
                              message=f"bounded repair retry (<= {MAX_REPAIR_ATTEMPTS}) did not "
                              f"yield a passing candidate: {[v['message'] for v in second['violations']]}")])


def exit_code_for(result: dict) -> int:
    """Contract mapping. Enum overflow outranks everything else (12:115)."""
    codes = {v["code"] for v in result["violations"]}
    if result["valid"]:
        return EXIT_OK
    if CODE_SCHEMA_MISSING in codes or result.get("code") == CODE_SCHEMA_MISSING:
        return EXIT_SCHEMA_MISSING
    if CODE_ENUM in codes:
        return EXIT_ENUM_OUT_OF_RANGE
    if result.get("code") == CODE_SCHEMA_UNREADABLE or CODE_UNSUPPORTED in codes:
        return EXIT_FAIL_CLOSED
    return EXIT_FAIL_CLOSED


# --------------------------------------------------------------------------- artifact IO
def read_artifacts(path: str) -> list:
    """Read JSON/JSONL without accepting duplicate keys or nonstandard numbers.

    R03's strict JSON decoder is the shared parsing policy; S09 remains the
    sole authority for validating the decoded document against its Schema.
    """
    import kd_material_ops as json_input
    raw = _read_bounded(path, MAX_ARTIFACT_BYTES, CODE_MALFORMED, "artifact input")
    if not raw.strip():
        return []

    def decode(data: bytes, location: str):
        try:
            return json_input.strict_json(data)
        except json_input.Invalid as exc:
            raise SchemaProblem(CODE_MALFORMED, f"{location}: {exc.code}") from exc

    if not path.endswith(".jsonl"):
        return [decode(raw, "JSON input")]
    out = []
    for num, line in enumerate(raw.splitlines(), 1):
        if line.strip():
            out.append(decode(line, f"JSONL line {num}"))
    return out


def _require_json_structure(value) -> None:
    """Reject Python-only values before issuing a certificate for JSON bytes.

    json.dumps silently turns integer/boolean object keys into strings and
    tuples into arrays, which could bypass constraints checked on the original
    Python object. Validation and eventual wire bytes must describe one value.
    """
    if value is None or type(value) in (bool, int, float, str):
        return
    if type(value) is list:
        for item in value:
            _require_json_structure(item)
        return
    if type(value) is dict:
        for key, item in value.items():
            if type(key) is not str:
                raise TypeError("JSON object keys must be strings")
            _require_json_structure(item)
        return
    raise TypeError("non-JSON value")


def canonical_bytes(obj) -> bytes:
    _require_json_structure(obj)
    return json.dumps(obj, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def _same_file_target(first: str, second: str) -> bool:
    """Detect input/output aliases before staging may replace a source file.

    realpath catches parent-directory symlinks even for a new output; samefile
    catches aliases of existing paths on case-insensitive filesystems.
    """
    if os.path.realpath(first) == os.path.realpath(second):
        return True
    return os.path.exists(first) and os.path.exists(second) and os.path.samefile(first, second)


class _UsageArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        # argparse's normal exit 2 is *reserved* for the S09 enum verdict.
        # Avoid echoing arbitrary argument values (which could be sensitive).
        self.print_usage(sys.stderr)
        self.exit(EXIT_USAGE, "usage error: invalid command-line arguments\n")


def main(argv=None) -> int:
    ap = _UsageArgumentParser(
        prog="kd_validate.py",
        description="S09 deterministic schema gate. Validates stage artifacts against the "
                    "schemas on disk; one bounded repair retry, which goes through the same gate.")
    ap.add_argument("--kind", help="schema kind, i.e. the file name stem in --schemas-dir "
                                   "(learning, pattern, evidence, scope-tuple, artifact, ...)")
    ap.add_argument("--input", help="artifact file: one JSON document, or .jsonl with one per line")
    ap.add_argument("--schemas-dir", default=DEFAULT_SCHEMAS_DIR,
                    help=f"resolved at call time (default: {DEFAULT_SCHEMAS_DIR})")
    ap.add_argument("--out", help="write the validated (unchanged) artifacts here; only on pass")
    ap.add_argument("--report", help="write the JSON validation report here")
    ap.add_argument("--retry-with", metavar="FILE",
                    help="the caller's ONE bounded resubmission; re-validated by this same gate")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    import kd_store_layout as layout
    try:
        for path in (args.report, args.out):
            if path:
                layout.assert_staging_path(path)
    except layout.LayoutViolation as exc:
        # Layout exception text includes the caller-supplied filesystem path.
        # Ordinary diagnostics are not a trusted place for that metadata.
        print(f"USAGE: protected output target ({type(exc).__name__})", file=sys.stderr)
        return EXIT_USAGE

    # --kind/--input remain manually required; _UsageArgumentParser maps all
    # other argparse errors to 4 instead of the reserved enum verdict 2.
    if not args.kind or not args.input:
        print("usage error: --kind and --input are both required", file=sys.stderr)
        return EXIT_USAGE

    # S08 guards where staging may be written, but only S09 knows which
    # input, retry and Schema files are sources rather than derived outputs.
    # Check parent symlinks and existing inode aliases as well as path spelling.
    schema_source = schema_path(args.kind, args.schemas_dir)
    paths = (
        (args.input, args.retry_with, "--input and --retry-with"),
        (args.report, args.out, "--report and --out"),
        (args.report, args.input, "--report and --input"),
        (args.out, args.input, "--out and --input"),
        (args.report, args.retry_with, "--report and --retry-with"),
        (args.out, args.retry_with, "--out and --retry-with"),
        (args.report, schema_source, "--report and Schema"),
        (args.out, schema_source, "--out and Schema"),
    )
    try:
        for first, second, labels in paths:
            if first and second and _same_file_target(first, second):
                print(f"usage error: {labels} must refer to different files", file=sys.stderr)
                return EXIT_USAGE
    except OSError as exc:
        print(f"usage error: unable to verify path isolation ({type(exc).__name__})",
              file=sys.stderr)
        return EXIT_USAGE

    # Publish a non-success receipt BEFORE opening inputs. This also replaces
    # a previous run's success at a reused --report path when this run fails
    # during JSON/retry loading, rather than leaving a stale success receipt.
    first_gate_call = GATE_CALLS
    report = {"kind": args.kind, "schemas_dir": "<redacted>",
              "gate_calls": 0, "max_repair_attempts": MAX_REPAIR_ATTEMPTS,
              "exit_code": EXIT_USAGE, "passed": 0, "total": 0, "results": []}

    def save_report(code: int) -> None:
        layout.write_staging_text(args.report, json.dumps(
            dict(report, exit_code=code), ensure_ascii=False, sort_keys=True, indent=2) + "\n")

    if args.report:
        try:
            save_report(EXIT_USAGE)
        except (OSError, layout.LayoutViolation) as exc:
            print(f"USAGE: cannot write --report: {type(exc).__name__}", file=sys.stderr)
            return EXIT_USAGE

    def _file_repair(_artifact, _violations):
        return replacement

    replacement = None
    repair = None
    if args.retry_with:
        try:
            docs = read_artifacts(args.retry_with)
        except OSError as exc:
            print(f"input error: retry document unavailable ({type(exc).__name__})", file=sys.stderr)
            return EXIT_USAGE
        except SchemaProblem as exc:
            print(f"{exc}", file=sys.stderr)
            return EXIT_USAGE
        if len(docs) != 1:
            print("usage error: --retry-with must hold exactly one document", file=sys.stderr)
            return EXIT_USAGE
        replacement = docs[0]
        repair = _file_repair

    try:
        artifacts = read_artifacts(args.input)
    except OSError as exc:
        print(f"input error: source unavailable ({type(exc).__name__})", file=sys.stderr)
        return EXIT_USAGE
    except SchemaProblem as exc:
        print(f"{exc}", file=sys.stderr)
        return EXIT_USAGE
    if not artifacts:
        print("input error: no documents to validate", file=sys.stderr)
        return EXIT_USAGE
    if repair is not None and len(artifacts) != 1:
        print("usage error: --retry-with requires exactly one input document", file=sys.stderr)
        return EXIT_USAGE

    worst = EXIT_OK
    rows = []
    kept = []
    for idx, art in enumerate(artifacts):
        result = validate_artifact(args.kind, art, schemas_dir=args.schemas_dir, repair=repair)
        code = exit_code_for(result)
        worst = code if code > worst and code != EXIT_USAGE else worst
        rows.append({"index": idx, "kind": args.kind, "valid": result["valid"],
                     "code": result["code"], "retried": result["retried"],
                     "attempts": result["attempts"],
                     "violations": [dict(v) for v in result["violations"][:20]]})
        if result["valid"]:
            kept.append(result["artifact"])

    report.update({"gate_calls": GATE_CALLS - first_gate_call,
                   "exit_code": worst, "passed": len(kept),
                   "total": len(artifacts), "results": rows})

    # With both outputs requested, publish a fail-closed provisional report
    # first. It replaces any stale prior success; only successful delivery of
    # --out allows the final report to claim success. An interruption or
    # failed output leaves exit_code=4 rather than a false success receipt.
    if args.report and args.out and worst == EXIT_OK:
        try:
            save_report(EXIT_USAGE)
        except (OSError, layout.LayoutViolation) as exc:
            print(f"USAGE: cannot write --report: {type(exc).__name__}", file=sys.stderr)
            return EXIT_USAGE

    # fail-closed: nothing passes through a gate it did not clear
    if worst == EXIT_OK and args.out:
        try:
            layout.write_staging_text(args.out, "".join(
                canonical_bytes(doc).decode("utf-8") + "\n" for doc in kept))
        except (OSError, layout.LayoutViolation) as exc:
            print(f"USAGE: cannot write --out: {type(exc).__name__}", file=sys.stderr)
            return EXIT_USAGE
    if args.report:
        try:
            save_report(worst)
        except (OSError, layout.LayoutViolation) as exc:
            print(f"USAGE: cannot write --report: {type(exc).__name__}", file=sys.stderr)
            return EXIT_USAGE
    if not args.quiet:
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return worst


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
