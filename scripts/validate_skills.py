#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
skills = sorted((root / 'skills').glob('*/SKILL.md'))
errors = []
required = ['## Overview', '## When to Use', '## Workflow', '## Artifacts', '## Common Rationalizations', '## Red Flags', '## Verification']

for path in skills:
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        errors.append(f'{path}: missing YAML frontmatter')
        continue
    front = text.split('---', 2)[1]
    name = re.search(r'^name:\s*(\S+)\s*$', front, re.M)
    desc = re.search(r'^description:\s*(.+)$', front, re.M)
    if not name:
        errors.append(f'{path}: missing name')
    elif name.group(1) != path.parent.name:
        errors.append(f'{path}: name does not match directory')
    if not desc:
        errors.append(f'{path}: missing description')
    elif len(desc.group(1)) > 1024:
        errors.append(f'{path}: description exceeds 1024 chars')
    for sec in required:
        if sec not in text:
            errors.append(f'{path}: missing {sec}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'OK: {len(skills)} skills validated')
