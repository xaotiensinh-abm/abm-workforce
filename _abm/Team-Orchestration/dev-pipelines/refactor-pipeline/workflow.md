# Refactor Pipeline Workflow
# Pattern: Router → Orchestrator → Impact Analysis → Code Workers → Static Analysis/Test → Risk Evaluator → Orchestrator

## Refactor Pipeline

Use when:
- Wide-impact code restructuring
- Migration between patterns/frameworks
- Need to avoid hidden regressions

### Step 1: Impact Analysis
- Identify all affected files and modules
- Map dependencies and call chains
- Estimate blast radius
- Flag high-risk areas (auth, payments, data)

### Step 2: Create Phased Plan
- Break refactor into atomic, verifiable steps
- Each step must leave system in working state
- Each step has its own contract and acceptance criteria

### Step 3: Execute Phase by Phase
For each phase:
- Create contract for Code Worker
- Worker executes within defined scope
- Run static analysis after each phase
- Verify no regressions after each phase

### Step 4: Static Analysis
- Run lint, type check, unused code detection
- Compare before/after static analysis results
- Flag any degradation

### Step 5: Risk Evaluation
- If high-risk areas touched: route to Security Evaluator
- Check for behavioral changes in test results
- Verify API contracts maintained

### Step 6: Synthesis
- Aggregate all phase results
- Show before/after comparison
- Present risk assessment
- Walkthrough explaining refactor rationale and effects
