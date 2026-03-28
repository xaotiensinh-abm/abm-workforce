---
description: Xử lý Excel files: tạo, edit, formulas, data analysis
---

Workflow cho Excel (.xlsx): tạo mới, edit, formulas, data analysis, visualization.

---

## Decision Tree

| Task | Tool |
|------|------|
| **Data analysis** | pandas |
| **Formulas & formatting** | openpyxl |
| **Simple data export** | pandas |

---

## Quick Start (pandas)

```python
import pandas as pd

# Read Excel
df = pd.read_excel('file.xlsx')
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # All sheets

# Analyze
df.head()
df.info()
df.describe()

# Write
df.to_excel('output.xlsx', index=False)
```

---

## Create Excel với Formulas (openpyxl)

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

wb = Workbook()
sheet = wb.active

# Add data
sheet['A1'] = 'Revenue'
sheet['B1'] = 1000

# Add formula - LUÔN dùng formula, KHÔNG hardcode giá trị
sheet['B10'] = '=SUM(B2:B9)'
sheet['C5'] = '=(C4-C2)/C2'  # Growth rate

# Formatting
sheet['A1'].font = Font(bold=True, color='0000FF')  # Blue = inputs
sheet.column_dimensions['A'].width = 20

wb.save('output.xlsx')
```

---

## Quy tắc Quan trọng

### ❌ SAI - Hardcode giá trị
```python
total = df['Sales'].sum()
sheet['B10'] = total  # BAD!
```

### ✅ ĐÚNG - Dùng Excel formula
```python
sheet['B10'] = '=SUM(B2:B9)'  # GOOD!
```

---

## Recalculate Formulas (Bắt buộc!)

```bash
python D:\Antigravity\Skill\claude-skills\xlsx\recalc.py output.xlsx
```

Output JSON:
```json
{
  "status": "success",
  "total_errors": 0,
  "total_formulas": 42,
  "error_summary": {}
}
```

---

## Financial Models - Color Standards

| Color | RGB | Dùng cho |
|-------|-----|----------|
| **Blue text** | `0,0,255` | Inputs, user-changeable values |
| **Black text** | `0,0,0` | Formulas, calculations |
| **Green text** | `0,128,0` | Links từ sheets khác |
| **Red text** | `255,0,0` | External links |
| **Yellow background** | `255,255,0` | Key assumptions |

---

## Number Formatting

| Loại | Format |
|------|--------|
| Currency | `$#,##0` + units in header |
| Percentages | `0.0%` |
| Multiples | `0.0x` (EV/EBITDA, P/E) |
| Negative | `(123)` not `-123` |
| Zeros | `-` (dash) |
| Years | Text string `"2024"` not `2,024` |

---

## Workflow Chuẩn

1. **Choose tool**: pandas (data) hoặc openpyxl (formulas/formatting)
2. **Create/Load**: `Workbook()` hoặc `load_workbook()`
3. **Modify**: Data, formulas, formatting
4. **Save**: `wb.save()`
5. **Recalculate**: `python recalc.py output.xlsx`
6. **Fix errors**: Check `error_summary` và sửa #REF!, #DIV/0!, etc.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `#REF!` | Invalid cell reference | Check cell references |
| `#DIV/0!` | Division by zero | Add IF check |
| `#VALUE!` | Wrong data type | Check formula inputs |
| `#NAME?` | Unknown formula | Check spelling |
