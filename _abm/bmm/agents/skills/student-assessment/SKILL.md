---
name: student-assessment
description: "Đánh giá học viên AI — rubrics, quiz design, project-based assessment, certification criteria"
---

# Đánh Giá Học Viên — Student Assessment

## Mục đích
Skill này giúp thiết kế hệ thống đánh giá học viên toàn diện cho khóa đào tạo AI.

## 4 Loại Đánh Giá

### 1. Quiz / Trắc nghiệm
**Khi dùng:** Kiểm tra kiến thức lý thuyết sau mỗi module

```yaml
quiz_design:
  questions_per_quiz: 10-15
  time_limit: "15-20 phút"
  pass_score: 70
  attempts: 3
  question_types:
    - multiple_choice: 40%    # Chọn 1 đáp án đúng
    - multiple_select: 20%    # Chọn nhiều đáp án đúng
    - code_output: 20%        # Đoán output của code
    - fill_blank: 10%         # Điền từ/code vào chỗ trống
    - matching: 10%           # Nối khái niệm
  
  rules:
    - "Không hỏi định nghĩa thuần túy — hỏi ÁP DỤNG"
    - "Mỗi câu có giải thích đáp án (hiện sau khi nộp)"
    - "Đáp án sai phải hợp lý (không troll)"
    - "Random thứ tự câu hỏi + đáp án"
```

### 2. Lab / Bài tập thực hành
**Khi dùng:** Kiểm tra khả năng áp dụng sau bài lý thuyết

```yaml
lab_design:
  format: "jupyter_notebook | google_colab | github_repo"
  structure:
    - setup: "Cung cấp dataset + starter code"
    - tasks: "3-5 tasks từ dễ → khó"
    - bonus: "1 task nâng cao (optional)"
    - submission: "Nộp notebook + kết quả"
  
  grading:
    code_runs: 30          # Code chạy không lỗi
    correct_output: 30     # Output đúng
    code_quality: 20       # Clean code, comments
    explanation: 20        # Giải thích approach
```

### 3. Project / Dự án
**Khi dùng:** Capstone, final assessment

```yaml
project_assessment:
  types:
    - individual: "1 học viên, 2-4 tuần"
    - team: "2-4 người, 3-6 tuần"
  
  phases:
    - proposal: { weight: 10%, deadline: "Tuần 1" }
    - implementation: { weight: 50%, deadline: "Tuần 3" }
    - presentation: { weight: 20%, deadline: "Tuần 4" }
    - documentation: { weight: 20%, deadline: "Tuần 4" }
  
  rubric:
    problem_definition: 15    # Bài toán rõ ràng, có ý nghĩa
    data_handling: 15         # Thu thập, làm sạch, EDA
    model_selection: 20       # Chọn model hợp lý, so sánh
    results: 20               # Metrics, visualization
    presentation: 15          # Trình bày rõ ràng
    code_quality: 15          # Clean, documented, reproducible
```

### 4. Peer Review / Đánh giá ngang hàng
**Khi dùng:** Bổ trợ project assessment, phát triển kỹ năng review

```yaml
peer_review:
  reviewers_per_project: 2
  anonymous: true
  template:
    - strengths: "3 điểm mạnh"
    - improvements: "3 điểm cần cải thiện"
    - score: "1-10 theo rubric"
    - comment: "Nhận xét tổng thể"
  
  calibration:
    - "Instructor review 10% submissions để calibrate"
    - "Nếu peer scores chênh > 3 điểm → instructor resolve"
```

## Rubric tổng quát

### Mức đánh giá

| Mức | Điểm | Mô tả |
|-----|------|-------|
| **Xuất sắc** | 90-100 | Vượt kỳ vọng, sáng tạo, giải thích sâu |
| **Giỏi** | 80-89 | Đạt tất cả tiêu chí, ít lỗi |
| **Khá** | 70-79 | Đạt phần lớn, một số thiếu sót nhỏ |
| **Đạt** | 60-69 | Đạt yêu cầu tối thiểu |
| **Chưa đạt** | <60 | Cần học lại / làm lại |

### Template Rubric

