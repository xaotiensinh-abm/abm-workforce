# Getting started

Dùng skill này khi bạn muốn biến tài liệu rời rạc thành một **song sinh số vận hành** có thể tái sử dụng.

## Chọn luồng nhanh
- **Build**: khi có SOP, policy, report, memo, deck, notes và muốn dựng twin doanh nghiệp.
- **Operate**: khi đã có twin và muốn tạo artefact mới như SOP, playbook, onboarding, memo, report template hoặc checklist.
- **Update**: khi có tài liệu mới và muốn cập nhật twin.
- **Audit**: khi muốn kiểm tra độ phủ, độ nhất quán hoặc drift giữa twin và artefact thực tế.

## Nếu case thuộc khách hàng Việt Nam theo ngành cụ thể
- **Bất động sản**: bắt đầu với `real-estate-vi-v1`, rồi thu hẹp xuống `primary-project-sales-vi-v1`, `brokerage-resale-vi-v1` hoặc `legal-transaction-ops-vi-v1` nếu tín hiệu rõ.
- **Phòng khám nha khoa**: bắt đầu với `dental-clinic-vi-v1`, rồi thu hẹp xuống `single-clinic-vi-v1`, `multi-chair-clinic-vi-v1` hoặc `implant-ortho-heavy-vi-v1`.
- **SMEs**: bắt đầu với `sme-ops-vi-v1`, rồi chọn `service-agency-vi-v1`, `trading-distribution-vi-v1` hoặc `light-manufacturing-vi-v1` nếu đã rõ mô hình.

## Nếu case đi qua nhiều motion cùng lúc
- chọn **1 primary pack** gần business model nhất
- chọn thêm **1–2 adjacent packs** cho phần handoff, governance hoặc exception mà primary pack còn thiếu
- dùng `references/cross-pack-orchestration.md` và `assets/templates/orchestration-brief.md` để khóa logic ghép pack

Ví dụ:
- dự án sơ cấp + pháp lý giao dịch -> `primary-project-sales-vi-v1` + `legal-transaction-ops-vi-v1`
- nha khoa nhiều ghế + implant/ortho -> `multi-chair-clinic-vi-v1` + `implant-ortho-heavy-vi-v1`
- phân phối + governance founder-led -> `trading-distribution-vi-v1` + `sme-ops-vi-v1`

## Cách bắt đầu tối thiểu
Nếu người dùng chưa mô tả rõ, hãy tự dựng một build brief tối giản gồm:
- twin này phục vụ team hoặc business area nào
- artefact nào cần ưu tiên trước
- ai sẽ dùng twin
- tài liệu nguồn có loại nào
- ngành, business model hoặc phân khúc con là gì nếu suy ra được
- có cần ghép thêm pack nào không

## Không chờ brief hoàn hảo
Khi đã có đủ nguồn và mục tiêu tương đối rõ, hãy bắt đầu build và ghi rõ assumptions thay vì hỏi quá nhiều.

## Luồng chi tiết theo mode
Sau khi chọn mode, đọc file instruction tương ứng để lấy checklist thực thi đầy đủ:
- **Build** → `references/mode-build-instructions.md` (11 bước: build brief → source manifest → corpus check → pack selection → normalization → evidence bank → process mapping → DNA synthesis → convergence → export → quality check)
- **Operate** → `references/mode-operate-instructions.md` (7 bước: đọc twin → xác định artefact → artifact adaptation → soạn nháp → tự chấm → sửa → trả bản cuối)
- **Update** → `references/mode-update-instructions.md` (5 bước: đọc twin cũ → ingest mới → so sánh → cập nhật → xuất changelog)
- **Audit** → `references/mode-audit-instructions.md` (6 bước: đọc twin → đọc artefact → chấm rubric → 3 đúng → 3 lệch → remediation)
