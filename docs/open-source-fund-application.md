# Codex for Open Source application — ready-to-paste draft

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

The v0.1 pilot contains five de-identified draft cases. The repository includes local schema validation, a deterministic validator runner, prompt hashing, a versioned run-manifest format, and a no-API structural smoke path. It has not run model experiments or generated measured costs. Its public-release privacy review is complete and it is licensed under Apache-2.0.

## Why this project is useful

Public agent evaluations often emphasize isolated English-language tasks. They are less likely to represent workflows where a Traditional Chinese user coordinates Windows PowerShell, coding agents, browser tools, GitHub, MCP services, cloud systems, and human approval boundaries over many steps.

This project focuses on inspectable failure patterns rather than a single leaderboard score. Maintainers should be able to rerun a case, see exactly which requirement failed, and extend the dataset with new cases.

## Official form fields (each response is under 500 characters)

### Role

Primary maintainer

### Interest

API credits for my project

### Why does this repository qualify? — 478 characters

zh-tw-agent-reliability is a small, actively maintained open-source toolkit for reproducible evaluation of long-horizon AI-agent reliability in Traditional Chinese. It targets underrepresented multi-tool workflows—Windows/PowerShell, code repositories, browser verification, and human approval boundaries—using de-identified cases, transparent validators, and privacy-first contribution rules. The public v0.1 is a foundation, not a claim of broad adoption or benchmark results.

### How will you use API credits for your project? — 424 characters

API credits will fund reproducible pilot execution across five de-identified cases and minimal, compact, and structured context conditions; each approved run will record configuration, prompt hash, validator evidence, token usage, and estimated cost. Credits will also support regression maintenance as new cases and validators are contributed. No credits will be used for secrets, private logs, or unreviewed public claims.

### Anything else we should know? — 429 characters

I am the primary maintainer and will keep the project small, inspectable, and privacy-first. The repository has a deterministic local runner and no-API smoke path, but no paid model runs, 90-run matrix, token/cost measurements, or adoption claims yet. Results will be reported only after reproducible execution and evidence-based review. The immediate goal is a careful public pilot and a durable regression-maintenance workflow.

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
- repository intentionally remains private until the maintainer performs the final visibility action;
- schema drafted;
- taxonomy drafted;
- five pilot cases drafted;
- local executable pilot foundation implemented; no paid API execution performed;
- measured pilot execution pending;
- Apache-2.0 license selected and committed;
- privacy and publication review completed; no raw responses, secrets, private hostnames/IPs, private conversations, or actual local-only paths remain;
- application not yet submitted.

## Account-held fields and final submission prerequisites

- First name, last name, and the email associated with the ChatGPT account;
- OpenAI Organization ID (required by the form; not retrieved or stored by this repository);
- GitHub profile visibility set to public, if it is not already public;
- repository visibility changed to public;
- acceptance of the Codex for Open Source Program Terms and final Submit action.

No pilot result link, measured token/cost estimate, contributor list, or exact credit amount is asserted because none is required to be invented for this v0.1 application and no paid run has occurred.
