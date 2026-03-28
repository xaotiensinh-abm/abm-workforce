# MEP Design Automation - Script Templates

## Shared Style Module

All scripts should import this shared styling module for consistency.

```python
# mep_styles.py — Shared styling for all MEP Excel files
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# Colors
NAVY = '0F3460'
BLUE_LIGHT = 'E8F4FD'
RED = 'E94560'
RED_LIGHT = 'FFF3F3'
GREEN = '27AE60'
GREEN_LIGHT = 'E8F8F5'
GRAY = '666666'

# Fonts
header_font = Font(name='Arial', bold=True, size=9, color='FFFFFF')
section_font = Font(name='Arial', bold=True, size=9, color=NAVY)
data_font = Font(name='Arial', size=9)
note_font = Font(name='Arial', size=8, italic=True, color=GRAY)
formula_font = Font(name='Arial', bold=True, size=9, color=RED)
total_font = Font(name='Arial', bold=True, size=10, color=GREEN)
title_font = Font(name='Arial', bold=True, size=12, color=NAVY)

# Fills
header_fill = PatternFill(start_color=NAVY, end_color=NAVY, fill_type='solid')
section_fill = PatternFill(start_color=BLUE_LIGHT, end_color=BLUE_LIGHT, fill_type='solid')
formula_fill = PatternFill(start_color=RED_LIGHT, end_color=RED_LIGHT, fill_type='solid')
total_fill = PatternFill(start_color=GREEN_LIGHT, end_color=GREEN_LIGHT, fill_type='solid')

# Border
thin_border = Border(
    left=Side('thin'), right=Side('thin'),
    top=Side('thin'), bottom=Side('thin')
)

# Alignment
center_align = Alignment(horizontal='center', vertical='center', wrap_text=True)
left_align = Alignment(horizontal='left', vertical='center', wrap_text=True)

# Helper functions
def apply_header(ws, row, cols):
    """Apply header styling to a row"""
    for c in range(1, cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

def write_row(ws, row, data, bold=False):
    """Write a data row with styling"""
    for c, v in enumerate(data, 1):
        cell = ws.cell(row=row, column=c, value=v)
        cell.font = Font(name='Arial', bold=bold, size=9) if bold else data_font
        cell.alignment = center_align
        cell.border = thin_border

def write_section(ws, row, cols, text):
    """Write a section header (merged)"""
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=cols)
    ws.cell(row=row, column=1, value=text).font = section_font
    ws.cell(row=row, column=1).fill = section_fill
    ws.cell(row=row, column=1).alignment = left_align
    for c in range(1, cols + 1):
        ws.cell(row=row, column=c).border = thin_border

def write_formula(ws, row, col, formula, fmt='#,##0'):
    """Write a formula cell with red highlight"""
    cell = ws.cell(row=row, column=col, value=formula)
    cell.font = formula_font
    cell.fill = formula_fill
    cell.alignment = center_align
    cell.border = thin_border
    cell.number_format = fmt

def write_title(ws, row, cols, text):
    """Write a title row (merged, no border conflicts)"""
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=cols)
    ws.cell(row=row, column=1, value=text).font = title_font

def write_total(ws, row, col, formula, fmt='#,##0'):
    """Write a total cell with green highlight"""
    cell = ws.cell(row=row, column=col, value=formula)
    cell.font = total_font
    cell.fill = total_fill
    cell.alignment = center_align
    cell.border = thin_border
    cell.number_format = fmt
```

## Script File Naming Convention

```
extract_project_docs.py    — Phase 0: Extract all PDFs
extract_templates.py       — Phase 0: Extract internal templates
create_roombook.py         — Phase 1.1: Roombook/MECHANICAL ROOM MATRIX
create_calc_hvac.py        — Phase 1.2: HVAC calculations
create_calc_pccc_equip.py  — Phase 1.2-1.3: PCCC + Plumbing + Equipment List
create_phase2_3.py         — Phase 2-3: Drawing List, Project Outline, BoQ template, Spec Compare
create_final_all.py        — Phase 1.2+3: Calc_Electrical + Complete BoQ + Final Quotation
```

## Key Formulas Reference

### HVAC
- Ventilation: `Vbz = Rp × Pz + Ra × Az` (ASHRAE 62.1)
- Cooling Load: `Q = Area × W/m² × Safety Factor`
- Spot Cooling: `Q = Air Volume × ΔT × 1.2 / 3600`

### Electrical
- Current: `I = P / (√3 × V × PF)`
- Voltage Drop: `VD% = P × L × 2 / (σ × V² × A) × 100`
- Lighting: `N = Area × Lux / (Lumens × MF × UF)`

### Fire Fighting
- Sprinkler Flow: `Q = Density × Design Area`
- Tank Volume: `V = Q × Duration (hours)`
- Hydrant: refer TCVN 2622 Table 6

### Plumbing
- Water Supply: WSFU method (ASPE Vol.2)
- Drainage: DFU method
