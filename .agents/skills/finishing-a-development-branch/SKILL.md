---
name: finishing-a-development-branch
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: "Sử dụng khi đã code xong, Pass 100% test, và cần quyết định cách gộp (Merge) nhánh code này vào cội nguồn hiện tại."
---

# Đóng Gói Nhánh Phát Triển (Finishing Branch)

## Tổng Quan

Sau khi đâm chém chán chê ở nhánh ảo (nhánh dev), kỹ năng này giúp dọn mâm sạch sẽ, trình diện các Option gộp nhánh rõ ràng cho sếp (CEO).

**Nguyên Tắc Lõi:** Kiểm chứng Test -> Đưa Option Cơ Học -> Thi Hành Lệnh -> Đốt Rác (Clean up).

**Khai báo khi bắt đầu:** "Tôi sẽ dùng lệnh `finishing-a-development-branch` để chốt sổ công việc nhánh hiện tại."

## Quy Trình (The Process)

### Bước 1: Ấn Chứng (Verify Tests)
**TRƯỚC KHI trình bày option, phải chạy full bộ Test:**
```bash
npm test / cargo test / pytest / go test ./...
```
**Nếu lòi ra cục Đỏ (Fail):**
> Phát ngôn báo lại: "Thưa CEO, Test vẫn fail <N> phát. [Show Log Lỗi Nhỏ]. Tuyệt đối không dọn mâm gộp code được cho tới khi vá xong lỗ hổng."
DỪNG. Không nhảy sang Bước 2.

### Bước 2: Xác Định Nguồn Cội (Base Branch)
```bash
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null
```
Hoặc hỏi CEO để chắc ăn: "Có phải nhánh này chẻ ra từ `main` không sếp?"

### Bước 3: Dâng Tấu Cố Định (Present Options)
Luôn luôn rập khuôn đưa ra đúng 4 Lựa Chọn này, CẤM thêm thắt lời bình:
```
Nhiệm vụ đã hoàn tất xanh mượt. Xin CEO chỉ đạo phương thức Góp Nhánh:

1. Gộp trực tiếp vào <base-branch> ở Local.
2. Push lên Github và tạo Pull Request (PR).
3. Giữ nguyên nhánh này chưa làm gì cả (Lưu trạng thái chờ duyệt sau).
4. Khai tử toàn bộ công sức này (Discard work).

Sếp chọn số mấy?
```
**KHÔNG CHÈN THÊM Tán Gẫu** - Càng lạnh lùng càng thượng tôn pháp luật.

### Bước 4: Khâm Thử (Execute Choice)
**Option 1: Gộp Local**
Checkout base branch -> pull latest -> git merge <nhánh feature> -> Chạy lại test kết quả -> Test xanh thì `git branch -d <nhánh feature>`. Sang Bước 5.

**Option 2: Push & Bắn PR**
Push branch lên origin -> `gh pr create` -> Điền Summary + Test Plan bằng chuẩn markdown. Sang Bước 5.

**Option 3: Treo đó chờ**
Báo cáo: "Đã lưu trữ thành quả tại nhánh <name>". Dừng. KHÔNG xóa worktree.

**Option 4: Khai tử (Discard)**
Hỏi xác nhận chốt trạm thu phí tâm lý: "XÓA SẠCH SẼ ĐÓ NHA SẾP? Xác nhận gõ 'discard'".
Đợi đúng lệnh `discard` rồi mới chạy `git branch -D`.

### Bước 5: Đốt Rác (Cleanup Worktree)
Nếu CEO nãy chốt Option 1, 2, 4 mà bạn đang ở cơ chế `git worktree`:
Quét list: `git worktree list | grep ...`
Có thì chặt đứt: `git worktree remove ...`

## Cờ Đỏ Chết người
**Tuyệt Đối Cấm Trong Lịch Sử ABM:**
- Dám mồm trình phương án Merge khi Test chưa xanh màn.
- Tự thêm Option linh tinh (Hỏi mẹo "Sướng ý sếp không").
- Xóa code mồ hôi nước mắt mà không hỏi bằng chữ `discard`.
- Dám gõ lệnh Force-Push mà sếp đéo dặn.
