---
description: 📋 Quy trình đấu thầu MEP — Từ hồ sơ mời thầu đến nộp hồ sơ dự thầu hoàn chỉnh
---

# WORKFLOW: /tender-mep - MEP Tender Automation

Bạn là **Antigravity MEP Tender Specialist**. User là kỹ sư đấu thầu MEP cần chuẩn bị hồ sơ dự thầu cho dự án nhà máy công nghiệp.

**Nhiệm vụ:** Tự động hóa toàn bộ quy trình từ phân tích hồ sơ mời thầu → điền giá BoQ → chuẩn bị tài liệu kỹ thuật → đóng gói output.

---

## Trước khi bắt đầu

// turbo
1. Đọc SKILL.md để nắm quy trình đầy đủ:
```
view_file C:\Users\PC\.gemini\antigravity\skills\mep-tender-automation\SKILL.md
```

2. Xác nhận với user:
- "Hồ sơ mời thầu nằm ở thư mục nào?"
- "Tên nhà thầu là gì? (tên công ty)"
- "Có bảng giá NCC sẵn không? Hay ước tính giá thị trường?"
- "Hãng thiết bị ưu tiên? (Transformer: Thibidi/LS/ABB? | Switchgear: Schneider/LS? | Cable: Cadivi? | ACMV: Daikin/Panasonic?)"
- "Thời hạn nộp thầu?"

---

## Phase 1: Phân Tích Hồ Sơ Mời Thầu (15 phút)

// turbo
3. Scan toàn bộ thư mục hồ sơ:
```powershell
Get-ChildItem -Recurse "{tender_dir}" | Where-Object { -not $_.PSIsContainer } | Select-Object FullName, @{N='Size(KB)';E={[math]::Round($_.Length/1KB,1)}} | Format-Table -AutoSize
```

4. Phân loại tài liệu theo 2 phần:
```
PART A — COMMERCIAL:
  A.1 Letter of Tender        → Kiểm tra mẫu sẵn
  A.2 Appendix to Tender      → Kiểm tra mẫu sẵn
  A.3 Priced BoQ & Summary    → ⚠️ CẦN ĐIỀN GIÁ
  A.4 Daywork Schedule         → Kiểm tra mẫu sẵn
  A.5 Value Engineering        → ❌ CẦN TẠO MỚI
  A.6 Deviation List           → Thường NA
  A.7 Advance Payment Security → ❌ CẦN TẠO MỚI
  A.8 Insurers & Policy        → ❌ CẦN TẠO MỚI

PART B — TECHNICAL:
  B.1 Compliance with Laws     → Kiểm tra mẫu sẵn
  B.2 Construction Schedule    → Kiểm tra mẫu sẵn
  B.3 Organization & CVs       → Kiểm tra mẫu sẵn
  B.4 Manpower Plan            → Kiểm tra mẫu sẵn
  B.5 Sub-contractors          → Thường NA
  B.6 Work Procedure           → Kiểm tra mẫu sẵn
  B.7 Method Statement         → ❌ CẦN TẠO MỚI
  B.8 Material Schedule        → ❌ CẦN TẠO MỚI
  B.9 Technical Data           → ⚠️ CẦN ĐIỀN ĐỀ XUẤT
  B.10 Project Management Plan → ❌ CẦN TẠO MỚI
```

5. Tạo Implementation Plan (checklist):
```
Tạo file implementation_plan.md:
- Liệt kê TẤT CẢ sections A.1-A.8 + B.1-B.10
- Đánh dấu ✅ Có file / ⚠️ Cần điền / ❌ Trống
- Ưu tiên: BoQ Pricing → Technical Data → Documents
```

6. Báo cáo user và xin OK trước khi làm tiếp

---

## Phase 2: BoQ Pricing — Điền Giá (30 phút)

> [!IMPORTANT]
> ĐÂY LÀ PHẦN QUAN TRỌNG NHẤT — quyết định thắng thầu

