---
name: "pdf"
version: 1.0.1
author: ABM Skill Architect
last_updated_date: 2026-04-09
description: "LOCAL-ONLY — Đọc, merge/split, tạo PDF đơn giản (invoice, biên nhận) bằng fpdf2 + PyPDF2. Chỉ dùng khi user YÊU CẦU CỤ THỂ thao tác PDF local (merge, split, đọc text). Mặc định tạo document PDF MỚI → dùng skywork-doc --format pdf."
---

> [!IMPORTANT]
> **Routing Rule:** Mặc định tạo file PDF mới → dùng `skywork-doc --format pdf` (Skywork Cloud API). Skill này CHỈ dùng khi: (1) merge/split PDF local, (2) đọc/trích xuất text từ PDF, (3) tạo PDF đơn giản (invoice template) mà không cần AI viết nội dung, (4) user nói rõ "làm offline".

# 📄 PDF — Tạo & Xử Lý File PDF

Skill tạo, đọc và xử lý file `.pdf` — dùng `fpdf2` (tạo) + `PyPDF2` (đọc/xử lý).

## Sử dụng khi

- Tạo invoice, hóa đơn, biên nhận
- Tạo báo cáo PDF từ data
- Merge nhiều PDF thành 1 file
- Tách pages từ PDF lớn
- Đọc text từ PDF hiện có

## KHÔNG sử dụng khi

- Cần file Word editable → dùng `skywork-doc` (mặc định) hoặc `docx-official` (local)
- Cần bảng tính → dùng `skywork-excel` (mặc định) hoặc `xlsx-official` (local)
- Cần visual art/poster → dùng `skywork-design` hoặc `canvas-design`

## VÍ DỤ NHANH

```
Input:  "Tạo invoice cho đơn hàng #1234"
Output: invoice_1234.pdf
  → Header: Logo + thông tin công ty
  → Body: Bảng sản phẩm + giá
  → Footer: Tổng tiền + VAT + thanh toán
```

---

## CÁCH TRIỂN KHAI

### Tạo PDF mới (fpdf2)

```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# Font tiếng Việt
pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
pdf.set_font('DejaVu', '', 13)

# Header
pdf.set_font('DejaVu', 'B', 18)
pdf.cell(0, 10, 'HÓA ĐƠN BÁN HÀNG', ln=True, align='C')

# Bảng
pdf.set_font('DejaVu', '', 11)
col_widths = [20, 80, 30, 30, 30]
headers = ['STT', 'Sản phẩm', 'SL', 'Đơn giá', 'Thành tiền']
for w, h in zip(col_widths, headers):
    pdf.cell(w, 8, h, border=1, align='C')
pdf.ln()

# Data rows
items = [('1', 'Laptop Dell XPS', '2', '25,000,000', '50,000,000')]
for item in items:
    for w, val in zip(col_widths, item):
        pdf.cell(w, 8, val, border=1, align='C')
    pdf.ln()

pdf.output('invoice.pdf')
```

### Đọc PDF (PyPDF2)

```python
from PyPDF2 import PdfReader

reader = PdfReader('document.pdf')
for page in reader.pages:
    text = page.extract_text()
    print(text)
```

### Merge PDFs

```python
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append('file1.pdf')
merger.append('file2.pdf')
merger.write('merged.pdf')
merger.close()
```

---

## QUY TẮC BẮT BUỘC

1. **Font tiếng Việt**: PHẢI add font Unicode (DejaVu, Roboto)
2. **Page size**: A4 (210 × 297mm)
3. **Margins**: 15mm mỗi bên
4. **Bảng**: Luôn có borders + header row
5. **Number format**: Tiền VNĐ có dấu phẩy phân cách nghìn
6. **Footer**: Số trang + ngày tạo

---

## Nguồn gốc
- Gốc: Anthropic official skills (pdf) — adapt cho ABM
- Thư viện: `fpdf2` (tạo) + `PyPDF2` (đọc/xử lý)
- ABM Workforce v2.4 — Jarvis Orchestrator
