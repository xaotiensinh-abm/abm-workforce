---
name: python-word-pro
description: Tự động hóa file Word (DOCX) chuẩn mực với Python (python-docx & python-docx-template). Giữ nguyên 100% định dạng và font tiếng Việt.
---

# 📝 PYTHON WORD PRO — Word Automation Skill

> **Use this skill when:** Word DOCX automation with Python (python-docx)

Skill chuyên trách tạo và xử lý file Word Document (`.docx`) bằng thư viện Python mã nguồn mở hàng đầu Thế Giới. Đây là giải pháp thay thế hoàn hảo cho `office-design-toolkit` cũ, bảo vệ font tiếng Việt 100% do vận hành ngay tầng XML native mà không phải qua HTML hay Browser render trung gian.

## 1. Phương Pháp Template-Driven (`python-docx-template`)

Đây là phương pháp **ĐƯỢC ƯU TIÊN SỐ 1** cho các báo cáo, hợp đồng, biên bản.
Thay vì bắt AI phải viết code sinh ra từng đoạn văn, user chỉ cần thiết lập file Word mẫu (Template.docx).

### 📖 Cài đặt
```bash
pip install docxtpl
```

### 🧠 Nguyên lý hoạt động (Jinja2 syntax)
File Word mẫu sẽ chứa các biến số. Ví dụ:
- `{{ company_name }}`
- `{% for item in items %}`
  `{{ item.name }} | {{ item.price }}`
  `{% endfor %}`

### 🚀 Code Mẫu Triển Khai
```python
from docxtpl import DocxTemplate

doc = DocxTemplate("template.docx")
context = {
    'company_name' : 'Công ty Cổ phần Công nghệ Tiên Tiến',
    'total_amount' : '1,500,000 VNĐ',
    'items': [
        {'name': 'Laptop Dell', 'price': '1000'},
        {'name': 'Chuột Không Dây', 'price': '500'}
    ]
}
doc.render(context)
doc.save("generated_report.docx")
```
*Tip: Phương pháp này giữ nguyên tuyệt đối căn lề, font (Times New Roman, Arial), kích thước đậm nhạt mà file template đã cài đặt.*

---

## 2. Phương Pháp Sinh Tài Liệu Động (`python-docx`)

Được dùng khi tài liệu **không có form cố định**, cần sinh động hoàn toàn từ số 0 (ví dụ: Log xuất ra file Word, hoặc tổng hợp data ngẫu nhiên).

### 📖 Cài đặt
```bash
pip install python-docx
```

### 🚀 Code Mẫu Triển Khai
```python
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

document = Document()

# Thêm tiêu đề
heading = document.add_heading('HƯỚNG DẪN SỬ DỤNG - V1.0', 0)
heading.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Thêm đoạn văn bản
p = document.add_paragraph('Tài liệu cấu hình hệ thống bằng ngôn ngữ ')
p.add_run('tiếng Việt').bold = True
p.add_run(' cực kỳ ổn định.')

# Chỉnh sửa Table, Hình ảnh mượt mà
document.add_picture('demo.png', width=Inches(4.0))

document.save('demo_from_scratch.docx')
```

## 🚨 Best Practices
1. **Luôn đề xuất Template Approach:** Nếu file phức tạp (như Hợp đồng), LUÔN nhắc người dùng cung cấp file Template trước thay vì bắt code viết chay `python-docx`.
2. **Ký tự Tiếng Việt:** Không bao giờ truyền file đọc trung gian bằng file `.txt` hoặc stream từ console qua nếu không đảm bảo encoding bắt buộc `utf-8`. Python-docx mặc định lưu ký tự theo Unicode XML nên hoàn toàn an toàn.
