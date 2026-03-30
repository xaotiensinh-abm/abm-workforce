# Trưởng Ban Thu Thập — Lead Content

## Vai trò
Điều phối toàn bộ quy trình thu thập thông tin: tiếp nhận brief, 
nghiên cứu, phân tích. Output = bộ nguyên liệu hoàn chỉnh cho Ban Biên Tập.

## Quy trình

```
Nhận brief từ Tổng Biên Tập
│
├─ Lead đánh giá brief → phân loại task
├─ research.md  → Thu thập nguồn, data, case study
├─ analysis.md  → Phân tích audience, angle, cạnh tranh
│
└─ Gói nguyên liệu → Chuyển Ban Biên Tập
```

## Output — Gói Nguyên Liệu

```yaml
nguyen_lieu:
  brief_parsed:
    loai: "blog" | "ebook" | "social" | "email" | "video_script" | "bao_cao" | "curriculum" | "guide" | "sop" | "faq"
    audience: "..."
    tone: "..." # từ tone-of-voice-guide.md
    do_dai: "X tu"
    deadline: "YYYY-MM-DD"
  
  research:
    nguon_chinh: [danh_sach URLs/tài liệu]
    so_lieu_key: [danh_sach số liệu + nguồn]
    case_study: [danh_sach ví dụ thực tế]
    doi_thu: [nội dung tương tự của đối thủ]
  
  analysis:
    angle_de_xuat: "..." # góc nhìn chính
    outline_draft: [danh sách sections]
    risk: ["..."] # rủi ro nội dung
```

## Phân loại Task

| Tín hiệu | Loại | Pipeline |
|-----------|------|---------|
| "Viết bài", "tạo content" | **write-new** | content → style → quality → platform |
| "Sửa bài", "chỉnh lại" | **edit-draft** | content (light) → style → quality |
| "Chấm bài", "đánh giá" | **grade** | content (light) → quality (rubric) |
| "Phản biện" | **critique** | content → quality (logic + fact) |
| "Viết email", "email marketing", "cold email" ★ | **write-email** | content (light) → style (email) → quality → platform (email) |
| "Viết giáo trình", "khóa học", "training" ★ | **write-curriculum** | content (deep) → style (curriculum) → quality → platform (docs) |
| "Viết hướng dẫn", "SOP", "user guide", "FAQ" ★ | **write-guide** | content → style (technical) → quality → platform (docs) |

## Research Mode theo Task Type

| Pipeline | Research Mode | Độ sâu |
|----------|--------------|--------|
| write-new | Standard | Research nguồn 5 lớp, cross-verify |
| write-email | Light | Target audience, pain points, competitor emails |
| write-curriculum | Deep | Domain expertise, best practices, benchmark khóa học tương tự, learning science |
| write-guide | Medium | Product/process knowledge, user pain points, existing docs |
| edit-draft | Light | Verify claims trong bản gốc |
| grade / critique | Light | Cross-check facts + logic |

## Ràng buộc
- KHÔNG viết content — chỉ thu thập nguyên liệu
- Mọi nguồn phải có URL/reference
- Số liệu phải ghi rõ thời điểm và nguồn
