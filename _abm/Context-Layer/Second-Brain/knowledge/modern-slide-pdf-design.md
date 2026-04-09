# 🎨 Modern Slide & PDF Design Guidelines (2026 Edition)

Tài liệu này là chuẩn mực thiết kế hình ảnh cho ABM Workforce. Bất kỳ AI Agent nào (đặc biệt là Skywork PPT và Skywork Doc) khi được giao nhiệm vụ xuất bản file trình chiếu (Slide) hoặc tài liệu (PDF) đều **BẮT BUỘC** phải tuân thủ và tham chiếu các tiêu chuẩn dưới đây để đảm bảo Output chuẩn quốc tế.

---

## 1. 📊 Tiêu Chuẩn Thiết Kế Slide (Presentation)

Thay vì thiết kế theo kiểu truyền thống nhồi nhét chữ, Slide hiện đại năm 2026 tập trung vào trải nghiệm "Liquid Layouts" và thị giác.

### 1.1. Nguyên Tắc "1 Slide = 1 Idea"
- Tuyệt đối không dồn ép 2-3 ý tưởng phức tạp vào 1 trang duy nhất. Nếu nội dung quá dài, hãy cắt qua trang mới.
- Người xem phải hiểu được thông điệp của Slide trong vòng **3 giây** đầu tiên nhìn lướt qua.

### 1.2. Quy Tắc Vàng 6x6 (6 by 6 Rule)
- Một slide không có quá **6 dòng văn bản**.
- Một dòng không có quá **6 từ**.
- Không bắt khán giả đọc chữ thay vì nghe thuyết trình. Chữ trên Slide chỉ là mỏ neo (Anchor) cho lời nói.

### 1.3. Khoảng Trắng Phục Vụ Thị Giác (Whitespace)
- Luôn giữ vùng Margins (lề) rộng. Whitespace là "oxi" cho Slide, giúp các ý chính thở được.
- Không phóng to hình ảnh hay bảng biểu chạm viền (trừ khi là ảnh tràn lề làm Background).

### 1.4. Kể Chuyện bằng Dữ Liệu (Narrative Data Storytelling)
- Đừng để một cái biểu đồ trống trơn. Hãy thêm các mũi tên (Annotations), Textbox Highlight màu đỏ/xanh để chỉ ra "Tại sao số này lại tăng/giảm".
- Xóa bỏ lưới (Grid lines) và trục không cần thiết trên biểu đồ để làm sạch mắt.

### 1.5. Thẩm Mỹ Hậu Tối Giản (Post-Minimalism)
- Sử dụng hiệu ứng **Glassmorphism 2.0** (kính mờ) khi tạo Box chứa Text.
- Asymmetrical Grids: Layout bất đối xứng (như Bento Grid) sẽ giúp slide bớt nhàm chán hơn chia đôi màn hình cơ bản.

---

## 2. 📄 Tiêu Chuẩn Trình Bày PDF & Document

PDF và Báo Cáo Document không phải là chỗ nhồi chữ loạn xạ, nó cần một cấu trúc cực rõ (Hierarchy).

### 2.1. Cấu Trúc Đọc Thân Thiện (Logical Structure)
- **H1 (Tiêu đề chính):** Chỉ có 1 cái duy nhất cho 1 Chương/Phần.
- **H2 & H3:** Phân cấp rõ ràng. Không dùng chữ In Đậm (Bold) thông thường thay cho H2. Điều này giúp tính năng Screen Reader và Outline (Mục lục PDF) hoạt động chuẩn xác.
- Tạo một bảng **Mục Lục (Table of Contents)** ở đầu nếu file dài hơn 5 trang.

### 2.2. Font Chữ & Trợ Năng (Accessibility)
- Sử dụng font Sans-serif (như Inter, Roboto, Helvetica) cho phần thân bài.
- Kích thước Body text tối thiểu là **12pt**. Chú thích (Footnote) là **10pt**.
- Tuyệt đối giữ **High Contrast** (Độ Tương Phản Cao): Chữ xám đậm/đen trên nền trắng. Không viết chữ vàng trên nền trắng.

### 2.3. Hỗ Trợ Đa Thiết Bị (Mobile-Ready)
- Document hiện nay được đọc trên điện thoại rất nhiều. Không sử dụng cấu trúc "Text 2 cột" (Two-column format) trừ phi đó là báo cáo khoa học đặc thù. Cấu trúc 1 cột lớn giúp user cuộn tài liệu mượt mà.

### 2.4. Tính Tương Tác (Interactivity)
- Các liên kết (Hyperlinks) phải được in đậm hoặc tô màu xanh/gạch chân để biết là có thể click được.

---

> **LỜI NHẮC GỬI AI AGENTS:** Trước khi truyền câu lệnh (Prompt) cho nền tảng Skywork (Skywork PPT / Skywork Doc), hãy **nhúng** các gạch đầu dòng này vào trong Prompt Input để bắt Skywork Model tuân thủ đúng định dạng thịnh hành nhất của năm nay.
