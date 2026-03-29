# Quy tắc Leo thang — v3.1

## Mục đích

Quy định KHI NÀO BTV/Trưởng Ban phải **escalate** lên Tổng Biên Tập
thay vì tự quyết định. Ngăn BTV self-decide trong tình huống rủi ro.

---

## Ma trận Leo thang

| Trigger | Severity | Escalate to | Action |
|---------|----------|-------------|--------|
| Rubric score < 40 | 🔴 Critical | Tổng Biên Tập | REJECT + nghiên cứu lại |
| Anti-AI score > 60 | 🔴 Critical | Tổng Biên Tập | Full anti-AI rewrite |
| Claim risk = critical | 🔴 Critical | Tổng Biên Tập | Block publish |
| Email spam score > 5/10 ★ | 🔴 Critical | Ban Biên Tập (style/email) | Rewrite subject + body |
| 2 vòng REVISE thất bại | 🟡 High | Tổng Biên Tập | Manual intervene |
| Research tất cả nguồn < Tier 2 | 🟡 High | Ban Thu Thập (content/) | Nâng cấp nguồn |
| Brief mơ hồ (3+ unknowns) | 🟡 High | Ban Thu Thập (content/) | Hỏi user |
| Bloom progression nhảy 2+ levels ★ | 🟡 High | Ban Biên Tập (style/curriculum) | Refactor module sequence |
| SOP thiếu RACI hoặc flowchart ★ | 🟡 High | Ban Biên Tập (style/technical) | Bổ sung required sections |
| Tone drift > 3 sections | ⚪ Medium | Ban Biên Tập (style/) | BTV rhythm/narrative sửa |
| Consistency score < 70 | ⚪ Medium | Ban Kiểm Duyệt (quality/) | Chạy lại consistency.md |
| Format non-standard | ⚪ Low | Tự xử lý | Auto-fix |

---

## Quy trình Leo thang

### Bước 1: BTV/Trưởng Ban phát hiện vấn đề

```yaml
escalation_request:
  from: "Ban/quality/anti-ai"  # Tên Ban + BTV
  issue: "Anti-AI score 72%, vượt ngưỡng"
  severity: "critical"
  attempted_fix: "Đã thay 5 cụm từ AI → vẫn > 60%"
  evidence: "15 dấu hiệu AI detected, xem chi tiết tại..."
```

### Bước 2: Tổng Biên Tập nhận và quyết định

- **Critical**: STOP pipeline → Tổng BT review
- **High**: PAUSE bước hiện tại → Tổng BT quyết định
- **Medium**: CONTINUE nhưng flag trong output
- **Low**: BTV tự xử lý, ghi log

### Bước 3: Giải quyết

```yaml
resolution:
  decision: "rewrite" | "fix" | "override" | "hoi_user"
  by: "tong-bien-tap"
  route_to: "Ban/style/lead-style"  # Chuyển cho Ban nào xử lý
  notes: "Score anti-AI quá cao, cần viết lại toàn bộ đoạn 2-4"
```

---

## Auto-escalation Triggers

Không cần BTV nhận ra — engine tự phát hiện:

1. **REVISE count ≥ 2** → auto-escalate to Tổng BT
2. **Pipeline runtime > 10 phút** → auto-notify
3. **Output mâu thuẫn giữa các Ban** → flag for human review
4. **User phản hồi tiêu cực** → escalate + log lesson vào `Ban/meta/`
