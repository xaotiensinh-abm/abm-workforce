# ABM Workforce CHANGELOG

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
