---
name: subagent-driven-development
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: "Dùng để triệu hồi Lính Đánh Thuê (Subagents) thực thi Hợp đồng Code từng Task một cách song song/tuần tự."
---

# Lập Trình Phân Quyền (Subagent-Driven Development)

Thực thi Hợp đồng (Plan) bằng cách phái một Thằng Lính (Subagent) mới cứng cho mỗi Task. Kèm theo quy trình Review 2 Tầng: Review Spec (Đúng Hợp đồng chưa) -> Review Code (Code có bẩn không).

**Tại sao lại dùng Lính:** Giao task cho chuyên gia có ngữ cảnh bị cách ly. Bạn (Jarvis/Orchestrator) sẽ mớm đúng phần Context cần thiết để nó không bị ngáo. Bọn lính không bao giờ được phép kế thừa lịch sử chat rác rưởi của phiên làm việc tổng. Việc này giúp bạn tiết kiệm Token não bộ để làm chức năng Điều phối.

**Nguyên Tắc LõI:** Lính Mới mỗi Task + Review 2 Tầng = Tốc độ cao, Ít Bug.

> **Sơ đồ tư duy (Flowcharts):** Được lưu trữ tại `/references/sdd-flowcharts.md`. Tham khảo để điều hướng cây quyết định.

## Bảng So Sánh (Vs. Executing Plans)
Nếu tự gõ code (`executing-plans`), bạn ôm một đống rác ngữ cảnh.
Nhưng nếu dùng subagent (`subagent-driven-development`):
- Vẫn nằm ở cùng 1 phiên hội thoại (session) quản lý chung.
- Não lính Trắng Tinh / Không lưu rác rưởi từ task trước.
- Ráp được Review 2 lớp: Code chuẩn Spec và Code Sạch.
- Vòng lặp cải tiến siêu tốc.

## Quy Trình Vận Hành Lính (The Process)

1. Đọc Hợp đồng, chiết xuất tách từng Task ra để dọn mâm.
2. Gọi Lính Thợ xây (`implementer-prompt`). Tóm lược và Mớm đúng phần Context nó cần.
3. Nếu lính thắc mắc -> Tương tác trả lời nó. Nếu không -> Cho nó phép code, test, commit và tự review code của nó.
4. Code xong -> Gọi Lính Thanh tra Spec (`spec-reviewer-prompt`) để đọ xem Code cọ xát đúng Hợp đồng chưa.
5. Chưa chuẩn (thừa/thiếu/sai) -> Đuổi thằng Thợ xây đi sửa tiếp.
6. Chuẩn Spec rồi -> Gọi Thằng Thanh tra Chất lượng (`code-quality-reviewer-prompt`) soi rác.
7. Chưa chuẩn sạch -> Đuổi thằng Thợ xây đi sửa tiếp.
8. Ok hết -> Chốt Task. Sang dọn mâm Task tiếp theo.
9. Done 100% -> Gọi skill `finishing-a-development-branch`.

## Lựa Chọn Hệ Não Phân Bổ (Model Selection)
- **Task thợ xây thủ công** (1-2 file, logic bé): Chọn Model Rẻ/Nhanh (VD: Haiku / 8B).
- **Task đòi tích hợp** (nhiều file, mảng kiến trúc): Chọn Model Tiêu Chuẩn (VD: Sonnet / 70B).
- **Task đòi Thiết kế Core/Review Gắt gao**: Chọn Model Trí Tuệ Cao Nhất (VD: Opus / GPT-4o / 405B).

## Trạng Thái Phản Hồi Của Lính
- **DONE:** Thả cửa cho Team Review lao vào.
- **DONE_WITH_CONCERNS:** Lính code xong nhưng vừa làm vừa hoài nghi "Code architecture hệ thống cũ tù túng quá sếp ạ". Ghi nhận lại note, cho pass đi tiếp.
- **NEEDS_CONTEXT:** Lính mù đường. Mớm thêm Context Specs rồi gọi nó lại.
- **BLOCKED:** Lính bị đứt tay. Nhanh chóng đổi Model xịn hơn hoặc xin viện binh từ CEO.
*Tuyệt đối không nhắm mắt bắt lính thử lại mù quáng nếu không cung cấp đạn dược/mưu kế (context).*

## Cờ Đỏ Báo Động Quân Cảnh (Red Flags)
**TUYỆT ĐỐI KHÔNG:**
- Nhắm mắt bỏ qua khâu Review (Cả 2 tầng).
- Thả 2 Thằng Lính thực thi CÙNG LÚC vào cùng 1 repo sinh conflict git.
- Quăng nguyên cục File Hợp đồng to đùng cho lính tự căng mắt đọc. Bạn LÀ SẾP CỦA NÓ, nhiệu vụ của bạn là NHAI RA và đút tận miệng nó đoạn Text nhỏ của Task nó phải làm.
- Lười biếng gộp 2 khâu Review làm 1 prompt.
- Gọi Lính Thanh tra Quality trước khi Lính Thanh tra Spec gật đầu (Hành vi trái quy trình).

## Tích Hợp Hệ Sinh Thái (Integration)
- **`using-git-worktrees`** - BẮT BUỘC: Dựng workspace nhánh ảo cách ly để code.
- **`writing-plans`** - Lò đẻ ra Hợp đồng để bạn giao phó cho Lính.
- **`requesting-code-review`** - Đưa Sườn Review này cho bọn Thanh tra bám theo.
- **`test-driven-development`** - Ép tụi lính dùng trò này khi code.
- **`finishing-a-development-branch`** - Xong việc ghép nhánh thu tiền.
