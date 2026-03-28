---
description: Cài đặt OpenClaw từ GitHub source — full build + ChatGPT OAuth + Telegram + Auto-Start
---
// turbo-all

# OpenClaw Full Setup from GitHub

> Quy trình cài đặt tối ưu cho Windows, đã kiểm chứng.

## Prerequisites

Kiểm tra trước khi bắt đầu:

```powershell
node --version     # Cần >= 22
pnpm --version     # Cần >= 10
git --version      # Cần có Git + Git Bash
```

**Git Bash** cần có tại `D:\Git\bin\bash.exe` (hoặc chỉnh PATH tương ứng) — cần cho build step A2UI.

## Phase 1: Clone + Install + Build

```powershell
# 1. Clone repo
git clone https://github.com/openclaw/openclaw.git D:\OpenClaw

# 2. Install dependencies (37 workspaces)
cd D:\OpenClaw
pnpm install

# 3. Build UI
pnpm ui:build

# 4. Full build (cần Git Bash trong PATH cho A2UI shell script)
$env:PATH = "D:\Git\bin;D:\Git\usr\bin;$env:PATH"
pnpm build
```

## Phase 2: Onboard (Interactive)

Chạy trong **cửa sổ CMD riêng** (KHÔNG phải terminal piped) để browser OAuth popup hoạt động:

```cmd
cd /d D:\OpenClaw
pnpm openclaw onboard --auth-choice openai-codex --skip-skills
```

**Bước interactive:**
1. Continue? → **Yes**
2. Mode → **QuickStart**
3. Browser OAuth → **Đăng nhập ChatGPT**
4. Telegram → Paste bot token từ @BotFather
5. Hoàn tất → Dashboard URL hiện ra

## Phase 3: Fix Model Config

Onboard có thể default model sang Anthropic. Kiểm tra và fix:

```powershell
# Xem model hiện tại
pnpm openclaw gateway --force
# Nếu log hiện "agent model: anthropic/..." → cần fix
```

Mở `D:\OpenClaw\state\openclaw.json` và đảm bảo có:

```json
{
  "auth": {
    "profiles": {
      "openai-codex:default": {
        "provider": "openai-codex",
        "mode": "oauth"
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "openai-codex/gpt-5.3-codex"
      }
    }
  }
}
```

## Phase 4: Telegram Pairing

```powershell
# Nhắn tin cho bot trên Telegram → nhận pairing code
# Approve:
pnpm openclaw pairing approve telegram <CODE>
```

## Phase 5: Auto-Start + Auto-Restart

### Tạo wrapper script `D:\OpenClaw\openclaw-autostart.cmd`:

```cmd
@echo off
title OpenClaw Gateway [Auto-Restart]
cd /d "D:\OpenClaw"
set PATH=D:\Git\bin;D:\Git\usr\bin;%PATH%
:start
echo [%date% %time%] Starting OpenClaw Gateway...
call pnpm openclaw gateway --force
echo [%date% %time%] Gateway exited. Restarting in 5s...
timeout /t 5 /nobreak >nul
goto start
```

### Đăng ký Windows Scheduled Task (chạy Admin):

```powershell
schtasks /create /tn "OpenClaw Gateway" /tr "D:\OpenClaw\openclaw-autostart.cmd" /sc onlogon /rl highest /f
```

## Phase 6: Verify

```powershell
# Health check
pnpm openclaw health

# Status
pnpm openclaw status --deep

# Dashboard
# http://127.0.0.1:18789/#token=<TOKEN_FROM_CONFIG>
```

## Troubleshooting

| Vấn đề | Nguyên nhân | Fix |
|---------|------------|-----|
| `pnpm build` fail A2UI | Thiếu bash | Thêm Git Bash vào PATH |
| Browser OAuth không popup | Terminal piped | Chạy onboard trong CMD riêng |
| Model mismatch (anthropic) | Config thiếu model | Thêm `model.primary` vào JSON |
| Gateway token mismatch | Dashboard cached | Dùng URL có `#token=...` |
| Telegram "access not configured" | Chưa pairing | `openclaw pairing approve telegram <CODE>` |
