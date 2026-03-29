# Động cơ Chấm điểm

## Mục đích

Engine tính điểm thống nhất — dùng cho cả grading (chấm bài user) và
internal quality assessment (chấm output trước khi xuất).

## Chấm điểm Models

### Model 1: Rubric 100 (cho grading pipeline)

| Tiêu chí | Trọng số | Scale |
|----------|----------|-------|
| Accuracy | 25% | 0-100 |
| Structure | 20% | 0-100 |
| Clarity | 20% | 0-100 |
| Persuasion | 15% | 0-100 |
| Style | 10% | 0-100 |
| Value | 10% | 0-100 |

**Công thức**: `total = Σ(score_i × weight_i)`

### Model 2: Quality Gate (cho internal checks)

| Check | Weight | PASS threshold |
|-------|--------|---------------|
| Anti-AI score | 30% | ≤ 40 |
| Consistency | 25% | ≥ 85 |
| Proofread | 20% | ≥ 95 |
| Risk level | 15% | ≤ medium |
| Format compliance | 10% | ≥ 90 |

**Gate verdict:**
- Tất cả PASS → ✅ PASS
- 1+ FAIL → ❌ NEEDS_REVISION
- 2+ critical → 🚫 FAIL

### Model 3: Anti-AI Score (standalone)

```
Score = count_of_patterns × severity_weight

Pattern weights:
  opening_cliché: 15
  connector_spam: 10 
  closing_khuôn: 15
  flowery_words: 8
  uniform_structure: 8
  passive_voice_vn: 5
  filler_phrases: 5

Target: total ≤ 40
```

## Calibration Rules

- Grading bài người dùng: dùng Model 1
- Quality check nội bộ: dùng Model 2
- Anti-AI standalone: dùng Model 3
- Score từ 2 sources khác nhau → lấy trung bình
- Tiêu chí nào thiếu data → skip, tính trọng số lại

## Định dạng đầu ra

```yaml
scoring_result:
  model_used: "[rubric_100/quality_gate/anti_ai]"
  scores:
    - criterion: "[tên]"
      score: [N]
      weight: [N%]
      comment: "[nhận xét]"
  total: [weighted_average]
  band: "[xuất sắc/tốt/khá/trung bình/yếu]"
  verdict: "[pass/needs_revision/fail]"
```
