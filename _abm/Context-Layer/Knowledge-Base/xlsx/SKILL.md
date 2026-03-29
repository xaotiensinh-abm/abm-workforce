---
name: "xlsx"
description: "Tạo và xử lý bảng tính Excel (.xlsx) — báo cáo tài chính, KPI dashboard, data analysis. Dùng openpyxl. Giao tiếp tiếng Việt."
---

# 📊 XLSX — Tạo & Xử Lý Bảng Tính Excel

Skill tạo và xử lý file `.xlsx` (Microsoft Excel) bằng `openpyxl`.

## Sử dụng khi

- Tạo báo cáo tài chính, bảng lương, chi phí
- Xây dashboard KPI, bảng theo dõi
- Phân tích dữ liệu: pivot, formulas, charts
- Import/export data từ hệ thống

## KHÔNG sử dụng khi

- Cần phân tích data chuyên sâu → dùng `data-analysis`
- Cần văn bản → dùng `docx`
- Cần trình chiếu → dùng `pptx`

## VÍ DỤ NHANH

```
Input:  "Tạo báo cáo doanh thu Q1/2026"
Output: bao_cao_doanh_thu_Q1.xlsx
  → Sheet 1: Bảng doanh thu theo tháng
  → Sheet 2: Chart xu hướng
  → Sheet 3: Summary KPIs
  → Formulas: SUM, AVERAGE, % growth
```

---

## CÁCH TRIỂN KHAI

### Bước 1: Khởi tạo workbook

```python
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill, numbers
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active
ws.title = "Doanh Thu"
```

### Bước 2: Headers + Styling

```python
headers = ['Tháng', 'Doanh Thu', 'Chi Phí', 'Lợi Nhuận', '% Margin']
header_font = Font(name='Arial', size=12, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='2563EB', end_color='2563EB', fill_type='solid')

for col, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal='center')
```

### Bước 3: Data + Formulas

```python
data = [
    ['Tháng 1', 500000000, 350000000],
    ['Tháng 2', 620000000, 380000000],
    ['Tháng 3', 580000000, 360000000],
]

for row_idx, row_data in enumerate(data, 2):
    for col_idx, value in enumerate(row_data, 1):
        ws.cell(row=row_idx, column=col_idx, value=value)
    # Lợi nhuận = Doanh thu - Chi phí
    ws.cell(row=row_idx, column=4, value=f'=B{row_idx}-C{row_idx}')
    # % Margin
    ws.cell(row=row_idx, column=5, value=f'=D{row_idx}/B{row_idx}')
    ws.cell(row=row_idx, column=5).number_format = '0.0%'

# Tổng cộng
last_row = len(data) + 2
ws.cell(row=last_row, column=1, value='TỔNG').font = Font(bold=True)
ws.cell(row=last_row, column=2, value=f'=SUM(B2:B{last_row-1})')
```

### Bước 4: Chart

```python
chart = BarChart()
chart.title = "Doanh Thu Q1/2026"
chart.y_axis.title = "VNĐ"
data_ref = Reference(ws, min_col=2, max_col=3, min_row=1, max_row=len(data)+1)
cats = Reference(ws, min_col=1, min_row=2, max_row=len(data)+1)
chart.add_data(data_ref, titles_from_data=True)
chart.set_categories(cats)
ws.add_chart(chart, "G2")
```

### Bước 5: Lưu file

```python
wb.save('bao_cao.xlsx')
```

---

## QUY TẮC BẮT BUỘC

1. **Header row**: Luôn bold + background color + center aligned
2. **Number format**: Tiền VNĐ dùng `#,##0` — Percent dùng `0.0%`
3. **Column width**: Auto-fit hoặc tối thiểu 15 characters
4. **Sheet names**: Tiếng Việt không dấu đặc biệt, ngắn gọn
5. **Freeze panes**: Freeze row 1 (header) cho dễ scroll
6. **Formulas**: Dùng formulas thay hardcode values khi có thể
7. **Borders**: Table Grid cho data tables

---

## Nguồn gốc
- Gốc: Anthropic official skills (xlsx) — adapt cho ABM
- Thư viện: `openpyxl` (pip install openpyxl)
- ABM Workforce v2.4 — Jarvis Orchestrator
