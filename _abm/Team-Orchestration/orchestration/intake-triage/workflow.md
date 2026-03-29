# Intake & Triage Workflow
# First step in every task — classify, assess risk, select pattern

## Intake & Triage Protocol

When Jarvis receives a new task from the user, follow this workflow:

### Step 1: Understand Intent
- Read the user's request completely
- Identify: what is being asked (action) + what is the target (subject)
- Clarify any ambiguity BEFORE proceeding

### Step 2: Classify Task
Classify into one of:
| Type | Keywords |
|------|----------|
| bug | fix, broken, error, regression, crash |
| feature | new, add, create, implement, build |
| refactor | refactor, migrate, restructure, clean, rename |
| ui | UI, frontend, design, visual, layout, CSS |
| infra | deploy, CI/CD, config, env, docker, k8s |
| data | schema, migration, query, database, API data |
| docs | document, readme, guide, tutorial, explain |
| security | auth, permissions, secrets, vulnerability |

### Step 3: Assess Risk
| Level | Triggers |
|-------|----------|
| low | docs, simple bug, 1-2 files, no auth/payment |
| medium | feature, multi-file, refactor |
| high | auth, payments, production config, infra |
| critical | secrets, IAM, DB schema, data loss risk |

### Step 4: Estimate Complexity
- **Simple**: 1-2 files, clear acceptance criteria
- **Moderate**: 3-10 files, some cross-cutting concerns
- **Complex**: 10+ files, multi-domain, architectural impact

### Step 5: Select Pattern
| Complexity | Risk | Pattern |
|-----------|------|---------|
| Simple | Low | Single agent (Code Worker only) |
| Simple | Medium | Code Worker + Test Verifier |
| Moderate | Low-Med | Orchestrator → Code → Test |
| Moderate | High | Orchestrator → Code → Test → Security → Human |
| Complex | Any | Full pipeline with parallel workers |

### Step 6: Assemble Team
Select workers from the agent pool:
- Amelia (Dev) — code changes
- Quinn (QA) — test verification
- Browser Subagent — UI verification
- Shield (Security) — security audit
- Paige (Tech Writer) — documentation
- Winston (Architect) — architecture decisions
- John (PM) — requirements clarification
- Mary (Analyst) — analysis/research
- Bob (SM) — sprint/story management

### Step 7: Present Triage Report
Output a structured triage report to the user with:
- Task classification
- Risk level
- Recommended pattern
- Worker team
- Estimated effort
- Any concerns or questions

Wait for user confirmation before proceeding to delegation.
