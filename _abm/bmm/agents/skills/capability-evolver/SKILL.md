---
name: capability-evolver
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Self-evolution engine — Analyze task logs and history to identify improvements. Fix broken processes, crystallize knowledge, generate new skills automatically. The Ascension Protocol."
tags: [meta, ai, self-improvement, core]
---

## KHONG su dung khi

- Can tao skill moi -> dung skill-creator. Can review he thong -> dung multi-dimensional-review.


# 🧬 Capability Evolver — Self-Evolution Engine

> Adapted from CLAWDBOT's [Evolver Ascension Protocol v2.0](https://github.com/obra/) for the Jarvis Multi-Agent system.

**"I don't just complete tasks. I write the rules that make future tasks easier."**

## Overview

The Capability Evolver is a meta-skill that allows Jarvis to inspect its own runtime history,
identify failures or inefficiencies, and autonomously improve the system by:
- Writing new skills
- Updating governance rules
- Optimizing pipeline routing
- Extracting lessons learned

## Khi nào sử dụng (Triggers)
- **Hoàn thành Non-trivial Workflow**: Khi một task tốn > 5 tool calls thành công và phức tạp
- **User Correction**: Khi user phải chỉnh sửa/phản hồi > 2 lần để đạt kết quả đúng
- **Task Lặp Lại**: Khi nhận ra pattern giống hệt các task trong quá khứ (task history analysis)
- After every 10 completed tasks (via HEARTBEAT)
- After FAIL or ESCALATION event
- When user requests "optimize", "improve", hoặc "tự động hóa workflow này"

## The Ascension Protocol

### Phase 1: INTROSPECT
```
Scan for signals:
1. task-log.yaml → failure patterns, retry rates, confidence scores
2. attestations/ → worker performance, scope violations
3. governance-policy violations → security findings
4. User feedback patterns → repeated corrections, dissatisfaction signals
5. Skill usage frequency → which skills used most/least
```

### Phase 2: DIAGNOSE
```
Pattern Classification:
| Pattern | Signal | Action |
|---------|--------|--------|
| Tác vụ phức tạp thành công | > 5 tool calls, kết quả tốt | Đóng gói thành Skill mới |
| User correction | User phải sửa sai agent nhiều lần | Cập nhật Skill hiện tại (Pitfalls/Rules) |
| Repeated failure | Same task_type fails >2x | Investigate root cause |
| High retry rate | avg retries > 1.0 | Worker skill gap |
| Low confidence | avg confidence < 0.7 | Need better acceptance criteria |
| Scope violations | scope_out files touched | Tighten contract scope |
| Human escalation spike | >30% tasks escalated | Governance too strict OR too risky |
| Skill not used | skill loaded 0x in 20 tasks | Remove or improve discovery |
| New pattern | Repeated task type without skill | Create new skill |
```

### Phase 3: EVOLVE
```
Based on diagnosis:

FIX: For broken processes
- Update governance-policy.yaml
- Adjust default budget in contract template
- Add constraint to agent AGENTS.md

CRYSTALLIZE: For new knowledge
- Run knowledge-crystallizer skill
- Create KNOWLEDGE_BASE entry

CONDENSE (Context Condensation): For long-running memory
- Khi conversation history quá dài (>10,000 tokens), kích hoạt nén bộ nhớ.
- Tạo/Cập nhật file `.agents/memory/goals.md` chứa tóm tắt tiến trình và file quan trọng.
- Xóa bớt log không cần thiết.

GENERATE (Inspired by Hermes `skill_manage`): For new capabilities
1. Analyze successful execution path → extract tool sequence & parameters.
2. Auto-generate `SKILL.md` (ABM Format: Goal, Triggers, Output format).
3. Đặt vào thư mục `_quarantine` hoặc dán nhãn `Draft`.
4. **REVIEW GATE**: Yêu cầu CEO approve trước khi chuyển thành Active Skill.
5. Đăng ký vào `skill-manifest.csv`.

UPDATE: Nâng cấp Skill hiện có
- Thêm "Quy tắc sắt" (Pitfalls) dựa trên lỗi vừa gặp.
- Tối ưu hóa "Quy trình" (Procedure) để giảm số bước.

OPTIMIZE: For efficiency
- Adjust ROMA tier routing rules
- Update concurrency limits
- Modify worker team defaults
```

### Phase 4: VALIDATE
```
Before applying any change:
1. Document the change + rationale
2. Compare old vs new behavior (predicted)
3. Present to human for approval (ALWAYS)
4. Apply change
5. Monitor next 5 tasks for regression
6. Rollback if regression detected
```

### Phase 5: PERSIST
```
1. Git commit all changes
2. Update HEARTBEAT.md with new checks
3. Log evolution event to task-log.yaml
4. Generate human-readable report
```

## Evolution Report Template

```markdown
# 🧬 Evolution Report — [Date]

## Signals Detected
| Signal | Count | Severity |
|--------|-------|----------|

## Changes Made
| # | Type | What Changed | Rationale |
|---|------|-------------|-----------|

## Expected Impact
[Predicted improvement]

## Monitoring Plan
[What to watch for next 5 tasks]
```

## Safety & Risk Protocol (MANDATORY)

| Risk | Level | Mitigation |
|------|-------|------------|
| Hallucinated fixes | Medium | ALWAYS require human approval before applying changes |
| Infinite recursion | High | Evolver MUST NOT spawn itself. Single execution only. |
| Breaking good processes | Medium | Compare metrics before/after. Rollback if regression. |
| Overoptimization | Low | Review changes with user quarterly |

## Integration with Other Skills

- **knowledge-crystallizer** — Handles the CRYSTALLIZE step
- **memory-keeper** — Runs backup BEFORE any evolution
- **verification-before-completion** — Validates changes actually improve things
- **prompt-sentinel** — Khi phát hiện prompt quality issue (low confidence, failures) → chạy prompt-sentinel review trước khi sửa
