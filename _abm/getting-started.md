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

## 📋 23 Task Types (tự động routing)

### Kinh doanh & Phân tích
| Type | Agent | Khi nào |
|------|-------|---------|
| competitive | business-analyst | Phân tích đối thủ, cạnh tranh |
| research | business-analyst | Nghiên cứu chuyên sâu |
| startup | business-analyst | Phân tích kinh doanh, financial modeling |
| report | business-analyst | Báo cáo KPI, data analysis |

### Marketing & Sales
| Type | Agent | Khi nào |
|------|-------|---------|
| marketing | marketing-specialist | Content, copywriting, chiến lược |
| seo-planning | marketing-specialist | SEO content plan, topic clusters |
| sales | marketing-specialist | Cold email, follow-up, proposals |
| pricing | marketing-specialist | Chiến lược giá, CRO |
| launch | marketing-specialist | Ra mắt sản phẩm |
| cro | marketing-specialist | Tối ưu chuyển đổi |
| retention | marketing-specialist | Giảm churn, email marketing |

### Dev & Vận hành
| Type | Agent | Khi nào |
|------|-------|---------|
| bug | code-worker | Sửa bug |
| feature | code-worker | Tính năng mới |
| refactor | code-worker | Refactor code |
| hr | hr-specialist | JD, onboarding, review |
| docs | office-manager | SOP, proposal, memo |
| automation | automation-engineer | Tự động hóa workflow |
| improvement | jarvis | Cải tiến hệ thống, tối ưu agent |

---

## ⚙️ Cấu trúc hệ thống

```
G:\AGY\
├── .agents/workflows/    ← Slash commands (8 lệnh)
│   ├── jarvis.md         ← /jarvis
│   ├── marketing.md      ← /marketing
│   ├── hr.md             ← /hr
│   ├── report.md         ← /report
│   ├── docs.md           ← /docs
│   ├── dev.md            ← /dev
│   ├── review.md         ← /review
│   └── skill-sync.md     ← /skill-sync (NEW)
├── _abm/                 ← ABM Core
│   ├── bmm/agents/skills/ ← 48 skills
│   ├── bmm/workflows/    ← 14 orchestration workflows
│   ├── TOP-10-SKILLS.md  ← Quick Start Guide (NEW)
│   └── CHANGELOG.md      ← Lịch sử thay đổi (NEW)
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

## 📚 Tài Liệu Thêm

- [TOP-10-SKILLS.md](_abm/TOP-10-SKILLS.md) — Bắt đầu nhanh với 10 skills hay dùng nhất
- [HUONG-DAN-SU-DUNG.md](_abm/HUONG-DAN-SU-DUNG.md) — Hướng dẫn chi tiết
- [CHANGELOG.md](_abm/CHANGELOG.md) — Lịch sử thay đổi
