---
name: dispatching-parallel-agents
description: Use when you have multiple independent problems to solve simultaneously. Identify independent domains, create focused agent tasks, dispatch in parallel, review and integrate.
---

# Dispatching Parallel Agents

> Adapted from [obra/superpowers](https://github.com/obra/superpowers) for the Jarvis Multi-Agent system.

## Overview

When you have multiple independent problems, dispatch focused agents in parallel.
Each agent gets a narrow scope and clear goal. Results integrate without conflicts.

**Core principle:** Independent domains + focused scope = parallel speedup

## When to Use

- Multiple independent failures/tasks across different files
- Each domain is self-contained (fixing A doesn't affect B)
- Agents won't edit the same files
- Time savings justify the setup

## When NOT to Use

- Related failures (fixing one might fix others)
- Need full system context to understand the problem
- Exploratory debugging (you don't know what's broken yet)
- Shared state (agents would edit same files)

## The Pattern

### 1. Identify Independent Domains
Group by what's broken/needed:
- domain A: Feature X tests / files
- domain B: Feature Y tests / files
- domain C: Feature Z tests / files

Each domain is independent — fix in A doesn't affect B.

### 2. Create Focused Task Contracts
Each agent gets a Task Contract with:
- **Specific scope_in:** Only files in their domain
- **Clear objective:** What to fix/implement
- **scope_out:** Everything not in their domain
- **Expected attestation:** Summary of findings + changes

### 3. Dispatch in Parallel
```
Jarvis:
  Task("Fix feature-X tests", scope=["src/features/x/"])
  Task("Fix feature-Y tests", scope=["src/features/y/"])
  Task("Fix feature-Z tests", scope=["src/features/z/"])
  // All three run concurrently
```

### 4. Review and Integrate
When agents return attestations:
1. Read each summary
2. Verify fixes don't conflict (no shared files modified)
3. Run FULL test suite (verification-before-completion skill)
4. Integrate all changes
5. If conflicts: resolve sequentially

## Agent Prompt Structure

Good agent prompts are:
1. **Focused** — One clear problem domain
2. **Self-contained** — All context needed
3. **Specific about output** — What should the agent return?

```markdown
Fix the failing tests in {file_path}:

1. {test_name_1} — expects {expected}, gets {actual}
2. {test_name_2} — {error_description}

Your task:
1. Read the test file and understand intent
2. Identify root cause
3. Fix by addressing the actual issue (not increasing timeouts)

Scope: Only modify files in {scope_directory}
Do NOT change: {scope_out_files}

Return: Summary of root cause + changes made + test results
```

## Common Mistakes

| ❌ Bad | ✅ Good |
|--------|---------|
| "Fix all the tests" (too broad) | "Fix feature-X tests in src/x/" (focused) |
| No error context | Paste error messages + test names |
| No constraints | "Do NOT change production code" |  
| "Fix it" (vague output) | "Return summary of root cause and changes" |

## Delegation Chain Integration

Maps to Jarvis system as:
- Jarvis creates **parallel Task Contracts** for each domain
- Each worker gets an **independent scope_in**
- Workers return **attestations** independently
- Jarvis collects all attestations, checks for conflicts
- Runs **verification-before-completion** on integrated result
