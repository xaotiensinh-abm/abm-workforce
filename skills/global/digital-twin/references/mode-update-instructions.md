# Mode Update Instructions

Dùng mode này khi người dùng đã có twin pack và muốn bổ sung tài liệu mới.

Thực hiện theo thứ tự:
1. đọc twin hiện có
2. ingest nguồn mới
3. so với dna cũ
4. cập nhật có kiểm soát
5. xuất bản cập nhật và changelog

### bước 1: đọc twin hiện có
Ưu tiên đọc:
- `twin.yaml`
- `organization-dna.md`
- `process-catalog.md`
- `decision-rules.md`
- `convergence-report.md`
- `knowledge-gaps.md`

Mục tiêu là hiểu cái gì đang là invariant, tendency, accident, và gap nào còn mở.

### bước 2: ingest nguồn mới
Áp cùng intake rules như build mode:
- tạo source manifest cho nguồn mới
- chuẩn hóa
- tạo evidence units mới

### bước 3: so với twin cũ
Tự hỏi:
- nguồn mới xác nhận invariant cũ hay làm yếu nó
- có process mới, role mới, system mới hoặc rule mới đủ mạnh để thêm vào không
- có thay đổi thật trong vận hành hay chỉ là thay đổi cục bộ của một team
- có drift theo thời gian, theo công cụ hoặc theo lãnh đạo không

### bước 4: cập nhật có kiểm soát
Chỉ cập nhật khi evidence đủ mạnh.
Quy tắc:
- không hạ invariant cũ chỉ vì vài nguồn mới yếu
- không nâng tendency lên invariant nếu chưa đủ phủ
- nếu có xung đột giữa nguồn cũ và mới, nêu rõ trong `knowledge-gaps.md` hoặc changelog
- nếu update làm scope rộng hơn, nói rõ twin đã đổi phạm vi

### bước 5: xuất bản cập nhật
Xuất twin pack phiên bản mới với:
- `twin.yaml` cập nhật
- tài liệu human-readable cập nhật
- `convergence-report.md` cập nhật
- nếu có orchestration, cập nhật lại `orchestration-map.md` và `integration-risks.md`
- `assets/templates/update-changelog.md` điền đầy đủ
