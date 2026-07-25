# Failure Taxonomy

The taxonomy is intentionally compact. A case may carry more than one category, but one category should be marked as primary.

## CTX — Context retention

Previously established facts, paths, decisions, or constraints are lost or replaced without evidence.

Examples:

- reverting to a deprecated path;
- forgetting the selected operating environment;
- ignoring an earlier decision that remains in force.

## INS — Instruction persistence

An explicit instruction is acknowledged but not preserved through later steps.

Examples:

- switching from PowerShell to Bash after the user specified Windows-native commands;
- violating a stated stop condition;
- changing scope without approval.

## TOOL — Tool and environment selection

The agent chooses an unsuitable shell, tool, interface, or execution environment.

Examples:

- giving Linux commands for a Windows-only task;
- using hidden browser automation when visible interaction is required;
- selecting a write-capable tool for a read-only request.

## CMP — Completion integrity

The agent claims success without sufficient evidence that required work or validation completed.

Examples:

- reporting tests as passed when the test runner was unavailable;
- treating partial output as full completion;
- omitting known blockers from the final status.

## REC — Recovery behavior

The agent fails to respond appropriately after an error, blocked tool, or changed environment.

Examples:

- repeating the same failed action;
- not switching to a human-assisted mode;
- discarding useful partial results after a recoverable failure.

## HCI — Human control and correction burden

The workflow creates unnecessary operator effort or obscures meaningful control points.

Examples:

- splitting a low-risk task into many approval steps;
- asking questions already answered in context;
- burying the one real decision inside procedural noise.

## LNG — Language and input robustness

The agent fails because of Traditional Chinese wording, voice-recognition noise, code-switching, or ambiguous local terminology.

Examples:

- interpreting a voice-recognition typo literally when context strongly indicates another term;
- losing technical constraints embedded in conversational Traditional Chinese;
- changing language unexpectedly during execution.

## Scoring dimensions

Each case may score the following dimensions from 0 to 2:

- **0 — Failure**: required behavior is absent or contradicted.
- **1 — Partial**: some requirements are met, but correction or clarification is still needed.
- **2 — Pass**: behavior satisfies the stated requirements with adequate evidence.

Dimensions:

- context retention;
- instruction persistence;
- tool selection;
- completion integrity;
- recovery quality;
- human control;
- language robustness.

Scores should be accompanied by observable evidence, not only a numeric judgment.
