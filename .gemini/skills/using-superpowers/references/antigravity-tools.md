# Antigravity (Google Deepmind) — Tool Mapping

Skills use Claude Code tool names. Antigravity has a SUPERSET of capabilities. Use this mapping:

## Core Tool Equivalents

| Skill references | Antigravity equivalent | Notes |
|-----------------|----------------------|-------|
| `Read` (file reading) | `view_file` | Supports line ranges, binary files |
| `Write` (file creation) | `write_to_file` | Auto-creates parent dirs |
| `Edit` (file editing) | `replace_file_content` / `multi_replace_file_content` | Multi-chunk editing supported |
| `Bash` (run commands) | `run_command` | PowerShell on Windows, async support |
| `Grep` (search content) | `grep_search` | Ripgrep-based, JSON results |
| `Glob` (search by name) | `find_by_name` | fd-based, type/ext/depth filters |
| `TodoWrite` (task tracking) | `task_boundary` + `write_to_file` (task.md) | Structured task UI |
| `Skill` tool (invoke skill) | `view_file` on SKILL.md | Read skill file directly |
| `WebSearch` | `search_web` | Web search with citations |
| `WebFetch` | `read_url_content` | HTML→Markdown conversion |
| `Task` tool (dispatch subagent) | `browser_subagent` | ✅ SUPPORTED — browser automation subagent |

## Antigravity-Exclusive Tools (No Claude Code Equivalent)

| Tool | Purpose | Skill Impact |
|------|---------|-------------|
| `browser_subagent` | Dispatch browser automation subagent | **Unlocks** subagent-driven-development |
| `generate_image` | AI image generation | Enhances brainstorming visual companion |
| `notify_user` | Structured user communication during tasks | Better than terminal output |
| `task_boundary` | Task progress UI with mode switching | PLANNING → EXECUTION → VERIFICATION |
| `command_status` | Monitor background commands | Async command monitoring |
| `send_command_input` | Interactive terminal input | REPL interaction |
| `multi_replace_file_content` | Multi-chunk file editing | Precise non-contiguous edits |
| `list_dir` | Directory listing with metadata | Size, type info |
| MCP: `StitchMCP` | UI design generation | Screen design/edit/variants |
| MCP: `netlify` | Deploy, project management | Direct deployment |

## Subagent Support — KEY DIFFERENCE

**Antigravity DOES support subagents** via `browser_subagent`. Unlike vanilla Gemini CLI:

- `subagent-driven-development` → **FULLY OPERATIONAL** (use `browser_subagent`)
- `dispatching-parallel-agents` → **PARTIALLY SUPPORTED** (sequential browser subagents)
- `executing-plans` → Use as **fallback** for complex multi-file tasks

### browser_subagent Usage Pattern

```
browser_subagent(
  Task: "Implement [specific task] following TDD...",
  TaskName: "Implementing Feature X",
  RecordingName: "feature_x_impl"
)
```

**Limitations vs Claude Code Task tool:**
- Browser context only (no filesystem access in subagent)
- Sequential, not parallel dispatch
- Best for: UI testing, visual verification, browser-based workflows

## ABM Workforce Integration Tools

Antigravity also has access to ABM Workforce tools via user rules:

| ABM Concept | Antigravity Mechanism |
|---|---|
| Contract creation | `write_to_file` → task.md with contract format |
| Attestation | `notify_user` with evidence paths |
| 6-step verification | `task_boundary` mode switching (PLANNING→EXECUTION→VERIFICATION) |
| Skill invocation | `view_file` on SKILL.md files |
| Evidence gathering | `run_command` + `grep_search` + `view_file` |

## Command Execution Notes (Windows)

- Shell: **PowerShell** (not bash)
- Use `run_command` with `SafeToAutoRun: true` for safe commands
- Background commands: use `WaitMsBeforeAsync` + `command_status`
- **NEVER** use `cd` — specify `Cwd` parameter instead
