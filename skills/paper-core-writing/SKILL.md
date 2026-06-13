---
name: paper-core-writing
description: Creates the paper core: one-sentence pitch, problem, motivation, insight, contributions, abstract, outline, and writing risks. Use when turning a grounded research plan into a paper structure.
---

# Paper Core Writing

## Overview

Turn an idea, gap, framework, and experiment plan into the paper spine that guides section drafting.

## When to Use

- The user asks “把这个 idea 变成论文”, “写 abstract”, or “生成论文主线”
- Contributions or outline are unclear
- Writing begins before claims are coherent

## Workflow

1. Check inputs: idea, literature search, gap analysis, framework, experiment plan, and results if available.
2. Label missing inputs as provisional rather than inventing them.
3. Write the paper spine: pitch, problem, motivation, gap, insight, method, contributions, evidence plan/results, limitations, target venue fit.
4. Map each contribution to gap, method module, empirical evidence, or resource artifact.
5. Draft abstract, introduction logic, section outline, figure/table plan, and writing risks.

## Artifacts

- `ideas/<idea-id>/paper-core.md`
- `projects/<project-id>/drafts/outline.md`


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
