---
name: digital-twin
description: dựng và vận hành digital-twin doanh nghiệp từ sop, policy, quy trình, báo cáo, memo, deck, meeting notes, template và tài liệu vận hành; dùng khi cần đóng gói cách doanh nghiệp hoạt động, tạo twin pack tái sử dụng, nhân bản playbook, soạn role handbook, process catalog, decision rules, reporting cadence, onboarding guide, audit độ phủ và drift giữa tài liệu với vận hành thực tế, hoặc ghép nhiều pack ngành và phân khúc để mô hình hóa hệ vận hành liên phòng ban.
---

# Goal
Đóng gói, chuẩn hóa và tái sử dụng operating system của doanh nghiệp dưới dạng Digital Twin, đảm bảo "evidence-first" để chống AI hallucination. Dựng và vận hành digital-twin của doanh nghiệp từ các nguồn tri thức phân mảnh.

# Examples

## Ví dụ 1: Build Mode — Ingest nguồn và dựng twin
**User Input**: "Tạo twin từ SOP quản lý kho này: Bước 1 Nhận hàng, Bước 2 Phân loại, Bước 3 Nhập kho (Chỉ định: Thủ kho duyệt)."
**AI Action**: Đọc `references/mode-build-instructions.md` → tạo source manifest → trích evidence (owner: Thủ kho, trigger: Nhận hàng, steps: 3) → xuất `twin.yaml` + `process-catalog.md` + `role-handbook.md` + `knowledge-gaps.md`.

## Ví dụ 2: Operate Mode — Tạo artefact từ twin
**User Input**: "Dùng twin này để soạn onboarding guide cho nhân sự mới trong team support."
**AI Action**: Đọc `references/mode-operate-instructions.md` → đọc twin hiện có → xác định artefact: onboarding_guide → áp `artifact-adaptations.md` → soạn nháp (role context, tuần 1-4, tài liệu cần đọc, review cadence) → tự chấm theo rubric → trả bản cuối.

## Ví dụ 3: Audit Mode — Kiểm tra drift
**User Input**: "Audit SOP xử lý escalation này theo twin hiện có."
**AI Action**: Đọc `references/mode-audit-instructions.md` → đọc twin → so SOP với decision-rules & process-catalog → chấm 8 trục (scope, role, process, decision...) → nêu 3 điểm đúng + 3 điểm lệch → đề xuất remediation plan.

*(Thêm 13 ví dụ ngành cụ thể tại `references/examples.md` và 56 prompt mẫu tại `references/sample-prompts-vi.md`)*

# Instructions
Xác định mode trước khi làm:
- **build**: khi người dùng muốn dựng twin doanh nghiệp từ tài liệu mới. **Đọc CẤP TỐC hướng dẫn chi tiết tại `references/mode-build-instructions.md`.**
- **operate**: khi người dùng muốn dùng twin để tạo hoặc chuẩn hóa artefact vận hành. **Đọc CẤP TỐC hướng dẫn chi tiết tại `references/mode-operate-instructions.md`.**
- **update**: khi người dùng muốn bổ sung tài liệu mới vào twin hiện có. **Đọc CẤP TỐC hướng dẫn chi tiết tại `references/mode-update-instructions.md`.**
- **audit**: khi người dùng muốn kiểm tra độ phủ, độ nhất quán hoặc độ lệch giữa twin và tài liệu vận hành. **Đọc CẤP TỐC hướng dẫn chi tiết tại `references/mode-audit-instructions.md`.**

Luôn tuân theo các nguyên tắc sau:
- làm theo hướng **evidence-first**
- dựng lại **operating system** của doanh nghiệp, không dựng lại danh tính cá nhân riêng tư
- phân biệt rõ **invariants**, **tendencies** và **accidents**
- không kết luận mạnh nếu corpus yếu, chồng chéo hoặc lẫn nhiều đội/ngữ cảnh
- luôn nêu **confidence level**, **coverage gaps** và **open questions** khi build hoặc update
- ưu tiên tiếng việt; nếu nguồn pha nhiều ngôn ngữ hoặc thiếu ngữ cảnh doanh nghiệp, gắn cảnh báo về độ tin cậy

