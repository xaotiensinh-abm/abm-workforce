# Data-Aware Pipeline Workflow
# Pattern: Router → Orchestrator → MCP/Data Worker → Code Worker → Integration Verifier → Orchestrator

## Data-Aware Pipeline

Use when:
- Task requires real schema, logs, or analytics
- Database/service context needed
- MCP integration for dynamic data retrieval

### Step 1: Data Context Gathering
- Identify required data sources
- Route to Data/MCP Worker to gather:
  - Database schema
  - API endpoint specs
  - Log patterns
  - Analytics data
  - Ticket/issue context
- Worker returns structured data context

### Step 2: Code Implementation
- Provide Code Worker with:
  - Task contract
  - Data context from Step 1
  - Only relevant schema/API specs
- Worker implements changes

### Step 3: Integration Verification
- Verify integration with data sources
- Check query correctness
- Validate API contract compliance
- Test with representative data

### Step 4: Synthesis
- Aggregate results with data evidence
- Document data dependencies
- Present to user
