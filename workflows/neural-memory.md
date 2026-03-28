---
description: 🧠 Quản lý NeuralMemory - Working Memory Layer cho Antigravity
---

# NeuralMemory Workflow

> **Layer 2: Working Memory** — Bổ sung cho KI (Layer 1) và Conversation Logs (Layer 3)

## Khi nào dùng
- Lưu quyết định, insight, context trong quá trình làm việc
- Recall thông tin qua liên tưởng (associative recall)
- Index codebase để nhớ code-level context
- Thay thế manual `/save-brain` cho working memory

## Quick Reference

### Lưu trí nhớ
```bash
# Auto-detect type
nmem remember "Nội dung cần nhớ"

# Specify type
nmem remember "Quyết định dùng PostgreSQL" --type decision
nmem remember "Pattern: always validate input" --type insight
nmem remember "API docs: https://..." --type reference
nmem todo "Review PR #123" --priority 7
```

### Recall trí nhớ
```bash
nmem recall "auth bug"              # Tìm qua spreading activation
nmem recall "database" --depth 2    # Deep traversal
nmem last 5                         # 5 trí nhớ gần nhất
nmem today                          # Trí nhớ hôm nay
```

### Brain management
```bash
nmem brain list                     # Liệt kê brains
nmem brain create <name>            # Tạo brain mới
nmem brain use <name>               # Chuyển brain
nmem brain health                   # Kiểm tra sức khỏe
nmem brain export -o backup.json    # Export
nmem brain import backup.json       # Import
```

### Codebase indexing
```bash
nmem index src/                     # Index thư mục code
```

### Memory lifecycle
```bash
nmem decay                          # Áp dụng forgetting curve
nmem consolidate                    # Gộp, cắt tỉa, tóm tắt
nmem cleanup                        # Xóa trí nhớ hết hạn
```

### Visual tools
```bash
nmem dashboard                      # Terminal dashboard
nmem ui                             # Interactive browser
nmem graph "keyword"                # Visualize connections
```

### Server mode
```bash
nmem serve                          # localhost:8000
nmem serve -p 9000                  # Custom port
```

## Workflow tích hợp

### Đầu buổi làm việc
```
1. nmem recap                       # Load context từ session trước
2. /recap                           # KI + conversation context (nếu cần)
```

### Trong quá trình làm việc
```
- nmem remember tự động qua MCP tools
- Hoặc thủ công: nmem remember "..." --type <type>
```

### Cuối buổi làm việc
```
1. nmem consolidate                 # Gộp working memory
2. /save-brain                      # Lưu KI (strategic knowledge)
```

## MCP Configuration

Thêm vào MCP config của editor:
```json
{
  "neural-memory": {
    "command": "nmem-mcp"
  }
}
```

## Brain Stack Architecture
```
Layer 1: Strategic Knowledge (KI)     → Curated, long-term
Layer 2: Working Memory (NeuralMemory) → Dynamic, associative
Layer 3: Conversation Logs             → Raw history
```
