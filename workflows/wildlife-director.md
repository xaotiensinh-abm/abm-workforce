---
description: Đạo diễn video động vật viral với Multi-Agent System - YouTube/TikTok Wildlife Content
---

Workflow Multi-Agent chuyên biệt cho việc sản xuất **video động vật viral** trên YouTube/TikTok, sử dụng VEO3 Text-to-Video.

---

## 🎯 Tổng quan

Hệ thống này biến ý tưởng về động vật thành **video 8s viral-ready** với style nhất quán theo từng series. Áp dụng **5-Pillar Framework** và **Mission Control pattern**.

---

## ⚖️ GOVERNANCE: 6 Luật Không Phá Vỡ

| # | Rule | Mô tả |
|---|------|-------|
| **R001** | 8s Max | Mỗi cảnh = 8 giây (VEO3 default) |
| **R002** | One-Line | Mỗi prompt viết trên 1 dòng duy nhất |
| **R003** | Text-to-Video Only | Chỉ dùng T2V, không image reference |
| **R004** | Series Style Lock | Style PHẢI match với series đã định nghĩa |
| **R005** | No Text Overlay | Không có text trong video |
| **R006** | Natural Sound | Âm thanh tự nhiên ưu tiên |

---

## 👥 WORKFORCE: 5 Agents

| Agent | Emoji | Nhiệm vụ |
|-------|-------|----------|
| **Wildlife Director** | 🎬 | Mission Control, điều phối toàn bộ |
| **Research Agent** | 🔬 | Nghiên cứu hành vi, habitat động vật |
| **Style Director** | 🎨 | Áp dụng visual style theo series |
| **Prompt Writer** | ✍️ | Viết prompt VEO3 theo formula |
| **QA Auditor** | 🕵️ | Kiểm tra compliance với 6 rules |

---

## 🎬 3 SERIES ĐÃ ĐỊNH NGHĨA

### 🔬 Series 1: MICRO KINGDOMS
**Thế giới thu nhỏ - Đế chế của sinh vật bé nhỏ**

| Thuộc tính | Giá trị |
|------------|---------|
| **Mood** | Tò mò, kinh ngạc, ASMR |
| **Animals** | Kiến, ong, bướm, bọ cánh cứng, nhện, ốc sên |
| **Style Lock** | `Macro lens extreme close-up, shallow depth of field, vibrant saturated colors, soft golden backlight, dewdrops visible, ASMR aesthetic, bokeh background` |

---

### 🌙 Series 2: APEX HOUR
**Giờ của kẻ săn mồi - Khoảnh khắc đỉnh cao**

| Thuộc tính | Giá trị |
|------------|---------|
| **Mood** | Kịch tính, adrenaline, tôn kính sức mạnh |
| **Animals** | Sư tử, hổ, báo, cá mập, đại bàng, sói |
| **Style Lock** | `Cinematic dark moody atmosphere, high contrast, film grain, blue hour lighting, dramatic side-light, National Geographic documentary style` |

---

### 💚 Series 3: GENTLE GIANTS
**Đối lập hài hòa - Từ voi khổng lồ đến chim ruồi bé xíu**

| Thuộc tính | Giá trị |
|------------|---------|
| **Mood** | Healing, thư giãn, kết nối cảm xúc |
| **Animals** | Voi, cá voi, gấu + Chim ruồi, sóc, thỏ, mèo |
| **Style Lock** | `Soft cinematic, pastel color grade, dreamy gaussian blur background, golden hour warmth, emotional documentary style` |

---

## 🔧 PHASE 1: PLANNING

### Step 1.1: Series Selection
```
🎬 WILDLIFE DIRECTOR: Chọn series phù hợp với ý tưởng:
- [ ] Micro Kingdoms (côn trùng, sinh vật nhỏ, ASMR)
- [ ] Apex Hour (săn mồi, drama, kịch tính)
- [ ] Gentle Giants (healing, emotional, cute)
```

### Step 1.2: Animal Research
```
🔬 RESEARCH AGENT: Nghiên cứu về [ANIMAL]:
□ Tên khoa học
□ Habitat tự nhiên
□ Hành vi đặc trưng (3-5 actions tiêu biểu)
□ Thời điểm hoạt động (sáng/tối/seasonal)
□ Đặc điểm ngoại hình nổi bật
```

### Step 1.3: Scene Concept
```
🎨 STYLE DIRECTOR: Xây dựng concept cảnh:
□ Animal: [tên động vật]
□ Action: [hành động cụ thể]
□ Environment: [môi trường/bối cảnh]
□ Time: [thời điểm trong ngày]
□ Mood: [cảm xúc muốn truyền tải]
```

**→ HITL Checkpoint: User approve concept**

---

## 🔧 PHASE 2: PRODUCTION

### Step 2.1: Apply Style Lock
```
🎨 STYLE DIRECTOR: Áp dụng Style Lock của series [SERIES_NAME]:
[PASTE STYLE LOCK HERE]
```

### Step 2.2: Build Prompt (6-Element Formula)
```
✍️ PROMPT WRITER: Xây dựng prompt theo formula:

[STYLE LOCK] + [ANIMAL] + [ACTION] + [ENVIRONMENT] + [TIME/LIGHTING] + [CAMERA] + [AUDIO CUE]
```

**Camera Vocabulary:**
| Shot | Dùng khi |
|------|----------|
| `extreme close-up` | Chi tiết (mắt, lông, vảy) |
| `wide establishing shot` | Toàn cảnh habitat |
| `tracking shot` | Follow movement |
| `slow push-in` | Build tension |
| `orbit shot` | Reveal grandeur |
| `low angle shot` | Power, dominance |

