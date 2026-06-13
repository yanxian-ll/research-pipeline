---
name: code-to-research-idea
description: Extracts defensible research ideas, hypotheses, contributions, and literature-search anchors from an existing codebase. Use when Codex must inspect a repository, infer what was implemented, distinguish code facts from hypotheses, or turn code into an idea artifact before literature review and paper writing.
---

# Code To Research Idea

## Overview

Turn an existing repository into a traceable research idea without treating implementation details as proof of novelty or effectiveness.

## When to Use

- The user has code but no clear paper idea
- A repository must be understood before literature search or method writing
- Claimed contributions must be traced to files, symbols, configs, tests, or experiment logs

## Workflow

1. Inspect the repository structure, README, dependencies, entry points, configs, tests, experiment scripts, log metadata, and git history when relevant.
2. Build a code evidence map for the task, inputs, outputs, algorithm, data flow, losses, preprocessing, evaluation, and distinctive choices.
3. Separate `Observed in code`, `Inferred intent`, `Unverified claim`, and `Missing evidence`.
4. Reconstruct the likely research question, hypothesis, mechanism, baseline differences, contribution type, and claim boundary.
5. Generate literature-search anchors from the task, method family, data, losses, architecture, evaluation protocol, and closest implementation patterns.
6. Produce 2-4 candidate paper ideas, score value, feasibility, novelty risk, and evidence readiness, then recommend one or mark `needs-literature`.
7. Update the code analysis and idea artifacts. Hand off to `literature-grounding`, then `gap-and-novelty-review`.

## Artifacts

- `projects/<project-id>/code/code-evidence.md`
- `ideas/<idea-id>/idea.md`
- Optional `projects/<project-id>/code/architecture.md`

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "The code is the contribution." | Code shows implementation, not novelty, correctness, or research value. |
| "The class name explains the method." | Names are hints; trace actual data flow and behavior. |
| "Results can be inferred from the model." | Empirical claims require logs or reproducible experiments. |
| "Similar code means similar papers." | Search and verify conceptual overlap. |

## Red Flags

- Describing unexecuted code as working
- Claiming novelty before closest-work search
- Ignoring configs, preprocessing, or evaluation code
- Missing file and symbol anchors
- Confusing third-party code with project-owned contributions
- Exposing secrets, private URLs, or sensitive data

## Verification

- [ ] Every code claim has a file, symbol, config, test, or log anchor
- [ ] Observations, inferences, and unverified claims are separated
- [ ] Third-party and project-owned code are distinguished
- [ ] Candidate ideas include novelty risks and evidence gaps
- [ ] Literature-search anchors and the next workflow are named
