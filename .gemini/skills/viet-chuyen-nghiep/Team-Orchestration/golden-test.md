# Golden End-to-End Test — Pipeline write-new

## Mục đích
Kiểm tra toàn bộ pipeline v3.0 hoạt động đúng end-to-end.

---

## Test Case 1: Viết Blog 1200 từ

### Input (Brief từ User)
```
"Viết bài blog 1200 từ về 5 sai lầm phổ biến khi CEO ứng dụng AI vào doanh nghiệp.
Audience: CEO SME Việt Nam. 
Tone: Chuyên gia tư vấn, gần gũi.
Platform: LinkedIn."
```

### Bước 1: Ban Thu Thập (content/) ✅

**Expected output:**
```yaml
goi_nguyen_lieu:
  brief:
    loai: "blog"
    audience: "CEO SME Việt Nam"
    tone: "chuyên-gia-gần-gũi"
    do_dai: "1200 từ"
    platform: "linkedin"
  research:
    nguon:
      - {url: "...", tieu_de: "McKinsey AI Report 2025", do_tin_cay: "tier-1"}
      - {url: "...", tieu_de: "VnExpress AI Survey VN", do_tin_cay: "tier-2"}
    so_lieu_key:
      - {gia_tri: "70% dự án AI thất bại", nguon: "McKinsey", ngay: "2025"}
      - {gia_tri: "23% SME VN dùng AI", nguon: "VCCI", ngay: "2025"}
  analysis:
    angle: "Chia sẻ kinh nghiệm thực chiến, không lý thuyết suông"
    outline:
      - {section: "Hook", noi_dung: "Câu hỏi gây sốc + số liệu"}
      - {section: "Sai lầm 1-5", noi_dung: "Mỗi sai lầm = tình huống + giải pháp"}
      - {section: "Kết", noi_dung: "CTA tải checklist"}
```

**Checklist verify:**
- [ ] Có ít nhất 3 nguồn tier-1 hoặc tier-2
- [ ] Angle rõ ràng, không generic
- [ ] Outline có hook + body + CTA

### Bước 2: Ban Biên Tập (style/) ✅

**BTV cần kích hoạt:**
- `storytelling.md` → hook mở đầu bằng tình huống thực
- `rhythm.md` → biến tấu câu ngắn/dài, punch line cuối mỗi sai lầm
- `technical.md` → thuật ngữ AI giải thích đúng cho CEO
- `presentation.md` → heading H2 cho mỗi sai lầm, bold key insight

