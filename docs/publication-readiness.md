# Publication-readiness report — v0.1

**Review date:** 2026-08-09
**Scope:** README, CONTRIBUTING, schemas, five pilot cases, documentation, tests, manifests/examples, generated files, and tracked repository history reachable from `master`.

## DONE

- [x] The tracked repository was reviewed for credential-shaped values, secrets, private hostnames, IPv4 addresses, private conversation exports, raw system logs, private repository references, and local-only paths.
- [x] No secret values, API keys, credentials, recovery codes, private hostnames, IP addresses, raw conversations, or identifiable logs were found in the reviewed files.
- [x] The one path-pattern case that used a real local workspace path was rewritten to use generic example paths (`C:\\example-workspace\\projects` and `D:\\deprecated-example`).
- [x] The five pilot cases are de-identified, validate against `schema/case.schema.json`, and state `contains_secrets: false`.
- [x] No generated run manifests, raw responses, build artifacts, virtual environments, or Python bytecode are tracked. `.gitignore` excludes those classes of files.
- [x] Intentional maintainer identity is limited to Wang Shijun (Edgar), Taiwan, and the public GitHub username/repository URL in the README and application draft.
- [x] Apache-2.0 was selected as one repository-wide, permissive license for code, schemas, de-identified cases, and documentation; no custom restrictions or ambiguous dual-license boundary is used.
- [x] Documentation now distinguishes verified local harness evidence from pending model measurements, token/cost measurements, 90-run execution, and adoption evidence.

## PENDING — deliberately not performed

- [ ] Make the GitHub profile public if required by the application form.
- [ ] Change the GitHub repository visibility from private to public.
- [ ] Retrieve the OpenAI Organization ID from the account and enter the applicant name and ChatGPT-account email in the form.
- [ ] Review and accept the current Codex for Open Source Program Terms, then submit the form.
- [ ] Run any paid model/API evaluation, including the proposed 90-run matrix.

## Findings and limits

The review is a repository-content review, not a claim that the future public GitHub UI, account profile, Git history outside this repository, or third-party dependencies have been audited. The repository intentionally contains no sample raw response or generated manifest because those would need a separate privacy review before publication.

`docs/open-source-fund-application.md` holds ready-to-paste text for the official form. It avoids claims of real model outcomes, token costs, broad adoption, or measured 90-run results.
