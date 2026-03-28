# Orchestration patterns for Vietnam

## Bất động sản
- `primary-project-sales-vi-v1` + `legal-transaction-ops-vi-v1` khi cần đi hết từ launch, booking, cọc đến hồ sơ và ký kết
- `brokerage-resale-vi-v1` + `legal-transaction-ops-vi-v1` khi team resale có admin/pháp lý xử lý cọc, công chứng, sang tên

## Nha khoa
- `multi-chair-clinic-vi-v1` + `implant-ortho-heavy-vi-v1` khi phòng khám vừa phải tối ưu capacity vừa có nhiều treatment plan dài hạn
- `single-clinic-vi-v1` + `implant-ortho-heavy-vi-v1` khi clinic nhỏ nhưng doanh thu phụ thuộc nhiều vào case implant/ortho

## SMEs
- `trading-distribution-vi-v1` + `sme-ops-vi-v1` khi doanh nghiệp phân phối cần thêm governance, reporting cadence và approval layer
- `service-agency-vi-v1` + `sme-ops-vi-v1` khi agency đang tăng quy mô và founder muốn giảm lệ thuộc vào họp miệng
- `light-manufacturing-vi-v1` + `sme-ops-vi-v1` khi xưởng nhỏ cần thêm weekly review, approval và escalation discipline

## Functional bridge packs
- ghép thêm `founder-office-vi-v1` khi pattern quyết định, review cadence hoặc planning loop còn quá founder-led
- ghép thêm `sales-ops-vi-v1` khi motion bán hàng và hygiene report cần rõ hơn tầng vận hành nền
