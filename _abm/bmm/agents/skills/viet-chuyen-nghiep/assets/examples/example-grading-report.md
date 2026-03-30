# Ví dụ: Báo cáo Chấm điểm

## Tóm tắt brief

```yaml
task_type: grade-content
content: "Bài blog về 'Lợi ích của Thiền' — 800 từ"
rubric: rubric-100
```

---

## Output

### 📊 Bảng điểm: "5 Lợi ích Khoa Học Của Thiền Định"

| Tiêu chí | Điểm | Trọng số | Weighted | Nhận xét |
|----------|-------|----------|----------|----------|
| Accuracy | 62 | 25% | 15.5 | 2/5 claims thiếu source. Claim "thiền giảm 40% stress" không có citation |
| Structure | 78 | 20% | 15.6 | Listicle rõ ràng nhưng thiếu intro context + conclusion |
| Clarity | 85 | 20% | 17.0 | Dễ hiểu, ngôn ngữ phù hợp audience. P3 hơi jargon ("cortisol") |
| Persuasion | 55 | 15% | 8.25 | Arguments yếu — list benefits mà không convince WHY |
| Style | 40 | 10% | 4.0 | Rõ mùi AI: "Trong thế giới bận rộn ngày nay", "Hơn nữa" x4 |
| Value | 70 | 10% | 7.0 | Actionable ở mức trung bình — có tips nhưng quá generic |

**Total: 67.35 → 67/100 🟡 KHÁ**

---

### Điểm mạnh ✅

1. **Cấu trúc rõ ràng** — 5 lợi ích, mỗi lợi ích 1 section, dễ scan
2. **Ngôn ngữ accessible** — phù hợp audience phổ thông
3. **Có call-to-action cuối** — khuyến khích thử thiền

### Điểm yếu ⚠️

1. **Evidence yếu** — "40% stress reduction" claim không có source.
   "Theo nghiên cứu" — nghiên cứu nào? Năm nào? Sample size?
2. **Mùi AI rõ** — mở bài sáo (P1), transition words lặp (P2-5),
   kết bài khuôn (P6)
3. **Thiếu depth** — mỗi benefit chỉ 2-3 câu, quá surface

### Đề xuất cải thiện 🔧

1. **Accuracy**: Thêm citation cho mọi claim số liệu. Gợi ý: Harvard
   Medical School study on meditation (2023), hoặc Mayo Clinic resources
2. **Style**: Viết lại P1 (mở bài) và P6 (kết bài). Bỏ "Hơn nữa" —
   dùng cách nối tự nhiên hoặc bỏ connector
3. **Depth**: Mỗi benefit thêm 1 ví dụ thực tế hoặc micro case study

### Verdict

**Đọc được, nhưng cần fix evidence + rewrite style trước khi publish.**
Priority: Accuracy fix → Anti-AI rewrite → Depth enhancement.

---

## Số liệu chất lượng

```yaml
rubric_total: 67/100 🟡 Khá
anti_ai_score: 72/100 🟠 (chính bài viết có AI score cao)
critique_depth: detailed ✅
```
