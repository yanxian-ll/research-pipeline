---
name: using-research-skills
description: Discovers and invokes research workflow skills while deciding whether work is independent, idea-linked, or project-linked. Use when starting a research session or routing work across paper reading, literature grounding, GitHub repositories, code-to-idea extraction, novelty analysis, framework design, experiments, writing, logs, review, publication, or submission.
---

# Using Research Skills

## Overview

Route work first by ownership scope, then by lifecycle stage and starting
artifact. Researcher-level reading and summaries do not automatically belong to
the most recently discussed project.

## When to Use

- Starting a research session
- Starting from an existing local or GitHub repository
- A request spans multiple research activities
- The next workflow is unclear

## Workflow

1. Classify scope as independent, idea-linked, or project-linked.
2. Treat generic paper reading, topic surveys, and researcher-level logs as
   independent by default.
3. Link work to an idea or project only when the user names it, requests
   implications for it, or provides an object-local path.
4. Conversation proximity, current working directory, or the existence of an
   active project is not sufficient evidence of linkage.
5. If ambiguity changes the output location or analysis, ask one concise scope
   question. Otherwise proceed independently.
6. Identify the starting object: paper/topic, repository, raw idea, framework,
   experiments, draft, or submission.
7. Map the task to: read/synthesize, acquire, extract/define, ground, frame,
   verify, write, review, publish/submit.
8. Use `paper-deep-reading` for 精读/深读, problem-first explanation,
   method derivation, figure/table/ablation auditing, or reproduction-level
   understanding of one paper.
9. Use `paper-reading-and-synthesis` for concise summaries, comparisons, and
   topic surveys.
10. Use `literature-grounding` when literature is being used to assess a named
   idea or project's novelty, baselines, claims, or experiment design.
11. For GitHub acquisition or publication, use
    `github-repository-operations`; default clones to `--depth=1`.
12. For existing code, use `code-to-research-idea`, then
    `literature-grounding` and `gap-and-novelty-review` before asserting
    novelty.
13. For a Method section grounded in implementation, use
    `research-method-writing`; use `evidence-based-writing` for other
    evidence-grounded sections.
14. State the selected scope, skill sequence, and assumptions.
15. Create or update the smallest useful artifact in the matching scope.
16. End with verification and the next smallest action.

## Artifacts

- No mandatory artifact
- Optional `active-context.md` or `context-packet.md`

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "This is obvious." | Research decisions still need artifacts and acceptance criteria. |
| "We can fill evidence later." | Evidence changes the claim boundary. Label provisional content. |
| "The code proves the paper." | Code supports implementation claims, not novelty or effectiveness by itself. |
| "One skill should do everything." | Compose only the stages needed for the current task. |
| "We were just discussing a project." | Nearby context does not authorize linking an independent reading task to that project. |

## Red Flags

- Confident claims without evidence
- Novelty asserted before closest-work search
- Code claims without file or symbol anchors
- No artifact created or updated
- Missing next action
- Repository operations without credential or sensitive-file checks
- Independent paper notes written into a project
- Unrequested "implications for the active project" sections

## Verification

- [ ] Scope is classified as independent, idea-linked, or project-linked
- [ ] The starting object and active artifact are named
- [ ] Artifact location matches the scope
- [ ] Facts, hypotheses, plans, and code inferences are separated
- [ ] Evidence gaps are labeled
- [ ] The selected skill sequence matches the lifecycle
- [ ] The next action is concrete and small
