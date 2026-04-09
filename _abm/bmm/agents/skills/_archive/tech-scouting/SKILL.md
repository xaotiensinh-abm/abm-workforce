---
name: tech-scouting
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Đánh giá công nghệ AI mới — LLM, framework, tools, APIs — feasibility + adoption recommendation"
---

# Đánh Giá Công Nghệ AI — Tech Scouting

## Mục đích
Skill này giúp đánh giá nhanh và có hệ thống các công nghệ AI mới, quyết định có nên đưa vào chương trình đào tạo ABM.

## Framework đánh giá RAPID

```
R — Relevance   : Liên quan đến AI education không?
A — Accessibility: Học viên có thể tiếp cận được không?
P — Potential    : Tiềm năng thị trường / career impact?
I — Integration  : Tích hợp vào curriculum hiện tại dễ không?
D — Durability   : Bền vững hay chỉ hype ngắn hạn?
```

### Bảng chấm điểm RAPID

```yaml
rapid_scorecard:
  technology: "[Tên công nghệ]"
  version: "[Version đánh giá]"
  date: "YYYY-MM-DD"
  evaluator: "[Tên]"
  
  scores:  # 1-10 mỗi chiều
    relevance:
      score: 0
      evidence: "..."
      questions:
        - "Thuộc lĩnh vực AI nào? (NLP, CV, RL, Agents...)"
        - "Doanh nghiệp VN có nhu cầu không?"
        - "Học viên ABM có thể ứng dụng ngay không?"
    
    accessibility:
      score: 0
      evidence: "..."
      questions:
        - "Miễn phí / Open source?"
        - "Chạy trên Colab được không? (GPU requirement)"
        - "Tài liệu tiếng Anh/Việt có đủ không?"
        - "API có sẵn không? Giá hợp lý?"
    
    potential:
      score: 0
      evidence: "..."
      questions:
        - "Job market cần skill này không?"
        - "Công ty lớn nào đang dùng?"
        - "Growth trend trên GitHub/HuggingFace?"
    
    integration:
      score: 0
      evidence: "..."
      questions:
        - "Thay module hiện tại hay thêm module mới?"
        - "Prerequisite nào cần?"
        - "Lab exercise tạo được trong bao lâu?"
    
    durability:
      score: 0
      evidence: "..."
      questions:
        - "Backed bởi ai? (Google, Meta, startup...)"
        - "Có community mạnh không?"
        - "Competitor nào? Có thể bị thay thế?"
  
  total: 0  # Tổng / 50
  recommendation: "adopt | trial | assess | hold | drop"
```

### Ma trận quyết định

| RAPID Score | Recommendation | Hành động |
|:-----------:|:--------------:|-----------|
| 40-50 | **ADOPT** | Đưa vào curriculum ngay sprint tới |
| 30-39 | **TRIAL** | Tạo workshop thử nghiệm, thu feedback |
| 20-29 | **ASSESS** | Theo dõi thêm 1-2 tháng, làm POC |
| 10-19 | **HOLD** | Ghi nhận, chờ mature hơn |
| 0-9 | **DROP** | Không phù hợp, không theo dõi |

## Quy trình scouting

```
1. PHÁT HIỆN
   ← Từ ai-trend-radar (🔴 HOT / 🟡 WARM)
   ← Từ yêu cầu CEO
   ← Từ feedback học viên
   
2. ĐÁNH GIÁ NHANH (30 phút)
   → Đọc docs, README, demo
   → Chấm RAPID sơ bộ (5 câu hỏi nhanh)
   → Nếu ≥ 25 → tiếp Bước 3
   
3. ĐÁNH GIÁ SÂU (2-4 giờ)
   → Chạy thử hands-on
   → So sánh với alternatives
   → RAPID scorecard đầy đủ
   → Viết Tech Scout Report
   
4. QUYẾT ĐỊNH
   → Trình CEO với recommendation
   → CEO approve → chuyển research-to-training
```

## Comparison Template

```yaml
tech_comparison:
  category: "[VD: LLM Frameworks]"
  candidates:
    - name: "LangChain"
      rapid_score: 38
      pros: ["Ecosystem lớn", "Nhiều integrations"]
      cons: ["Complex API", "Breaking changes thường xuyên"]
      
    - name: "LlamaIndex"
      rapid_score: 35
      pros: ["RAG-focused", "Simpler API"]
      cons: ["Ít integrations hơn", "Community nhỏ hơn"]
      
    - name: "Semantic Kernel"
      rapid_score: 28
      pros: [".NET native", "Microsoft backing"]
      cons: ["Ít dùng ở VN", "Python support yếu hơn"]
  
  recommendation: "LangChain cho khóa chính, LlamaIndex cho module RAG"
```

## Output khi được yêu cầu

1. **RAPID Scorecard** — Chấm điểm 5 chiều cho 1 công nghệ
2. **Comparison Matrix** — So sánh 2-4 alternatives
3. **Tech Scout Report** — Báo cáo đánh giá chi tiết
4. **Adoption Roadmap** — Lộ trình đưa vào curriculum
5. **POC Plan** — Kế hoạch proof-of-concept
