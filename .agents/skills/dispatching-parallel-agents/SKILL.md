---
name: dispatching-parallel-agents
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: "Dùng khi đối mặt với 2 hoặc nhiều Bug/Task Độc lập (Không chung State hay thứ tự) - Gọi nhiều Lính chém song song."
---

# Lệnh Bài Phân Thân (Dispatching Parallel Agents)

## Tổng Quan

Khi dự án nổ ra nhiều lỗi Bug hoàn toàn không dính dáng tới nhau (Ví dụ: Lỗi ở file UI và Lỗi cắm Database), việc cử 1 thằng đệ đi soi từng cái theo tuần tự là cực kỳ lãng phí Token thời gian.
Đây là lúc bạn (Jarvis/Orchestrator) phân thân và thả nhiều Subagent cùng lúc.

**Tôn Chỉ:** Cử 1 Thợ cho 1 vùng đất độc lập. Để chúng cày Song Song.

> **Sơ đồ ra quyết định:** Lưu tại `references/parallel-flowchart.md`.

## Dấu Hiệu Nhận Biết

**Mở Skill này khi:**
- Có từ 3+ File test fail vì những nguyên nhân cực kỳ khác biệt.
- 2 chức năng khác nhau bị vỡ riêng lẻ.
- Tự tin là 2 tác vụ đó mà code thì không bao giờ đâm đầu commit chung vào 1 file hệ thống (Shared state = 0).

**Cất Skill này đi khi:**
- Đám Bug có vẻ dính nhau dây chuyền (đụng thằng này chết thằng kia).
- Cần cái nhìn kiến trúc bao quát để hiểu toàn hệ thống.
- Tụi Subagent sẽ phải tranh giành file để sửa đụng nhau.

## Chiến Thuật (The Pattern)

### 1. Gom Vùng Sự Cố (Identify Domains)
Phân loại lỗi theo cụm kiến trúc.
Ví dụ: Cụm A (Lỗi Tool Approval), Cụm B (Lỗi hiển thị Batch Completion). Đây là 2 vùng độc lập, chia 2 Hỏng.

### 2. Soạn Nhánh Chuyên Biệt
Cho mỗi Subagent:
- **Scope (Phạm vi):** Đóng khung vùng cấm địa (Chỉ được sửa file test Auth, cấm đụng thư mục khác).
- **Goal (Mục tiêu):** Kéo bằng được test Auth về trạng thái Pass.
- **Constraints (Khóa Giới Hạn):** Cấm sửa production code, chỉ sửa UI component.
- **Output:** Buộc chúng trả về một báo cáo Root Cause rõ ràng.

### 3. Khai Hỏa Cùng Lúc (Dispatch in Parallel)
```typescript
// Ý niệm Logic cho các nền tảng:
Task("Sửa file agent-tool-abort.test")
Task("Sửa file batch-completion.test")
Task("Sửa file tool-approval.test")
// Cả 3 anh thợ lên đường cùng 1 lúc!
```

### 4. Thu Thập & Hội Quân (Integration)
Đám lính báo cáo chiến công về:
- Đọc từng Summary.
- Validate xem code tụi nó có đụng nhau đôm đốp chưa.
- Bấm chạy tổng duyệt lại toàn bộ Test Suite (Verification).

## Bệnh Rập Khuôn Cốt Lõi (Common Mistakes)
**❌ Khoán việc ngáo:** "Đi fix hết test giùm tao" -> Subagent đi lạc.
**✅ Trúng đích:** "Fix duy nhất lỗi ThreadId ở file `abort.test.js`".

**❌ Thiếu Constraint:** Subagent hăng máu đập đi xây lại cả hệ thống.
**✅ Có Rào Cản:** "Tuyệt đối không đụng vào config Production".

## Thực Chiến
- Bạn tiết kiệm được 1/3 thời gian suy luận nổ não so với Serial Execution.
- Token context không lấp đầy vào não của Main Agent.
