# zh-tw-agent-reliability

An open-source evaluation toolkit for failures in long-horizon AI agent workflows conducted in Traditional Chinese.

## Purpose

This project converts anonymized practitioner-observed failures into reproducible cases for evaluating:

- context retention;
- instruction persistence;
- tool and environment selection;
- completion integrity;
- recovery behavior;
- human control and correction burden;
- robustness to noisy Traditional Chinese input.

The goal is not to produce a single leaderboard score. The goal is to make specific failures inspectable, rerunnable, and easier to discuss.

## Pilot v0.1

The initial pilot contains five cases:

1. Canonical path loss across a continued task.
2. Bash instructions returned for a Windows PowerShell environment.
3. Excessive approval fragmentation for a low-risk task.
4. Unsupported completion claims when validation tools did not run.
5. Failure to switch to visible human-assisted recovery after browser verification blocks automation.

## Repository layout

```text
zh-tw-agent-reliability/
├─ README.md
├─ CONTRIBUTING.md
├─ schema/
│  └─ case.schema.json
├─ taxonomy/
│  └─ failure-taxonomy.md
├─ data/
│  └─ pilot/
│     ├─ ZH-TW-LHAR-001.json
│     ├─ ZH-TW-LHAR-002.json
│     ├─ ZH-TW-LHAR-003.json
│     ├─ ZH-TW-LHAR-004.json
│     └─ ZH-TW-LHAR-005.json
└─ docs/
   ├─ pilot-plan.md
   └─ open-source-fund-application.md
```

## Evaluation design

Each case may be executed under three context conditions:

1. **Minimal context**: only the immediate task.
2. **Compact context**: a short natural-language reminder of important constraints.
3. **Structured context**: explicit environment, tool, constraint, and completion requirements.

The pilot records deterministic validation results where possible and uses a transparent rubric where judgment is unavoidable.

## Status

This is a practitioner-led pilot. It is not yet a validated benchmark and does not claim population-level conclusions.

Current state:

- schema drafted;
- five cases drafted;
- pilot execution pending;
- public release pending privacy and reproducibility review.

## Privacy

No raw private conversations, credentials, personal identifiers, secret values, or identifiable logs are included. Cases are rewritten as minimal synthetic reproductions of observed failure patterns.

## License

License selection is pending before public release.
