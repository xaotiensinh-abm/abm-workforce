# Rollback Workflow
# Safe reversion of changes with verification

## Rollback Protocol

### Step 1: Identify Rollback Scope
- List all files changed by the failed task
- Identify the rollback strategy from the original plan
- Check for dependent changes that need reverting too

### Step 2: Execute Rollback
- Revert changes using git or manual file restoration
- If database migrations: run down migration
- If config changes: restore previous configs

### Step 3: Verify Rollback
- Run full test suite to confirm clean state
- Check that the pre-change behavior is restored
- Verify no orphaned resources (files, configs, DB entries)

### Step 4: Report
- Document what was rolled back and why
- Note the failure that triggered rollback
- Recommend next steps
- Save as Knowledge Item for future reference
