<agents_md>
# ABM-Workforce AI Agent Guidelines

This file conforms to the `agents.md` specification for repository-level AI directives.

## 🤖 Context
This is an orchestrator repository for a multi-agent multi-layered workforce system (ABM-Workforce). 
It contains 110+ specialized skills designed to emulate a full Human Resources pipeline, including marketing, R&D, finance, development, and more.

## 🛡️ Safe Autonomy (Guardrails)
1. **No Destructive Operations**: Agents traversing this repository MUST NOT delete archiving records in `_abm/bmm/agents/skills/_archive/` without explicit `CEO` authorization.
2. **Environment Masking**: API keys are isolated in `_abm/_config/` and `.env`. Auto-publishing commands MUST explicitly ignore the config directory.
3. **Execution Limits**: If a task requires more than 10 sequential tool calls with a high fail rate, the Agent MUST PAUSE and escalate to the human user for evaluation.

## 📂 Architecture Map
- `_abm/bmm/agents/skills/`: The Absolute Source of Truth for all skills.
- `.agents/skills/`: Auto-generated symlink directory for IDEs (Cursor/Windsurf/Antigravity) - DO NOT EDIT DIRECTLY.
- `.agents/workflows/`: Global slash-commands for orchestrator workflows.
- `_abm/_config/skills-index-l0.json`: 0-dependency lightweight payload summarizing all skills. **ALWAYS read this first to prevent context window overflow.**
- `CLAUDE.md`: Behavioral rules targeting native Claude integration.

## ⚙️ Standard Tooling
- We employ Git Worktrees for isolated task development (`using-git-worktrees` skill).
- We utilize N8N for extended web automation (Webhooks registered under `mcp-registry.yaml`).
- 9Router/Claude CLI bridges Local API capabilities with minimal cost routing (`claude-router.sh`).

## 🧠 Memory Rules
Do not store large task artifacts or memory states in `.md` files at the root. All local memories and task checkpoints MUST be routed to `.gemini/` or `.agents/tasks/`.
</agents_md>
