---
name: systematic-debugging
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: "Dùng BẮT BUỘC mỗi khi đụng độ BẤT KỲ một con Bug, Test fail hay hành vi dị thường nào, TRƯỚC KHI định đề xuất cách fix."
---

# Truy Vết Bắt Bug (Systematic Debugging)

## Tổng Quan

Đoán mò rồi Fix ngẫu nhiên chỉ đẻ ra Bug nhánh. Chắp vá qua loa là biểu hiện chối bỏ trách nhiệm.

**Lõi nguyên tắc:** LUÔN LUÔN tìm ra Gốc Rễ (Root Cause) trước khi gõ phím. Chữa bệnh từ ngọn là bản án khai trừ.

## Kỷ Luật Thép Của ABM (The Iron Law)

```
KHÔNG FIX RÁC NẾU TRƯỚC ĐÓ CHƯA CÓ BÁO CÁO PHÂN TÍCH ROOT CAUSE RÕ RÀNG
```
Chưa làm xong Phase 1 thì câm nín, cấm xin sửa code.

## Không Có Ngoại Lệ
Cứ đụng tới Lỗi Production, Lỗi Build C#, Lỗi Node CLI, hay Đỏ một dòng Test case. Lấy skill này ra dùng.
Và ĐỪNG có viện cớ "Sếp hối quá fix lẹ đi". Vội vàng là đẻ rác. Systematic luốn nhanh hơn Đập-Phá-Chữa.

## Bốn Cột Mốc Bắt Bug (The Four Phases)

Bắt buộc tuân thủ không được nhảy cóc:

### Kỷ Nguyên 1: Săn Đuổi Gốc Rễ (Root Cause Investigation)
**TRƯỚC KHI đề xuất đổi 1 Dấu Phẩy:**
1. **Dán mắt vào Error Message:** Đọc kỹ từng chữ của Stack Trace. Đừng skip đoạn giữa dài ngoằng. Ghi nhận số Line, File path.
2. **Khơi lại hiện trường:** Liệu Bug có tái hiện liên tục không? Các bước tái hiện? Cần nhiều data hơn để soi.
3. **Môi trường & Vết cắt:** Gần đây ai Push lên (check git Commit log). Dependency nào vừa bump version.
4. **Cài cắm Camera (Trường phái mổ tim System Layer):** 
   - Đôi khi data đi từ FE -> Logic -> DB chết ở khúc giữa.
   - Thêm câu `console.log` / `print` / `logger` ở CỔNG VÀO và CỔNG RA của từng cụm Component.
   - Khởi chạy lấy Log. Đau chỗ nào, đào đúng 1 chỗ đó. Không càn quét linh tinh.
5. **Trace Data Backward:** Dò ngược lên thượng nguồn. Đứa nào truyền vào cái biến độc hại này?

### Kỷ Nguyên 2: Soi Pattern (Pattern Analysis)
1. **Ví dụ đang sống:** Có hàm nào trong codebase đang chạy chung logic này mà Mượt không?
2. So sánh và Tìm Dị Biệt. Tại sao thằng A sống mà thằng B lại ném NotFound Exception? Danh sách ra khác biệt đó.


### Kỷ Nguyên 3: Đặt Cược Một Cửa (Hypothesis & Testing)
1. **Đúc Kết Giả Thuyết:** "Nguyên nhân gốc rễ là X, vì ở vòng đời Rendering, nó gọi hàm Y mà chưa Wait Z".
2. **Test Tiêm Yếu Định (Minimal):** Bơm một dòng mã nhỏ nhất (Tweak 1 biến, hoặc mock đon giản) để kiểm chứng giả thuyết. MỘT BIẾN DUY NHẤT. Cấm gộp chung Fix giao diện với Fix bug async mâm xôi.
3. Không thành công? Sáng tạo giả thuyết số 2. 

### Kỷ Nguyên 4: Xuống Dao Thực Sự (Implementation)
1. Mở Cổng TDD (`test-driven-development`) để đúc 1 file Test chặn họng con Bug này. Test đang chạy ĐỎ chót.
2. Fix nhẹ nhàng vào tận Mạch máu con Root Cause đã bắt mạch.
3. Chạy lệnh. Kiểm chứng Xanh dờn với `verification-before-completion`.

> **LUẬT SỐ 5 ĐẶC BIỆT:**
> **Thiến 3 Lần Không Lành Lặn -> Khóa Hệ Thống:**
> Nếu đã đổi 3 lần mã Fix khác nhau mà Đỏ vẫn hoàn Đỏ, hoặc Lỗi từ File A lại leo sang File B. ĐỪNG cố đi code Fix 4.
> GIỮ NGUYÊN HIỆN TRƯỜNG. Đây là lỗi **Architecture Flaws (Sai Kiến Trúc Nền Tảng)**. Trình báo CEO. Phanh ngay lại.

## Cờ Đỏ Chết Nhát
Khi lười biếng AI thường lẩm bẩm trong ruột các câu:
- "Quick fix cái đã, chạy rồi truy sát sau" (Ngu muội).
- "Cứ quăng cái Fix thử vô coi hên xui pass thì tốt" (Bố Láo).
- "Đừng test, tao nhìn bằng mắt tao biết nó chạy được" (Kiêu ngạo).
- "Còn có 1 Bug lôi nốt hàm này ra là xong... ugh, thêm 2 bug mới"

Gặp mấy suy nghĩ này -> **DỪNG LẠI**, Gọi thẳng về ROOT CAUSE INVESTIGATION.
