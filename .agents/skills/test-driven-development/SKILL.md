---
name: test-driven-development
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: "Dùng trong khi code Tính Năng hay Fix Bug, CẤM gõ production code trước khi có file test bắt lỗi."
---

# Lập Trình Thử Dòng (Test-Driven Development - TDD)

## Tổng Quan

Viết Test chặn họng trước. Chạy và dán mắt xem nó hiện màu Đỏ (Fail). Cuối cùng viết dòng code bé tẹo để bóp nó thành Xanh (Pass).

**Tôn Chỉ:** Nếu bạn chưa bao giờ thấy Test File tạch một cách quang minh chính đại, bạn đéo bao giờ chắc là file Test của bạn chạy đúng cái cần đo.

## Kỷ Luật Thép ABM (The Iron Law)

```
KHÔNG CÓ DÒNG PRODUCTION CODE NÀO ĐƯỢC CHỨA CHẤP NẾU CHƯA CÓ FILE TEST ĐANG BÁO FAIL.
```

- Nhỡ tay gõ Môi trường chạy chính (Production Code) trước rồi mới nhớ đẻ file Test? **XÓA SẠCH SẼ ĐOẠN ĐÓ. KHÔNG BAO GIỜ CHO PHÉP CHỤP LẠI SCREENSHOT "LÀM MẪU DÀNH BẠN" RỒI VIẾT TEST RỒI "HIỆN THỰC HÓA" LẠI. RÁC RƯỞI!** Bắt đầu code lại!

> **Sơ đồ Tư Duy Red-Green:** Kèm tại `references/tdd-flowchart.md`.

## Vòng Luân Hồi (Red-Green-Refactor)

### BƯỚC 1: RED - Vạch mặt Lỗi
Sáng tạo một Case test cực cắn (One minimal test), ném tả thực yêu cầu. Gọi tên function, tên case súc tích. Đừng đẻ test theo kiểu "X_is_true".
- Yêu cầu: Đâm thẳng code (Hạn chế Mocking lung tung rác dính).

### BƯỚC 2: Tận Hưởng Nó Thất Bại (Verify RED)
BẤM CHẠY LỆNH TEST NGAY. (`npm test ...`, `pytest ...`).
- Phải đảm bảo Mầu Đỏ đập vô mắt màn hình (Báo FAIL vì chưa implement hàm, Error 404...vv).
- Báo FAIL vì Syntax Error chữ HOA/thường là Lỗi Gõ Máy chứ đéo do TDD.
- Chạy phát XANH luôn: Suy ra Code cũ đã ôm feature này. Đổi kịch bản Test ngay lập tức!

### BƯỚC 3: GREEN - Kê Đơn Thuốc Độc Đắc
Chạy Code chống vã. ĐÚNG BÀI TOÁN LÀ QUA ẢI. Đéo Cần Mở Rộng Linh Tinh. Thượng đế (YAGNI) dạy phải làm code siêu bé là vậy.

### BƯỚC 4: Nghiệm Thu Kê Đơn (Verify GREEN)
CHẠY LẠI TEST. Mầu xanh lá mát mẻ! 
Đỏ các Test khác? Mò lại và fix cái tính đập phá vừa làm đi.

### BƯỚC 5: Tẩy Trần (Refactor Cleanup)
Test Xanh? Mở cửa thiên đàng cho việc: Dọn bớt Comment rác rưởi, Gộp code DRY, Rã method dài, Chuốt tên Function... Test mầu Xanh giữ lưng an toàn rồi!

## Biện Minh Cho Tội Lỗi TDD
Con người sợ TDD, và AI cũng ngáo ngơ trước nó:
| Lời thốt ra | Nghiệp chướng nhận lại |
|--------|---------|
| "Thêm Code tí tẹo chắc qua test" | Simple code = Fail vô hình cực gắt. Tốn 30s cào TDD lại ra. |
| "Thôi tao code Feature rồi mai mốt bù Unit Test sau" | Test Xanh dờn vì Code viết sẵn. Nhưng éo chặn được Side Effects rỉ mủ. |
| "Tao manual check tay thấy sống ngon rồi" | Bug không nằm ở lúc check tay, Bug nằm ở Thằng thứ Hai mò tới nó 3 tháng sau. |
| "TDD tốn não mệt quá" | TDD giúp khoanh mẹ Bug trên màn đen hôi thúi rồi đằng nào cũng FIX nhàn vkl, mệt đíu gì! |
| "Đéo có test Framework chỗ repo này" | Ngụy biện dốt, AI phải biết tự Gen 1 con Bash Script con con chạy Verify thay thế. |

## Thất Bại Khởi Đầu (Red Flags System)
AI dính án LƯƠN LẸO hão huyền với CEO:
- Viết Test khi Tưởng mình Done (Sĩ diện nhét cho kín KPI).
- Chạy Test thấy Đỏ loét xong đếch hiểu Cớ sự Gốc rễ, tự nhủ "Thôi test ngu xóa test code production chắc dính".
- Đi xin Code Mẫu, nhét đống comment "// code logic như vầy nè" để nhớ hờ hờ -> Vi phạm Iron Law. Phải xóa hết.

**Tất cả mấy Cờ Đỏ = RESTART TỪ VẠCH XUẤT PHÁT!** Lôi cổ kỹ thuật này ra dùng. Code chay trần truồng là tự sát.
