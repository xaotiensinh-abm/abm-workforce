---
name: abm-audit-file-refs
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: Audit ABM source files for file-reference convention violations using parallel Haiku subagents. Use when users requests an "audit file references" for a skill, workflow or task.
---

# audit-file-refs

Audit new-format ABM source files for file-reference convention violations using parallel Haiku subagents.

## Convention

In new-format ABM workflow and task files (`src/bmm/`, `src/core/`, `src/utility/`), every file path reference must use one of these **valid** forms:

- `{project-root}/_abm/path/to/file.ext` — canonical form, always correct
- `{installed_path}/relative/path` — valid in new-format step files (always defined by workflow.md before any step is reached)
- Template/runtime variables: `{nextStepFile}`, `{workflowFile}`, `{{mustache}}`, `{output_folder}`, `{communication_language}`, etc. — skip these, they are substituted at runtime

**Flag any reference that uses:**

- `./step-NN.md` or `../something.md` — relative paths
- `step-NN.md` — bare filename with no path prefix
- `steps/step-NN.md` — bare steps-relative path (missing `{project-root}/_abm/...` prefix)
- `` `_abm/core/tasks/help.md` `` — bare `_abm/` path (missing `{project-root}/`)
- `/Users/...`, `/home/...`, `C:\...` — absolute system paths

References inside fenced code blocks (``` ``` ```) are examples — skip them.

Old-format files in `src/bmm/workflows/4-implementation/` use `{installed_path}` by design within the XML calling chain — exclude that directory entirely.

## 📚 Bách Khoa Toàn Thư (Knowledge Base & SOPs)

> [!TIP]
> File này đã được Đại Phẫu V2 ép chuẩn Kiến Trúc 9-Layer (Lazy-Loading) bởi ABM. Các ví dụ, giới hạn, và quy trình xử lý cồng kềnh đã được rút vứt vào kho dự phòng.
> Để đọc bộ tài liệu đầy đủ cực kỳ quan trọng đó, hãy chạy Tool `view_file` dọc vào đây trước khi bắt tay làm:
> 👉 **/Users/dungtq/ABM-Workforce/.agents/skills/abm-audit-file-refs/references/sop.md**

<!-- 📦 Refactored by ABM Skill Architect v2.0 | Mass-Extraction Token Decoupling -->