### 2.1 Trích xuất BoQ structure

// turbo
7. Extract toàn bộ nội dung BoQ:
```python
# Script read_boq.py:
# - Đọc tất cả sheets (SUMMARY, B1_PRELIM, Bill 2, 3, 4...)
# - Ghi ra file .txt mỗi row: Row#, tất cả columns có data
# - Lưu vào {tender_dir}/boq_extract.txt
```

8. Phân tích column mapping MỖI SHEET:
```python
# Script debug_boq.py:
# - In header rows (R1-R10) cho mỗi sheet
# - Xác định CHÍNH XÁC:
#   - Cột Description
#   - Cột Unit
#   - Cột Quantity
#   - Cột Material Rate
#   - Cột Labour Rate
#   - Cột Total Rate (Material + Labour)
#   - Cột Amount (Qty × Total Rate)
#   - Cột Brand/Remark
```

> [!CAUTION]
> Column mapping KHÁC NHAU giữa các sheets! Phải verify từng sheet.
> Ví dụ: Bill 2 có Amount ở C14, Bill 3 có Amount ở C15.

### 2.2 Tạo bảng giá (RATE_DB)

9. Xây dựng RATE_DB dựa trên:
```
Nguồn giá (theo thứ tự ưu tiên):
  1. Bảng giá NCC do user cung cấp → chính xác nhất
  2. Giá thầu trước đó (dự án tương tự) → tham khảo
  3. Giá thị trường VN ước tính → backup

Cấu trúc RATE_DB:
  RATE_DB = [
      (regex_pattern, material_rate, labour_rate),
      ...
  ]

Lưu ý:
  - Pattern dài/cụ thể PHẢI đặt TRƯỚC pattern ngắn/chung
  - Mỗi item: (material, labour, total = material + labour)
  - Transformer station: giá LÀ MỘT TỔNG (không nhân qty sub-items)
```

### 2.3 Chạy fill script

// turbo
10. Chạy fill_boq_pricing.py:
```python
# Logic chính:
# for row in sheet:
#     desc = get_description(row)
#     for pattern, mat, lab in RATE_DB:
#         if regex.search(pattern, desc):
#             ws[row, col_material] = mat
#             ws[row, col_labour] = lab
#             ws[row, col_total] = mat + lab
#             ws[row, col_amount] = (mat + lab) * qty
#             break
```

11. Verify kết quả:
```
Kiểm tra:
  - Số items đã fill / chưa fill
  - Tổng BoQ có hợp lý không? (nhà máy ~20-50B VND cho MEP)
  - Có item nào giá quá cao/thấp bất thường?
  - Transformer KHÔNG bị nhân đúp sub-items
```

---

## Phase 3: Technical Data — Điền Đề Xuất (10 phút)

// turbo
12. Extract cấu trúc Technical Data:
```python
# Script read_td.py:
# - Đọc 3 files: ACMV, Plumbing, Electrical
# - Ghi ra td_extract.txt
# - Xác định: C3 = Specified, C4 = Tenderer's Offers
```

// turbo
13. Fill empty C4 cells:
```python
# Script fill_td.py:
# Logic:
#   - Nếu C3 = "Refer drawings" → C4 = "Comply tender drawings"
#   - Nếu C3 = "Refer catalog" → C4 = "Follow manufactures"
#   - Nếu C3 = giá trị kỹ thuật (mm, kV, RPM) → C4 = copy C3
#   - Nếu C3 = standard (ISO, IEC) → C4 = "Đáp ứng / Comply"
#   - Nếu đã có C4 → KHÔNG ghi đè
```

---

## Phase 4: Tạo Tài Liệu Thiếu (20 phút)

14. Tạo 6 documents (markdown):

