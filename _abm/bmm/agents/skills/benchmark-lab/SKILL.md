---
name: benchmark-lab
description: "So sánh và benchmark models/tools AI — evaluation metrics, head-to-head tests, cost-performance analysis"
---

# Benchmark Lab — Phòng Thí Nghiệm So Sánh AI

## Mục đích
Skill này giúp so sánh và đánh giá các models, tools, frameworks AI một cách có hệ thống — cung cấp dữ liệu thực cho quyết định đào tạo.

## Framework đánh giá SQUARE

```
S — Speed      : Tốc độ inference / training
Q — Quality    : Chất lượng output
U — Usability  : Dễ dùng / tích hợp
A — Affordability: Chi phí (API, compute, license)
R — Reliability: Ổn định, uptime, consistency
E — Ecosystem  : Community, plugins, integrations
```

## Quy trình benchmark

### Bước 1: Xác định scope

```yaml
benchmark_setup:
  category: "[VD: LLM for Vietnamese]"
  candidates:
    - "GPT-4o"
    - "Gemini 2.5 Pro"
    - "Claude 3.5 Sonnet"
    - "Qwen 2.5"
  
  tasks:
    - "Text generation (tiếng Việt)"
    - "Code generation"
    - "Summarization"
    - "RAG Q&A accuracy"
    - "Reasoning (math, logic)"
  
  datasets:
    - name: "Vietnamese QA (custom)"
      size: "200 câu hỏi"
      source: "ABM team tạo"
    - name: "Code tasks"
      size: "50 bài"
      source: "HumanEval + custom VN"
  
  environment:
    hardware: "Colab Pro+ / A100 (nếu local)"
    api_calls: "100 calls per model per task"
    temperature: 0.3  # Consistent across models
```

### Bước 2: Chạy benchmark

```yaml
benchmark_execution:
  metrics:
    quality:
      - accuracy: "% đúng trên dataset chuẩn"
      - coherence: "1-5 human rating"
      - vietnamese_quality: "1-5 chất lượng tiếng Việt"
    
    performance:
      - latency_p50: "Median response time (ms)"
      - latency_p99: "99th percentile (ms)"
      - tokens_per_second: "Tốc độ generate"
    
    cost:
      - cost_per_1k_tokens: "USD / 1K tokens (input + output)"
      - monthly_estimate: "Chi phí hàng tháng cho 1 khóa học"
    
    practical:
      - context_window: "Max tokens"
      - multimodal: "Hỗ trợ image/video/audio?"
      - function_calling: "Có / Không / Quality"
      - streaming: "Có / Không"
  
  methodology:
    - "Mỗi task chạy 3 lần → lấy trung bình"
    - "Đánh giá quality bởi 2 reviewer độc lập"
    - "Ghi lại TOÀN BỘ prompts + outputs"
    - "Screenshot / recording làm bằng chứng"
```

### Bước 3: Báo cáo

```yaml
benchmark_report:
  format: "benchmark-[category]-YYYY-MM.md"
  
  sections:
    executive_summary: "Top 3 findings — CEO đọc đây"
    methodology: "Setup, datasets, metrics"
    results_table: "Bảng so sánh đầy đủ"
    detailed_analysis: "Phân tích từng chiều"
    cost_analysis: "Chi phí vận hành cho ABM"
    recommendation: "Model nào dùng cho mục đích nào"
    raw_data: "Link to full results spreadsheet"
```

## Mẫu bảng kết quả

| Model | Accuracy | VN Quality | Latency P50 | Cost/1K | Context | SQUARE |
|-------|:--------:|:----------:|:-----------:|:-------:|:-------:|:------:|
| GPT-4o | 92% | ★★★★☆ | 1.2s | $0.01 | 128K | 43/60 |
| Gemini 2.5 | 90% | ★★★★★ | 0.8s | $0.007 | 1M | 45/60 |
| Claude 3.5 | 91% | ★★★★☆ | 1.5s | $0.012 | 200K | 42/60 |
| Qwen 2.5 | 85% | ★★★☆☆ | 0.5s | Free* | 128K | 38/60 |

## Benchmark templates theo use case

```yaml
benchmark_templates:
  llm_general:
    tasks: ["QA", "Summarize", "Translate", "Code", "Reasoning"]
    metrics: ["Accuracy", "VN Quality", "Latency", "Cost"]
  
  rag_system:
    tasks: ["Retrieval Accuracy", "Answer Quality", "Hallucination Rate"]
    metrics: ["Precision@5", "ROUGE-L", "Faithfulness Score"]
  
  image_generation:
    tasks: ["Text-to-Image", "Image Edit", "Style Transfer"]
    metrics: ["FID", "Human Rating", "Speed", "Cost"]
  
  code_assistant:
    tasks: ["Code Generation", "Bug Fix", "Refactor", "Explain"]
    metrics: ["Pass@1", "Correctness", "Code Quality"]
```

## Budget Template — Chi phí R&D

```yaml
rd_budget:
  api_costs:
    llm_benchmarking:
      - model: "GPT-4o"
        cost_per_1k_tokens: "$0.01 input / $0.03 output"
        benchmark_budget: "~100 calls × 2K tokens = $6/benchmark"
      - model: "Gemini 2.5 Pro"
        cost_per_1k_tokens: "$0.00125 input / $0.01 output"
        benchmark_budget: "~100 calls × 2K tokens = $2.25/benchmark"
      - model: "Claude 3.5 Sonnet"
        cost_per_1k_tokens: "$0.003 input / $0.015 output"
        benchmark_budget: "~100 calls × 2K tokens = $3.6/benchmark"
    
    monthly_estimate:
      benchmarks: "2-3 / tháng × $10 avg = $20-30"
      trend_research: "Deep research API = $5-10"
      total_api: "$25-40 / tháng (~625K-1M VNĐ)"
  
  compute_costs:
    colab_pro_plus: "$49.99/tháng — A100 GPU cho fine-tuning tests"
    local_gpu: "Nếu có — $0 (điện ~200K/tháng)"
    
  tools_costs:
    huggingface_pro: "$9/tháng — private models, inference"
    apify_starter: "$49/tháng — social media trend tracking (optional)"
    
  total_monthly:
    minimum: "$85 (~2.1M VNĐ) — API + Colab Pro+"
    recommended: "$135 (~3.4M VNĐ) — + HF Pro + Apify"
    
  roi_formula: |
    ROI = (Revenue từ modules mới tạo bởi R&D) / (Total R&D cost)
    Target: ROI ≥ 5x trong 6 tháng đầu
    VD: 1 module mới → 30 HV × 2.4M = 72M revenue vs 20M R&D cost = 3.6x
```

---

## Output khi được yêu cầu

1. **Benchmark Report** — Bảng so sánh + phân tích chi tiết
2. **SQUARE Scorecard** — Chấm điểm 6 chiều cho models
3. **Cost Analysis** — Chi phí vận hành cho ABM
4. **Recommendation** — Model nào cho mục đích nào
5. **Lab Exercise** — Bài lab cho học viên tự benchmark
6. **Budget Estimate** — Chi phí API/compute cho benchmark
