---
name: python-excel-pro
description: Xử lý và thiết kế Báo cáo Excel chuyên nghiệp (XlsxWriter, openpyxl, pandas). Tốc độ cao, siêu cấp bảng biểu đồ.
---

# 📊 PYTHON EXCEL PRO — Excel Automation Skill

> **Use this skill when:** Excel report generation with Python (XlsxWriter, openpyxl)

Hệ sinh thái công cụ hỗ trợ đọc, ghi, và thiết kế các file Báo cáo Excel cấp độ Doanh nghiệp (Enterprise-level).

## 1. Khởi tạo Báo Cáo Chuyên Sâu (Premium Enterprise Excel)

Kỹ năng `python-excel-pro` đã được nâng cấp (v2.0) với kịch bản đóng gói sẵn, tự động áp dụng 12 premium features (Theme colors, Autofit columns, Freeze panes, Formatting, Charts, Print setup).

### 🚀 Cách Dùng Nhanh (Sử dụng Script có sẵn)

Thay vì viết code Python từ đầu, hãy tạo một file cấu hình JSON (`data.json`) chứa metadata và dữ liệu bảng, sau đó chạy script đã đóng gói:

```bash
# Antigravity Global Environment:
C:\Users\PC\AppData\Local\Programs\Python\Python311\python.exe ~/.gemini/antigravity/skills/python-excel-pro/scripts/build_excel.py "đường_dẫn_json.json" "đường_dẫn_xuất.xlsx"
```

### 📋 Cấu trúc JSON Mẫu (v3.0)
```json
{
  "report_title": "Báo cáo Doanh Thu",
  "author": "ABM-Workforce Agent",
  "theme": "ocean",
  "tables": [
    {
      "sheet_name": "Data",
      "column_groups": [
        {"title": "Thông Tin Bệnh Nhân", "span": 5, "collapsed": false},
        {"title": "Hồ Sơ Lâm Sàng", "span": 5, "collapsed": true}
      ],
      "conditional_formats": [
        {"col": 8, "type": "3_color_scale", "min_color": "#63BE7B", "mid_color": "#FFEB84", "max_color": "#F8696B"},
        {"col": 9, "type": "data_bar", "bar_color": "#638EC6"}
      ],
      "headers": ["Ngày", "Khách Hàng", "Doanh Thu"],
      "types": ["date", "string", "currency"],
      "data": [
        ["2026-03-01", "Vingroup", 150000000]
      ],
      "totals_row": true,
      "chart": {
        "type": "column",
        "title": "Biểu Đồ Doanh Thu",
        "category_col": 0,
        "value_col": 2
      }
    }
  ]
}
```

**Các mảng mở rộng v3.0 (Tùy chọn):**
- `column_groups`: Dùng cho báo cáo >15 cột. Tạo Multi-level Headers (Merged Cells) và tính năng Collapse/Expand.
- `conditional_formats`: Dùng `3_color_scale` cho thang điểm đánh giá, và `data_bar` cho cột dòng tiền.
- *Lưu ý: Mọi cảnh báo lỗi `number_stored_as_text` sẽ được AI tự động dọn dẹp sạch sẽ.*

Các kiểu dữ liệu `types` hỗ trợ: `string`, `int`, `float`, `currency`, `date`.

---

## 2. Xử lý Data Custom (`pandas` + `openpyxl`)

Nếu bạn chỉ cần đọc file mẫu, hoặc xử lý DataFrame phức tạp (như Data ETL Pipeline), bạn vẫn có thể tự viết mã Python bằng Pandas và Openpyxl.

### 🚨 Best Practices
1. Xác định CỰC RÕ hành vi thao tác:
   - Tạo Mới HOÀN TOÀN Report Doanh Nghiệp ➔ Chạy script `build_excel.py`
   - Đọc, Load Mẫu, Sửa data ➔ Viết script dùng `pandas` + `openpyxl`
2. Kịch bản `build_excel.py` tự lo phần UI/UX cho Excel (Zebra striping, Freeze Panes, Formatting). Đừng phí token tự căn chỉnh từng ô.
