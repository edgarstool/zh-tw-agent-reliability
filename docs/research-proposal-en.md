# Traditional Chinese Long-Horizon Agent Reliability

## Practitioner-led pilot study proposal

### Background

I am an independent Traditional Chinese AI systems operator based in Taiwan. I work with long-running workflows that combine Windows and PowerShell, coding agents, browser agents, GitHub repositories, MCP tools, cloud services, and human approval gates.

Through repeated real-world use, I have observed failures that are not well represented by short, isolated benchmarks. These include loss of previously established constraints across sessions, incorrect tool or shell selection, premature claims of completion, excessive task fragmentation, and failures to preserve operator intent in noisy Traditional Chinese input.

### Research question

How can real-world Traditional Chinese agent workflow failures be converted into reproducible evaluations of context retention, instruction persistence, tool selection, completion integrity, recovery behavior, and operator correction burden?

### Scope

This pilot focuses on long-horizon agent workflows in which a human operator coordinates multiple tools and agents. It does not claim broad population-level conclusions. It uses a practitioner-led case-study approach supported by structured incident records and a small repeated-task benchmark.

### Existing foundation

I have already built and maintained:

- A cross-agent knowledge and rule layer for preserving canonical constraints and recent operational context.
- A desktop operator interface for controlling models, agents, sessions, tools, scheduled jobs, and recovery actions.
- A multi-tool MCP environment connecting coding agents, browser workflows, Git operations, local systems, and cloud services.
- Versioned project records, automated tests, smoke tests, incident notes, and repair protocols.

### Method

1. Define a Traditional Chinese agent failure taxonomy.
2. Publish at least 20 de-identified reproducible cases.
3. Build a small benchmark comparing minimal, natural-language, and structured-context conditions.
4. Measure task completion, rule violations, human corrections, validation success, recovery behavior, and failure type.
5. Document limitations caused by operator involvement and rubric-based judgment.
6. Publish the dataset, evaluation criteria, pilot results, and practical recommendations.

### Requested support

I am requesting OpenAI API credits to build, run, and document reproducible evaluations of Traditional Chinese long-horizon agent workflows.

### Research integrity

This project will not publish private conversations, credentials, personal identifiers, secret values, or raw system logs. Cases will be manually anonymized and rewritten into minimal reproducible examples. Observed evidence, interpretation, and inference will be reported separately.
