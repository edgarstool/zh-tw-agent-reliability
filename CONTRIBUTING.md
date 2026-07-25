# Contributing

Thank you for helping improve Traditional Chinese long-horizon agent reliability evaluations.

## Before contributing

Please read:

- `README.md`
- `schema/case.schema.json`
- `taxonomy/failure-taxonomy.md`
- `docs/pilot-plan.md`

## Accepted contributions

- new de-identified failure cases;
- corrections to expected behavior or validators;
- reproducibility improvements;
- execution harness code;
- scoring rubric clarification;
- Traditional Chinese wording review;
- privacy and data-governance review;
- pilot result replication.

## Case requirements

A contributed case must:

1. represent a specific observable failure pattern;
2. avoid raw private conversations or identifiable logs;
3. contain no credentials, tokens, private keys, recovery codes, personal identifiers, private hostnames, or private repository names;
4. use synthetic or minimally necessary environment details;
5. define expected behavior;
6. include at least one validator;
7. include scoring dimensions and evidence expectations;
8. state known limitations;
9. validate against `schema/case.schema.json`;
10. avoid broad claims that are not supported by the case.

## Evidence standard

Separate the following:

- **Observation:** what the model or tool actually produced;
- **Interpretation:** why the behavior may represent a failure;
- **Inference:** a broader hypothesis that still requires testing.

Do not present an inference as an observed fact.

## Privacy

Do not submit:

- raw chat exports;
- screenshots containing account or personal data;
- secrets or secret-like values;
- private service URLs;
- real IP addresses;
- unredacted system logs;
- material that you do not have permission to publish.

Rewrite incidents into minimal synthetic reproductions before opening a pull request.

## Pull request checklist

- [ ] The case validates against the JSON schema.
- [ ] The primary category is appropriate.
- [ ] Context conditions test the same underlying task.
- [ ] Validators are observable and not circular.
- [ ] Rubric scores require evidence.
- [ ] Privacy review is complete.
- [ ] Limitations are stated.
- [ ] No claims of broad model superiority are based on one case.

## Review policy

A case may remain in `draft` when its failure pattern is useful but its validators or wording still require review.

A case should move to `pilot` only after schema validation and at least one successful harness execution.

A case should move to `validated` only after independent review or replication criteria are defined and met.
