# System Architecture — Viết Chuyên Nghiệp v3.0 Tòa Soạn

## Tổng quan

Hệ thống sản xuất nội dung tiếng Việt chuyên nghiệp, hoạt động theo mô hình
**Kiến Trúc Tòa Soạn** — 6 Ban chuyên môn với 25 BTV, 4 engines tự động,
45+ knowledge files.

## Kiến trúc

```
┌──────────────────────────────────────────────┐
│              SKILL.md (Entry Point)          │
│         Tổng Biên Tập — Điều phối            │
├──────────────────────────────────────────────┤
│                                              │
│  ┌─────────────────────────────────────────┐ │
│  │         ORCHESTRATOR LAYER              │ │
│  │  editor-in-chief.md                     │ │
│  │  routing-matrix.md                      │ │
│  │  delegation-protocol.md                 │ │
│  │  escalation-rules.md                    │ │
│  │  interface-contract.md                  │ │
│  └─────────────────────────────────────────┘ │
│                                              │
│  ┌─────────────────────────────────────────┐ │
│  │         AUTONOMOUS CORE (4 engines)     │ │
│  │  task-classifier │ workflow-engine       │ │
│  │  scoring-engine  │ state-manager         │ │
│  └─────────────────────────────────────────┘ │
│                                              │
│  ┌─────────────────────────────────────────┐ │
│  │         6 BAN CHUYÊN MÔN               │ │
│  │                                         │ │
│  │  content/ (3)  → Thu thập & nghiên cứu  │ │
│  │  style/ (6)    → Biên tập phong cách    │ │
│  │  quality/ (7)  → Kiểm duyệt            │ │
│  │  platform/ (5) → Xuất bản đa nền tảng   │ │
│  │  examples/ (1) → Thư viện bài mẫu      │ │
│  │  meta/ (3)     → Phát triển & audit     │ │
│  └─────────────────────────────────────────┘ │
│                                              │
│  ┌─────────────────────────────────────────┐ │
│  │         CONTEXT LAYER (45+ files)       │ │
│  │  CoreModules/ │ Knowledge-Base/         │ │
│  │  Second-Brain/ │ Memory/                │ │
│  └─────────────────────────────────────────┘ │
│                                              │
│  ┌─────────────────────────────────────────┐ │
│  │    TEAM ORCHESTRATION (7 pipelines)     │ │
│  │  write-new │ edit-draft │ grade-content  │ │
│  │  critique │ deep-research │ publish      │ │
│  │  golden-test                             │ │
│  └─────────────────────────────────────────┘ │
│                                              │
│  ┌─────────────────────────────────────────┐ │
│  │         LEGACY (deprecated)             │ │
│  │  Workers/ (8 files) — v2.0              │ │
│  │  SubAgents/ (32 files) — v2.0           │ │
│  └─────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

## Pipeline Flow

```
User Request
    │
    ▼
Tổng Biên Tập (SKILL.md)
    │
    ├─ Phân loại → routing-matrix.md
    │
    ▼
Ban Thu Thập (content/)
    │ research.md → analysis.md
    ▼
Ban Biên Tập (style/)
    │ storytelling → rhythm → narrative → presentation → technical
    ▼
Ban Kiểm Duyệt (quality/)
    │ 6 kiểm tra song song
    │
    ├─ PASS ──→ Ban Xuất Bản (platform/) → Output
    ├─ REVISE → Quay lại style/ (max 2 lần)
    └─ REJECT → Quay lại content/
```

## Thống kê

| Component | Files | Phiên bản |
|-----------|-------|-----------|
| Ban/ (agents) | 25 | v3.0 |
| Orchestrator/ | 5 | v3.0 |
| Team-Orchestration/ | 7 | v3.0 |
| Autonomous-Core/ | 4 | v2.0 (giữ nguyên) |
| Context-Layer/ | 45+ | v2.0 (giữ nguyên) |
| Workers/ (legacy) | 8+1 | DEPRECATED |
| SubAgents/ (legacy) | 32+1 | DEPRECATED |
| **Tổng** | **142** | |

## Global Skill Registration

- **Skill path:** `C:\Users\PC\.gemini\antigravity\skills\viet-chuyen-nghiep\`
- **Junction target:** `D:\AntigravityWorkspace\Viet-chuyen-nghiep\`
- **Workflow:** `/viet-pro` tại `global_workflows/viet-pro.md`
- **Auto-triggers:** 30+ keywords (VN + EN)

## Lịch sử Phiên bản

| Version | Ngày | Thay đổi |
|---------|------|---------|
| v1.0 | 2026-02 | Khởi tạo: 8 Workers + SubAgents |
| v2.0 | 2026-03-08 | Thêm Autonomous-Core, Context-Layer |
| v3.0 | 2026-03-10 | Kiến Trúc Tòa Soạn: 6 Ban, 25 BTV |
| v3.0.1 | 2026-03-10 | Fix audit: routing, orchestrator, docs |
| v3.0.2 | 2026-03-10 | Đóng gói global skill + junction |
