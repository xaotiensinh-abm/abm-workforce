---
name: "Goal"
description: "Tự động hóa 80% công việc chuẩn bị hồ sơ dự thầu MEP cho dự án nhà máy công nghiệp tại Việt Nam — từ phân tích hồ sơ mời thầu, điền giá BoQ (300-500 items), fill Technical Data, tạo 6 tài liệu hỗ trợ,"
---

﻿---
name: MEP Tender Automation
description: Automate MEP tender process â€” from bid document analysis to submission packaging.
---
---

# Goal

> **Use this skill when:** MEP tender process automation or bid document analysis

Tự động hóa 80% công việc chuẩn bị hồ sơ dự thầu MEP cho dự án nhà máy công nghiệp tại Việt Nam — từ phân tích hồ sơ mời thầu, điền giá BoQ (300-500 items), fill Technical Data, tạo 6 tài liệu hỗ trợ, đến đóng gói hồ sơ sẵn sàng nộp — trong ~90 phút thay vì 3-5 ngày.

# Instructions

## Phase 1: Phân Tích Hồ Sơ Mời Thầu (15 phút)

1. Nhận thư mục hồ sơ mời thầu từ user — xác nhận có BoQ Excel + tài liệu HSMT
2. Scan toàn bộ file — phân loại theo Section A (Commercial) và Section B (Technical)
3. Tạo **Implementation Plan** — checklist đánh dấu ✅/⚠️/❌ cho từng mục A.1→A.8 + B.1→B.10
4. Hỏi user: tên công ty nhà thầu, hãng thiết bị ưu tiên
5. ✅ VERIFY: Xác nhận plan với user trước khi tiếp tục

**Output**: `implementation_plan.md`

## Phase 2: BoQ Pricing (30 phút)

6. Extract toàn bộ BoQ → `boq_extract.txt`
7. ⚠️ **CRITICAL**: Chạy debug script TRƯỚC KHI fill — mỗi BoQ có column mapping KHÁC NHAU:
   ```
   Bill 2: Material=C11, Labour=C12, Total=C13, Amount=C14
   Bill 3: Material=C12, Labour=C13, Total=C14, Amount=C15
   ```
8. Tạo debug script → `debug_headers.txt` (output to FILE, không terminal — tránh lỗi encoding Việt)
9. Xây dựng RATE_DB — sử dụng list of tuples (KHÔNG dùng dict — cần thứ tự pattern dài trước):
   ```python
   RATE_DB = [
       (r"MV cable 24kV.*3C-240", 750000, 50000),  # Cụ thể → trước
       (r"cable", 50000, 10000),                     # Chung → sau
   ]
   ```
10. ⚠️ **Transformer**: Giá trọn gói station — sub-items (MV panel, LV panel) ĐÃ BAO GỒM → không nhân đúp
11. Chạy fill script → `*-PRICED.xlsx`
12. ✅ VERIFY: Kiểm tra tổng, đếm unfilled items, so sánh với benchmark (~95% match)

**Output**: `*-PRICED.xlsx` + `boq_extract.txt` + `debug_headers.txt`

### Bảng giá tham khảo (VN 2025)

| Hạng mục | Material (VND) | Labour (VND) | Unit |
|----------|---------------|-------------|------|
| MV cable 24kV 3C-240mm² | 750,000 | 50,000 | m |
| Transformer 2000kVA kiosk | 2,200,000,000 | 200,000,000 | set |
| MSB 4000A | 350,000,000 | 30,000,000 | set |
| Cable LV CXV 1C-300mm² | 280,000 | 20,000 | m |
| LED Highbay 100W | 850,000 | 50,000 | ea |
| Split AC 12kBTU | 6,500,000 | 350,000 | ea |
| PPR PN10 D25 | 35,000 | 12,000 | m |
| HDPE PE100 D100 | 85,000 | 15,000 | m |
| WC (INAX floor mount) | 2,800,000 | 150,000 | ea |
| IP Camera 2MP | 2,200,000 | 150,000 | ea |

> Giá ước tính thị trường VN 2025. Cần verify với báo giá NCC thực tế.

## Phase 3: Technical Data Fill (10 phút)

13. Extract cấu trúc TD files: `Row → C1=NO | C2=Description | C3=Specified | C4=Tenderer's Offers`
14. Fill C4 theo logic:
    - `C3` = "refer drawings" → C4 = "Comply tender drawings"
    - `C3` = "refer catalog" → C4 = "Follow manufactures"  
    - `C3` = giá trị kỹ thuật → copy C3
    - `C3` = standard (ISO/IEC) → "Đáp ứng / Comply"
