---
name: evidence-based-writing
description: Writes research paper sections with traceable claims, citation discipline, and evidence mapping. Use when drafting related work, experiments, results, discussion, limitations, or rebuttal content; use research-method-writing when a Method section must be reconstructed and audited against an existing codebase.
---

# Evidence Based Writing

## Overview

Write paper sections from evidence instead of confidence. Every important claim traces to literature, code, experiment, or a labeled hypothesis. Delegate code-aligned Method reconstruction to `research-method-writing`.

## When to Use

- Drafting related work, method, experiments, results, discussion, limitations, or rebuttal
- Revising unsupported or overclaimed writing
- Turning notes into publishable prose

## Workflow

1. Build an evidence map for central claims with evidence type, source, strength, and missing support.
2. Choose the section pattern: related work by concepts, method by modules, experiments by evidence, discussion by implication.
3. Draft with guardrails: avoid “first”, “novel”, or “SOTA” unless proven; separate observation from interpretation.
4. Attach citations or evidence sources where available.
5. End with unsupported claims, missing citations, missing experiments, weak transitions, and reviewer attack points.

## Artifacts

- `projects/<project-id>/drafts/*.md`
- Optional `evidence-map.md`


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
