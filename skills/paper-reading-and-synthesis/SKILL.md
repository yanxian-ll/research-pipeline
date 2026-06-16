---
name: paper-reading-and-synthesis
description: Reads, summarizes, compares, and synthesizes academic papers as an independent research activity or within an explicitly named project. Use for concise paper summaries, multi-paper comparisons, method-family explanations, reading notes, and topic surveys. Use paper-deep-reading instead when the user asks for 精读/深读, problem-first method derivation, detailed figure/table/ablation analysis, or reproduction-level understanding. Default to independent artifacts unless explicitly linked to a project, idea, experiment, or manuscript.
---

# Paper Reading and Synthesis

## Overview

Produce concise, source-grounded paper notes, comparisons, and topic
syntheses. Preserve independent research scope unless the user explicitly
links the reading to an idea or project.

## When to Use

- Summarizing one or more papers without reproduction-level detail.
- Comparing methods on a consistent matrix.
- Explaining a paper family or writing a topic survey.
- Recording independent literature in a research log.

Use `paper-deep-reading` when the request requires a problem-first causal
reconstruction, detailed figures/tables/ablations, or reproduction guidance.

## Scope Decision

Classify the request before reading or writing.

### Independent

Use independent scope when the user asks to:

- read, explain, summarize, or compare papers;
- survey a topic, company, laboratory, or method family;
- collect general background knowledge;
- add literature reading to a researcher-level daily log.

The existence of an active or recently discussed project is not sufficient to
make the task project-linked.

### Project-linked

Use project scope only when the user:

- names a project, idea, experiment, manuscript, or repository;
- says the papers are for related work, novelty, baselines, method design, or
  experiments of that object;
- asks what the papers imply for that object;
- provides a project-local output path.

Do not add a "relevance to project" section to independent notes.

### Ambiguous

If both interpretations are plausible and the choice changes the artifact
location or analysis, ask one concise scope question. If the task can proceed
without that decision, create an independent artifact and leave it unlinked.

## Workflow

1. State whether the reading is independent or project-linked.
2. Verify paper identity using primary sources.
3. Read the abstract, method, training, experiments, ablations, limitations, and
   appendices relevant to the request.
4. Separate paper claims, verified design facts, author interpretation, and your
   synthesis.
5. For multiple papers, compare them on a consistent matrix rather than writing
   disconnected abstracts.
6. Record uncertainty for unverified project names, unpublished systems, or
   company announcements.
7. Write to the artifact location determined by scope.

For problem-first close reading of one paper, hand off to
`paper-deep-reading`; do not stretch this summary workflow into a section-by-
section pseudo-deep-read.

## Artifacts

Independent:

- `knowledge/papers/<paper-id>.md`
- `knowledge/topics/<topic-id>.md`
- `reviews/<topic-id>.md`

Project-linked:

- `projects/<project-id>/literature/papers/<paper-id>.md`
- `projects/<project-id>/literature/matrix.md`
- a manuscript section only when explicitly requested

Daily reading can also be recorded in `logs/daily/YYYY-MM-DD.md`, under an
independent literature section unless it was explicitly project-linked.

## Reading Note Structure

- Citation and source
- Research question
- Problem and assumptions
- Method and architecture
- Training data and objectives
- Evaluation protocol
- Main findings
- Ablations
- Limitations and evidence strength
- Cross-paper synthesis, when applicable

Include project implications only for project-linked scope.

## Guardrails

- Do not infer project relevance merely from conversation proximity.
- Do not turn every paper summary into an idea or novelty analysis.
- Do not create or modify project files for an independent reading request.
- Do not treat company marketing material as equivalent to a paper.
- Do not claim a paper was fully read when only metadata or an abstract was
  available.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "Nearby project context implies linkage." | Independent reading stays independent unless linkage is explicit. |
| "More detail always improves a summary." | Use `paper-deep-reading` when causal reconstruction is required. |
| "The abstract is enough." | Method, experiments, and limitations are needed for verified paper notes. |
| "Separate mini-summaries form a comparison." | Multi-paper work needs a shared comparison matrix. |

## Red Flags

- Writing project implications for an independent request.
- Comparing papers with inconsistent dimensions.
- Treating author claims as verified findings.
- Hiding unavailable full text or appendices.
- Using this skill for a requested deep reading.

## Verification

- [ ] Scope is explicitly classified
- [ ] Artifact location matches the scope
- [ ] Paper identity and source are verified
- [ ] Summary distinguishes facts from synthesis
- [ ] Independent notes contain no unsolicited project analysis
