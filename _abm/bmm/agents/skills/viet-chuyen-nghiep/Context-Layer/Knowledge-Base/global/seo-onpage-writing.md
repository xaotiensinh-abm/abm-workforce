# SEO On-Page cho Bài Viết Tiếng Việt

## Heading Hierarchy — Cấu trúc Tiêu đề

### Quy tắc bắt buộc
- **H1:** Duy nhất 1 cái/trang, chứa keyword chính
- **H2:** Các section lớn, chứa keyword phụ
- **H3:** Chi tiết trong section, chứa long-tail keyword
- **Không bao giờ** nhảy cấp: H1 → H3 (bỏ H2)

### Ví dụ đúng
```
H1: Hướng Dẫn Marketing AI cho Doanh Nghiệp Việt Nam 2026
  H2: Marketing AI là gì?
    H3: Định nghĩa và Phân loại
    H3: Sự khác biệt với Marketing Truyền thống
  H2: 5 Công cụ Marketing AI Tốt Nhất
    H3: Gemini — Trợ lý Viết Content
    H3: NotebookLM — Nghiên cứu Thị trường
  H2: Cách Triển Khai Marketing AI Từng Bước
```

---

## Keyword Placement — Vị trí Từ khóa

| Vị trí | Mức quan trọng | Lưu ý |
|--------|---------------|-------|
| **Title tag (H1)** | ★★★★★ | Keyword ở đầu, ≤60 ký tự |
| **Meta description** | ★★★★☆ | Keyword tự nhiên, ≤155 ký tự |
| **URL slug** | ★★★★☆ | Không dấu, gạch nối: `marketing-ai-viet-nam` |
| **Đoạn mở đầu (100 từ đầu)** | ★★★★☆ | Keyword trong 2 câu đầu |
| **H2, H3** | ★★★☆☆ | Keyword phụ, long-tail |
| **Alt text ảnh** | ★★★☆☆ | Mô tả ảnh + keyword |
| **Anchor text internal link** | ★★☆☆☆ | Đa dạng, không spam |

### Mật độ Keyword
- Tối ưu: **1-2%** (1-2 lần/100 từ)
- >3%: Quá dày → penalize
- Dùng **LSI keywords** (từ đồng nghĩa, liên quan) thay vì lặp

---

## Meta Title & Description — Tiếng Việt có Dấu

### Meta Title
```
Công thức: [Keyword chính] + [Lợi ích/Số] + [Brand] (tùy chọn)
Ví dụ: "Marketing AI cho Doanh Nghiệp: 5 Công Cụ Hiệu Quả Nhất 2026"
Ký tự: 50-60 (có dấu tiếng Việt = ít ký tự hơn Anh)
```

### Meta Description
```
Công thức: [Hook] + [Nội dung chính] + [CTA]
Ví dụ: "Khám phá 5 công cụ marketing AI hàng đầu cho SME Việt Nam.
        So sánh chi tiết, hướng dẫn triển khai từng bước. Đọc ngay!"
Ký tự: 130-155
```

### Lưu ý tiếng Việt
- Dấu tiếng Việt chiếm nhiều pixel → title có thể bị cắt sớm hơn
- Test trên Google Search Preview tool
- URL slug: bỏ dấu, space → gạch nối: `huong-dan-marketing-ai`

---

## Internal Linking — Liên kết Nội bộ

### Chiến lược Pillar-Cluster
```
PILLAR PAGE (bài trụ)
  ├─ Cluster 1: [keyword phụ 1] → link ← → pillar
  ├─ Cluster 2: [keyword phụ 2] → link ← → pillar
  └─ Cluster 3: [keyword phụ 3] → link ← → pillar
```

### Quy tắc Anchor Text
- ✅ Anchor text descriptive: "hướng dẫn SEO tiếng Việt"
- ❌ Anchor text generic: "nhấn vào đây", "đọc thêm"
- ❌ Anchor text exact match lặp lại: spam

---

## Featured Snippet — Tiếng Việt

### Loại Snippet & Cách Tối ưu

| Loại | Format tối ưu | Ví dụ |
|------|-------------|-------|
| **Paragraph** | Trả lời trực tiếp 40-60 từ | "Marketing AI là gì? Marketing AI là việc ứng dụng..." |
| **List** | Danh sách đánh số/bullet | "5 bước triển khai: 1. Xác định mục tiêu..." |
| **Table** | Bảng so sánh | Bảng so sánh các công cụ AI |
| **Video** | YouTube embed + timestamp | "Hướng dẫn trong video dưới đây" |

### Mẹo Snippet tiếng Việt
- Google hiểu tiếng Việt có dấu tốt → viết đúng chính tả
- Đặt câu hỏi trong H2 → trả lời ngay dưới: "Marketing AI là gì?"
- Dùng bảng / bullet list nhiều → tăng khả năng snippet

---

## Schema Markup cho Bài Viết

### Article Schema (bắt buộc)
```json
{
  "@type": "Article",
  "headline": "Tiêu đề bài viết",
  "author": {"@type": "Person", "name": "Tên tác giả"},
  "datePublished": "2026-03-10",
  "dateModified": "2026-03-10"
}
```

### FAQ Schema (nếu có phần Q&A)
```json
{
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Marketing AI là gì?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Marketing AI là..."
    }
  }]
}
```

### HowTo Schema (nếu có hướng dẫn)
- Mỗi bước = 1 step có name + text
- Google hiển thị dạng "X bước" trên SERP

---

## Checklist SEO On-Page

1. ☐ H1 duy nhất, chứa keyword chính
2. ☐ Meta title ≤60 ký tự, keyword ở đầu
3. ☐ Meta description 130-155 ký tự, có CTA
4. ☐ URL slug ngắn gọn, không dấu, có keyword
5. ☐ Keyword trong 100 từ đầu tiên
6. ☐ H2/H3 chứa keyword phụ
7. ☐ Alt text cho mọi hình ảnh
8. ☐ ≥3 internal links
9. ☐ ≥1 external link (nguồn uy tín)
10. ☐ Bài ≥1500 từ cho keyword cạnh tranh
11. ☐ Schema markup phù hợp
12. ☐ Mobile-friendly (đoạn ngắn, font đủ lớn)
