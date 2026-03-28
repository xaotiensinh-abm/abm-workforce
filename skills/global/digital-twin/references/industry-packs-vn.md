# Industry packs for Vietnam

Dùng các industry packs này khi case cần bám sát cách doanh nghiệp Việt Nam thường tổ chức vận hành, tài liệu và nhịp điều hành.

## 1. Bất động sản
Phù hợp cho:
- sàn môi giới bất động sản
- đội sales dự án sơ cấp
- phòng vận hành giao dịch, booking, đặt cọc, ký HĐ
- team admin sale hoặc sales ops bất động sản

Tín hiệu nhận diện:
- có lead từ marketing hoặc referral
- có bước tư vấn, qualify, site visit, booking, đặt cọc, ký HĐ, chăm sóc sau bán
- có vai trò sale, trưởng nhóm, admin, pháp lý, CSKH, kế toán giao dịch
- có báo cáo theo giỏ hàng, pipeline, booking, conversion, tồn kho, tiến độ hồ sơ

Artefact nên ưu tiên tạo:
- process catalog cho lead-to-booking-to-contract
- decision rules cho giữ chỗ, booking, hoàn cọc, chuyển căn, ngoại lệ pháp lý
- role handbook cho sale, trưởng nhóm, admin, pháp lý, CSKH
- metric cadence cho nguồn lead, show-up, booking, conversion, tồn hồ sơ

### Sub-packs bất động sản
- `primary-project-sales-vi-v1`: khi case là bán dự án sơ cấp, có inventory, chính sách booking và nhịp launch mở bán.
- `brokerage-resale-vi-v1`: khi case là môi giới thứ cấp, trọng tâm là sourcing hàng, matching, xem nhà, đàm phán và chốt cọc.
- `legal-transaction-ops-vi-v1`: khi case thiên về pháp lý giao dịch, hồ sơ, tiến độ thanh toán, ký kết, sang tên, bàn giao.

## 2. Phòng khám nha khoa
Phù hợp cho:
- phòng khám 1 cơ sở hoặc chuỗi nhỏ
- đội lễ tân, điều phối lịch, bác sĩ, phụ tá, tư vấn điều trị, chăm sóc khách hàng
- vận hành patient journey từ đặt lịch tới tái khám

Tín hiệu nhận diện:
- có các bước tiếp nhận, xác nhận lịch, khám, tư vấn kế hoạch điều trị, chụp phim, điều trị, thanh toán, tái khám
- có vai trò lễ tân, tư vấn, bác sĩ, phụ tá, điều phối, thu ngân, quản lý cơ sở
- có quy tắc cho no-show, dời lịch, consent, nhắc lịch, sau điều trị, xử lý khiếu nại
- có báo cáo lịch hẹn, tỷ lệ đến khám, chốt kế hoạch, doanh thu ghế, tái khám, rating dịch vụ

Artefact nên ưu tiên tạo:
- patient journey process catalog
- decision rules cho xác nhận lịch, xếp ghế, ưu tiên cấp cứu, thay đổi bác sĩ, xử lý no-show
- role handbook cho lễ tân, tư vấn, bác sĩ, phụ tá, quản lý cơ sở
- metric cadence cho booking, show rate, treatment acceptance, chair utilization, recall

### Sub-packs nha khoa
- `single-clinic-vi-v1`: cho phòng khám 1 cơ sở, founder hoặc bác sĩ chủ còn can thiệp trực tiếp, team gọn.
- `multi-chair-clinic-vi-v1`: cho phòng khám có nhiều ghế, cần điều phối capacity, lịch bác sĩ, vô trùng, no-show và turn-time.
- `implant-ortho-heavy-vi-v1`: cho case nhiều kế hoạch điều trị dài hơi, consent, tài chính điều trị, recall và theo dõi compliance.

## 3. SMEs
Phù hợp cho:
- công ty dịch vụ, thương mại, phân phối, agency, xưởng nhỏ hoặc vận hành liên phòng ban quy mô vừa và nhỏ
- founder-led business chưa chuẩn hóa hoàn toàn
- team vận hành cần đóng gói cách chạy việc liên phòng ban

Tín hiệu nhận diện:
- quy trình còn nằm rải trong chat, memo, sheet, file cũ
- quyết định tập trung ở founder hoặc quản lý chủ chốt
- có nhu cầu chuẩn hóa sales, delivery, finance ops, HR ops, customer care, procurement
- có báo cáo tuần, họp giao ban, checklist nhưng chưa nối thành operating model rõ

Artefact nên ưu tiên tạo:
- operating model
- process catalog theo chức năng chính
- decision rules cho approval, ngoại lệ, ngân sách, ưu tiên việc
- onboarding guide và meeting brief để giảm phụ thuộc vào người cũ

### Sub-packs SMEs
- `service-agency-vi-v1`: cho agency hoặc doanh nghiệp dịch vụ dựa trên account, scope, delivery, utilization và client health.
- `trading-distribution-vi-v1`: cho thương mại phân phối với mua hàng, tồn kho, đơn hàng, công nợ, giao hàng, đổi trả.
- `light-manufacturing-vi-v1`: cho xưởng sản xuất nhẹ với kế hoạch sản xuất, vật tư, QC, năng suất, lỗi, giao hàng.

## Cách dùng industry packs đúng
- chỉ dùng sample pack ngành để mượn cấu trúc, độ chi tiết và các lớp quy trình thường gặp
- không sao chép facts của sample pack sang case thực tế
- nếu case là SMEs trong một ngành cụ thể, ưu tiên chọn pack ngành cụ thể trước, pack SMEs dùng để bổ sung lớp điều hành chung
- khi đã xác định được phân khúc con, ưu tiên sub-pack gần business model nhất thay vì pack ngành rộng

## Gợi ý orchestration theo ngành
- Bất động sản: bắt đầu bằng sub-pack gần motion bán hàng nhất, rồi ghép legal transaction ops nếu tài liệu cho thấy hồ sơ, thanh toán, ký kết và bàn giao có vai trò nổi bật.
- Nha khoa: bắt đầu bằng pack clinic phù hợp quy mô ghế, rồi ghép implant-ortho-heavy khi doanh thu hoặc tải vận hành phụ thuộc nhiều vào treatment plan dài hạn.
- SMEs: bắt đầu bằng pack ngành hoặc sub-pack business model, rồi ghép `sme-ops-vi-v1` hoặc `founder-office-vi-v1` nếu vấn đề cốt lõi là governance, founder dependency, weekly review và approval.
