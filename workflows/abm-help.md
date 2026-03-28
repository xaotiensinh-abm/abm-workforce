---
description: 🧙 ABM-Workforce Help — Hướng dẫn sử dụng ABM agents & workflows
---

# /ABM-help — ABM-Workforce Intelligent Guide

## Mục đích
Điểm vào chính cho ABM-Workforce trong Antigravity. Hướng dẫn user chọn agent/workflow phù hợp.

## Quy trình

### Step 1: Load ABM Help Database
Đọc file: `C:\Users\PC\.gemini\antigravity\ABM-Workforce\_ABM\_config\ABM-help.csv`

File này chứa toàn bộ knowledge base của ABM về:
- Các agent có sẵn và khi nào nên dùng
- Các workflow và thứ tự thực hiện
- Các skill và trigger
- Hướng dẫn cho từng giai đoạn dự án

### Step 2: Xác định ngữ cảnh User
Hỏi user (hoặc detect từ câu hỏi):
1. User đang ở giai đoạn nào? (Brainstorming → Planning → Architecture → Implementation)
2. Loại project? (New / Existing / Bug fix)
3. Độ phức tạp? (Quick fix → Small project → Enterprise)

### Step 3: Recommend Agent & Workflow
Dựa trên ngữ cảnh, recommend:

| Giai đoạn | Agent | Workflow |
|---|---|---|
| Brainstorming | ABM Master | `ABM-brainstorming` |
| Analysis | Analyst | `ABM-domain-research`, `ABM-create-product-brief` |
| Planning | PM | `ABM-create-prd`, `ABM-create-ux-design` |
| Architecture | Architect | `ABM-create-architecture` |
| Epics & Stories | PM/SM | `ABM-create-epics-and-stories` |
| Implementation | Dev | `ABM-dev-story`, `ABM-sprint-planning` |
| Quick Fix | Quick-Flow | `ABM-quick-spec`, `ABM-quick-dev` |
| Testing | QA | `ABM-code-review` |
| Documentation | Tech Writer | `ABM-document-project` |

### Step 4: Load Agent
Khi user chọn agent, load file tương ứng từ:
`C:\Users\PC\.gemini\antigravity\ABM-Workforce\_ABM\bmm\agents\{agent-name}.md`

Danh sách agents:
- `analyst.md` — Analyst
- `architect.md` — Architect
- `dev.md` — Developer
- `pm.md` — Product Manager
- `qa.md` — QA Engineer
- `quick-flow-solo-dev.md` — Quick Flow Solo Dev
- `sm.md` — Scrum Master
- `ux-designer.md` — UX Designer

Core agent:
- `C:\Users\PC\.gemini\antigravity\ABM-Workforce\_ABM\core\agents\ABM-master.md` — ABM Master

### Step 5: Execute
Follow hướng dẫn trong agent file. Agent sẽ:
1. Greet user
2. Show menu
3. Guide through workflow
4. Save outputs to `_ABM-output/`

## Quick Reference

```
/ABM-help                  → Help tổng quát
/ABM-help brainstorming    → Bắt đầu brainstorming
/ABM-help I have an idea   → Hướng dẫn từ ý tưởng
/ABM-help architecture     → Tạo kiến trúc
/ABM-help quick fix        → Quick Fix flow
/ABM-update                → Cập nhật ABM từ GitHub
```

## ABM Paths
- **Repo**: `C:\Users\PC\.gemini\antigravity\ABM-Workforce\`
- **Installed**: `C:\Users\PC\.gemini\antigravity\ABM-Workforce\_ABM\`
- **Config**: `C:\Users\PC\.gemini\antigravity\ABM-Workforce\_ABM\bmm\config.yaml`
- **Agents**: `C:\Users\PC\.gemini\antigravity\ABM-Workforce\_ABM\bmm\agents\`
- **Workflows**: `C:\Users\PC\.gemini\antigravity\ABM-Workforce\_ABM\bmm\workflows\`
- **Output**: `C:\Users\PC\.gemini\antigravity\ABM-Workforce\_ABM-output\`
