---
name: research-critic-review
description: Performs adversarial review of ideas, literature grounding, gaps, frameworks, experiments, and paper drafts. Use before committing to a direction, submitting, or when a confident answer needs stress testing.
---

# Research Critic Review

## Overview

Act as a skeptical reviewer before real reviewers do, finding weak claims, missing evidence, novelty collisions, and unclear story early.

## When to Use

- The user asks “审稿人会怎么批评”, “帮我找问题”, or “这个能投吗”
- A paper core or draft is ready
- Novelty, experiments, or framing feel fragile

## Workflow

1. Classify the review target: idea, literature, gap, framework, experiments, or draft.
2. Use severity labels: Blocker, Major, Minor, Nit.
3. Ask fresh-reviewer questions: strongest rejection reason, closest paper attack, missing claim evidence, missing experiment, vague contribution, needed narrowing.
4. Create a revision plan with severity, issue, evidence, fix, and next action.
5. Give Go/No-Go or readiness decision.

## Artifacts

- `reviews/critic-review.md`
- `reviews/revision-plan.md`


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
