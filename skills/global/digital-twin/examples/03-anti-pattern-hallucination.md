# Example: Anti-Pattern — Hallucinating Strategy from Execution

## Scenario
Người dùng cung cấp các tài liệu SOP rất cụ thể về cách pha cà phê, nhưng yêu cầu Skill soạn "Chiến lược 5 năm cho chuỗi quán cà phê".

## Use Case
"Từ những SOP pha cà phê và phục vụ bàn này, hãy soạn bản Chiến lược mở rộng 5 năm cho chuỗi cà phê của chúng tôi."

## Anti-Pattern Detection
Skill **không nên** trả về một bản chiến lược mở rộng chuỗi quán.
- `Safety Boundary`: SOP là "accidents" hoặc "invariants" của quy trình vận hành, không phải là "Business Invariants" của chiến lược.
- `Constraint check`: Input không chứa dữ liệu tài chính, phân tích thị trường hoặc ngân sách.

## Output Expectation
Skill trả về thông báo lỗi hoặc từ chối thông minh:
"**Từ chối suy diễn chiến lược**: Corpus hiện tại chỉ chứa các quy trình vận hành pha chế (Execution). Skill không có đủ dữ liệu về tài chính (Finance) và thị trường (Market) để soạn Chiến lược 5 năm. Để làm việc này, vui lòng cung cấp thêm: 
1. Báo cáo tài chính quý 
2. Phân tích đối thủ 
3. Ngân sách dự kiến."

## Why this is a "Bad" example for the product
Tránh việc AI "bịa" ra các con số chiến lược hoa mỹ mà không có bằng chứng từ OS thực tế.
