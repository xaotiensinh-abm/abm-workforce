# Changelog — ABM Workforce

Mọi thay đổi quan trọng của hệ thống ABM Workforce được ghi tại đây.

## [2.1.0] — 2026-03-09

### Thêm mới — 12 Skills từ antigravity-awesome-skills

**P0 — 7 Skills (ưu tiên cao):**
- `competitive-landscape` — Phân tích cạnh tranh: Porter's Five Forces, ma trận đối thủ, positioning map
- `market-sizing-analysis` — Tính TAM/SAM/SOM bằng 3 phương pháp (top-down, bottom-up, value theory)
- `startup-analyst` — Phân tích startup toàn diện: market, financial, competitive, strategic
- `deep-research` — Nghiên cứu chuyên sâu đa bước có trích dẫn
- `seo-content-planner` — Lập kế hoạch content SEO: topic clusters, content calendar
- `sales-automator` — Cold email sequences, follow-up, objection handling
- `competitor-intelligence` — Thu thập dữ liệu đối thủ qua nhiều kênh

**P1 — 5 Skills (nâng cao):**
- `multi-agent-brainstorming` — Review thiết kế 5 vai trò agent, 3 giai đoạn
- `kaizen` — Cải tiến liên tục 4 trụ cột (Kaizen, Poka-Yoke, Standardized Work, JIT)
- `agent-improve` — Tối ưu agent: phân tích hiệu suất, prompt engineering, testing
- `content-creator` — Tạo nội dung SEO-optimized với brand voice nhất quán
- `startup-financial-modeling` — Mô hình tài chính 3-5 năm, scenario analysis

### Thêm mới — 6 Task Types
- `competitive` — Phân tích cạnh tranh (business-analyst)
- `research` — Nghiên cứu chuyên sâu (business-analyst)
- `seo-planning` — Lập kế hoạch SEO (marketing-specialist)
- `startup` — Phân tích startup (business-analyst)
- `improvement` — Cải tiến hệ thống (jarvis)

### Thay đổi
- Manifest: 36 → 48 skills
- Route `sales`: thêm `sales-automator`, bỏ `revops` khỏi default
- Route `marketing`: giữ `marketing-psychology` (phục hồi sau review)
- Route `seo-planning`: thêm `content-creator`
- Route `startup`: thêm `startup-financial-modeling`

### Sửa lỗi
- Header manifest ghi "36 Skills" → sửa thành "48 Skills"
- Comment orchestrator ghi "36 skills" → sửa thành "48 skills"
- Thêm ranh giới rõ ràng giữa `competitive-landscape` và `competitor-intelligence`
- Thêm conflict resolution cho overlapping task types

## [2.0.0] — 2026-03-08

### Ra mắt
- ABM Workforce v2.0 — Hệ thống AI đa agent điều phối doanh nghiệp
- 36 skills ban đầu (8 hệ thống, 7 phát triển, 15 marketing, 4 văn phòng, 2 phân tích)
- 5 SubAgents, 10 Workers, 9 Workflows
- Delegation Chain Management + Verification Protocol
- Second Brain 4 lớp memory system
