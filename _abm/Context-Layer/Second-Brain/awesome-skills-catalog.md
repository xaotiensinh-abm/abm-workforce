# Awesome-Skills Catalog Reference — Truy Xuất Khi Cần Bổ Sung

> **Source**: https://github.com/sickn33/antigravity-awesome-skills
> **Total**: 1,254 skills | 9 categories | Cập nhật: 2026-02-08

## Categories Summary

| Category | Count | Focus | Top Skills |
|----------|:-----:|-------|------------|
| Architecture | 81 | System design, ADRs, C4, patterns | `architecture`, `c4-context`, `senior-architect`, `bash-linux`, `brainstorming` |
| Business | 56 | Growth, pricing, CRO, SEO, GTM | `copywriting`, `pricing-strategy`, `seo-audit`, `brand-guidelines`, `content-creator` |
| Data & AI | 230 | LLM, RAG, agents, analytics | `rag-engineer`, `prompt-engineer`, `langgraph`, `vector-db`, `openai-patterns` |
| Development | 179 | Languages, frameworks, code quality | `typescript-expert`, `python-patterns`, `react-patterns`, `go-patterns` |
| General | 298 | Planning, docs, product ops, writing | `brainstorming`, `doc-coauthoring`, `writing-plans`, `code-review` |
| Infrastructure | 134 | DevOps, cloud, CI/CD, deployment | `docker-expert`, `aws-serverless`, `vercel-deployment`, `terraform` |
| Security | 146 | AppSec, pentesting, compliance | `api-security`, `sql-injection-testing`, `vulnerability-scanner` |
| Testing | 35 | TDD, test design, QA | `test-driven-development`, `testing-patterns`, `test-fixing` |
| Workflow | 95 | Automation, orchestration | `workflow-automation`, `inngest`, `trigger-dev`, `create-pr` |

## ABM Đã Cài Từ Awesome-Skills (11 junctions)

`documentation`, `docx-official`, `pptx-official`, `xlsx-official`, `security-audit`, `test-driven-development`, `typescript-expert`, `web-performance-optimization`, `webapp-testing`, `web-security-testing`, `skill-generator`

## Gaps Cần Bổ Sung (Priority Order)

### P0 — Critical gaps ABM thiếu hoàn toàn:
1. `architecture` — System design + ADR
2. `docker-expert` — Container deployment
3. `ci-cd-pipeline` — Automated testing/deploy
4. `prompt-engineer` — Core AI engineering
5. `api-design-principles` — API architecture

### P1 — Strengthen existing:
6. `testing-patterns` — Bổ sung TDD
7. `debugging-strategies` — Bổ sung systematic-debugging
8. `create-pr` — PR workflow
9. `monitoring-alerting` — System health
10. `rag-engineer` — RAG cho knowledge systems

### P2 — Nice to have:
11. `python-patterns`, 12. `react-patterns`, 13. `doc-coauthoring`, 14. `lint-and-validate`, 15. `incident-response`

## Cấu Trúc Skill Awesome-Skills (Modular)

```
skill-name/
├── SKILL.md           # Core definition
├── OUTPUT_SPEC.md     # Output specifications
├── CHECKLIST.md       # Quality gates
├── REFERENCE.md       # Technical reference
├── EXAMPLES.md        # Usage examples
├── CHANGELOG.md       # Version history
├── reference/         # Design tokens, components
├── resources/
│   ├── modules/       # Domain-specific modules
│   └── templates/     # Output templates
└── scripts/
    └── validate_*.py  # Validation scripts
```

## Install Command
```bash
npx antigravity-awesome-skills --antigravity
# Or specific skill:
npx -y skills add https://github.com/sickn33/antigravity-awesome-skills --skill [name]
```
