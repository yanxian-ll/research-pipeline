---
name: paper-deep-reading
description: Performs source-grounded, problem-first close reading of an academic paper by reconstructing its starting point, prior paradigm, observed failure, core contradiction, design constraints, method derivation, evidence chain, and unresolved questions. Use when the user asks to 精读/深读/深入解读 a paper, understand why a method was proposed, trace how each module follows from the problem, inspect figures/tables/ablations, request reproduction-level analysis, prepare for technical discussion, or produce detailed paper notes rather than a summary or broad survey.
---

# Paper Deep Reading

## Overview

Reconstruct the paper's reasoning instead of following its section order. Start
from the world before the paper existed, derive why the proposed design was a
reasonable response, and audit whether experiments actually support that
response.

## When to Use

- The user asks for a close, deep, critical, or problem-first reading.
- The user asks why the paper exists or how the method was derived.
- A paper must be understood well enough for reproduction, presentation,
  framework design, or technical discussion.
- Figures, tables, equations, ablations, and appendices must be connected into
  one evidence chain.

Use `paper-reading-and-synthesis` for concise summaries, paper comparisons, and
topic surveys. Use `literature-grounding` when the primary goal is novelty,
closest-work, baseline, or citation search for a named idea or project.

## Workflow

### 1. Fix Scope and Evidence

1. Classify the reading as independent or explicitly idea/project-linked.
2. Verify title, version, venue, authors, source, code, and supplementary
   material using primary sources.
3. State what was actually available: full text, appendix, code, abstract only,
   or inaccessible material.
4. Read the introduction, related work, method, experiments, ablations,
   limitations, and relevant appendix before claiming a full reading.

### 2. Reconstruct the Starting Point

Answer these questions before explaining the proposed method:

1. **Target capability:** What should an ideal system do?
2. **Prior paradigm:** What did the field normally do before this paper?
3. **Concrete failure:** On what data, geometry, scale, cost, or assumption
   does that paradigm fail?
4. **Why the obvious fix is insufficient:** What tempting solution does not
   resolve the failure, and why?
5. **Core contradiction:** Which two desirable properties appear incompatible?
6. **Design constraints:** What must a valid solution preserve, avoid, or make
   efficient?

Separate author-stated motivation from reconstructed interpretation. If the
paper provides no direct evidence for a claimed failure, label it as a premise
or hypothesis.

### 3. Derive the Method

Build a problem-to-design map:

| Problem or constraint | Required capability | Proposed mechanism | Expected observable effect |
|---|---|---|---|

For every major module:

1. Identify the exact failure or constraint it addresses.
2. Explain inputs, outputs, representation, coordinate frame, and information
   flow.
3. Explain why this mechanism is preferable to a simpler alternative.
4. State what would break if the module were removed.
5. Classify it as core innovation, enabling component, inherited baseline, or
   implementation detail.

Do not present architecture order as causal reasoning. A component that cannot
be tied back to the starting problem is not automatically a contribution.

### 4. Trace Supervision and Inference

Audit:

- training data, labels, pseudo-labels, priors, frozen modules, and leakage;
- objectives and what behavior each loss can actually enforce;
- train/inference mismatch;
- preprocessing, post-processing, alignment, retrieval, optimization, or
  external sensors required at inference;
- coordinate systems, scale assumptions, normalization, and gauge freedoms;
- computational cost and scaling variable.

For equations, explain symbols, physical meaning, optimization target, and the
assumption that makes the equation valid. Do not merely paraphrase notation.

### 5. Audit the Evidence Chain

For each principal claim, record:

| Claim | Evidence | Metric/protocol | What it supports | What it does not support |
|---|---|---|---|---|

Check:

- whether the baseline isolates the claimed novelty;
- whether metrics measure the target capability directly or through alignment;
- whether ablations test necessity, interaction, and alternative explanations;
- whether qualitative examples are representative or selected;
- whether generalization crosses datasets, domains, scales, or only scenes;
- whether efficiency comparisons use comparable hardware and settings;
- whether limitations contradict broad wording in the abstract or conclusion.

Explain every central figure and table by stating the question it answers, the
comparison to inspect, the result, and the remaining ambiguity.

### 6. Rebuild the Paper in One Causal Chain

Produce a concise chain:

```text
desired capability
-> prior paradigm
-> observed failure
-> core contradiction
-> design constraints
-> proposed mechanism
-> training signal
-> experimental test
-> supported conclusion
-> unresolved boundary
```

If any arrow is unsupported, mark the gap instead of smoothing it over.

### 7. Extract Reusable Understanding

Conclude with:

- strongest supported contribution;
- contribution that is mainly engineering or presentation;
- hidden assumptions and likely failure cases;
- minimum reproduction recipe;
- most informative ablation to rerun;
- follow-up questions suggested by the paper itself.

Add implications for an idea or project only when the user explicitly requests
that linkage.

## Artifacts

Independent:

- `knowledge/papers/<paper-id>-deep-read.md`
- `reviews/<paper-id>-deep-read.md`

Idea/project-linked:

- `ideas/<idea-id>/literature/<paper-id>-deep-read.md`
- `projects/<project-id>/literature/papers/<paper-id>-deep-read.md`

Use `templates/paper-deep-reading.md` from the research pipeline when creating
the artifact.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "The abstract states the motivation." | The starting point requires the prior paradigm, concrete failure, contradiction, and constraints. |
| "Listing modules explains the method." | A close reading must show why each module follows from a specific problem. |
| "The benchmark improved, so the claim is proved." | The metric and alignment protocol may measure a weaker capability. |
| "The appendix is optional." | Critical supervision, implementation, and ablation details often live there. |
| "A project implication is obviously useful." | Independent reading remains independent unless linkage is requested. |

## Red Flags

- Starting with architecture before establishing the problem.
- Repeating introduction rhetoric without locating supporting evidence.
- Treating all modules as equally novel.
- Ignoring coordinate frames, alignment, external inputs, or post-processing.
- Reporting headline numbers without protocol and units.
- Calling an ablation causal when multiple factors change together.
- Claiming full-paper reading from an abstract or metadata page.
- Inventing project implications for independent reading.

## Verification

- [ ] Paper identity, version, and available sources are recorded
- [ ] The starting point includes prior paradigm, failure, contradiction, and constraints
- [ ] Every major method component maps to a problem or is labeled implementation detail
- [ ] Training, inference, coordinate frames, scale, and post-processing are explicit
- [ ] Main claims map to figures, tables, metrics, or ablations
- [ ] Evidence limits and alternative explanations are stated
- [ ] The causal chain contains no silently unsupported arrow
- [ ] Artifact scope and location are correct
- [ ] The next reading or reproduction action is concrete
