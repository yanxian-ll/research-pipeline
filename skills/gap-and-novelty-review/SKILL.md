---
name: gap-and-novelty-review
description: Analyzes literature evidence to identify research gaps, novelty risk, and go/pivot/stop decisions. Use when deciding whether an idea is worth pursuing or when turning related work into a contribution claim.
---

# Gap And Novelty Review

## Overview

Turn a literature matrix into a defensible gap and a decision: go, pivot, stop, or search more.

## When to Use

- The user asks “创新点在哪里”, “这个 idea 值不值得做”, or “找 gap”
- Closest works exist and need comparison
- Contribution claims need support

## Workflow

1. Reconstruct the research map by grouping prior work into directions.
2. Compare closest works against the proposed idea using similarity, difference, risk, and required action.
3. Classify candidate gaps: problem, method, data, evaluation, system, theory, application, and writing/story gap.
4. Assess feasibility: data, engineering, experiment cost, writing difficulty, venue fit.
5. Decide Go, Pivot, Stop, or Need More Literature.
6. Create or update `gap-analysis.md` with the decision and next actions.

## Artifacts

- `ideas/<idea-id>/gap-analysis.md`


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
