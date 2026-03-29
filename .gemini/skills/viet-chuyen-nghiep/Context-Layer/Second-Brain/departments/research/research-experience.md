# Bộ nhớ Kinh nghiệm: Ban Nghiên cứu

## Nguồn tin cậy theo Lĩnh vực (Whitelist)

### Kinh tế & Tài chính
- Tổng cục Thống kê (gso.gov.vn)
- Ngân hàng Nhà nước Việt Nam
- World Bank Vietnam Reports
- McKinsey Vietnam, BCG Vietnam
- Bloomberg, Reuters (international)

### Công nghệ
- ArXiv, IEEE, ACM Digital Library
- TechCrunch, The Verge (international)
- TechInAsia, TheLead.vn (regional)

### Y tế
- WHO, PubMed, The Lancet
- Bộ Y tế Việt Nam, CDC Vietnam

## Trường hợp Xử lý Mâu thuẫn

**Case 1**: Source A nói "thị trường AI VN tăng 30%", Source B nói "25%"
→ **Resolution**: Ghi cả 2, note methodology khác nhau, ưu tiên source có methodology rõ

**Case 2**: Chuyên gia X nói "remote work tốt", chuyên gia Y nói "kém"
→ **Resolution**: Trình bày cả 2 quan điểm, note context khác nhau (industry, role)

**Case 3**: Data 2024 vs Data 2025 khác nhau
→ **Resolution**: Dùng data mới nhất, ghi rõ năm

## Mẫu Ghi chú Nghiên cứu

```yaml
research_note:
  topic: "[chủ đề]"
  date: "[ngày research]"
  findings:
    - finding: "[phát hiện]"
      source: "[nguồn]"
      confidence: "[high/medium/low]"
      type: "[fact/assumption/opinion]"
  gaps: ["[thông tin chưa tìm được]"]
  next_steps: ["[cần research thêm gì]"]
```
