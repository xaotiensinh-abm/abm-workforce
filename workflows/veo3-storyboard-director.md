---
description: Multi-Agent workflow để tạo storyboard VEO3 chuyên nghiệp - từ concept đến production-ready prompts
version: 2.0
---

# 🎬 VEO3 Storyboard Director

// turbo-all

## Overview

Workflow multi-agent chuyên tạo storyboard cho video AI dài trên VEO3. 
- Mỗi video clip = **8 giây** (VEO3 optimal duration)
- Video = **Start Frame + End Frame + Motion Prompt**
- Hỗ trợ 2 modes: **Seamless** (story) và **Cinematic** (TVC)

---

## 📥 Step 1: Input Collection

Thu thập từ user:

```markdown
Story: [Câu chuyện/concept video]
Duration: [Tổng thời lượng, VD: 32 giây]
Mode: [Seamless / Cinematic]
Platform: [YouTube / TikTok / TVC]
Voice Over: [Yes / No]
Style: [Documentary / Cinematic / Commercial]
Reference: [Video tham khảo nếu có]
```

**Output**: `project_brief.md`

---

## 🎬 Step 2: Director Agent - Mode Selection & Identity Locks

**Role**: Phân tích story, chọn mode, tạo Identity Locks

### Mode Decision:
| If Story Needs... | Choose |
|:--|:--|
| Continuous narrative, character journey | **SEAMLESS** |
| Multiple scenes, product focus, dynamic cuts | **CINEMATIC** |

### Identity Locks (Template: `templates/identity_locks_template.md`):

```markdown
## 🔒 IDENTITY LOCKS

📌 LOCATION: [Giữ nguyên / Changes allowed]
📌 CHARACTER: [100% consistent / Varies]  
📌 PRODUCT/BRAND: [100% consistent]
📌 CAMERA: [Fixed position / Dynamic]
📌 LIGHTING: [Progressive / Independent per scene]
📌 STYLE: [Unified aesthetic throughout]
📌 TEXT: [❌ NO VIETNAMESE TEXT - All text added in post-production]
```

> ⚠️ **RULE R009: NO VIETNAMESE TEXT** - VEO3 không render text tiếng Việt tốt. Tất cả text phải thêm trong POST-PRODUCTION.

**Output**: `identity_locks.md`

---

## 📐 Step 3: Storyboard Architect - Scene Segmentation

**Role**: Chia scenes, thiết kế Start/End Frames

### 8-Second Rule:
```
Total Duration ÷ 8 = Number of Scenes
Example: 32s ÷ 8s = 4 scenes
```

### Mode-Specific Rules:

**SEAMLESS Mode:**
- End Frame của Scene N = Start Frame của Scene N+1
- Subject giữ nguyên 100%
- Lighting progression tự nhiên

**CINEMATIC Mode:**
- Scenes độc lập
- Jump cuts cho phép
- Product/Brand consistent, context thay đổi OK

### Scene Design (Template: `templates/scene_breakdown_template.md`):

```markdown
## SCENE [N]: [TITLE] (8s)

### 📍 START FRAME (0s)
- Subject: [Chi tiết ở trạng thái đầu]
- Position: [Vị trí trong frame]
- Environment: [Bối cảnh]
- Lighting: [Ánh sáng]

### 📍 END FRAME (8s)
- Subject: [Trạng thái sau 8s]
- Key Visual: [Điểm nhấn]

### 🎬 TRANSFORMATION
[Mô tả chi tiết sự thay đổi 0→8s]

### 🔗 TRANSITION
[Seamless: End = Next Start / Cinematic: Cut type]
```

**Output**: `scene_breakdown.md`

---

## 🖼️ Step 4: Image Prompt Engineer - Nano Banana Pro

**Skill Reference**: `/nano-banana-pro-prompt`, `D:\Antigravity\Skill\Master-Guide-to-Nano-Banana-Pro-Prompts-main`

### Master Formula:
```
[SUBJECT + CHI TIẾT] + [HÀNH ĐỘNG] + [BỐI CẢNH]
+ [CAMERA/GÓC MÁY] + [ÁNH SÁNG] + [PHONG CÁCH]
```

### Consistency Lock (SEAMLESS Mode):
```
"Keep the [person/product] exactly as shown with 100% identical 
[facial features/design]. Same [skin tone/colors], [hair/texture]."
```

### Image Prompt Format:
```markdown
## SCENE [N] - IMAGE PROMPTS

### 📸 START FRAME

📝 English Prompt:
[Consistency lock if SEAMLESS]
[Full Nano Banana Pro prompt]
Shot on [lens] at [f-stop]. [Camera position]. [Style].

📝 Vietnamese:
[Bản diễn giải tiếng Việt]

💡 Tech: Camera: [specs] | Lighting: [type] | Style: [reference]

---

### 📸 END FRAME
📝 English Prompt:
[Consistency lock]
[Transformed state description]
[Same technical specs for consistency]
```