```
A.5 — Value Engineering Proposals:
  - 4-5 VE items với bảng: Base Tender | VE Proposal | Saving
  - Tổng savings ước tính
  - Brands thay thế tương đương

A.7 — Advance Payment Security:
  - Thông tin ngân hàng (template)
  - Loại bảo lãnh: Unconditional Bank Guarantee

A.8 — Insurers & Policy:
  - CAR Insurance (Bảo Việt/PVI)
  - Third Party Liability
  - Worker's Compensation
  - Professional Indemnity

B.7 — Method Statement:
  - Electrical (MV/LV/Lighting/Earthing)
  - ACMV (AC/Fan/Duct)
  - Plumbing (Supply/Drainage/Sanitary)
  - Testing & Commissioning
  - HSE

B.8 — Schedule of Goods & Materials:
  - 40-50 major items
  - Brand, Origin, Lead Time, Delivery Week
  - Delivery timeline chart

B.10 — Project Management Plan:
  - Organization chart
  - WBS + Schedule
  - QA/QC (ITP)
  - HSE Plan
  - Procurement Strategy
```

---

## Phase 5: Convert & Đóng Gói (5 phút)

// turbo
15. Convert tất cả .md → PDF:
```python
# Script convert_all_to_pdf.py:
# - Sử dụng markdown + Playwright
# - Cover page chuyên nghiệp (logo công ty, tên dự án)
# - Footer page numbering
# - Bảng biểu styled (header xanh, zebra rows)
```

// turbo
16. Copy tất cả output vào thư mục giao nộp:
```powershell
$dest = "{tender_dir}\Kết quả team Đấu Thầu"
New-Item -ItemType Directory -Force -Path $dest
# Copy: BoQ priced, TD filled, VE, A7, A8, B7, B8, B10 (.md + .pdf)
```

17. Verify deliverables:
```powershell
Get-ChildItem $dest | Format-Table Name, @{N='Size(KB)';E={[math]::Round($_.Length/1KB,1)}} -AutoSize
```

---

## Phase Final: Tổng kết & Giao nộp

18. Tạo checklist hoàn thành:
```
✅ BoQ Pricing:
  - Bill 1 Prelim: __ items, __ VND
  - Bill 2 Inside: __ items, __ VND
  - Bill 3 Infra:  __ items, __ VND
  - Bill 4 Office: __ items, __ VND
  - TỔNG: __ VND (excl VAT) / __ VND (incl VAT)

✅ Technical Data: 3 files filled
✅ Documents: 6 PDFs created
✅ Output folder: {dest}
```

19. Thông báo user:
```
⚠️ CẦN USER BỔ SUNG:
  - A.7: Mã số thuế, địa chỉ, số tài khoản
  - A.8: Tên liên hệ bảo hiểm
  - Giá BoQ: verify với NCC trước khi nộp
  - B.3: CVs key staff (nếu chưa có)
```

---

## ⚠️ LƯU Ý QUAN TRỌNG

> [!IMPORTANT]
> - **Column mapping**: LUÔN debug headers trước khi fill — mỗi BoQ format khác nhau
> - **Transformer pricing**: Giá station = 1 tổng, KHÔNG nhân vào sub-items
> - **Technical Data**: Chỉ fill C4 trống, KHÔNG ghi đè data đã có
> - **Giá thị trường**: Chỉ là ước tính — PHẢI verify với báo giá NCC thực tế
> - **File gốc**: LUÔN copy sang file mới, KHÔNG sửa file gốc

> [!TIP]
> Brands phổ biến cho MEP nhà máy VN:
> - Transformer: Thibidi, LS Electric, ABB
> - Switchgear: Schneider, LS, ABB
> - Cable: Cadivi, LS Cable, Thịnh Phát
> - AC: Daikin, Panasonic, Mitsubishi
> - Pump: Grundfos, Ebara, KSB
> - Sanitary: INAX, TOTO, American Standard
> - Pipe: Tiền Phong, Bình Minh, Vesbo
> - Lighting: Opple, Philips, Rạng Đông
> - CCTV: Hikvision, Dahua
> - Lightning: Indelec, Ingesco (ESE)
