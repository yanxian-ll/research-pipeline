# Skill Anatomy for Research Workflows

Each skill follows this structure:

```yaml
---
name: lowercase-hyphenated-skill-name
description: What the skill does. Use when specific trigger conditions apply.
---
```

Recommended sections:

1. `Overview` — one or two sentences describing the workflow.
2. `When to Use` — positive triggers and exclusions.
3. `Workflow` — the ordered process the agent must follow.
4. `Artifacts` — files or outputs the workflow creates or updates.
5. `Common Rationalizations` — excuses that cause poor research behavior.
6. `Red Flags` — observable violations.
7. `Verification` — exit checklist with evidence requirements.

Research-specific constraints:

- Literature search must produce query strings and closest-work candidates.
- Gap claims must reference the literature matrix or be labeled as hypotheses.
- Paper writing must map claims to sources, experiments, code, or discussion records.
- Logs are not project reports by default. They are researcher-level records with optional links.
