# 🧠 ABM Workforce — AI Business Master

> **Hệ thống AI đa agent điều phối doanh nghiệp — biến AI thành đội ngũ nhân sự thực sự.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-36-blue.svg)](_abm/_config/skill-manifest.csv)
[![Language](https://img.shields.io/badge/Language-Vietnamese-red.svg)](.gemini/RULES.md)

---

## 📋 Giới thiệu

**ABM Workforce** là nền tảng AI Multi-Agent được xây dựng theo mô hình **Chuỗi Ủy Quyền (Delegation Chain Management)** — nơi mọi task đều có hợp đồng, bằng chứng, và trách nhiệm rõ ràng.

Hệ thống do **Jarvis** — Trưởng Điều Phối tối cao — quản lý toàn bộ đội ngũ agent chuyên biệt, từ marketing đến HR, từ phát triển đến phân tích dữ liệu.

### Tại sao ABM Workforce?

| Vấn đề | Giải pháp ABM |
|--------|--------------|
| AI chạy lung tung, không kiểm soát | Hợp đồng → Thực hiện → Chứng nhận → Xác minh |
| Output không đáng tin cậy | Luật Sắt: Bằng chứng trước khi khẳng định |
| Trách nhiệm không rõ ràng | Chuỗi trách nhiệm luôn đi lên: Agent → Worker → Jarvis → CEO |
| AI trả lời tiếng Anh, khó hiểu | 100% tiếng Việt, dễ hiểu với mọi người dùng |
| Cần nhớ quá nhiều lệnh | Slash commands đơn giản: `/jarvis`, `/marketing`, `/hr`... |

---

## 🏗️ Kiến trúc hệ thống

```
ABM Workforce
├── 🧠 Jarvis (Trưởng Điều Phối)
│   ├── Delegation Chain Protocol
│   ├── 17 Task Routes
│   └── 5 Tier System
│
├── 👥 SubAgents (5 agent chuyên biệt)
│   ├── Marketing Specialist
│   ├── HR Specialist
│   ├── Business Analyst
│   ├── Office Manager
│   └── Security Evaluator
│
├── 🔧 Workers (10 worker kỹ thuật)
│   ├── Code Worker
│   ├── QA Worker
│   └── ...
│
├── 📚 Knowledge Base (36 skills)
│   ├── Hệ thống (3): delegation-chain, verification, context-engineering
│   ├── Meta (5): skill-creator, knowledge-crystallizer, multi-dimensional-review...
│   ├── Marketing (15): product-marketing-context, page-cro, cold-email, pricing-strategy...
│   ├── Phát triển (7): code-review, systematic-debugging, writing-plans...
│   ├── Văn phòng (4): hr-operations, office-documents, internal-comms...
│   └── Phân tích (2): data-analysis, workflow-automation
│
├── 🧠 Second-Brain (Bộ nhớ dài hạn)
│   ├── memory/ — Lịch sử phiên làm việc
│   ├── patterns/ — Mẫu thành công + thất bại
│   ├── standards/ — Tiêu chuẩn tài liệu
│   └── evolution/ — Tri thức tích lũy + lịch sử tiến hóa
│
└── ⚡ Global Workflows (7 slash commands)
    ├── /jarvis — Menu đầy đủ
    ├── /marketing — Nội dung, email, social, SEO
    ├── /hr — Tuyển dụng, onboarding, đánh giá
    ├── /report — Báo cáo KPI, phân tích dữ liệu
    ├── /docs — Đề xuất, SOP, biên bản
    ├── /dev — Sửa bug, tính năng, refactor
    └── /review — Đánh giá phản biện đa chiều
```

---

## 🔥 Quy tắc tối thượng — Delegation Chain

```
┌──────────────────┐  hợp_đồng  ┌──────────────────┐  hợp_đồng  ┌──────────────────┐
│ Jarvis           │────────────▶│ Worker           │────────────▶│ SubAgent         │
│ (Orchestrator)   │  chứng_nhận │ (Người thực hiện)│  chứng_nhận │ (Người phụ)      │
│                  │◀────────────│                  │◀────────────│                  │
└──────────────────┘             └──────────────────┘             └──────────────────┘
       ▲                                                                │
       │         Giao việc đi xuống  ───────────────────▶               │
       │         ◀───────────────────  Trách nhiệm đi lên             │
       └────────────────────────────────────────────────────────────────┘
```

**6 bước bắt buộc:** Tạo hợp đồng → Chọn worker → Thực hiện → Chứng nhận → Xác minh → Giải quyết trách nhiệm

---

## 🚀 Cài đặt

### Yêu cầu

- **IDE**: [Antigravity](https://antigravity.google) hoặc bất kỳ IDE hỗ trợ `.gemini/` rules
- **OS**: Windows / macOS / Linux
- **Git**: Để clone và quản lý phiên bản

### Bước 1: Clone dự án

```bash
git clone https://github.com/YOUR_USERNAME/abm-workforce.git
cd abm-workforce
```

### Bước 2: Cấu trúc đã sẵn sàng

Hệ thống **không cần cài đặt dependencies** — toàn bộ là markdown files và YAML configs.

```
abm-workforce/
├── .gemini/          ← Rules toàn cục (tự động apply)
│   ├── RULES.md      ← Kỷ luật sắt + Quy tắc tối thượng
│   └── settings.json ← Cấu hình ngôn ngữ
├── .agents/          ← Slash commands
│   └── workflows/    ← /jarvis, /marketing, /hr...
├── _abm/             ← Core system
│   ├── bmm/          ← Agents + Skills + Workflows
│   ├── _config/      ← Manifests
│   └── Context-Layer/← Second-Brain + Knowledge Base
└── _abm-output/      ← Kết quả runtime (auto-generated)
```

### Bước 3: Tùy chỉnh

1. Mở `_abm/bmm/config.yaml` → sửa `user_name` thành tên của bạn
2. Mở `_abm/Context-Layer/Second-Brain/patterns/ceo-preferences.yaml` → sửa preferences
3. (Tùy chọn) Thêm skills mới bằng `/jarvis` → skill-creator

---

## 💡 Cách sử dụng

### Cách 1: Slash Commands (Đơn giản nhất)

| Lệnh | Khi nào dùng | Ví dụ |
|-------|-------------|-------|
| `/jarvis` | Menu đầy đủ, điều phối tổng | "Tôi cần phân tích đối thủ" |
| `/marketing` | Viết content, email, social | "Viết email marketing cho sản phẩm X" |
| `/hr` | Tuyển dụng, JD, onboarding | "Viết JD cho vị trí Marketing Manager" |
| `/report` | Báo cáo, KPI, phân tích | "Báo cáo doanh thu tháng 3" |
| `/docs` | Đề xuất, SOP, biên bản | "Viết SOP quy trình tuyển dụng" |
| `/dev` | Bug, feature, refactor | "Sửa bug đăng nhập" |
| `/review` | Đánh giá phản biện | "Đánh giá hệ thống CRM" |

### Cách 2: Nói trực tiếp

Không cần nhớ lệnh — chỉ cần mô tả yêu cầu bằng tiếng Việt:

```
"Viết email marketing giới thiệu sản phẩm mới"
→ Jarvis tự phân loại → marketing → load skills → thực hiện

"Tạo JD cho vị trí Backend Developer"
→ Jarvis tự phân loại → hr → load skills → thực hiện
```

### Luồng công việc chi tiết

```
Bạn gõ yêu cầu
       │
       ▼
┌─────────────────┐
│ 1. PHÂN LOẠI    │  Jarvis xác định loại task (marketing, hr, dev...)
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 2. CHỌN SKILLS  │  Load tối đa 3 skills phù hợp (tự động)
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 3. TẠO HỢP ĐỒNG│  Objective + Scope + Criteria + Budget
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 4. THỰC HIỆN    │  Agent làm việc trong phạm vi hợp đồng
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 5. XÁC MINH     │  Kiểm tra bằng chứng + tiêu chí + phạm vi
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 6. TRÌNH CEO    │  Kết quả + bằng chứng → Bạn quyết định
└─────────────────┘
```

---

## 📊 36 Skills

### Hệ thống & Meta (8)

| Skill | Mô tả |
|-------|-------|
| `delegation-chain` | Giao thức cốt lõi: Hợp đồng → Chứng nhận → Xác minh |
| `verification-before-completion` | LUẬT SẮT: Bằng chứng trước khi khẳng định |
| `context-engineering` | Lắp ráp ngữ cảnh 5 lớp + kiểm soát token |
| `skill-creator` | Tạo skills mới — 7 pha: thu thập → tối ưu → đăng ký |
| `multi-dimensional-review` | Đánh giá 6 bước + 8 góc phản biện |
| `knowledge-crystallizer` | Tinh chế tri thức từ lịch sử tasks |
| `capability-evolver` | Tự tiến hóa hệ thống |
| `memory-keeper` | Sao lưu ngữ cảnh quan trọng |

### Marketing (15)

| Skill | Mô tả |
|-------|-------|
| `product-marketing-context` | ★ Nền tảng — 12 sections, mọi skill đọc trước |
| `copywriting` | Copy chuyên nghiệp cho mọi kênh |
| `content-strategy` | Chiến lược nội dung + lịch đăng bài |
| `cold-email` | B2B outreach + follow-up 5 bước |
| `page-cro` | Tối ưu chuyển đổi — 7 trụ cột |
| `pricing-strategy` | Chiến lược giá — Van Westendorp + tâm lý giá |
| `launch-strategy` | Ra mắt sản phẩm — ORB Framework + 5 phase |
| `sales-enablement` | Sales deck + battle cards + demo script |
| `revops` | Lead scoring + pipeline + lifecycle |
| `ab-test-setup` | Thiết kế A/B test data-driven |
| `churn-prevention` | Ngăn rời bỏ — cancel flow + dunning |
| `email-marketing` | Chuỗi email tự động |
| `social-content` | Hook social media + tái sử dụng nội dung |
| `marketing-psychology` | 50+ mô hình tâm lý thuyết phục |
| `seo-audit` | SEO kỹ thuật + on-page |

### Phát triển (7)
`code-review` · `systematic-debugging` · `writing-plans` · `subagent-driven-development` · `dispatching-parallel-agents` · `finishing-a-development-branch` · `git-worktrees`

### Văn phòng & HR (4)
`hr-operations` · `office-documents` · `internal-comms` · `brainstorming`

### Phân tích (2)
`data-analysis` · `workflow-automation`

---

## 🧠 Second-Brain

Bộ nhớ dài hạn giúp Jarvis **học từ kinh nghiệm** và **cải thiện liên tục**.

| Tầng | Mục đích | File |
|------|---------|------|
| **Memory** | Lịch sử phiên + context snapshots | `sessions.yaml`, `context-snapshots.yaml` |
| **Patterns** | Mẫu thành công + thất bại + preferences | `success-patterns.yaml`, `failure-patterns.yaml`, `ceo-preferences.yaml` |
| **Standards** | Tiêu chuẩn tài liệu | `documentation-standards.yaml` |
| **Evolution** | Tri thức tích lũy + lịch sử tiến hóa | `crystallized-knowledge.yaml`, `capability-log.yaml` |

---

## 📝 Ví dụ sử dụng

### Marketing — Viết email cold outreach

```
/marketing Viết email cold outreach cho sản phẩm SaaS quản lý nhân sự,
đối tượng: giám đốc HR các công ty 50-200 nhân viên
```

Jarvis sẽ:
1. Load skills: `cold-email`, `product-marketing-context`, `marketing-psychology`
2. Kiểm tra `product-marketing-context.md` (nếu chưa có → tạo mới)
3. Viết email theo 5 nguyên tắc cold email
4. Tạo follow-up sequence 5 bước
5. Trả kết quả có benchmarks (open rate, reply rate)

### HR — Viết JD

```
/hr Viết JD cho vị trí Senior Frontend Developer,
stack: React, TypeScript, Next.js
```

### Đánh giá — Review hệ thống

```
/review Đánh giá phản biện website hiện tại từ góc nhìn CRO
```

---

## 🤝 Đóng góp

1. Fork dự án
2. Tạo branch: `git checkout -b feature/ten-tinh-nang`
3. Commit: `git commit -m "feat: mô tả thay đổi"`
4. Push: `git push origin feature/ten-tinh-nang`
5. Tạo Pull Request

### Thêm skill mới

Dùng `/jarvis` → chọn chế độ `skill-creator` → theo 7 pha:
1. Thu thập intent
2. Phỏng vấn chi tiết
3. Viết SKILL.md
4. Test cases
5. Đánh giá
6. Tối ưu description
7. Đăng ký vào manifest

---

## 📜 License

MIT License — xem file [LICENSE](LICENSE)

---

## 👤 Tác giả

**DũngTQ** — Kiến trúc sư ABM Workforce

- 📱 Liên hệ: **0976 202 028**
- 🏗️ Nền tảng gốc: Phát triển sâu từ BMAD-METHOD
- 🎯 Sứ mệnh: Biến AI thành đội ngũ nhân sự thực sự cho doanh nghiệp Việt Nam

---

<p align="center">
  <b>ABM Workforce</b> — AI Business Master<br>
  <i>Kỷ luật sắt. Bằng chứng thật. Kết quả đo được.</i>
</p>
