"""Deterministic validation and manifest generation for pilot runs.

This module deliberately does not call model APIs.  A caller supplies a response
after obtaining it through an approved execution path, which keeps secrets and
paid API policy outside the harness.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from typing import Any

from jsonschema import Draft202012Validator


MANIFEST_FORMAT = "zh-tw-agent-reliability.run-manifest/v0.1"
PROMPT_FORMAT = "zh-tw-agent-reliability.case-context/v0.1"


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def prompt_for(case: dict[str, Any], condition: str) -> str:
    """Return the complete model-input payload for a declared context condition.

    v0.1 intentionally sends only that condition payload: no hidden instruction,
    case metadata, or synthetic answer is appended.  This preserves the pilot's
    minimal/compact/structured comparison while making the hashed bytes explicit.
    """
    try:
        context = case["context_conditions"][condition]
    except KeyError as exc:
        raise ValueError(f"Unknown context condition: {condition}") from exc
    return context if isinstance(context, str) else canonical_json(context)


def prompt_hash(prompt: str) -> str:
    return "sha256:" + hashlib.sha256(prompt.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ValidatorResult:
    id: str
    type: str
    state: str
    description: str
    evidence: str | None = None


def _json_schema_target(validator: dict[str, Any]) -> dict[str, Any]:
    target = validator.get("schema", validator.get("target"))
    if isinstance(target, dict):
        return target
    if isinstance(target, str):
        try:
            parsed = json.loads(target)
        except json.JSONDecodeError as exc:
            raise ValueError("json_schema target must be a JSON Schema object or JSON string") from exc
        if isinstance(parsed, dict):
            return parsed
    raise ValueError("json_schema validator has no usable schema")


def evaluate_validator(validator: dict[str, Any], response_text: str) -> ValidatorResult:
    """Evaluate one validator without turning errors or manual checks into passes."""
    validator_id = validator["id"]
    validator_type = validator["type"]
    description = validator["description"]
    target = validator.get("target")
    try:
        if validator_type == "manual_rubric":
            return ValidatorResult(validator_id, validator_type, "manual_required", description)
        if validator_type == "contains":
            passed = isinstance(target, str) and target in response_text
        elif validator_type == "not_contains":
            passed = isinstance(target, str) and target not in response_text
        elif validator_type == "regex":
            passed = isinstance(target, str) and re.search(target, response_text, re.MULTILINE) is not None
        elif validator_type == "json_schema":
            payload = json.loads(response_text)
            errors = list(Draft202012Validator(_json_schema_target(validator)).iter_errors(payload))
            if errors:
                return ValidatorResult(validator_id, validator_type, "failed", description, errors[0].message)
            return ValidatorResult(validator_id, validator_type, "passed", description)
        else:
            return ValidatorResult(validator_id, validator_type, "error", description, "Unsupported validator type")
    except (ValueError, json.JSONDecodeError, re.error) as exc:
        return ValidatorResult(validator_id, validator_type, "error", description, str(exc))
    return ValidatorResult(validator_id, validator_type, "passed" if passed else "failed", description)


def final_state(results: list[ValidatorResult]) -> str:
    states = {result.state for result in results}
    if "error" in states:
        return "error"
    if "failed" in states:
        return "failed"
    if "manual_required" in states:
        return "pending_manual_review"
    return "passed"


def run_case(
    case: dict[str, Any],
    condition: str,
    response_text: str,
    *,
    model: str | None = None,
    repetition: int = 1,
    token_usage: dict[str, int] | None = None,
    estimated_cost_usd: float | None = None,
    raw_response_ref: str | None = None,
    response_provenance: str = "unknown",
) -> dict[str, Any]:
    prompt = prompt_for(case, condition)
    results = [evaluate_validator(item, response_text) for item in case["validators"]]
    return {
        "case_id": case["id"],
        "context_condition": condition,
        "repetition": repetition,
        "model": model,
        "prompt_format": PROMPT_FORMAT,
        "prompt_hash": prompt_hash(prompt),
        "request_timestamp": datetime.now(timezone.utc).isoformat(),
        "raw_response_ref": raw_response_ref,
        "response_provenance": response_provenance,
        "token_usage": token_usage,
        "estimated_cost_usd": estimated_cost_usd,
        "validator_results": [asdict(result) for result in results],
        "final_state": final_state(results),
    }


def new_manifest(*, execution_mode: str, runs: list[dict[str, Any]], api_calls_made: bool = False) -> dict[str, Any]:
    return {
        "format": MANIFEST_FORMAT,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "execution_mode": execution_mode,
        "api_calls_made": api_calls_made,
        "api_calls_made_by_harness": False,
        "runs": runs,
    }


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_cases(cases_dir: Path, schema_path: Path) -> list[tuple[Path, list[str]]]:
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)
    results: list[tuple[Path, list[str]]] = []
    for path in sorted(cases_dir.glob("*.json")):
        errors = sorted(validator.iter_errors(load_json(path)), key=lambda error: list(error.absolute_path))
        results.append((path, [error.message for error in errors]))
    return results
