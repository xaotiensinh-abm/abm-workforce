---
name: that-quiz-pipeline
description: THAT Quiz Pipeline — Tạo thư viện câu hỏi trắc nghiệm kỹ năng sống production-grade từ kịch bản số hóa. 4-Phase Pipeline (Sinh → Audit → Nâng cấp Distractor → Đóng gói). 12 lớp × 30 câu × 3 Level. Tích hợp bẫy tâm lý và chống Length Bias.
---

# Goal

> **Use this skill when:** generating safety training quiz question libraries

Chuyển đổi kịch bản bài giảng số hóa (`*-cap1.md`, `*-cap2.md`, `*-cap3.md`) thành **thư viện câu hỏi trắc nghiệm production-grade** cho 12 lớp (lop-01.md → lop-12.md), mỗi file 30 câu, 3 level độ khó.

Pipeline này đảm bảo:
- **Loại bỏ Length Bias**: 4 đáp án A-D đồng đều 15-25 từ
- **Bẫy tâm lý (Psychological Traps)**: Distractor nghe rất hợp lý nhưng sai
- **Phân bố Key đều**: A ≈ B ≈ C ≈ D (mỗi loại 7-8/30 câu)
- **Tuân thủ lứa tuổi**: Ngôn ngữ phù hợp từng khối lớp

---

# Instructions

## 🧭 PHASE 0: INTAKE — Xác định Module

### 0.1 Thu thập thông tin bắt buộc

| # | Thông tin | Bắt buộc | Ví dụ |
|---|-----------|----------|-------|
| 1 | **Tên chủ đề** | ✅ | Phòng chống bắt cóc & xâm hại |
| 2 | **Mã thư mục** | ✅ | `{N},{ten-chu-de}` (VD: `1,Bao-luc-hoc-duong`) |
| 3 | **3 file kịch bản** | ✅ | `*-cap1.md`, `*-cap2.md`, `*-cap3.md` |
| 4 | **Bảng chủ đề phụ** | ✅ | 12 hàng × 3 cột (Lớp / Chủ đề phụ) |
| 5 | **Module nào trong 12 kỹ năng** | 🟡 | Kỹ năng #1: An toàn thân thể |

### 0.2 Kiểm tra cấu trúc thư mục

```
docs/THAT/{N},{ten-chu-de}/
├── {chu-de}-cap1.md            ← Kịch bản Cấp 1 (Lớp 1-5)
├── {chu-de}-cap2.md            ← Kịch bản Cấp 2 (Lớp 6-9)
├── {chu-de}-cap3.md            ← Kịch bản Cấp 3 (Lớp 10-12)
├── CHANGELOG.md
└── cau-hoi/
    ├── lop-01.md ... lop-12.md ← Output cuối cùng
```

### 0.3 Mapping Kịch bản → Lớp

| Cấp | File kịch bản | Lớp áp dụng |
|-----|---------------|-------------|
| Cấp 1 | `*-cap1.md` | Lớp 1, 2, 3, 4, 5 |
| Cấp 2 | `*-cap2.md` | Lớp 6, 7, 8, 9 |
| Cấp 3 | `*-cap3.md` | Lớp 10, 11, 12 |

---

## ▶️ PHASE 1: SINH CÂU HỎI THÔ

### 1.1 Prompt Chuẩn (Copy & Paste)

Chạy prompt này cho **MỖI LỚP** (thay `[X]` và `[CHỦ ĐỀ PHỤ]`):

