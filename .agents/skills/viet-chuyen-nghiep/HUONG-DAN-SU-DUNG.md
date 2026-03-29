# Hướng Dẫn Sử Dụng — Viết Chuyên Nghiệp v3.1 Kiến Trúc Tòa Soạn

## Giới thiệu

**Viết Chuyên Nghiệp** là skill AI viết nội dung tiếng Việt chuyên nghiệp, 
hoạt động theo mô hình **Tòa Soạn** — Tổng Biên Tập điều phối 6 Ban 
với **31 biên tập viên (BTV)** chuyên biệt.

## Kiến trúc Tòa Soạn v3.1

```
TỔNG BIÊN TẬP (SKILL.md)
│
├─ 📝 BAN THU THẬP (content/)     — 3 BTV
│  Bóc brief, nghiên cứu 5 lớp, phân tích audience/angle
│
├─ ✍️ BAN BIÊN TẬP (style/)       — 8 BTV (+2 mới: email, curriculum)
│  Cốt truyện, nhịp văn, tường thuật, trình bày, học thuật, email, giáo trình
│
├─ 🔍 BAN KIỂM DUYỆT (quality/)  — 7 BTV
│  Dấu câu, viết hoa, tự nhiên, anti-AI, fact-check, nhất quán
│  + Domain-specific checks (email spam, Bloom, step validation)
│  → PASS / REVISE / REJECT
│
├─ 📱 BAN XUẤT BẢN (platform/)    — 9 BTV (+4 mới: email-platform, zalo, threads, docs)
│  Facebook VN, TikTok Gen Z, LinkedIn B2B, Video Script, Email, Zalo, Threads, Docs
│
├─ 📚 BAN TƯ LIỆU (examples/)    — Thư viện bài mẫu
│
├─ 🔧 BAN PHÁT TRIỂN (meta/)      — 3 agents
│  Self-improve, audit, nâng cấp hệ thống
│
└─ ⚙️ Workers/ (v3.1)           — 3 execution specialists
   email-worker, curriculum-worker, guide-worker
```

## Cách sử dụng

### Viết mới (ebook, tài liệu, content social, video script)
```
"Viết ebook về AI cho CEO, 5 chương"
"Viết 3 bài social (FB + TikTok + LinkedIn) về remote work"
"Viết kịch bản video 60s giới thiệu sản phẩm"
```
Pipeline: `content → style → quality → platform`

### Sửa bản nháp
```
"Sửa lại bài viết này cho tự nhiên hơn"
"Viết lại đoạn mở bài cho hấp dẫn"
```
Pipeline: `content (light) → style → quality`

### Chấm bài (thang 100 điểm)
```
"Chấm bài marketing này thang 100"
"Đánh giá bài viết của em"
```
Pipeline: `content (light) → quality (rubric)`

### Phản biện
```
"Phản biện bài phân tích thị trường này"
"Kiểm tra logic bài viết"
```
Pipeline: `content → quality (critique mode)`

### Viết email ★
```
"Viết chuỗi 5 email nurture cho khóa coaching AI"
"Viết cold email B2B cho dịch vụ marketing"
```
Pipeline: `content (light) → style (email) → quality → platform (email)`

### Viết giáo trình ★
```
"Viết giáo trình 8 module về ứng dụng AI"
"Thiết kế khóa học digital marketing"
```
Pipeline: `content (deep) → style (curriculum+technical) → quality → platform (docs)`

### Viết user guide / SOP ★
```
"Viết SOP quy trình onboarding nhân viên mới"
"Viết user manual cho phần mềm CRM"
```
Pipeline: `content → style (technical+presentation) → quality → platform (docs)`

### Xuất bản
```
"Kiểm duyệt bài này, sẵn sàng publish chưa?"
```
Pipeline: `quality (full) → platform`

## Pipelines

| Lệnh | Pipeline v3.1 |
|-------|--------------|
| Viết mới | content → style → quality → platform |
| Sửa bài | content → style → quality |
| Chấm bài | content → quality (rubric) |
| Phản biện | content → quality (critique) |
| Research | content → quality (verify) |
| Xuất bản | quality → platform |
| Viết email ★ | content (light) → style (email) → quality → platform (email) |
| Viết giáo trình ★ | content (deep) → style (curriculum) → quality → platform (docs) |
| Viết guide/SOP ★ | content → style (technical) → quality → platform (docs) |

