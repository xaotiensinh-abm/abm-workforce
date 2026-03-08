---
name: "blockrun"
description: "Gateway đa model AI — tạo ảnh (DALL-E, Nano Banana), truy vấn Grok real-time, GPT-5.2, DeepSeek qua micropayment wallet. Không cần API keys riêng."
---

# BlockRun — Gateway Đa Model AI

Framework kết nối nhiều model AI qua hệ thống micropayment (x402). Tạo ảnh, tìm kiếm X/Twitter real-time, second opinion từ nhiều LLM — tất cả qua 1 wallet duy nhất.

## Sử dụng skill này khi

- User yêu cầu tạo ảnh (DALL-E, Nano Banana)
- Cần dữ liệu real-time từ X/Twitter (Grok Live Search)
- Muốn second opinion từ GPT-5.2 hoặc model khác
- Cần xử lý giá rẻ (DeepSeek)
- User nói "blockrun", "use grok", "use gpt", "generate image"

## KHÔNG sử dụng khi

- Agent có thể tự xử lý (không cần model ngoài)
- Cần image editing phức tạp → dùng `image-studio`
- Cần tạo video → dùng `veo-video-gen`
- Cần thiết kế workflow visual → dùng `freepik-spaces`

## Cơ Chế Hoạt Động

```
User yêu cầu → BlockRun SDK → Wallet thanh toán tự động
                                ↓
               ┌────────────────┼────────────────┐
               ↓                ↓                ↓
          DALL-E 3         Nano Banana       Grok-3
        ($0.04/img)       ($0.01/img)     ($3/M tokens)
              Photorealistic    Artistic      + Live Search
                                             ($0.025/source)
```

## Bảng Giá Models

| Model | Chức năng | Giá |
|-------|----------|-----|
| `openai/dall-e-3` | Tạo ảnh photorealistic | $0.04/ảnh |
| `google/nano-banana` | Tạo ảnh artistic, nhanh | **$0.01/ảnh** (rẻ nhất) |
| `xai/grok-3` | Chat + Live Search X/Twitter | $3/M tokens + $0.025/source |
| `openai/gpt-5.2` | Second opinion, code review | $1.75/M input, $14/M output |
| `deepseek/deepseek-chat` | Xử lý bulk giá rẻ | $0.14/M input, $0.28/M output |
| `google/gemini-2.5-flash` | Tài liệu dài, nhanh | $0.15/M input, $0.60/M output |

## Hướng Dẫn Sử Dụng

### Cài đặt
```bash
pip install blockrun-llm
```

### Khởi tạo Wallet
```python
from blockrun_llm import setup_agent_wallet
client = setup_agent_wallet()  # Tự tạo wallet, hiện QR nếu mới
```

### Tạo Ảnh
```python
from blockrun_llm import ImageClient
client = ImageClient()
result = client.generate("Logo startup công nghệ giáo dục")
print(result.data[0].url)
```

### Live Search X/Twitter
```python
response = client.chat(
    "xai/grok-3",
    "Xu hướng AI mới nhất trên X hôm nay?",
    search=True  # BẮT BUỘC cho real-time data
)
```

### Second Opinion
```python
response = client.chat("openai/gpt-5.2", "Review đoạn code này...")
```

## Lưu Ý

- Wallet cần nạp USDC trên Base network ($1-5 để bắt đầu)
- Luôn bật `search=True` khi cần dữ liệu real-time từ X
- Theo dõi chi tiêu: `client.get_spending()`
- File wallet: `$HOME/.blockrun/.session`

## Nguồn gốc
- Nguồn: [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) — `blockrun` (community)
- Adapter: ABM Workforce v2.1 — Jarvis Orchestrator
