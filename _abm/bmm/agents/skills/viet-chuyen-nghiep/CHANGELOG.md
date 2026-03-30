# Changelog — Viết Chuyên Nghiệp

## [v3.2.0] — 2026-03-12

### Added — Novel-Writer Pipelines Integration
- `Workers/edu-worker.md` — EduWriter: tài liệu học tập (handout, workbook, quiz, lesson plan)
- `Workers/slide-worker.md` — SlideWriter: slide thuyết trình (narrative arc, speaker notes)
- `Workers/research-writer-worker.md` — ResearchWriter: tài liệu nghiên cứu (white paper, policy brief)
- `Workers/social-writer-worker.md` — SocialWriter: content social đa nền tảng + repurposing
- `Team-Orchestration/write-fiction.md` — Pipeline viết truyện fiction (7+1 agent, 130đ QA, 8 thể loại)
- `Team-Orchestration/write-edu.md` — Pipeline viết tài liệu học tập
- `Team-Orchestration/write-slide.md` — Pipeline tạo slide thuyết trình
- `Team-Orchestration/write-research.md` — Pipeline viết tài liệu nghiên cứu
- `Team-Orchestration/write-social.md` — Pipeline content social đa nền tảng

### Changed
- `SKILL.md` v3.1 → v3.2: +5 pipelines, +8 workers, +5 ví dụ, +triggers mới, platform roadmap v3.3+
- `Orchestrator/routing-matrix.md` → v3.2 với +5 routes mới, Workers section
- `workforce-config.json` → v3.2.0, +5 routes, +4 workers
- `global_workflows/novel-writer.md` → v3.2 reference
- `global_workflows/viet-pro.md` → +5 pipeline commands

### Notes
- Twitter/X nay thuộc danh sách platform supported (qua social-writer-worker)
- Blog/SEO nay có pipeline riêng (`write-social` với SEO mode)
- Fiction pipeline sử dụng QA 130 điểm (khác các pipeline khác dùng 100 điểm)

## [v3.1.1] — 2026-03-10

### Added — Merge Output Pipeline
- `Workers/merge-worker.md` — Worker ghép nhiều file MD thành 1 file, encoding UTF-8 chuẩn
- `scripts/merge-parts.py` — Python CLI tool merge parts (pattern discovery, BOM strip, VN verify)
- `Team-Orchestration/merge-output.md` — Pipeline ghép file output

### Changed
- `Orchestrator/routing-matrix.md` — Thêm route `merge-output` cho ghép file
- `viet-pro.md` — Thêm pipeline merge-output vào bảng routing workflow

### Notes
- ⚠️ **KHÔNG dùng PowerShell** để merge file tiếng Việt (gây lỗi encoding)
- **LUÔN dùng** `scripts/merge-parts.py` hoặc `write_to_file` tool

## [v3.1.0] — 2026-03-10

