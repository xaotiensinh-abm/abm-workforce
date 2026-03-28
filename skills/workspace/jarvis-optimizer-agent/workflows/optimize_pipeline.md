# Optimize Pipeline Workflow

## Step 1: Receive Critic Feedback
1. Load Critic Review (scores, issues, directives)
2. Load original Worker output
3. Load Task Contract (original requirements)

## Step 2: Analyze Issues
1. Categorize: 🔴 Critical → fix first, 🟡 Important → then, 🟢 Minor → if time
2. Check if issues are in my domain capability
3. If outside domain → escalate to Jarvis for Worker re-assignment

## Step 3: Fix
1. Address each issue in Critic's directive list
2. Document before/after for each change  
3. DO NOT modify approved portions
4. Keep changes minimal and focused

## Step 4: Self-Assess
1. Verify fixes address Critic's concerns
2. Run any automated checks (tests, lint, SEO score)
3. Self-score improvement estimation
4. Submit to W8:CriticAgent for re-review

## Loop Control
```
Iteration 1: Fix all Critical + Important issues
Iteration 2: Fix remaining + Minor issues  
Iteration 3: Final polish — must be ≥ 4.5 or HITL
```

## Circuit Breaker
- Score DECREASES after fix → STOP → HITL
- Same issues re-flagged → STOP → try different approach or HITL
- 3 iterations exhausted → STOP → HITL
