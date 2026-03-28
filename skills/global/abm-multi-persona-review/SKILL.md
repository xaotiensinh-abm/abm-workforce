---
name: abm-multi-persona-review
description: Khởi chạy quy trình review đa chiều với 8 personas chuyên biệt (Hacker, Auditor, CEO, Architect, Pragmatist, Competitor, Operator, New Hire) để đánh giá code, kiến trúc hoặc strategy.
---

# ABM Multi-Persona Review

Đánh giá phản biện đa chiều sử dụng 8 personas chuyên biệt của hệ thống ABM Workforce.

**Nguyên tắc cốt lõi:** Mỗi persona là một góc nhìn độc lập. Không persona nào có quyền phủ quyết — User (CEO) quyết định cuối cùng.

## Khi nào sử dụng (Triggers)
Auto-activate triggers (VN): "hội đồng đánh giá", "review đa chiều", "phản biện kiến trúc", "kiểm tra chéo", "đánh giá tổng thể", "8 personas review"
Auto-activate triggers (EN): "multi-persona review", "comprehensive audit", "architecture review council", "cross-evaluation", "evaluate strategy"

- Đánh giá architecture / design decisions
- Review code sau khi implementation hoàn tất
- Audit system integrity
- Phản biện business plan / strategy
- Trù bị trước khi deploy production

## 8 Personas

| # | Persona | Góc nhìn (Perspective) | Trọng số (Weight) |
|---|---|---|---|
| 1 | 🔴 **Hacker** | Tấn công lỗ hổng, injection, bypass | 15% |
| 2 | 📊 **Auditor** | Compliance, traceability, audit trail | 15% |
| 3 | 💼 **CEO** | ROI, business value, strategic fit | 15% |
| 4 | 🏗️ **Architect** | Kiến trúc, mở rộng, tech debt | 15% |
| 5 | 🔧 **Pragmatist** | Thực tiễn, complexity, maintenance cost | 10% |
| 6 | ⚔️ **Competitor** | So sánh alternatives, market position | 10% |
| 7 | 🔄 **Operator** | Vận hành, monitoring, incident response | 10% |
| 8 | 📚 **New Hire** | Learning curve, documentation quality | 10% |

## Quy trình Thực Thi

### Bước 1: THU THẬP BẰNG CHỨNG (Evidence Gathering)

```
Không dùng giả định "chắc là" — đếm file thực tế, đo dòng code, đọc content, review dependency.
```

### Bước 2: CHẤM ĐIỂM TỪNG PERSONA (Persona Scoring)

Mỗi persona đánh giá 1-10 với evidence cụ thể:

```markdown
| Persona | Điểm | Phát hiện | Mức độ | Evidence |
|---|---|---|---|---|
| Hacker | 7 | SQL injection possible | 🔴 | [file:line] |
| Auditor | 6 | No audit log | 🟡 | Missing logging |
```

### Bước 3: PHÂN LOẠI PHÁT HIỆN (Finding Classification)

- 🔴 **Nghiêm trọng (P0)** — Cần fix ngay lập tức, chặn quy trình deploy
- 🟡 **Cần sửa (P1)** — Phải fix trước release
- 🔵 **Cải thiện (P2)** — Đưa vào backlog
- ✅ **Tốt** — Giữ nguyên

### Bước 4: ĐỐI CHIẾU CHÉO (Cross-Reference)

Ma trận cross-reference: Phát hiện của persona A có tác động lên phương án của persona B không? (VD: Khắc phục theo bài Auditor gây ảnh hưởng tiêu cực lên Operator?)

### Bước 5: KẾ HOẠCH HÀNH ĐỘNG (Action Plan)

Ưu tiên giải quyết: P0 (🔴 nghiêm trọng) → P1 (🟡 cần sửa) → P2 (🔵 cải thiện)

## Output Format

```markdown
## Tóm tắt (≤ 200 từ)
[CEO đọc tóm tắt tại đây]

## Bảng điểm Đa Chiều
| Persona | Điểm | Top Finding |
|---|---|---|

## Điểm tổng: X.X/10 (Trung bình có trọng số)

## Kế hoạch Hành động
| # | Priority | Action | Phân công | Deadline |
```

## Tích hợp Skills Bổ Trợ

**REQUIRED SUB-SKILL:** `verification-before-completion` — Verify toàn bộ evidence kỹ thuật trước khi đưa vào bảng điểm.

**After review:** Sử dụng `writing-plans` nếu cần lập kế hoạch fix issues sau đánh giá.

## Ví dụ: Tham chiếu Review API Authentication Module

**Input:** Review module `src/auth/` (3 files, 450 lines)

**Thu thập evidence:** Đọc 3 files, 450 lines mã nguồn. Lọc ra API auth endpoint.

**Bảng điểm:**
| Persona | Điểm | Top Finding | Mức |
|---|---|---|---|
| 🔴 Hacker | 7 | JWT secret hardcoded trong config.js | 🔴 |
| 📊 Auditor | 6 | Không log failed login attempts | 🟡 |
| 💼 CEO | 9 | Auth module phục vụ 100% users | ✅ |
| 🏗️ Architect | 8 | Tách concerns tốt, thiếu rate limiting | 🟡 |
| 🔧 Pragmatist | 8 | Code clean, dễ maintain | ✅ |
| ⚔️ Competitor | 9 | Tương đương industry standard | ✅ |
| 🔄 Operator | 7 | Thiếu health check endpoint | 🟡 |
| 📚 New Hire | 8 | README rõ, thiếu API docs | 🔵 |

**Điểm tổng:** 7.8/10 (weighted)

**Kế hoạch Hành động:**
| # | Priority | Action | Khi nào |
|---|---|---|---|
| 1 | P0 | Move JWT secret → env var | Ngay lập tức |
| 2 | P1 | Add login attempt logging | Sprint này |
| 3 | P1 | Implement rate limiting | Sprint này |

## Red Flags (Cảnh Báo Dừng)

- ❌ Suy diễn chấm điểm cảm tính mà **không lấy evidence từ code/file cụ thể**.
- ❌ Bỏ qua một persona vì cho rằng "không liên quan".
- ❌ Tự thoả mãn tất cả personas cùng cho điểm 10/10 vô lý.
- ❌ In ra kết quả mà **thiếu Kế hoạch hành động tiếp theo**.
