---
name: literature-grounding
description: Grounds research ideas in literature by generating search queries, finding candidate papers, building a paper matrix, and identifying closest work. Use when prior work is unknown, novelty is uncertain, citations are needed, or the user asks whether anyone has done something.
---

# Literature Grounding

## Overview

Convert an idea into evidence by searching prior work, organizing papers, and identifying the closest work that threatens or supports the idea.

## When to Use

- The user asks “有没有人做过”, “查文献”, “找相关工作”, “找 baseline”, or “找 survey”
- A paper claim lacks citations
- Novelty is unknown
- Datasets, metrics, benchmarks, or baselines are needed

## Workflow

1. Read `idea.md` and any prior `literature-search.md`.
2. Generate 6-10 queries covering task, method, domain, dataset/benchmark, survey, closest-work, and collision-risk search.
3. Search in layers: surveys/benchmarks, recent papers, foundational papers, closest work, datasets, code.
4. Screen candidates into a matrix with task, method, data, relevance, novelty risk, and reuse value.
5. Identify closest works and state overlap, difference, risk, and required action.
6. Save or update paper notes and the literature-search artifact.

## Artifacts

- `ideas/<idea-id>/literature-search.md`
- `knowledge/papers/<paper-id>.md`
- `projects/<project-id>/literature/matrix.md`


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
