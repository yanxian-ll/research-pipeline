---
name: github-repository-operations
description: Manages GitHub repositories for research projects, including authentication checks, shallow cloning public or private repositories, creating repositories, configuring remotes, branching, committing, and pushing. Use when Codex must acquire code from GitHub or publish a research project; prefer the installed GitHub plugin and use gh or git for local operations.
---

# GitHub Repository Operations

## Overview

Acquire and publish research repositories with explicit scope, minimal history transfer, and credential-safe workflows.

## When to Use

- Clone a public or private GitHub repository
- Create a GitHub repository for a local research project
- Configure remotes, commit, branch, or push research artifacts
- Check authentication or repository publication state

## Workflow

1. Inspect the local path, git status, current branch, remotes, and ownership before changing anything.
2. Check authentication with the GitHub plugin or `gh auth status`. Never print, store, or request raw tokens when authenticated tooling is available.
3. Clone with minimal history by default:
   - Private or GitHub-aware: `gh repo clone OWNER/REPO [DEST] -- --depth=1`
   - URL fallback: `git clone --depth=1 URL [DEST]`
   - Add `--branch BRANCH --single-branch` when a branch is specified.
4. Create with `gh repo create NAME --private|--public --source PATH --remote origin`; never assume visibility. Prefer the GitHub plugin when it supports the operation.
5. Before publishing, inspect diffs and exclude credentials, datasets, checkpoints, generated outputs, and private metadata.
6. Create or reuse an approved branch, stage only intended files, commit intentionally, then run `git push -u origin BRANCH`.
7. Do not force-push, delete branches, rewrite history, change visibility, or overwrite remotes unless explicitly requested.
8. Report repository URL, branch, commit, visibility, and intentionally excluded files.

## Artifacts

- Local repository checkout
- GitHub repository and configured remote
- Optional `projects/<project-id>/code/repository.md`

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "Cloning full history is harmless." | Default to `--depth=1` unless history is needed. |
| "Private is probably intended." | Visibility must be explicit. |
| "Push everything for convenience." | Research folders often contain secrets, data, and large artifacts. |
| "Force push fixes divergence." | Rewriting remote history requires explicit authorization. |

## Red Flags

- Raw credentials in commands, logs, remotes, or files
- Publishing private data, model weights, API keys, or licensed datasets
- Overwriting an existing remote without inspection
- Committing unrelated user changes
- Destructive git operations without explicit approval
- Claiming a remote action succeeded without verification

## Verification

- [ ] Authentication and repository ownership are known
- [ ] Clone uses `--depth=1` unless history is required
- [ ] Visibility is explicit before repository creation
- [ ] Diff and sensitive-file checks precede push
- [ ] Remote, branch, commit, and push state are verified