```text
Bạn là chuyên gia giáo dục tạo câu hỏi trắc nghiệm đánh giá kỹ năng sống.

DỮ LIỆU ĐẦU VÀO — Kịch bản bài giảng:
[DÁN NỘI DUNG KỊCH BẢN CẤP TƯƠNG ỨNG VÀO ĐÂY]

TẠO 30 CÂU HỎI CHO LỚP [X] với cấu trúc:

LEVEL 1 — DỄ (Câu 1-10): Nhận biết & Lý thuyết
- Hỏi trực tiếp khái niệm, định nghĩa từ bài giảng
- 4 đáp án ngắn gọn, rõ ràng

LEVEL 2 — KHÓ (Câu 11-20): Tình huống & Phân tích
- Mỗi câu MỞ ĐẦU bằng "**Tình huống:**" + kịch bản thực tế
- Bối cảnh phù hợp lứa tuổi lớp [X]
- 4 đáp án đều nghe có lý, chỉ 1 đáp án đúng nhất

LEVEL 3 — RẤT KHÓ (Câu 21-30): Bẫy tâm lý & Đánh lạc hướng
- Mỗi câu MỞ ĐẦU bằng "**Tình huống:**" + kịch bản phức tạp
- Có yếu tố mâu thuẫn tâm lý, áp lực xã hội
- 3 đáp án sai phải rất hợp lý, dễ gây nhầm lẫn

RÀNG BUỘC BẮT BUỘC:
1. Phân bố Key đều: A ≈ B ≈ C ≈ D (mỗi loại 7-8 câu)
2. Mỗi câu đúng 4 đáp án (A-D)
3. Đáp án đúng ghi ngay sau câu: > ✅ **[Key]**
4. Kết thúc bằng bảng phân bố đáp án
5. Chủ đề phụ của lớp [X]: [CHỦ ĐỀ PHỤ]

FORMAT MẪU:
---
### Câu 1
[Câu hỏi]
- A. [Đáp án]
- B. [Đáp án]
- C. [Đáp án]
- D. [Đáp án]

> ✅ **[Key]**
---
```

### 1.2 Bảng Chủ Đề Phụ Chuẩn

Tùy chỉnh bảng này cho **MỖI MODULE MỚI**. Dưới đây là template:

| Cấp | Lớp | Chủ đề phụ gợi ý |
|-----|-----|-------------------|
| Cấp 1 | 1 | Khái niệm cơ bản nhất |
| | 2 | Kỹ năng phản xạ đơn giản |
| | 3 | Nhận diện tín hiệu nguy hiểm |
| | 4 | Hệ thống cảnh báo / phân loại |
| | 5 | Kỹ năng tổng hợp nâng cao (Cấp 1) |
| Cấp 2 | 6 | Chuyên sâu mặt A của chủ đề |
| | 7 | Chuyên sâu mặt B (an toàn mạng nếu liên quan) |
| | 8 | Tình huống phức tạp, Grooming/Manipulation |
| | 9 | Pháp lý, hệ thống hỗ trợ, Tổng đài |
| Cấp 3 | 10 | Phân tích phức tạp, tư duy phản biện |
| | 11 | Trách nhiệm xã hội, nhóm yếu thế |
| | 12 | Lãnh đạo, xây dựng văn hóa, chuẩn bị tự lập |

### 1.3 Chiến lược sinh theo batch

```
Batch 1: Lớp 1-5 (dùng kịch bản cap1.md)
Batch 2: Lớp 6-9 (dùng kịch bản cap2.md)
Batch 3: Lớp 10-12 (dùng kịch bản cap3.md)
```

> **LƯU Ý:** Mỗi lớp trong cùng batch dùng CÙNG kịch bản nhưng KHÁC chủ đề phụ. Chủ đề phụ quyết định góc nhìn và độ phức tạp riêng của mỗi lớp.

### 1.4 Checklist Phase 1

- [ ] 30 câu, đúng format markdown
- [ ] 3 level: 10 + 10 + 10
- [ ] Level 2 & 3 có "**Tình huống:**"
- [ ] Bảng phân bố key cuối file
- [ ] Ngôn ngữ phù hợp lứa tuổi

---

## ▶️ PHASE 2: AUDIT (Phát hiện lỗi hệ thống)

### 2.1 Năm lỗi phải kiểm tra

