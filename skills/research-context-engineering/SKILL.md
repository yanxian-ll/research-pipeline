---
name: research-context-engineering
description: Loads the right research context without flooding the agent. Use when a session spans many ideas, papers, projects, logs, or drafts, when output quality drops, or when context must be packed for another research workflow.
---

# Research Context Engineering

## Overview

Select the minimum useful context for the task so the agent does not mix projects, stale assumptions, or irrelevant papers.

## When to Use

- Multiple ideas or projects exist
- The user switches context
- The model starts repeating stale assumptions
- A downstream skill needs a context packet

## Workflow

1. Identify the task type and active object.
2. Load only the artifacts required by the task.
3. Build a context packet with active object, user goal, known facts, hypotheses, constraints, relevant artifacts, missing evidence, and next workflow.
4. Exclude unrelated projects, old logs, and full drafts unless needed.
5. Use the context packet as the input to the next skill.

## Artifacts

- `active-context.md`
- Optional `context-packet.md`


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
