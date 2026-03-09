---
name: "pptx"
description: "Tạo slide PowerPoint (.pptx) chuyên nghiệp — pitch deck, báo cáo, training. Dùng python-pptx. Giao tiếp tiếng Việt."
---

# 📊 PPTX — Tạo Slide PowerPoint Chuyên Nghiệp

Skill tạo file `.pptx` (Microsoft PowerPoint) bằng `python-pptx`.

## Sử dụng khi

- Tạo pitch deck cho investor/khách hàng
- Tạo báo cáo trình bày (monthly, quarterly)
- Tạo tài liệu training/onboarding
- Tạo proposal thương mại

## KHÔNG sử dụng khi

- Cần văn bản dài → dùng `docx`
- Cần bảng tính → dùng `xlsx`
- Cần poster/visual art → dùng `canvas-design`

## VÍ DỤ NHANH

```
Input:  "Tạo pitch deck 10 slides cho startup"
Output: pitch_deck.pptx
  → Slide 1: Cover (logo + tagline)
  → Slide 2: Problem
  → Slide 3: Solution
  → Slide 4: Market Size (TAM/SAM/SOM)
  → Slide 5-10: Business model, Traction, Team, Financials, Ask
```

---

## CÁCH TRIỂN KHAI

### Bước 1: Khởi tạo presentation

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

prs = Presentation()
prs.slide_width = Inches(13.333)  # 16:9
prs.slide_height = Inches(7.5)
```

### Bước 2: Cover slide

```python
slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank

# Background
background = slide.background
fill = background.fill
fill.solid()
fill.fore_color.rgb = RGBColor(0x0F, 0x17, 0x2A)  # Dark blue

# Title
left = Inches(1)
top = Inches(2.5)
txBox = slide.shapes.add_textbox(left, top, Inches(11), Inches(2))
tf = txBox.text_frame
p = tf.paragraphs[0]
p.text = "STARTUP NAME"
p.font.size = Pt(48)
p.font.bold = True
p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
p.alignment = PP_ALIGN.CENTER
```

### Bước 3: Content slide với bullets

```python
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Title
add_title(slide, "VẤN ĐỀ", Inches(0.5), Inches(0.5))

# Bullet points
bullets = [
    "80% doanh nghiệp SME chưa số hóa quy trình",
    "Mất 40% thời gian cho công việc thủ công",
    "Chi phí nhân sự tăng 15%/năm"
]
add_bullets(slide, bullets, Inches(0.5), Inches(1.5))
```

### Bước 4: Chart slide

```python
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE

chart_data = CategoryChartData()
chart_data.categories = ['2024', '2025', '2026']
chart_data.add_series('Doanh thu', (500, 1200, 2800))

slide.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_CLUSTERED,
    Inches(1), Inches(2), Inches(10), Inches(4.5),
    chart_data
)
```

### Bước 5: Lưu file

```python
prs.save('pitch_deck.pptx')
```

---

## DESIGN RULES

1. **Font**: Dùng 1 font family (Inter, Arial, hoặc Roboto)
2. **Tỷ lệ**: 16:9 (widescreen) — KHÔNG 4:3
3. **Tối đa 6 bullets/slide** — mỗi bullet ≤ 2 dòng
4. **Color palette**: Tối đa 3 màu chính + 1 accent
5. **Background**: Dark → white text HOẶC Light → dark text
6. **Image/chart chiếm ≥ 50%** diện tích slide khi có
7. **Không đọc slide** — slides hỗ trợ presenter, không thay presenter

## SLIDE TEMPLATES

| Loại | Số slides | Cấu trúc |
|------|:---------:|----------|
| **Pitch Deck** | 10-12 | Cover → Problem → Solution → Market → Business Model → Traction → Competition → Team → Financials → Ask |
| **Monthly Report** | 6-8 | Cover → Highlights → KPIs → Revenue → Issues → Next Steps |
| **Training** | 15-20 | Cover → Agenda → Content sections → Quiz → Summary |
| **Proposal** | 8-10 | Cover → Context → Approach → Timeline → Team → Pricing → Next Steps |

---

## Nguồn gốc
- Gốc: Anthropic official skills (pptx) — adapt cho ABM
- Thư viện: `python-pptx` (pip install python-pptx)
- ABM Workforce v2.4 — Jarvis Orchestrator