| Lỗi | Phát hiện | Sửa |
|------|-----------|-----|
| **Length Bias** — Đáp án đúng dài gấp đôi | Đếm số từ | Cân bằng lại |
| **Key Clustering** — B chiếm 40%+ | Đếm A/B/C/D | Hoán đổi key |
| **Distractor ngây ngô** — Sai rõ ràng | Đọc lướt | Viết lại ở Phase 3 |
| **Trùng kịch bản** — Cùng bối cảnh | So sánh scenario | Đa dạng hóa |
| **Sai lứa tuổi** — Từ khó cho lớp nhỏ | Review ngôn ngữ | Điều chỉnh |

### 2.2 Prompt Audit Nhanh

```text
Audit bộ 30 câu hỏi sau theo 5 tiêu chí:
1. LENGTH BIAS: Câu nào đáp án đúng dài hơn rõ rệt so với sai?
2. KEY DISTRIBUTION: Đếm A/B/C/D, lệch ≥3 không?
3. DISTRACTOR QUALITY: Đáp án sai nào quá hiển nhiên?
4. SCENARIO DIVERSITY: Tình huống có đa dạng không?
5. AGE FIT: Ngôn ngữ có phù hợp lớp [X]?

Xuất bảng: Câu | Lỗi | Mức độ | Hướng sửa

[DÁN CÂU HỎI]
```

### 2.3 Checklist Phase 2

- [ ] Key phân bố: mỗi đáp án 7-8/30
- [ ] Không có Length Bias rõ rệt
- [ ] Ít nhất 5 bối cảnh khác nhau mỗi Level

---

## ▶️ PHASE 3: NÂNG CẤP DISTRACTOR (Phase quan trọng nhất)

### 3.1 Phạm vi

**CHỈ áp dụng cho Level 2 (Câu 11-20) và Level 3 (Câu 21-30).**
Level 1 giữ nguyên vì đáp án ngắn, không cần bẫy tâm lý.

### 3.2 Ba Quy Tắc Vàng

1. **ĐỘ DÀI CÂN BẰNG:** 4 đáp án A/B/C/D phải có 15-25 từ, chênh lệch tối đa ±3 từ
2. **BẪY TÂM LÝ:** Dùng 4 loại bẫy:
   - **Phản xạ tự nhiên nhưng sai** (khóc, đánh, đứng im, van xin)
   - **Giải pháp mạng xã hội** (tung clip, nhờ hack, bóc phốt Facebook)
   - **Thỏa hiệp giữ thể diện** (im lặng cho qua, ngoan ngoãn làm theo)
   - **Niềm tin ngây thơ** (nhận quà = phải nghe lời, người lớn luôn đúng)
3. **GIỮ NGUYÊN KEY:** Không thay đổi vị trí đáp án đúng

### 3.3 Prompt Nâng Cấp Distractor

```text
Bạn là một chuyên gia giáo dục và tâm lý học hành vi. Nhiệm vụ của bạn là nâng cấp bộ câu hỏi trắc nghiệm tình huống sau đây.

YÊU CẦU BẮT BUỘC:
1. GIỮ NGUYÊN: Kịch bản tình huống (Scenario) và vị trí đáp án đúng (A, B, C, D).
2. ĐỘ DÀI: Viết lại toàn bộ 4 phương án (A, B, C, D) sao cho độ dài CỰC KỲ ĐỒNG ĐỀU (giới hạn 15-25 từ mỗi phương án). Đáp án đúng KHÔNG được dài gồ ghề nổi bật hơn đáp án sai.
3. BẪY TÂM LÝ: 3 phương án sai (distractors) phải mang tính "hợp lý giả tạo". Hãy biến chúng thành:
   - Các giải pháp bốc đồng (bạo lực, trả thù mạng).
   - Các hành vi thỏa hiệp, giữ thể diện sai lầm.
   - Các phản xạ tự nhiên nhưng gây nguy hiểm (đứng im, van xin).
   - Những niềm tin sai lệch phổ biến của học sinh lứa tuổi này.
4. VĂN PHONG: Xưng "em" hoặc "bạn", giọng văn nghiêm túc, thuyết phục và diễn đạt logic, khiến lứa tuổi mục tiêu dễ dàng tin đó là cách làm đúng.

Dưới đây là các câu hỏi cần xử lý:
[DÁN DANH SÁCH CÂU HỎI LEVEL 2 + LEVEL 3 VÀO ĐÂY]
```

