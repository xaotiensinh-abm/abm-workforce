---
name: finishing-a-development-branch
description: Hướng dẫn hoàn thành công việc development bằng cách trình bày các lựa chọn cấu trúc để merge, tạo PR, hoặc dọn dẹp (cleanup). Dùng khi code đã xong và test đã pass.
---

# Finishing a Development Branch

Khép lại quá trình phát triển tính năng bằng cách cung cấp các lựa chọn rõ ràng và xử lý luồng công việc tương ứng do người dùng chọn.

**Nguyên tắc cốt lõi:** Xác minh test pass → Đưa ra lựa chọn → Thực thi lựa chọn → Dọn dẹp.

## Khi nào sử dụng (Triggers)
Auto-activate triggers (VN): "hoàn thành branch", "merge code", "tạo PR", "finish branch", "dọn dẹp nhánh", "đã code xong"
Auto-activate triggers (EN): "finish branch", "create PR", "merge to main", "pull request", "cleanup worktree"

## Quy trình Thực Thi

### Bước 1: Xác Minh Tests (Verify Tests)

**Trước khi đưa ra lựa chọn, PHẢI kiểm tra tests pass:**

```bash
# Run project's test suite
npm test / cargo test / pytest / go test ./...
```

**Nếu tests fail:** Báo cáo chi tiết và dừng lại, bắt buộc phải fix xong mới đi tiếp.
**Nếu tests pass:** Chuyển sang Bước 2.

### Bước 2: Xác Định Base Branch

Tìm base branch phổ biến (`main` hoặc `master`) hoặc hỏi xác nhận từ người dùng.

### Bước 3: Đưa Ra Lựa Chọn

Chỉ đưa ra đúng 4 lựa chọn gọn gàng, không giải thích dài dòng:

```
Công việc đã hoàn tất. Bạn muốn làm gì tiếp theo?

1. Merge về <base-branch> locally
2. Push & tạo Pull Request (PR)
3. Giữ nguyên branch (Để tôi tự xử lý sau)
4. Hủy bỏ (Discard) toàn bộ thay đổi
```

### Bước 4: Thực Thi Lựa Chọn

**Option 1: Merge Locally**
- Chuyển về base branch, git pull, git merge `<feature-branch>`.
- Chạy lại tests trên kết quả merge.
- Nếu pass, xóa `<feature-branch>`. Kế tiếp: Bước 5 (Dọn dẹp).

**Option 2: Push và Tạo PR**
- Push branch lên remote.
- Dùng `gh pr create` tạo PR với `Summary` và `Test Plan`. Kế tiếp: Bước 5.

**Option 3: Giữ Nguyên (Keep As-Is)**
- Báo cáo: "Đang giữ branch <name> và worktree." Không làm gì thêm. DỪNG.

**Option 4: Hủy Bỏ (Discard)**
- Cảnh báo sẽ xóa branch và toàn bộ commit, yêu cầu gõ chính xác chữ `discard` để xác nhận.
- Nếu xác nhận: Checkout base branch, Force delete feature branch. Kế tiếp: Bước 5.

### Bước 5: Dọn dẹp Worktree (Cleanup)

- Áp dụng cho Option 1, 2, 4.
- Kiểm tra xem có đang dùng git worktree hay không, nếu có hãy remove nó đi `git worktree remove <vi-tri>`.

## Red Flags (Cảnh Báo Dừng)

- ❌ Merge khi chưa chạy test kiểm chứng output cuối cùng.
- ❌ Xóa code khi chưa có confirm `discard` rõ ràng từ lệnh Option 4.
- ❌ Hỏi chung chung "Làm gì tiếp?". Phải đưa rõ 4 Options.
