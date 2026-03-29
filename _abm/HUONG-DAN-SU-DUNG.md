# 🇻🇳 Hướng Dẫn Sử Dụng — ABM Workforce

## Cách gọi Jarvis nhanh nhất

### Slash Commands

| Lệnh | Chức năng | Agent xử lý |
|-------|----------|-------------|
| `/jarvis` | 🧠 Menu đầy đủ — Jarvis tự phân tích và xử lý | Jarvis |
| `/marketing` | 📢 Content, email, social media, SEO | marketing-specialist |
| `/hr` | 👥 JD, onboarding, đánh giá, đào tạo | hr-specialist |
| `/report` | 📊 Báo cáo KPI, phân tích dữ liệu | business-analyst |
| `/docs` | 📄 Đề xuất, SOP, biên bản, ghi nhớ | office-manager |
| `/dev` | 💻 Sửa bug, tính năng mới, refactor | code-worker |
| `/review` | 🔍 Đánh giá phản biện đa chiều | Jarvis + review skill |

### Nói trực tiếp

Bạn có thể nói bất kỳ câu nào bằng tiếng Việt:

```
"jarvis - viết JD tuyển frontend developer, lương 15-25 triệu"
"jarvis - tạo email marketing giới thiệu sản phẩm mới"
"jarvis - báo cáo kinh doanh tháng 3, doanh thu 2.5 tỷ"
"jarvis - viết SOP quy trình onboarding nhân viên mới"
"jarvis - đánh giá phản biện toàn bộ hệ thống"
```

---

## 23 loại công việc Jarvis xử lý

### Dev & Kỹ thuật
| Loại | Skills tự động load | Agent |
|------|---------------------|-------|
| 🐛 bug | systematic-debugging, code-review | code-worker |
| ✨ feature | writing-plans, subagent-dev, code-review | code-worker |
| 🔄 refactor | writing-plans, code-review, git-worktrees | code-worker |
| 🖼️ ui | writing-plans, subagent-driven-development | code-worker |
| 🏗️ infra | writing-plans, verification-before-completion | code-worker |
| 🔒 security | verification-before-completion | security-evaluator |

### Marketing & Bán hàng
| Loại | Skills tự động load | Agent |
|------|---------------------|-------|
| 📢 marketing | content-strategy, copywriting, marketing-psychology | marketing-specialist |
| 🎯 seo-planning | seo-content-planner, seo-audit, content-creator | marketing-specialist |
| 💰 sales | cold-email, sales-automator, sales-enablement | marketing-specialist |
| 💲 pricing | pricing-strategy, page-cro, marketing-psychology | marketing-specialist |
| 🚀 launch | launch-strategy, content-strategy, email-marketing | marketing-specialist |
| 📈 cro | page-cro, ab-test-setup, marketing-psychology | marketing-specialist |
| 🔄 retention | churn-prevention, email-marketing, data-analysis | marketing-specialist |

### Phân tích & Nghiên cứu
| Loại | Skills tự động load | Agent |
|------|---------------------|-------|
| 📊 report | data-analysis, office-documents | business-analyst |
| 🏟️ competitive | competitive-landscape, competitor-intelligence, market-sizing | business-analyst |
| 🔬 research | deep-research, data-analysis, competitive-landscape | business-analyst |
| 🚀 startup | startup-analyst, market-sizing, financial-modeling | business-analyst |

### Hệ thống & Vận hành
| Loại | Skills tự động load | Agent |
|------|---------------------|-------|
| 👥 hr | hr-operations, internal-comms | hr-specialist |
| 📄 docs | office-documents, brainstorming | office-manager |
| ⚙️ automation | workflow-automation, data-analysis | automation-engineer |
| 📊 data | data-analysis, workflow-automation | business-analyst |
| 🔧 improvement | kaizen, agent-improve, capability-evolver | jarvis |

---

## Quy trình hoạt động

```
CEO nói yêu cầu
    ↓
Jarvis phân tích → xác định task_type (23 loại)
    ↓
Skill Routing → load skills phù hợp (tối đa 3)
    ↓
Agent Routing → chọn agent xử lý
    ↓
Tạo Task Contract (hợp đồng công việc)
    ↓
Agent thực hiện → trả Attestation (chứng nhận)
    ↓
Jarvis xác minh evidence → IRON LAW
    ↓
Trả kết quả cho CEO
```

---

## 4 Mẹo sử dụng

1. **Nói ngắn gọn** — "viết JD frontend" tốt hơn giải thích dài dòng
2. **Dùng slash** — `/marketing` nhanh hơn mô tả
3. **Tin Jarvis** — Jarvis tự chọn pipeline, skills, agent. Bạn chỉ cần duyệt
4. **Nói "sửa lại"** — Nếu kết quả chưa ổn, chỉ cần nói và Jarvis sẽ cải thiện

---

## Cấu trúc thư mục

| Thư mục | Nội dung | Mô tả |
|---------|----------|-------|
| `bmm/agents/skills/` | 48 skills | Kỹ năng chuyên biệt cho từng domain |
| `SubAgents/` | 5 agents | marketing, HR, office, automation, analyst |
| `Workers/` | 10 workers | dev, QA, PM, architect, security... |
| `Autonomous-Core/` | 41 files | Jarvis engine + consciousness model |
| `Team-Orchestration/` | 14 pipelines | dev + business + orchestration workflows |
| `Context-Layer/` | 53 files | Second-Brain + Knowledge-Base |
| `_design-specs/` | 149 files | Đặc tả thiết kế pipeline chi tiết |
| `Outputs/` | runtime | Task log + contracts + attestations |
