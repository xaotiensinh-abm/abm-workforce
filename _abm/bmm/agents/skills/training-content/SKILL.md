---
name: training-content
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Tạo tài liệu đào tạo AI — slide, handout, lab exercises, video script, practical demos"
---

# Tài Liệu Đào Tạo AI — Training Content

## Mục đích
Skill này giúp tạo tài liệu đào tạo chất lượng cao cho khóa học AI — từ slide đến lab exercises.

## 5 Loại Tài Liệu

### 1. Slide bài giảng

**Nguyên tắc thiết kế:**
- **10-20-30**: Tối đa 10 slide / 20 phút / font ≥ 30pt
- **1 ý chính / slide** — không nhồi thông tin
- **Visual > Text** — dùng diagram, code snippet, ảnh minh họa
- **Mỗi slide có speaker notes** — ghi chú cho giảng viên

**Template slide:**
```yaml
slide_deck:
  title_slide:
    title: "[Tên bài]"
    subtitle: "Module X — Khóa [Tên khóa]"
    author: "ABM Education"
  
  agenda_slide:
    items: ["Mục tiêu", "Nội dung chính", "Demo", "Lab", "Q&A"]
  
  content_slides:
    - type: "concept"         # Giải thích khái niệm
      layout: "text_left_image_right"
    - type: "code_walkthrough" # Giải thích code
      layout: "code_block_full"
    - type: "comparison"       # So sánh 2+ options
      layout: "table_or_columns"
    - type: "diagram"          # Kiến trúc, flow
      layout: "mermaid_or_image"
    - type: "demo"             # Live coding demo
      layout: "terminal_screenshot"
  
  summary_slide:
    key_takeaways: 3
    next_steps: "Lab exercise + đọc thêm"
  
  style:
    theme: "dark"  # ABM brand
    primary_color: "#FF0000"
    font: "Inter"
    code_font: "JetBrains Mono"
```

### 2. Handout / Tài liệu tóm tắt

**1-2 trang A4 cho mỗi module:**
- Tóm tắt key concepts
- Cheat sheet (formulas, commands, syntax)
- Links tài liệu tham khảo
- Bài tập tự luyện

### 3. Lab Exercise

```yaml
lab_template:
  title: "Lab X: [Tên bài lab]"
  estimated_time: "60 phút"
  difficulty: "⭐⭐⭐ (3/5)"
  
  objectives:
    - "Sau lab này, học viên sẽ..."
  
  prerequisites:
    - "Đã xem video Module X"
    - "Đã cài đặt Python 3.10+"
  
  setup:
    environment: "Google Colab | Local"
    dataset: "link hoặc auto-download trong notebook"
    starter_code: true  # Cung cấp code khung
  
  tasks:
    - task_id: 1
      title: "Load và khám phá dữ liệu"
      difficulty: "⭐"
      hints: ["Dùng pandas", "Kiểm tra shape, dtypes, null"]
      expected_output: "DataFrame summary"
    
    - task_id: 2
      title: "Tiền xử lý dữ liệu"
      difficulty: "⭐⭐"
      hints: ["Handle missing values", "Encode categorical"]
    
    - task_id: 3
      title: "Xây dựng model"
      difficulty: "⭐⭐⭐"
      hints: ["Train/test split", "Chọn metric phù hợp"]
    
    - task_id: "BONUS"
      title: "Tối ưu hyperparameters"
      difficulty: "⭐⭐⭐⭐"
      optional: true
  
  solution:
    provided_after: "deadline"  # Giải sau deadline
    format: "notebook_with_explanation"
```

### 4. Video Script

```yaml
video_script:
  type: "lecture | demo | tutorial"
  duration: "10-15 phút"  # Tối ưu cho attention span
  
  structure:
    hook: "30 giây — Tại sao topic này quan trọng?"
    overview: "30 giây — Hôm nay học gì?"
    content:
      - segment: "Phần 1"
        duration: "3-4 phút"
        visual: "Slide + talking head"
      - segment: "Demo"
        duration: "4-5 phút"
        visual: "Screen recording + voiceover"
      - segment: "Phần 2"
        duration: "3-4 phút"
    summary: "1 phút — 3 key takeaways"
    cta: "30 giây — Làm lab X để thực hành"
  
  production_notes:
    resolution: "1920x1080"
    audio: "Mic chất lượng, không echo"
    editing: "Jump cuts cho demo, transitions cho concept"
    captions: "Tiếng Việt + English subtitles"
```

### 5. Practical Demo

**Mỗi module cần ít nhất 1 demo live:**
- Setup: Chuẩn bị environment, data trước
- Flow: Giải thích → Code → Run → Kết quả → Giải thích
- Lỗi có chủ đích: Cố tình tạo lỗi phổ biến → debug live
- Thời lượng: 5-10 phút

## Quy tắc tạo nội dung AI

1. **Thực tế > Lý thuyết**: Mọi concept phải có code example
2. **Dataset thật**: Dùng dataset thực tế, không toy data
3. **Công cụ phổ biến**: Python, PyTorch/TensorFlow, HuggingFace
4. **Cập nhật**: Kiểm tra version tools mỗi 3 tháng
5. **Đa cấp độ**: Cung cấp cả basic và advanced path

---

## Modules Chuyên Sâu (từ Community Skill Integration)

### Module: Prompt Engineering Patterns

