---
name: "agent-improve"
description: "Cải thiện agent — phân tích hiệu suất, prompt engineering, testing, và triển khai cải tiến có kiểm soát."
---

# Cải Thiện Agent (Agent Performance Optimization)

Quy trình cải thiện agent có hệ thống qua phân tích hiệu suất, prompt engineering, và lặp lại liên tục.

## Sử dụng skill này khi

- Agent cho kết quả chưa đạt yêu cầu
- Cần tối ưu prompt/persona của agent
- Muốn cải thiện chất lượng output agent
- Cần đánh giá và nâng cấp agent sau một thời gian sử dụng
- Phát triển test suite cho agent

## KHÔNG sử dụng khi

- Tạo agent mới → dùng `skill-creator`
- Cải tiến quy trình chung → dùng `kaizen`
- Tự tiến hóa hệ thống → dùng `capability-evolver`

## Quy Trình 4 Giai Đoạn

### Giai đoạn 1: Phân Tích Hiệu Suất & Baseline

#### 1.1 Thu thập dữ liệu hiệu suất
- Tỷ lệ hoàn thành task thành công
- Thời gian trung bình mỗi task
- Số lần thử lại (retries)
- Các lỗi phổ biến nhất

#### 1.2 Phân tích feedback
- Patterns trong feedback của CEO/user
- Các trường hợp agent phải escalate
- Output bị từ chối — lý do

#### 1.3 Phân loại Failure Modes
| Loại | Mô tả | Mức độ |
|------|--------|--------|
| Hiểu sai yêu cầu | Agent diễn giải sai task | Nghiêm trọng |
| Output thiếu | Thiếu section hoặc dữ liệu | Trung bình |
| Format sai | Không theo template yêu cầu | Nhẹ |
| Scope creep | Làm ngoài phạm vi | Trung bình |
| Hallucination | Tạo thông tin sai | Nghiêm trọng |

#### 1.4 Báo cáo Baseline
```
Agent: [tên agent]
Tỷ lệ thành công: [%]
Failure mode phổ biến nhất: [loại]
Điểm cần cải thiện: [1, 2, 3]
```

### Giai đoạn 2: Cải Thiện Prompt Engineering

#### 2.1 Chain-of-Thought
- Thêm bước suy nghĩ trung gian
- Yêu cầu agent giải thích logic trước khi output

#### 2.2 Few-Shot Examples
- Thêm 2-3 ví dụ output tốt vào prompt
- Đảm bảo ví dụ đa dạng scenarios

#### 2.3 Role Definition
- Clarify persona: CÓ THỂ và KHÔNG THỂ
- Thêm ranh giới rõ ràng cho scope

#### 2.4 Output Format
- Chuẩn hóa format output
- Thêm template bắt buộc
- Yêu cầu self-check trước khi trả kết quả

### Giai đoạn 3: Testing & Validation

#### 3.1 Test Suite
- Tạo 5-10 test cases cho mỗi agent
- Bao gồm: happy path, edge cases, adversarial inputs
- Mỗi test case có expected output rõ ràng

#### 3.2 A/B Testing
- Chạy agent cũ vs. agent mới trên cùng test cases
- So sánh: chất lượng, tốc độ, tỷ lệ thành công

#### 3.3 Metrics đánh giá
- Accuracy: output đúng yêu cầu
- Completeness: output đầy đủ
- Format compliance: đúng template
- Time efficiency: thời gian xử lý

### Giai đoạn 4: Triển Khai & Giám Sát

#### 4.1 Version Control
```
agent-v1.0.md → agent-v1.1.md (cải thiện prompt)
                 agent-v1.2.md (thêm examples)
```

#### 4.2 Staged Rollout
1. Test nội bộ (5 tasks)
2. Chạy song song (phiên bản cũ + mới)
3. Nếu mới tốt hơn → thay thế hoàn toàn

#### 4.3 Giám sát liên tục
- Theo dõi metrics sau triển khai
- So sánh vs. baseline
- Rollback nếu tệ hơn

## Tích Hợp Với ABM

- **Kết hợp capability-evolver**: agent-improve cho cải thiện cụ thể, capability-evolver cho tự tiến hóa
- **Kết hợp kaizen**: áp dụng nguyên tắc cải tiến từng bước
- **Decision Log**: ghi lại mọi thay đổi và lý do

## Nguồn gốc
- Nguồn: [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) — `agent-orchestration-improve-agent` (community)
- Adapter: ABM Workforce v2.0 — Jarvis Orchestrator
