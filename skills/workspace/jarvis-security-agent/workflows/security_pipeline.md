# Security Audit Workflow

## Step 1: Scan
1. Identify attack surface (endpoints, auth flows, data flows)
2. Check OWASP Top 10 vulnerabilities
3. Review secrets management
4. Check dependencies for known CVEs

## Step 2: Assess
1. Score each finding: 🔴 Critical | 🟡 High | 🟢 Medium | ⚪ Low
2. Prioritize by impact × exploitability
3. Document with proof of concept

## Step 3: Fix
1. Create fix recommendations with code examples
2. Request W1:CodeAgent to implement fixes
3. Verify fixes don't break functionality

## Step 4: Verify
1. Re-scan fixed code
2. Confirm all Critical/High findings resolved
3. Generate security report
4. **HITL**: User sign-off before deploy
