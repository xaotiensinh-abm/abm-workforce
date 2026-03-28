# Sample pack selection

## Functional packs
- Chọn `customer-support-vi-v1` khi case thiên về xử lý case, escalation, queue, qa, sla.
- Chọn `sales-ops-vi-v1` khi case thiên về pipeline, forecast, hygiene, approval, report review.
- Chọn `founder-office-vi-v1` khi case thiên về operating cadence, memo quyết định, planning và review.

## Vietnam industry packs
- Chọn `real-estate-vi-v1` khi case thiên về lead, qualify, site visit, booking, đặt cọc, hợp đồng, hồ sơ giao dịch và phối hợp giữa sale, admin, pháp lý, CSKH.
- Chọn `dental-clinic-vi-v1` khi case thiên về patient journey, lịch hẹn, bác sĩ, ghế điều trị, tư vấn điều trị, chăm sóc sau điều trị và tái khám.
- Chọn `sme-ops-vi-v1` khi case là SMEs cần chuẩn hóa vận hành liên phòng ban, approval, giao ban, báo cáo tuần, onboarding và giảm phụ thuộc vào founder.

## Vietnam sub-packs
### Bất động sản
- Chọn `primary-project-sales-vi-v1` khi case là bán dự án sơ cấp, cần quản lý inventory, booking, ưu đãi và nhịp launch.
- Chọn `brokerage-resale-vi-v1` khi case là môi giới mua bán hoặc cho thuê thứ cấp, trọng tâm là sourcing, matching, xem nhà, đàm phán, chốt cọc.
- Chọn `legal-transaction-ops-vi-v1` khi case là bộ phận pháp lý hoặc giao dịch, trọng tâm là hồ sơ, tiến độ thanh toán, ký kết, sang tên, bàn giao.

### Nha khoa
- Chọn `single-clinic-vi-v1` khi phòng khám 1 cơ sở, team nhỏ và owner hoặc bác sĩ chủ can thiệp trực tiếp.
- Chọn `multi-chair-clinic-vi-v1` khi cần điều phối nhiều ghế, nhiều bác sĩ, turn-time, no-show, vô trùng và capacity.
- Chọn `implant-ortho-heavy-vi-v1` khi case tập trung vào treatment plan dài hơi, consent, follow-up, thu tiền theo chặng, recall.

### SMEs
- Chọn `service-agency-vi-v1` khi mô hình là agency hoặc dịch vụ theo account/project, cần scope, delivery, utilization, client health.
- Chọn `trading-distribution-vi-v1` khi doanh nghiệp mua-bán-phân phối, cần kiểm soát tồn kho, đơn hàng, giao hàng, công nợ, đổi trả.
- Chọn `light-manufacturing-vi-v1` khi xưởng sản xuất nhẹ cần kế hoạch sản xuất, vật tư, QC, lỗi, giao hàng, năng suất.

## Common orchestration choices
- `primary-project-sales-vi-v1` + `legal-transaction-ops-vi-v1`: dùng khi muốn mô hình hóa trọn vẹn từ launch/booking đến hồ sơ, cọc, hợp đồng.
- `brokerage-resale-vi-v1` + `legal-transaction-ops-vi-v1`: dùng khi resale vừa cần motion bán hàng vừa cần chốt giao dịch và công chứng.
- `multi-chair-clinic-vi-v1` + `implant-ortho-heavy-vi-v1`: dùng khi clinic có áp lực capacity và nhiều ca dài hạn.
- `trading-distribution-vi-v1` + `sme-ops-vi-v1`: dùng khi doanh nghiệp phân phối còn founder-led và cần thêm governance, reporting cadence.
- `service-agency-vi-v1` + `sme-ops-vi-v1`: dùng khi agency muốn ghép delivery motion với lớp điều hành liên phòng ban.

## Quy tắc chọn pack
- Ưu tiên pack gần business model nhất trước.
- Nếu case vừa có lớp ngành vừa có lớp điều hành chung, chọn pack ngành hoặc sub-pack làm khung chính và pack `sme-ops-vi-v1` hoặc `founder-office-vi-v1` làm lớp bổ sung cho governance, họp, duyệt việc và reporting cadence.
- Nếu case còn mơ hồ, bắt đầu bằng pack ngành rộng rồi thu hẹp xuống sub-pack ngay khi thấy tín hiệu rõ từ tài liệu nguồn.
- Nếu case đi qua nhiều motion có handoff rõ, tạo orchestration thay vì ép tất cả vào một pack đơn lẻ.
