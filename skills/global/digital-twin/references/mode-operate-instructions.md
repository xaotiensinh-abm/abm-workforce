# Mode Operate Instructions

Dùng mode này khi người dùng đã có twin pack hoặc mô tả rõ twin cần dùng, và muốn tạo hoặc chuẩn hóa artefact vận hành.

Artefact phổ biến gồm:
- sop
- playbook
- checklist
- onboarding guide
- role handbook
- memo
- meeting brief
- report template
- faq
- escalation note
- dashboard note

Thực hiện theo thứ tự:
1. đọc twin
2. xác định artefact đích
3. áp artifact adaptation
4. soạn nháp
5. tự chấm theo rubric
6. sửa một vòng
7. trả bản cuối

### bước 1: đọc twin
Ưu tiên đọc:
1. `twin.yaml`
2. `organization-dna.md`
3. `operating-model.md`
4. `process-catalog.md`
5. `decision-rules.md`
6. `role-handbook.md`
7. `activation-guide.md`
8. `knowledge-gaps.md`
9. `orchestration-map.md` hoặc `integration-risks.md` nếu twin có ghép pack

Nếu có mâu thuẫn giữa các file:
- ưu tiên `twin.yaml` làm canonical layer
- dùng tài liệu markdown để diễn giải và làm rõ

### bước 2: xác định artefact đích
Xác định một trong các loại sau:
- sop
- playbook
- checklist
- onboarding guide
- role handbook
- memo
- meeting brief
- report template
- faq
- escalation note
- dashboard note
- tài liệu khác gần với các loại trên

Nếu không rõ, chọn loại gần nhất với yêu cầu của người dùng.

### bước 3: áp artifact adaptation
Dựa trên `references/artifact-adaptations.md`, giữ:
- operating principles
- role clarity
- decision logic
- cadence và controls phù hợp

Cho phép co giãn:
- độ chi tiết
- độ formal
- mức độ giải thích nền
- số lượng ví dụ
- mức độ prescriptive hay advisory

Không biến twin thành đống văn bản chung chung. Mỗi artefact phải phản ánh cách doanh nghiệp thực sự vận hành.

### bước 4: soạn nháp
Khi soạn:
- bám scope của twin
- bám role map, process map, decision rules và metrics
- nếu twin có orchestration, làm rõ integration point giữa các pack và owner của từng handoff
- làm rõ owner, trigger, input, output, step, exception, escalation nếu artefact cần
- gọi ra coverage gap thay vì bịa chỗ chưa có bằng chứng

Không:
- bịa tool, vai trò, approval path hoặc sla không có chứng cứ
- suy ra chính sách nhạy cảm vượt quá nguồn
- nhầm process địa phương thành chuẩn toàn công ty

### bước 5: tự chấm theo rubric
Dựa trên `references/evaluation-rubric.md`, tự chấm ít nhất các trục:
- scope fidelity
- role clarity
- process fidelity
- decision fidelity
- metric and cadence fidelity
- artifact usability
- control awareness
- completeness without fabrication

Bản nháp chỉ nên được xem là đạt khi:
- scope fidelity không thấp
- process fidelity không thấp
- role clarity không thấp
- không vi phạm gap hoặc anti-pattern lớn

### bước 6: sửa một vòng
Sửa theo hướng:
- bỏ chỗ generic
- bỏ chỗ bịa owner hoặc approval
- làm rõ trigger, handoff, exception
- tăng khả năng dùng ngay của artefact
- nêu rõ open questions nếu thiếu dữ liệu

### bước 7: trả bản cuối
Trả artefact ở trạng thái đã tự hiệu chỉnh.
Nếu phù hợp, có thể kèm:
- note về assumptions
- checklist triển khai
- danh sách thông tin còn thiếu để hoàn thiện bản chính thức
