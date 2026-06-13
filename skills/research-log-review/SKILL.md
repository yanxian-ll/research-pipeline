---
name: research-log-review
description: Maintains researcher-level daily, weekly, monthly, and decision logs with explicit separation between independent literature/work and project- or idea-linked activity. Use when recording progress, paper reading, reviewing a week, extracting decisions, or summarizing cross-project and non-project work.
---

# Research Log Review

## Overview

Logs are researcher-level memory, not just project status. They capture project work, idea movement, literature insights, non-project work, decisions, blockers, and next actions.

## When to Use

- The user asks for daily, weekly, or monthly reports
- Work spans multiple projects or no project
- The user says logs should not always be project-related
- Research decisions need to be recorded

## Workflow

1. Choose log type: daily, weekly, monthly, or decision.
2. Classify each entry independently as unlinked, paper/topic-linked,
   idea-linked, or project-linked.
3. Default general paper reading, topic surveys, skill maintenance, and
   researcher administration to unlinked or paper/topic-linked.
4. Link an entry to a project only when the underlying task was explicitly
   project-linked. Do not inherit linkage from adjacent conversation turns.
5. Separate buckets: independent literature, project-linked work, idea-linked
   work, writing, experiment/code, administration, decisions, blockers, and
   next actions.
6. Do not add project implications to independent literature entries.
7. For weekly/monthly logs, extract repeated blockers, status changes, papers
   that changed direction, implicit decisions, outputs worth archiving, and
   next strategy while preserving original scope.
8. Create or update the correct log file.

## Artifacts

- `logs/daily/YYYY-MM-DD.md`
- `logs/weekly/YYYY-WXX.md`
- `logs/monthly/YYYY-MM.md`
- `logs/decisions/*.md`


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
- Independent reading silently attributed to the latest active project

## Verification

- [ ] The active artifact is named
- [ ] Every entry's linkage is justified by the originating task
- [ ] Known facts, hypotheses, and plans are separated
- [ ] Assumptions are surfaced when needed
- [ ] Evidence gaps are labeled
- [ ] Next action is concrete and small
