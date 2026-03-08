# Bug Fix Pipeline Workflow
# Pattern: Router → Orchestrator → Code Worker → Test Worker → Browser QA → Orchestrator

## Bug Fix Pipeline

Use this pipeline when:
- Error report with clear reproduction steps
- Acceptance criteria are deterministic
- Need fast turnaround

### Step 1: Receive Bug Report
- Parse: description, reproduction steps, expected vs actual behavior
- Identify affected files/modules
- Classify severity: P0 (critical), P1 (high), P2 (medium), P3 (low)

### Step 2: Create Contract for Code Worker
Delegate to Amelia (Dev):
- Objective: Fix the described bug
- Scope: Identified affected files only
- Acceptance criteria: Bug no longer reproducible + existing tests pass
- Required artifacts: diff_summary, test_result

### Step 3: Code Worker Executes
- Reads bug report and affected files
- Implements fix
- Writes/updates test covering the bug
- Returns attestation with evidence

### Step 4: Create Contract for Test Verifier
Delegate to Quinn (QA):
- Objective: Verify bug fix and no regression
- Scope: Run test suite on affected modules
- Acceptance criteria: All tests pass, bug test passes
- Required artifacts: test_log, coverage_report

### Step 5: Browser QA (if UI bug)
If the bug involves UI:
- Delegate to Browser Subagent
- Objective: Verify UI renders correctly, interaction works
- Required artifacts: screenshots, browser_recording

### Step 6: Synthesis
Jarvis aggregates:
- Code Worker attestation (fix details)
- Test Verifier attestation (test results)
- Browser QA attestation (if applicable)
- Creates walkthrough and presents to user
