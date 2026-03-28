# Review Pipeline Workflow

## Step 1: Receive
1. Receive Task Report from Worker
2. Load original Task Contract (expected output + quality gate)
3. Compare deliverables vs requirements

## Step 2: Evaluate
1. Score each of 5 dimensions (1-5)
2. Calculate weighted average
3. Identify specific issues with severity
4. Note strengths

## Step 3: Verdict
```
Score ≥ 4.5 → ✅ APPROVE → Pass to Phase 7 (Synthesis)
Score 3.5-4.4 → ⚠️ IMPROVE → Write directives → Send to W9:Optimizer
Score < 3.5 → ❌ REDO → Detailed feedback → Send back to original Worker
```

## Step 4: Directives (if IMPROVE/REDO)
1. List specific issues to fix
2. Provide actionable instructions (not vague)
3. Reference original contract criteria
4. Estimate effort for fixes

## Re-Review (after W9:Optimizer)
1. Compare with previous version
2. Check all flagged issues are addressed
3. Re-score — must improve or plateau
4. If score decreases → circuit breaker → HITL
