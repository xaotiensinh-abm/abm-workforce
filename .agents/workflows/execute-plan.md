---
description: "Khai hỏa thực thi Hợp đồng Code đã được duyệt. Tự động tuân thủ vòng lặp Code-Test-Review của ABM."
---

// turbo-all

# ⚙️ Execute Plan — Plan → Code

## Bước 1: Load Executing Plans Skill
Đọc và thực thi toàn bộ skill:
- Load file: `{project-root}/.agents/skills/executing-plans/SKILL.md`
- Follow ALL steps trong skill

## Bước 2: Thực thi Plan
1. Đọc implementation plan
2. Set up git worktree nếu cần
3. Thực hiện từng task theo thứ tự
4. Verification after each batch
5. Code review khi hoàn thành

## Bước 3: Verification
Sau khi thực thi xong → bắt buộc tuân thủ `evidence-driven-verification` skill để lập Báo cáo Bằng Chứng Nghiệm Thu. Cấm báo "Done" suông.
