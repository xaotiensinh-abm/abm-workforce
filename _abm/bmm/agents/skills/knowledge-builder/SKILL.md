---
name: knowledge-builder
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Xây dựng knowledge base AI cho học viên — tài liệu tham khảo, cheat sheets, glossary, learning resources"
---

# Xây Dựng Knowledge Base — Knowledge Builder

## Mục đích
Skill này giúp xây dựng và duy trì kho tri thức AI có cấu trúc cho học viên ABM — từ glossary đến reference guides.

## Cấu trúc Knowledge Base

```
knowledge-base/
├── 📖 glossary/           → Thuật ngữ AI (VN-EN)
├── 📋 cheat-sheets/       → Tóm tắt nhanh theo topic
├── 🗺️ roadmaps/           → Lộ trình học theo goal
├── 🔗 resources/          → Links tài liệu tham khảo
├── 💡 tips-and-tricks/    → Mẹo thực hành
├── ❓ faq/                → Câu hỏi thường gặp
└── 📊 comparisons/        → So sánh tools/frameworks
```

## Templates cho từng loại

### 1. Glossary Entry (Thuật ngữ)
```yaml
glossary_entry:
  term_en: "Fine-tuning"
  term_vn: "Tinh chỉnh mô hình"
  category: "LLM"
  difficulty: "intermediate"
  
  definition_simple: "Lấy model AI có sẵn, train thêm trên data riêng để nó giỏi hơn trong lĩnh vực cụ thể."
  definition_technical: "Quá trình cập nhật weights của pre-trained model bằng domain-specific data, thường dùng LoRA/QLoRA để giảm compute."
  
  analogy: "Như thuê 1 bác sĩ đa khoa, rồi cho bác sĩ đó chuyên thêm về tim mạch."
  
  example:
    use_case: "Fine-tune GPT cho chatbot CSKH ngân hàng VN"
    code_snippet: |
      from peft import LoraConfig, get_peft_model
      config = LoraConfig(r=16, lora_alpha=32)
      model = get_peft_model(base_model, config)
  
  related_terms: ["Transfer Learning", "LoRA", "QLoRA", "Pre-training"]
  see_also: ["cheat-sheets/fine-tuning.md", "labs/fine-tuning-lab.ipynb"]
```

### 2. Cheat Sheet
```yaml
cheat_sheet:
  topic: "[Tên chủ đề]"
  format: "1-2 trang, visual, scannable"
  
  sections:
    - what: "1 câu: [Topic] là gì?"
    - when: "Khi nào dùng? Khi nào KHÔNG dùng?"
    - how: "Code snippet / commands cơ bản"
    - params: "Hyperparameters quan trọng + giá trị mặc định"
    - gotchas: "3-5 lỗi thường gặp + cách fix"
    - resources: "2-3 links đọc thêm"
  
  style:
    - "Dùng bảng thay paragraph"
    - "Code blocks có syntax highlighting"
    - "Icons/emoji cho visual scanning"
    - "Không quá 500 từ"
```

### 3. Resource Collection
```yaml
resource_collection:
  topic: "[Tên chủ đề]"
  
  official_docs:
    - { name: "...", url: "...", quality: "★★★★★" }
  
  tutorials:
    - { name: "...", url: "...", level: "beginner", lang: "VN/EN" }
  
  videos:
    - { name: "...", url: "...", duration: "Xh", channel: "..." }
  
  books:
    - { name: "...", author: "...", level: "...", free: true/false }
  
  courses_external:
    - { name: "...", platform: "Coursera/edX/...", price: "..." }
  
  tools:
    - { name: "...", url: "...", free_tier: true/false }
  
  vietnamese_resources:  # Ưu tiên nguồn tiếng Việt
    - { name: "...", url: "...", author: "..." }
```

### 4. Comparison Guide
```yaml
comparison:
  title: "[A vs B vs C]"
  category: "[VD: LLM Frameworks]"
  updated: "YYYY-MM-DD"
  
  matrix:
    criteria:
      - name: "Ease of use"
        a_score: 8
        b_score: 7
        c_score: 9
      - name: "Performance"
        a_score: 9
        b_score: 8
        c_score: 7
  
  verdict: "Khi nào dùng A? Khi nào dùng B? Khi nào dùng C?"
  abm_recommendation: "ABM dạy [X] vì [lý do]"
```

## Quy trình cập nhật

```yaml
update_process:
  trigger:
    - "Mỗi khi có module mới (từ research-to-training)"
    - "Mỗi khi tool/framework update major version"
    - "Mỗi khi học viên hỏi câu hỏi lặp lại ≥ 3 lần"
    - "Monthly review bởi R&D team"
  
  review:
    frequency: "Monthly"
    checklist:
      - "Glossary entries còn chính xác không?"
      - "Links còn hoạt động không?"
      - "Cheat sheets cần cập nhật version?"
      - "Có gaps nào cần thêm entry?"
  
  versioning:
    method: "YYYY-MM-DD timestamps"
    changelog: "Mỗi entry có 'last_updated' field"
```

## Output khi được yêu cầu

1. **Glossary Entry** — Thuật ngữ AI song ngữ VN-EN
2. **Cheat Sheet** — 1-2 trang tóm tắt topic
3. **Resource Collection** — Links tài liệu curated
4. **Comparison Guide** — So sánh tools/frameworks
5. **Knowledge Audit** — Kiểm tra gaps trong KB hiện tại
