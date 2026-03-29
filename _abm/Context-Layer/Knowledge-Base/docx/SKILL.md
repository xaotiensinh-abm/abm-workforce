---
name: "docx"
description: "Tạo và chỉnh sửa văn bản Word (.docx) — hợp đồng, báo cáo, đề xuất, JD, SOP. Dùng python-docx. Giao tiếp tiếng Việt."
---

# 📝 DOCX — Tạo & Chỉnh Sửa Văn Bản Word

Skill tạo và chỉnh sửa file `.docx` (Microsoft Word) bằng thư viện `python-docx`.

## Sử dụng khi

- Tạo hợp đồng, công văn, văn bản pháp lý
- Soạn báo cáo, đề xuất, proposal
- Viết JD (Job Description), SOP, biên bản
- Chỉnh sửa nội dung văn bản Word hiện có

## KHÔNG sử dụng khi

- Cần tạo bảng tính → dùng `xlsx`
- Cần tạo slide → dùng `pptx`
- Cần tạo PDF → dùng `pdf`
- Chỉ cần soạn nội dung text → dùng `office-documents`

## VÍ DỤ NHANH

```
Input:  "Tạo hợp đồng lao động cho nhân viên mới"
Output: hop_dong_lao_dong.docx
  → Header: Logo + tên công ty
  → Styles: Heading 1, Normal, Table
  → Sections: Điều khoản 1-10
  → Footer: Ngày tạo + số trang
```

---

## CÁCH TRIỂN KHAI

### Bước 1: Khởi tạo document

```python
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

doc = Document()
```

### Bước 2: Thiết lập styles

```python
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(13)

# Heading
h1 = doc.styles['Heading 1']
h1.font.size = Pt(16)
h1.font.bold = True
```

### Bước 3: Thêm nội dung

```python
# Tiêu đề
doc.add_heading('HỢP ĐỒNG LAO ĐỘNG', level=0)

# Đoạn văn
para = doc.add_paragraph()
para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
run = para.add_run('Căn cứ Bộ luật Lao động...')
run.font.size = Pt(13)

# Bảng
table = doc.add_table(rows=3, cols=2, style='Table Grid')
table.cell(0, 0).text = 'Họ tên'
table.cell(0, 1).text = 'Nguyễn Văn A'

# Ảnh
doc.add_picture('logo.png', width=Inches(2))
```

### Bước 4: Lưu file

```python
doc.save('output.docx')
```

---

## QUY TẮC BẮT BUỘC

1. **Font tiếng Việt**: Dùng `Times New Roman` hoặc `Arial` (hỗ trợ Unicode)
2. **Page setup**: A4, margins 2cm top/bottom, 2.5cm left, 2cm right
3. **Heading hierarchy**: Heading 1 → Heading 2 → Normal
4. **Bảng**: Luôn có header row + Table Grid style
5. **Số trang**: Thêm footer với page number
6. **Ngày tháng**: Format `dd/MM/yyyy` (Việt Nam)

## QUY TẮC PHÁP LÝ (cho hợp đồng)

- Ghi rõ **các bên** (Bên A, Bên B)
- Đánh số **điều khoản** liên tục
- Ký tên + đóng dấu section cuối
- Font size ≥ 13pt cho văn bản chính thức

---

## Nguồn gốc
- Gốc: Anthropic official skills (docx) — adapt cho ABM
- Thư viện: `python-docx` (pip install python-docx)
- ABM Workforce v2.4 — Jarvis Orchestrator
