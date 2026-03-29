---
name: skill-creator
description: "Creates and iteratively improves skills for the ABM (AI Business Master) system. Use whenever: user says 'create a skill', 'make this a skill', 'turn this into a workflow', detected repeated pattern >3x, or Capability Evolver signals 'New pattern'. Guides through intent capture, interview, drafting, testing, evaluation, and description optimization."
tags: [meta, core, ai, self-improvement]
---

## KHONG su dung khi

- Can review skill -> dung multi-dimensional-review. Can cai thien agent -> dung agent-improve.


# 🏭 Skill Creator v2.0

> Adapted from [Anthropic's skill-creator](https://skills.sh/anthropics/skills/skill-creator) for ABM.

The process of creating a skill goes like this:
1. Capture what the user wants the skill to do
2. Interview for edge cases and details
3. Write a draft SKILL.md
4. Create test cases and run them
5. Evaluate results, improve, repeat
6. Optimize the description for triggering

Figure out where the user is in this process and help them progress. Be flexible — if they already have a draft, skip to step 4. If they say "just do it", skip the tests.

## Phase 1: CAPTURE INTENT

Start by understanding what the user wants. The conversation might already contain a workflow to capture (e.g., "turn this into a skill"). If so, extract answers from conversation history first:

1. **What** should this skill enable Jarvis/agents to do?
2. **When** should it trigger? (user phrases, contexts, task_types)
3. **Output** — what's the expected format?
4. **Testing** — should we set up test cases?
   - Objectively verifiable outputs (file transforms, data extraction, workflows) → YES
   - Subjective outputs (writing style, creative work) → usually NO

## Phase 2: INTERVIEW & RESEARCH

Proactively ask about:
- Edge cases and error handling
- Input/output formats
- Success criteria
- Dependencies on other skills
- Which existing ABM skills relate to this

Check existing skills for overlap:
```
Read: {project-root}/_abm/_config/skill-manifest.csv
Check: Is there already a skill for this? → Enhance, don't duplicate.
```

## Phase 3: WRITE SKILL.md

### Anatomy of an ABM Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── references/  — docs loaded into context as needed
    ├── templates/   — output templates
    └── examples/    — usage examples
```

### Progressive Disclosure (3 levels)

| Level | What | Size | When loaded |
|-------|------|------|-------------|
| 1. Metadata | name + description | ~100 words | ALWAYS in context |
| 2. SKILL.md body | Full instructions | <500 lines | When skill triggers |
| 3. Bundled resources | references/, templates/ | Unlimited | On demand, as needed |

Keep SKILL.md under 500 lines. If approaching limit, add hierarchy with references/.

### Writing Guide

**Use imperative form.** Explain WHY things matter rather than heavy-handed MUSTs.

**Description is critical** — it determines whether the skill triggers. Make descriptions slightly "pushy" to combat under-triggering. Include both what the skill does AND specific contexts/phrases that should use it.

```yaml
# ❌ Too narrow:
description: "Creates data analysis reports"

# ✅ Good — pushy, with trigger phrases:
description: "Creates data analysis reports with KPI dashboards and insights.
Use this skill whenever: user mentions 'report', 'KPI', 'metrics', 'dashboard',
'data analysis', 'monthly report', or asks to analyze any business data."
```

**Define output formats explicitly:**
```markdown
## Report Structure
ALWAYS use this exact template:
# [Title]
## Executive Summary
## Key Findings
## Recommendations
```

**Include examples:**
```markdown
## Example
Input: "Phân tích doanh thu Q1"
Output: Business report with KPI dashboard, trend analysis, 3 recommendations
Skills used: data-analysis + office-documents
```

### Frontmatter Template

```yaml
---
name: {kebab-case-name}
description: "{what it does}. Use whenever: {trigger phrases and contexts}."
tags: [{category}, {subcategory}]
---
```

## Phase 4: TEST CASES

Create 2-3 realistic test prompts — what a CEO would actually say:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt (realistic)",
      "expected_output": "Description of expected result",
      "success_criteria": ["criterion 1", "criterion 2"]
    }
  ]
}
```

Save to: `{project-root}/_abm-output/skill-evals/{skill-name}/evals.json`

Present test cases to user: "Here are test cases I'd like to try. Look right, or want to add more?"

## Phase 5: EVALUATE & ITERATE

The iteration loop:
1. **Run** each test case mentally through the skill
2. **Score** each result against success_criteria
3. **Identify** gaps: what didn't work? Why?
4. **Rewrite** the relevant section of SKILL.md
5. **Repeat** until satisfied

Ask the user after each iteration:
- "Does this output match what you expected?"
- "What would you change?"
- "Are we ready to ship, or should we iterate?"

## Phase 6: DESCRIPTION OPTIMIZATION

After the skill works well, optimize description for triggering:

1. Generate 5-10 trigger phrases users might say
2. Check: does the description cover all of them?
3. Add missing trigger phrases to description
4. Keep description concise but comprehensive

## Phase 7: REGISTER IN ABM

Follow the standard ABM registration process:

```
1. Save to: _abm/bmm/agents/skills/{name}/SKILL.md
2. Update: _abm/_config/skill-manifest.csv (add row)
3. Assign category: system | development | marketing | office | analytics | meta
4. If skill needs routing: Update <skill-routing> in jarvis-orchestrator.md
5. If skill serves a task_type: Update <agent-routing> if needed
6. Log creation in task-log.yaml
7. Present to human for final review
```

## Quality Checklist

Before publishing, verify:
- [ ] Description ≤ 200 chars with trigger phrases
- [ ] SKILL.md < 500 lines
- [ ] Steps are specific and actionable (imperative form)
- [ ] At least 1 output template
- [ ] All configurable values parameterized (no hardcoded values)
- [ ] At least 1 usage example
- [ ] Related skills listed
- [ ] Name is kebab-case, unique in manifest
- [ ] Does NOT duplicate existing skill functionality

## Safety Rules
- ✅ ALWAYS present generated skill to human before activating
- ✅ ALWAYS add to skill-manifest.csv
- ❌ NEVER overwrite existing skills without approval
- ❌ NEVER auto-activate without human review
- ❌ NEVER create skills that could be deceptive or malicious

## Integration
- **capability-evolver** — detects pattern → triggers skill-creator
- **knowledge-crystallizer** — extracts lessons → feeds into new skill templates
- **context-engineering** — new skills follow progressive disclosure for token efficiency
