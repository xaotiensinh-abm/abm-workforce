# Mode Audit Instructions

Dùng mode này khi người dùng muốn kiểm tra twin hoặc tài liệu vận hành theo twin.

Audit phổ biến gồm:
- tài liệu có phản ánh đúng cách doanh nghiệp vận hành không
- process có đủ owner, step, handoff, exception, escalation chưa
- các artefact có mâu thuẫn nhau không
- twin có thiếu coverage ở đâu
- có drift giữa policy, sop và báo cáo hay không

Thực hiện theo thứ tự:
1. đọc twin
2. đọc artefact hoặc bộ artefact cần audit
3. chấm theo rubric
4. nêu điểm đúng
5. nêu điểm lệch hoặc thiếu
6. đề xuất remediation plan

### bước 1: đọc twin
Ưu tiên:
- `twin.yaml`
- `organization-dna.md`
- `process-catalog.md`
- `decision-rules.md`
- `knowledge-gaps.md`
- `activation-guide.md`
- `orchestration-map.md` nếu audit case ghép pack

### bước 2: đọc artefact cần audit
Xác định:
- artefact type
- scope team hoặc process
- owner và audience nếu có
- phần nào là trigger, step, decision, exception, escalation, metric

### bước 3: chấm theo rubric
Chấm ít nhất các trục:
- scope fidelity
- role clarity
- process fidelity
- decision fidelity
- metric and cadence fidelity
- control awareness
- usability
- completeness without fabrication

### bước 4: nêu điểm đúng
Nêu **3 điểm đúng nhất**:
- điều gì đã bám twin
- cơ chế vận hành nào đang phản ánh đúng
- chỗ nào đủ rõ để dùng ngay

### bước 5: nêu điểm lệch hoặc thiếu
Nêu **3 điểm lệch hoặc thiếu lớn nhất**:
- sai scope ở đâu
- sai role, handoff hoặc approval ở đâu
- thiếu exception, metric, escalation hoặc control ở đâu
- có vi phạm anti-pattern nào không

### bước 6: đề xuất remediation plan
Nếu người dùng muốn sửa:
- điền `assets/templates/remediation-plan.md`
- đề xuất thứ tự sửa: scope -> role -> process -> decision -> control -> metric -> wording
- viết lại tài liệu quan trọng nếu cần
- không giả vờ lấp đầy gap khi bằng chứng chưa có
