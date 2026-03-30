# Pipeline: Viết Email (write-email) — v3.1

## Khi nào kích hoạt
- User yêu cầu viết email marketing, cold outreach, nurture sequence
- User yêu cầu viết email nội bộ, follow-up, transactional
- Tín hiệu: "viết email", "email marketing", "cold email", "email sequence", "email nội bộ"

## Pipeline

```
content/ (light) → style/ (email) → quality/ → platform/ (email) → Output
   │                    │               │              │
   │                    │               │              └─ Deliverability + format
   │                    │               └─ 6 kiểm tra → PASS/REVISE/REJECT
   │                    └─ BTV email biên tập
   └─ Brief + research target audience
```

## Bước chi tiết

### 1. Ban Thu Thập (content/) — Light Mode
1. `lead-content.md` nhận brief → xác định loại email (6 types)
2. `analysis.md` phân tích: audience, goal, context, previous interactions
3. Output: **Email Brief YAML** → chuyển Ban Biên Tập

### 2. Ban Biên Tập (style/)
1. `lead-style.md` route trực tiếp đến `email.md`
2. BTV Email xử lý: subject line, preview text, body structure, CTA
3. Nếu email sequence: thiết kế flow 3-5 emails với progression logic
4. Output: **Email Draft** → chuyển Ban Kiểm Duyệt

### 3. Ban Kiểm Duyệt (quality/)
1. `lead-quality.md` chạy kiểm tra:
   - punctuation + capitalization (chuẩn email formal/casual)
   - natural (văn phong tự nhiên, không robot)
   - anti-ai (đặc biệt quan trọng cho email — phải authentic)
   - consistency (tone nhất quán trong sequence)
2. Bonus check: **spam trigger scan** (kiểm tra từ khóa spam)
3. PASS → Ban Xuất Bản | REVISE → Ban Biên Tập

### 4. Ban Xuất Bản (platform/)
1. `lead-platform.md` route đến `email-platform.md`
2. BTV Email Platform tối ưu: deliverability, responsive, personalization
3. Output: **Email sẵn sàng gửi** (text + HTML structure)

## Email Sequence Mode
Khi user yêu cầu chuỗi email:
1. Thiết kế sequence map (3-7 emails)
2. Mỗi email chạy qua pipeline riêng
3. Kiểm tra consistency cross-email
4. Output: full sequence với timing suggestions

## Tham chiếu Knowledge
- `Context-Layer/CoreModules/email-templates.md`
- `Context-Layer/CoreModules/tone-of-voice-guide.md`
- `Ban/style/email.md` — editorial rules
- `Ban/platform/email-platform.md` — platform optimization
- `Workers/email-worker.md` — execution templates (subject formulas, personalization tokens, sequence logic) ★
