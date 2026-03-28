# Example: Edge Case — Auditing with Low-Confidence Sources

## Scenario
Người dùng cung cấp một URL công khai và một screenshot mờ của một quy trình cũ, sau đó yêu cầu audit quy trình hiện tại dựa trên "mớ hỗn độn" này.

## User Input
"Audit cái SOP này giùm tôi, xem có đúng với tinh thần của cái link (nhấp vào link) và cái hình này (screenshot đính kèm) không."

## AI Strategy (L2 Instructions)
1.  **Source Validation**: Identify the screenshot as "Low Confidence" because it's blurry.
2.  **Conflict Resolution**: Use `references/convergence-rules.md` to identify contradictions between the URL (new) and screenshot (old).
3.  **Confidence Tagging**: Skill sẽ không audit một cách tuyệt đối mà trả về: "Audit Report (Confidence: Low - Mixed Sources)".
4.  **Remediation Suggestion**: Đề xuất người dùng chép tay (manual transcription) screenshot hoặc tìm file gốc PDF để tăng độ chính xác.

## Output Structure
- **Drift Identification**: Chỉ ra 2 điểm URL quy định bước X, nhưng thực tế Screenshot yêu cầu bước Y.
- **Safety Boundary**: Tuyệt đối không suy diễn SLA từ screenshot nếu không đọc được số rõ ràng.
