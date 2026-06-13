---
name: research-framework-design
description: Designs a research framework from a grounded idea by defining question, hypothesis, key insight, modules, baseline differences, and failure modes. Use when moving from gap analysis to method design or paper storyline.
---

# Research Framework Design

## Overview

Convert a defensible gap into a coherent method or conceptual framework that can support experiments and paper writing.

## When to Use

- The user asks for “技术路线”, “方法框架”, or “论文主线”
- Experiments cannot be planned because the method is unclear
- The method has modules but no hypothesis

## Workflow

1. Define the research contract: question, hypothesis, key insight, claim boundary, and non-claims.
2. Design modules with purpose, input, output, mechanism, why needed, and evidence required.
3. Map differences from baselines to required experiments.
4. Identify failure modes such as false assumptions, dataset overfit, weak baselines, data leakage, or overly broad story.
5. Create a figure plan that communicates the key insight, not just boxes.
6. Create or update `framework.md`.

## Artifacts

- `ideas/<idea-id>/framework.md`


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
