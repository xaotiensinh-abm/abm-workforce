# Ví dụ: Báo cáo Phê bình

## Tóm tắt brief

```yaml
task_type: critique-content
input: "Bài viết 1000 từ: 'Tại sao nên đầu tư BĐS năm 2026'"
critique_depth: standard
focus: "logic + evidence + risk"
```

---

## Output

### 🔍 Critique Report: "Tại sao nên đầu tư BĐS năm 2026"

**Verdict:** 🟠 **Cần sửa đáng kể trước khi publish**

---

#### 1. Logic Analysis (Logic Critic)

| # | Claim | Fallacy | Severity |
|---|-------|---------|----------|
| 1 | "BĐS luôn tăng giá" | **Hasty generalization** — BĐS giảm 2022-2023 | 🔴 High |
| 2 | "Lãi suất thấp = phải mua ngay" | **False urgency** — lãi suất có thể thấp nhiều quý | 🟡 Medium |
| 3 | "Vàng không an toàn bằng BĐS" | **False comparison** — 2 asset class khác risk profile | 🟡 Medium |
| 4 | "Người giàu đều đầu tư BĐS" | **Appeal to authority** — survivorship bias | ⚪ Low |

**Logic score: 45/100** 🟠

---

#### 2. Evidence Assessment (Claim Risk Checker)

| Claim | Evidence provided | Verdict |
|-------|------------------|---------|
| "Giá đất tăng 15% năm 2025" | Không citation | ❌ **Unverified** |
| "Lãi suất 7%" | Có nhưng source mơ hồ ("theo báo cáo") | ⚠️ **Weak** |
| "Dân số tăng → demand tăng" | Logic đúng nhưng oversimplified | ⚠️ **Partial** |

**Evidence score: 35/100** 🔴

> [!WARNING]
> **RISK DOMAIN: BĐS = Domain nhạy cảm**
> Bài này khuyến khích đầu tư BĐS mà KHÔNG có disclaimer.
> Cần thêm: "Bài viết là quan điểm cá nhân, không phải tư vấn
> đầu tư. Mọi quyết định đầu tư cần tham khảo chuyên gia tài chính."

---

#### 3. Clarity Assessment (Clarity Critic)

- **P1-P3**: Dễ hiểu, ngôn ngữ đại chúng ✅
- **P4**: Thuật ngữ "cap rate", "yield" không giải thích → ⚠️
- **P5**: Câu dài (45 từ/câu) → khó theo dõi → ⚠️

**Clarity score: 72/100** 🟡

---

#### 4. Recommended Revisions (Revision Advisor)

| Priority | Revision | Effort |
|----------|----------|--------|
| 🔴 P0 | Thêm disclaimer BĐS/tài chính | 2 phút |
| 🔴 P0 | Remove/fix "BĐS luôn tăng giá" — false | 5 phút |
| 🟡 P1 | Thêm citation cho "15% tăng giá" hoặc remove | 10 phút |
| 🟡 P1 | Balance angle: thêm risks alongside benefits | 15 phút |
| ⚪ P2 | Giải thích "cap rate", "yield" | 5 phút |
| ⚪ P2 | Tách câu dài P5 | 3 phút |

---

### Tổng kết

| Dimension | Score | Visual |
|-----------|-------|--------|
| Logic | 45 | ████▒░░░░░ |
| Evidence | 35 | ███▒░░░░░░ |
| Clarity | 72 | ███████░░░ |
| **Overall** | **51/100** | 🟠 Trung bình |

**Decision: ❌ KHÔNG publish ở trạng thái hiện tại.**
Fix P0 items trước → re-critique → quyết định lại.

---

## Số liệu chất lượng

```yaml
critique_depth: standard ✅
risk_flagged: true ✅ (BĐS = domain nhạy cảm)
actionable_revisions: 6 items ✅
bias_in_critique: no ✅ (critique balanced, not anti-BĐS)
```
