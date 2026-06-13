---
name: literature-grounding
description: Grounds an explicitly identified research idea or project in literature by generating search queries, finding candidate papers, building a paper matrix, and identifying closest work. Use when novelty, related work, baselines, citations, datasets, or experiment design are needed for a named idea, project, manuscript, or repository. For independent paper reading, summaries, comparisons, or topic surveys, use paper-reading-and-synthesis instead.
---

# Literature Grounding

## Overview

Convert a named idea or project into evidence by searching prior work,
organizing papers, and identifying the closest work that threatens or supports
its claims. This is not the default workflow for independent reading.

## When to Use

- The user asks “有没有人做过”, “查文献”, “找相关工作”, “找 baseline”, or “找 survey”
- A paper claim lacks citations
- Novelty is unknown
- Datasets, metrics, benchmarks, or baselines are needed

## Workflow

1. Confirm the named idea, project, manuscript, or repository being grounded.
2. If none is named and the request is only to read or survey papers, hand off
   to `paper-reading-and-synthesis`.
3. Read `idea.md`, project direction, or the relevant manuscript claim and any
   prior `literature-search.md`.
4. Generate 6-10 queries covering task, method, domain, dataset/benchmark,
   survey, closest-work, and collision-risk search.
5. Search in layers: surveys/benchmarks, recent papers, foundational papers,
   closest work, datasets, code.
6. Screen candidates into a matrix with task, method, data, relevance, novelty
   risk, and reuse value.
7. Identify closest works and state overlap, difference, risk, and required
   action.
8. Save or update paper notes and the literature-search artifact inside the
   named idea or project.

## Artifacts

- `ideas/<idea-id>/literature-search.md`
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
- No named idea/project, but project-grounding analysis is still performed
- Independent summaries polluted with unsolicited novelty or project sections
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
