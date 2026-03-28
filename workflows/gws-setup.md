---
description: 🔧 Cài đặt và cấu hình Google Workspace CLI (gws) — từ install đến auth hoàn chỉnh
---

# GWS CLI Setup — Quy Trình Chuẩn

> **Mục tiêu**: Cài đặt `gws` CLI + 89 AI Agent Skills + xác thực OAuth đầy đủ scopes.
> **Thời gian dự kiến**: 10-15 phút (nếu đã có GCP project)

---

## Phase 0: Kiểm Tra Điều Kiện

```bash
# Kiểm tra Node.js 18+
node --version

# Kiểm tra gcloud CLI
gcloud --version

# Kiểm tra đăng nhập gcloud (phải là USER account, không phải service account)
gcloud auth list
```

> [!CAUTION]
> Nếu gcloud chỉ có **service account** (dạng `xxx-compute@developer.gserviceaccount.com`),
> PHẢI login bằng user account trước:
> ```bash
> gcloud auth login --no-launch-browser
> # Mở URL → đăng nhập → paste verification code
> ```

---

## Phase 1: Cài Đặt CLI

```bash
# Cài gws CLI global
npm install -g @googleworkspace/cli

# Verify
gws --version
```

---

## Phase 2: Cài Đặt AI Agent Skills

### Option A: Clone repo và copy skills (Recommended)

```bash
# Clone repo
git clone https://github.com/googleworkspace/cli.git gws-cli-repo

# Copy 89 skills vào Antigravity skills directory
# Windows:
Copy-Item -Path "gws-cli-repo\skills\*" -Destination "C:\Users\PC\.gemini\antigravity\skills\" -Recurse -Force

# Linux/macOS:
cp -r gws-cli-repo/skills/* ~/.gemini/antigravity/skills/

# Cleanup (optional)
rm -rf gws-cli-repo
```

### Option B: Cherry-pick skills

```bash
# Chỉ copy skills cần thiết
cp -r gws-cli-repo/skills/gws-drive ~/.gemini/antigravity/skills/
cp -r gws-cli-repo/skills/gws-gmail ~/.gemini/antigravity/skills/
cp -r gws-cli-repo/skills/gws-sheets ~/.gemini/antigravity/skills/
# ...
```

### Danh sách skills theo category:

| Category | Skills (38 gws-*) | Description |
|----------|-------------------|-------------|
| **Core Services** | gws-drive, gws-gmail, gws-calendar, gws-sheets, gws-docs, gws-slides, gws-tasks, gws-chat, gws-people, gws-keep, gws-forms, gws-meet, gws-classroom, gws-events, gws-admin-reports, gws-modelarmor | API wrappers |
| **Shortcuts** | gws-drive-upload, gws-gmail-send, gws-gmail-triage, gws-gmail-watch, gws-calendar-agenda, gws-calendar-insert, gws-chat-send, gws-docs-write, gws-sheets-append, gws-sheets-read, gws-events-subscribe, gws-events-renew, gws-modelarmor-* | One-click actions |
| **Workflows** | gws-workflow, gws-workflow-email-to-task, gws-workflow-meeting-prep, gws-workflow-standup-report, gws-workflow-weekly-digest, gws-workflow-file-announce | Cross-service automations |
| **Personas** | persona-exec-assistant, persona-project-manager, persona-sales-ops, persona-content-creator, persona-customer-support, persona-event-coordinator, persona-hr-coordinator, persona-it-admin, persona-researcher, persona-team-lead | Role-based agents |
| **Recipes** | 50 recipe-* skills | Ready-made automations |
| **Shared** | gws-shared | Auth + CLI reference |

---

## Phase 3: Chuẩn Bị GCP Project

### 3.1 Chọn / Tạo Project

```bash
# Dùng project có sẵn
gcloud config set project YOUR_PROJECT_ID

# Hoặc tạo project mới (cần quota)
gcloud projects create gws-workspace-2026 --name="GWS Workspace"
```

### 3.2 Enable APIs Bắt Buộc

```bash
gcloud services enable \
  serviceusage.googleapis.com \
  drive.googleapis.com \
  gmail.googleapis.com \
  calendar-json.googleapis.com \
  sheets.googleapis.com \
  docs.googleapis.com \
  slides.googleapis.com \
  tasks.googleapis.com \
  chat.googleapis.com \
  people.googleapis.com \
  keep.googleapis.com \
  forms.googleapis.com \
  meet.googleapis.com \
  classroom.googleapis.com \
  admin.googleapis.com \
  pubsub.googleapis.com \
  --project=YOUR_PROJECT_ID
```

### 3.3 Tạo OAuth Client (THỦ CÔNG — bắt buộc)

> [!IMPORTANT]
> `gws auth setup` KHÔNG THỂ tự tạo OAuth client. Phải làm thủ công trên Cloud Console.

1. **OAuth Consent Screen**: `https://console.cloud.google.com/apis/credentials/consent?project=YOUR_PROJECT_ID`
   - User Type: **External**
   - App name: `gws CLI`
   - Support email: email của bạn
   - **Scopes** → Add or Remove Scopes → thêm:
     - `../auth/drive`
     - `../auth/gmail.modify`
     - `../auth/calendar`
     - `../auth/spreadsheets`
     - `../auth/documents`
     - `../auth/presentations`
     - `../auth/tasks`
   - **Test users** → Add email của bạn
   - Save & Continue qua hết

2. **Create OAuth Client**: `https://console.cloud.google.com/apis/credentials?project=YOUR_PROJECT_ID`
   - Create Credentials → OAuth client ID
   - Type: **Desktop app**
   - Name: `gws CLI`
   - **Download JSON file**