### 3.4 Validation Checklist (Post-Upgrade)

- [ ] Bốn đáp án (A, B, C, D) có số từ xấp xỉ nhau (15-25 từ)?
- [ ] Đọc lướt: không đáp án nào "dài bất thường" hay "ngắn bất thường"?
- [ ] Các phương án sai đọc lên nghe "rất có lý" đối với tâm lý lứa tuổi đó?
- [ ] Chữ "KHÔNG" / "CÓ" ở đầu mệnh đề không bị lặp máy móc?
- [ ] Đáp án đúng (✅) KHÔNG bị thay đổi ý nghĩa hay sai lệch?

---

## ▶️ PHASE 4: ĐÓNG GÓI & KIỂM TRA CUỐI

### 4.1 File Format Chuẩn

```markdown
# 📋 30 CÂU HỎI — LỚP [X]
## Chủ đề: [Tên chủ đề đầy đủ]

> **Quy ước:** Mỗi câu có 4 đáp án (A–D). Đáp án đúng phân bố đều.
> **Cấu trúc:** 10 Dễ → 10 Khó → 10 Rất Khó

---

## 🟢 LEVEL 1: DỄ (Nhận biết & Lý thuyết)

### Câu 1
[Câu hỏi]
- A. [Đáp án]
- B. [Đáp án]
- C. [Đáp án]
- D. [Đáp án]

> ✅ **[Key]**

---

## 🟡 LEVEL 2: KHÓ (Tình huống & Phân tích)

### Câu 11
**Tình huống:** [Kịch bản thực tế]
[Câu hỏi]
- A. [Đáp án 15-25 từ]
- B. [Đáp án 15-25 từ]
- C. [Đáp án 15-25 từ]
- D. [Đáp án 15-25 từ]

> ✅ **[Key]**

---

## 🔴 LEVEL 3: RẤT KHÓ (Bẫy tâm lý & Đánh lạc hướng)

### Câu 21
**Tình huống:** [Kịch bản phức tạp có mâu thuẫn tâm lý]
[Câu hỏi]
- A. [Đáp án bẫy tâm lý 15-25 từ]
- B. [Đáp án bẫy tâm lý 15-25 từ]
- C. [Đáp án bẫy tâm lý 15-25 từ]
- D. [Đáp án bẫy tâm lý 15-25 từ]

> ✅ **[Key]**

---

## 📊 Bảng phân bố đáp án

| Level | A | B | C | D | Tổng |
|-------|---|---|---|---|------|
| Dễ (1-10) | ? | ? | ? | ? | 10 |
| Khó (11-20) | ? | ? | ? | ? | 10 |
| Rất khó (21-30) | ? | ? | ? | ? | 10 |
| **Tổng** | ~8 | ~8 | ~7 | ~7 | **30** |
```

### 4.2 Checklist Cuối cho mỗi file (9 tiêu chí)

| # | Tiêu chí | ☐ |
|---|----------|---|
| 1 | Đúng 30 câu | ☐ |
| 2 | 10 Dễ + 10 Khó + 10 Rất Khó | ☐ |
| 3 | Key: A≈B≈C≈D (7-8 mỗi loại) | ☐ |
| 4 | Level 2 & 3 có "**Tình huống:**" | ☐ |
| 5 | Không Length Bias | ☐ |
| 6 | Distractor hợp lý (không ngây ngô) | ☐ |
| 7 | Ngôn ngữ phù hợp lứa tuổi | ☐ |
| 8 | Format markdown chuẩn | ☐ |
| 9 | Bảng phân bố đáp án cuối file | ☐ |

