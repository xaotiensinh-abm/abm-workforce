---
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
name: verification-before-completion
description: IRON LAW — Evidence before claims, always. Use BEFORE claiming any work is complete, fixed, or passing. Run verification and confirm output before making success claims.
---

## KHONG su dung khi

- Skill bat buoc - luon active. Khong co truong hop khong su dung.


# Verification Before Completion

> Adapted from [obra/superpowers](https://github.com/obra/superpowers) for the Jarvis Multi-Agent system.

## Overview

Claiming work is complete without verification is dishonesty, not efficiency.

**Core principle:** Evidence before claims, always.

**Violating the letter of this rule is violating the spirit of this rule.**

## The Iron Law

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you haven't run the verification command in this message, you cannot claim it passes.

## The Gate Function

```
BEFORE claiming any status or expressing satisfaction:

1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
   - If NO: State actual status with evidence
   - If YES: State claim WITH evidence
5. ONLY THEN: Make the claim

Skip any step = lying, not verifying
```

## Common Failures

| Claim | Requires | Not Sufficient |
|-------|----------|----------------|
| Tests pass | Test command output: 0 failures | Previous run, "should pass" |
| Linter clean | Linter output: 0 errors | Partial check, extrapolation |
| Build succeeds | Build command: exit 0 | Linter passing, logs look good |
| Bug fixed | Test original symptom: passes | Code changed, assumed fixed |
| Worker completed | VCS diff + test run | Worker attestation says "done" |
| Requirements met | Line-by-line checklist | Tests passing alone |
| Contract fulfilled | Evidence per criterion | Worker confidence score |

## Integration with Delegation Chain

This skill is **MANDATORY** at these points:

1. **Worker completing attestation**: Worker MUST run verification before setting `status: done`
2. **Jarvis verifying attestation**: Jarvis MUST re-run tests independently, not trust worker's claim
3. **Synthesis output**: Before presenting walkthrough to human, verify ALL evidence is fresh
4. **Rollback verification**: After rollback, MUST verify system is in clean state

### Attestation Verification Checklist
```
Before accepting any attestation:
□ Worker provided test command output? (not just "tests pass")
□ Evidence files exist at stated paths?
□ Confidence score backed by evidence?
□ Scope violations checked against contract?
□ Re-run at least one verification command independently?
```

## Red Flags — STOP Immediately

- Using "should", "probably", "seems to"
- Expressing satisfaction before verification ("Great!", "Perfect!", "Done!")
- About to commit/push without verification
- Trusting worker attestation without independent check
- Relying on partial verification
- Thinking "just this once"

## When To Apply

**ALWAYS before:**
- ANY variation of success/completion claims  
- ANY expression of satisfaction
- Accepting worker attestation
- Creating synthesis/walkthrough
- Committing, PR creation, task completion
- Moving to next task in pipeline
