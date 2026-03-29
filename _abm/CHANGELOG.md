# ABM Workforce CHANGELOG

## [2026-03-18] v4.3 — Token Optimization + Affiliate Specialist v2
### Optimized
- 🚀 **Token giảm 45%**: Typical task 13,078 → 7,150 tokens/call
- 📄 `RULES.md` slim: 2,780 → 694 tokens (-75%)
- 🧠 `jarvis-orchestrator.md` slim: 5,819 → 2,177 tokens (-63%)
- 📦 `jarvis-delegation-protocol.md` mới: 928 tokens (lazy-load)

### Upgraded
- 🔗 **Affiliate Specialist v2**: audit 3 rounds → 9.2/10 (Grade S)
  - 4-section ABM chuẩn (Goal/Instructions/Examples/Constraints)
  - VN market context: Shopee, TikTok Shop, Lazada, AccessTrade
  - Error recovery + confidence scoring + affiliate_metrics
- ✅ `affiliate-specialist-checklist.md`: quality gate pre/during/post
- 📘 Hướng dẫn sử dụng Affiliate tiếng Việt

### Changed
- 📖 README.md viết lại hoàn toàn: mermaid diagrams, lazy-load architecture
- 📋 Workflow `/affiliate` nâng cấp: stage menu, hợp đồng template, quick commands
- 🔧 SKILL.md wrapper: fix path ABM, Windows setup, web_search fallback

## [2026-03-16] v4.2 — NotebookLM Second Brain + UUPM v2.0 + Affiliate
### Added
- 🧠 **NotebookLM Second Brain** — prototype tại `tools/notebooklm-brain/`
  - Knowledge Notebook: semantic skill routing từ 78 skills (421KB)
  - Memory Notebook: long-term memory search (session logs, task history, patterns)
  - CLI: `python brain.py skill|memory|ask|collect|upload|refresh|status`
- 🔗 **Phòng Affiliate Marketing** — 32 skills, 8 stages full funnel
  - SubAgent: `affiliate-specialist.md`
  - Workflow: `/affiliate` — pipeline research → content → blog → landing → deploy
  - Skills tại `.agent/skills/affiliate-skills/` (từ Affitor/affiliate-skills)
- 🔧 **notebooklm-py setup toolkit** — tại `tools/notebooklm/`
  - Setup script tự động (PowerShell), login workaround, README tiếng Việt
- 📊 SESSION-006 milestone save

### Changed
- 🎨 **UI UX Pro Max v2.0** — upgrade qua `uipro-cli`
  - 2 files (8KB) → 31 files (571KB)
  - 161 industry-specific reasoning rules (CSV datasets)
  - Design system generation tự động
  - Python scripts: core.py, design_system.py, search.py
  - Chuyển từ `_abm/bmm/agents/skills/` → `.agent/skills/` (standard location)
- skill-manifest.csv: 79 → 78 skills (ui-ux-pro-max moved to .agent/)
- config.yaml: version 2.0.0 → 3.0.0

### Architecture
- NotebookLM = External long-term memory layer, bổ sung Second Brain 4 tầng
- Semantic skill routing qua Google NotebookLM API thay vì keyword matching

## [2026-03-14] — Hybrid 3-Tier + Major Upgrade
### Added
- 5 SubAgents: marketing, sales, hr, training, web specialists
- 5 Workers: content-writer, data-analyst, web-developer, email-marketer, seo-optimizer
- 7 new skills: seo-fundamentals, growth-engine, landing-page-builder, responsive-web-design, web-accessibility, proposal-generator, roi-calculator
- 47 CHECKLIST.md files (Tier 2+3 quality gates)
- 6 Second-Brain knowledge files
- 3 Team-Orchestration pipelines (marketing, sales, training)
- README.md getting-started guide
- Output naming convention

### Changed
- Skill architecture: Monolith → Hybrid 3-Tier
- skill-manifest.csv: rebuilt (116→78 skills)
- agent-manifest.csv: rebuilt (21 entries)
- pricing-strategy: 83→130 lines (5 models, psychology)
- email-marketing: 98→135 lines (3 sequences, PAS)

### Removed
- coaching-delivery (CEO decision)
- 37 skills archived (_archive/)
- 11 deprecated skills deleted

## [2026-03-14] — Initial Audit
### Findings
- Score: 6.8/10 → 7.7/10 after fixes
- Critical: SubAgents=0, Workers=0, manifests outdated
- 8-persona critique conducted
