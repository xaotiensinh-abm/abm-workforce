---
name: using-git-worktrees
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: "Dùng trước khi bắt tay làm Feature lớn hoặc thực thi Hợp đồng - tự động dọn dẹp và tạo nhánh Git Worktree ảo cách ly."
---

# Ảo Hóa Nhánh Git (Using Git Worktrees)

## Tổng Quan

Làm việc trên `git worktrees` giúp bạn tung hoành code trên nhiều nhánh cùng một lúc mà không sợ tạo ra đống rác (unstashed changes).
Thử nghiệm ảo, đập bỏ không sót lại vết tích.

**Khai báo lúc bắt đầu:** "Tôi sẽ dùng lệnh `using-git-worktrees` để đẻ ra một phân khu code cách ly an toàn."

## Trình Tự Chọn Thư Mục (Directory Selection)

Ưu tiên theo phân cấp:
### 1. Tìm Ổ Trống 
```bash
ls -d .worktrees 2>/dev/null     # Ưu tiên 1 (Thư mục ẩn đỡ rác mắt)
ls -d worktrees 2>/dev/null      # Ưu tiên 2
```
Nếu có sẵn thì xài luôn.

### 2. Kiểm Tra Lệnh Bài (CLAUDE.md / GEMINI.md)
```bash
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
grep -i "worktree.*director" GEMINI.md 2>/dev/null
```

### 3. Hỏi Sếp (Ask User)
Nếu không có 2 cái trên:
"Thưa CEO, tạo thư mục Worktree ở đâu bây giờ:
1. `[TênDựÁn]/.worktrees/` (Tạo ngay trong repo hiện tại, ẩn đi)
2. `~/.config/abm/worktrees/<project-name>/` (Lưu ngoài hệ điều hành máy chủ Global)

Sếp chọn phương án nào?"

## Khâu Kiểm Định An Toàn (Safety Verirfication)

**BẮT BUỘC Check file `.gitignore` nếu chốt phương án 1:**
```bash
git check-ignore -q .worktrees 2>/dev/null || git check-ignore -q worktrees 2>/dev/null
```
**Nếu CẢNH SÁT BÁO LÀ CHƯA IGNORE:**
Theo luật sửa sai lập tức của ABM:
1. Lập tức bổ sung `.worktrees` vào `.gitignore` 
2. Commit lên git.
3. Chờ test qua rồi Mới làm tiếp. 
*(Quy tắc máu: Không bao giờ được phép đẩy file của nhánh worktrees đè lên History Github)*.

## Mở Cổng Tác Chiến (Creation Steps)

1. Tự chích xuất độ thuôn Tên dự án: `project=$(basename "$(git rev-parse --show-toplevel)")`
2. Tạo Worktree: `git worktree add <path> -b <tên-nhánh>`
3. Nhảy dù vào tọa độ mới: `cd <path>`
4. Lắp ráp vũ khí (Project Setup): `npm install`, `cargo build`, `pip install`, `go mod`... 
5. **Đo Lường Sinh Hiệu Gốc:** Chạy `npm test` hoặc `pytest`. Phải XANH 100% (Baseline Sạch) mới được bắt tay gõ code tính năng mới. Nếu tạch từ đầu, báo sếp ngay.
6. Báo cáo Tọa độ hành quân: 
> "Worktree đã sẵn sàng tại `<path>`. 100% Test gốc màu xanh. Đã sẵn sàng nã đạn thực thi Hợp Đồng!"

## Tích Hợp Hệ Sinh Thái (Integration)
Đây là skill **BẮT BUỘC** được kích hoạt tự động bởi các Agent khi:
- Bắt đầu lệnh `executing-plans`.
- Phái lính đi chặt chém trong `subagent-driven-development`.
- `finishing-a-development-branch` dùng để cất dọn bãi rác worktree này sau khi merge.
