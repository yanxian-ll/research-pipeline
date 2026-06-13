# Research Agent Skills

**Production-grade research workflows for AI research agents.**

This pack restructures a research pipeline as a set of small, composable skills rather than one long instruction file. It follows a lifecycle pattern:

```text
  DEFINE        GROUND        FRAME        VERIFY        WRITE        REVIEW        SUBMIT
 ┌──────┐      ┌──────┐      ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐      ┌──────┐
 │Idea  │ ───▶│Lit   │ ───▶ │Gap & │ ───▶│Exp   │ ───▶│Paper │ ───▶│Critic│ ───▶ │Venue │
 │Refine│      │Search│      │Frame │     │Plan  │     │Draft │     │Revise│      │Ship  │
 └──────┘      └──────┘      └──────┘     └──────┘     └──────┘     └──────┘      └──────┘
  /idea          /lit          /gap,/frame  /exp         /paper       /review       /submit
```

## Commands

| What you're doing | Command | Activates | Key principle |
|---|---|---|---|
| Capture or refine a raw research idea | `/idea` | `research-idea-refine` | Idea before project |
| Search and ground in literature | `/lit` | `literature-grounding` | Evidence before claims |
| Find novelty and research gaps | `/gap` | `gap-and-novelty-review` | Closest work first |
| Design the research framework | `/frame` | `research-framework-design` | Hypothesis before architecture |
| Plan experiments | `/exp` | `experiment-planning` | Verification before results |
| Write paper core or sections | `/paper` | `paper-core-writing`, `evidence-based-writing` | Claims trace to evidence |
| Maintain daily/weekly research logs | `/log` | `research-log-review` | Logs are independent objects |
| Manage project state | `/project` | `research-project-management` | Project is execution, not thinking |
| Review as a critic | `/review` | `research-critic-review` | Doubt before submission |
| Prepare submission/rebuttal | `/submit` | `research-submission-readiness` | Venue-specific quality gates |

## Skills

| Phase | Skill | Use when |
|---|---|---|
| Meta | `using-research-skills` | Routing a research task |
| Define | `research-idea-refine` | Raw idea, vague direction, paper-worthiness |
| Define | `research-context-engineering` | Need the right context packet |
| Ground | `literature-grounding` | Need prior work, papers, baselines, closest work |
| Ground | `gap-and-novelty-review` | Need gap, novelty risk, go/pivot/stop |
| Frame | `research-framework-design` | Need research framework or method design |
| Verify | `experiment-planning` | Need hypotheses, datasets, baselines, metrics |
| Write | `paper-core-writing` | Need pitch, abstract, contributions, outline |
| Write | `evidence-based-writing` | Need full sections grounded in evidence |
| Operate | `research-log-review` | Need daily/weekly/monthly logs |
| Operate | `research-project-management` | Need project roadmap/progress |
| Review | `research-critic-review` | Need adversarial review |
| Submit | `research-submission-readiness` | Need final submission/rebuttal readiness |

## Directory Layout

```text
research-agent-skills/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── commands/
├── docs/
├── examples/
├── scripts/
├── skills/
├── templates/
└── workspace/
```

## Workspace Model

```text
research-hub/
├── active-context.md
├── workspace.md
├── inbox/
├── ideas/
├── knowledge/
├── projects/
├── logs/
│   ├── daily/
│   ├── weekly/
│   ├── monthly/
│   └── decisions/
└── templates/
```

Initialize a workspace:

```bash
python scripts/init_research_workspace.py /path/to/research-hub
```

## Design Principles

1. **Workflows over knowledge dumps.** A skill is a process the agent follows, not a textbook.
2. **Small skills compose better than a giant skill.** Route by lifecycle stage.
3. **Evidence over confidence.** Claims require citations, experiments, code, or clearly labeled hypotheses.
4. **Closest work first.** Novelty analysis starts with the most similar paper.
5. **Logs are first-class.** Daily and weekly logs are independent objects that link to ideas/projects/papers.
6. **Anti-rationalization.** Each skill names the excuses that cause bad research work.
7. **Verification gates.** Each workflow ends with checkable outputs.