**Motion Keywords by Animal Type:**
| Type | Keywords |
|------|----------|
| Fast Predators | `explosive burst`, `powerful stride`, `lightning reflexes` |
| Slow Giants | `deliberate movement`, `majestic pace`, `gentle sway` |
| Birds | `graceful glide`, `hover mid-air`, `sudden dive` |
| Insects | `quick darting`, `methodical crawl`, `delicate flutter` |

### Step 2.3: Prompt Optimization
```
✍️ PROMPT WRITER: Tối ưu hóa prompt:
□ Đảm bảo 1 dòng duy nhất
□ Thêm audio cue phù hợp
□ Kiểm tra flow câu văn
□ Remove redundancy
```

**→ HITL Checkpoint: User approve prompt**

---

## 🔧 PHASE 3: QUALITY

### Step 3.1: Rule Compliance Check
```
🕵️ QA AUDITOR: Kiểm tra 6 Rules:
□ R001: Prompt tạo video 8s phù hợp? ✓/✗
□ R002: Prompt trên 1 dòng duy nhất? ✓/✗
□ R003: Không có image reference? ✓/✗
□ R004: Style Lock match series? ✓/✗
□ R005: Không yêu cầu text overlay? ✓/✗
□ R006: Audio tự nhiên/phù hợp? ✓/✗
```

### Step 3.2: Style Consistency Audit
```
🕵️ QA AUDITOR: Kiểm tra Style Consistency:
□ Visual style match series definition
□ Mood phù hợp với series
□ Lighting keywords correct
□ Color grade keywords present
```

### Step 3.3: Delivery Package
```
📦 DELIVERY:
├── prompt.txt        # VEO3 prompt (1 dòng)
├── metadata.json     # Series, animal, style info
└── notes.md          # Research notes
```

### Step 3.4: Export TXT (cho video nhiều cảnh)
```
📄 EXPORT PROMPTS.TXT:
Khi tạo video dài (VD: 64s = 8 cảnh):

1. Tạo file [series]_prompts.txt
2. Mỗi prompt = 1 dòng duy nhất
3. Đánh số thứ tự: "1. [prompt]", "2. [prompt]"...
4. KHÔNG thêm bất kỳ nội dung nào khác
5. Sẵn sàng copy-paste vào VEO3

Format:
1. [Full prompt scene 1]
2. [Full prompt scene 2]
...
N. [Full prompt scene N]
```

---

## 📝 PROMPT TEMPLATES

### Template: Micro Kingdoms
```
Macro lens extreme close-up, shallow depth of field, vibrant saturated colors, soft golden backlight, [ANIMAL_DESCRIPTION] [ACTION_DESCRIPTION], [DETAIL_DESCRIPTION], [ENVIRONMENT_BOKEH], [AUDIO_CUE]
```

### Template: Apex Hour
```
Cinematic dark moody atmosphere, high contrast, film grain, blue hour lighting, [ANIMAL_DESCRIPTION] [ACTION_DESCRIPTION], [DRAMATIC_DETAIL], [CAMERA_MOVEMENT], [AUDIO_CUE]
```

### Template: Gentle Giants
```
Soft cinematic, pastel color grade, dreamy gaussian blur background, golden hour warmth, [ANIMAL_DESCRIPTION] [ACTION_DESCRIPTION], [EMOTIONAL_DETAIL], [PEACEFUL_AUDIO]
```

---

## 🎯 VÍ DỤ PROMPT HOÀN CHỈNH

### Micro Kingdoms - Honeybee
```
Macro lens extreme close-up, shallow depth of field, vibrant saturated colors, soft golden backlight, a honeybee covered in bright yellow pollen lands delicately on a purple lavender flower, its legs carefully brush against stamens collecting golden pollen grains, translucent wings catching sunlight and creating rainbow refraction, dewdrops visible on flower petals, lush garden bokeh background, ambient sound of gentle buzzing and soft rustling leaves
```

### Apex Hour - Lion
```
Cinematic dark moody atmosphere, high contrast, film grain, blue hour lighting, a massive male lion with dark scarred mane walks slowly through tall dry African savanna grass at dusk, muscles rippling beneath weathered golden fur, intense amber eyes scan the distant horizon, dust particles float in dramatic side-light casting long shadows, low angle tracking shot, distant thunder rumbles as a storm approaches
```

### Gentle Giants - Baby Elephant
```
Soft cinematic, pastel color grade, dreamy gaussian blur background, golden hour warmth, an adorable baby elephant playfully sprays crystal water with its tiny trunk while mother elephant watches protectively nearby, African waterhole at magical sunset, warm orange and pink reflections shimmer on calm water surface, the calf splashes joyfully creating water droplets that catch golden light, peaceful ambient sounds of splashing water and distant bird calls
```

---

## 🚀 QUICK START

1. **Chọn Series**: Micro Kingdoms / Apex Hour / Gentle Giants
2. **Chọn Animal + Action**: VD: "Ong thu thập phấn hoa"
3. **Chạy workflow**: Agent sẽ tự động generate prompt
4. **Review & Approve**: Kiểm tra prompt trước khi generate video
5. **Generate**: Copy prompt → VEO3 → Get 8s video

---

## 📚 REFERENCES

- VEO Fashion Director: `~/.gemini/antigravity/global_workflows/veo-fashion-director.md`
- Agent Manager: `~/.gemini/antigravity/global_workflows/agent-manager.md`
- 5-Pillar Framework: Knowledge Base
