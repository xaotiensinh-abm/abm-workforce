# Ops Pipeline Workflow

## Step 1: Pre-Deploy Checks
1. Build succeeds (`npm run build` / `docker build`)
2. All tests pass
3. W6:SecurityAgent scan complete
4. Rollback plan documented
5. **HITL**: User approves deploy target

## Step 2: Deploy
1. Build production artifact
2. Deploy to target platform
3. Verify deployment health
4. Run smoke tests

## Step 3: Post-Deploy
1. Monitor logs for errors (first 15 minutes)
2. Verify all endpoints responding
3. Check performance metrics
4. Update deployment record

## Rollback Protocol
1. If health check fails → auto-rollback
2. If errors > threshold → alert → manual rollback
3. Document rollback reason
