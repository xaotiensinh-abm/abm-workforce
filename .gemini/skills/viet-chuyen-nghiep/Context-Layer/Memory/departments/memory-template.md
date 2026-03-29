# Mẫu Bộ nhớ: Phiên làm việc theo Ban

## Objective

Template chuẩn cho mỗi department's session memory. Khi worker hoàn thành task,
lưu lesson vào file tương ứng.

## Định dạng Nhật ký Phiên Toàn cục

```yaml
session:
  date: "[YYYY-MM-DD]"
  department: "[intake/research/strategy/longform/social/video/critique/quality]"
  task_type: "[write-new/edit-draft/grade/critique/research]"
  
  # What worked
  wins:
    - "[Kỹ thuật hiệu quả]"
    
  # What didn't work
  issues:
    - issue: "[Mô tả vấn đề]"
      root_cause: "[Nguyên nhân gốc]"
      fix: "[Cách đã fix]"
      
  # Learnings
  lessons:
    - "[Bài học rút ra]"
    
  # Patterns to remember
  patterns:
    - trigger: "[Khi gặp tình huống X]"
      action: "[Làm Y thay vì Z]"
```

## Per-Department Memory Files

| Department | File | Tracks |
|-----------|------|--------|
| intake | `intake-sessions.md` | Brief quality, common ambiguities |
| research | `research-sessions.md` | Source issues, contradiction cases |
| strategy | `strategy-sessions.md` | Outline iterations, angle effectiveness |
| longform | `longform-sessions.md` | Chapter patterns, reader flow |
| social | `social-sessions.md` | Engagement patterns, viral triggers |
| video | `video-sessions.md` | Script timing, hook effectiveness |
| critique | `critique-sessions.md` | Scoring calibration, feedback quality |
| quality | `quality-sessions.md` | Anti-AI catches, false positives |

## Quy trình Sử dụng

1. Worker hoàn thành → ghi session_log
2. Cùng department → đọc sessions cũ trước khi bắt đầu
3. Mỗi 10 sessions → distill patterns vào Knowledge-Base
