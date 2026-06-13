---
name: research-method-writing
description: Writes a publication-ready paper Method section from code, framework, experiment plans, and verified implementation evidence. Use when Codex must explain an implemented method, convert repository architecture into equations or pseudocode, align prose with actual code, define notation and objectives, or revise a Method section without inventing behavior.
---

# Research Method Writing

## Overview

Write a reproducible Method section whose technical claims trace to code or an explicitly labeled design plan.

## When to Use

- Existing code must be described as a paper method
- A framework needs notation, equations, algorithms, or implementation detail
- A draft Method section may disagree with the implementation

## Workflow

1. Read the idea, code evidence map, framework, literature matrix, experiment plan, and target venue constraints.
2. Define the method contract: problem formulation, inputs, outputs, assumptions, notation, and scope.
3. Build a method-to-code map for every module, objective, training stage, inference stage, and implementation detail.
4. Structure the section as overview, formulation, modules, objectives, optimization or algorithm, inference, complexity, and implementation details.
5. Derive equations only when supported by code or author-provided design. Mark conceptual formulas and unresolved details as provisional.
6. Explain why each module exists and how it differs from verified baselines; leave novelty judgments to the literature and gap artifacts.
7. Draft figure or pseudocode requirements and a reproducibility checklist.
8. Audit the draft against code, configs, tensor shapes, defaults, and experiment settings.

## Artifacts

- `projects/<project-id>/drafts/method.md`
- `projects/<project-id>/drafts/method-code-map.md`
- Optional `projects/<project-id>/drafts/algorithm.md`

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "A plausible equation is good enough." | Equations must match implemented computation or be labeled conceptual. |
| "Implementation details belong only in code." | Readers need enough detail to reproduce the method. |
| "Novelty can be stated in the Method section." | Novelty claims require closest-work evidence. |
| "Module names explain their purpose." | Explain mechanism, role, and interactions explicitly. |

## Red Flags

- Invented equations, losses, schedules, or architectural behavior
- Method prose that conflicts with defaults or configs
- Undefined symbols or inconsistent tensor dimensions
- Uncited borrowed mechanisms
- Mixing experimental results into method description
- Hiding missing implementation evidence

## Verification

- [ ] Each technical claim maps to code or a labeled design assumption
- [ ] Notation and dimensions are consistent
- [ ] Training and inference procedures are covered
- [ ] Borrowed components are identified for citation
- [ ] Reproducibility gaps and unresolved questions are listed
