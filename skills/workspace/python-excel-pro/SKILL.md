---
name: python-excel-pro
description: Xử lý và thiết kế Báo cáo Excel chuyên nghiệp (XlsxWriter, openpyxl, pandas). Tốc độ cao, siêu cấp bảng biểu đồ.
---

# 📊 PYTHON EXCEL PRO — Excel Automation Skill

> **Use this skill when:** Excel report generation with Python (XlsxWriter, openpyxl)

Hệ sinh thái công cụ hỗ trợ đọc, ghi, và thiết kế các file Báo cáo Excel cấp độ Doanh nghiệp (Enterprise-level).

## 1. Khởi tạo Báo Cáo Chuyên Sâu (`XlsxWriter`)
**XlsxWriter** là thư viện Python số 1 để **TẠO MỚI** file Excel từ đầu.
- Tốc độ vô địch (hỗ trợ ghi stream cho hàng triệu dòng data)
- Hỗ trợ Chart, Formatting, Pivot Table mạnh nhất trong số các thư viện.

### 📖 Cài đặt
```bash
pip install XlsxWriter
```

### 🚀 Code Mẫu Triển Khai
```python
import xlsxwriter

workbook = xlsxwriter.Workbook('doanh_thu.xlsx')
worksheet = workbook.add_worksheet('Tháng 1')

# Định dạng in đậm & Tiền tệ
bold = workbook.add_format({'bold': True, 'font_name': 'Arial'})
money = workbook.add_format({'num_format': '#,##0 "VNĐ"', 'font_name': 'Arial'})

worksheet.write('A1', 'Dịch Vụ', bold)
worksheet.write('B1', 'Thành Tiền', bold)

expenses = [
    ['Thiết kế Website', 15000000],
    ['Chạy Quảng Cáo', 20000000],
]

row = 1
for item, cost in expenses:
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, cost, money)
    row += 1

worksheet.write(row, 0, 'Tổng', bold)
worksheet.write(row, 1, '=SUM(B2:B3)', money)

workbook.close()
```

---

## 2. Xử lý & Phân tích Data (`pandas` + `openpyxl`)
**Openpyxl** cực mạnh trong quy trình **ĐỌC, CHỈNH SỬA & GHI ĐÈ** các file Excel đã có (chuyên dùng thay đổi file Excel Mẫu hoặc chạy Data ETL Pipeline trực tiếp cùng AI Agent W5: Data).

### 📖 Cài đặt
```bash
pip install pandas openpyxl
```

### 🚀 Code Mẫu Triển Khai
```python
import pandas as pd

# Load data và dọn dẹp cấp tốc bằng Pandas
df = pd.read_excel('raw_data.xlsx')
df_filtered = df[df['Doanh_Thu'] > 1000000]

# Xuất ra với OpenPyXL làm engine
with pd.ExcelWriter('bao_cao_final.xlsx', engine='openpyxl') as writer:
    df_filtered.to_excel(writer, index=False, sheet_name='Data Lọc')
```

## 🚨 Best Practices
1. Xác định CỰC RÕ hành vi thao tác:
   - Tạo Mới HOÀN TOÀN + Charts đẹp ➔ `XlsxWriter`
   - Đọc, Load Mẫu, Sửa data ➔ `openpyxl`
2. Tuyệt đối không hardcode giá trị bảng tổng (Sum) nếu có thể xài Formula excel `=SUM(...)`.
3. Lưu ý Font mặc định: Khi tạo file mới, cài đặt Font Family mặc định như Arial hoặc Times New Roman để File tương thích tối đa trên cả MS Excel & Google Sheets.
