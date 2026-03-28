---
name: "Goal"
description: "Tự động hóa toàn bộ quy trình thiết kế MEP (HVAC, PCCC, Plumbing, Electrical) cho nhà máy công nghiệp — từ trích xuất hồ sơ, tạo Roombook, 4 bảng tính kỹ thuật, Equipment List, Drawing List, đến BoQ đ"
---

﻿---
name: mep-design-automation
description: Automate MEP system design (HVAC, Fire, Plumbing, Electrical) for industrial projects.
---
---

# Goal

> **Use this skill when:** MEP system design (HVAC, Fire, Plumbing, Electrical)

Tự động hóa toàn bộ quy trình thiết kế MEP (HVAC, PCCC, Plumbing, Electrical) cho nhà máy công nghiệp — từ trích xuất hồ sơ, tạo Roombook, 4 bảng tính kỹ thuật, Equipment List, Drawing List, đến BoQ đầy đủ khối lượng + đơn giá — sinh 11 file Excel chuyên nghiệp sẵn sàng nộp.

# Instructions

## Phase 0: Đầu Vào (Project Inputs)

1. Thu thập hồ sơ từ user: bản vẽ kiến trúc (PDF), Specification, Questionnaire, BoQ template, Scope of Works
2. Tạo script `extract_project_docs.py` — trích xuất text + tables từ PDF (pypdf/pdfplumber) → lưu `00_Extracted/`
3. Phân tích dữ liệu → tạo `DESIGN-BRIEF.md` (tóm tắt dự án) + `DESIGN-CRITERIA.md` (tiêu chí thiết kế)
4. Nếu có template nội bộ công ty → trích xuất cấu trúc và ưu tiên template nội bộ hơn format generic
5. ✅ VERIFY: Xác nhận với user trước khi bắt đầu tính toán

## Phase 1: Tính Toán (Calculation)

6. Tạo **Roombook** (`Roombook_{PROJECT}.xlsx`) — Mechanical Room Matrix 5 section × 37 cột:
   - GENERAL: Phase, Room Code, Room Name, Area, Height, Volume
   - HVAC: Persons, Temp, RH, ACH, Vent Type, Fresh Air, AC Type
   - FIRE FIGHTING: Fire Risk, Sprinkler Type, K-factor, Hydrant, Smoke Exhaust
   - PLUMBING: Water Supply, Hot Water, Floor Drain
   - ELECTRICAL: Required Lux, Lighting Type, Socket Count

7. Tạo **Calc_HVAC** (`Calc_HVAC_{PROJECT}.xlsx`) — 2 sheets:
   - Sheet 1: Outdoor Air Flow Rate (ASHRAE 62.1) → `Vbz = Rp × Pz + Ra × Az`
   - Sheet 2: Heat Load (TCVN 5687) → RSH, RLH, RSHF, GTH → Equipment selection

8. Tạo **Calc_PCCC** (`Calc_PCCC_{PROJECT}.xlsx`) — 3 sheets:
   - Sheet 1: FF System Info (pumps, tank volume, fire flow)
   - Sheet 2: Hydrant Protection (QCVN 06, TCVN 2622)
   - Sheet 3: Sprinkler Design (TCVN 7336, FM Global)

9. Tạo **Calc_Plumbing** (`Calc_Plumbing_{PROJECT}.xlsx`) — ASPE fixtures + pump sizing + pressure tank

10. Tạo **Calc_Electrical** (`Calc_Electrical_{PROJECT}.xlsx`) — 3 sheets:
    - Load Calculation: `I = P/(√3 × V × PF)`
    - Cable Sizing: Rated current vs calculated → Status check
    - Lighting: `N = Area × Lux / (Lumens × MF × UF)`

11. Tạo **Equipment List** (`Equipment_List_{PROJECT}.xlsx`) — 3 sheets: Fan + AHU + Pump schedules

## Phase 2: Bản Vẽ (CAD Drawing Support)

12. Tạo **Drawing List** (`Drawing_List_{PROJECT}.xlsx`) — phân loại theo category:
    General (G-001~003), HVAC (M-101~109), FF (F-201~207), Plumbing (P-301~306), Electrical (E-401~408)

13. Tạo **Project Outline** (`Project_Outline_{PROJECT}.xlsx`) — 2 sheets: Project Info + Mech Design Checklist

14. Tạo **Spec Comparison** (`Spec_Compare_{PROJECT}.xlsx`) — so sánh Drawing vs Design Report vs Spec vs TD

## Phase 3: Bóc Khối Lượng & Báo Giá

