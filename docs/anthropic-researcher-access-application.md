# Anthropic External Researcher Access Program — application draft

## Purpose

This document is a ready-to-adapt application draft for Anthropic's External Researcher Access Program. It intentionally excludes private account identifiers, personal email addresses, API keys, and Claude Console organization IDs.

## Applicant

**Name:** Wang Shijun (Edgar)  
**Role:** Independent practitioner-researcher and primary maintainer  
**Location:** Taiwan  
**Affiliation:** Independent  
**Project:** `zh-tw-agent-reliability`  
**Repository:** https://github.com/edgarstool/zh-tw-agent-reliability

## Research title

**Structured Context and Human-Control Boundaries for Long-Horizon Agent Reliability in Traditional Chinese Workflows**

## Short research summary

I am studying observable reliability and alignment-relevant failures in long-horizon AI-agent workflows conducted in Traditional Chinese. The project converts de-identified practitioner-observed incidents into reproducible evaluation cases covering context retention, instruction persistence, tool selection, completion integrity, recovery behavior, and preservation of human control.

The public pilot currently contains five cases, three context conditions, deterministic validators, a manual 0–2 rubric, prompt hashing, a versioned run-manifest format, and a no-API structural smoke path. The planned primary experiment is a 90-run matrix: five cases × three context conditions × three repetitions × two model configurations.

## Research question

Do structured persistent context and explicit human-control boundaries reduce observable reliability and alignment-relevant failures in long-horizon Traditional Chinese agent workflows, compared with minimal or compact natural-language context?

## Why this is relevant to AI safety and alignment

The project focuses on behaviors that directly affect whether a human operator can reliably supervise an agent over extended workflows:

- preserving previously established constraints and operator intent;
- avoiding unsupported claims of completion when required validation did not occur;
- selecting the correct tool, shell, or execution environment;
- recovering visibly when browser or tool automation fails rather than silently fabricating success;
- preserving meaningful human approval boundaries without excessive approval fragmentation;
- remaining robust to noisy Traditional Chinese input and continued-task context.

These are not jailbreak or adversarial policy-bypass tests. The aim is to measure ordinary agent behavior under realistic multi-tool conditions where oversight, truthful completion, and recoverability matter.

## Method

The pilot uses five de-identified, synthetic or minimally reconstructed cases derived from practitioner-observed failure patterns. Each case is evaluated under three context conditions:

1. **Minimal:** only the immediate task.
2. **Compact:** a short natural-language reminder of important constraints.
3. **Structured:** explicit environment, tool, constraint, and completion requirements.

For each approved model response, the harness records the prompt format and hash, model configuration, response provenance, deterministic validator evidence, manual-rubric state, token usage, estimated cost, and explicit final state. Observations, interpretations, and broader inferences are kept separate.

The initial primary matrix is 5 cases × 3 context conditions × 3 repetitions × 2 model configurations = 90 runs. A smaller calibration batch will be run first before releasing the full matrix.

## Why Claude API access is needed

Claude API credits would be used to execute controlled, reproducible model runs against the existing evaluation cases. API access is important because the study needs stable recording of model configuration, exact prompts, response provenance, token usage, and repeatable execution conditions rather than manually copied chat sessions.

The credits would fund the pilot itself, not product traffic, private conversations, unrelated development, or unreviewed benchmark claims.

## Requested support

I am requesting support through Anthropic's standard External Researcher Access allocation. If approved, the credits will be used for the calibration batch, the primary pilot matrix, and limited regression reruns required to verify the evaluation harness and findings.

No claim is made that the project requires more than the standard allocation.

## Existing evidence and readiness

The repository is already public and Apache-2.0 licensed. It contains:

- five de-identified pilot cases;
- JSON Schema validation;
- deterministic validators;
- a Python execution harness;
- a versioned run-manifest schema;
- prompt hashing and response provenance fields;
- a no-API smoke path covering all five cases under all three context conditions;
- privacy and contribution rules;
- a pilot report skeleton and publication-readiness review.

No paid model measurements, token/cost measurements, or 90-run benchmark results are claimed yet. The purpose of the requested credits is to execute that measured pilot reproducibly.

## Expected public outputs

If the pilot is completed, the intended public outputs are:

- the de-identified evaluation cases and schemas;
- the evaluation harness and validators;
- reproducible run manifests without secrets or private source material;
- a pilot report with per-case results and limitations;
- measured token/cost information where appropriate;
- practical observations about context structure, operator control, truthful completion, and recovery behavior in Traditional Chinese agent workflows.

## Privacy and research integrity

The project does not publish raw private conversations, credentials, personal identifiers, secret values, private service URLs, real IP addresses, or identifiable system logs. Practitioner-observed incidents are rewritten into minimal synthetic or de-identified reproductions before publication.

The reporting standard distinguishes observation, interpretation, and inference. Ambiguous outcomes remain ambiguous instead of being converted into unsupported passes or failures.

## Team

This is currently a single-maintainer independent research project led by Wang Shijun (Edgar) in Taiwan. External contributions may be accepted through the public repository under the project's privacy and evidence rules.

## Form-only information

Fill these directly in Anthropic's form or Claude Console. **Do not commit them to the public repository:**

- contact email;
- Claude Console organization ID;
- any account-specific identifiers;
- any API key or billing information.

## Concise version for a short free-text field

I am an independent practitioner-researcher in Taiwan studying long-horizon AI-agent reliability in Traditional Chinese. My public Apache-2.0 project converts de-identified real-world failure patterns into reproducible evaluations of context retention, instruction persistence, tool choice, truthful completion, recovery, and human-control boundaries. The current pilot has five cases, three context conditions, deterministic validators, prompt hashing, run manifests, and a no-API smoke path. Anthropic API credits would fund a controlled calibration batch and a planned 90-run pilot, with results, limitations, token/cost evidence, and de-identified manifests published openly. The work is not jailbreak research; it focuses on ordinary agent oversight, recoverability, and completion integrity.