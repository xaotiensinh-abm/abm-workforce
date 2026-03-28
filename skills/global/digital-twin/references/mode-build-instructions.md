# Mode Build Instructions

## quy tắc intake chung
Khi nhận nguồn mới:
1. nếu người dùng chưa nói rõ mục tiêu build, tự tạo **build brief** theo `assets/templates/build-brief.md`
2. lập **source manifest** nội bộ cho từng nguồn
3. ghi lại tối thiểu:
   - source id
   - source type: upload | pasted_text | url
   - artifact type ước tính: sop | policy | report | memo | deck | meeting_notes | template | onboarding | faq | checklist | dashboard_note | unknown
   - title hoặc nhãn ngắn
   - business area hoặc team nếu suy ra được
   - language
   - estimated word count
   - quality note
4. đánh giá độ đủ của corpus trước khi rút kết luận mạnh

Dùng các ngưỡng thực tế sau:
- **high confidence**: khoảng 5000+ từ, có hơn một nguồn mạnh, và có ít nhất hai loại artefact khác nhau
- **usable**: khoảng 2000 đến 5000 từ
- **provisional**: dưới 2000 từ hoặc chỉ có một loại artefact hẹp
- **mixed source warning**: có dấu hiệu nhiều đội, nhiều cấp quyết định hoặc nhiều ngữ cảnh mâu thuẫn chưa được tách scope

Không giả vờ chắc chắn khi corpus yếu. Khi cần, gắn:
- `confidence: low`
- `status: provisional`
- `mixed_source_warning`
- `coverage_gaps`

## quy tắc weighting nguồn
Không coi mọi nguồn có giá trị như nhau.

Ưu tiên cao hơn cho:
- sop hoặc runbook có bước rõ
- policy có rule và exception rõ
- report định kỳ có metric và nhịp vận hành
- memo quyết định có owner, scope, deadline, escalation
- onboarding guide hoặc role handbook đã được dùng thật

Ưu tiên trung bình cho:
- meeting notes
- deck chiến lược
- dashboard notes
- faq nội bộ
- checklist đã có owner và tần suất

Ưu tiên thấp hơn hoặc chỉ dùng bổ trợ cho:
- one-off note thiếu ngữ cảnh
- slide khẩu hiệu hoặc thông điệp thương hiệu
- tài liệu ngắn chỉ mô tả outcome mà không mô tả quy trình
- screenshot ít chữ hoặc cắt rời ngữ cảnh

Không dựng “luật twin” chỉ từ:
- một câu slogan đẹp
- một deck vision đơn lẻ
- một báo cáo quý duy nhất
- một tài liệu campaign quá đặc thù bối cảnh

## mode: build
Dùng mode này khi người dùng muốn dựng twin doanh nghiệp từ nguồn mới.

Thực hiện theo thứ tự:
1. tạo build brief tối thiểu
2. tạo source manifest
3. đánh giá corpus adequacy và scope
4. nếu cần, chọn primary pack và adjacent packs rồi tạo orchestration brief
5. chuẩn hóa nguồn
6. tạo evidence bank
7. map operating system
8. tổng hợp enterprise twin dna
9. phân loại invariants, tendencies, accidents
10. xuất twin pack
11. tự kiểm chất lượng

### bước 1: tạo build brief tối thiểu
Nếu người dùng chưa nói rõ mục tiêu sử dụng twin, tự tạo brief ngắn theo `assets/templates/build-brief.md` với các trường tối thiểu:
- mục tiêu chính của twin
- business area hoặc team ưu tiên
- loại artefact đầu ra ưu tiên
- người dùng chính của twin
- phạm vi thời gian hoặc nhịp vận hành
- có cần ghép pack nào không
- điều cần tránh hoặc chưa chắc

Không chặn workflow chỉ vì thiếu brief hoàn hảo. Nếu đã đủ nguồn và mục tiêu tương đối rõ, tạo brief mặc định rồi tiếp tục.

### bước 2: tạo source manifest
Lập manifest cho toàn bộ nguồn vào.

Nếu là **upload**:
- xác định loại file
- lấy text sạch nếu được
- giữ heading, table header, bullet, owner, sla, rule, exception, deadline, metric, decision line
- bỏ phần lặp thừa như header hoặc footer khi có thể

Nếu là **pasted text**:
- tách theo block hợp lý
- nếu có dấu hiệu là nhiều tài liệu khác nhau, xem mỗi block là một source riêng
- giữ nguyên thứ tự block để tránh mất ngữ cảnh quyết định

Nếu là **public url**:
- đọc theo `references/url-ingestion-rules.md`
- ưu tiên main content
- bỏ nav, footer, sidebar, related posts, comments, widgets
- giữ title, author, date nếu trích được
- nếu không lấy được nội dung chính, báo rõ và yêu cầu file hoặc pasted text

### bước 3: đánh giá corpus adequacy và scope
Trả lời nội bộ các câu hỏi sau:
- scope có đủ hẹp để dựng một twin nhất quán chưa
- có đang trộn nhiều business unit hoặc nhiều cấp điều hành không
- có đủ text để thấy trigger, step, handoff, owner, metric và control lặp lại chưa
- có loại artefact nào đang áp đảo quá mức không
- có nguồn nào quá yếu hoặc quá nhiễu cần giảm trọng số không

