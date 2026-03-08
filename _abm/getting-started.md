# 🧠 ABM — AI Business Master

## Hệ thống Multi-Agent cho doanh nghiệp

> Jarvis là Lead Orchestrator. Bạn chỉ cần nói, Jarvis lo phần còn lại.

---

## 🚀 Cách gọi Jarvis

### Nhanh nhất — Slash Commands

| Lệnh | Tác dụng |
|-------|---------|
| **`/jarvis`** | 🧠 Gọi Jarvis — menu đầy đủ, Jarvis tự phán đoán và xử lý |
| **`/marketing`** | 📢 Viết content, email, social media, SEO |
| **`/hr`** | 👥 Viết JD, onboarding, performance review, training |
| **`/report`** | 📊 Báo cáo KPI, monthly report, data analysis |
| **`/docs`** | 📄 Proposal, SOP, meeting minutes, memo |
| **`/dev`** | 💻 Bug fix, feature, refactor code |
| **`/review`** | 🔍 Đánh giá phản biện đa chiều bất kỳ thứ gì |

### Hoặc nói trực tiếp

Bạn có thể nói bất kỳ câu nào, ví dụ:
- *"jarvis - viết JD tuyển frontend developer"*
- *"jarvis - tạo email marketing cho sản phẩm mới"*
- *"jarvis - báo cáo kinh doanh tháng 3"*

Jarvis sẽ tự classify → chọn pipeline → delegate → verify → trả kết quả.

---

## 📋 9 Task Types

| Type | Skills Auto-loaded | Agent | Pipeline |
|------|-------------------|-------|----------|
| marketing | content-strategy, copywriting, psychology | marketing-specialist | marketing-pipeline |
| hr | hr-operations, internal-comms | hr-specialist | hr-pipeline |
| report | data-analysis, office-documents | business-analyst | report-pipeline |
| docs | office-documents, brainstorming | office-manager | document-pipeline |
| bug | systematic-debugging, code-review | code-worker | bug-fix-pipeline |
| feature | writing-plans, subagent-dev, code-review | code-worker | feature-pipeline |
| refactor | writing-plans, code-review, git-worktrees | code-worker | refactor-pipeline |
| automation | workflow-automation, data-analysis | automation-engineer | document-pipeline |
| security | verification-before-completion | security-evaluator | (manual) |

---

## ⚙️ Cấu trúc hệ thống

```
G:\AGY\
├── .agents/workflows/    ← Slash commands (global)
│   ├── jarvis.md         ← /jarvis
│   ├── marketing.md      ← /marketing
│   ├── hr.md             ← /hr
│   ├── report.md         ← /report
│   ├── docs.md           ← /docs
│   ├── dev.md            ← /dev
│   └── review.md         ← /review
├── _abm/                 ← ABM Core
│   ├── bmm/agents/       ← 27 skills + 18 agents
│   ├── bmm/workflows/    ← 14 orchestration workflows
│   └── bmm/data/         ← governance, contracts, attestations
└── _abm-output/          ← Runtime output
    ├── task-log.yaml
    ├── contracts/
    └── attestations/
```

---

## 💡 4 Tips

1. **Nói ngắn gọn** — "viết JD frontend" tốt hơn "tôi muốn bạn giúp tôi viết một JD..."
2. **Dùng slash** — `/marketing` nhanh hơn giải thích
3. **Tin Jarvis** — Jarvis tự chọn pipeline, skills, agent. Bạn chỉ cần approve
4. **Escalate** — Nếu kết quả không ổn, nói "sửa lại" hoặc "escalate"