### Added — Mở rộng Content Types
- `Ban/style/email.md` — BTV Email (6 loại email, subject line, CTA, sequence)
- `Ban/style/curriculum.md` — BTV Giáo Trình (Bloom's Taxonomy, module design)
- `Ban/platform/email-platform.md` — BTV Email Platform (deliverability, spam)
- `Ban/platform/zalo.md` — BTV Zalo (OA, ZNS, Zalo Ads)
- `Ban/platform/threads.md` — BTV Threads (micro-content)
- `Ban/platform/docs.md` — BTV Tài Liệu (PDF, DOCX, Notion)
- `Team-Orchestration/write-email.md` — Pipeline viết email
- `Team-Orchestration/write-curriculum.md` — Pipeline viết giáo trình
- `Team-Orchestration/write-guide.md` — Pipeline viết user guide/SOP
- `Workers/email-worker.md` — Email execution specialist
- `Workers/curriculum-worker.md` — Curriculum design specialist
- `Workers/guide-worker.md` — Technical writing specialist
- `Context-Layer/CoreModules/email-templates.md` — Email templates + spam blacklist
- `Context-Layer/CoreModules/curriculum-framework.md` — ADDIE + Bloom framework
- `Context-Layer/CoreModules/guide-standards.md` — Guide writing standards

### Changed — Core Updates
- `SKILL.md` v3.0 → v3.1: 25→31 BTV, +3 pipelines, +3 ví dụ, platform roadmap
- `Orchestrator/routing-matrix.md` → +3 routes (email, curriculum, guide)
- `Ban/style/lead-style.md` → 7 BTV routing, count clarification (1 Lead + 7 BTV = 8)
- `Ban/platform/lead-platform.md` → 9 BTV routing (+4 platform mới)

### Fixed — Audit D1-D9
- `Ban/content/lead-content.md` → +4 enum values (curriculum, guide, sop, faq), +3 pipelines, +research modes
- `Ban/quality/lead-quality.md` → +domain-specific checks (email spam, Bloom alignment, step validation)
- `Workers/*.md` → +role boundary notes (Worker vs BTV clarification)
- `Team-Orchestration/write-*.md` → +Worker references
- `SKILL.md` → blog clarification, platform roadmap (X, Instagram, YouTube planned for v3.2)

## [v3.0.2] — 2026-03-10

### Added
- Đóng gói global skill: directory junction `skills/viet-chuyen-nghiep`
- Workflow `/viet-pro` tại `global_workflows/viet-pro.md`
- Auto-activate triggers mới: "viết blog", "viết báo cáo", "viết đề án", "viết email marketing"
- `base_path` directive trong SKILL.md cho global skill resolution

### Changed
- SKILL.md: Examples + Constraints cập nhật 100% v3.0 Ban terminology

## [v3.0.1] — 2026-03-10

### Fixed (Audit fix — 54→100/100)
- `Orchestrator/routing-matrix.md` → pipeline v3.0 Ban/
- `Orchestrator/editor-in-chief.md` → 6 Ban (thay 8 phòng ban)
- `Orchestrator/delegation-protocol.md` → Ban/BTV terminology
- `Orchestrator/escalation-rules.md` → escalation đến đúng Ban
- 6 files `Team-Orchestration/*.md` → tham chiếu Ban/
- `workforce-config.json` → v3.0 Ban/ + legacy markers
- `HUONG-DAN-SU-DUNG.md` → v3.0 kiến trúc Tòa Soạn
- `README.md` → v3.0 architecture

### Added
- `Orchestrator/interface-contract.md` — YAML schema giữa 6 Ban
- `Team-Orchestration/golden-test.md` — 2 test cases end-to-end
- `Workers/DEPRECATED.md` + `SubAgents/DEPRECATED.md` — legacy markers

## [v3.0.0] — 2026-03-10

### Added (Kiến Trúc Tòa Soạn)
- `Ban/content/` (3 files): lead-content, research, analysis
- `Ban/style/` (6 files): lead-style, storytelling, rhythm, narrative, presentation, technical
- `Ban/quality/` (7 files): lead-quality, punctuation, capitalization, natural, anti-ai, fact-check, consistency
- `Ban/platform/` (5 files): lead-platform, facebook, tiktok, linkedin, video
- `Ban/examples/` (1 file): lead-examples
- `Ban/meta/` (3 files): lead-meta, upgrade, style-audit

### Changed
- SKILL.md: v3.0 Tổng Biên Tập, sơ đồ Tòa Soạn, routing table

### Deprecated
- `Workers/` (8 files) → thay thế bởi `Ban/`
- `SubAgents/` (32 files) → thay thế bởi `Ban/`

## [v2.0.0] — 2026-03-08

### Added
- Autonomous-Core: 4 engines (task-classifier, workflow, scoring, state)
- Context-Layer: CoreModules, Knowledge-Base, Second-Brain, Memory
- Team-Orchestration: 6 pipeline definitions
- Orchestrator: editor-in-chief, routing-matrix, delegation, escalation

## [v1.0.0] — 2026-02

### Added
- Initial release: 8 Workers + 32 SubAgents
- Basic pipeline: intake → research → strategy → output → quality
