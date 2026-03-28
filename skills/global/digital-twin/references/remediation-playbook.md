# Remediation playbook

Khi audit phát hiện lệch nhiều, sửa theo thứ tự ưu tiên sau:

## Thứ tự sửa (Scope → Logic → Wording)
1. **Khóa lại scope** — twin đại diện cho team/process nào? Scope sai thì mọi thứ sai.
2. **Làm rõ role và owner** — ai chịu trách nhiệm chính? Ai duyệt? Ai escalate?
3. **Sửa process steps và handoff** — trigger → steps → output có đúng thứ tự không? Handoff có rõ người nhận?
4. **Sửa decision rules và approval layers** — điều kiện rẽ nhánh, ngưỡng phê duyệt, exception path.
5. **Thêm exception, escalation, control** — khi quy trình bị phá vỡ thì đi đâu?
6. **Thêm metric hoặc cadence** — đo gì, theo nhịp nào, ai review?
7. **Cuối cùng mới sửa wording và format** — chỉ polish khi logic đã đúng.

## Khi nào nên viết lại thay vì sửa
- Khi scope fidelity < 3 (artefact đang nói về scope sai hẳn)
- Khi role clarity < 2 (owner bị bịa hoặc sai hoàn toàn)
- Khi artefact bịa process không có trong twin

## Khi nào chỉ cần sửa nhẹ
- Khi scope và role đúng nhưng thiếu exception hoặc escalation
- Khi metric cadence chưa khớp nhưng process flow đúng
- Khi wording quá generic nhưng logic nền đúng

## Template remediation plan
```markdown
# Remediation Plan

## Artefact: [tên artefact được audit]
## Audit score tổng: [x/5]

### Vấn đề ưu tiên cao
1. [Mô tả vấn đề] → [Hướng sửa] → [Owner]

### Vấn đề ưu tiên trung bình
1. [Mô tả vấn đề] → [Hướng sửa]

### Open questions (cần thêm data)
1. [Câu hỏi]

### Timeline đề xuất
- [ ] Phase 1: Sửa scope và role (ngay)
- [ ] Phase 2: Sửa process và decision (trong tuần)
- [ ] Phase 3: Bổ sung metric, control và polish (tuần sau)
```
