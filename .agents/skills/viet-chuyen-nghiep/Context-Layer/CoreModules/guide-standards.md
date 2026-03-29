# Guide Standards — CoreModule

## Technical Writing Standards cho Tài Liệu Hướng Dẫn

### Nguyên tắc vàng
1. **1 step = 1 action** — không gộp nhiều việc vào 1 bước
2. **Start with verb** — "Nhấn", "Chọn", "Nhập", "Mở", "Kéo"
3. **Show result** — Sau mỗi step, nêu kết quả mong đợi
4. **Assume nothing** — Đừng giả sử reader biết, viết explicit
5. **Task-based** — Tổ chức theo nhiệm vụ, không theo tính năng

### Action Verbs chuẩn
| Hành động | Verb VN | Verb EN |
|-----------|---------|---------|
| Mouse click | Nhấn / Bấm | Click |
| Type text | Nhập / Gõ | Type / Enter |
| Select option | Chọn | Select |
| Navigate | Vào / Mở | Navigate to / Open |
| Drag | Kéo | Drag |
| Toggle | Bật / Tắt | Toggle on/off |
| Scroll | Cuộn xuống | Scroll down |
| Upload | Tải lên | Upload |
| Download | Tải về | Download |

## Callout Box Standards

### Types & Usage
```markdown
> 💡 **TIP:** Mẹo giúp làm nhanh hơn hoặc hiệu quả hơn
> Dùng cho: shortcuts, best practices, pro tips

> ⚠️ **WARNING:** Hành động có thể gây vấn đề nếu không cẩn thận
> Dùng cho: common mistakes, data loss risk

> 📌 **NOTE:** Thông tin bổ sung, không critical
> Dùng cho: context, alternatives, clarification

> 🚫 **DANGER:** Hành động KHÔNG THỂ hoàn tác
> Dùng cho: destructive actions, permanent changes

> ✅ **RESULT:** Kết quả mong đợi sau bước vừa thực hiện
> Dùng cho: confirmation, expected output
```

## Numbering Convention

### Sections
```
1. Section chính
   1.1 Sub-section
      1.1.1 Sub-sub (tối đa 3 cấp)
```

### Figures & Tables
```
Hình [chapter].[sequence]: [Caption]
Bảng [chapter].[sequence]: [Caption]

Ví dụ:
Hình 2.3: Giao diện cài đặt hệ thống
Bảng 4.1: So sánh các gói dịch vụ
```

### Procedural Steps
```
Bước 1: [Action]
   → [Expected result]
Bước 2: [Action]
   → [Expected result]
```

## Screenshot Standards

### Placement Rules
- Screenshot ĐẶT NGAY SAU step mà nó minh họa
- Caption mô tả rõ: "Hình X: [Gì] ở [Đâu]"
- Highlight vùng cần chú ý (red circle / arrow)
- Max width: 80% page width
- Alt text bắt buộc (accessibility)

### Annotation
```
🔴 Red circle — điểm cần click
🟢 Green highlight — kết quả đúng
↗️ Arrow — hướng dẫn follow
📝 Callout text — giải thích element
```

## Version Control Standards

### Header mỗi document
```
Document: [Tên tài liệu]
Version: [X.Y]
Last Updated: [YYYY-MM-DD]
Author: [Tên]
Status: Draft | Review | Published
```

### Change Log
```markdown
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-10 | Team | First release |
| 1.1 | 2026-03-15 | Team | Updated Section 3, added FAQ |
| 2.0 | 2026-04-01 | Team | Major restructure, new features |
```

### Versioning Rules
- **X.0** — Major rewrite / restructure
- **X.Y** — New sections, significant updates
- **X.Y.Z** — Typo fixes, minor corrections

## Document Types — Checklist

### User Guide ✅
- [ ] Cover page
- [ ] Table of Contents
- [ ] Getting Started section
- [ ] Task-based core sections
- [ ] Screenshots at key steps
- [ ] Troubleshooting section
- [ ] Glossary
- [ ] Version & date

### SOP ✅
- [ ] Purpose & scope
- [ ] RACI matrix
- [ ] Flowchart
- [ ] Numbered steps
- [ ] Forms/templates
- [ ] Review schedule
- [ ] Version control

### FAQ ✅
- [ ] Sorted by frequency
- [ ] Clear Q&A format
- [ ] Related links
- [ ] Contact info for unsolved
- [ ] Last reviewed date
