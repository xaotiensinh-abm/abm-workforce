---
name: brainstorming
description: Khám phá, làm rõ yêu cầu và lên bản thiết kế (design/spec) cho mọi task sáng tạo, code tính năng mới, hoặc thay đổi hệ thống. Bắt buộc phải có file thiết kế được duyệt trước implementation.
---

# Brainstorming Ideas Into Designs / Kích Tố Ý Tưởng Thành Thiết Kế

Đóng vai trò định hình yêu cầu và biến đổi ý tưởng thành các bản thiết kế hoàn chỉnh (design/spec) thông qua vòng lặp cộng tác giao tiếp với người dùng.

Khởi động bằng việc thấu hiểu ngữ cảnh dự án tĩnh, sau đó đặt câu hỏi từng câu một để tinh chỉnh ý tưởng. Khi nắm rõ việc cần xây dựng, trình bày bản thiết kế kiến trúc/tiếp cận cho người dùng duyệt.

Auto-activate triggers (VN): "brainstorm", "thảo luận thiết kế", "lên ý tưởng", "đưa ra giải pháp", "cùng suy nghĩ", "tạo spec", "design feature"
Auto-activate triggers (EN): "brainstorm ideas", "design this feature", "let's think about", "create spec", "discuss approach"

<HARD-GATE>
TUYỆT ĐỐI KHÔNG GỌI (invoke) bất kỳ skill cấp độ code/implementation nào, không tạo structure project hay viết mã thực tế cho tới khi bạn đã trình bày Thiết kế và Người dùng CHẤP THUẬN nó. Điều này áp dụng cho MỌI project, bất chấp cảm giác "tác vụ này quá đơn giản".
</HARD-GATE>

## Anti-Pattern: "Việc Này Quá Đơn Giản, Chẳng Cần Design"

Mọi project đều phải kinh qua quá trình này. Một todo list, một utility function đơn giản, thay đổi config — tất cả. Những project được gán mác "đơn giản" thường là nguyên nhân gây ra lãng phí công sức lớn nhất vì những giả định thiếu kiểm chứng. Design có thể rất ngắn (chỉ vài dòng), nhưng BẮT BUỘC phải trình bày và chờ duyệt.

## Checklist Yêu Cầu

Thực hiện các bước theo đúng trình tự sau (và dùng task checklist để track):

1. **Khám phá Project Context** — đọc file README, codebase, recent commits để nắm ngữ cảnh.
2. **Cung cấp Visual Companion (tùy chọn)** — nếu thảo luận liên quan đến hình ảnh/UI, offer tính năng này ở 1 tin nhắn RIÊNG BIỆT.
3. **Brainstorm Query (Hỏi làm rõ)** — hỏi từng câu một, xác định Purpose, Constraints, Success criteria.
4. **Đề xuất 2-3 Phương pháp (Approaches)** — đưa ra lựa chọn, trade-offs của chúng và đề xuất/khuyến nghị (recommendation) của bạn.
5. **Trình bày Thiết kế (Present design)** — Trình bày các phần của design (chia theo độ phức tạp), sau đó xin người dùng duyệt.
6. **Viết Design Doc (Spec)** — Tái hiện lại spec và lưu dưới dạng `docs/specs/YYYY-MM-DD-<topic>-design.md` và commit (với project mới / không có style ưu tiên).
7. **Spec Review Loop** — Kiểm duyệt chéo; sửa lỗi trong bản thảo thiết kế (giới hạn tối đa 3 vòng thử).
8. **User Reviews Specification** — Yêu cầu người dùng review file Markdown cuối cùng.
9. **Chuyển giao (Transition)** — Gọi skill `writing-plans` để tạo the implementation plan.

## The Process (Quy trình chi tiết)

**1. Thấu hiểu ý tưởng (Understanding):**

- Kiểm tra file code hiện tại.
- Trước khi hỏi chi tiết, đánh giá Scope: Nếu request gồm nhiều subsystem lớn (chat, file storage, billing...), hãm đà lại ngay. Chia nhỏ project thành sub-projects. Đừng đi vào tiểu tiết khi bức tranh toàn cảnh chưa được xác định.
- Mỗi sub-project sẽ có chu trình spec → plan → implementation riêng biệt.
- Nếu là tính năng tầm trung, hỏi TỪNG CÂU MỘT. 
- Ưu tiên câu hỏi Trắc nghiệm (Multiple choice) hơn Tự luận. Tập trung vào: mục đích, rào cản và tiêu chí thành công.

**2. Khám phá Phương pháp (Exploring approaches):**

- Đề xuất ít nhất 2 hoặc 3 lựa chọn tiếp cận kèm ưu nhược điểm (trade-offs).
- Giải thích vì sao bạn lại Recommend hướng A thay vì B.

**3. Trình bày Design:**

- Khi đã hiểu, bắt đầu miêu tả hình thù thiết kế. Đi qua Data Flow, Architecture, Error Handling, Testing methodology, Components.
- Sau khi trình bày 1 block kiến trúc quan trọng, dừng lại hỏi user "Bạn thấy phần này ổn chứ?". Lắng nghe feedback và hiệu chỉnh (revise) linh hoạt.

**4. Thiết kế ranh giới hệ thống (Design isolation):**

- Modularize ý tưởng. Mỗi phần có 1 logic rõ ràng và Interface giao tiếp chuẩn. Nó giúp việc viết tính toán dễ hiểu và test biệt lập.
- Nằm lòng câu hỏi: Module này có bị ảnh hưởng bởi bên thứ ba không? Nếu thay đổi nội hàm thì Module khác có hỏng không? Nếu có, boundary đang được thiết kế sai.

**5. Hoạt động với code Legacy:**

- Khảo sát các Component có sẵn và "Bắt chước" pattern của system đó.
- Không lôi refactor vào giữa chừng trừ khi nó block trực tiếp task hiện tại. Giữ focus cao độ vào mục tiêu.

## Sau khi Thiết kế xong (After the Design)

Viết document lưu trữ xuống đĩa cứng (Ví dụ: `docs/specs/YYYY-MM-DD-<topic>.md`), và mời User duyệt lại Document thực tế.

> "Toàn bộ file Thiết kế đã được viết và lưu tại `<path>`. Vui lòng xem qua và cho tôi biết nếu có phần nào cần điều chỉnh trước khi chúng ta chuyển sang bước viết Implementation Plan."

Nếu User đồng ý -> Gọi `writing-plans` để bước sang Plan phase. KHÔNG gọi bất kì dev skill nào khác tại bước này.

## Nguyên Tắc Khắc Cốt Ghi Tâm

- **Mỗi lần hỏi 1 ý chính (One question at a time)** - Không làm người dùng choáng ngợp.
- **Ưu tiên trắc nghiệm (Multiple choice preferred)** - Giúp trả lời nhanh hơn.
- **YAGNI (You aren't gonna need it) RUTHLESSLY** - Mạnh tay cắt bỏ feature vô bổ, rườm rà.
- **Explore alternatives (Đa lựa chọn)** - Không ốp mặc định một lựa chọn duy nhất.
- **Vòng tuần hoàn linh hoạt (Be flexible)** - Sẵn sàng bẻ lái kịch bản dựa trên feedback.