**Checklist verify:**
- [ ] Hook 2 dòng đầu gây tò mò
- [ ] Mỗi sai lầm có ví dụ cụ thể (show, don't tell)
- [ ] Biến tấu câu: không quá 3 câu liên tiếp cùng độ dài
- [ ] Thuật ngữ AI không dùng jargon mà CEO không hiểu

### Bước 3: Ban Kiểm Duyệt (quality/) ✅

**6 kiểm tra chạy song song:**

| BTV | Expected Result |
|-----|----------------|
| punctuation.md | 0 lỗi dấu câu |
| capitalization.md | Viết hoa đúng tên riêng, đầu câu |
| natural.md | ≤ 2 tín hiệu "mùi dịch" |
| anti-ai.md | Score ≤ 30% (grade A hoặc B) |
| fact-check.md | 100% claims có nguồn tier-1/2 |
| consistency.md | Tone nhất quán, xưng hô "bạn" suốt bài |

**Expected phán quyết:**
```yaml
phan_quyet:
  ket_qua: "PASS"
  diem_tong: 82
```

**Nếu REVISE:**
- Ghi chú cụ thể: "Đoạn 3 anti-AI 45%, cần thay 'hơn nữa' → ví dụ cụ thể"
- Chuyển style/ → sửa → quality/ chạy lại

### Bước 4: Ban Xuất Bản (platform/) ✅

**BTV linkedin.md tối ưu:**
```yaml
xuat_ban:
  platform: "linkedin"
  content: "..." # Đã tối ưu: hook 2 dòng, 1300 ký tự max, CTA rõ
  metadata:
    do_dai: "1180 từ"
    hashtags: ["#AIforBusiness", "#CEOInsights", "#DigitalTransformation"]
    format: "text"
  quality_stamp:
    diem: 82
    anti_ai: "B"
    verified: true
```

**Checklist verify:**
- [ ] Hook 2 dòng đầu xuất hiện trước "see more"
- [ ] Có hashtag liên quan
- [ ] CTA cuối bài rõ ràng

---

## Test Case 2: Chấm Bài (grade-content)

### Input
```
"Chấm bài marketing 800 từ về cloud computing theo thang 100"
```

### Expected Pipeline
```
content/ (light) → quality/ (rubric mode)
```

### Expected Output
```yaml
phan_quyet:
  ket_qua: "GRADED"
  diem_tong: 67
  chi_tiet:
    noi_dung_do_sau: 15/25
    cau_truc_logic: 16/20
    phong_cach: 12/20
    chinh_xac: 12/15
    anti_ai: 5/10
    format: 7/10
  nhan_xet: "Bài viết có nội dung tốt nhưng thiếu ví dụ cụ thể..."
  de_xuat: ["Thêm case study VN", "Giảm cụm từ AI-generated"]
```

---

## Regression Checklist

Sau mỗi thay đổi hệ thống, chạy lại:

- [ ] Test Case 1 (write-new → blog LinkedIn) — pipeline 4 Ban
- [ ] Test Case 2 (grade-content → rubric 100) — pipeline 2 Ban
- [ ] Test Case 3 (write-email → email sequence) — pipeline email ★
- [ ] Test Case 4 (write-curriculum → 5 modules) — pipeline curriculum ★
- [ ] Test Case 5 (write-guide → SOP onboarding) — pipeline guide ★
- [ ] Test Case 6 (write-meeting-minutes → biên bản họp) — pipeline meeting minutes ★
- [ ] REVISE loop: cố ý tạo bài anti-AI > 60% → verify quality/ reject → style/ sửa
- [ ] Escalation: cố ý brief mơ hồ → verify hệ thống hỏi user
- [ ] Email escalation: spam score > 5 → verify escalation to style/email ★
- [ ] Curriculum escalation: Bloom nhảy 2+ levels → verify escalation ★

---

## Test Case 3: Viết Email Sequence (write-email) ★ v3.1

### Input
```
"Viết chuỗi 3 email nurture cho khóa coaching AI.
Audience: CEO SME Việt Nam.
Tone: Chuyên gia tư vấn.
Mục đích: Nurture → đăng ký demo."
```

### Expected Pipeline
```
content/ (light) → style/ (email) → quality/ → platform/ (email)
```

### Bước kiểm tra
| Checkpoint | Expected |
|-----------|----------|
| BTV email.md activated | ✅ Subject line formulas applied |
| Sequence progression | Email 1 (awareness) → 2 (consideration) → 3 (CTA) |
| Spam trigger scan | 0 spam words from blacklist |
| CTA clarity | Mỗi email 1 CTA duy nhất, rõ ràng |
| Personalization tokens | [Tên], [Công ty] ở vị trí phù hợp |
| Platform optimization | Responsive layout, preheader text |

### Expected Output
```yaml
xuat_ban:
  platform: "email"
  content: "..." # 3 emails đã biên tập
  metadata:
    format: "email_sequence"
    subject_lines: ["...", "...", "..."]
  quality_stamp:
    diem: 85
    spam_score: 1
    verified: true
```

---

## Test Case 4: Viết Giáo Trình (write-curriculum) ★ v3.1

### Input
```
"Viết giáo trình 5 module về ứng dụng AI vào quản trị doanh nghiệp.
Audience: CEO/quản lý cấp trung.
Mỗi module 45 phút. Có bài tập + quiz."
```

### Expected Pipeline
```
content/ (deep) → style/ (curriculum + technical) → quality/ → platform/ (docs)
```

### Bước kiểm tra
| Checkpoint | Expected |
|-----------|----------|
| BTV curriculum.md activated | ✅ Bloom's Taxonomy mapping |
| Module progression | Remember → Understand → Apply → Analyze → Create |
| Assessment matrix | Quiz + Bài tập + Case study đúng level |
| Ratio check | 40% theory / 40% practice / 20% assessment |
| Module bridge | Mỗi module kết thúc với preview module sau |

### Expected Output
```yaml
xuat_ban:
  platform: "docs"
  content: "..." # 5 modules đầy đủ
  metadata:
    format: "pdf"
    do_dai: "5 modules"
  quality_stamp:
    diem: 80
    bloom_alignment: true
    verified: true
```

---

## Test Case 5: Viết SOP (write-guide) ★ v3.1

### Input
```
"Viết SOP quy trình onboarding nhân viên mới cho công ty tech 50 người.
Bao gồm checklist ngày 1, tuần 1, tháng 1."
```

### Expected Pipeline
```
content/ → style/ (technical + presentation) → quality/ → platform/ (docs)
```

### Bước kiểm tra
| Checkpoint | Expected |
|-----------|----------|
| BTV technical.md activated | ✅ Step-by-step numbering |
| SOP structure | Mục đích → Phạm vi → RACI → Quy trình → Biểu mẫu |
| Steps single action | Mỗi step = 1 action, verb đầu câu |
| Callout boxes | ⚠️ WARNING, 💡 TIP present |
| Troubleshooting | FAQ section cuối |
| Version tracking | Ngày + phiên bản header |

### Expected Output
```yaml
xuat_ban:
  platform: "docs"
  content: "..." # SOP đầy đủ
  metadata:
    format: "docx"
    do_dai: "15 steps"
    attachments: ["checklist_ngay1.md", "raci_matrix.md"]
  quality_stamp:
    diem: 82
    step_validation: true
    verified: true
```

---

## Test Case 6: Viết Biên Bản Cuộc Họp (write-meeting-minutes) ★ v3.2

### Input
```
"Viết biên bản cuộc họp review sprint tuần 11.
Người tham dự: Dũng (PM), Hà (Dev), Minh (QA), Lan (Design), Tuấn (DevOps).
Nội dung: review 8 story completed, 2 carry-over, demo feature login.
Action items:
- Hà fix bug #234, deadline thứ 4
- Minh viết test cho module payment, deadline thứ 6
- Tuấn deploy staging, deadline thứ 3
Rút kinh nghiệm: cần estimate chính xác hơn, demo nên có script."
```

### Expected Pipeline
```
content/ → style/ (technical + presentation) → meeting-minutes-worker
→ quality/ → platform/ (docs)
```

### Bước kiểm tra
| Checkpoint | Expected |
|-----------|----------|
| Input extraction | ✅ 5 người, 3 action items, 2 chủ đề thảo luận |
| Cấu trúc 6 mục | ✅ I→VI đầy đủ |
| Bảng action items | ✅ 3 dòng, mỗi dòng có: việc + người + deadline |
| Danh sách tham dự | ✅ 5 tên nhất quán giữa mục I và mục IV |
| Phần rút kinh nghiệm | ✅ 3 sub-section: đã tốt / cần cải thiện / định hướng |
| Bảng ký tên | ✅ 2 cột: người ghi + đại diện |
| Completeness check | ✅ Tất cả người trong action items có trong danh sách tham dự |

### Expected Output
```yaml
xuat_ban:
  platform: "docs"
  content: "..." # Biên bản 6 mục đầy đủ
  metadata:
    format: "docx"
    attendees: 5
    action_items: 3
  quality_stamp:
    diem: 85
    completeness: true
    verified: true
```