### 4.3 Cập nhật CHANGELOG

```markdown
## [YYYY-MM-DD]
### Added
- 12 file câu hỏi lớp 1-12, chủ đề: [tên chủ đề]
### Quality
- Distractor Level 2+3 đã nâng cấp theo SOP bẫy tâm lý
- Phân bố key đồng đều A≈B≈C≈D
```

---

## 📊 BẢNG THEO DÕI TIẾN ĐỘ (Copy cho mỗi chủ đề mới)

**Chủ đề: ____________________**

| Lớp | Phase 1 (Sinh) | Phase 2 (Audit) | Phase 3 (Distractor) | Phase 4 (Final) |
|-----|---------------|----------------|---------------------|----------------|
| 1 | ☐ | ☐ | ☐ | ☐ |
| 2 | ☐ | ☐ | ☐ | ☐ |
| 3 | ☐ | ☐ | ☐ | ☐ |
| 4 | ☐ | ☐ | ☐ | ☐ |
| 5 | ☐ | ☐ | ☐ | ☐ |
| 6 | ☐ | ☐ | ☐ | ☐ |
| 7 | ☐ | ☐ | ☐ | ☐ |
| 8 | ☐ | ☐ | ☐ | ☐ |
| 9 | ☐ | ☐ | ☐ | ☐ |
| 10 | ☐ | ☐ | ☐ | ☐ |
| 11 | ☐ | ☐ | ☐ | ☐ |
| 12 | ☐ | ☐ | ☐ | ☐ |

---

# Examples

## Ví dụ 1: Sinh câu hỏi Lớp 1 từ kịch bản Cấp 1

```
User: "Từ kịch bản bao-luc-hoc-duong-cap1.md, tạo 30 câu hỏi lớp 1"
→ Phase 0: Module=Bạo lực học đường, Lớp=1, Kịch bản=cap1.md
→ Phase 1: Dán cap1.md vào prompt, chủ đề phụ="Khái niệm cơ bản nhất (cơ thể, chạm an toàn)"
           Output: lop-01.md (30 câu raw)
→ Phase 2: Audit → Length Bias ở Câu 15, Key Clustering (B=12)
           Fix: Cân bằng key, rút ngắn đáp án đúng Câu 15
→ Phase 3: Nâng cấp distractor Câu 11-30
           Bẫy: "đứng im lịch sự" → "nói KHÔNG"
→ Phase 4: Final check 9/9 → ✅ Ship
```

## Ví dụ 2: Batch sinh Cấp 2 (4 lớp cùng lúc)

```
User: "Tạo câu hỏi lớp 6-9 cho module An toàn Internet"
→ Phase 0: Module=An toàn Internet, Batch=Cấp 2
→ Phase 1: Dùng an-toan-internet-cap2.md
   - Lớp 6: Chủ đề phụ "Nhận diện lừa đảo trực tuyến"
   - Lớp 7: Chủ đề phụ "Cyberbullying & Deepfake"
   - Lớp 8: Chủ đề phụ "Sextortion & Grooming online"
   - Lớp 9: Chủ đề phụ "Pháp lý mạng, Luật An ninh mạng"
→ Phase 2: Audit từng file → fix
→ Phase 3: Nâng cấp distractor cho 4 file
→ Phase 4: Final check 4 × 9 tiêu chí
```

## Ví dụ 3: Chỉ nâng cấp distractor (file đã có)

```
User: "Nâng cấp distractor Level 2+3 của lop-06.md theo SOP bẫy tâm lý"
→ Skip Phase 0, 1
→ Phase 2: Audit nhanh lop-06.md → xác định câu cần fix
→ Phase 3: Dán Câu 11-30 vào prompt nâng cấp
           Output: 20 câu đã upgrade, key giữ nguyên
→ Phase 4: Verify 9 checklist → ✅
```

