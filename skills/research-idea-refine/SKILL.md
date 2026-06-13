---
name: research-idea-refine
description: Refines raw research ideas into sharp, testable research questions and one-page idea artifacts. Use when an idea is vague, broad, overclaiming, or when the user asks whether a direction can become a paper.
---

# Research Idea Refine

## Overview

Turn a raw research idea into a clear research question with assumptions, scope, risks, variants, and next validation steps.

## When to Use

- The user says “我有个 idea”, “帮我分析这个想法”, or “这个方向能不能做成论文”
- The idea is only a topic, not a question
- The project is being created before the idea is scoped

## Workflow

1. Restate the idea as a concise research question.
2. Extract domain, task, method, data, contribution type, and target audience/venue.
3. State assumptions explicitly.
4. Generate 3-5 distinct variants using task, method, data, evaluation, and story lenses.
5. Score variants by value, feasibility, novelty risk, evidence needed, and recommendation.
6. Converge to one recommended direction or mark as `needs-literature`.
7. Create or update `ideas/<idea-id>/idea.md` with raw idea, question, assumptions, not-doing list, risks, evidence needed, and next actions.

## Artifacts

- `ideas/<idea-id>/idea.md`
- `ideas/<idea-id>/discussion.md` when interactive


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
