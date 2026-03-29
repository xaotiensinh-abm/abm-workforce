---
name: brainstorming
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: "BẮT BUỘC sử dụng trước mọi công việc mang tính sáng tạo hay hệ thống - thêm mới tính năng, thiết kế UI, cấu trúc DB. Gạn lọc yêu cầu và ý đồ của User để xuất bản Spec Design trước khi Code."
---

# Khơi Nguồn Phân Tích (Brainstorming) & Thiết Kế

Giúp chuyển đổi các ý tưởng thô từ một câu prompt của CEO thành bản thiết kế (Specs) chặt chẽ thông qua việc đối thoại phản biện nhiều vòng.

Khởi đầu bằng việc đọc ngữ cảnh dự án (Project Context), sau đó ĐẶT CÂU HỎI (chỉ hỏi 1 câu mỗi lượt) để tinh chỉnh ý đồ. Khi đã nắm chắc thứ cần làm, trình bày toàn văn Design và xin duyệt.

<HARD-GATE>
TUYỆT ĐỐI KHÔNG kích hoạt các skill thực thi code, KHÔNG tạo cấu trúc dự án dự thảo, KHÔNG viết bất kỳ dòng mã nào cho tới khi đạt được cái gật đầu phê duyệt cho bản Design Spec từ CEO/Người dùng. Luật này KHÔNG CÓ NGOẠI LỆ, áp dụng với cả những lỗi vặt.
</HARD-GATE>

## Ngụy Biện: "Task này dễ cần gì Design"

Cập nhật lại 1 dòng configs, viết 1 array utils con con, thêm 1 thẻ P... mọi thứ đều phải có thiết kế vi mô. Các task "cỏn con" chính là nơi các assumption sai lệch sinh ra rác trong dự án nhất. Bản thiết kế có thể chỉ ngắn gọn trong 1 câu tóm tắt, nhưng BẮT BUỘC phải show ra và nhận cái "ok" trước khi đụng vào code.

## Danh Sách Bắt Buộc (Checklist)

Tần suất: Xóa từng mục theo thứ tự:

1. **Khảo sát hệ tri thức (Context)** — Đọc file cấu trúc, docs, review vài commit gốc gác vấn đề.
2. **Offer tính năng thị giác (Visual Companion)** — Xem chi tiết `/references/visual-companion.md` nếu đang thiết kế UI.
3. **Khai vấn (Clarifying Questions)** — Hỏi duy nhất 1 vấn đề mỗi prompt. Tìm ra the "Why", constraints, mục tiêu thành công.
4. **Trình bày 2-3 kịch bản giải pháp** — Cung cấp Bảng Trade-offs và tự tin đưa ra đề xuất Tối ưu nhất của Agent.
5. **Trình bày Thiết kế (Spec)** — Tùy theo độ phức tạp, nếu quá dài thì cắt ra trình bày từng phần.
6. **Lưu cứng Design Doc** — Xuất file lưu tại `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` và commit.
7. **Đệ trình Review Spec** — (Dùng subagent nếu có hệ chuyên gia) soát chéo lại thiết kế chống lỗi logic.
8. **User Duyệt File Chữ** — Nhờ CEO đọc lại file markdown và xin cái "ok".
9. **Chuyển hóa (Transition)** — Gọi `writing-plans` để lập Hợp đồng Code (Bitesize).

> Sơ đồ kỹ thuật: Được rẽ nhánh tại `references/brainstorming-flow.md`

## Kỹ Năng Đặt Câu Hỏi (Giao Tiếp Thuần Việt)

- **Tránh dồn dập:** Dồn 3 câu vào 1 prompt chỉ làm User bối rối.
- **Multiple Choice:** Ưu tiên đưa cho họ Option A/B/C thay vì bắt họ tự điền vào chỗ trống.
- **Tách rời vương quốc:** Nếu yêu cầu đòi làm "App Chat Tích Hợp Ví", phím ngay là phải tách 2 dự án Sub-project. Tuyệt đối không nấu chung một nồi lẩu Design.
- **Micro-services:** Modul hóa thiết kế. Chặn tương tác hỗn loạn. Tránh một file ôm 1000 dòng.

## Cầu Nối Tiếp Theo (Sau Thiết Kế)

Dùng lời lẽ chuyên nghiệp khi kết thúc phiên:
> "Bản phác thảo ranh giới hệ thống đã được đúc thành văn bản tại `<path>`. Mời CEO soát lại mục tiêu. Nếu ổn thỏa, xin phép được khởi động luồng `writing-plans` để chia rã Thành từng Hợp Đồng Code (Contract Steps)."

**Cấm kỵ:** Không tự ý quẹo sang gọi `frontend-design` hay nhảy thẳng đi viết Script. Chỉ mở cổng đến `writing-plans` để ký hợp đồng execution.