Nếu corpus yếu:
- vẫn có thể build
- nhưng phải gắn `status: provisional`
- và phải nêu rõ giới hạn trong `convergence-report.md` và `knowledge-gaps.md`

### bước 4: chọn pack và orchestration khi cần
Nếu scope khớp rõ với một ngành hoặc sub-segment, chọn sample pack gần nhất làm khung tham chiếu.

Nếu case cần ghép nhiều motion hoặc governance layer:
- chọn **primary pack** gần business model nhất
- chọn 1–2 **adjacent packs** cho handoff, legal, governance hoặc treatment cadence
- điền `assets/templates/orchestration-brief.md`
- tạo `assets/templates/orchestration-map.md` nếu cần mô tả integration points
- chỉ dùng pack mẫu để mượn cấu trúc, không sao chép facts

### bước 5: chuẩn hóa nguồn
Chuẩn hóa theo `references/source-normalization.md`.
Mục tiêu:
- giữ lại authored content liên quan đến vận hành
- bỏ phần trang trí, điều hướng và nội dung hệ thống không liên quan
- giữ cấu trúc có ý nghĩa như heading, step list, approvals, owner, exception, risk note, metric, cadence

Không làm phẳng hoàn toàn văn bản nếu việc đó làm mất tín hiệu role, handoff hoặc decision rule.

### bước 6: tạo evidence bank
Dựa trên `references/evidence-bank-schema.md`, chia nguồn thành các **evidence units** có chức năng rõ.

Mỗi evidence unit nên được gắn nhãn nội bộ theo các vai trò như:
- trigger
- input
- step
- owner
- handoff
- decision_rule
- exception
- approval
- metric
- cadence
- control
- escalation
- output

Khi tạo evidence bank:
- ưu tiên những đoạn có tín hiệu vận hành rõ
- giữ trích đoạn đủ dài để không mất ngữ cảnh
- tránh lấy câu một mình nếu câu đó không đủ để suy ra cách doanh nghiệp vận hành

### bước 7: map operating system
Dựa trên `references/process-mapping-rules.md` và `references/organization-dna-schema.md`, map các lớp sau:
- business scope và service boundaries
- core roles và responsibilities
- core processes và trigger map
- inputs, outputs, handoff, sla
- decision rules, approval layers, exception paths
- systems, templates, data dependencies
- metrics, reporting cadence, review loops
- controls, failure points, escalation paths
- operating principles và style of execution

### bước 8: tổng hợp enterprise twin dna
Từ evidence bank và process mapping, tổng hợp twin thành:
- lớp human-readable
- lớp machine-readable

Lớp human-readable tối thiểu:
- `organization-dna.md`
- `operating-model.md`
- `process-catalog.md`
- `decision-rules.md`
- `role-handbook.md`
- `metric-cadence.md`
- `system-landscape.md`
- `activation-guide.md`
- `orchestration-map.md` nếu audit case ghép pack
- `convergence-report.md`
- `knowledge-gaps.md`

Lớp machine-readable tối thiểu:
- `twin.yaml`

### bước 9: phân loại convergence
Dựa trên `references/convergence-rules.md`, phân loại từng kết luận thành:
- **invariant**: pattern vận hành lặp lại đủ mạnh và đủ rộng
- **tendency**: pattern khá rõ nhưng chưa đủ phủ
- **accident**: pattern lẻ, gắn với một giai đoạn, một manager hoặc một tình huống đặc biệt

Không biến tendency thành invariant nếu bằng chứng chưa đủ.

### bước 10: xuất twin pack
Khi build xong, xuất **twin pack** có cấu trúc nhất quán.
Twin pack tối thiểu phải có:
- `twin.yaml`
- `organization-dna.md`
- `operating-model.md`
- `process-catalog.md`
- `decision-rules.md`
- `role-handbook.md`
- `metric-cadence.md`
- `system-landscape.md`
- `activation-guide.md`
- `orchestration-map.md` nếu audit case ghép pack
- `convergence-report.md`
- `knowledge-gaps.md`

Nếu case có orchestration, nên thêm:
- `orchestration-brief.md`
- `orchestration-map.md`
- `integration-risks.md`

Nếu đủ mạnh, nên thêm:
- `source-manifest.md`
- `evidence-map.md`
- `control-risks.md`
- `operating-playbook.md`
- `onboarding-guide.md`
- `meeting-brief.md`
- `report-template.md`
- `audit-scorecard.md`

### bước 11: tự kiểm chất lượng
Trước khi trả kết quả build:
- kiểm tra twin có đang overfit một tài liệu nổi bật không
- kiểm tra mixed source warning có cần bật không
- kiểm tra coverage gaps có đủ trung thực không
- kiểm tra role, process, decision, metric có khớp nhau không
- nếu có `scripts/validate_twin_yaml.py`, chạy validator lên `twin.yaml` trước khi kết luận pack đã ổn