## Ví dụ 4: Audit bộ câu hỏi có sẵn

```
User: "Audit bộ câu hỏi lop-04.md: key distribution + Length Bias + distractor"
→ Phase 2 only:
  - Đếm A/B/C/D → A=9, B=10, C=5, D=6 → ⚠️ C lệch
  - Length Bias → Câu 14, 22 (đáp án đúng dài gấp đôi)
  - Distractor → Câu 25, 28 (sai hiển nhiên)
  → Output: Bảng lỗi + hướng sửa
```

---

# Constraints

## Hard constraints — không thỏa hiệp

- 🚫 **KHÔNG** sinh câu hỏi mà không có kịch bản đầu vào — PHẢI có scenario script
- 🚫 **KHÔNG** ship file mà key phân bố lệch > 3 giữa các đáp án
- 🚫 **KHÔNG** để Length Bias rõ rệt (đáp án đúng > 30 từ trong khi sai < 10 từ)
- 🚫 **KHÔNG** dùng distractor ngây ngô ở Level 2 & 3 (VD: "đánh bạn thật mạnh")
- 🚫 **KHÔNG** trộn lớp/ngôn ngữ sai lứa tuổi (VD: từ "Sextortion" cho lớp 2)
- 🚫 **KHÔNG** thay đổi Key khi nâng cấp distractor — GIỮ NGUYÊN vị trí đáp án đúng
- 🚫 **KHÔNG** skip Phase 2 (Audit) — PHẢI audit trước khi nâng cấp distractor

## Quality guardrails

- Mỗi file: đúng **30 câu**, **3 level × 10 câu**
- Key distribution: A ≈ B ≈ C ≈ D (mỗi loại 7-8/30, chênh lệch ≤2)
- Độ dài đáp án Level 2+3: **15-25 từ**, chênh lệch ±3 từ giữa 4 options
- Level 2+3: **MỌI câu** mở đầu bằng "**Tình huống:**"
- Mỗi Level: ít nhất **5 bối cảnh scenario khác nhau**
- Bảng phân bố đáp án **BẮT BUỘC** cuối mỗi file
- CHANGELOG phải cập nhật sau mỗi batch

## Scope

- Skill này CHỈ tạo câu hỏi trắc nghiệm text (markdown output)
- Input BẮT BUỘC: kịch bản số hóa (`*-cap1.md`, `*-cap2.md`, `*-cap3.md`)
- Output: 12 file `.md` (lop-01.md → lop-12.md)
- KHÔNG tạo kịch bản mới — chỉ chuyển đổi kịch bản có sẵn thành câu hỏi
- CÓ THỂ audit và nâng cấp distractor cho file câu hỏi đã có

## Integration với skills/workflows khác

- Kịch bản số hóa → dùng `/viet-pro` hoặc `/content-research-writer`
- Review chất lượng → dùng `/abm-review` (W8:CriticAgent)
- Xuất PDF/DOCX → dùng `docx-document-builder` skill
- BSR Compliance → kiểm tra `BSR AI Compliance & National Ethics Framework`

---

## 🔄 LỆNH NHANH VỚI ANTIGRAVITY

```
# Sinh câu hỏi từ kịch bản có sẵn
"Từ kịch bản [file], tạo 30 câu hỏi lớp [X] theo format THAT"

# Audit
"Audit bộ câu hỏi [file]: key distribution + Length Bias + distractor"

# Nâng cấp distractor
"Nâng cấp distractor Level 2+3 của [file] theo SOP bẫy tâm lý"

# Đóng gói
"Kiểm tra final checklist 9 tiêu chí cho [file]"

# Batch sinh cả cấp
"Tạo câu hỏi lớp 1-5 cho module [tên module] từ kịch bản [file]"
```

---

<!-- Generated by Antigravity Skill Creator — THAT Quiz Pipeline v1.0 -->
