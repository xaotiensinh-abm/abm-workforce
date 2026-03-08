# Verification Chain Workflow
# 3-layer verification protocol for worker attestations

## Verification Chain Protocol

### Layer 1: Syntactic Verification
Automated checks on code quality:

1. **Test Suite**: Run all tests mentioned in attestation `tests_run`
   - All tests must pass
   - Check for new test coverage on changed files
   - Verify no existing tests were removed

2. **Lint/Format**: Verify code quality
   - ESLint pass (if configured)
   - Prettier format check (if configured)
   - No new lint warnings introduced

3. **Type Check**: Verify type safety
   - TypeScript compilation (if applicable)
   - No new type errors

### Layer 2: Behavioral Verification
Functional correctness checks:

1. **Acceptance Criteria**: Check each criterion from the Task Contract
   - Map each criterion to evidence in the attestation
   - Mark: MET / PARTIAL / NOT MET

2. **Browser Verification** (if UI changes):
   - Trigger Browser QA Subagent
   - Verify visual rendering
   - Check interaction flows
   - Capture screenshots as evidence

3. **Integration**: Cross-cutting concerns
   - API contracts maintained
   - Database interactions correct
   - External service calls valid

### Layer 3: Policy Verification
Governance and compliance checks:

1. **Scope Compliance**: Did worker stay within contract scope?
   - Check `files_changed` against `scope_in`
   - Flag any files in `scope_out` that were modified

2. **Security Review** (if high/critical risk):
   - Route to Security Evaluator (Shield)
   - Wait for security attestation
   - Any CRITICAL finding → STOP and escalate

3. **Human Gate** (if required by governance policy):
   - Present Review Changes to human
   - Present Walkthrough with evidence
   - Wait for human approval

### Verification Decision Matrix

| Layer 1 | Layer 2 | Layer 3 | Decision |
|---------|---------|---------|----------|
| ✅ | ✅ | ✅ | ACCEPT |
| ✅ | ✅ | ⚠️ (non-critical) | ACCEPT_WITH_RISKS |
| ✅ | ⚠️ | ✅ | RETRY (partial criteria) |
| ❌ | * | * | RETRY (fix tests) |
| * | * | 🛑 (critical security) | ESCALATE to human |
| ❌ | ❌ | * | FAIL → ROLLBACK |
