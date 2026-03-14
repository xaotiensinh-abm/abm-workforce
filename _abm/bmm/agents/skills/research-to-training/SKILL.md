---
name: research-to-training
description: "Chuyển đổi nghiên cứu AI → lộ trình đào tạo — từ paper/tool mới thành module, lab, workshop cho học viên"
---

# Nghiên Cứu → Đào Tạo — Research to Training Pipeline

## Mục đích
Skill này là CẦU NỐI giữa phòng R&D và phòng Đào Tạo — chuyển đổi nghiên cứu AI thành nội dung đào tạo thực tế cho học viên ABM.

## Pipeline 5 bước

```
┌─────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌─────────┐
│ NGHIÊN  │────▶│ CHẮT LỌC │────▶│ THIẾT KẾ │────▶│ THỬ     │────▶│ TRIỂN  │
│ CỨU     │     │          │     │ MODULE   │     │ NGHIỆM  │     │ KHAI   │
│(R&D)    │     │(R2T)     │     │(Training)│     │(Pilot)   │     │(Live)  │
└─────────┘     └──────────┘     └──────────┘     └──────────┘     └─────────┘
  Input:          Simplify        Course           Test with        Full
  Papers,         for learners    Design           10-15 HV         rollout
  Tools,                                           feedback
  Trends
```

### Bước 1: Nhận đầu vào từ R&D

```yaml
input_sources:
  from_trend_radar:
    - "🔴 HOT items → chuyển thành workshop ngay (1-2 tuần)"
    - "🟡 WARM items → lên kế hoạch module mới (1-2 tháng)"
  
  from_tech_scouting:
    - "ADOPT recommendations → module chính thức"
    - "TRIAL recommendations → workshop thử nghiệm"
  
  from_benchmark_lab:
    - "Kết quả benchmark → lab exercises so sánh"
    - "Best practices mới → cập nhật module hiện tại"
  
  from_ceo:
    - "Yêu cầu trực tiếp → priority cao nhất"
```

### Bước 2: Chắt lọc — Simplification Framework

```yaml
simplification:
  principles:
    - "Loại bỏ toán phức tạp → giữ intuition"
    - "Thay code research-grade → code production-ready"
    - "Mapping concept → real-world use case ở VN"
    - "80/20: 20% kiến thức cốt lõi → 80% năng lực thực hành"
  
  translation_rules:
    paper_to_module:
      - "Abstract → 1 câu 'Cái này làm gì?'"
      - "Method → Diagram đơn giản + code snippet"
      - "Results → Demo trực quan"
      - "Limitations → 'Khi nào KHÔNG nên dùng'"
    
    tool_to_lab:
      - "Installation → 1 cell Colab setup"
      - "API docs → 3 ví dụ cụ thể (dễ → khó)"
      - "Advanced features → Bonus task optional"
    
    trend_to_workshop:
      - "What: Xu hướng này là gì? (10 phút)"
      - "Why: Tại sao quan trọng? (10 phút)"
      - "How: Demo + hands-on (60 phút)"
      - "Next: Học sâu hơn ở đâu? (10 phút)"
  
  difficulty_mapping:
    beginner: "Dùng tool/API, không code model từ scratch"
    intermediate: "Hiểu architecture, fine-tune, customize"
    advanced: "Build từ scratch, optimize, deploy production"
```

### Bước 3: Thiết kế Module (dùng course-design skill)

```yaml
module_template:
  title: "[Tên module — từ research/tool]"
  origin: "[Link paper/tool/trend]"
  rapid_score: "[Điểm từ tech-scouting]"
  target_level: "beginner | intermediate | advanced"
  estimated_duration: "[X giờ]"
  
  learning_outcomes:
    - "LO1: Giải thích [concept] bằng ngôn ngữ đơn giản"
    - "LO2: Triển khai [tool/technique] trên dữ liệu thực"
    - "LO3: Đánh giá khi nào nên/không nên dùng [approach]"
  
  content_plan:
    theory: "30% — concept + intuition + diagram"
    demo: "20% — live coding / pre-recorded"
    lab: "40% — hands-on exercise"
    discussion: "10% — Q&A + use cases VN"
  
  prerequisites:
    courses: ["Khóa nào cần học trước"]
    skills: ["Python level?", "ML basics?"]
  
  lab_dataset:
    source: "Kaggle / HuggingFace / custom"
    vietnamese: true  # Ưu tiên dataset VN nếu có
```

### Bước 4: Pilot Test

```yaml
pilot:
  participants: "10-15 học viên (mix levels)"
  duration: "1 buổi workshop (2-3 giờ)"
  
  collect:
    - "Completion rate — bao nhiêu % hoàn thành lab?"
    - "Difficulty rating — quá khó / quá dễ / vừa?"
    - "NPS — giới thiệu không?"
    - "Content gaps — thiếu gì?"
    - "Time accuracy — đủ thời gian không?"
  
  iterate:
    - "Nếu completion < 60% → giảm độ khó"
    - "Nếu NPS < 30 → redesign content"
    - "Nếu time over → cắt hoặc chia 2 buổi"
```