3. **Copy file JSON**:
   ```bash
   # Windows:
   New-Item -ItemType Directory -Path "$env:USERPROFILE\.config\gws" -Force
   Copy-Item "path\to\client_secret_xxx.json" "$env:USERPROFILE\.config\gws\client_secret.json"

   # Linux/macOS:
   mkdir -p ~/.config/gws
   cp path/to/client_secret_xxx.json ~/.config/gws/client_secret.json
   ```

### 3.4 Publish OAuth App (Khuyến nghị)

> [!TIP]
> **Testing mode** giới hạn số scopes và token hết hạn sau 7 ngày.
> Nếu chỉ dùng cá nhân, **Publish** app để tránh giới hạn.

- Vào OAuth Consent Screen → bấm **Publish App**
- Không cần Google verification nếu dùng scopes ở mức "Recommended"

---

## Phase 4: Đăng Nhập OAuth

> [!CAUTION]
> **PHẢI dùng `--scopes` hoặc `--full` flag.** Flag `-s` CHỈ filter scope picker, KHÔNG thêm scopes vào OAuth URL.

```bash
# Option A: Full scopes (khuyến nghị)
gws auth login --full

# Option B: Chọn scopes cụ thể
gws auth login --scopes "https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/gmail.modify,https://www.googleapis.com/auth/calendar,https://www.googleapis.com/auth/spreadsheets,https://www.googleapis.com/auth/documents,https://www.googleapis.com/auth/presentations,https://www.googleapis.com/auth/tasks"
```

- Mở URL in ra → chọn account → **Allow tất cả scopes**
- Nếu thấy "Google hasn't verified this app" → bấm **Continue**

---

## Phase 5: Xác Minh

```bash
# Check auth status
gws auth status

# Test Drive
gws drive files list --params '{\"pageSize\": 3}'

# Test Gmail
gws gmail users messages list --params '{\"userId\": \"me\", \"maxResults\": 3}'

# Test Calendar
gws calendar calendarList list --params '{\"maxResults\": 3}'

# Test Sheets (tạo spreadsheet)
gws sheets spreadsheets create --json '{\"properties\": {\"title\": \"Test GWS\"}}'
```

---

## Troubleshooting

### ❌ Lỗi 403: insufficient scopes (sau khi auth thành công)

**Root cause**: `token_cache.json` cache access token CŨ (không có scopes mới).

```bash
# FIX: Xóa token cache
# Windows:
Remove-Item "$env:USERPROFILE\.config\gws\token_cache.json" -Force
Remove-Item "$env:USERPROFILE\.config\gws\cache" -Recurse -Force

# Linux/macOS:
rm -f ~/.config/gws/token_cache.json
rm -rf ~/.config/gws/cache/

# Rồi chạy lại command → gws sẽ tự refresh token với đủ scopes
gws drive files list --params '{\"pageSize\": 3}'
```

### ❌ Lỗi 403: API not enabled

```bash
# FIX: Enable API cần thiết
gcloud services enable drive.googleapis.com --project=YOUR_PROJECT_ID
```

### ❌ Login chỉ có openid + userinfo.email

**Root cause**: Dùng `-s` flag thay vì `--scopes` flag.

```bash
# SAI: -s chỉ filter scope picker
gws auth login -s drive,gmail

# ĐÚNG: --scopes truyền scopes vào OAuth URL
gws auth login --scopes "https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/gmail.modify"

# ĐÚNG: --full lấy tất cả scopes
gws auth login --full
```

### ❌ PowerShell JSON escaping

```powershell
# SAI: Single quotes bị strip
gws drive files list --params '{"pageSize": 3}'

# ĐÚNG: Escape double quotes
gws drive files list --params '{\"pageSize\": 3}'
```

### ❌ gws auth setup thất bại

**Root cause**: Không thể tự tạo OAuth client via API.
**FIX**: Tạo thủ công trên Cloud Console (xem Phase 3.3).

### ❌ gcloud: Service Usage API not enabled

```bash
# FIX: Login bằng user account (không phải service account)
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable serviceusage.googleapis.com
```

### ❌ Project quota exceeded

**FIX**: Dùng project có sẵn hoặc xóa project cũ không dùng:
```bash
gcloud projects list
gcloud projects delete OLD_PROJECT_ID
```

---

## Full Reset (Nuclear Option)

Khi mọi thứ bị hỏng, reset toàn bộ:

```bash
# 1. Logout
gws auth logout

# 2. Xóa toàn bộ config
# Windows:
Remove-Item "$env:USERPROFILE\.config\gws" -Recurse -Force

# Linux/macOS:
rm -rf ~/.config/gws/

# 3. Bắt đầu lại từ Phase 3.3 (copy client_secret.json) → Phase 4 (login)
```

---

## MCP Server (Bonus)

Dùng `gws` như MCP server cho Claude Desktop, Gemini CLI, VS Code:

```json
{
  "mcpServers": {
    "gws": {
      "command": "gws",
      "args": ["mcp", "-s", "drive,gmail,calendar,sheets,docs"]
    }
  }
}
```

> [!TIP]
> Mỗi service thêm 10-80 tools. Giữ số service ít để không vượt tool limit (~50-100).

---

## Cấu Trúc Files

```
~/.config/gws/
├── client_secret.json     # OAuth client config (from Cloud Console)
├── credentials.enc        # Encrypted OAuth credentials (AES-256-GCM)
├── .encryption_key        # Encryption key (OS Keyring backup)
├── token_cache.json       # Cached access token (⚠️ xóa khi đổi scopes)
└── cache/                 # API schema cache
    ├── drive_v3.json
    ├── gmail_v1.json
    └── calendar_v3.json
```

---

*GWS CLI Setup Workflow v1.0 — Antigravity Workflow Framework*
*Verified: 2026-03-06*
