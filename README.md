# Research Agent Skills

**Production-grade research workflows for AI research agents, from code acquisition to publication.**

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
| Clone/create/publish a repository | `/github` | `github-repository-operations` | Verify before changing remotes |
| Extract a research idea from code | `/code-idea` | `code-to-research-idea` | Code evidence before research claims |
| Capture or refine a raw research idea | `/idea` | `research-idea-refine` | Idea before project |
| Read, summarize, or compare papers | `/read-paper` | `paper-reading-and-synthesis` | Independent by default |
| Deep-read one paper from motivation to evidence | `/deep-read-paper` | `paper-deep-reading` | Independent by default |
| Ground a named idea/project in literature | `/lit` | `literature-grounding` | Evidence before claims |
| Find novelty and research gaps | `/gap` | `gap-and-novelty-review` | Closest work first |
| Design the research framework | `/frame` | `research-framework-design` | Hypothesis before architecture |
| Plan experiments | `/exp` | `experiment-planning` | Verification before results |
| Write paper core or sections | `/paper` | `paper-core-writing`, `evidence-based-writing` | Claims trace to evidence |
| Write a code-aligned Method section | `/method` | `research-method-writing` | Method prose matches implementation |
| Maintain daily/weekly research logs | `/log` | `research-log-review` | Logs are independent objects |
| Manage project state | `/project` | `research-project-management` | Project is execution, not thinking |
| Review as a critic | `/review` | `research-critic-review` | Doubt before submission |
| Prepare submission/rebuttal | `/submit` | `research-submission-readiness` | Venue-specific quality gates |

## Skills

| Phase | Skill | Use when |
|---|---|---|
| Meta | `using-research-skills` | Routing a research task |
| Acquire/Publish | `github-repository-operations` | Need clone, create, remote, commit, or push |
| Extract | `code-to-research-idea` | Need to derive candidate ideas from code |
| Define | `research-idea-refine` | Raw idea, vague direction, paper-worthiness |
| Define | `research-context-engineering` | Need the right context packet |
| Read | `paper-reading-and-synthesis` | Need paper notes, explanations, comparisons, or topic surveys |
| Deep read | `paper-deep-reading` | Need problem-first derivation, figures/tables/ablations, or reproduction-level understanding |
| Ground | `literature-grounding` | Need prior work, baselines, or closest work for a named idea/project |
| Ground | `gap-and-novelty-review` | Need gap, novelty risk, go/pivot/stop |
| Frame | `research-framework-design` | Need research framework or method design |
| Verify | `experiment-planning` | Need hypotheses, datasets, baselines, metrics |
| Write | `paper-core-writing` | Need pitch, abstract, contributions, outline |
| Write | `evidence-based-writing` | Need full sections grounded in evidence |
| Write | `research-method-writing` | Need a reproducible Method section aligned with code |
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
8. **Code traceability.** Implementation claims point to files, symbols, configs, tests, or logs.
9. **Credential-safe GitHub operations.** Prefer authenticated tooling; shallow clone by default.
