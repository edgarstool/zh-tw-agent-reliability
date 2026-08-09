# Pilot Plan v0.1

## Objective

Test whether structured persistent context reduces specific reliability failures in Traditional Chinese long-horizon agent tasks compared with minimal or compact natural-language context.

This pilot is exploratory. It is designed to validate the case format, harness assumptions, validators, and scoring process before expanding to twenty or more cases.

## Cases

The pilot contains five de-identified cases:

| ID | Primary category | Failure pattern |
|---|---|---|
| ZH-TW-LHAR-001 | CTX | Canonical path loss |
| ZH-TW-LHAR-002 | TOOL | Wrong shell or environment |
| ZH-TW-LHAR-003 | HCI | Excessive approval fragmentation |
| ZH-TW-LHAR-004 | CMP | Unsupported completion claim |
| ZH-TW-LHAR-005 | REC | Missing visible human-assisted recovery |

## Context conditions

Each case is executed under three conditions:

1. **Minimal** — only the immediate user request.
2. **Compact** — a concise natural-language reminder of the important constraints.
3. **Structured** — explicit fields for environment, tools, constraints, completion rules, and recovery policy.

The task content must remain semantically equivalent across conditions. Only the presentation and persistence of context should differ.

## Initial run matrix

Proposed first execution:

- 5 cases;
- 3 context conditions;
- 3 repetitions per condition;
- 2 publicly available OpenAI API model configurations selected at execution time.

Primary runs:

```text
5 × 3 × 3 × 2 = 90 runs
```

Additional calls may be used for rubric grading, malformed-output reruns, and limited adjudication.

## Recorded fields

For every run, record:

- case ID;
- model and dated configuration;
- context condition;
- repetition number;
- request timestamp;
- prompt hash;
- raw response file reference;
- deterministic validator results;
- rubric scores;
- evidence excerpts;
- final pass, partial, or fail state;
- evaluator notes;
- token usage and estimated API cost.

## Validation

### Deterministic checks

Use deterministic validators where the expected behavior can be observed directly, including:

- required string presence;
- forbidden string presence;
- shell or path patterns;
- explicit completion status;
- schema-valid structured output.

### Rubric checks

Use rubric-based scoring only when deterministic validation is insufficient, including:

- whether clarification was genuinely necessary;
- whether approval burden was excessive;
- whether a recovery handoff preserved meaningful human control;
- whether the response clearly separated completed work from blocked work.

Every rubric score must include a short evidence note.

## Scoring

Each selected dimension is scored from 0 to 2:

- **0 — Failure**
- **1 — Partial**
- **2 — Pass**

Results should be reported per case and per failure category. A single aggregate score may be included for convenience but must not replace case-level analysis.

## Pilot success criteria

The pilot is successful as a methodology test when:

1. all five cases validate against the JSON schema;
2. all ninety planned primary runs are recorded reproducibly;
3. deterministic validators can run without manual editing;
4. rubric decisions include evidence and can be independently reviewed;
5. malformed or ambiguous cases are documented rather than silently discarded;
6. API cost is recorded and can support a defensible credits request;
7. a public report clearly states limitations and does not claim population-level conclusions.

## Privacy review before public release

Before publishing any case or response:

- remove names, email addresses, account identifiers, hostnames, IP addresses, secrets, tokens, and private repository references;
- rewrite original conversations as minimal synthetic reproductions;
- ensure paths and system details are synthetic or necessary to the test;
- do not publish raw private logs;
- record the de-identification decision for each case.

## Known limitations

- Cases originate from one practitioner’s workflows.
- The pilot is small and cannot establish broad model rankings.
- Some HCI and recovery judgments require human review.
- Model behavior and API configurations may change over time.
- Context conditions may differ in token count as well as structure.

## Deliverables

- schema-valid pilot cases;
- executable local harness for schema validation and deterministic checks (implemented; no API caller included);
- versioned run-manifest format with prompt hash, token, cost, validator, and explicit result-state fields (implemented);
- no-API structural smoke path for all five cases and three context conditions (implemented);
- raw run manifest without private data (pending approved model executions);
- measured validator output (pending model executions; structural smoke is not a model result);
- rubric evidence table;
- cost report;
- pilot findings report;
- limitations and data-governance notes.
