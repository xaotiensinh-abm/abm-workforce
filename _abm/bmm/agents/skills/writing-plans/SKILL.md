---
name: writing-plans
description: Use when you have a spec or requirements for a multi-step task, before touching code. Creates comprehensive implementation plans with bite-sized TDD tasks.
---

# Writing Plans

> Adapted from [obra/superpowers](https://github.com/obra/superpowers) for the Jarvis Multi-Agent system.

## Overview

Write comprehensive implementation plans assuming the engineer has zero context.
Document everything needed: files to modify, code, testing, how to verify.
Deliver as bite-sized TDD tasks. DRY. YAGNI. Frequent commits.

**Core principle:** Plans are the blueprint. Quality plans = quality code.

## Bite-Sized Task Granularity

Each step is ONE action (2-5 minutes):
- "Write the failing test" — step
- "Run it to make sure it fails" — step
- "Implement minimal code to pass" — step
- "Run tests, verify pass" — step
- "Commit" — step

## Plan Document Header

Every plan MUST start with:

```markdown
# [Feature Name] Implementation Plan

> **For Jarvis:** Use subagent-driven-development to execute this plan task-by-task.

**Goal:** [One sentence: what this builds]
**Architecture:** [2-3 sentences: approach]
**Risk Level:** [low | medium | high | critical]
**Estimated Tasks:** [count]

---
```

## Task Structure

```markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.ts`
- Modify: `exact/path/to/existing.ts:L123-L145`
- Test: `tests/exact/path/to/test.ts`

**Acceptance Criteria:**
- [ ] Feature X works as specified
- [ ] All tests pass
- [ ] No scope_out files modified

**Step 1: Write failing test**
[exact test code]

**Step 2: Run test — verify FAIL**
Run: `npm test -- path/test.ts`
Expected: FAIL with "function not defined"

**Step 3: Implement minimal code**
[exact implementation code]

**Step 4: Run test — verify PASS**
Run: `npm test -- path/test.ts`
Expected: PASS

**Step 5: Commit**
`git commit -m "feat: add specific feature"`
```

## Integration with Delegation Chain

Each plan task maps to a **Task Contract**:
- `scope_in` = Files listed in task
- `acceptance_criteria` = Task's acceptance criteria
- `budget` = Estimated based on step count

## Execution Handoff

After saving plan, offer execution choice:

**1. Subagent-Driven (this session)**
Use `subagent-driven-development` skill — fresh subagent per task with review

**2. Parallel Agents (if tasks are independent)**
Use `dispatching-parallel-agents` skill — concurrent execution

## Red Flags

- ❌ Vague steps ("add validation logic")
- ❌ Missing file paths
- ❌ No test steps
- ❌ Steps that take >10 minutes
- ❌ Skipping commit steps