```yaml
rubric:
  criteria:
    - name: "[Tiêu chí]"
      weight: X%
      levels:
        excellent: "Mô tả mức xuất sắc"
        good: "Mô tả mức giỏi"
        adequate: "Mô tả mức đạt"
        insufficient: "Mô tả mức chưa đạt"
```

## Certification Criteria

```yaml
certification:
  requirements:
    - quiz_avg: ">= 70%"
    - labs_completed: ">= 80%"
    - capstone_score: ">= 70%"
    - attendance: ">= 75% (nếu offline)"
  
  levels:
    - name: "AI Foundation"
      badge_color: "bronze"
      requirement: "Hoàn thành Foundation modules"
    - name: "AI Practitioner"
      badge_color: "silver"
      requirement: "Hoàn thành Core + 1 Capstone"
    - name: "AI Specialist"
      badge_color: "gold"
      requirement: "Hoàn thành Advanced + Portfolio 3 projects"
```

## Plagiarism Detection — Phát Hiện Gian Lận

### Code Plagiarism
```yaml
code_plagiarism:
  tools:
    - name: "MOSS (Stanford)"
      url: "https://theory.stanford.edu/~aiken/moss/"
      languages: ["python", "java", "c++"]
      usage: "Upload tất cả submissions → MOSS so sánh chéo"
      threshold: "> 70% similarity = flag"
    
    - name: "JPlag"
      url: "https://jplag.github.io/JPlag/"
      languages: ["python", "java", "javascript"]
      usage: "Self-hosted, chạy local"
      threshold: "> 60% similarity = flag"
    
    - name: "Manual Review"
      when: "MOSS/JPlag flag + suspicious patterns"
      checks:
        - "Variable names giống nhau bất thường"
        - "Comment/docstring identical"
        - "Error handling pattern copy"
        - "Submission time gần nhau"

  process:
    1_auto: "Chạy MOSS/JPlag trên tất cả submissions"
    2_flag: "Đánh dấu cặp > threshold"
    3_review: "Instructor review manual các cặp flagged"
    4_action: |
      Lần 1: Cảnh cáo + redo assignment (điểm max 70%)
      Lần 2: Điểm 0 cho assignment
      Lần 3: Fail toàn khóa + báo cáo
```

### AI-Generated Content Detection
```yaml
ai_detection:
  strategy: "Thiết kế assignment CHỐNG được AI"
  techniques:
    - "Yêu cầu explain quá trình thinking (video/voice)"
    - "Dùng dataset UNIQUE cho mỗi học viên (random seed)"
    - "Hỏi viva voce (phỏng vấn miệng) cho capstone"
    - "Yêu cầu commit history (Git log) — thấy quá trình code"
    - "In-class timed coding challenge (không internet)"
  
  acceptable_ai_use:
    - "Dùng AI để debug (nhưng phải giải thích lỗi)"
    - "Dùng AI để tìm tài liệu (nhưng phải đọc và tóm tắt)"
    - "Dùng AI để brainstorm (nhưng phải chọn lọc và modify)"
  
  unacceptable:
    - "Copy-paste output AI làm bài nộp"
    - "Dùng AI viết toàn bộ report"
    - "Share prompts/answers với bạn cùng lớp"
```

### Academic Integrity Policy
```
Quy định được công bố ở NGÀY ĐẦU TIÊN của khóa học:
1. Mọi bài nộp là sản phẩm cá nhân/nhóm (trừ khi ghi rõ collaboration)
2. Được phép dùng AI làm CÔNG CỤ HỖ TRỢ, KHÔNG phải THAY THẾ
3. Mọi nguồn tham khảo phải ghi credit
4. Vi phạm sẽ xử lý theo thang 3 cấp: Cảnh cáo → Điểm 0 → Fail
```

---

## Output khi được yêu cầu

1. **Assessment Plan** — Loại, trọng số, timeline cho toàn khóa
2. **Quiz Template** — 10-15 câu mẫu cho module cụ thể
3. **Rubric** — Tiêu chí chấm điểm chi tiết
4. **Project Brief** — Đề bài + requirements + rubric
5. **Plagiarism Policy** — Tools, process, academic integrity rules
