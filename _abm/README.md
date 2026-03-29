# 🧠 ABM Workforce — Getting Started

> **AI Business Master** — Hệ thống quản trị doanh nghiệp bằng AI
> Version: Post Hybrid 3-Tier | Skills: 78 active | Agents: 16+

---

## Quick Start (5 phút)

### 1. Gọi Jarvis
```
/jarvis
```
→ Jarvis Orchestrator sẽ online, hiển thị menu 14 items.

### 2. Dùng slash commands
```
/marketing   — Giao việc marketing
/sales       — Giao việc sales
/hr          — Giao việc HR
/dev         — Giao việc dev
/docs        — Tạo tài liệu
/report      — Tạo báo cáo
/review      — Đánh giá phản biện
/save        — Lưu trạng thái
```

### 3. Hoặc nói tự nhiên
```
"Viết landing page cho coaching 250tr"
"Tạo email sequence cho leads mới"
"Đánh giá hiệu suất team Q1"
```

---

## Cấu Trúc Hệ Thống

```
_abm/
├── bmm/agents/
│   ├── jarvis-orchestrator.md    # 🧠 Lead Orchestrator
│   ├── skills/                   # 78 active skills (Hybrid 3-Tier)
│   │   ├── [skill]/SKILL.md      # Core definition
│   │   ├── [skill]/CHECKLIST.md  # Quality gates (Tier 2+)
│   │   └── _archive/             # 37 archived skills
│   └── [11 agent .md files]      # Specialized agents
├── SubAgents/                    # 5 SubAgent SOUL.md
│   ├── marketing-specialist.md
│   ├── sales-specialist.md
│   ├── hr-specialist.md
│   ├── training-specialist.md
│   └── web-specialist.md
├── Workers/                      # 5 Workers
│   ├── content-writer/
│   ├── data-analyst/
│   ├── web-developer/
│   ├── email-marketer/
│   └── seo-optimizer/
├── Context-Layer/Second-Brain/   # Knowledge base
├── Team-Orchestration/           # 3 pipelines
├── _config/                      # Manifests + configs
└── Autonomous-Core/              # Jarvis engine
```

## Delegation Chain

```
CEO → Jarvis → SubAgent → Worker → Output
         ↑         ↑          ↑
     Orchestrate  Route     Execute
```

## Skill Tiers

| Tier | Structure | Khi nào |
|:----:|-----------|---------|
| 1 | `SKILL.md` only | Skills ≤120 dòng |
| 2 | + `CHECKLIST.md` | Skills 120-250 dòng |
| 3 | + `EXAMPLES.md` / `OUTPUT_SPEC.md` | Skills ≥250 dòng |

## Quy Tắc Sắt

1. **Tiếng Việt 100%** — mọi output business
2. **Bằng chứng trước khi khẳng định** — không "chắc là"
3. **Hợp đồng trước khi giao việc** — scope_in/scope_out
4. **Max 3 skills/lần load** — kiểm soát context
5. **Output → `_abm-output/`** — không file rải rác

## Cần help?
```
/jarvis      — Gọi Jarvis
abm-help.csv — Tra cứu commands
```
