---
description: Đạo diễn video thời trang VEO 3.1 với The Auteur's Algorithm
---

Workflow cho VEO 3.1 Image-to-Video, chuyên biệt cho **luxury fashion** và **cinematic advertising**.

---

## Tổng quan

Skill này biến ảnh thời trang tĩnh thành video điện ảnh cao cấp sử dụng "The Auteur's Algorithm" - coi từ ngữ như ánh sáng, cú pháp như vật lý.

---

## Bước 1: Physics & Texture Analysis

Phân tích ảnh input để xác định thuộc tính vật liệu:

| Loại vải | Đặc điểm | Motion Keywords |
|----------|----------|-----------------|
| **Structured/Rigid** (Leather, Denim) | Ít drape, giữ form | `stiff movement`, `minimal flutter` |
| **Fluid/Lightweight** (Silk, Chiffon) | Drape cao, mềm mại | `liquid movement`, `gentle flutter`, `fabric cascade` |

// turbo
Tham khảo: `D:\Antigravity\Skill\claude-skills\veo-fashion-director\references\visual_grammar.md`

---

## Bước 2: Narrative Archetype Selection

Chọn công thức điện ảnh phù hợp:

| Archetype | Khi nào dùng | Đặc điểm |
|-----------|--------------|----------|
| **Fabric Hero** | Focus texture & weave | Cận cảnh chi tiết vải |
| **Runway Walk** | Power & motion | Toàn thân, chuyển động mạnh |
| **Emotional Portrait** | Detail & mood | Biểu cảm, ánh sáng mood |
| **Surreal Editorial** | Scroll-stopping effects | Visual effects ấn tượng |

---

## Bước 3: The 5-Layer Cinematic Stack

Xây dựng prompt theo 5 layers:

### Layer 1: CAMERA
```
[CAMERA]: (Shot Type, Angle, Camera Movement, Lens, Focus, Aspect Ratio)
```
- Lenses: 35mm (wide), 85mm (portrait)
- Rigs: Glambot, Phantom
- Movements: Dolly, Orbit, Slow push-in

### Layer 2: SUBJECT ANCHOR
```
[SUBJECT]: (Detailed description of Model, Garment, Fabric Properties. *Reference input image*)
```
- Garment weight, fabric drape
- Model identity preservation

### Layer 3: ACTION CHOREOGRAPHY
```
[ACTION]: (Primary Motion, Secondary Motion [hair/fabric], Environmental Forces [wind/gravity])
```
Sử dụng **Force Prompting** để simulate gravity và drag.

### Layer 4: ENVIRONMENT/LIGHTING
```
[ENVIRONMENT]: (Location, Time of Day, Lighting Setup, Atmosphere)
```
Default: **Soft/Neutral** hoặc **Overcast**. Tránh direct sunlight trừ khi được yêu cầu.

### Layer 5: TECHNICAL/AUDIO
```
[AUDIO]: (Ambient Noise, Specific Sound Effects, Music Vibe)
[TECHNICAL]: (Resolution, Color Grade, Film Stock, Motion Speed)
```
Sonic textures: swish, clack, rustle

---

## Master Template

```text
[CAMERA]: (Shot Type, Angle, Camera Movement, Lens, Focus, Aspect Ratio)
[SUBJECT]: (Detailed description of Model, Garment, Fabric Properties. *Reference input image*)
[ACTION]: (Primary Motion, Secondary Motion [hair/fabric], Environmental Forces [wind/gravity])
[ENVIRONMENT]: (Location, Time of Day, Lighting Setup, Atmosphere)
[AUDIO]: (Ambient Noise, Specific Sound Effects, Music Vibe)
[TECHNICAL]: (Resolution, Color Grade, Film Stock, Texture Quality, Motion Speed: Real-time pacing)
[NEGATIVE]: (What to exclude: distortion, morphing, plastic skin, sliding feet)
```

---

## Troubleshooting Guide

| Vấn đề | Nguyên nhân | Giải pháp |
|--------|-------------|-----------|
| **Plastic Skin** | Thiếu skin texture keywords | Thêm `natural skin texture`, `pores visible` |
| **Sliding Feet** | Thiếu grounding | Thêm `feet firmly planted`, `stable stance` |
| **Fabric Hallucination** | Mô tả mơ hồ | Chi tiết hóa: `silk with liquid drape`, `weighted hem` |
| **Audio Hallucinations** | Conflict audio cues | Simplify audio description |
| **🚨 Vietnamese Text Lỗi** | VEO3 không render text VN tốt | **KHÔNG** dùng text tiếng Việt trong prompt. Thêm `[NEGATIVE]: NO TEXT, NO VIETNAMESE CHARACTERS`. Text thêm trong post-production |

---

## References

// turbo
- Principles: `D:\Antigravity\Skill\claude-skills\veo-fashion-director\references\principles.md`
- Visual Grammar: `D:\Antigravity\Skill\claude-skills\veo-fashion-director\references\visual_grammar.md`
- Formulas: `D:\Antigravity\Skill\claude-skills\veo-fashion-director\references\formulas.md`
- Advanced Techniques: `D:\Antigravity\Skill\claude-skills\veo-fashion-director\references\advanced_techniques.md`