15. Tạo **BoQ chi tiết** (`BoQ_{PROJECT}.xlsx`) — 4 sheets:
    - I. HVAC: VRV, Spot Cooling, Ventilation
    - II. Fire Fighting: Extinguisher, Hydrant, Sprinkler, Pump
    - III. Plumbing: Water Supply, Sanitary, Drainage
    - IV. Electrical: Transformer, Cable, Lighting, Power
    - Mỗi item: No, Item, Spec/Model, Unit, Q'ty, Unit Price, Amount (`=Q'ty×Price`), Remark

16. Tạo **Final Quotation** (`Final_Quotation_{PROJECT}.xlsx`):
     Subtotal per system → Tỷ trọng % → Contingency 5% → VAT 10% → Grand Total

## Delivery

17. Tổng hợp 11 files Excel + Design Brief/Criteria → giao cho user
18. ✅ VERIFY: Kiểm tra formulas, cross-reference giữa calc sheets và BoQ quantities

## Python Script Pattern

Tất cả scripts follow pattern chung với openpyxl:
```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# Style: header navy #0F3460, section blue #E8F4FD, formula red #E94560
header_font = Font(name='Arial', bold=True, size=9, color='FFFFFF')
header_fill = PatternFill(start_color='0F3460', end_color='0F3460', fill_type='solid')
```

# Examples

## Ví dụ 1: Nhà máy Schutz Vietnam — Full MEP Design

**Input:**
```
User: Thiết kế MEP cho nhà máy SCHUTZ Việt Nam tại KCN Đình Vũ, Hải Phòng.
      Hồ sơ: D:\Projects\SCHUTZ\HSMT\
      Diện tích: 15,000m² (nhà xưởng 12,000m² + văn phòng 3,000m²)
