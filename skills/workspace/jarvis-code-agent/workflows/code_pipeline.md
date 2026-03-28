# Code Pipeline Workflow

## Full Pipeline: /plan → /code → /test → /deploy

### Step 1: Plan (Mandatory for M+ complexity)
1. Read existing codebase structure
2. Identify affected files and dependencies
3. Create implementation plan with file list
4. Get approval (from Jarvis or user)

### Step 2: Code
1. Set up project if new (`npx -y create-...`)
2. Implement core logic first, UI second
3. Follow standards in `resources/standards.md`
4. Use templates from `resources/templates.md`
5. Commit logically (1 commit per feature/fix)

### Step 3: Test
1. Write tests for critical paths
2. Run `npm test` / `npm run lint`
3. Fix all errors before proceeding
4. Coverage target: >80% for business logic

### Step 4: Deploy
1. Build production bundle: `npm run build`
2. Verify build succeeds with no warnings
3. Hand off to W7:OpsAgent for deployment
4. Post-deploy smoke test

## Sub-Agent Spawning Decision
```
Task has frontend AND backend? → Spawn both SubAgents
Task is only UI? → Spawn FrontendSubAgent only
Task is only API? → Spawn BackendSubAgent only
Need test suite? → Spawn TestingSubAgent
```
