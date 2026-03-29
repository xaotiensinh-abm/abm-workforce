---
description: Sync manifests sau khi thay đổi skills/agents/workers
---
// turbo-all

# 🔄 Manifest Sync

## Bước 1: Run Sync Script
```powershell
& "G:\AGY\_abm\_config\manifest-sync.ps1"
```

## Bước 2: Verify
- Check skill count matches actual directories
- Check agent count includes SubAgents + Workers
- Report differences if any

## Bước 3: Confirm
Hiển thị kết quả sync cho CEO
