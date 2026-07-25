# Codex Open Source Fund Application Draft

## Applicant

**Name:** Wang Shijun (Edgar)

**Location:** Taiwan

**GitHub:** https://github.com/edgarstool

## Project

**Project name:** zh-tw-agent-reliability

**Repository:** https://github.com/edgarstool/zh-tw-agent-reliability

## Brief description

zh-tw-agent-reliability is an open-source evaluation toolkit for studying failures in long-horizon AI agent workflows conducted in Traditional Chinese.

The project converts anonymized practitioner-observed failures into reproducible test cases covering context retention, instruction persistence, tool and environment selection, completion integrity, recovery behavior, language robustness, and the amount of human correction required to complete a task.

Each case includes the task, prior constraints, three context conditions, expected behavior, deterministic validators where possible, transparent rubric dimensions, privacy notes, and known limitations.

The formal private pilot currently contains five drafted cases. They will be prepared for public release after schema validation, harness execution, privacy review, and license selection. The dataset is intended to expand to at least twenty cases after the pilot process has been tested.

## Why this project is useful

Public agent evaluations often emphasize isolated English-language tasks. They are less likely to represent workflows where a Traditional Chinese user coordinates Windows PowerShell, coding agents, browser tools, GitHub, MCP services, cloud systems, and human approval boundaries over many steps.

This project focuses on inspectable failure patterns rather than a single leaderboard score. Maintainers should be able to rerun a case, see exactly which requirement failed, and extend the dataset with new cases.

## How API credits would be used

API credits would support:

- controlled repeated execution of the evaluation matrix;
- comparison of minimal, compact, and structured context conditions;
- testing context retention and instruction persistence;
- testing tool, shell, and environment selection;
- measuring unsupported completion claims and recovery behavior;
- structured model grading alongside deterministic validators;
- malformed-output reruns and limited adjudication;
- public baseline and regression reports;
- Codex CLI use for test generation, schema maintenance, contribution review, and validator improvements.

The pilot matrix currently proposes:

```text
5 cases × 3 context conditions × 3 repetitions × 2 model configurations = 90 primary runs
```

The full milestone will expand to at least twenty cases. Token usage and estimated cost will be recorded for every run so the final credits request can be justified from measured pilot costs instead of requesting the maximum amount by default.

## Planned public outputs

- case JSON Schema;
- failure taxonomy;
- at least twenty de-identified cases;
- execution harness and run-manifest format;
- deterministic validators;
- transparent scoring rubrics;
- pilot and regression reports;
- API cost report;
- privacy, limitations, and data-governance documentation;
- contribution guidelines.

## Maintainer context

I am an independent builder and long-term AI power user based in Taiwan. My work focuses on the gap between what an agent appears to understand in one response and what it reliably preserves across a multi-step, multi-tool workflow.

The project is practitioner-led and exploratory. It does not claim that the initial cases represent all Traditional Chinese users, and it does not present operator observations as universal scientific conclusions.

## Privacy and responsible publication

The repository will not publish private conversations, credentials, personal identifiers, secret values, or raw identifiable system logs.

Cases are rewritten as minimal synthetic reproductions of observed failure patterns. Evidence, interpretation, and inference are separated in reports. Ambiguous results are documented rather than silently converted into passes or failures.

## Current status

- formal repository name and root structure established;
- repository remains private pending publication review;
- schema drafted;
- taxonomy drafted;
- five pilot cases drafted;
- pilot execution pending;
- license selection pending;
- application not yet submitted.

## Fields to complete before submission

- selected open-source license;
- public visibility and release review;
- pilot result link;
- measured token and cost estimate;
- contributor list, if any;
- exact amount of API credits requested.