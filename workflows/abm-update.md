---
description: 🔄 Cập nhật ABM-Workforce từ repo gốc GitHub
---

# /ABM-update — Auto-Update ABM-Workforce

## Mục đích
Tự động cập nhật ABM-Workforce v6 từ GitHub repo gốc (`ABM-code-org/ABM-Workforce`).

## Quy trình

// turbo-all

### Step 1: Kiểm tra phiên bản hiện tại
```
node -e "const p=require('C:/Users/PC/.gemini/antigravity/ABM-Workforce/package.json'); console.log('Current ABM version: v' + p.version)"
```

### Step 2: Chạy ABM-update script
```
powershell -ExecutionPolicy Bypass -File C:\Users\PC\.gemini\antigravity\scripts\ABM-update.ps1
```

### Step 3: Verify phiên bản mới
```
node -e "const p=require('C:/Users/PC/.gemini/antigravity/ABM-Workforce/package.json'); console.log('Updated ABM version: v' + p.version)"
```

### Step 4: Xác nhận cấu trúc _ABM/
```
dir C:\Users\PC\.gemini\antigravity\ABM-Workforce\_ABM /b
```

### Step 5: Báo cáo kết quả
Báo cáo cho user:
- Phiên bản trước → phiên bản sau
- Các thay đổi (nếu có)
- Trạng thái: ✅ Success hoặc ❌ Failed

## Troubleshooting
- **Git conflict**: Chạy `git -C C:\Users\PC\.gemini\antigravity\ABM-Workforce reset --hard origin/main` rồi retry
- **npm error**: Xóa `node_modules` và chạy `npm install --production` lại
- **ABM install error**: Chạy full install: `node tools/cli/ABM-cli.js install --directory . --modules bmm --tools none --yes`
