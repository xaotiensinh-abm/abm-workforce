---
description: 🏗️ Thiết kế MEP cho nhà máy công nghiệp (HVAC, PCCC, Cấp thoát nước, Điện)
---

# WORKFLOW: /mep-project - MEP Design Automation

Bạn là **Antigravity MEP Engineer**. User là kỹ sư thiết kế MEP cần tạo hồ sơ thiết kế cho dự án nhà máy.

**Nhiệm vụ:** Tự động hóa toàn bộ quy trình từ trích xuất hồ sơ → tính toán → bảng vẽ → bóc khối lượng → báo giá.

---

## Trước khi bắt đầu

// turbo
1. Đọc SKILL.md để nắm quy trình đầy đủ:
```
view_file C:\Users\PC\.gemini\antigravity\skills\mep-design-automation\SKILL.md
```

2. Xác nhận với user:
- "Tên dự án và vị trí?"
- "Hồ sơ đầu vào ở đâu? (thư mục chứa PDF/Excel)"
- "Có template nội bộ công ty không? (ví dụ thư mục 02.TÍNH TOÁN)"
- "Scope: HVAC + PCCC + Plumbing + Electrical hay chỉ 1 phần?"

---

## Phase 0: Đầu Vào (5 phút)

// turbo
3. Trích xuất toàn bộ PDF:
```bash
python {project_dir}/extract_project_docs.py
```

4. Nếu có template nội bộ, trích xuất cấu trúc:
```bash
python {project_dir}/extract_templates.py
```

5. Tạo DESIGN-BRIEF.md + DESIGN-CRITERIA.md từ dữ liệu extracted

---

## Phase 1: Tính Toán (15 phút)

// turbo
6. Tạo Roombook:
```bash
python {project_dir}/create_roombook.py
```
- Output: `Roombook_{PROJECT}.xlsx` (MECHANICAL ROOM MATRIX)
- Kiểm tra: đủ phòng, đủ cột, dữ liệu hợp lý

// turbo
7. Tạo Bảng Tính HVAC:
```bash
python {project_dir}/create_calc_hvac.py
```
- Output: `Calc_HVAC_{PROJECT}.xlsx`
- Sheet 1: Outdoor Air Flow (ASHRAE 62.1)
- Sheet 2: Heat Load Calculated

// turbo
8. Tạo Bảng Tính PCCC + Plumbing + Equipment List:
```bash
python {project_dir}/create_calc_pccc_equip.py
```
- Output: `Calc_PCCC_{PROJECT}.xlsx`, `Calc_Plumbing_{PROJECT}.xlsx`, `Equipment_List_{PROJECT}.xlsx`

---

## Phase 2: Bản Vẽ + Phase 3: BoQ (10 phút)

// turbo
9. Tạo Drawing List + Project Outline + BoQ + Spec Compare:
```bash
python {project_dir}/create_phase2_3.py
```

// turbo
10. Tạo Calc Electrical + BoQ đầy đủ + Final Quotation:
```bash
python {project_dir}/create_final_all.py
```

---

## Phase Final: Verification

11. Kiểm tra tất cả file đã tạo:
```powershell
Get-ChildItem "{project_dir}\*.xlsx" | Select-Object Name, @{N='Size(KB)';E={[math]::Round($_.Length/1KB,1)}} | Format-Table
```

12. Xác nhận 11 files:
```
✅ Roombook_{PROJECT}.xlsx
✅ Calc_HVAC_{PROJECT}.xlsx
✅ Calc_PCCC_{PROJECT}.xlsx
✅ Calc_Plumbing_{PROJECT}.xlsx
✅ Calc_Electrical_{PROJECT}.xlsx
✅ Equipment_List_{PROJECT}.xlsx
✅ Drawing_List_{PROJECT}.xlsx
✅ Project_Outline_{PROJECT}.xlsx
✅ Spec_Compare_{PROJECT}.xlsx
✅ BoQ_{PROJECT}.xlsx
✅ Final_Quotation_{PROJECT}.xlsx
```

---

## ⚠️ NEXT STEPS:
```
1️⃣ Review file Excel → Mở và kiểm tra dữ liệu
2️⃣ Bổ sung data từ CAD → Cập nhật Roombook
3️⃣ Liên hệ NCC → Điền đơn giá thực tế vào BoQ
4️⃣ Vẽ CAD → Dựa theo Drawing List + Equipment List
```

---

## Lưu ý quan trọng

> [!IMPORTANT]
> - Luôn dùng **template nội bộ** thay vì tạo format generic
> - **Formulas Excel** được nhúng trực tiếp (không phải giá trị tĩnh)
> - Tiêu chuẩn VN: TCVN, QCVN. Quốc tế: ASHRAE, FM Global, NFPA, IEC
> - Đơn giá ước tính theo thị trường VN — cần cập nhật khi có giá NCC thực tế
