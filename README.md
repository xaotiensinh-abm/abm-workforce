# 🚀 ABM-Workforce v3.0

> **Agile AI-Driven Multi-Agent Development Framework**
> 10 Workers · 143 Skills · 94 Workflows · 4-Phase Methodology · 9-Layer Skill Engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![ABM-Workforce Banner](banner-bmad-method.png)

---

🌐 **[English](#-what-is-abm-workforce)** | **[Tiếng Việt](#-abm-workforce-là-gì)**

---

## 🎯 What is ABM-Workforce?

ABM-Workforce is a production-grade **multi-agent AI development framework** designed for [Google Antigravity](https://blog.google/technology/google-labs/project-mariner-gemini-ai-agent/) and compatible AI coding assistants. It provides:

- **10 Specialized AI Workers** — CodeAgent, ContentAgent, BusinessAgent, DesignAgent, DataAgent, SecurityAgent, OpsAgent, CriticAgent, OptimizerAgent, WorkspaceAgent
- **143 Skills** — Production-grade instruction sets with 9-Layer quality compliance
- **94 Workflows** — End-to-end task automation from analysis to deployment
- **4-Phase Methodology** — Analysis → Planning → Solutioning → Implementation

## 🎯 ABM-Workforce là gì?

ABM-Workforce là một **framework phát triển đa tác tử AI chuẩn production**, được thiết kế cho [Google Antigravity](https://blog.google/technology/google-labs/project-mariner-gemini-ai-agent/) và các trợ lý AI coding tương thích. Framework cung cấp:

- **10 Worker AI chuyên biệt** — CodeAgent (lập trình), ContentAgent (nội dung), BusinessAgent (kinh doanh), DesignAgent (thiết kế), DataAgent (dữ liệu), SecurityAgent (bảo mật), OpsAgent (vận hành), CriticAgent (đánh giá), OptimizerAgent (tối ưu), WorkspaceAgent (Google Workspace)
- **143 Skills** — Bộ kỹ năng chuẩn production với 9 tầng kiểm soát chất lượng
- **94 Workflows** — Tự động hoá toàn bộ quy trình từ phân tích đến triển khai
- **Phương pháp 4 Giai đoạn** — Phân tích → Lập kế hoạch → Thiết kế giải pháp → Triển khai

---

## 🏗️ 9-Layer Skill Engineering | Kỹ thuật Skill 9 tầng

Mỗi skill tuân thủ framework chất lượng nghiêm ngặt:

| Tầng | Tên | Mục đích |
|:----:|-----|----------|
| L0 | Use Case & Trigger Map | Khi nào kích hoạt skill này |
| L1 | Metadata | Phiên bản, worker phụ trách, mức trưởng thành, tags |
| L2 | Core SKILL.md | Hướng dẫn, ràng buộc, quy tắc hoạt động |
| L3 | References | Thư viện tri thức nền của domain |
| L4 | Examples | Happy Path / Edge Case / Anti-Example |
| L5 | Scripts & Tools | Scripts xác thực, tự động hoá |
| L6 | Assets & Templates | Templates đầu ra mẫu |
| L7 | Output Contract | Rubric chất lượng & yêu cầu format |
| L8 | Governance | CHANGELOG, theo dõi phiên bản, chủ sở hữu |

**Trạng thái hiện tại: 🏆 138/138 skills đạt Tier S (Trưởng thành) — Điểm sức khoẻ 100/100**

---

## 📁 Cấu trúc Repository

```
abm-workforce/
├── rules/                   # Luật tối thượng & Tiêu chuẩn lập trình
│   ├── GEMINI.md            # ABM Supreme Rules v3.0
│   └── AGENTS.md            # Kỷ luật coding workspace
│
├── skills/                  # 143 Skills chuẩn Production
│   ├── _standards/          # Framework 9-Layer & Quản trị
│   │   ├── SKILL-TEMPLATE-V2.md    # Template chuẩn tạo skill mới
│   │   ├── USER-GUIDE.md           # Hướng dẫn sử dụng đầy đủ
│   │   ├── governance/             # Registry trưởng thành, quy trình audit
│   │   ├── output-contracts/       # Hợp đồng chất lượng theo domain
│   │   └── scripts/                # Scanner kiểm tra sức khoẻ skill
│   ├── global/              # 80 Global Skills
│   └── workspace/           # 57 Workspace Skills
│
├── workflows/               # 94 Workflows tự động
│   ├── abm-*.md             # 31 workflows phương pháp ABM
│   └── *.md                 # 63 workflows chuyên biệt
│
├── _abm/                    # Định nghĩa session & persona ABM
├── docs/                    # Tài liệu
└── scripts/                 # Scripts cài đặt & tiện ích
```

---

## ⚡ Bắt đầu nhanh | Quick Start

### 1. Clone & Cài đặt

```bash
git clone https://github.com/xaotiensinh-abm/abm-workforce.git
cd abm-workforce
```

### 2. Cài đặt cho Google Antigravity

Sao chép skills và workflows vào workspace Antigravity:

```powershell
# Windows (PowerShell)
# Sao chép Global Skills
Copy-Item -Recurse skills\global\* "$env:USERPROFILE\.gemini\antigravity\skills\"

# Sao chép Workspace Skills
Copy-Item -Recurse skills\workspace\* "D:\AntigravityWorkspace\.agent\skills\"

# Sao chép Workflows
Copy-Item workflows\* "$env:USERPROFILE\.gemini\antigravity\global_workflows\"

# Sao chép Rules
Copy-Item rules\GEMINI.md "$env:USERPROFILE\.gemini\GEMINI.md"
```

```bash
# macOS/Linux
cp -r skills/global/* ~/.gemini/antigravity/skills/
cp -r skills/workspace/* ~/.gemini/antigravity/.agent/skills/
cp -r workflows/* ~/.gemini/antigravity/global_workflows/
cp rules/GEMINI.md ~/.gemini/GEMINI.md
```

### 3. Kiểm tra cài đặt

```bash
# Chạy scanner kiểm tra sức khoẻ skill
python skills/_standards/scripts/skill_health_check.py ~/.gemini/antigravity/skills
```

---

## 🧠 Bảng đăng ký Worker | Worker Registry

| Worker | Vai trò | Skills chính |
|--------|---------|-------------|
| **W1: CodeAgent** | Kỹ sư Full-Stack | react-expert, typescript-expert, nestjs-expert, database-expert |
| **W2: ContentAgent** | Chiến lược gia nội dung | viet-pro, seo-content-writer, copywriting |
| **W3: BusinessAgent** | Tư vấn kinh doanh | business-analyst, pricing-strategy, market-sizing |
| **W4: DesignAgent** | Giám đốc sáng tạo | ui-ux-pro-max, css-expert, nano-banana-pro |
| **W5: DataAgent** | Kỹ sư dữ liệu & Tự động hoá | rag-engineer, web-scraper, python-excel-pro |
| **W6: SecurityAgent** | Kỹ sư bảo mật | vulnerability-scanner, auth-expert, api-security |
| **W7: OpsAgent** | Kỹ sư DevOps | docker-expert, kubernetes-architect, terraform |
| **W8: CriticAgent** | Cố vấn chất lượng | code-review, find-bugs, oracle |
| **W9: OptimizerAgent** | Tự động sửa lỗi | self-correction-engine, refactoring-expert |
| **W10: WorkspaceAgent** | Google Workspace | gws-gmail, gws-drive, gws-calendar, gws-sheets |

---

## 📋 Phương pháp ABM (4 Giai đoạn)

### Giai đoạn 1: Phân tích (Analysis)
> Khám phá ý tưởng, nghiên cứu thị trường, phân tích domain
```
/abm-brainstorm → /abm-research → /abm-market → /abm-brief
```

### Giai đoạn 2: Lập kế hoạch (Planning)
> Viết tài liệu yêu cầu sản phẩm, thiết kế UX, xác nhận quality gates
```
/abm-prd → /abm-ux → /abm-validate
```

### Giai đoạn 3: Thiết kế giải pháp (Solutioning)
> Thiết kế kiến trúc, tạo epics & stories, kiểm tra sẵn sàng
```
/abm-arch → /abm-epics → /abm-readiness
```

### Giai đoạn 4: Triển khai (Implementation)
> Lập sprint, implement từng story, review chất lượng
```
/abm-sprint → /abm-story → /abm-dev → /abm-review
```

### Luồng nhanh (Quick Flow) — Cho tác vụ đơn giản
> Bỏ qua giai đoạn 1-3, đi thẳng vào code
```
/abm-quick-spec → /abm-quick-dev → /test
```

---

## 🔧 Danh mục Workflows chính

| Danh mục | Workflows | Mô tả |
|----------|-----------|-------|
| **Lập trình** | `/code`, `/debug`, `/test`, `/deploy`, `/refactor`, `/audit` | Viết code, sửa lỗi, kiểm thử, triển khai |
| **AI Media** | `/gemini-3-image-prompt`, `/veo-fashion-director`, `/wildlife-director` | Tạo ảnh/video AI chuyên nghiệp |
| **Kinh doanh** | `/vietnam-business-planner`, `/sales-pipeline`, `/finance-ops` | Kế hoạch KD, pipeline bán hàng, tài chính |
| **Nội dung** | `/content-research-writer`, `/novel-writer`, `/viet-pro` | Nghiên cứu & viết content, truyện, bài viết SEO |
| **DevOps** | `/deploy`, `/cloudflare-tunnel`, `/init` | Triển khai, quản lý tunnel, khởi tạo dự án |
| **Điều phối** | `/jarvis`, `/adaptive-routing`, `/agent-manager`, `/deep-research` | Điều phối đa tác tử, nghiên cứu chuyên sâu |
| **Google Workspace** | `/gws-setup` | Cài đặt & quản lý Google Workspace (Gmail, Drive, Sheets...) |

---

## 📊 Bảng điều khiển sức khoẻ Skill | Skill Health Dashboard

Hệ sinh thái skill được giám sát bởi scanner tự động:

```bash
python skills/_standards/scripts/skill_health_check.py <đường_dẫn_thư_mục_skills>
```

Kết quả bao gồm:
- Điểm tuân thủ 9-layer cho từng skill
- Phân loại mức trưởng thành (S/A/B/C)
- Điểm sức khoẻ tổng hợp (0-100)
- Đề xuất nâng cấp cụ thể

---

## 🏗️ Kiến trúc hệ thống | System Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    USER REQUEST                          │
└──────────────┬───────────────────────────────────────────┘
               ▼
┌──────────────────────────────────────────────────────────┐
│              ABM SUPREME RULES (GEMINI.md)               │
│     Plan Before Code · Context Management · Worker-      │
│         Driven · Security First · Verify Before Done     │
└──────────────┬───────────────────────────────────────────┘
               ▼
┌──────────────────────────────────────────────────────────┐
│           WORKFLOW ENGINE (94 Workflows)                  │
│                                                          │
│  ┌─────────┐ ┌──────────┐ ┌─────────┐ ┌──────────────┐ │
│  │ Phase 1 │→│ Phase 2  │→│ Phase 3 │→│   Phase 4    │ │
│  │Analysis │ │ Planning │ │Solution │ │Implementation│ │
│  └─────────┘ └──────────┘ └─────────┘ └──────────────┘ │
│                                                          │
│  Quick Flow: /abm-quick-spec → /abm-quick-dev → /test   │
└──────────────┬───────────────────────────────────────────┘
               ▼
┌──────────────────────────────────────────────────────────┐
│              10 SPECIALIZED WORKERS                       │
│                                                          │
│  W1:Code  W2:Content  W3:Business  W4:Design  W5:Data   │
│  W6:Security  W7:Ops  W8:Critic  W9:Optimizer  W10:GWS  │
│                                                          │
│           ┌──────── 143 Skills (Tier S) ────────┐       │
│           │  9-Layer Compliance · Health 100/100 │       │
│           └─────────────────────────────────────┘       │
└──────────────────────────────────────────────────────────┘
```

---

## 🇻🇳 Tính năng đặc biệt cho Việt Nam

ABM-Workforce được tối ưu cho thị trường Việt Nam:

- **Viết content tiếng Việt** — `/viet-pro` với Anti-AI Engine, 6 pipeline (Fiction, Article, Education, Presentation, Research, Social Media)
- **Kế hoạch kinh doanh VN** — `/vietnam-business-planner` tích hợp pháp lý VN, văn hoá VN, xu hướng thị trường
- **Thiết kế MEP** — `/mep-project` cho nhà máy công nghiệp (HVAC, PCCC, Điện, Cấp thoát nước)
- **Đấu thầu MEP** — `/tender-mep` quy trình đấu thầu theo chuẩn Việt Nam
- **AI Media Việt** — `/sora2-tvc-vietnam` tạo TVC cho thị trường VN
- **Quản lý tài chính** — `/finance-ops` chuẩn kế toán Việt Nam
- **Nhân sự** — `/hr-manager` tuân thủ Luật Lao động VN

---

## 🤝 Đóng góp | Contributing

Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết hướng dẫn:
- Thêm skill mới (bắt buộc dùng `SKILL-TEMPLATE-V2.md`)
- Tạo workflow mới
- Gửi Pull Request

### Quy tắc đóng góp:
1. Mỗi skill mới **PHẢI** tuân thủ 9-Layer framework
2. Chạy `skill_health_check.py` trước khi gửi PR
3. Đạt tối thiểu **Tier A** để được merge

---

## 📄 Giấy phép | License

Dự án được cấp phép theo MIT License — xem file [LICENSE](LICENSE).

---

## 🏗️ Xây dựng với | Built With

- [Google Antigravity](https://blog.google/technology/google-labs/project-mariner-gemini-ai-agent/) — AI Coding Agent
- [BMAD Method](https://github.com/bmad-method/bmad-method) — Agile AI Development (upstream)
- ABM-Workforce v3.0 — Hệ sinh thái đa tác tử AI Việt Nam

---

## 📈 Lịch sử phát triển | Changelog

| Phiên bản | Ngày | Thay đổi chính |
|-----------|------|----------------|
| v3.0 | 2026-03-28 | 9-Layer Skill Engineering, 138 skills Tier S, Health 100/100 |
| v2.0 | 2026-03 | 10 Workers, 94 Workflows, 4-Phase Methodology |
| v1.0 | 2026-02 | Fork BMAD-Method, ABM customizations |

---

*ABM-Workforce v3.0 × Antigravity*
*"Agile AI-Driven Multi-Agent Development"*
*🏆 138/138 Skills đạt Tier S — Điểm sức khoẻ 100/100*
