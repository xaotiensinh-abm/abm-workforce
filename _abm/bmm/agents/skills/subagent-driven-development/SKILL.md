---
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
name: subagent-driven-development
description: Execute implementation plans by dispatching fresh subagent per task, with two-stage review (spec compliance then code quality) after each. Use when you have a plan with independent tasks.
---

## KHONG su dung khi

- Task nho khong can subagent -> tu lam. Can parallel -> dung dispatching-parallel-agents.


# Subagent-Driven Development

> Adapted from [obra/superpowers](https://github.com/obra/superpowers) for the Jarvis Multi-Agent system.

## Overview

Execute plan by dispatching fresh subagent per task, with two-stage review after each:
spec compliance review first, then code quality review.

**Core principle:** Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration

## When to Use

- Have implementation plan with bite-sized tasks
- Tasks are mostly independent  
- Want same-session execution with quality gates
- Complex enough to need fresh context per task

## The Process

```
1. Read plan, extract ALL tasks with full text, note context
2. For each task:
   a. Dispatch implementer (Task tool) with full task text + context
   b. Answer implementer questions (if any)
   c. Implementer: implements → tests → commits → self-reviews
   d. Dispatch spec reviewer → checks code matches spec
      - If spec issues → implementer fixes → re-review
   e. Dispatch code quality reviewer → checks implementation quality
      - If quality issues → implementer fixes → re-review
   f. Mark task complete
3. After all tasks: dispatch final code reviewer
4. Use finishing-a-development-branch skill
```

## Delegation Chain Integration

In the Jarvis system, this maps to:
- **Orchestrator (Jarvis)** = Controller dispatching subagents
- **Implementer subagent** = Code Worker (Amelia/Dev) with Task Contract
- **Spec reviewer subagent** = Jarvis self-review or QA Worker (Quinn)
- **Code quality reviewer** = Separate review role dispatch

### Contract-Based Dispatch

Instead of raw prompts, every subagent dispatch uses a Task Contract:

```yaml
# For implementer
task_id: "TG-{n}-W1"
objective: "[task description from plan]"
scope_in: [files from plan]
scope_out: [everything else]
acceptance_criteria:
  - "Tests pass for the specific feature"
  - "Self-review completed"
  - "Committed to feature branch"
budget:
  max_tool_calls: 25
  max_retries: 2
```

## Prompt Templates

### Implementer Prompt
```markdown
You are implementing Task {N}: {task_title}

## Context
{scene-setting context about where this task fits}

## Task Details
{full task text from plan}

## Rules
- Follow TDD: write failing test → implement → verify pass
- Stay within scope: only modify files listed above
- Self-review before completing
- Commit with descriptive message
- Return attestation with evidence
```

### Spec Reviewer Prompt
```markdown
Review the implementation of Task {N} for spec compliance.

## Original Spec
{task requirements}

## Check
- Does implementation match ALL requirements?
- Anything MISSING from spec?
- Anything EXTRA not requested?
- Tests cover requirements?

Return: PASS or list specific issues
```

### Code Quality Reviewer Prompt
```markdown
Review code quality for Task {N}.

## Changes
{git diff or files changed}

## Check
- Code style consistent?
- Error handling adequate?
- No magic numbers/hardcoded values?
- Tests meaningful (not just "passes")?
- Performance concerns?

Return: APPROVED or list issues with severity
```

## Red Flags — NEVER Do

- ❌ Skip reviews (spec compliance OR code quality)
- ❌ Proceed with unfixed issues
- ❌ Dispatch multiple implementers in parallel on same files
- ❌ Make subagent read the entire plan file (provide full text instead)
- ❌ Skip scene-setting context
- ❌ Accept "close enough" on spec compliance
- ❌ Start quality review before spec compliance is ✅
- ❌ Move to next task with open review issues

## Required Skills

- **verification-before-completion** — Verify before claiming done
- **writing-plans** — Creates the plan this skill executes
- **finishing-a-development-branch** — Complete after all tasks
