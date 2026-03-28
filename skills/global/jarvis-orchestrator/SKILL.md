---
name: jarvis-orchestrator
description: Meta-orchestrator: auto-analyze > DAG decompose > route to 15 Workers + 15 SubAgents.
---
---

# Goal

> **Use this skill when:** Jarvis meta-orchestration or multi-agent task routing

Điều phối mọi tác vụ phức tạp end-to-end — user chỉ cần mô tả mục tiêu → Jarvis tự phân tích complexity, phân rã thành DAG, route đến Workers chuyên biệt, giám sát Critic-Optimizer loop, và deliver kết quả production-grade.

**Workspace**: `d:\AntigravityWorkspace\_abm\`

# Instructions

## Step 0: Load Core Engine

Đọc orchestrator core engine:
```
d:\AntigravityWorkspace\_abm\Autonomous-Core\jarvis-orchestrator.md
```

## Step 1: 📥 INTAKE — Nhận & Phân loại

1. **Parse** yêu cầu → xác định intent + scope
2. **Classify** complexity bằng 5-Question Formula:

| # | Question | 1 | 2 | 3 | 4 |
|---|----------|---|---|---|---|
| 1 | Bao nhiêu domain? | 1 | 2 | 3 | 4+ |
| 2 | Bao nhiêu steps? | 1-3 | 4-6 | 7-12 | 13+ |
| 3 | Dependencies? | Không | Sequential | Some parallel | Complex DAG |
| 4 | Risk level? | Low | Medium | High | Critical |
| 5 | User input needed? | Không | 1 lần | 2-3 lần | Liên tục |

**Total (5-20)** → Size:
- **5-8 = S**: 1 Worker, direct execution
- **9-12 = M**: 1-2 Workers, sequential
- **13-16 = L**: 3-4 Workers, DAG + parallel
- **17-20 = XL**: 5+ Workers, full orchestration + HITL

3. **Confirm** với user nếu ambiguous hoặc XL

## Step 2: 🧠 PLANNING — Tạo Task DAG

Tạo Mission Control document:

```markdown
## 📋 Mission Control: [MISSION-NAME]

### Objective
[1-2 câu mô tả mục tiêu]

### Task Breakdown
| ID | Task | Worker | Depends On | Priority |
|----|------|--------|------------|----------|
| T1 | ... | Dev | — | HIGH |
| T2 | ... | UX Designer | — | HIGH |
| T3 | ... | Dev | T2 | MEDIUM |

### Parallel Groups
- **Group A** (parallel): T1, T2
- **Group B** (sequential after A): T3
```

## Step 3: 🔀 ROUTING — Chọn Worker

Load task router: `d:\AntigravityWorkspace\_abm\Workers\task-router.md`

**Quick Reference:**

| Signal | Worker | Workflows |
|--------|--------|-----------|
| code, build, debug, API | **Dev** + **QA** | /plan → /code → /test |
| write, content, SEO, blog | **Content Writer** + **SEO Optimizer** | /content-research-writer |
| business, plan, finance | **PM** + **Analyst** | /vietnam-business-planner |
| design, UI/UX | **UX Designer** + **Web Developer** | /ui-ux-pro-max |
| data, research, ETL | **Data Analyst** | /deep-research |
| security, auth, audit | **Security Evaluator** | /audit |
| deploy, docker, CI/CD | **Dev** + task-router | /deploy |
| marketing, email | **Email Marketer** | /abm-market |

**Multi-Worker Patterns:**
- Full-stack web → UX Designer → Dev → Security Evaluator → Dev (deploy)
- Content campaign → Data Analyst (research) → Content Writer → UX Designer (visuals)
- Business launch → PM (plan) + Data Analyst (research) → UX Designer (pitch) → Dev (MVP)

## Step 4: 📋 DELEGATION — Giao Task Contract

Mỗi task PHẢI có Task Contract:

```markdown
## 📋 Task Contract: [TASK-ID]
**Assigned to**: [Worker]
**Goal**: [Measurable objective]
**Input**: [Data/files/context]
**Expected Output**: [Format, quality criteria]
**Constraints**: [Scope, security, performance]
**Quality Gate**: [PASS/FAIL criteria]
```

**Rules:**
1. Mỗi Worker CHỈ 1 Contract tại 1 thời điểm
2. Input PHẢI đầy đủ — không để Worker tự đoán
3. Dependencies PHẢI resolve trước khi giao

## Step 5: 🔍 CRITIC REVIEW — Phản biện tự động

SAU MỖI task completion, **QA Worker** đánh giá:

| Dimension | Weight | Scoring |
|-----------|--------|---------|
| Correctness | 30% | Logic đúng? Bugs? |
| Completeness | 25% | Đủ requirements? |
| Quality | 20% | Professional grade? |
| Alignment | 15% | Khớp contract specs? |
| Efficiency | 10% | Tối ưu? Performance? |

| Score | Verdict | Action |
|-------|---------|--------|
| ≥ 4.5 | ✅ APPROVE | Auto-pass → Phase 7 |
| 3.5 - 4.4 | ⚠️ IMPROVE | → Fix & re-review → Phase 6 |
| < 3.5 | ❌ REDO | Send back to Worker + feedback |

## Step 6: ⚡ OPTIMIZE LOOP — Critic-Optimizer (max 3x)

```
Agent completes → QA reviews → Score ≥ 4.5? → ✅ Done
                                    ↓ NO
                   Fix & optimize → QA re-reviews → loop (max 3x)
                                    ↓ 3x fail
                   🚨 HITL → Escalate to user