15. Lưu `*-FILLED.xlsx`

**Output**: 3 files TD-FILLED (ACMV, Plumbing, Electrical)

## Phase 4: Tạo Tài Liệu Hỗ Trợ (20 phút)

16. Tạo 6 tài liệu markdown theo template:
    - A.5 Value Engineering (VE Proposals)
    - A.7 Advance Payment Security
    - A.8 Insurance Information
    - B.7 Method Statement MEP
    - B.8 Material Schedule + Delivery Timeline
    - B.10 Project Management Plan
17. Nếu thiếu thông tin → đánh dấu `[USER INPUT REQUIRED]` và liệt kê cuối

## Phase 5: Convert & Đóng Gói (5 phút)

18. Convert MD → HTML → PDF (Playwright, A4, Inter font, cover page chuyên nghiệp)
19. Apply CSS: header navy #0F3460, table styling, page breaks
20. Thêm cover page với logo bar + project name + date

## Phase 6: Giao Nộp (5 phút)

21. Tổng hợp tất cả vào thư mục output:
    ```
    📁 Kết quả Đấu Thầu/
    ├── *-BOQ-PRICED.xlsx
    ├── TECHNICAL DATA_*-FILLED.xlsx (3 files)
    ├── VE-Proposals.pdf + 5 tài liệu PDF
    └── 6 file .md gốc
    ```
22. Liệt kê items cần user bổ sung (mã số thuế, CVs, verify giá NCC)
23. ✅ VERIFY: Đếm file output, kiểm tra tổng giá BoQ hợp lý

# Examples

## Ví dụ 1: Gói thầu nhà máy Core5 Hai Phong II (~30 tỷ VND)

**Input:**
```
User: Em có hồ sơ mời thầu cho gói MEP nhà máy Core5 Hải Phòng.
      Thư mục: D:\Projects\Core5-HP2\HSMT\
      Công ty: Thăng Tiến Construction
      Hãng ưu tiên: Daikin (HVAC), Schneider (điện)
```

**Thought Process:**
- Scan thư mục → tìm BoQ.xlsx + 3 TD files + Spec docs
- Phân loại A/B sections → tạo implementation plan
- BoQ: 4 bills (Electrical, ACMV, Plumbing, PCCC) × ~80 items = ~320 items
- Debug columns → Bill 2 khác Bill 3 → cần 2 RATE_DB patterns

**Output (rút gọn):**
```
✅ Phase 1: Implementation Plan — 18 mục checked
✅ Phase 2: BoQ-PRICED.xlsx — 305/320 items filled (95.3%)
   Tổng giá: 28.5 tỷ VND (Material: 22.1B + Labour: 6.4B)
   15 items cần manual review (merged cells, custom items)
✅ Phase 3: 3 TD-FILLED.xlsx — 100% sections filled
✅ Phase 4: 6 tài liệu MD created
✅ Phase 5: 6 PDF generated (cover page + formatting)
✅ Phase 6: 16 files đóng gói sẵn sàng nộp

⚠️ User cần bổ sung:
- Mã số thuế, số tài khoản → A.7
- CVs key staff (PM, Site Eng, QC) → B.3
- Verify giá Transformer 2000kVA với NCC
```

## Ví dụ 2: Edge Case — BoQ format lạ (merged cells, columns khác)

**Input:**
```
User: BoQ này format JLL, columns rất khác, em fill sai hết rồi
```

**Thought Process:**
- JLL format: columns không chuẩn → PHẢI chạy debug trước
- Merged cells → openpyxl cần unmerge trước khi ghi
- Output debug_headers.txt → xác định đúng column mapping

**Output:**
```
⚠️ Phát hiện: JLL format — columns khác hoàn toàn
   Bill 1: Rate=C8, Amount=C9 (thay vì C11/C14 thông thường)
   Merged cells: rows 1-5 mỗi sheet
   
→ Đã unmerge + remap columns
→ Rerun fill script với RATE_DB adjusted
→ Kết quả: 280/295 items filled (94.9%)
```

# 🔴 ANTI-HALLUCINATION RULES (v2.0 — SCHUTZ Lessons Learned)

> BÀI HỌC: AI tự sinh brands (Panasonic thay ABB), tự tạo giá,
> bịa lead times → BoQ sai, VE proposals vô nghĩa. RULES DƯỚI ĐÂY BẮT BUỘC.

