# 📑 SOP: QUY TRÌNH NÂNG CẤP VÀ CHUẨN HÓA DISTRACTOR (PHƯƠNG ÁN SAI)

Tài liệu này đóng gói quy trình chuẩn để thiết kế hoặc tự động hóa việc viết lại các phương án sai (distractors) trong bộ câu hỏi trắc nghiệm kỹ năng, nhằm loại bỏ mẹo làm bài và tăng độ khó tâm lý.

---

## 🎯 1. Mục tiêu Cốt lõi
1. **Cân bằng thị giác (Length Bias Elimination):** Độ dài của cả 4 đáp án (A, B, C, D) phải tương đương nhau, dao động trong khoảng hẹp (VD: 15 - 25 từ). Tuyệt đối không để đáp án đúng dài và chi tiết đặc biệt hơn hẳn đáp án sai.
2. **Bẫy tâm lý (Deceptive Options):** Phương án sai không được sai một cách "ngây ngô" hay hiển nhiên. Chúng phải nghe vô cùng hợp lý, phản ánh đúng những lầm tưởng phổ biến, các phản xạ vô điều kiện hoặc các lý lẽ sai lệch trên mạng.
3. **Giữ nguyên tính toàn vẹn:** Không làm thay đổi bản chất kịch bản tình huống (Scenario) và phải giữ nguyên vị trí của đáp án đúng (Key).

---

## 🧠 2. Công thức tạo bẫy tâm lý (Psychological Traps)
Khi xây dựng các phương án sai cho câu hỏi Tình huống (Level 2 & Level 3), sử dụng 4 loại bẫy chính:

*   **Bẫy "Phản xạ tự nhiên nhưng sai kỹ năng":**
    *   *Ví dụ:* Khóc lóc van xin tha thứ, ngồi gục xuống im lặng chịu trận, đánh trả một cách mù quáng bằng bạo lực.
*   **Bẫy "Giải pháp mạng xã hội":**
    *   *Ví dụ:* Ghi hình tung lên mạng để "cộng đồng mạng" xử lý, nhờ bạn bè hack tài khoản, bóc phốt trên Facebook.
*   **Bẫy "Thỏa hiệp / Giữ thể diện":**
    *   *Ví dụ:* Lịch sự im lặng cho qua chuyện để không làm mất mặt người lớn, ngoan ngoãn làm theo hướng dẫn vì giữ thể diện cho gia đình.
*   **Bẫy "Niềm tin ngây thơ":**
    *   *Ví dụ:* Cho rằng nhận quà đắt tiền thì phải có nghĩa vụ đáp lại, tin rằng người lớn tuổi luôn luôn nói sự thật, tin rằng đã gửi 1 ảnh rồi thì gửi thêm họ sẽ tha.

---

## 🤖 3. Prompt Template mẫu cho AI

```text
Bạn là một chuyên gia giáo dục và tâm lý học hành vi. Nhiệm vụ của bạn là nâng cấp bộ câu hỏi trắc nghiệm tình huống sau đây.

YÊU CẦU BẮT BUỘC:
1. GIỮ NGUYÊN: Kịch bản tình huống (Scenario) và vị trí đáp án đúng (A, B, C, D).
2. ĐỘ DÀI: Viết lại toàn bộ 4 phương án (A, B, C, D) sao cho độ dài của chúng CỰC KỲ ĐỒNG ĐỀU (giới hạn 15-25 từ mỗi phương án). Đáp án đúng KHÔNG được dài gồ ghề nổi bật hơn đáp án sai.
3. BẪY TÂM LÝ: 3 phương án sai (distractors) phải mang tính "hợp lý giả tạo". Hãy biến chúng thành:
   - Các giải pháp bốc đồng (bạo lực, trả thù mạng).
   - Các hành vi thỏa hiệp, giữ thể diện sai lầm.
   - Các phản xạ tự nhiên nhưng gây nguy hiểm (đứng im, van xin).
   - Những niềm tin sai lệch phổ biến của học sinh lứa tuổi này.
4. VĂN PHONG: Xưng "em" hoặc "bạn", giọng văn nghiêm túc, thuyết phục và diễn đạt logic, khiến lứa tuổi mục tiêu dễ dàng tin đó là cách làm đúng.

Dưới đây là các câu hỏi cần xử lý:
[DÁN DANH SÁCH CÂU HỎI VÀO ĐÂY]
```

---

## 🚀 4. Quy trình Thực hiện (Validation Checklist)

Sau khi AI (hoặc tác giả) sinh ra đáp án mới, hãy dùng checklist này để rà soát:
- [ ] Bốn đáp án (A, B, C, D) có số dòng và số lượng chữ xấp xỉ nhau không?
- [ ] Đọc lướt qua xem có đáp án nào trông "dài bất thường" hay "ngắn bất thường" không?
- [ ] Các phương án sai đọc lên nghe có vẻ "rất có lý" đối với tâm sinh lý lứa tuổi đó không?
- [ ] Chữ "KHÔNG" / "CÓ" ở đầu mệnh đề có bị lặp lại quá máy móc không? (Nên thay bằng các từ ngữ mềm dẻo hơn)
- [ ] Đáp án đúng (✅) có bị thay đổi ý nghĩa hay sai lệch so với kỹ năng cốt lõi không?

---
*Lưu ý: Quy trình này hoạt động tốt nhất cho cấu trúc câu hỏi phân loại (Level Khó và Rất Khó).*
