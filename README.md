# 🏢 ABM Workforce — Văn Phòng Số Thông Minh

> **Hệ sinh thái AI Agent nâng cao năng suất doanh nghiệp — 9 phòng ban, 71 kỹ năng, 1 bộ não điều phối.**

[![Version](https://img.shields.io/badge/Version-2.6-purple.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-71-blue.svg)](_abm/_config/skill-manifest.csv)
[![Workflows](https://img.shields.io/badge/Workflows-14-green.svg)](.agents/workflows/)
[![Routes](https://img.shields.io/badge/Routes-26-orange.svg)](_abm/bmm/agents/jarvis-orchestrator.md)
[![Language](https://img.shields.io/badge/Language-Vietnamese_100%25-red.svg)](.gemini/RULES.md)

---

## 🆕 What's New — v2.6 (10/03/2026)

| Thay đổi | Chi tiết |
|---------|----------|
| 🧠 **BMAD Upgrade** | 5 skills chiến lược từ feedback cộng đồng BMAD |
| 🏗️ **Project Hierarchy** | State Machine + Context Inheritance: Epic → Feature → Story. Chống loạn não |
| 🏃 **Sprint Planning** | Pipeline PRD → Epic → Story → Sprint. Gate reviews, T-shirt sizing, MoSCoW |
| 🗄️ **Database Management** | Schema design, migration protocol, SQL/NoSQL patterns |
| 🧠 **Critical Thinking** | Meta-skill phản biện: Devil's Advocate, 5 Whys, First Principles, Pre-mortem |
| 🕸️ **Knowledge Graph** | Entities, relationships, cognee integration. Nâng cấp từ flat KB |
| 🎨 **Creative Strategist** | SubAgent mới: tư duy sáng tạo TRIZ + rejected ideas backlog |
| 👥 **Council Workflow** | `/council` — hội đồng đánh giá multi-agent + scoring rubric |
| 📊 **Review Score** | 8.33 → **9.08/10** sau BMAD upgrade |

---

## Tại sao ABM Workforce?

| Vấn đề doanh nghiệp | Giải pháp ABM |
|---------------------|--------------|
| Mỗi phòng ban dùng AI kiểu khác | **9 phòng ban** với agent + skills + workflow riêng |
| AI chạy lung tung, không kiểm soát | **Hợp đồng → Thực hiện → Chứng nhận → Xác minh** |
| Output không đáng tin cậy | **Luật Sắt**: Bằng chứng trước khi khẳng định |
| Cần nhớ quá nhiều lệnh | **13 slash commands**: `/jarvis`, `/marketing`, `/sales`... |
| AI trả lời tiếng Anh | **100% tiếng Việt**, dễ hiểu với mọi nhân viên |

---

## 📋 9 Phòng Ban — Mapping Hoàn Chỉnh

```
                         🧠 CEO
                          │
                    ⚡ Jarvis Lead Orchestrator
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
  ┌────┴────┐       ┌────┴────┐       ┌────┴────┐
  │  🏛 BGĐ  │       │  📣 MKT │       │  💻 IT  │
  │  100%   │       │  100%   │       │  100%   │
  └─────────┘       └─────────┘       └─────────┘
  ┌─────────┐       ┌─────────┐       ┌─────────┐
  │ 👥 HC-NS │       │ 🤝 KD   │       │ 💬 CSKH │
  │  80%    │       │  80%    │       │  80%    │
  └─────────┘       └─────────┘       └─────────┘
  ┌─────────┐       ┌─────────┐       ┌─────────┐
  │ 💰 Kế Toán│      │ 📦 Vận Hành│     │ ⚖️ Pháp Chế│
  │  80%    │       │  30%    │       │  50%    │
  └─────────┘       └─────────┘       └─────────┘
```

| Phòng ban | Agent | Workflow | Skills chính |
|-----------|-------|----------|-------------|
| 🏛 **Ban Giám Đốc** | Jarvis + business-analyst | `/jarvis`, `/review` | brainstorming, writing-plans, data-analysis, pptx, multi-dimensional-review |
| 👥 **Hành Chính - Nhân Sự** | hr-specialist, office-manager | `/hr`, `/docs` | hr-operations, docx, xlsx, task-planning, internal-comms |
| 💰 **Kế Toán - Tài Chính** | business-analyst | `/finance`, `/report` | xlsx, pdf, data-analysis, startup-financial-modeling |
| 📣 **Marketing - Truyền Thông** | marketing-specialist | `/marketing` | copywriting, content-strategy, social-content, seo-audit, page-cro |
| 🤝 **Kinh Doanh - Bán Hàng** | marketing-specialist | `/sales` | cold-email, sales-enablement, pricing-strategy, pptx, docx |
| 💬 **Chăm Sóc Khách Hàng** | — | `/cskh` | agent-email-cli, churn-prevention, email-marketing, copywriting |
| 💻 **IT - Công Nghệ** | automation-engineer | `/dev` | code-review, systematic-debugging, frontend-developer, vercel-react-best-practices |
| 📦 **Vận Hành - Logistics** | automation-engineer | — | workflow-automation, data-analysis |
| ⚖️ **Pháp Chế - Tuân Thủ** | — | `/legal` | docx, office-documents, pdf |

---

## 🚀 Bắt Đầu Trong 2 Phút

### 1. Clone

```bash
git clone https://github.com/xaotiensinh-abm/abm-workforce.git
cd abm-workforce
```

### 2. Mở trong IDE

Mở bằng **Antigravity**, **Cursor**, hoặc IDE hỗ trợ `.gemini/` rules.

> Không cần cài dependencies — toàn bộ là markdown + YAML.

### 3. Gõ lệnh đầu tiên

```
/jarvis
```

Jarvis sẽ online và sẵn sàng nhận việc.

---

## 💡 13 Slash Commands

### Điều phối

| Lệnh | Phòng ban | Ví dụ |
|-------|----------|-------|
| `/jarvis` | Tổng điều phối | "Phân tích đối thủ X" |
| `/review` | Đánh giá phản biện | "Review hệ thống CRM" |
| `/save` | Lưu trạng thái | "Lưu tiến độ hôm nay" |

### Phòng ban

| Lệnh | Phòng ban | Ví dụ |
|-------|----------|-------|
| `/marketing` | Marketing | "Viết email marketing cho sản phẩm X" |
| `/sales` | Kinh Doanh | "Tạo proposal cho khách hàng Y" |
| `/hr` | Nhân Sự | "Viết JD cho vị trí Frontend Developer" |
| `/finance` | Kế Toán | "Báo cáo doanh thu Q1" |
| `/legal` | Pháp Chế | "Soạn hợp đồng lao động" |
| `/cskh` | CSKH | "Email follow-up khách hàng bỏ giỏ hàng" |
| `/docs` | Văn phòng | "Viết SOP quy trình tuyển dụng" |
| `/report` | Báo cáo | "Báo cáo KPI tuần" |
| `/dev` | IT | "Sửa bug đăng nhập" |
| `/skill-sync` | Hệ thống | "Sync skills mới từ community" |

### Hoặc nói trực tiếp

```
"Viết email cold outreach cho sản phẩm SaaS"
→ Jarvis tự phân loại → marketing → load 3 skills → thực hiện → trả kết quả
```

---

## 📊 66 Skills — 10 Nhóm

### 🔒 Hệ thống & Meta (9)

| Skill | Chức năng |
|-------|----------|
| `delegation-chain` | Giao thức cốt lõi: Hợp đồng → Chứng nhận → Xác minh |
| `verification-before-completion` | LUẬT SẮT: Bằng chứng trước khi khẳng định |
| `context-engineering` | Lắp ráp ngữ cảnh 5 lớp + kiểm soát token |
| `skill-creator` | Tạo skills mới — 7 pha |
| `multi-dimensional-review` | Đánh giá 6 bước + 8 góc phản biện |
| `knowledge-crystallizer` | Tinh chế tri thức từ lịch sử |
| `capability-evolver` | Tự tiến hóa hệ thống |
| `memory-keeper` | Sao lưu ngữ cảnh |
| `save` | Lưu trạng thái: task/daily/milestone save |

### 📣 Marketing — Content & Sales (16)

`product-marketing-context` · `copywriting` · `content-strategy` · `social-content` · `email-marketing` · `marketing-psychology` · `page-cro` · `seo-audit` · `ab-test-setup` · `cold-email` · `sales-enablement` · `revops` · `pricing-strategy` · `launch-strategy` · `churn-prevention` · `seo-content-planner`

### 🔧 Phát triển (10)

`subagent-driven-development` · `dispatching-parallel-agents` · `writing-plans` · `code-review` · `systematic-debugging` · `finishing-a-development-branch` · `git-worktrees` · `project-hierarchy` · `sprint-planning` · `database-management`

### 🌐 Web Development (7)

`ui-ux-pro-max` · `frontend-design` · `frontend-developer` · `vercel-react-best-practices` · `web-design-guidelines` · `vercel-composition-patterns` · `canvas-design`

### 📁 Văn Phòng Số (6)

| Skill | Tạo file | Thư viện |
|-------|---------|---------|
| `docx` | Word (.docx) | python-docx |
| `xlsx` | Excel (.xlsx) | openpyxl |
| `pdf` | PDF (.pdf) | fpdf2 + PyPDF2 |
| `pptx` | PowerPoint (.pptx) | python-pptx |
| `agent-email-cli` | Email tự động | SMTP / Resend API | 🛡️ Sandbox mặc định |
| `task-planning` | Kế hoạch công việc | WBS + T-shirt sizing |

### 👥 Văn Phòng & HR (4)

`hr-operations` · `office-documents` · `internal-comms` · `brainstorming`

### 📈 Phân Tích (8)

`data-analysis` · `workflow-automation` · `competitive-landscape` · `market-sizing-analysis` · `startup-analyst` · `deep-research` · `competitor-intelligence` · `knowledge-graph`

### 🧠 Bổ Sung Nâng Cao (6)

`multi-agent-brainstorming` · `kaizen` · `agent-improve` · `content-creator` · `startup-financial-modeling` · `sales-automator`

### 🎨 Multimedia (4)

`imagen` · `veo-video-gen` · `grok-imagen` · `freepik-spaces`

---

## 🔥 Chuỗi Ủy Quyền — Quy Tắc Tối Thượng

```
Bạn gõ yêu cầu
       │
       ▼
┌─────────────────┐
│ 1. PHÂN LOẠI    │  Jarvis xác định loại task
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 2. CHỌN SKILLS  │  Load tối đa 3 skills phù hợp
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 3. TẠO HỢP ĐỒNG│  Objective + Scope + Criteria
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 4. THỰC HIỆN    │  Agent làm việc trong phạm vi
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 5. XÁC MINH     │  Kiểm tra bằng chứng
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 6. TRÌNH CEO    │  Kết quả → Bạn quyết định
└─────────────────┘
```

**Trách nhiệm luôn đi LÊN**: SubAgent → Worker → Jarvis → CEO

---

## 🏗️ Cấu Trúc Thư Mục

```
abm-workforce/
├── .gemini/              ← Rules toàn cục (100% tiếng Việt)
├── .agents/workflows/    ← 13 slash commands
├── _abm/
│   ├── bmm/
│   │   ├── agents/       ← Jarvis + 5 SubAgents
│   │   │   └── skills/   ← 66 skills (SKILL.md)
│   │   └── config.yaml
│   ├── _config/          ← skill-manifest.csv
│   ├── SubAgents/        ← 5 agent chuyên biệt
│   ├── Workers/          ← 10 worker kỹ thuật
│   ├── Context-Layer/
│   │   ├── Knowledge-Base/  ← 66 KB entries
│   │   └── Second-Brain/    ← Bộ nhớ dài hạn
│   └── Team-Orchestration/  ← 14 workflow pipelines
├── _abm-output/          ← Kết quả runtime
└── docs/                 ← Tài liệu mở rộng
```

---

## 🧠 Second-Brain — Bộ Nhớ Dài Hạn

| Tầng | Mục đích |
|------|---------|
| **Memory** | Lịch sử phiên + context snapshots |
| **Patterns** | Mẫu thành công/thất bại + CEO preferences |
| **Standards** | Tiêu chuẩn tài liệu |
| **Evolution** | Tri thức tích lũy + lịch sử tiến hóa |

Dùng `/save` để lưu trạng thái công việc vào Second-Brain.

---

## 📝 Ví Dụ Sử Dụng

### Marketing — Cold Email B2B

```
/marketing Viết email cold outreach cho SaaS quản lý nhân sự,
đối tượng: giám đốc HR công ty 50-200 nhân viên
```

### Kế Toán — Báo Cáo Doanh Thu

```
/finance Tạo báo cáo doanh thu Q1/2026 dạng Excel,
có biểu đồ xu hướng + so sánh YoY
```

### HR — Viết JD

```
/hr Viết JD cho vị trí Senior Frontend Developer,
stack: React, TypeScript, Next.js. Remote-first.
```

### IT — Review Code

```
/dev Review performance cho ProductPage.tsx,
tối ưu load time và bundle size
```

### Pháp Chế — Soạn Hợp Đồng

```
/legal Soạn hợp đồng hợp tác kinh doanh B2B,
giữa công ty A và công ty B, thời hạn 12 tháng
```

---

## 🤝 Đóng Góp

1. Fork dự án
2. Tạo branch: `git checkout -b feature/ten-tinh-nang`
3. Commit: `git commit -m "feat: mô tả thay đổi"`
4. Push + tạo Pull Request

### Thêm skill mới

```
/jarvis → skill-creator → 7 pha: thu thập → phỏng vấn → viết → test → đánh giá → tối ưu → đăng ký
```

---

## 📜 License

MIT License — xem file [LICENSE](LICENSE)

---

## 👤 Tác Giả

**DũngTQ** — Kiến trúc sư ABM Workforce

- 📱 Liên hệ: **0976 202 028**
- 🎯 Sứ mệnh: Biến AI thành đội ngũ nhân sự thực sự cho doanh nghiệp Việt Nam

---

<p align="center">
  <b>ABM Workforce v2.6</b> — Văn Phòng Số Thông Minh<br>
  <i>71 Skills · 26 Routes · 14 Workflows · 6 SubAgents · 9 Phòng Ban · 100% Tiếng Việt</i><br>
  <i>Kỷ luật sắt. Bằng chứng thật. Kết quả đo được.</i>
</p>
