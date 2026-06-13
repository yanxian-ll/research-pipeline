---
name: research-project-management
description: Manages research projects as execution containers linked to ideas, papers, experiments, drafts, and logs. Use when creating projects, upgrading ideas to projects, tracking roadmap/progress, or deciding project status.
---

# Research Project Management

## Overview

A project is an execution container, not the starting point for every thought. Use it after an idea is scoped enough to act on.

## When to Use

- The user asks to create or switch projects
- An idea should become an executable project
- Roadmap, progress, blockers, or milestones need tracking

## Workflow

1. Decide whether the object is ready to be a project: question, output, owner, next action, and scope.
2. If not ready, keep it as an idea.
3. Create project structure with meta, direction, roadmap, literature, experiments, code, drafts, reviews, and progress. Record repository URL, remote, branch, and commit when code is linked.
4. Link active idea, relevant papers, framework, experiment plan, paper core, and decisions.
5. Maintain roadmap with milestones, success criteria, risks, next actions, and stop/pivot triggers.
6. Update progress with completed work, evidence/output, blocker, decision needed, and next action.

## Artifacts

- `projects/<project-id>/meta.md`
- `projects/<project-id>/direction.md`
- `projects/<project-id>/roadmap.md`
- `projects/<project-id>/progress.md`
- `projects/<project-id>/code/repository.md`


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
