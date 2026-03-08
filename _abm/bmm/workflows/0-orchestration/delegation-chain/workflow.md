# Delegation Chain Workflow
# Core workflow for contract-based task delegation

## Delegation Chain Protocol

### Step 1: Create Task Contract
1. Load template from `{project-root}/_abm/bmm/data/task-contract-template.yaml`
2. Fill in fields based on triage results:
   - `task_id`: Generate unique ID (format: TG-{nn}-W{n})
   - `objective`: From user request / triage classification
   - `scope_in/scope_out`: From impact analysis
   - `acceptance_criteria`: From requirements
   - `budget`: Based on complexity estimate
   - `risk_level`: From triage assessment
3. Save contract to `{implementation_artifacts}/contracts/{task_id}.yaml`

### Step 2: Assign Worker(s)
Based on triage team assembly:
1. Select primary worker for each subtask
2. For parallel tasks: assign independent workers simultaneously
3. For sequential tasks: create dependency chain

### Step 3: Execute Delegation
For each worker:
1. Provide the Task Contract
2. Provide ONLY the context files listed in `context_files`
3. Instruct worker to follow contract scope strictly
4. Worker begins execution

### Step 4: Monitor Progress
While workers are executing:
1. Track budget usage (tool calls, runtime)
2. Check for scope violations
3. Handle blocked workers (reassign or escalate)
4. If worker exceeds budget → trigger retry policy

### Step 5: Collect Attestation
When worker completes:
1. Worker returns attestation using `{project-root}/_abm/bmm/data/attestation-template.yaml`
2. Verify attestation completeness:
   - Has status? ✅/❌
   - Has evidence? ✅/❌
   - Has files_changed? ✅/❌
   - Has confidence score? ✅/❌

### Step 6: Verify Results
Apply 3-layer verification:

**Layer 1 — Syntactic**
- Tests pass? (from attestation test results)
- Lint clean? (if applicable)
- Type check pass? (if applicable)

**Layer 2 — Behavioral**
- Acceptance criteria met? (check each criterion)
- Browser verification needed? (if UI changes)
- Integration test pass? (if applicable)

**Layer 3 — Policy**
- Scope respected? (check scope_violations in attestation)
- Security concerns? (check against governance-policy.yaml)
- Human gate required? (check risk_level)

### Step 7: Decision
Based on verification:
```
ALL PASS → Accept and proceed to synthesis
PARTIAL PASS → Accept with risks, document risks
FAIL (recoverable) → Create retry contract with feedback
FAIL (unrecoverable) → Escalate to human
SECURITY FLAG → Route to Security Evaluator
```

### Step 8: Chain Resolution
If this was a sub-delegation (level 2):
1. Worker sends attestation back to parent delegator
2. Parent delegator verifies and adds to their own attestation
3. Liability returns upward through the chain

If this was top-level (level 1):
1. Jarvis synthesizes all worker outputs
2. Creates final Walkthrough artifact
3. Presents to human for review
