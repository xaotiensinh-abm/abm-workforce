---
name: jarvis-workers
description: ABM-Workforce Worker & SubAgent Registry — 15 Workers + 15 SubAgents. Unified ABM 4-Phase methodology with Jarvis Orchestrator.
metadata:
  author: ABM-Workforce
  version: "3.1"
  category: orchestration
---

# ABM-Workforce — Worker & SubAgent Registry

> **Use this skill when:** ABM-Workforce worker registry or sub-agent coordination

> Hệ thống đa tác tử thống nhất theo cấu trúc GitHub `xaotiensinh-abm/abm-workforce`.
> Worker definitions tại `D:\AntigravityWorkspace\_abm\Workers\`
> SubAgent definitions tại `D:\AntigravityWorkspace\_abm\SubAgents\`

## Workers (15)

| # | Worker | File | Domain |
|---|--------|------|--------|
| 1 | 📊 Analyst | `Workers/analyst.md` | Phân tích yêu cầu, stakeholders, user stories |
| 2 | 🏗️ Architect | `Workers/architect.md` | Kiến trúc hệ thống, technical design |
| 3 | ⚡ Dev | `Workers/dev.md` | Full-stack development, implementation |
| 4 | 📋 PM | `Workers/pm.md` | Project management, PRD, planning |
| 5 | 🧪 QA | `Workers/qa.md` | Testing, quality assurance, validation |
| 6 | 🛡️ Security Evaluator | `Workers/security-evaluator.md` | Security audit, OWASP, vulnerability |
| 7 | 🏃 SM | `Workers/sm.md` | Scrum Master, sprint ceremonies |
| 8 | 🎨 UX Designer | `Workers/ux-designer.md` | UI/UX design, user research |
| 9 | ✍️ Content Writer | `Workers/content-writer/` | Content strategy, SEO writing |
| 10 | 📈 Data Analyst | `Workers/data-analyst/` | Data analysis, ETL, reporting |
| 11 | 📧 Email Marketer | `Workers/email-marketer/` | Email campaigns, automation |
| 12 | 🔍 SEO Optimizer | `Workers/seo-optimizer/` | SEO audit, optimization |
| 13 | 🌐 Web Developer | `Workers/web-developer/` | Frontend/backend web dev |
| 14 | 🔀 Task Router | `Workers/task-router.md` | Auto-route tasks → workers |
| 15 | 🚀 Quick Flow Solo Dev | `Workers/quick-flow-solo-dev.md` | Rapid spec & implement |

## SubAgents (15)

| # | SubAgent | File | Specialization |
|---|----------|------|---------------|
| 1 | 💼 Business Analyst | `SubAgents/business-analyst/` | Market research, competitive analysis |
| 2 | 🎯 Marketing Specialist | `SubAgents/marketing-specialist.md` | Marketing strategy, campaigns |
| 3 | 💰 Sales Specialist | `SubAgents/sales-specialist.md` | Sales pipeline, lead generation |
| 4 | 👥 HR Specialist | `SubAgents/hr-specialist.md` | Recruitment, onboarding |
| 5 | 🎓 Training Specialist | `SubAgents/training-specialist.md` | Course design, training programs |
| 6 | 🔗 Affiliate Specialist | `SubAgents/affiliate-specialist.md` | Affiliate marketing, partnerships |
| 7 | 🤖 Automation Engineer | `SubAgents/automation-engineer/` | Workflow automation, bots |
| 8 | 🎨 Creative Strategist | `SubAgents/creative-strategist/` | Brand, creative direction |
| 9 | 📁 Office Manager | `SubAgents/office-manager/` | Operations, admin tasks |
| 10 | 🔬 R&D Specialist | `SubAgents/rd-specialist/` | Research & development |
| 11 | 🌐 Web Specialist | `SubAgents/web-specialist.md` | Web presence, hosting |

## ABM 4-Phase Methodology

| Phase | ABM Workflows | Primary Workers |
|-------|-------------|----------------|
| **Analysis** | `/abm-brainstorm`, `/abm-research` | Analyst + Data Analyst |
| **Planning** | `/abm-prd`, `/abm-ux` | PM + UX Designer |
| **Solutioning** | `/abm-arch`, `/abm-epics` | Architect + Dev |
| **Implementation** | `/abm-dev`, `/abm-review` | Dev + QA |
| **Quick Flow** | `/abm-quick-spec`, `/abm-quick-dev` | Quick Flow Solo Dev |

## Task Routing (via task-router.md)

```
User Request → Task Router analyzes:
  ├── code/build/debug    → Dev + QA
  ├── design/UI/UX        → UX Designer + Web Developer
  ├── content/SEO/write   → Content Writer + SEO Optimizer
  ├── business/plan       → PM + Analyst + Business Analyst
  ├── security/audit      → Security Evaluator
  ├── marketing/email     → Marketing Specialist + Email Marketer
  ├── data/research/ETL   → Data Analyst
  └── quick fix           → Quick Flow Solo Dev
```

## Orchestration Flow

```
Jarvis Orchestrator (Autonomous-Core/jarvis-orchestrator.md)
  ↓
Task Router (Workers/task-router.md) 
  ↓
Worker(s) execute → spawn SubAgent(s) if needed
  ↓
QA reviews output
  ↓
Deliver to user
```

## Key Files

| Resource | Path |
|----------|------|
| Orchestrator | `_abm/Autonomous-Core/jarvis-orchestrator.md` |
| Consciousness | `_abm/Autonomous-Core/consciousness/` |
| Engine | `_abm/Autonomous-Core/engine/` |
| Config | `_abm/workforce-config.json` |
| Full Guide | `_abm/HUONG-DAN-SU-DUNG.md` |
