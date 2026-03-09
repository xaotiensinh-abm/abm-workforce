---
name: code-review
description: Two-role code review skill — requesting review (dispatch reviewer subagent) and receiving review (handle feedback correctly). Use after completing implementation or before merging.
---

## KHONG su dung khi

- Can go loi -> dung systematic-debugging. Can viet ke hoach code -> dung writing-plans.


# Code Review

> Adapted from [obra/superpowers](https://github.com/obra/superpowers) for the Jarvis Multi-Agent system.

## Overview

Two-stage code review integrated with the Delegation Chain.

**Core principle:** Review early, review often. Fresh eyes catch what tired ones miss.

## When to Request Review

**Mandatory:**
- After each task in subagent-driven-development
- After completing major feature
- Before merge to main
- When worker attestation has confidence < 0.8

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing complex bug

## Requesting Review

### 1. Prepare Evidence
```bash
BASE_SHA=$(git rev-parse HEAD~N)  # or origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

### 2. Dispatch Reviewer
Create a Task Contract for the reviewer:

```yaml
task_id: "TG-{n}-REVIEW"
objective: "Code review for Task {N}: {description}"
scope_in: [changed files]
scope_out: []  # reviewer can read everything
acceptance_criteria:
  - "Review all changed files"
  - "Check for: correctness, style, security, performance"
  - "Classify issues as Critical/Important/Minor"
required_artifacts: ["review_report"]
```

### 3. Review Report Format
Reviewer returns:
```markdown
## Code Review Report

### Strengths
- [what's good]

### Issues
| # | Severity | File | Line | Issue | Fix |
|---|----------|------|------|-------|-----|

### Assessment
[APPROVED | APPROVED_WITH_MINOR | CHANGES_REQUIRED | REJECTED]
```

### 4. Acting on Feedback
| Severity | Action |
|----------|--------|
| Critical | Fix immediately, re-review |
| Important | Fix before proceeding |
| Minor | Fix or note for later |
| Wrong feedback | Push back with evidence |

## Receiving Review

### Response Pattern
```
1. Read ALL feedback first
2. For each issue:
   - Agree → "Good catch, fixing"
   - Disagree → "I chose X because Y. [evidence]"
   - Unclear → "Can you clarify what you mean by Z?"
3. Fix agreed issues
4. Request re-review if Critical/Important changes
```

### Forbidden Responses
- ❌ "I'll fix it later" (for Critical)
- ❌ Ignoring feedback without response
- ❌ Defensive reactions without evidence
- ❌ "It works" without tests proving it

## Delegation Chain Integration

In the Jarvis system:
- **Worker completes** → Jarvis dispatches review subagent
- **Reviewer returns** → Jarvis evaluates review findings
- **Critical issues** → Worker fixes → re-review loop
- **Approved** → Proceed to next pipeline stage
- **Review evidence** → Included in attestation
