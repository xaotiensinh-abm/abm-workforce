# Synthesis Workflow
# Final output aggregation and walkthrough generation

## Output Synthesis Protocol

### Step 1: Collect All Attestations
Gather attestations from all workers in the delegation chain:
- List all completed contracts and their attestations
- Note any outstanding or failed tasks
- Calculate overall confidence score (weighted average of worker confidences)

### Step 2: Aggregate Changes
Create a unified change manifest:
- All files changed across all workers
- All files created and deleted
- All tests run and results
- All evidence artifacts collected

### Step 3: Risk Synthesis
Combine risk assessments from all attestations:
- Consolidate `known_risks` from every worker
- Note any scope violations
- Include Security Evaluator findings (if applicable)
- Overall risk level: highest risk from any single worker

### Step 4: Create Executive Summary
Write a concise summary for the human user:

```markdown
## Executive Summary
**Task**: [original user request]
**Status**: [COMPLETE | COMPLETE_WITH_RISKS | PARTIAL | FAILED]
**Confidence**: [0.0 - 1.0]

### What Changed
- [file list with brief description of changes]

### What Was Verified
- [tests run, browser verifications, security scans]

### Remaining Risks
- [consolidated risk list]

### Recommended Next Steps
- [follow-up actions, if any]
```

### Step 5: Generate Walkthrough Artifact
Create a Walkthrough artifact with:
- Problem statement
- Solution approach
- Changes made (with diffs or summaries)
- Verification evidence (test results, screenshots, recordings)
- Risk assessment
- Lessons learned (for Knowledge Items)

### Step 6: Present to Human
Deliver the final output through:
1. **Implementation Plan** (if it was a large task)
2. **Review Changes** (diff view)
3. **Walkthrough** (narrative with evidence)
4. **Screenshots/Recordings** (if UI changes)

Wait for human approval, comments, or requests for changes.

### Step 7: Memory Update
After human approval:
1. Capture any lessons learned as Knowledge Items
2. If a repeatable pattern emerged, consider creating a new Skill
3. Update project context if significant changes were made
4. Archive contracts and attestations for audit trail
