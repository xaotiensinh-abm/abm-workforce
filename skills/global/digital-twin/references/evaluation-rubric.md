# Evaluation rubric

Chấm thang 1 đến 5 cho các trục sau:

## 8 trục đánh giá

### 1. Scope fidelity
- **5**: artefact bám đúng team, process, business area mà twin mô tả
- **4**: đúng scope chính, có 1-2 chỗ mở rộng hơi quá
- **3**: scope đúng ở mức khung nhưng lẫn vài scope khác
- **2**: scope lệch rõ, artefact nói về team/process khác
- **1**: scope sai hoàn toàn

### 2. Role clarity
- **5**: owner, approval, escalation rõ ràng và khớp twin
- **4**: role đúng, có 1-2 handoff chưa rõ
- **3**: role ở mức chung, thiếu owner cụ thể ở vài step
- **2**: owner bị bịa hoặc nhầm vai trò
- **1**: không có role nào khớp twin

### 3. Process fidelity
- **5**: trigger, steps, handoff, output khớp twin chính xác
- **4**: flow đúng, thiếu 1-2 exception hoặc edge case
- **3**: flow đúng ở mức đại cương, thiếu chi tiết quan trọng
- **2**: flow sai thứ tự hoặc thiếu bước chính
- **1**: flow bịa hoặc không liên quan

### 4. Decision fidelity
- **5**: decision rules, approval layers, exception paths khớp twin
- **4**: decision đúng, có 1-2 exception chưa cover
- **3**: decision ở mức generic, thiếu ngưỡng hoặc điều kiện cụ thể
- **2**: decision sai logic hoặc approval bị bịa
- **1**: không có decision nào từ twin

### 5. Metric and cadence fidelity
- **5**: metric, review cadence, reporting nhịp khớp twin
- **4**: metric đúng, cadence hơi lệch
- **3**: có metric nhưng chưa khớp twin rõ
- **2**: metric bị bịa hoặc cadence sai
- **1**: không có metric hoặc cadence

### 6. Control awareness
- **5**: checkpoint, QA gate, audit trail, compliance rõ ràng
- **4**: control đúng ở các step chính, thiếu ở edge case
- **3**: có nhắc đến control nhưng chưa cụ thể
- **2**: thiếu control quan trọng
- **1**: không có control nào

### 7. Artifact usability
- **5**: dùng được ngay, rõ ràng, actionable, không cần sửa
- **4**: dùng được, cần sửa nhỏ
- **3**: cần sửa trung bình để dùng thực tế
- **2**: khó dùng vì quá generic hoặc thiếu context
- **1**: không dùng được

### 8. Completeness without fabrication
- **5**: đầy đủ, mọi thông tin đều có bằng chứng, gap được gọi rõ
- **4**: đầy đủ phần lớn, gap nhỏ được nêu
- **3**: có chỗ bịa nhẹ hoặc suy diễn quá mức
- **2**: bịa nhiều chi tiết không có trong twin
- **1**: phần lớn nội dung bị bịa

## Quality gate
Bản nháp chỉ nên coi là đạt khi:
- scope fidelity >= 4
- process fidelity >= 4
- role clarity >= 4
- completeness without fabrication >= 4

## Anti-patterns phổ biến
- Mọi artefact đều đạt 5/5 → AI đang không đánh giá thật, cần kiểm tra lại
- Scope fidelity = 5 nhưng process fidelity = 2 → khả năng đang copy scope từ twin nhưng bịa process
- Completeness = 5 nhưng knowledge-gaps trống → không trung thực về giới hạn corpus
