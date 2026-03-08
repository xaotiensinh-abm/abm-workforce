# Feature Implementation Pipeline
# Pattern: Router → Orchestrator → Plan → Code Workers (parallel) → Test → Browser QA → Docs → Orchestrator

## Feature Pipeline

Use this pipeline when:
- New feature spanning multiple files
- Needs UI verification
- Requires documentation/walkthrough

### Step 1: Requirements Clarification
- Parse feature request
- If unclear: delegate to John (PM) for requirements elicitation
- Output: Clear acceptance criteria list

### Step 2: Create Implementation Plan
- Jarvis creates Implementation Plan artifact
- List all files to be created/modified
- Define task groups (parallel vs sequential)
- Identify risks and rollback strategy
- Present plan to user for approval

### Step 3: Architecture Check (if complex)
- If feature has architectural implications:
  - Delegate to Winston (Architect) for architecture review
  - Verify alignment with existing patterns

### Step 4: Parallel Delegation to Code Workers
For independent subtasks:
- Create separate contracts for each
- Assign to Code Worker (Amelia/Dev)
- Workers execute in parallel within their scope
- Each returns attestation independently

### Step 5: Test Verification
After all code workers complete:
- Delegate to Quinn (QA) for comprehensive testing
- Run full test suite
- Verify all acceptance criteria

### Step 6: Browser QA (if UI feature)
- Delegate to Browser Subagent
- Navigate through new feature flows
- Capture screenshots and recordings

### Step 7: Documentation
- Delegate to Paige (Tech Writer)
- Create/update relevant docs
- Update project knowledge

### Step 8: Synthesis
Jarvis aggregates all attestations:
- Executive summary
- All changes with evidence
- Walkthrough with screenshots
- Risk assessment
- Present to user for final approval
