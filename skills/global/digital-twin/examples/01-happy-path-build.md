# Example: Happy Path — Building a Store Management Twin

## Scenario
Xây dựng một Digital Twin cho bộ phận quản lý kho của một công ty thương mại điện tử nhỏ. Dữ liệu đầu vào là một SOP chi tiết dạng văn bản.

## User Input
"Tạo twin từ SOP quản lý kho này: 
1. Nhận hàng: Kiểm tra số lượng và chất lượng sản phẩm từ nhà cung cấp. 
2. Phân loại: Dán nhãn mã vạch theo SKU. 
3. Nhập kho: Di chuyển hàng vào khu vực chỉ định. 
Thủ kho là người duyệt cuối cùng cho mỗi bước."

## Output Expectation
- **Twin.yaml**: Chứa 3 quy trình con với role "Thủ kho".
- **Evidence Map**: Trích xuất đúng các logic: "Kiểm hàng" → "Dán nhãn" → "Chỉ định chỗ".
- **Gap Analysis**: Tự động nhận diện việc thiếu "Tiêu chí kiểm hàng" (Audit gate) là một gap.

## Strategic Reasoning
Skill sẽ tự động đọc `references/mode-build-instructions.md`, áp dụng `source-normalization.md` để cấu trúc lại text thô thành OS model. Nó sẽ không bịa ra SLA (thời gian xử lý) vì input không cung cấp, nhưng sẽ gắn nhãn "Invariants" cho các bước bắt buộc.