## tài nguyên cần đọc khi cần
- đọc `references/getting-started.md` để chọn luồng bắt đầu nhanh trong chat
- đọc `references/mode-detection.md` khi cần phân loại yêu cầu vào build, operate, update hoặc audit
- đọc `references/intake-build-brief.md` khi cần tạo brief đầu vào tối thiểu
- đọc `references/source-normalization.md` khi cần chuẩn hóa sop, policy, memo, report, notes hoặc deck
- đọc `references/url-ingestion-rules.md` khi cần ingest public url
- đọc `references/evidence-bank-schema.md` khi cần trích bằng chứng vận hành
- đọc `references/process-mapping-rules.md` khi cần map role, handoff, trigger, input, output và control
- đọc `references/organization-dna-schema.md` khi cần tổng hợp operating dna của doanh nghiệp
- đọc `references/twin-yaml-schema.md` khi cần xuất `twin.yaml`
- đọc `references/artifact-adaptations.md` khi cần tạo artefact mới từ twin
- đọc `references/convergence-rules.md` khi cần phân loại invariants, tendencies, accidents
- đọc `references/evaluation-rubric.md` khi cần tự chấm hoặc audit
- đọc `references/safety-boundaries.md` khi gặp ranh giới an toàn hoặc rủi ro suy diễn quá mức
- đọc `references/examples.md` khi cần case mẫu
- đọc `references/sample-prompts-vi.md` khi cần prompt mẫu để gọi build, operate, update hoặc audit
- đọc `references/industry-packs-vn.md` khi case thuộc bất động sản, phòng khám nha khoa hoặc SMEs tại Việt Nam
- đọc `references/industry-subpacks-vn.md` khi cần chọn đúng phân khúc con trong từng ngành
- đọc `references/cross-pack-orchestration.md` khi case cần ghép nhiều pack
- đọc `references/orchestration-patterns-vn.md` khi case thuộc các pattern orchestration phổ biến ở Việt Nam
- đọc `references/sample-twin-pack-walkthrough.md` và `references/sample-pack-selection.md` khi cần sample twin pack tham chiếu gần nhất
- đọc `references/remediation-playbook.md` khi cần biến audit thành kế hoạch khắc phục

## đầu vào hỗ trợ
Hỗ trợ ba loại đầu vào:
- **upload**: sop, policy, deck, memo, report, template, pdf, docx, markdown, text, screenshot có chữ rõ
- **pasted text**: một hoặc nhiều khối nội dung người dùng dán trực tiếp
- **public url**: url truy cập công khai và đọc được nội dung chính

Không dựa vào:
- private url cần login
- trang paywall
- trang render động không lấy được nội dung chính
- audio hoặc video thô chưa có transcript
- nguồn không đọc được chữ rõ ràng

Nếu nguồn không đọc được hoặc quá nhiễu:
- nói rõ nguồn nào có vấn đề
- nêu lý do vì sao nguồn đó yếu
- yêu cầu người dùng dán text hoặc tải file lên nếu cần

## quy tắc bắt đầu nhanh
Khi người dùng muốn dùng skill ngay trong chat:
- đọc `references/getting-started.md` để chọn luồng nhanh phù hợp
- nếu yêu cầu còn mơ hồ nhưng đã đủ để hành động, ưu tiên tạo build brief tối thiểu và bắt đầu build thay vì hỏi quá nhiều
- nếu người dùng đã có twin pack, ưu tiên vào operate, update hoặc audit trực tiếp
- nếu có sample twin pack phù hợp, đọc `references/sample-twin-pack-walkthrough.md` và `references/sample-pack-selection.md` để bám cấu trúc, mức chi tiết và cách phân rã quy trình
- nếu case thuộc bất động sản, phòng khám nha khoa hoặc doanh nghiệp SMEs tại Việt Nam, đọc thêm `references/industry-packs-vn.md` rồi chọn pack ngành gần nhất làm điểm tham chiếu
- nếu tài liệu cho thấy phân khúc con rõ ràng như dự án sơ cấp, resale, legal ops, single clinic, multi-chair, implant, agency, phân phối hoặc sản xuất nhẹ, đọc thêm `references/industry-subpacks-vn.md` và chọn sub-pack gần nhất làm khung chính
- nếu case đi qua nhiều motion hoặc có handoff rõ giữa nhiều sub-packs, đọc `references/cross-pack-orchestration.md`, tạo `assets/templates/orchestration-brief.md` và dùng primary pack + adjacent packs thay vì cố nhồi tất cả vào một pack

## quy tắc về output

### khi build hoặc update
Luôn cố gắng xuất đầy đủ twin pack.
Tối thiểu phải có:
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

### khi operate
Trả artefact đã được tự kiểm.
Nếu phù hợp, có thể kèm:
- assumptions rõ ràng
- checklist triển khai
- open questions còn thiếu dữ liệu

### khi audit
Luôn có:
- điểm tổng quan
- điểm theo trục
- 3 điểm đúng nhất
- 3 điểm lệch hoặc thiếu lớn nhất
- remediation plan hoặc hướng sửa

# Constraints
Mục tiêu của skill này là:
- dựng lại **song sinh số vận hành** của doanh nghiệp hoặc một phần doanh nghiệp
- đóng gói và nhân bản cách vận hành thành twin pack tái sử dụng
- giúp tạo playbook, handbooks, report templates, onboarding guides và artefact vận hành khác
- nhưng vẫn trung thực với chất lượng bằng chứng và độ phủ tài liệu

Không bao giờ:
- tuyên bố twin là sự thật tuyệt đối về doanh nghiệp nếu corpus còn hẹp
- bịa vai trò, process, approval path, sla, metric hoặc tool không có bằng chứng
- suy ra dữ liệu nhạy cảm, chiến lược bí mật hoặc quyết định pháp lý vượt quá nguồn
- trộn nhiều scope khác nhau rồi gọi đó là một twin thống nhất
- che giấu mixed source risk hoặc coverage gaps

Luôn làm rõ:
- mức confidence
- giới hạn của corpus
- phần nào là invariant
- phần nào chỉ là tendency
- phần nào chưa đủ chắc để áp cứng
- twin này đại diện cho team, quy trình hay phạm vi nào
