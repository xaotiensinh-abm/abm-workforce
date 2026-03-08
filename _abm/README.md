# 🧠 ABM — AI Business Master

## Hệ thống Multi-Agent Workforce cho doanh nghiệp

> **278 files** | **27 skills** | **14 workflows** | **15 agents** | **12 task routes**

---

## Cấu trúc ABM Workforce

```
ABM-Workforce/
├── SubAgents/              # 5 agent chuyên biệt theo lĩnh vực
│   ├── marketing-specialist/
│   ├── hr-specialist/
│   ├── office-manager/
│   ├── automation-engineer/
│   └── business-analyst/
├── Workers/                # 10 worker thực thi kỹ thuật
│   ├── dev.md, qa.md, pm.md, sm.md
│   ├── analyst.md, architect.md
│   ├── security-evaluator.md, task-router.md
│   └── ux-designer.md, quick-flow-solo-dev.md
├── Autonomous-Core/        # 41 files — Jarvis engine + consciousness
│   ├── jarvis-orchestrator.md
│   ├── consciousness/     # SOUL, IDENTITY, AGENTS, HEARTBEAT, TOOLS, USER, MEMORY
│   └── engine/            # Core processing engine
├── Team-Orchestration/     # 14 quy trình phối hợp
│   ├── dev-pipelines/     # bug-fix, feature, refactor, data
│   ├── business-pipelines/ # marketing, hr, report, document, add-agent
│   └── orchestration/     # delegation-chain, triage, verification, synthesis, rollback
├── _design-specs/          # 149 đặc tả thiết kế pipeline
├── Context-Layer/          # 53 files ngữ cảnh và tri thức
│   ├── CoreModules/       # Config, governance, contracts, templates
│   ├── Knowledge-Base/    # 27 skills chuyên môn
│   └── Second-Brain/      # Bộ nhớ, lịch sử, tiêu chuẩn
├── Outputs/                # Kết quả runtime
│   ├── task-log.yaml
│   ├── contracts/
│   └── attestations/
├── workforce-config.json   # Cấu hình Workforce
├── README.md               # File này
└── HUONG-DAN-SU-DUNG.md   # Hướng dẫn sử dụng
```

## Công nghệ cốt lõi

| Component | Mô tả |
|-----------|-------|
| ROMA 6-Tier Pipeline | Phân tầng xử lý: Strategy → Intelligence → Content → Analysis → Validation → Synthesis |
| Context Engineering 5-Layer | Quản lý ngữ cảnh: Identity → Domain → Runtime → Task → History |
| Contract-Attestation Model | Hợp đồng → Chứng nhận → Xác minh = Trách nhiệm rõ ràng |
| Skill Routing | Auto-chọn skill theo task_type (12 routes) |
| Agent Routing | Auto-chọn agent theo task_type (12 routes) |
