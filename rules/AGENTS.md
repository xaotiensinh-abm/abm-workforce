# AGENTS.md — ABM-Workforce Workspace Instructions
# This file provides project-wide context to all AI agents in the workspace.

## 🎯 Project Context
You are working inside an **ABM-Workforce Workspace** — a unified multi-agent AI ecosystem.
This workspace contains 143 skills, 94 workflows, and 10 Jarvis Workers managed by
ABM-Workforce v3.0 with the 4-Phase Agile Methodology. You are the **coding executor**.

## 📏 Coding Standards (Iron Discipline)

### Security First
- NEVER hard-code API keys, passwords, or secrets
- Always use environment variables for sensitive data
- Validate ALL user input before processing
- Sanitize data before database operations

### Error Handling
- try-catch for ALL async operations
- Meaningful error messages (Vietnamese context acceptable)
- Structured logging with appropriate levels (debug, info, warn, error)

### Code Quality
- Input validation on all public functions
- TypeScript preferred for web projects (strict mode)
- Go for backend services and CLI tools
- Python for scripts and data processing
- Every function should have a single responsibility

### Testing
- Write tests alongside implementation
- Unit tests for business logic
- Integration tests for API endpoints
- Aim for >80% coverage on critical paths

## 🏗️ Architecture Patterns
- Modular architecture with clear separation of concerns
- Use dependency injection where applicable
- Prefer composition over inheritance
- Keep functions small (<50 lines)
- Document complex logic with inline comments

## 📁 Directory Conventions
- `src/` — Source code
- `tests/` or `__tests__/` — Test files
- `.env.example` — Environment template (never commit `.env`)
- `docs/` — Documentation

## 🚫 Anti-Patterns to Avoid
- No `any` types in TypeScript (use proper typing)
- No magic numbers (use named constants)
- No deeply nested callbacks (use async/await)
- No copy-paste code (extract shared logic)
- No `console.log` in production (use proper logger)
- **CRITICAL**: No dependencies (`node_modules`, `.venv`, `.git`) inside AI Skills folders. Skills are purely declarative rules (`SKILL.md`), they should act as black boxes and offload execution to system tools or paths outside of `.agent/skills/`.

## 🌐 Localization
- UI text may be in Vietnamese (tiếng Việt)
- Code comments and variable names in English
- Error messages can be bilingual

## 🤖 ABM-Workforce Integration
- Use `/abm-help` to determine the right workflow for any task
- Follow 4-Phase methodology: Analysis → Planning → Solutioning → Implementation
- Quick fixes: `/abm-quick-spec` → `/abm-quick-dev`
- All workflows at: `~/.gemini/antigravity/global_workflows/`
