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

## 9 loại công việc Jarvis xử lý

| Loại | Skills tự động load | Agent | Pipeline |
|------|---------------------|-------|----------|
| 📢 marketing | content-strategy, copywriting, marketing-psychology | marketing-specialist | marketing-pipeline |
| 👥 hr | hr-operations, internal-comms | hr-specialist | hr-pipeline |
| 📊 report | data-analysis, office-documents | business-analyst | report-pipeline |
| 📄 docs | office-documents, brainstorming | office-manager | document-pipeline |
| 🐛 bug | systematic-debugging, code-review | code-worker | bug-fix-pipeline |
| ✨ feature | writing-plans, subagent-dev, code-review | code-worker | feature-pipeline |
| 🔄 refactor | writing-plans, code-review, git-worktrees | code-worker | refactor-pipeline |
| ⚙️ automation | workflow-automation, data-analysis | automation-engineer | document-pipeline |
| 🔒 security | verification-before-completion | security-evaluator | (thủ công) |

---

## Quy trình hoạt động

```
CEO nói yêu cầu
    ↓
Jarvis phân tích → xác định task_type
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

| Thư mục | Số files | Mô tả |
|---------|----------|-------|
| `SubAgents/` | 5 | Agent chuyên biệt: marketing, HR, office, automation, analyst |
| `Workers/` | 10 | Worker kỹ thuật: dev, QA, PM, architect... |
| `Autonomous-Core/` | 41 | Jarvis engine + consciousness model (7 files) |
| `Team-Orchestration/` | 14 | 14 workflow pipeline: dev + business + orchestration |
| `Context-Layer/` | 53 | CoreModules + Knowledge-Base (27 skills) + Second-Brain |
| `_design-specs/` | 149 | Đặc tả thiết kế pipeline chi tiết |
| `Outputs/` | 6 | Task log + contracts + attestations |
