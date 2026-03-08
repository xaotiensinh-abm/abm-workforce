---
name: git-worktrees
description: Use when starting multi-task development to create isolated workspaces. Each feature gets its own worktree to prevent context pollution.
---

# Git Worktrees

> Adapted from [obra/superpowers](https://github.com/obra/superpowers) for the Jarvis Multi-Agent system.

## Overview

Create isolated workspaces for parallel development using git worktrees.
Each feature branch gets its own directory — no context pollution.

**Core principle:** Isolation prevents interference.

## When to Use

- Starting a new feature/bugfix in subagent-driven-development
- Dispatching parallel agents (each needs isolated workspace)  
- Want to preserve current work while starting something new

## Creation Steps

### 1. Create Worktree
```bash
# Create feature branch + worktree
git worktree add .worktrees/{feature-name} -b feature/{feature-name}
cd .worktrees/{feature-name}
```

### 2. Setup Environment
```bash
# Install dependencies in the worktree
npm install  # or project-specific setup
```

### 3. Verify Clean Baseline
```bash
# CRITICAL: Tests must pass before starting work
npm test
# Expected: All tests passing
```

If tests fail on clean worktree → problem in main branch, fix that first.

### 4. Report Location
```
Worktree created:
- Path: .worktrees/{feature-name}
- Branch: feature/{feature-name}
- Base: main (or current branch)
- Tests: All passing ✅
```

## Delegation Chain Integration

For **dispatching-parallel-agents**:
- Each parallel agent can get its own worktree
- Prevents file editing conflicts
- Clean merge after all agents complete

For **subagent-driven-development**:
- Create worktree before first task
- All tasks execute in isolated workspace
- Use **finishing-a-development-branch** to complete

## Cleanup

```bash
# After merge/discard
git worktree remove .worktrees/{feature-name}
git branch -d feature/{feature-name}
```

## Common Mistakes

- ❌ Skipping test verification on fresh worktree
- ❌ Assuming setup commands (check project docs)
- ❌ Forgetting to add .worktrees/ to .gitignore
- ❌ Working in main directory while worktree exists (confusion)

## .gitignore Entry
Ensure `.worktrees/` is in `.gitignore`:
```
.worktrees/
```