## Vòng lặp Chất lượng

```
              ┌──── REVISE (tối đa 2 lần) ────┐
              ▼                                │
content → style → quality ──── PASS ──→ platform → User
                     │
                     └── REJECT ──→ content (nghiên cứu lại)
```

## Cấu trúc Thư mục

```
Viet-chuyen-nghiep/
├─ SKILL.md                    ← Tổng Biên Tập (entry point)
├─ HUONG-DAN-SU-DUNG.md        ← File này
├─ workforce-config.json       ← Config v3.1
│
├─ Ban/                        ← 6 BAN CHUYÊN MÔN (v3.1)
│  ├─ content/   (3 files)     ← Thu thập & nghiên cứu
│  ├─ style/     (8 files)     ← Biên tập phong cách (+email, +curriculum)
│  ├─ quality/   (7 files)     ← Kiểm duyệt
│  ├─ platform/  (9 files)     ← Xuất bản đa nền tảng (+email, +zalo, +threads, +docs)
│  ├─ examples/  (1 file)      ← Thư viện bài mẫu
│  └─ meta/      (3 files)     ← Phát triển & audit
│
├─ Orchestrator/               ← Điều phối trung tâm
│  ├─ editor-in-chief.md       ← Vai trò Tổng BT
│  ├─ routing-matrix.md        ← Ma trận routing (9 pipelines)
│  ├─ delegation-protocol.md   ← Quy trình giao việc
│  ├─ interface-contract.md    ← YAML contracts giữa các Ban
│  └─ escalation-rules.md      ← Quy tắc báo cáo
│
├─ Team-Orchestration/         ← Pipeline chi tiết (9 pipelines)
│  ├─ write-new.md
│  ├─ edit-draft.md
│  ├─ grade-content.md
│  ├─ critique-content.md
│  ├─ deep-research.md
│  ├─ publish-ready.md
│  ├─ write-email.md           ← ★ v3.1
│  ├─ write-curriculum.md      ← ★ v3.1
│  └─ write-guide.md           ← ★ v3.1
│
├─ Workers/                    ← 3 specialists v3.1 + legacy v2.0
│  ├─ email-worker.md          ← ★ v3.1
│  ├─ curriculum-worker.md     ← ★ v3.1
│  ├─ guide-worker.md          ← ★ v3.1
│  └─ DEPRECATED.md            ← legacy markers
│
├─ Autonomous-Core/            ← 4 Engine tự động
│
├─ Context-Layer/              ← Knowledge Base (48+ files)
│  ├─ CoreModules/             ← Quy tắc lõi (+email-templates, +curriculum-framework, +guide-standards)
│  ├─ Knowledge-Base/          ← Kiến thức chuyên sâu
│  ├─ Second-Brain/            ← Kinh nghiệm tích lũy
│  └─ Memory/                  ← Session memory
│
├─ SubAgents/                  ← ⚠️ LEGACY v2.0 (xem DEPRECATED.md)
└─ assets/examples/            ← Ví dụ mẫu
```

## Xử lý Sự cố

| Vấn đề | Giải pháp |
|--------|----------|
| Bài viết bị reject nhiều lần | Kiểm tra brief rõ ràng chưa, yêu cầu cụ thể hơn |
| Anti-AI score cao (>30%) | Yêu cầu "viết lại cho tự nhiên, thêm ví dụ cá nhân" |
| Thiếu nguồn/số liệu | Yêu cầu "research kỹ hơn" hoặc cung cấp nguồn |
| Format không đúng platform | Chỉ rõ platform: "viết cho Facebook" hoặc "format LinkedIn" |

## Câu hỏi Thường gặp

**Q: Skill này có viết được tiếng Anh không?**
A: Mặc định tiếng Việt. Nếu cần tiếng Anh, hãy nói rõ trong yêu cầu.

**Q: Có giới hạn độ dài không?**
A: Không. Skill xử lý từ caption 50 từ đến ebook nhiều chương.

**Q: Workers/ và SubAgents/ còn dùng không?**
A: SubAgents/ DEPRECATED. Workers/ có 3 specialists mới (v3.1) hỗ trợ email/curriculum/guide. Các Workers v2.0 cũ đã thành legacy.

**Q: Mới có những nền tảng nào?**
A: Facebook, TikTok, LinkedIn, Video, Email, Zalo, Threads, Docs. Dự kiến v3.2: X, Instagram, YouTube.
