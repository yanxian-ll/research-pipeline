# Workspace Schema

## Workspace Root

```text
research-hub/
├── active-context.md
├── workspace.md
├── inbox/
├── ideas/
├── knowledge/
├── projects/
├── logs/
└── templates/
```

## Idea

```yaml
type: idea
id:
title:
status: seed | researching | discussing | refined | project-candidate | converted | archived
created_at:
updated_at:
linked_projects: []
linked_papers: []
tags: []
domain:
task:
method:
data:
target_venue:
novelty_risk:
confidence:
```

## Paper

```yaml
type: paper
id:
title:
authors:
year:
venue:
doi:
url:
source:
linked_ideas: []
linked_projects: []
relevance_score:
novelty_risk:
reuse_value:
```

## Project

```yaml
type: project
id:
title:
status: planning | literature | experimenting | writing | submitted | rebuttal | accepted | paused | archived
active_idea:
linked_ideas: []
linked_papers: []
target_venue:
deadline:
```

## Log

```yaml
type: daily_log | weekly_review | monthly_review | decision
linked_projects: []
linked_ideas: []
linked_papers: []
tags: []
```
