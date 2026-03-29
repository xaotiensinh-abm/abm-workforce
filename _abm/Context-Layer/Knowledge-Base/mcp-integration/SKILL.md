---
name: "mcp-integration"
description: "Tích hợp MCP Servers — kết nối Notion, Google Workspace, Slack, Trello, Jira trực tiếp từ ABM. Protocol chuẩn Model Context Protocol."
---

# 🔌 MCP Integration — Kết Nối Hệ Sinh Thái

Tích hợp các dịch vụ bên ngoài qua Model Context Protocol (MCP).

## Sử dụng khi

- Cần đọc/ghi Notion pages
- Sync tasks với Trello/Jira
- Đọc Google Docs/Sheets
- Gửi tin nhắn Slack

## KHÔNG sử dụng khi

- Dùng email → dùng `agent-email-cli`
- File office local → dùng `docx`/`xlsx`/`pptx`
- Chỉ cần search web → dùng built-in tools

## MCP SERVERS REGISTRY

| Server | Chức năng | Config |
|--------|----------|--------|
| `@modelcontextprotocol/server-google-drive` | Google Drive read/write | API key |
| `@notionhq/notion-mcp-server` | Notion pages/databases | Integration token |
| `@modelcontextprotocol/server-slack` | Slack messages/channels | Bot token |
| `@modelcontextprotocol/server-github` | GitHub issues/PRs | PAT |
| `@modelcontextprotocol/server-postgres` | PostgreSQL queries | Connection string |

## SETUP

```json
// .gemini/settings.json hoặc mcp-config.json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    },
    "google-drive": {
      "command": "npx",
      "args": ["-y", "@anthropic/google-drive-mcp-server"],
      "env": {
        "GOOGLE_SERVICE_ACCOUNT_KEY": "${GOOGLE_KEY}"
      }
    }
  }
}
```

## SECURITY

1. API keys → `.env` file, KHÔNG hardcode
2. Read-only mặc định — write cần CEO xác nhận
3. Rate limiting: tối đa 100 calls/phút/server
4. Audit log: mọi MCP call đều log

## QUY TẮC

1. **Sandbox mode**: MCP write operations cần CEO duyệt (giống email)
2. **Fallback**: Nếu MCP server down → thông báo, KHÔNG crash
3. **Credentials**: KHÔNG BAO GIỜ hardcode API keys

---

## Nguồn gốc
- Wave 2 v3.0: MCP Integration
