---
name: context-engineering
description: "5-Layer Context Assembly + Token Budget Enforcer. Controls what goes into every agent's context window. Prevents context bomb. Ensures agents get ONLY what they need."
tags: [meta, core, context, optimization]
---

## KHONG su dung khi

- Can giao viec -> dung delegation-chain. Can luu context -> dung save.


# 🧠 Context Engineering — 5-Layer Token-Optimized Assembly

> Based on the Context Engineering Architecture: Request → Priority Ranker → Layer Assembler → 5 Layers → Token Budget Enforcer → Optimized Window.

## Overview

Every agent interaction consumes tokens. This skill engineers the OPTIMAL context for each agent,
loading only what's needed and enforcing strict token budgets.

**Problem solved:** Orchestrator = 221 lines = 3,500 tokens BEFORE user speaks. With skills + consciousness = 5-7K tokens wasted.

## The 5 Context Layers

```
┌─────────────────────────────────────────┐
│         Agent Context Request           │
│    (task_type, agent_id, urgency)       │
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│        Context Priority Ranker          │
│   Scores each layer: 0.0 → 1.0         │
│   Based on: task_type + agent_role      │
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│          Layer Assembler                │
│   Pulls from 5 layers by priority       │
└──┬───────┬────────┬────────┬───────┬────┘
   ▼       ▼        ▼        ▼       ▼
┌──────┐┌───────┐┌───────┐┌──────┐┌───────┐
│Layer1││Layer2 ││Layer3 ││Layer4││Layer5 │
│Ident.││Domain ││Runtime││Task  ││History│
└──┬───┘└───┬───┘└───┬───┘└──┬───┘└───┬───┘
   └────────┴────────┼───────┴────────┘
                     ▼
          ┌─────────────────────┐
          │ Token Budget Enforcer│
          │ Max tokens per layer │
          └──────────┬──────────┘
                     ▼
          ┌─────────────────────┐
          │ Optimized Context    │
          │ Window (2000-4000t)  │
          └─────────────────────┘
```

## Layer Definitions

### Layer 1: Identity Layer (ALWAYS loaded)
```
Source: agents/{agent}/SOUL.md (hoặc legacy .md file)
Contains: WHO am I, core principles, communication style
Token budget: 200-400 tokens
Priority: 1.0 (always max)
```

### Layer 2: Domain Knowledge Layer (loaded by task_type)
```
Source: skills/{skill}/SKILL.md (via skill-routing)
Contains: Templates, frameworks, best practices for this task domain
Token budget: 500-1500 tokens
Priority: Varies by task_type (0.0 for irrelevant skills, 1.0 for matched)

Loading rules:
- Load ONLY skills from <skill-routing> matching current task_type
- NEVER load all 25 skills simultaneously
- Max 3 skills loaded per task
```

### Layer 3: Runtime State Layer (loaded on demand)
```
Source: delegation-dashboard, governance-policy.yaml
Contains: Active contracts, pending attestations, current pipeline position
Token budget: 200-500 tokens
Priority: 0.8 when managing workers, 0.0 for leaf workers

Loading rules:
- Jarvis: ALWAYS load (manages workers)
- Workers: NEVER load (they don't need orchestration state)
```

### Layer 4: Task Data Layer (loaded per task)
```
Source: Task Contract, context_files, context_artifacts
Contains: Current task scope, acceptance criteria, input data
Token budget: 500-2000 tokens
Priority: 1.0 for active task worker, 0.0 otherwise

Loading rules:
- Only the ACTIVE task contract
- Only context_files listed in contract
- Only knowledge_items referenced in contract
```

### Layer 5: History Layer (loaded selectively)
```
Source: task-log.yaml, attestations/, conversation history
Contains: Past task results, patterns, lessons learned
Token budget: 200-500 tokens
Priority: 0.3 default, 0.9 for evolver/crystallizer tasks

Loading rules:
- Default: Last 3 completed tasks only
- Evolver: Full task-log scan
- Bug fix: Previous related bug attestations
```

## Token Budget Enforcer

### Budget Allocation by Agent Role

| Agent | Total Budget | L1 Identity | L2 Domain | L3 Runtime | L4 Task | L5 History |
|-------|-------------|-------------|-----------|------------|---------|------------|
| **Jarvis** | 3000t | 300 | 200 | 500 | 1000 | 1000 |
| **Worker** | 2500t | 200 | 800 | 0 | 1200 | 300 |
| **Reviewer** | 2000t | 200 | 300 | 0 | 1200 | 300 |
| **Security** | 2000t | 200 | 500 | 200 | 800 | 300 |

### Enforcement Rules

```
RULE 1: NEVER exceed total budget. Trim lowest-priority layer first.
RULE 2: Identity Layer is UNTOUCHABLE — never trim below 100 tokens.
RULE 3: Task Data is CRITICAL — never trim below 500 tokens for active tasks.
RULE 4: History is EXPENDABLE — trim first when over budget.
RULE 5: Domain Knowledge follows skill-routing — load max 3 skills.
```

### Trimming Strategy (when over budget)

```
1. Remove History Layer entries older than 3 tasks
2. Summarize Domain Knowledge to key points only
3. Remove Runtime State details (keep summary only)
4. NEVER trim: Identity + Task Data core
```

## Context Priority Ranker — Scoring Matrix

| task_type | L1 Identity | L2 Domain | L3 Runtime | L4 Task | L5 History |
|-----------|-------------|-----------|------------|---------|------------|
| bug | 1.0 | 0.9 (debug) | 0.3 | 1.0 | 0.7 (prev bugs) |
| feature | 1.0 | 0.8 (plans) | 0.5 | 1.0 | 0.3 |
| marketing | 1.0 | 1.0 (copy) | 0.1 | 1.0 | 0.2 |
| hr | 1.0 | 1.0 (HR) | 0.1 | 1.0 | 0.2 |
| report | 1.0 | 0.9 (data) | 0.2 | 1.0 | 0.8 (trends) |
| review | 1.0 | 0.7 | 0.8 | 1.0 | 0.5 |

## Integration

When Jarvis delegates a task:
1. Determine `task_type` and `agent_id`
2. Run Context Priority Ranker → score each layer
3. Layer Assembler pulls files by priority
4. Token Budget Enforcer trims to budget
5. Final optimized context → inject into worker prompt

## Safety
- ❌ NEVER load all 25 skills into one context
- ❌ NEVER forward full orchestrator state to leaf workers
- ✅ ALWAYS verify total context stays within budget
- ✅ Log context composition for debugging
