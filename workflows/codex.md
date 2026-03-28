---
description: 🤖 Gọi Codex CLI để xử lý coding tasks bằng GPT-5.x (ChatGPT Team)
---

# /codex — Antigravity ↔ Codex CLI Bridge

Workflow này cho phép Antigravity dispatch coding tasks xuống OpenAI Codex CLI,
tận dụng GPT-5.x từ ChatGPT Team subscription.

// turbo-all

## Khi nào dùng

- Cần implement feature phức tạp (GPT-5 mạnh code hơn)
- Muốn chạy multi-agent song song trên cùng repo
- Cần sandbox execution an toàn
- Muốn cross-validate output giữa Gemini và GPT-5

## Prerequisites

- Codex CLI đã cài: `npm install -g @openai/codex`
- Đã đăng nhập ChatGPT Team: `codex` → Sign in
- File `AGENTS.md` đã có tại project root

## Workflow Steps

### 1. Xác định task cần giao cho Codex
Antigravity phân tích yêu cầu user và soạn prompt rõ ràng cho Codex.
Task phù hợp cho Codex:
- Code implementation (new features, refactoring)
- Bug fixing (với error logs)
- Test writing
- Code review

### 2. Chạy Codex CLI với prompt
Mở terminal và chạy:

```powershell
# Mode suggest (review trước khi apply)
codex "Implement a REST API endpoint for user authentication using JWT tokens in Express.js"

# Mode auto-edit (tự áp dụng changes)
codex --approval-mode auto-edit "Fix the TypeScript compilation errors in src/api/"

# Mode full-auto (hoàn toàn tự động, chạy trong sandbox)
codex --approval-mode full-auto "Refactor the database module to use connection pooling"
```

### 3. Chạy Codex với prompt dạng non-interactive (headless)
Khi muốn Antigravity gọi tự động mà không cần TUI:

```powershell
# Quiet mode — chỉ output kết quả, không TUI
codex -q "Write unit tests for src/utils/validator.ts"
```

### 4. Multi-agent cho task phức tạp
Với task lớn, Codex tự chia thành nhiều sub-agents chạy song song:

```powershell
codex "Implement the complete user management module: 
1. Create User model with validation
2. Create CRUD API endpoints  
3. Write comprehensive tests
4. Add API documentation"
```

### 5. Review kết quả
- Kiểm tra code changes trong Git diff
- Chạy tests: `npm test` hoặc `go test ./...`
- Nếu OK → commit. Nếu cần chỉnh → chạy Codex lại

## Tips

### Prompt hiệu quả cho Codex
```
BAD:  "fix the bug"
GOOD: "Fix the NullPointerException in UserService.getProfile() 
       when user.email is null. Add null check and return 
       appropriate error response with HTTP 400."
```

### Kết hợp Antigravity + Codex tối ưu
```
Antigravity: /plan → tạo spec chi tiết
Codex CLI:   Implement theo spec
Antigravity: /test → verify kết quả  
Antigravity: /audit → review security
```

### Xem models có sẵn
```powershell
# Trong Codex TUI, dùng:
/model
# Để switch model runtime
```
