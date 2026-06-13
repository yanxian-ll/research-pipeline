# Research Agent Skills Router

Choose the smallest applicable workflow.

```text
Unsure which workflow applies?                 -> using-research-skills
Clone, create, or push a GitHub repository?    -> github-repository-operations
Extract a research idea from existing code?    -> code-to-research-idea
Refine a raw research direction?               -> research-idea-refine
Read, summarize, or compare papers?            -> paper-reading-and-synthesis
Ground a named idea/project in literature?     -> literature-grounding
Assess novelty or go/pivot/stop?                -> gap-and-novelty-review
Design the research framework?                 -> research-framework-design
Plan datasets, baselines, metrics, ablations?  -> experiment-planning
Write pitch, abstract, contributions, outline? -> paper-core-writing
Write a Method section aligned with code?      -> research-method-writing
Write other evidence-grounded sections?        -> evidence-based-writing
Maintain research logs?                        -> research-log-review
Manage roadmap and progress?                   -> research-project-management
Run adversarial review?                        -> research-critic-review
Prepare submission or rebuttal?                -> research-submission-readiness
```

## Global Rules

1. Do not invent papers, citations, results, code behavior, or repository state.
2. Separate known facts, code observations, inferences, hypotheses, and plans.
3. Treat novelty as unproven until closest-work search is complete.
4. Anchor code claims to files, symbols, configs, tests, or logs.
5. Distinguish third-party code from project-owned contributions.
6. Classify work as independent, idea-linked, or project-linked before choosing
   artifacts. Generic paper reading and topic surveys are independent by
   default; recent project context alone does not create a link.
6. Default GitHub clones to `--depth=1` unless history is needed.
7. Never expose credentials or publish secrets, private data, licensed datasets, or large artifacts unintentionally.
8. Do not force-push, rewrite history, or overwrite remotes unless explicitly requested.
9. Create concrete artifacts and end with the next smallest useful action.