```

**Circuit Breaker**: Score giảm sau optimization → STOP → HITL

## Step 7: ✅ SYNTHESIS — Deliver

1. Collect tất cả approved Task Reports
2. Synthesize thành deliverable cuối cùng
3. Final Quality Check — review toàn bộ integration
4. Report cho user + quality scores
5. Auto-generate Next Tasks nếu cần follow-up
6. Learn — Ghi lessons learned

# Examples

## Ví dụ 1: Landing Page SaaS (Complexity M)

**Input:** "Jarvis, xây landing page SaaS AI tool, dark mode, glassmorphism, deploy Vercel"

**Flow:**
```
INTAKE: Complexity M (score 11) — 3 Workers
DAG: T1:UX Designer(design) → T2:Dev(code, depends T1) → T3:Security Evaluator(scan, parallel T2) → T4:Dev(deploy)
QA: score 4.6/5 → ✅ APPROVE
SYNTHESIS: Landing page live ✅
```

## Ví dụ 2: Business Plan + Content (Complexity L)

**Input:** "Jarvis, business plan EdTech VN + blog 2000 từ + pitch deck"

**Flow:**
```
INTAKE: Complexity L (score 14) — 4 Workers
DAG:
  T1: PM + Business Analyst → TAM/SAM/SOM (parallel)
  T2: Data Analyst → Deep research (parallel with T1)
  T3: PM → BMC + Financial (after T1)
  T4: Content Writer → Blog post (after T2)
  T5: UX Designer → Pitch deck (after T3)
QA: score 4.2 → ⚠️ IMPROVE → fix → 4.7 → ✅
SYNTHESIS: Business plan + blog + pitch deck ✅
```

# Constraints

- 🚫 KHÔNG BAO GIỜ code trước khi có plan (Phase 2 bắt buộc)
- 🚫 KHÔNG BAO GIỜ skip Phase 5 (Critic Review) — MỌI output phải qua phản biện
- 🚫 KHÔNG ĐƯỢC giao Worker task ngoài domain của nó
- 🚫 Max 3 concurrent Workers, 2 SubAgents/Worker
- 🚫 Max 50,000 tokens/mission, 30 min timeout/task
- 🚫 Max 3 Critic-Optimizer iterations → HITL bắt buộc
- ✅ LUÔN LUÔN tạo Task Contract trước khi delegate
- ✅ LUÔN LUÔN chạy Security scan (Security Evaluator) song song cho code tasks
- ✅ LUÔN LUÔN require HITL cho production deployments
- ✅ Đọc full Worker/SubAgent definitions từ `d:\AntigravityWorkspace\_abm\Workers\` và `SubAgents\` khi cần chi tiết

---

📦 ABM-Workforce Multi-Agent System v3.1
🏗️ Workspace: `d:\AntigravityWorkspace\_abm\`
🧠 Orchestrator: `d:\AntigravityWorkspace\_abm\Autonomous-Core\jarvis-orchestrator.md`
📖 Full Guide: `d:\AntigravityWorkspace\_abm\HUONG-DAN-SU-DUNG.md`
