---
name: systematic-debugging
description: Use when facing bugs, test failures, or unexpected behavior. Structured approach to root cause analysis instead of random trial-and-error.
---

# Systematic Debugging

> Adapted from [supercent-io/skills-template](https://github.com/supercent-io/skills-template) for the Jarvis Multi-Agent system.

## Overview

Never debug randomly. Follow a systematic process to identify root cause,
then fix with verification.

**Core principle:** Understand before fixing. Root cause before patches.

## The Process

### Step 1: REPRODUCE
```
Before fixing anything:
1. Can you reproduce the bug consistently?
2. What are the EXACT steps to trigger it?
3. What is the EXACT error message / behavior?
4. What is the EXPECTED behavior?

If you can't reproduce it → gather more information first
```

### Step 2: ISOLATE
```
Narrow down the problem:
1. Which file(s) are involved?
2. Which function(s)?
3. Which line(s)?
4. Is it data-dependent?
5. Is it timing-dependent?

Techniques:
- Binary search (comment out half the code)
- Add logging at key points
- Check recent git changes: git log --oneline -10
- git bisect if regression
```

### Step 3: HYPOTHESIZE
```
Form specific, testable hypotheses:
- "The bug happens because X returns null when Y is empty"
- "The race condition occurs because A completes before B"

NOT vague: "something is wrong with the data flow"
```

### Step 4: TEST HYPOTHESIS
```
For each hypothesis:
1. How would you prove it true?
2. How would you prove it false?
3. What's the simplest test?

Run the test. One hypothesis at a time.
```

### Step 5: FIX
```
1. Write a regression test that captures the bug (must FAIL)
2. Apply the minimal fix
3. Run the regression test (must PASS)
4. Run full test suite (no regressions)
5. Verify original reproduction steps no longer trigger bug
```

### Step 6: VERIFY (Iron Law)
```
Use verification-before-completion skill:
1. Run the regression test
2. Run the full test suite
3. Try the original reproduction steps
4. ONLY THEN claim the bug is fixed
```

## Delegation Chain Integration

### For Bug Fix Pipeline
```
1. Jarvis receives bug report
2. Dispatch to Code Worker with contract:
   - objective: "Debug and fix: {bug description}"
   - acceptance_criteria:
     - "Root cause identified"
     - "Regression test written (red-green verified)"
     - "Fix applied and all tests pass"
   - required_artifacts: ["root_cause_analysis", "regression_test", "test_result"]
3. Worker follows this skill's process
4. Worker returns attestation with:
   - Root cause analysis
   - Regression test (with red-green evidence)
   - Fix description
   - Full test suite results
5. Jarvis verifies (verification-before-completion skill)
```

## Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| Random code changes | Systematic hypothesis testing |
| "Try this and see" | "If my hypothesis is right, then..." |
| Fix symptoms | Fix root cause |
| Skip regression test | Always write one |
| "It works now" | "Here's the test proving it works" |
| Debug in production | Reproduce locally first |
