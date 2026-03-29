# Pipeline: Sửa Bản Nháp (edit-draft) — v3.0

## Khi nào kích hoạt
- User gửi bài viết đã có → muốn sửa, cải thiện, viết lại

## Pipeline

```
content/ (light) → style/ → quality/ → Output
     │                │         │
     │                │         └─ PASS/REVISE/REJECT
     │                └─ Biên tập phong cách
     └─ Đọc nhanh brief + bài gốc
```

## Bước chi tiết

### 1. Ban Thu Thập (content/) — CHẾ ĐỘ NHẸ
1. `lead-content.md` đọc bài gốc + yêu cầu sửa
2. `analysis.md` đánh giá: điểm yếu chính, tone hiện tại, audience
3. KHÔNG cần research sâu (bài đã có sẵn)
4. Output: **Bản đánh giá bài gốc** + yêu cầu sửa cụ thể

### 2. Ban Biên Tập (style/)
1. `lead-style.md` nhận bài gốc + đánh giá → phân công BTV
2. Tập trung vào điểm yếu đã phát hiện
3. Output: **Bản thảo đã chỉnh sửa** → chuyển quality/

### 3. Ban Kiểm Duyệt (quality/)
1. Chạy 6 kiểm tra → so sánh trước/sau
2. Quyết định: PASS → trả user | REVISE → trả style/
3. Output: **Bài đã sửa + báo cáo trước/sau**

## Lưu ý
- **Tôn trọng giọng gốc** trừ khi user nói rõ "viết lại hoàn toàn"
- Ghi rõ thay đổi: "Đã sửa X → Y, lý do: Z"