### Negative Prompt Lock (BắT BUỘC):
```
[NEGATIVE]: NO TEXT, NO NUMBERS, NO VIETNAMESE CHARACTERS, NO READABLE LETTERS, 
no text overlays, no banners with text, no price tags with numbers
```

**Output**: `image_prompts.md`

---

## 🎥 Step 5: VEO3 Prompt Engineer - Motion Prompts

**Template**: `templates/veo3_prompt_template.md`

### JSON Format (Complex):
```json
{
  "scene_id": 1,
  "duration": "8s",
  "mode": "seamless",
  "subject": {
    "description": "[Chi tiết]",
    "state_start": "[Trạng thái đầu]",
    "state_end": "[Trạng thái cuối]",
    "action": "[Movement]"
  },
  "camera": {
    "shot_type": "[wide/medium/close-up]",
    "movement": "[static/pan/dolly/orbit]",
    "lens": "[35mm/85mm]"
  },
  "lighting": {...},
  "audio": {
    "dialogue": "[Speech]",
    "sfx": ["[Sound 1]"],
    "ambient": "[Background]",
    "music": "[Mood/tempo]"
  },
  "style": {...}
}
```

### Natural Format (Simple):
```
[Shot type] of [subject] [action], transitioning from [start] to [end] over 8s.
[Environment]. [Lighting]. [Style].
Camera: [movement], [lens]. 
Audio: SFX: [sounds]. Ambient: [background]. Music: [description].
```

**Output**: `veo3_prompts.md`

---

## 🎤 Step 6: Voice Over Writer (if Voice Over = Yes)

**Template**: `templates/voice_over_template.md`

### 8-Second Sync:
```markdown
## Scene [N] Voice Over (8s)

| Time | Visual | Voice Over | Tone |
|:--|:--|:--|:--|
| 0-2s | [Action] | "[10-15 words]" | [Emotion] |
| 2-4s | [Action] | "[10-15 words]" | [Emotion] |
| 4-6s | [Action] | "[10-15 words]" | [Emotion] |
| 6-8s | [Action] | "[10-15 words]" | [Emotion] |

**Pacing**: [Slow/Medium/Fast]
**Word Count**: [40-60 words for 8s]
```

**Output**: `voice_over.md`

---

## 🔍 Step 7: Consistency Auditor - Quality Gate

### Checklist:
```markdown
## ✅ Consistency Checklist

### Identity Locks ✓
- [ ] Location consistent per mode rules
- [ ] Character 100% identical (SEAMLESS)
- [ ] Product/Brand 100% identical
- [ ] Style unified throughout

### Technical ✓
- [ ] Each scene ≤ 8 seconds
- [ ] [SEAMLESS] End Frame N = Start Frame N+1
- [ ] Image prompts include consistency locks
- [ ] VEO3 prompts include audio design

### Voice Over ✓ (if applicable)
- [ ] Word count within 8s limit per scene
- [ ] Sync points match visual action
- [ ] Tone consistent with video mood
### Text-Free Visual Check ✓
- [ ] NO Vietnamese text in any image prompt
- [ ] NO numbers or prices visible in frames
- [ ] All text elements replaced with visual symbols (graphs, icons, colors)
- [ ] Negative prompts include: "NO TEXT, NO VIETNAMESE CHARACTERS"
- [ ] Post-production text plan documented
```

---

## 📦 Step 8: Package Delivery

**Template**: `templates/storyboard_package_template.md`

### Final Deliverable Structure:
```
📦 STORYBOARD PACKAGE: [Project Title]

├── 📋 Overview (Duration, Scenes, Mode, Platform)
├── 🔒 Identity Locks
├── 📐 Scene Breakdown (N scenes × Start/End Frames)
├── 🖼️ Image Prompts (N×2 prompts)
├── 🎬 VEO3 Prompts (N video prompts)
├── 🎤 Voice Over Script (if applicable)
├── ✅ Consistency Checklist
└── 🎬 Production Guide
```

---

## 🔧 Skills Integration

| Skill | Usage |
|:--|:--|
| `/nano-banana-pro-prompt` | Image prompts (Step 4) |
| `Master-Guide-to-Nano-Banana-Pro-Prompts-main` | Advanced prompt techniques |
| `/agent-manager` | Multi-agent orchestration |
| `ai-multimodal` | Video reference analysis |

---

## 💡 Pro Tips

1. **Reference First**: Có video tham khảo? Dùng `ai-multimodal` để reverse-engineer
2. **Test 1 Scene**: Generate 1 scene trước để validate style
3. **Audio Matters**: Audio design trong VEO3 prompt giúp AI hiểu mood
4. **Consistency is King**: SEAMLESS mode = nhất quán tuyệt đối
5. **JSON for Complex**: Scenes phức tạp → dùng JSON format
6. **🚨 NO VIETNAMESE TEXT**: VEO3 render text tiếng Việt rất xấu - dùng visual symbols thay thế, thêm text trong post-production
7. **Visual Alternatives**: Thay text bằng: graphs/charts, color-coded elements, icons, abstract shapes
