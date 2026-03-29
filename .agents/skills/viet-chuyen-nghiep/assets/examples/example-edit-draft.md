# Ví dụ: Sửa Bản thảo (Trước/Sau)

## Tóm tắt brief

```yaml
task_type: edit-draft
input: "Bài blog 600 từ về 'Lợi ích của đọc sách' — tone quá AI"
goal: "Rewrite tự nhiên, giữ ý chính, fix anti-AI"
```

---

## Trước khi sửa (Draft gốc — AI score 78/100 🔴)

> Trong thế giới ngày nay, việc đọc sách đóng vai trò vô cùng quan trọng
> trong việc phát triển bản thân. Hơn nữa, đọc sách không chỉ giúp chúng ta
> mở rộng kiến thức mà còn giúp chúng ta phát triển tư duy phản biện.
> Ngoài ra, đọc sách còn mang lại nhiều lợi ích sức khỏe tinh thần.
> Tóm lại, đọc sách là một thói quen tuyệt vời mà ai cũng nên rèn luyện.

**AI smell detected:**
- ❌ "Trong thế giới ngày nay" — sáo mở bài
- ❌ "Hơn nữa" + "Ngoài ra" — connector robot
- ❌ "vô cùng quan trọng" — filler adjective
- ❌ "Tóm lại" — kết sáo
- ❌ "giúp chúng ta" × 2 — lặp chủ ngữ

---

## Sau khi sửa (Đã edit — AI score 22/100 ✅)

> Năm ngoái, mình đọc được 24 cuốn — nhiều gấp đôi năm trước. Mình
> không giỏi hơn, chỉ là tìm đúng cách: đọc 20 phút trước ngủ thay
> vì force ngồi 2 tiếng cuối tuần.
>
> Điều thú vị: sau 6 tháng, mình thấy khả năng lập luận trong meetings
> tốt hơn hẳn. Không phải vì nhớ nội dung sách, mà vì não quen phân
> tích nhiều góc nhìn. Đọc tiểu thuyết trinh thám cũng train tư duy —
> chỉ là ít ai nghĩ vậy.
>
> Bonus: ngủ nhanh hơn. Màn hình tắt, đèn đọc bật, 20 phút là mắt mờ.
> Rẻ hơn melatonin nhiều.

**Đã thay đổi:**
- Mở bài bằng personal data (24 cuốn) thay vì sáo rỗng
- Bỏ connector — dùng line break + thought flow
- Thêm cụ thể: "20 phút trước ngủ", "6 tháng", "trinh thám"
- Kết bằng humor micro ("rẻ hơn melatonin")

---

## Số liệu chất lượng

```yaml
anti_ai_score: "78 → 22" ✅
word_count: "600 → 580" ✅ (trimmed filler)
meaning_preserved: true ✅ (3/3 key points giữ nguyên)
```
