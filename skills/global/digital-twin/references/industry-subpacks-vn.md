# Vietnam industry sub-packs

Dùng file này khi case đã rõ hơn ngành rộng và cần chọn đúng phân khúc con để bám cấu trúc vận hành.

## Real estate
- `primary-project-sales-vi-v1`: phù hợp với chủ đầu tư hoặc đại lý bán dự án, có inventory, launch plan, booking, ưu đãi, booking ngoại lệ.
- `brokerage-resale-vi-v1`: phù hợp với môi giới mua bán hoặc cho thuê thứ cấp, có sourcing hàng, matching, xem nhà, thương lượng, chốt cọc.
- `legal-transaction-ops-vi-v1`: phù hợp với pháp lý giao dịch, admin sale, hồ sơ, thanh toán, ký kết, sang tên, bàn giao.
- orchestration thường gặp: `primary-project-sales-vi-v1` + `legal-transaction-ops-vi-v1`, hoặc `brokerage-resale-vi-v1` + `legal-transaction-ops-vi-v1`.

## Dental clinic
- `single-clinic-vi-v1`: phù hợp với 1 cơ sở, team nhỏ, owner hoặc bác sĩ chủ xuất hiện trong nhiều quyết định.
- `multi-chair-clinic-vi-v1`: phù hợp với nhiều ghế, cần điều phối chair, turn-time, bác sĩ, vô trùng, no-show.
- `implant-ortho-heavy-vi-v1`: phù hợp với treatment plan dài, consent, tài chính điều trị theo chặng, recall, compliance.
- orchestration thường gặp: `multi-chair-clinic-vi-v1` + `implant-ortho-heavy-vi-v1` khi clinic lớn vừa tối ưu ghế vừa phải giữ discipline treatment dài hạn.

## SMEs
- `service-agency-vi-v1`: phù hợp với client service, account, scope, delivery, utilization, client retention.
- `trading-distribution-vi-v1`: phù hợp với mua hàng, tồn kho, giao hàng, công nợ, đổi trả, chính sách giá.
- `light-manufacturing-vi-v1`: phù hợp với kế hoạch sản xuất, vật tư, QC, lỗi, năng suất, giao hàng.
- orchestration thường gặp: một sub-pack ngành + `sme-ops-vi-v1` hoặc `founder-office-vi-v1` khi cần thêm governance, approval, review cadence, founder delegation.

## Quy tắc dùng
- chọn sub-pack ngay khi tài liệu nguồn phát ra tín hiệu rõ về motion vận hành, metric và role system.
- dùng pack ngành rộng khi cần lớp khung chung; dùng sub-pack để thêm mức chi tiết, exception path và cadence gần với thực tế hơn.
- nếu tài liệu nguồn cho thấy nhiều motion nối tiếp hoặc chồng lớp governance, dùng orchestration thay vì nhồi tất cả vào một pack.
