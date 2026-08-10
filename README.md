# zh-tw-agent-reliability

**Traditional Chinese Long-Horizon Agent Reliability**

An evaluation toolkit for studying observable failures in long-horizon AI agent workflows conducted in Traditional Chinese.

> **Current status:** public pilot repository. The five initial cases have schema validation, a deterministic local runner, a run-manifest format, and a no-API structural smoke path. The public-release privacy review and Apache-2.0 licensing are complete. No real model measurements, token/cost measurements, or 90-run results have been produced.

## Local pilot commands

The executable foundation uses Python and one runtime dependency, `jsonschema`. It does **not** include API credentials or make model calls.

```powershell
python -m pip install -e .
python -m zh_tw_agent_reliability validate-cases
python -m zh_tw_agent_reliability smoke --output runs/structural-smoke.json
python -m unittest discover -s tests -v
```

`smoke` exercises all five cases under all three context conditions (15 structural runs). It deliberately provides no synthetic success response: failed deterministic checks remain `failed`, and rubric checks remain `pending_manual_review`.

For an approved externally obtained response, use `run` with a response file. The manifest records the exact context-prompt format and hash, response provenance, validator evidence, token/cost fields (initially `null`), and an explicit final state. If deterministic validation fails or errors, `run` exits nonzero. The harness itself never calls an API; an externally sourced API response is recorded as such rather than misreported as a no-API execution. See [the pilot report skeleton](docs/pilot-report.md).

## Research question

How can real-world Traditional Chinese agent workflow failures be converted into reproducible evaluations of context retention, instruction persistence, tool selection, completion integrity, recovery behavior, and operator correction burden?

## What this project evaluates

- context retention across continued tasks;
- persistence of previously established instructions;
- tool, shell, and environment selection;
- completion integrity and unsupported success claims;
- recovery after tools or browser automation fail;
- preservation of human control without excessive approval burden;
- robustness to noisy Traditional Chinese input.

The goal is not to produce one universal leaderboard score. The goal is to make specific failure patterns inspectable, rerunnable, and easier to discuss.

## Pilot v0.1

The initial pilot contains five de-identified cases:

1. **Canonical path loss** across a continued task.
2. **Wrong shell selection**, returning Bash instructions for Windows PowerShell.
3. **Excessive approval fragmentation** for a low-risk task.
4. **Unsupported completion claims** when required validation tools did not run.
5. **Missing visible human-assisted recovery** after browser verification blocks automation.

Each case includes the task, prior constraints, three context conditions, expected behavior, validators, a 0–2 scoring rubric, privacy notes, and known limitations.

## Repository layout

```text
.
├─ README.md
├─ CONTRIBUTING.md
├─ LICENSE
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
   ├─ publication-readiness.md
   ├─ open-source-fund-application.md
   ├─ anthropic-researcher-access-application.md
   └─ research-proposal-en.md
```

## Evaluation design

Each case can be executed under three context conditions:

1. **Minimal:** only the immediate task.
2. **Compact:** a short natural-language reminder of important constraints.
3. **Structured:** explicit environment, tool, constraint, and completion requirements.

The pilot plan proposes 5 cases × 3 context conditions × 3 repetitions × 2 model configurations, for 90 primary runs. Results must preserve the model output, validator evidence, rubric evidence, token usage, model configuration, and estimated API cost.

## Evidence standard

Reports must distinguish:

- **Observation:** what the model or tool actually produced.
- **Interpretation:** why the behavior may represent a failure.
- **Inference:** a broader hypothesis that still requires testing.

An inference must not be presented as an observed fact. Ambiguous outcomes should remain ambiguous rather than being silently converted into passes or failures.

## Quick navigation

- [Pilot execution plan](docs/pilot-plan.md)
- [Failure taxonomy](taxonomy/failure-taxonomy.md)
- [Case JSON Schema](schema/case.schema.json)
- [Contribution and privacy rules](CONTRIBUTING.md)
- [Publication-readiness report](docs/publication-readiness.md)
- [Codex Open Source Fund application draft](docs/open-source-fund-application.md)
- [Anthropic External Researcher Access application draft](docs/anthropic-researcher-access-application.md)
- [Research proposal draft](docs/research-proposal-en.md)

## Privacy

The repository must not publish raw private conversations, credentials, personal identifiers, secret values, private service URLs, real IP addresses, or identifiable system logs. Practitioner-observed incidents are rewritten as minimal synthetic reproductions before publication.

## Non-goals

The pilot does not claim:

- that five cases represent all Traditional Chinese users;
- that one aggregate score captures overall model quality;
- that practitioner observations establish universal causal conclusions;
- that the current draft is already a validated benchmark.

## Maintainer

**Wang Shijun (Edgar)**  
Independent builder and Traditional Chinese agent-systems evaluator based in Taiwan.

## License

This repository is licensed under [Apache-2.0](LICENSE). The license applies to the executable code, JSON Schemas, de-identified pilot cases, and repository documentation. It does not grant rights to private source material that is intentionally excluded from this repository.
