---
name: knowledge-crystallizer
description: "Ascension Protocol — Extract lessons from task logs, conversation history, and attestations. Crystallize into permanent knowledge items. The system learns from every task."
tags: [meta, ai, self-improvement, core]
---

## KHONG su dung khi

- Can luu nhanh -> dung save. Can review he thong -> dung multi-dimensional-review.


# 🧬 Knowledge Crystallizer — Ascension Protocol

> Adapted from CLAWDBOT's Evolver "Ascension Protocol v2.0" for the Jarvis Multi-Agent system.

**"I don't just complete tasks. I learn from them."**

## Overview

The Knowledge Crystallizer is a meta-skill that analyzes task history, identifies patterns,
and crystallizes lessons into permanent knowledge items. The system gets smarter over time.

## Khi nào sử dụng
- After completing a series of tasks (quarterly review)
- When task-log.yaml reaches 10+ entries
- After a FAIL or ESCALATION event
- Proactively by Jarvis during idle time

## The Ascension Process

### Step 1: INTROSPECT — Scan History
```
Sources to scan:
1. {output_folder}/task-log.yaml     → Task completion history
2. {output_folder}/contracts/         → All task contracts
3. {output_folder}/attestations/      → All worker attestations
4. Knowledge Items                    → Existing knowledge
5. Conversation logs                  → User feedback patterns
```

### Step 2: ANALYZE — Find Patterns
```
Pattern Types to detect:

1. FAILURE PATTERNS
   - Which tasks fail most? (type, worker, risk_level)
   - What's the retry rate? (retries > 0 → something wrong)
   - Common root causes?

2. EFFICIENCY PATTERNS
   - Average tool_calls per task type
   - Which workers are fastest?
   - Which pipeline paths are most efficient?

3. QUALITY PATTERNS
   - Average confidence scores by worker
   - First-pass accept rate
   - Human gate trigger frequency

4. KNOWLEDGE GAPS
   - Tasks that required escalation
   - Areas with no existing skills
   - Repeated questions from user
```

### Step 3: CRYSTALLIZE — Write Knowledge

For each significant pattern found:

```markdown
# Knowledge Item: [Title]

## Pattern Discovered
[What was observed in the data]

## Evidence
- Task IDs: [list]
- Data: [metrics]

## Lesson Learned
[What this means for future tasks]

## Action
- [ ] [Specific improvement to make]
- [ ] [Skill to create/update]
- [ ] [Workflow to optimize]

## Impact
[Expected improvement from applying this lesson]
```

### Step 4: PROMOTE — Update System

Based on lesson severity:

| Severity | Action |
|----------|--------|
| **Critical** | Update Jarvis rules or governance-policy.yaml |
| **Important** | Create/update a skill SKILL.md |
| **Minor** | Add to knowledge items only |
| **Optimization** | Adjust budget/concurrency defaults |

### Step 5: PERSIST — Save & Report

```
1. Save knowledge items to _abm-output/knowledge/
2. Update skill-manifest.csv if new skills created
3. Generate human report with findings
4. Log crystallization event to task-log.yaml
```

## KPI Dashboard Generation

From task-log.yaml, compute:

```markdown
# KPI Dashboard — [Period]

## Volume
| Metric | Value |
|--------|-------|
| Total tasks completed | [N] |
| Tasks by type | [breakdown] |
| Average tasks/day | [N] |

## Quality
| Metric | Value | Trend |
|--------|-------|-------|
| First-pass accept rate | [%] | [↑↓] |
| Average confidence | [0.X] | [↑↓] |
| Retry rate | [%] | [↑↓] |
| Escalation rate | [%] | [↑↓] |

## Efficiency
| Metric | Value |
|--------|-------|
| Avg tool calls per task | [N] |
| Avg time per task | [min] |
| Most used workers | [list] |
| Most used skills | [list] |

## Top Lessons Learned
1. [lesson]
2. [lesson]
```

## Safety Rules

- ❌ NEVER modify Jarvis agent files without human approval
- ❌ NEVER delete existing knowledge — only ADD
- ❌ NEVER auto-deploy changes to production
- ✅ ALWAYS generate human-readable report
- ✅ ALWAYS include evidence for every lesson
- ✅ ALWAYS version changes (git commit)
