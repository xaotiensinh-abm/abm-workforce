---
name: writing-plans
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: "Sử dụng khi đã có bản thiết kế (Spec) hoàn chỉnh hoặc yêu cầu nhiều bước, BẮT BUỘC dùng để lập Hợp Đồng Code (Contract) trước khi tiến hành code thật."
---

# Lập Hợp Đồng Code (Writing Plans)

## Tổng Quan

Khi có Spec thiết kế, hãy lập Hợp Đồng Triển Khai (Implementation Plan) với giả định rằng Dev Worker sẽ code mà **không hề biết ngữ cảnh trước đó** của dự án. 

Văn bản này chính là Bản Giao Việc chuẩn ABM Workforce. Chia kế hoạch thành các task nhỏ cỡ "vài miếng cắn" (Bite-sized). Tuân thủ tối đa: DRY, YAGNI, TDD, và commit liên tục.

Giả định Worker là thợ gõ code giỏi, nhưng "mù tịt" về cấu trúc code hay hệ thống hiện tại của app. 

**Khai báo khi bắt đầu:** "Tôi sẽ dùng skill `writing-plans` để đúc bản Hợp Đồng Triển Khai."

**Lưu Hợp đồng tại:** `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`

## Rà Soát Phạm Vi Lần Cuối (Scope Check)

Nếu Spec nói nãy giờ bao phủ đến tận nhiều phân hệ độc lập, thì nên chia thành nhiều Hợp đồng rời rạc (1 Hợp đồng 1 tính năng). Mỗi hợp đồng phải đem lại một Output Testable độc lập.

## Kiến Trúc File

Trước khi list task, phải vạch ra rõ ràng **những file nào bị chạm đến**, và file nào được sinh ra mới. Khóa chặt phạm vi ảnh hưởng.
Đừng tạo file rác (1 file to 1000 dòng). Tách theo trách nhiệm (Single Responsibility Principle). Nếu thấy file hiện tại quá to, cứ mạnh dạn thêm 1 step Refactor vào.

## Độ Chia Nhỏ Của Task (Granularity)

**Mỗi Step chỉ là 1 khoảnh khắc gõ code (2-5 phút thao tác thao tác nhanh):**
- "Viết 1 file Test lỗi" - 1 Step
- "Chạy thử CLI xem báo lỗi đỏ chưa" - 1 Step
- "Đắp đoạn code bé tí ti vào để fix cho Test xanh lại" - 1 Step
- "Chạy lại Test thấy xanh xanh" - 1 Step
- "Gõ git commit" - 1 Step

## Mẫu Tiêu Đề Bắt Buộc 

**Moị Hợp đồng (Plan) PHẢI bắt đầu bằng Header sau:**

```markdown
# Hợp Đồng Triển Khai: [Tên Tính Năng]

> **Dành cho Agent:** BẮT BUỘC gọi SUB-SKILL `superpowers:subagent-driven-development` hoặc `superpowers:executing-plans` để code theo từng task của hợp đồng này. Đánh dấu checkbox (`- [ ]`) khi gõ xong mỗi Step.

**Mục Tiêu:** [1 câu tóm gọn cái sẽ xây]

**Kiến Trúc:** [2-3 dòng miêu tả cách tiếp cận]

**Tech Stack:** [VD: React, Node, SQL]

---
```

## Cấu Trúc Khung Rập Khuôn

```markdown
### Task 1: [Tên Component]

**Phạm Vi File (Scope):**
- Tạo mới: `exact/path/to/file.py`
- Sửa đổi: `exact/path/to/existing.py:123-145`
- File Test: `tests/exact/path/to/test.py`

- [ ] **Step 1: Viết test báo lỗi đỏ**

  ```python
  def test_specific_behavior():
      result = function(input)
      assert result == expected
  ```

- [ ] **Step 2: Chạy thử Test thấy thất bại**

  Chạy lệnh: `pytest tests/path/test.py::test_name -v`
  Kết quả hy vọng: Báo FAIL vì thiếu hàm

- [ ] **Step 3: Viết Code chống cháy bé nhất có thể**

  ```python
  def function(input):
      return expected
  ```

- [ ] **Step 4: Chạy lại Test thấy PASS**

  Chạy lệnh: `pytest tests/path/test.py::test_name -v`
  Kết quả: PASS xanh rờn
  
- [ ] **Step 5: Dọn dẹp Commit**

  ```bash
  git add tests/path/test.py src/path/file.py
  git commit -m "feat: add specific feature"
  ```
```

## Khắc Cốt Ghi Tâm
- Đường dẫn file LUÔN LUÔN ghi chính xác Absolute Path hoặc Relative chuẩn.
- Ghi thẳng Code nhúng vào văn bản (KHÔNG hướng dẫn chung chung trừu tượng).
- Lệnh chạy CLI phải dán sẵn nguyên si để tiện Copy-Paste.
- Đừng quên tư duy YAGNI (làm ít ăn nhiều).

## Vòng Lặp Duyệt Hợp Đồng (Plan Review)

Sau khi viết xong Hợp đồng:
1. Bạn hãy hỏi ý kiến `plan-document-reviewer` subagent. Ném Link file/path cho nó.
2. Nếu nó chê ❌: Lập tức Fix lại Hợp đồng và gọi nó Review lần 2. (AI viết thì AI tự sửa).
3. Nếu ✅ Approved: Đi tới bước Bàn Giao.

*Quá 3 vòng chưa duyệt xong thì vẫy cờ gọi CEO (Human) ra khuyên bảo.*

## Bàn Giao Triển Khai (Execution Handoff)

Lưu xong Hợp đồng, Mời CEO chọn đường hướng tác chiến:

**"Hợp đồng đã soạn xong ở `docs/superpowers/plans/<filename>.md`. Xin CEO đưa ra Lệnh triển khai:**

**1. Giao Subagent (Subagent-Driven - Highly Recommended):** Tôi sẽ cắt cử từng lính đánh thuê ra làm từng cái Task một, cứ múc xong 1 cục tôi xin báo cáo lại. Vừa đi vừa dò cho chắc. 
**2. Code Nguyên Khối (Inline Execution):** Tự tôi (Main Agent) sẽ làm hết từ A-Z dùng skill `executing-plans`, tôi tự check point định kỳ. 

**Giám đốc muốn ra chỉ thị số 1 hay số 2?"**
