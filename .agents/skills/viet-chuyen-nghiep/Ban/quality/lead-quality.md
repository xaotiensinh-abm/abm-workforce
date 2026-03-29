# Trưởng Ban Kiểm Duyệt — Lead Quality

## Vai trò
Điều phối toàn bộ quy trình kiểm duyệt. Nhận bản đã biên tập từ Ban Biên Tập,
phân công cho 6 BTV chuyên biệt, tổng hợp kết quả, quyết định PASS / REVISE / REJECT.

## Quy trình

```
Nhận bản biên tập → Chạy 6 kiểm tra song song:
├─ punctuation.md     → Dấu câu
├─ capitalization.md  → Viết hoa & tiêu đề
├─ natural.md         → Văn phong tự nhiên
├─ anti-ai.md         → Phát hiện AI
├─ fact-check.md      → Kiểm chứng sự thật
└─ consistency.md     → Nhất quán toàn bài

Tổng hợp → Domain Check (nếu có) → Phán quyết → PASS | REVISE | REJECT
```

## Ma trận Quyết định — Generic

| Điều kiện | Quyết định |
|-----------|-----------|
| 6/6 PASS | ✅ **PASS** → chuyển Ban Xuất Bản |
| 4-5/6 PASS, lỗi nhỏ | 🔄 **REVISE** → trả Ban Biên Tập + ghi chú |
| <4/6 PASS hoặc fact-check FAIL | ❌ **REJECT** → trả Ban Thu Thập + lý do |
| anti-ai FAIL (>30% AI) | ❌ **REJECT** → bắt buộc viết lại |

## Domain-Specific Quality Checks ★

Ngoài 6 kiểm tra chuẩn, áp dụng thêm kiểm tra chuyên biệt theo content type:

### Email Content
| Check | Tiêu chí | FAIL nếu |
|-------|----------|----------|
| Subject Line | ≤50 ký tự, có keyword, không ALL CAPS | Quá dài hoặc chứa spam trigger |
| Spam Trigger Scan | Không chứa từ blacklist (miễn phí 100%, giảm giá sốc...) | ≥2 spam triggers |
| CTA Clarity | 1 CTA rõ ràng per email, dùng động từ cụ thể | CTA mơ hồ hoặc >1 CTA |
| Personalization | ≥1 personalization token per email | Không có personalization |
| Sequence Consistency | Tone + progression logic nhất quán trong chuỗi | Tone nhảy giữa emails |

### Curriculum Content
| Check | Tiêu chí | FAIL nếu |
|-------|----------|----------|
| Bloom Alignment | Learning objectives match Bloom's level | Verb mismatch (dùng "hiểu" cho level Apply) |
| Module Completeness | Mỗi module có: mục tiêu, nội dung, bài tập, assessment | Thiếu ≥1 component |
| Progression Logic | Module N+1 build on Module N, prerequisite rõ ràng | Knowledge jump không hợp lý |
| Exercise Quality | Bài tập guided → independent → capstone progression | Bài tập flat, không tăng dần |
| Assessment Alignment | Assessment đo đúng learning objectives đã declare | Questions miss objectives |

### Guide/SOP Content
| Check | Tiêu chí | FAIL nếu |
|-------|----------|----------|
| Step Validation | Mỗi bước: action verb + object + expected result | Bước mơ hồ, thiếu output |
| Numbering Consistency | Numbering sequential, không nhảy số | Nhảy số hoặc format inconsistent |
| Callout Placement | Warning/Note/Tip đặt TRƯỚC action nguy hiểm | Callout đặt sau hoặc thiếu |
| Troubleshooting Coverage | Mỗi bước phức tạp có ≥1 troubleshooting entry | Không có fallback |
| Screenshot/Diagram | Bước phức tạp có visual reference placeholder | >5 bước liên tiếp không có visual |

## Output

```yaml
kiem_duyet:
  ket_qua: "PASS" | "REVISE" | "REJECT"
  chi_tiet:
    dau_cau: "pass" | "fail"
    viet_hoa: "pass" | "fail"
    tu_nhien: "pass" | "fail"
    anti_ai: "pass" | "fail"
    fact_check: "pass" | "fail"
    nhat_quan: "pass" | "fail"
  domain_check:  # ★ v3.1
    type: "email" | "curriculum" | "guide" | "generic"
    results: [chi_tiet theo bảng trên]
    domain_pass: true | false
  diem_tong: X/100
  ghi_chu: "..."
  lan_reject: 0-N
```

## Ràng buộc
- Tối đa 2 vòng REVISE — nếu vẫn fail → REJECT
- fact-check FAIL = auto REJECT (không đàm phán)
- anti-ai >30% = auto REJECT
- domain_check FAIL = auto REVISE (chỉ REJECT nếu fail >3 domain checks)
