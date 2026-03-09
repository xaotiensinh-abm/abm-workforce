# Delegation Chain Skill
# How Jarvis manages the forward delegation and liability return chain

---
name: delegation-chain
description: Protocol for managing multi-level delegation chains with contracts and attestations
---

## KHONG su dung khi

- Skill bat buoc - luon active. Khong co truong hop khong su dung.


## Delegation Chain Management

This skill defines how the multi-agent system handles task delegation following the
**Delegation Chain Management** architecture.

### Core Concepts

```
┌──────────────┐  contract_1  ┌──────────────┐  contract_2  ┌──────────────┐
│ Delegator A  │─────────────▶│ Delegatee B  │─────────────▶│Sub-delegatee │
│(Orchestrator)│  attest_1    │  (Worker)    │  attest_2    │  C (Sub)     │
│   JARVIS     │◀─────────────│              │◀─────────────│              │
└──────────────┘              └──────────────┘              └──────────────┘
       ▲                                                           │
       │              Forward Delegation ──────────────────▶       │
       │              ◀──────────────────  Liability Return        │
       └───────────────────────────────────────────────────────────┘
```

### Step 1: Create Task Contract

Before delegating any task, the orchestrator MUST create a Task Contract:

1. Load the template from `{project-root}/_abm/bmm/data/task-contract-template.yaml`
2. Fill in ALL required fields:
   - `task_id`: Unique identifier (format: TG-{group}-W{worker})
   - `objective`: Clear, single-sentence description
   - `scope_in`: Exact files/areas the worker CAN modify
   - `scope_out`: Files/areas the worker MUST NOT touch
   - `acceptance_criteria`: Specific, measurable conditions for success
   - `budget`: Maximum tool calls, runtime, and retries
   - `risk_level`: Assessment from triage
3. Save the contract in `{implementation_artifacts}/contracts/`

### Step 2: Assign Worker

Select the appropriate worker based on task type:

| Task Type | Primary Worker | Supporting Workers |
|-----------|---------------|-------------------|
| Code changes | Amelia (Dev) | Quinn (QA) |
| Testing | Quinn (QA) | Browser Subagent |
| Architecture | Winston (Architect) | - |
| Requirements | John (PM) + Mary (Analyst) | - |
| Documentation | Paige (Tech Writer) | - |
| UI verification | Browser Subagent | - |
| Security audit | Shield (Security Eval) | - |
| Sprint planning | Bob (SM) | - |

### Step 3: Worker Executes

The assigned worker:
1. Reads the Task Contract
2. Works ONLY within the defined scope
3. Tracks budget usage (tool calls, time)
4. May create sub-contracts for SubAgents (level 2 delegation)

### Step 4: Worker Returns Attestation

Worker MUST return an attestation using `{project-root}/_abm/bmm/data/attestation-template.yaml`:

1. Fill in ALL required fields:
   - `status`: done | done_with_risks | blocked | failed
   - `summary`: What was accomplished
   - `files_changed`: All modified files
   - `evidence`: Test logs, screenshots, recordings
   - `confidence`: 0.0 to 1.0
   - `scope_violations`: Any deviations from contract

### Step 5: Orchestrator Verifies

Jarvis verifies the attestation:

1. **Acceptance Criteria Check**: Does output meet ALL criteria from the contract?
2. **Evidence Check**: Is there sufficient evidence (test logs, screenshots)?
3. **Scope Check**: Did worker stay within contract scope?
4. **Budget Check**: Was budget respected?
5. **Risk Check**: Any new risks introduced?

Decision tree:
```
All criteria met + evidence sufficient → ACCEPT
Criteria met but risks noted → ACCEPT_WITH_RISKS, add to risk log
Criteria partially met → RETRY with feedback
Worker blocked → REASSIGN or ESCALATE to human
Failed → ROLLBACK + ESCALATE
```

### Step 6: Liability Chain Resolution

- If SubAgent (C) fails → Worker (B) is responsible for retry/escalation
- If Worker (B) fails → Jarvis is responsible for retry/reassignment
- If Jarvis cannot resolve → Escalate to human with full evidence chain
- **Human is the ultimate authority** — Jarvis presents, human decides

### Anti-Patterns to Avoid

1. ❌ Accepting "done" without evidence
2. ❌ Delegating without a contract
3. ❌ Worker modifying files outside contract scope
4. ❌ Skipping verification steps
5. ❌ Over-delegating simple tasks (1-2 files should be single-agent)
6. ❌ Passing full repo context to every worker