### Bước 5: Triển khai chính thức

```yaml
rollout:
  checklist:
    - "[ ] Module đã qua pilot, feedback positive"
    - "[ ] Tài liệu đầy đủ (slide, lab, handout)"
    - "[ ] Giảng viên đã trained trên module mới"
    - "[ ] LMS đã cập nhật structure"
    - "[ ] Marketing đã announce module mới"
  
  announcement:
    channels: ["Email alumni", "Social media", "Website"]
    content: "Module mới: [Tên] — Tại sao bạn cần học điều này"
```

## Lộ trình đào tạo AI (mẫu)

```yaml
ai_training_roadmap:
  foundation:
    duration: "4-6 tuần"
    topics:
      - "Python for AI"
      - "Toán cho ML (Linear Algebra, Probability, Statistics)"
      - "Pandas, NumPy, Matplotlib"
      - "ML Basics (Scikit-learn)"
    output: "🥉 AI Foundation Certificate"
  
  core:
    duration: "8-12 tuần"
    tracks:
      - name: "NLP Track"
        topics: ["Text Processing", "Transformers", "BERT/GPT", "NER, Sentiment"]
      - name: "CV Track"
        topics: ["Image Processing", "CNNs", "Object Detection", "Segmentation"]
      - name: "Data Track"
        topics: ["Feature Engineering", "Model Selection", "AutoML", "MLOps Basics"]
    output: "🥈 AI Practitioner Certificate"
  
  advanced:
    duration: "12-16 tuần"
    topics:
      - "LLM & Prompt Engineering"
      - "RAG Systems (LangChain / LlamaIndex)"
      - "Fine-tuning (LoRA, QLoRA)"
      - "AI Agents (multi-agent systems)"
      - "Production Deployment (Docker, APIs)"
    output: "🏆 AI Specialist Certificate"
  
  emerging:  # ← CẬP NHẬT TỪ R&D
    duration: "Ongoing workshops"
    topics:
      - "🔴 [HOT trend from radar]"
      - "🟡 [WARM trend from radar]"
    frequency: "1-2 workshops / tháng"
```

## Handoff Protocol R&D ↔ Đào Tạo

### SLA (Service Level Agreement)

```yaml
handoff_sla:
  hot_trend_to_workshop:
    sla: "≤ 2 tuần"
    process: "Radar 🔴HOT → R2T simplify (3 ngày) → Workshop design (4 ngày) → Pilot (3 ngày) → Live"
    owner: "rd-specialist → training-specialist"
  
  adopt_to_module:
    sla: "≤ 6 tuần"
    process: "RAPID ADOPT → R2T full pipeline (2 tuần) → Module design (2 tuần) → Pilot + iterate (2 tuần)"
    owner: "rd-specialist → training-specialist"
  
  module_update:
    sla: "≤ 1 tuần"
    process: "Version change detected → R2T review (2 ngày) → Content update (3 ngày) → LMS update (2 ngày)"
    owner: "rd-specialist → training-specialist"
  
  escalation:
    miss_sla: "Báo CEO trong daily standup"
    blocked: "R&D và Training sync call (30 phút) để unblock"
```

### Handoff Checklist

```yaml
handoff_document:
  from_rd_to_training:
    required:
      - "[ ] RAPID scorecard (nếu tech mới)"
      - "[ ] Simplified content map (concept → dễ hiểu)"
      - "[ ] Draft learning outcomes (≥ 3)"
      - "[ ] Dataset recommendation (Kaggle / HF / custom)"
      - "[ ] Difficulty level assessment (beginner/intermediate/advanced)"
      - "[ ] Demo code / notebook (working, tested)"
    optional:
      - "Benchmark data (nếu có)"
      - "Competitor course reference"
      - "Video resources list"
  
  from_training_to_rd:
    feedback:
      - "[ ] Student comprehension issues (concepts quá khó)"
      - "[ ] Tool/version problems (outdated)"
      - "[ ] Feature requests (topics muốn học thêm)"
      - "[ ] NPS score module"
    frequency: "Sau mỗi khóa hoàn thành"
```

### Sync Meeting

```yaml
rd_training_sync:
  frequency: "Bi-weekly (2 tuần/lần)"
  duration: "30 phút"
  agenda:
    - "R&D: New trends flagged (5 phút)"
    - "R&D: Tech evaluations completed (5 phút)"
    - "Training: Student feedback on new modules (5 phút)"
    - "Training: Content update requests (5 phút)"
    - "Joint: Priority alignment (10 phút)"
  attendees: ["rd-specialist", "training-specialist", "CEO (optional)"]
```

---

## Output khi được yêu cầu

1. **R2T Pipeline Report** — Status chuyển đổi research → training
2. **Module Design** — Module mới từ paper/tool/trend
3. **Simplification Map** — Paper → Nội dung dễ hiểu
4. **AI Training Roadmap** — Lộ trình đào tạo cập nhật
5. **Pilot Results** — Feedback từ test group
6. **Handoff Document** — Checklist chuyển giao R&D→Training
