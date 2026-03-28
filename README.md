# 🚀 ABM-Workforce v3.0

> **Agile AI-Driven Multi-Agent Development Framework**
> 10 Workers · 143 Skills · 94 Workflows · 4-Phase Methodology · 9-Layer Skill Engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![ABM-Workforce Banner](banner-bmad-method.png)

---

## 🎯 What is ABM-Workforce?

ABM-Workforce is a production-grade **multi-agent AI development framework** designed for [Google Antigravity](https://blog.google/technology/google-labs/project-mariner-gemini-ai-agent/) and compatible AI coding assistants. It provides:

- **10 Specialized AI Workers** — CodeAgent, ContentAgent, BusinessAgent, DesignAgent, DataAgent, SecurityAgent, OpsAgent, CriticAgent, OptimizerAgent, WorkspaceAgent
- **143 Skills** — Production-grade instruction sets with 9-Layer quality compliance
- **94 Workflows** — End-to-end task automation from analysis to deployment
- **4-Phase Methodology** — Analysis → Planning → Solutioning → Implementation

### 🏗️ 9-Layer Skill Engineering

Every skill follows a rigorous quality framework:

| Layer | Name | Purpose |
|:-----:|------|---------|
| L0 | Use Case & Trigger Map | When to activate this skill |
| L1 | Metadata | Version, worker, maturity, tags |
| L2 | Core SKILL.md | Instructions, constraints, guidelines |
| L3 | References | Domain knowledge library |
| L4 | Examples | Happy Path / Edge Case / Anti-Example |
| L5 | Scripts & Tools | Validation, automation |
| L6 | Assets & Templates | Output templates |
| L7 | Output Contract | Quality rubric & format requirements |
| L8 | Governance | CHANGELOG, version tracking, owner |

**Current Status: 🏆 138/138 skills at Tier S (Mature) — Health Score 100/100**

---

## 📁 Repository Structure

```
abm-workforce/
├── rules/                   # Supreme Rules & Coding Standards
│   ├── GEMINI.md            # ABM Supreme Rules v3.0
│   └── AGENTS.md            # Workspace coding discipline
│
├── skills/                  # 143 Production-Grade Skills
│   ├── _standards/          # 9-Layer Framework & Governance
│   │   ├── SKILL-TEMPLATE-V2.md
│   │   ├── USER-GUIDE.md
│   │   ├── governance/      # Maturity registry, audit process
│   │   ├── output-contracts/# Domain-specific quality contracts
│   │   └── scripts/         # Health check scanner
│   ├── global/              # 80 Global Skills
│   └── workspace/           # 57 Workspace Skills
│
├── workflows/               # 94 Automated Workflows
│   ├── abm-*.md             # 31 ABM methodology workflows
│   └── *.md                 # 63 core + specialized workflows
│
├── _abm/                    # ABM session & persona definitions
├── docs/                    # Documentation
└── scripts/                 # Setup & utility scripts
```

---

## ⚡ Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/xaotiensinh-abm/abm-workforce.git
cd abm-workforce
```

### 2. Setup for Google Antigravity

Copy the skills and workflows to your Antigravity workspace:

```powershell
# Windows (PowerShell)
Copy-Item -Recurse skills\global\* "$env:USERPROFILE\.gemini\antigravity\skills\"
Copy-Item -Recurse skills\workspace\* "D:\AntigravityWorkspace\.agent\skills\"
Copy-Item workflows\* "$env:USERPROFILE\.gemini\antigravity\global_workflows\"
Copy-Item rules\GEMINI.md "$env:USERPROFILE\.gemini\GEMINI.md"
```

```bash
# macOS/Linux
cp -r skills/global/* ~/.gemini/antigravity/skills/
cp -r workflows/* ~/.gemini/antigravity/global_workflows/
cp rules/GEMINI.md ~/.gemini/GEMINI.md
```

### 3. Verify Installation

```bash
# Run the skill health scanner
python skills/_standards/scripts/skill_health_check.py ~/.gemini/antigravity/skills
```

---

## 🧠 Worker Registry

| Worker | Role | Key Skills |
|--------|------|------------|
| **W1: CodeAgent** | Senior Full-Stack Engineer | react-expert, typescript-expert, nestjs-expert, database-expert |
| **W2: ContentAgent** | Content Strategist & Writer | viet-pro, seo-content-writer, copywriting |
| **W3: BusinessAgent** | Business Consultant | business-analyst, pricing-strategy, market-sizing |
| **W4: DesignAgent** | Creative Director | ui-ux-pro-max, css-expert, nano-banana-pro |
| **W5: DataAgent** | Data Engineer & Automation | rag-engineer, web-scraper, python-excel-pro |
| **W6: SecurityAgent** | Security Engineer | vulnerability-scanner, auth-expert, api-security |
| **W7: OpsAgent** | DevOps Engineer | docker-expert, kubernetes-architect, terraform |
| **W8: CriticAgent** | Quality Advisor | code-review, find-bugs, oracle |
| **W9: OptimizerAgent** | Auto-Fixer | self-correction-engine, refactoring-expert |
| **W10: WorkspaceAgent** | Google Workspace | gws-gmail, gws-drive, gws-calendar, gws-sheets |

---

## 📋 ABM Methodology (4 Phases)

### Phase 1: Analysis
```
/abm-brainstorm → /abm-research → /abm-market → /abm-brief
```

### Phase 2: Planning
```
/abm-prd → /abm-ux → /abm-validate
```

### Phase 3: Solutioning
```
/abm-arch → /abm-epics → /abm-readiness
```

### Phase 4: Implementation
```
/abm-sprint → /abm-story → /abm-dev → /abm-review
```

### Quick Flow (Simple Tasks)
```
/abm-quick-spec → /abm-quick-dev → /test
```

---

## 🔧 Key Workflows

| Category | Workflows |
|----------|-----------|
| **Coding** | `/code`, `/debug`, `/test`, `/deploy`, `/refactor`, `/audit` |
| **AI Media** | `/gemini-3-image-prompt`, `/veo-fashion-director`, `/wildlife-director` |
| **Business** | `/vietnam-business-planner`, `/sales-pipeline`, `/finance-ops` |
| **Content** | `/content-research-writer`, `/novel-writer`, `/viet-pro` |
| **DevOps** | `/deploy`, `/cloudflare-tunnel`, `/init` |
| **Meta** | `/jarvis`, `/adaptive-routing`, `/agent-manager`, `/deep-research` |

---

## 📊 Skill Health Dashboard

The skill ecosystem is monitored by an automated health scanner:

```bash
python skills/_standards/scripts/skill_health_check.py <skills_directory>
```

Output includes:
- Per-skill 9-layer compliance score
- Maturity tier (S/A/B/C)
- Aggregated health score (0-100)
- Upgrade recommendations

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding new skills (must use `SKILL-TEMPLATE-V2.md`)
- Creating workflows
- Submitting PRs

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🏗️ Built With

- [Google Antigravity](https://blog.google/technology/google-labs/project-mariner-gemini-ai-agent/) — AI Coding Agent
- [BMAD Method](https://github.com/bmad-method/bmad-method) — Agile AI Development (upstream)
- ABM-Workforce v3.0 — Vietnamese AI multi-agent ecosystem

---

*ABM-Workforce v3.0 × Antigravity*
*"Agile AI-Driven Multi-Agent Development"*
*🏆 138/138 Skills at Tier S — Health Score 100/100*
