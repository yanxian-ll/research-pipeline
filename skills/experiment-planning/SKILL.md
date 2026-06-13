---
name: experiment-planning
description: Creates verifiable experiment plans with hypotheses, datasets, baselines, metrics, ablations, robustness checks, and risk mitigation. Use before running experiments or writing empirical claims.
---

# Experiment Planning

## Overview

Design experiments that can prove or falsify the research claims before results are interpreted or written.

## When to Use

- The user asks “怎么验证”, “设计实验”, or “规划 ablation”
- A framework exists but claims are untested
- A paper draft needs experiment structure

## Workflow

1. Map each claim to a hypothesis, evidence needed, and failure interpretation.
2. Select datasets and explain purpose, access, preprocessing, limitations, and claim relevance.
3. Select baselines including strongest current method, standard baseline, closest-work baseline, and simple baseline.
4. Define metrics that match the claims.
5. Plan ablations for every method module or explain why isolation is impossible.
6. Plan robustness/generalization and qualitative analysis when claimed.
7. Name expected failure modes, fallback experiments, minimum publishable evidence, and stopping conditions.

## Artifacts

- `ideas/<idea-id>/experiment-plan.md`
- `projects/<project-id>/experiments/plans/*.md`


## Common Rationalizations

| Rationalization | Reality |
|---|---|
| “This is obvious.” | Obvious research decisions still need artifacts and acceptance criteria. |
| “We can fill evidence later.” | Evidence changes the claim boundary; defer it only when labeled provisional. |
| “The user wants confidence.” | The user needs useful truth. Surface risks and tradeoffs. |
| “This step slows us down.” | A small gate now prevents expensive rework later. |

## Red Flags

- Confident claims without evidence
- No artifact created or updated
- Missing next action
- Scope expands beyond the user’s request
- Weaknesses hidden instead of tracked
- Decisions not traceable to literature, experiments, code, or logs

## Verification

- [ ] The active artifact is named
- [ ] Known facts, hypotheses, and plans are separated
- [ ] Assumptions are surfaced when needed
- [ ] Evidence gaps are labeled
- [ ] Next action is concrete and small
