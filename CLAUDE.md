# Research Agent Skills Router

Use this as the top-level instruction for agents that support project-level rules.

## Always Start Here

When a research task arrives, choose the smallest applicable workflow:

```text
Need to decide what workflow applies?         → using-research-skills
Raw idea / vague research direction?          → research-idea-refine
Need literature / “has anyone done this?”     → literature-grounding
Need novelty, gap, go/pivot/stop?             → gap-and-novelty-review
Need method / research framework?             → research-framework-design
Need datasets, baselines, metrics?            → experiment-planning
Need paper pitch, abstract, contributions?    → paper-core-writing
Need full section drafting with evidence?      → evidence-based-writing
Need daily/weekly/monthly logs?               → research-log-review
Need project roadmap/progress?                → research-project-management
Need adversarial review?                      → research-critic-review
Need submission/rebuttal readiness?           → research-submission-readiness
```

## Global Rules

1. Do not invent papers, DOIs, venues, citations, experimental results, or code behavior.
2. Surface assumptions before turning ambiguous ideas into confident plans.
3. Treat “novel” as unproven until closest-work search is complete.
4. Keep logs independent from projects unless the user explicitly links them.
5. Write concrete artifacts: `idea.md`, `literature-search.md`, `gap-analysis.md`, `framework.md`, `experiment-plan.md`, `paper-core.md`, `daily.md`, `weekly.md`.
6. Every output should name the next smallest useful action.
7. When evidence is missing, label statements as hypotheses, not facts.
