#!/usr/bin/env python3
from pathlib import Path
import sys

ROOTS = [
    'inbox/ideas', 'inbox/papers', 'inbox/questions', 'inbox/raw-notes',
    'ideas', 'knowledge/papers', 'knowledge/claims', 'knowledge/concepts',
    'knowledge/methods', 'knowledge/datasets', 'projects',
    'logs/daily', 'logs/weekly', 'logs/monthly', 'logs/decisions', 'templates'
]

def main():
    if len(sys.argv) != 2:
        print('Usage: python init_research_workspace.py /path/to/research-hub')
        sys.exit(2)
    root = Path(sys.argv[1]).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    for rel in ROOTS:
        (root / rel).mkdir(parents=True, exist_ok=True)
    active = root / 'active-context.md'
    if not active.exists():
        active.write_text('# Active Context\n\n## Active Project\n\nproject_id:\n\n## Active Idea\n\nidea_id:\n\n## Current Focus\n\n## Recent Files\n\n## Open Questions\n\n## Next Actions\n', encoding='utf-8')
    workspace = root / 'workspace.md'
    if not workspace.exists():
        workspace.write_text('# Research Workspace\n\n## Researcher Profile\n\n## Research Areas\n\n## Active Projects\n\n| Project | Status | Target | Next |\n|---|---|---|---|\n\n## Active Ideas\n\n| Idea | Status | Risk | Next |\n|---|---|---|---|\n\n## Knowledge Base\n\n## Writing Pipeline\n\n## Recent Decisions\n', encoding='utf-8')
    print(f'Initialized research workspace at {root}')

if __name__ == '__main__':
    main()