```yaml
prompt_engineering_module:
  level: "Core (tất cả tracks)"
  duration: "6 giờ"
  
  patterns:
    basic:
      - "Zero-shot: Viết prompt không ví dụ"
      - "Few-shot: Cho 2-5 ví dụ mẫu"
      - "Role-playing: System prompt gán vai trò"
      - "Chain-of-Thought (CoT): Yêu cầu giải thích từng bước"
    
    advanced:
      - "Tree-of-Thought (ToT): Explore nhiều nhánh suy luận"
      - "ReAct: Reasoning + Acting (tool use)"
      - "Self-Consistency: Chạy nhiều lần → vote kết quả"
      - "Structured Output: JSON / YAML / XML schema"
      - "Meta-prompting: Prompt viết prompt"
    
    anti_patterns:
      - "❌ Prompt mơ hồ: 'Hãy giúp tôi viết gì đó'"
      - "❌ Quá dài: > 2000 tokens prompt"
      - "❌ Thiếu context: Không cung cấp background"
      - "❌ Injection risk: Không sanitize user input"
    
    production_tips:
      - "Temperature: 0-0.3 cho factual, 0.7-1.0 cho creative"
      - "Max tokens: Set vừa đủ, tránh lãng phí"
      - "System prompt: Luôn set rõ role + constraints"
      - "Evaluation: A/B test prompts trước khi deploy"
  
  lab: "Lab PE-01: Tối ưu prompt cho chatbot CSKH tiếng Việt"
```

### Module: RAG Systems (Retrieval-Augmented Generation)

```yaml
rag_module:
  level: "Advanced track"
  duration: "8 giờ"
  
  content:
    part_1_fundamentals: # 2 giờ
      - "RAG là gì? So sánh với fine-tuning"
      - "Embedding models: text-embedding-ada-002, BGE, E5"
      - "Vector databases: ChromaDB, Pinecone, Weaviate, FAISS"
      - "Chunking strategies: Fixed, Semantic, Sentence"
    
    part_2_implementation: # 3 giờ
      - "Build RAG pipeline với LangChain"
      - "Build RAG pipeline với LlamaIndex"
      - "Document loaders: PDF, Web, CSV, Database"
      - "Retrieval strategies: Dense, Sparse, Hybrid"
    
    part_3_advanced: # 2 giờ
      - "Query transformation: HyDE, Multi-query"
      - "Re-ranking: Cohere, Cross-encoder"
      - "Evaluation: RAGAS, faithfulness, relevancy"
      - "Production: Caching, monitoring, cost optimization"
    
    part_4_project: # 1 giờ
      - "Capstone: RAG chatbot cho tài liệu ABM"
  
  lab: "Lab RAG-01: Build chatbot QA từ tài liệu PDF tiếng Việt"
  dataset: "Tài liệu nội bộ ABM (ẩn danh hóa)"
```

### Module: Data Storytelling (Data → Narrative)

```yaml
data_storytelling_module:
  level: "Intermediate (Analytics track)"
  duration: "4 giờ"
  
  framework: "DATA → INSIGHT → NARRATIVE → ACTION"
  
  content:
    data_to_insight:
      - "Chọn metric đúng: Leading vs Lagging"
      - "Phát hiện patterns: Trends, Outliers, Clusters"
      - "Statistical significance: Khi nào data đủ tin cậy?"
    
    insight_to_narrative:
      - "Pyramid principle: Key message trước, detail sau"
      - "Storytelling arc: Context → Conflict → Resolution"
      - "Visualization: Chart chọn đúng (bar vs line vs scatter)"
      - "Vietnamese business context: Cách trình bày cho CEO/Board VN"
    
    narrative_to_action:
      - "So what?: Từ insight → recommendation"
      - "Next steps: Specific, Measurable, Time-bound"
      - "Dashboard design: KPI cards, trend lines, alerts"
  
  lab: "Lab DS-01: Phân tích data enrollment ABM → Slide cho CEO"
```

### Module: AI Agent Development

```yaml
ai_agent_module:
  level: "Specialist track"
  duration: "12 giờ"
  
  content:
    part_1_foundations: # 3 giờ
      - "AI Agents là gì? Autonomous vs Semi-autonomous"
      - "Tool use: Function calling, API integration"
      - "Memory: Short-term (context) vs Long-term (vector DB)"
      - "Planning: ReAct, Plan-and-Execute"
    
    part_2_frameworks: # 4 giờ
      - "LangGraph: State machines cho agents"
      - "CrewAI: Multi-agent teams"
      - "Autogen: Conversational agents"
      - "Custom agents: Python từ scratch"
    
    part_3_multi_agent: # 3 giờ
      - "Orchestration patterns: Sequential, Parallel, Hierarchical"
      - "Communication: Message passing, shared state"
      - "Error handling: Retry, fallback, human-in-the-loop"
      - "ABM pattern: Delegation Chain (Hợp đồng → Chứng nhận)"
    
    part_4_production: # 2 giờ
      - "Testing agents: Unit test, Integration test, Eval"
      - "Deployment: Docker, serverless, edge"
      - "Monitoring: LangSmith, Arize, custom logging"
      - "Cost optimization: Token budget, caching, model routing"
  
  lab: "Lab AG-01: Build team 3 agents giải quyết bài toán business"
  capstone: "Capstone: Multi-agent hệ thống CSKH tự động"
```

---

## Output khi được yêu cầu

1. **Slide deck outline** — Structure + speaker notes
2. **Lab notebook** — Jupyter/Colab với starter code
3. **Handout** — 1-2 trang tóm tắt
4. **Video script** — Script + production notes
5. **Demo plan** — Step-by-step demo flow
6. **Module content** — Prompt Engineering / RAG / Data Storytelling / Agents
