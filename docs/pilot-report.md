# Pilot Report v0.1 — execution foundation

## Status

This is a reporting skeleton, not a results report. The executable local harness and structural smoke path were implemented on 2026-08-09. No model API calls, paid runs, rubric grades, token measurements, cost measurements, or comparative conclusions have been produced by this foundation alone.

## Measured implementation evidence

| Item | Status | Evidence |
|---|---|---|
| Pilot case schema validation | Measured locally | `validate-cases` validates the five current JSON case files. |
| Deterministic runner | Measured locally | Supports `contains`, `not_contains`, `regex`, `manual_rubric`, and `json_schema`. |
| Prompt identity and hashing | Measured locally | Each run records the versioned exact condition-prompt format and `sha256:<digest>` of its bytes; v0.1 appends no hidden instruction or synthetic answer. |
| Structural smoke | Measured locally | Runs 5 cases × 3 conditions without model/API execution and produces a manifest. |
| Failure integrity | Measured locally | Failed validators result in `failed`; manual checks result in `pending_manual_review`. |

## Pending measurements

| Measurement | Current state | Required before reporting |
|---|---|---|
| Model outcomes | Pending | An approved API execution plan and selected dated model configurations. |
| Token usage | Pending | API usage metadata for every run. |
| Estimated cost | Pending | Price basis plus recorded token usage. |
| Manual rubric scores | Pending | Independent reviewer score and evidence per rubric dimension. |
| 90-run comparison | Pending | 5 cases × 3 conditions × 3 repetitions × 2 model configurations. |

## Result state semantics

- `passed`: every automatic validator passed and no manual rubric remains.
- `pending_manual_review`: automatic validators passed, but a rubric still needs evidence-based review.
- `failed`: at least one deterministic validator failed.
- `error`: a validator could not be evaluated. This is never a pass. The `run` CLI exits nonzero for `failed` and `error` states.

## Limitations

- The structural smoke run exercises harness behavior, not model behavior.
- The current five cases are a de-identified practitioner-led pilot and cannot support population-level claims.
- Raw responses must remain outside the repository until privacy review confirms they contain no private data.
