# Output Contract: Digital Twin Pack (L7)

Kế thừa tiêu chuẩn: [Ops Contract](file:///C:/Users/PC/.gemini/antigravity/skills/_standards/output-contracts/ops.md)

Mỗi "Twin Pack" được xuất bởi skill `digital-twin` phải tuân thủ cấu trúc sau:

## 1. File Manifest
- Phải có file `twin.yaml` chứa cấu trúc máy đọc (L7.1).
- Phải có ít nhất 3 file tài liệu đi kèm (DNA, Process, Roles).

## 2. Evidence Integrity
- Mọi quy trình trong `process-catalog.md` phải có "Source Evidence" (Reference tới số dòng hoặc screenshot).
- Tuyệt đối không có "Hallucinated Fields" (SLA, Tool, hoặc Cost không có trong input).

## 3. Convergent Thinking
- Phân loại rõ ràng 100% các logic thành:
  - **Invariants**: Quy tắc cứng (100% frequency).
  - **Tendencies**: Thói quen (70-90% frequency).
  - **Accidents**: Sự kiện ngẫu nhiên (<10% frequency).

## 4. Format Standards
- Ngôn ngữ: Ưu tiên Tiếng Việt (Vietnamese locale focus).
- Mermaid Diagrams: Bắt buộc cho `orchestration-map.md`.
- Checklist: Mọi task trong `activation-guide.md` phải có dạng `[ ]`.

## 5. Metadata Header
Mỗi file tài liệu phải chứa header:
```markdown
---
twin_id: [ID]
version: [X.Y.Z]
confidence_score: [0-100%]
last_synced: [Date]
---
```
