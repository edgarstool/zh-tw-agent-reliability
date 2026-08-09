"""Command-line entry points for validation, local response evaluation, and smoke runs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .runner import load_json, new_manifest, run_case, validate_cases


def _write_json(value: object, output: Path | None) -> None:
    rendered = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    if output is None:
        print(rendered, end="")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
        print(f"Wrote {output}")


def command_validate(args: argparse.Namespace) -> int:
    results = validate_cases(Path(args.cases_dir), Path(args.schema))
    invalid = 0
    for path, errors in results:
        if errors:
            invalid += 1
            print(f"FAIL {path}: " + "; ".join(errors))
        else:
            print(f"PASS {path}")
    print(f"Validated {len(results)} case(s): {len(results) - invalid} passed, {invalid} failed")
    return 1 if invalid else 0


def command_run(args: argparse.Namespace) -> int:
    case = load_json(Path(args.case))
    response = Path(args.response_file).read_text(encoding="utf-8")
    token_usage = {key: value for key, value in {
        "input_tokens": args.input_tokens,
        "output_tokens": args.output_tokens,
        "total_tokens": args.total_tokens,
    }.items() if value is not None} or None
    run = run_case(
        case,
        args.condition,
        response,
        model=args.model,
        repetition=args.repetition,
        token_usage=token_usage,
        estimated_cost_usd=args.estimated_cost_usd,
        response_provenance=args.response_provenance,
    )
    _write_json(
        new_manifest(
            execution_mode="external_response",
            runs=[run],
            api_calls_made=args.response_provenance == "external_api",
        ),
        Path(args.output) if args.output else None,
    )
    return 1 if run["final_state"] in {"failed", "error"} else 0


def command_smoke(args: argparse.Namespace) -> int:
    # This deliberately uses a marker rather than a synthetic success response.
    # Failed checks remain failed and manual checks remain pending for review.
    response = "[STRUCTURAL_SMOKE_NO_MODEL_RESPONSE]"
    runs = []
    for path in sorted(Path(args.cases_dir).glob("*.json")):
        case = load_json(path)
        for condition in ("minimal", "compact", "structured"):
            runs.append(run_case(case, condition, response, model=None, raw_response_ref=None, response_provenance="structural_smoke"))
    manifest = new_manifest(execution_mode="structural_smoke", runs=runs)
    _write_json(manifest, Path(args.output) if args.output else None)
    print(f"Structural smoke executed {len(runs)} run(s); no model API call was made.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="zh-tw-agent-reliability")
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate-cases", help="Validate every pilot JSON file against the case schema.")
    validate.add_argument("--cases-dir", default="data/pilot")
    validate.add_argument("--schema", default="schema/case.schema.json")
    validate.set_defaults(func=command_validate)
    run = commands.add_parser("run", help="Evaluate one externally produced response; no API call is made.")
    run.add_argument("--case", required=True)
    run.add_argument("--condition", choices=("minimal", "compact", "structured"), required=True)
    run.add_argument("--response-file", required=True)
    run.add_argument("--model")
    run.add_argument("--repetition", type=int, default=1)
    run.add_argument("--response-provenance", choices=("external_api", "external_manual", "unknown"), default="unknown")
    run.add_argument("--input-tokens", type=int)
    run.add_argument("--output-tokens", type=int)
    run.add_argument("--total-tokens", type=int)
    run.add_argument("--estimated-cost-usd", type=float)
    run.add_argument("--output")
    run.set_defaults(func=command_run)
    smoke = commands.add_parser("smoke", help="Exercise all five cases and three conditions without a model API call.")
    smoke.add_argument("--cases-dir", default="data/pilot")
    smoke.add_argument("--output")
    smoke.set_defaults(func=command_smoke)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)
