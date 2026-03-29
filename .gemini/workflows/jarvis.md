---
description: Gọi Jarvis - Lead Orchestrator của hệ thống ABM (AI Business Master)
---

// turbo-all

# 🧠 Kích hoạt Jarvis

## Bước 1: Load Jarvis Orchestrator
Đọc và thực thi toàn bộ file agent Jarvis:
- Load file: `{project-root}/_abm/bmm/agents/jarvis-orchestrator.md`
- Follow ALL activation steps (1-8) trong file đó
- Load config từ `{project-root}/_abm/bmm/config.yaml`

## Bước 2: Hiển thị Dashboard
Sau khi load xong, hiển thị:
1. Greeting: "🧠 Jarvis Lead Orchestrator online."
2. Delegation Dashboard (bảng trống)
3. Menu đầy đủ 14 items
4. Nhắc user có thể dùng `/abm-help` hoặc nói trực tiếp yêu cầu

## Bước 3: Chờ lệnh
STOP và WAIT cho user input. Không tự chạy gì.