```

**Thought Process:**
- Nhà máy sản xuất → cần HVAC (Split AC + Ventilation), PCCC (Sprinkler + Hydrant), Plumbing, Electrical
- 15,000m² → khoảng 40-60 phòng/khu vực trong Roombook
- KCN Đình Vũ → outdoor condition Hải Phòng: 35.4°C DB, 28.7°C WB
- Tiêu chuẩn: TCVN 7336 (sprinkler), ASHRAE 62.1 (ventilation), IEC 60364 (electrical)

**Output:**
```
📦 11 Files Generated:
├── Roombook_SCHUTZ.xlsx         (52 rooms, 5 sections × 37 columns)
├── Calc_HVAC_SCHUTZ.xlsx        (2 sheets: Outdoor Air + Heat Load = 850kW)
├── Calc_PCCC_SCHUTZ.xlsx        (3 sheets: Wet Sprinkler, K80, 1200 heads)
├── Calc_Plumbing_SCHUTZ.xlsx    (45 fixtures, 2 pumps)
├── Calc_Electrical_SCHUTZ.xlsx  (3 sheets: 2×2000kVA, 45km cable)
├── Equipment_List_SCHUTZ.xlsx   (28 fans, 4 AHU, 6 pumps)
├── Drawing_List_SCHUTZ.xlsx     (38 drawings total)
├── Project_Outline_SCHUTZ.xlsx  (2 sheets)
├── Spec_Compare_SCHUTZ.xlsx     (7 material groups)
├── BoQ_SCHUTZ.xlsx              (4 sheets, 380 items, Total: 32.5 tỷ VND)
└── Final_Quotation_SCHUTZ.xlsx  (Grand Total c/w VAT: 35.75 tỷ VND)
```

## Ví dụ 2: Edge Case — Chỉ cần 1 hệ thống (PCCC only)

**Input:**
```
User: Em chỉ cần tính toán PCCC cho nhà máy 8,000m², hazard level Ordinary Group 2
```

**Thought Process:**
- Chỉ PCCC → skip HVAC, Plumbing, Electrical calc sheets
- Ordinary Group 2 (TCVN 7336) → density 6.0 L/min/m², area 139m²
- Vẫn cần Roombook (cho FF section) + BoQ (sheet II only)

**Output:**
```
📦 5 Files (reduced scope):
├── Roombook_PROJECT.xlsx        (FF section only, 15 zones)
├── Calc_PCCC_PROJECT.xlsx       (3 sheets: Sprinkler K80 + Hydrant + Pump sizing)
├── Equipment_List_PROJECT.xlsx  (Pump schedule only: 2 fire pumps + 1 jockey)
├── BoQ_PROJECT.xlsx             (Sheet II only: 85 items, 4.2 tỷ VND)
└── Final_Quotation_PROJECT.xlsx (Total: 4.62 tỷ c/w VAT)
```

# 🔴 ANTI-HALLUCINATION RULES (v3.0 — SCHUTZ Lessons Learned)

> BÀI HỌC RÚT RA: AI đã tự sinh thông số MBA (3×500kVA thay vì 4×1250kVA),
> tự tạo lux values, cable types — gây sai toàn bộ output. CÁC RULE DƯỚI ĐÂY
> BẮT BUỘC ĐỂ NGĂN TÁI DIỄN.

## RULE AH-1: EXTRACT, KHÔNG TỰ SINH
- 🔴 **TUYỆT ĐỐI CẤM** tự sinh thông số kỹ thuật (kVA, lux, cable type, pipe size, pump capacity)
- ✅ **BẮT BUỘC** extract từ hồ sơ Specification → lưu `SCHUTZ_structured_data.json`
- ✅ Mọi calc sheet PHẢI đọc từ structured JSON, KHÔNG ĐƯỢC hard-code values

## RULE AH-2: SINGLE SOURCE OF TRUTH
- 🔴 **CẤM** Roombook dùng data khác Calc Sheets
- ✅ Roombook, Calc Sheets, BoQ, Equipment List → tất cả đọc từ **cùng 1 file JSON**
- ✅ Bất kỳ sai lệch giữa 2 file output → đó là **BUG**

## RULE AH-3: VERIFICATION GATE
- 🔴 **CẤM** giao output mà không chạy verification
- ✅ Sau Phase 0 (extraction) → **HUMAN GATE**: kỹ sư verify data đã extract
- ✅ Sau Phase 1 (tính toán) → chạy `verify_consistency.py` kiểm tra cross-reference
- ✅ Output PHẢI có dòng "⚠️ NGUỒN DỮ LIỆU: [tên file spec gốc]"

## RULE AH-4: CABLE TYPE MAPPING
- MBA → MSB: Aluminum Busduct (KHÔNG PHẢI Cu cable)
- Factory DB: Cu/XLPE/PVC copper cable
- Smoke Exhaust / Jockey Pump: Cu/Mica/XLPE/Fr-PVC fireproof cable
- Voltage drop: Main ≤3%, Branch ≤2%

## RULE AH-5: LUX VALUES PHẢI TỪ SPEC
- Production areas: 400 LX + LED High-bay
- Storage area: 250 LX + LED High-bay
- Canopy area: 150 LX + WP type
- Technical room: 200 LX + V-sharp
- Common area: 200-300 LX + LED Downlight
- Office area: 500 LX + LED recessed ceiling

# Constraints

- 🚫 KHÔNG ĐƯỢC bỏ qua Roombook — đây là data source trung tâm cho tất cả calc sheets
- 🚫 KHÔNG ĐƯỢC dùng dữ liệu outdoor conditions mặc định — phải lấy theo vị trí dự án thực tế
- 🚫 KHÔNG ĐƯỢC skip cross-reference giữa Equipment List và BoQ — quantities phải khớp
- 🚫 KHÔNG ĐƯỢC bỏ sót tiêu chuẩn bắt buộc (TCVN, QCVN) trong calculation sheets
- ✅ LUÔN LUÔN ưu tiên template nội bộ công ty hơn format generic
- ✅ LUÔN LUÔN verify formulas trong calc sheets (đặc biệt: heat load, sprinkler density, cable sizing)
- ✅ LUÔN LUÔN apply consistent styling: header navy #0F3460, section blue #E8F4FD, formula red #E94560
- ✅ LUÔN LUÔN hỏi user confirm Design Brief trước khi bắt đầu tính toán
- ⚠️ Nếu user chỉ cần 1 hệ thống cụ thể → giảm scope — chỉ tạo files liên quan

## Standards Reference

| Hệ thống | Tiêu chuẩn chính |
|-----------|-----------------|
| HVAC - Outdoor Air | ASHRAE 62.1 |
| HVAC - Cooling Load | TCVN 5687-2010 |
| Fire Fighting - Sprinkler | TCVN 7336:2021, FM Global DS 2-0 |
| Fire Fighting - Hydrant | TCVN 2622, QCVN 06:2022 |
| Plumbing - Fixtures | ASPE Vol.2-2010 |
| Electrical - Load | IEC 60364, TCVN 7447 |
| Electrical - Lighting | QCVN 22:2016/BYT |

## Deliverables Checklist

| # | File | Phase | Sheets |
|---|------|-------|--------|
| 1 | `Roombook_{PROJECT}.xlsx` | 1.1 | 1 (MECHANICAL ROOM MATRIX) |
| 2 | `Calc_HVAC_{PROJECT}.xlsx` | 1.2 | 2 (Outdoor Air + Heat Load) |
| 3 | `Calc_PCCC_{PROJECT}.xlsx` | 1.2 | 3 (FF System + Hydrant + Sprinkler) |
| 4 | `Calc_Plumbing_{PROJECT}.xlsx` | 1.2 | 1 (ASPE Fixtures + Pump) |
| 5 | `Calc_Electrical_{PROJECT}.xlsx` | 1.2 | 3 (Load + Cable + Lighting) |
| 6 | `Equipment_List_{PROJECT}.xlsx` | 1.3 | 3 (Fan + AHU + Pump) |
| 7 | `Drawing_List_{PROJECT}.xlsx` | 2.1 | 1 |
| 8 | `Project_Outline_{PROJECT}.xlsx` | 2.2 | 2 (Info + Checklist) |
| 9 | `Spec_Compare_{PROJECT}.xlsx` | 2.3 | 1 |
| 10 | `BoQ_{PROJECT}.xlsx` | 3.1 | 4 (HVAC + FF + Plumbing + Elec) |
| 11 | `Final_Quotation_{PROJECT}.xlsx` | 3.2 | 1 (Summary + VAT) |

---

📦 Generated by Skill Generator v4.0
