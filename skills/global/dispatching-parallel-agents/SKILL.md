---
name: dispatching-parallel-agents
description: Sử dụng khi có 2+ tasks hoặc lỗi độc lập có thể được điều tra song song mà không chia sẻ trạng thái hoặc phụ thuộc tuần tự.
---

# Dispatching Parallel Agents (Giao Việc Tác Tử Song Song)

## Tổng Quan (Overview)

Bạn ủy thác task cho các subagent chuyên biệt để làm các tác vụ song song với vòng cảnh (context) độc lập. Thay vì đi loanh quanh giải quyết một chuỗi lỗi đan chéo không liên quan, việc cắt lát context cho từng subagent làm việc độc lập giúp chúng tối tập trung. Agent con (subagent) KHÔNG ĐƯỢC kế thừa session context hỗn mang hiện tại của bạn. Cần truyền đúng thứ nó cần biết. Điều này cũng giúp bạn đóng vai Orchestrator chuẩn xác.

**Nguyên lý cốt lõi:** Một agent xử lý MỘT vấn đề tách biệt. Chạy song song.

## Khi nào sử dụng (Triggers)
Auto-activate triggers (VN): "chạy song song", "xử lý đồng thời", "fix nhiều lỗi", "chia agent điều tra", "test failed nhiều chỗ do các nguyên nhân khác nhau"
Auto-activate triggers (EN): "parallel execution", "run concurrently", "independent errors", "dispatch agents", "multi-agent parallel"

**Dùng khi:**
- Có từ 3+ files test rớt do (các) nguyên nhân không giống nhau và không liên đới.
- Nhiều Subsystem bị lỗi độc lập.
- Mỗi vấn đề dễ dàng cô lập và có thể hiểu không cần soi vào mớ hỗn độn của subsystem khác.
- Tuyệt đối không có shared states lúc điều tra và chỉnh sửa.

**KHÔNG dùng khi:**
- Các lỗi dính dáng trói buộc lẫn nhau (Sửa 1 nơi, fix nhiều lỗi).
- Yêu cầu phải hiểu toàn cảnh Total System Status.
- Các Agents có thể va chạm / dẫm chân lên nhau.

## The Pattern (Khuôn mẫu)

### 1. Phân loại theo Vùng Không Liền Kề (Identify Independent Domains)

Ví dụ phân nhóm Failures:
- File A: Lỗi luồng tạo Account (Tool flow)
- File B: Lỗi xử lý hóa đơn Batch (Batching)
- File C: Chập chờn khi Abort system

Mỗi Domain độc lập, không liên đới.

### 2. Định nghĩa Agent Tasks (Focused Tasks)

Mỗi Local Agent phải gánh đủ 4 món vũ khí:
- **Specific scope:** Mục tiêu file/subsystem.
- **Clear goal:** Test nào cần pass, lỗi gì cần hết.
- **Constraints (Rào cản):** Chỉ chạm phạm vi được giao, cấm đi bậy.
- **Expected output:** Báo cáo gốc rễ (Root cause) và thay đổi thực tại.

### 3. Khởi chiếu Song Song (Dispatch Parallel)

Gây dựng các call tool subagent, tool-run, hoặc terminal processes song song.

```typescript
// Ý niệm Logic:
Task("Fix authen.test.ts")
Task("Fix billing-job.test.ts")
Task("Fix timeout.test.ts")
// Tất cả thực thi concurrently.
```

### 4. Review và Hòa Trộn Lại (Integrate)

Khi các subagents trả kết quả:
- Duyệt qua mớ Summary.
- Kiểm định code fixes không conflict.
- Run toàn bộ Full Test suite.
- Commit Integrate kết quả.

## Cấu Trúc Lệnh Giao Việc Chuẩn (Agent Prompt Structure)

Chất lượng Output = Dữ kiện Focus + Context tự gánh vác (Self-contained) + Kì vọng rõ ràng.

**Ví dụ Prompt Tốt:**
```text
Fix the 3 failing tests in src/agents/agent-tool-abort.test.ts:
1. "should abort tool..."
2. "should properly track..."
   
Your task:
1. Đọc test file để hiểu rõ logic test.
2. Identify Root Cause. Lỗi Logic hay do timeout hệ thống chạy lâu?
3. Sửa bằng cách: Dùng event-based đợi, tuyệt đối không hardcode Timeouts vớ vẩn.
4. KHÔNG chạm production code quá xa, chỉ xoay quanh abort func.
Return: Tổng kết gốc rễ và code đã thay đổi.
```

## Sai Lầm Thường Gặp (Common Mistakes)

- ❌ Quá bao quát: "Sửa tất cả test rớt đi." → Trượt.
- ✅ Cụ thể: "Fix file `agent-tool-abort.test.ts` lỗi X."

- ❌ Thiếu Context: "Sửa lỗi race condition kia." → Lạc trôi.
- ✅ Context: Paste Log Errors, Name Test vào.

- ❌ Giao việc không Rào Chắn: Agent lăng xăng đi refactor core lib.
- ✅ Constraints: "Tuân thủ Scope. Không đụng đến hàm XYZ."

## Lợi Ích Cốt Lõi

1. Tiết kiệm thời gian (1 lúc 3 task).
2. Tác vụ siêu tập trung (Focus scope).
3. Triệt tiêu nhiễu Context (Independence).
