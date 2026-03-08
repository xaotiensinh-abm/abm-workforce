---
name: finishing-a-development-branch
description: Use when implementation is complete and all tests pass. Guides completion by presenting merge/PR/discard options and cleaning up.
---

# Finishing a Development Branch

> Adapted from [obra/superpowers](https://github.com/obra/superpowers) for the Jarvis Multi-Agent system.

## Overview

Guide completion of development work. Verify → Present options → Execute → Cleanup.

**Core principle:** Verify tests → Present options → Execute choice → Clean up.

## The Process

### Step 1: Verify Tests (MANDATORY)

```bash
# Run full test suite
npm test  # or project-specific command
```

**If tests fail:** STOP. Fix before proceeding. Cannot merge/PR with failing tests.
**If tests pass:** Continue to Step 2.

### Step 2: Present Options

Present exactly 4 options:
```
Implementation complete. What would you like to do?

1. Merge back to {base-branch} locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)
4. Discard this work

Which option?
```

### Step 3: Execute Choice

**Option 1: Merge Locally**
```bash
git checkout {base-branch}
git pull
git merge {feature-branch}
# VERIFY tests after merge
npm test
git branch -d {feature-branch}
```

**Option 2: Push and Create PR**
```bash
git push -u origin {feature-branch}
gh pr create --title "{title}" --body "## Summary\n{changes}\n\n## Tests\n- [x] All tests passing"
```

**Option 3: Keep As-Is**
Report: "Branch {name} preserved."

**Option 4: Discard**
Confirm: "Type 'discard' to confirm permanently deleting {branch}."
```bash
git checkout {base-branch}
git branch -D {feature-branch}
```

### Step 4: Cleanup
Options 1, 2, 4 → clean up worktree if applicable.

## Delegation Chain Integration

This skill is the **final step** in both:
- `subagent-driven-development` (after all tasks complete)
- Pipeline workflows (after synthesis)

Jarvis presents options to human as part of the **Human Assurance Plane**.

## Red Flags

- ❌ Proceed with failing tests
- ❌ Merge without verifying tests on result
- ❌ Delete work without confirmation
- ❌ Force-push without explicit request
