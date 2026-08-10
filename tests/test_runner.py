import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator

from zh_tw_agent_reliability.runner import evaluate_validator, new_manifest, prompt_hash, run_case, validate_cases
from zh_tw_agent_reliability.cli import main


ROOT = Path(__file__).resolve().parents[1]


class RunnerTests(unittest.TestCase):
    def test_all_cases_match_schema(self):
        results = validate_cases(ROOT / "data/pilot", ROOT / "schema/case.schema.json")
        self.assertEqual(5, len(results))
        self.assertTrue(all(not errors for _, errors in results))

    def test_failure_cannot_become_pass(self):
        case = json.loads((ROOT / "data/pilot/ZH-TW-LHAR-004.json").read_text(encoding="utf-8"))
        run = run_case(case, "minimal", "Task completed; all checks passed.")
        self.assertEqual("failed", run["final_state"])

    def test_manual_rubric_requires_review(self):
        result = evaluate_validator({"id": "m", "type": "manual_rubric", "description": "review"}, "anything")
        self.assertEqual("manual_required", result.state)

    def test_json_schema_validator(self):
        validator = {"id": "json", "type": "json_schema", "description": "object", "target": '{"type":"object","required":["ok"]}'}
        self.assertEqual("passed", evaluate_validator(validator, '{"ok":true}').state)
        self.assertEqual("failed", evaluate_validator(validator, '{}').state)

    def test_all_automatic_passes_can_be_passed(self):
        case = {
            "id": "TEST-001",
            "context_conditions": {"minimal": "prompt"},
            "validators": [{"id": "c", "type": "contains", "target": "ok", "description": "contains ok"}],
        }
        self.assertEqual("passed", run_case(case, "minimal", "ok")["final_state"])

    def test_windows_path_validators_normalize_case_slashes_and_trailing_separator(self):
        canonical = {"id": "path", "type": "contains", "target": "C:\\example-workspace\\projects", "description": "canonical"}
        deprecated = {"id": "legacy", "type": "not_contains", "target": "D:\\deprecated-example", "description": "deprecated"}
        self.assertEqual("passed", evaluate_validator(canonical, "Use c:/example-workspace/projects/").state)
        self.assertEqual("failed", evaluate_validator(deprecated, "Do not use D:/DEPRECATED-EXAMPLE/").state)

    def test_manifest_matches_schema(self):
        case = json.loads((ROOT / "data/pilot/ZH-TW-LHAR-001.json").read_text(encoding="utf-8"))
        manifest = new_manifest(execution_mode="structural_smoke", runs=[run_case(case, "minimal", "")])
        schema = json.loads((ROOT / "schema/run-manifest.schema.json").read_text(encoding="utf-8"))
        self.assertEqual([], list(Draft202012Validator(schema).iter_errors(manifest)))
        self.assertTrue(manifest["runs"][0]["prompt_hash"].startswith("sha256:"))

    def test_failed_cli_run_returns_nonzero_and_records_external_api_usage(self):
        response_path = ROOT / "tests" / "_response_fixture.txt"
        output_path = ROOT / "tests" / "_manifest_fixture.json"
        self.addCleanup(response_path.unlink, missing_ok=True)
        self.addCleanup(output_path.unlink, missing_ok=True)
        response_path.write_text("Task completed; all checks passed.", encoding="utf-8")
        exit_code = main([
            "run", "--case", str(ROOT / "data/pilot/ZH-TW-LHAR-004.json"), "--condition", "minimal",
            "--response-file", str(response_path), "--response-provenance", "external_api",
            "--input-tokens", "12", "--output-tokens", "34", "--estimated-cost-usd", "0.001",
            "--output", str(output_path),
        ])
        manifest = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(1, exit_code)
        self.assertTrue(manifest["api_calls_made"])
        self.assertFalse(manifest["api_calls_made_by_harness"])
        self.assertEqual({"input_tokens": 12, "output_tokens": 34}, manifest["runs"][0]["token_usage"])


if __name__ == "__main__":
    unittest.main()
