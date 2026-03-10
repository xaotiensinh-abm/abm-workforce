# 📋 ABM Workforce Changelog

Tất cả thay đổi ABM Workforce được ghi lại tại đây.

---

## [v2.7] — 10/03/2026

### Thêm mới
- **Skill** `self-healing` — Retry chain 3 cấp + fallback map
- **Skill** `github-issues-sprint` — Import GitHub Issues → Sprint
- **Skill** `agentic-memory` — Vector DB (Chroma/Pinecone)
- **Skill** `mcp-integration` — Notion, Google, Slack, Jira qua MCP
- **Skill** `supply-chain` — Procurement, inventory, vendor cho Vận Hành
- **Skill** `contract-review` — Rà soát hợp đồng, red flags
- **Skill** `compliance-checker` — GDPR, PDPA, Luật ATNM VN
- **Skill** `inventory-management` — Quản lý kho hàng
- **Skill** `logistics-optimization` — Tối ưu logistics
- **Dashboard** `dashboard/index.html` — Visual 9 phòng ban + health + scoring
- **Template** `usage-metrics.yaml`
- **Workflow** `/product-launch`

### Thay đổi
- Manifest 71 → 80 skills
- Routes 26 → 30+
- Workflows 14 → 15
- Review score 9.08 → 9.35/10

---

## [v2.6] — 10/03/2026

### Thêm mới
- **Skill** `project-hierarchy` — State Machine Epic → Feature → Story
- **Skill** `sprint-planning` — PRD → Sprint pipeline
- **Skill** `database-management` — Schema, migration
- **Skill** `critical-thinking` — Devil's Advocate, 5 Whys, First Principles
- **Skill** `knowledge-graph` — Entities, relationships, cognee
- **SubAgent** `creative-strategist` — TRIZ, rejected ideas backlog
- **Workflow** `/council` — Hội đồng đánh giá multi-agent

---

## [v2.5] — 09/03/2026

### Thêm mới
- Mô hình Doanh Nghiệp Số — 9 phòng ban
- 6 skills Văn Phòng Số: `docx`, `xlsx`, `pdf`, `pptx`, `agent-email-cli`, `task-planning`
- 4 workflows: `/sales`, `/cskh`, `/finance`, `/legal`
- Email Sandbox Mode
- `health-check.ps1`, `FAQ.md`, CI/CD `verify.yml`

---

## [v2.4] — 09/03/2026
- Baseline: 54 skills + Web Dev (7) + Multimedia (4)
- Review score 8.33/10

---

## [v1.0] — 08/03/2026
- Khởi tạo: Jarvis + 36 skills + 5 SubAgents + 10 Workers
