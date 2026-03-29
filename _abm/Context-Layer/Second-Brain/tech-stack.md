# Tech Stack Decisions — Công Cụ & Nền Tảng

## Core Stack (Active)
| Tool | Purpose | Why Chosen | Alternative Rejected |
|------|---------|------------|---------------------|
| Antigravity | AI IDE | Local AI coding + MCP | Cursor (cloud-only) |
| Gemini 3.1 Pro | Primary LLM | Best reasoning, Viet context | GPT-4o (weaker VN) |
| Netlify | Web hosting | Free tier, easy deploy | Vercel (similar) |
| GitHub | Version control | Standard, free | GitLab |
| Zalo | Client comms | VN market standard | Telegram (less VN) |
| Google Workspace | Docs/Email | Client-familiar | MS 365 (more expensive) |

## Decision Criteria
1. Phù hợp thị trường VN (client dùng được)
2. Free tier / chi phí thấp (startup budget)
3. API/integration có sẵn
4. Vietnamese language support

## Skills Generated For Stack
- frontend-developer → HTML/CSS/JS
- database-management → Data handling
- workflow-automation → N8N/Zapier patterns
- agent-email-cli → Email automation

## Stack Evolution Log
| Date | Change | Reason |
|------|--------|--------|
| 2026-03 | Added Netlify | Need web hosting for training guides |
| 2026-03 | Added Antigravity Mobile | Remote access to IDE |