## RULE TH-1: APPROVED MAKERS ONLY
- 🔴 **TUYỆT ĐỐI CẤM** tự đặt tên hãng thiết bị
- ✅ **BẮT BUỘC** dùng danh sách Approved Makers từ Specification
- ✅ Nếu spec không có maker list → ghi "Subcontractor propose" hoặc hỏi user

## RULE TH-2: PRICE FROM DATABASE, KHÔNG TỰ SINH
- 🔴 **CẤM** bịa giá — mọi unit price PHẢI từ RATE_DB hoặc báo giá NCC
- ✅ Nếu không tìm được giá match → ghi `0` + flag `[NEED MANUAL PRICING]`
- ✅ Ghi rõ nguồn giá: "Market est. 2025" hoặc "NCC quotation [date]"

## RULE TH-3: LEAD TIME FROM SUPPLIER
- 🔴 **CẤM** bịa thời gian giao hàng
- ✅ Lead time PHẢI từ NCC quote hoặc kinh nghiệm dự án trước
- ✅ Nếu không có → ghi "TBD — confirm with supplier"

## RULE TH-4: VE PROPOSALS MUST BE VIABLE
- 🔴 **CẤM** đề xuất VE không thể thực hiện (ví dụ: thay busduct = cable khi spec chỉ định busduct)
- ✅ Mỗi VE item PHẢI có: tiết kiệm ước tính, lý do kỹ thuật, rủi ro
- ✅ VE KHÔNG ĐƯỢC vi phạm tiêu chuẩn bắt buộc (TCVN, FM Global)

## RULE TH-5: MATERIALS LIST BINDING
- 🔴 **CẤM** BoQ ghi spec khác với Structured Data JSON
- ✅ BoQ items PHẢI match với `SCHUTZ_structured_data.json`
- ✅ Cable type, transformer spec, sprinkler standard → phải khớp 100%

# Constraints

- 🚫 KHÔNG ĐƯỢC fill BoQ mà chưa chạy debug column mapping — sai columns = tổng sai toàn bộ
- 🚫 KHÔNG ĐƯỢC dùng dict cho RATE_DB — phải dùng list of tuples (pattern dài trước)
- 🚫 KHÔNG ĐƯỢC nhân đúp giá Transformer — sub-items đã bao gồm trong giá station
- 🚫 KHÔNG ĐƯỢC output debug info ra terminal — lỗi encoding tiếng Việt → dùng file
- 🚫 KHÔNG ĐƯỢC bỏ qua merged cells — phải unmerge trước khi ghi giá
- ✅ LUÔN LUÔN verify tổng giá BoQ sau khi fill — so sánh với benchmark
- ✅ LUÔN LUÔN hỏi user xác nhận implementation plan trước khi điền giá
- ✅ LUÔN LUÔN đánh dấu `[USER INPUT REQUIRED]` cho thông tin thiếu
- ✅ LUÔN LUÔN tạo debug_headers.txt TRƯỚC KHI chạy fill script
- ⚠️ Giá tham khảo là ước tính 2025 — CẦN verify với báo giá NCC thực tế cho mỗi dự án

## Scripts Reference

| Script | Mục đích | Input | Output |
|--------|---------|-------|--------|
| `read_boq.py` | Extract BoQ structure | BoQ.xlsx | boq_extract.txt |
| `debug_boq.py` | Verify column mapping | BoQ.xlsx | debug_headers.txt |
| `fill_boq_pricing.py` | Fill prices vào BoQ | BoQ.xlsx + RATE_DB | *-PRICED.xlsx |
| `read_td.py` | Extract Technical Data | TD files | td_extract.txt |
| `fill_td.py` | Fill tenderer offers | TD files | *-FILLED.xlsx |
| `convert_all_to_pdf.py` | Batch MD→PDF | .md files | .pdf files |

> Scripts được tạo ad-hoc cho từng dự án. Cấu trúc BoQ khác nhau → script cần adjust.

## Lessons Learned (Core5 HP II)

1. **Column mapping sai** → Amount ghi vào cột Rate → tổng sai toàn bộ
2. **Transformer double-counting** → Sub-items bị nhân giá station
3. **Terminal encoding lỗi** → Tiếng Việt bị garbled → output to file
4. **Merged cells** → openpyxl đôi khi không ghi được → unmerge trước
5. **RATE_DB dict ordering** → dict không có thứ tự → dùng list of tuples

---

📦 Generated by Skill Generator v4.0
