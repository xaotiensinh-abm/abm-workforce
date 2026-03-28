---
name: "Goal"
description: "Xử lý và sinh nội dung multimedia (audio, image, video, PDF, image generation) sử dụng Google Gemini API — cung cấp giao diện thống nhất cho mọi loại media với hỗ trợ batch processing và cost optimiza"
---

﻿---
name: ai-multimodal
description: Process multimedia (audio/video/image/PDF) via Gemini API. Transcription, analysis, generation.
license: MIT
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# Goal

> **Use this skill when:** audio, video, image, or PDF processing via Gemini API

Xử lý và sinh nội dung multimedia (audio, image, video, PDF, image generation) sử dụng Google Gemini API — cung cấp giao diện thống nhất cho mọi loại media với hỗ trợ batch processing và cost optimization.

# Instructions


# AI Multimodal Processing Skill

Process audio, images, videos, documents, and generate images using Google Gemini's multimodal API. Unified interface for all multimedia content understanding and generation.

## Core Capabilities

### Audio Processing
- Transcription with timestamps (up to 9.5 hours)
- Audio summarization and analysis
- Speech understanding and speaker identification
- Music and environmental sound analysis
- Text-to-speech generation with controllable voice

### Image Understanding
- Image captioning and description
- Object detection with bounding boxes (2.0+)
- Pixel-level segmentation (2.5+)
- Visual question answering
- Multi-image comparison (up to 3,600 images)
- OCR and text extraction

### Video Analysis
- Scene detection and summarization
- Video Q&A with temporal understanding
- Transcription with visual descriptions
- YouTube URL support
- Long video processing (up to 6 hours)
- Frame-level analysis

### Document Extraction
- Native PDF vision processing (up to 1,000 pages)
- Table and form extraction
- Chart and diagram analysis
- Multi-page document understanding
- Structured data output (JSON schema)
- Format conversion (PDF to HTML/JSON)

### Image Generation
- Text-to-image generation
- Image editing and modification
- Multi-image composition (up to 3 images)
- Iterative refinement
- Multiple aspect ratios (1:1, 16:9, 9:16, 4:3, 3:4)
- Controllable style and quality

## Capability Matrix

| Task | Audio | Image | Video | Document | Generation |
|------|:-----:|:-----:|:-----:|:--------:|:----------:|
| Transcription | ✓ | - | ✓ | - | - |
| Summarization | ✓ | ✓ | ✓ | ✓ | - |
| Q&A | ✓ | ✓ | ✓ | ✓ | - |
| Object Detection | - | ✓ | ✓ | - | - |
| Text Extraction | - | ✓ | - | ✓ | - |
| Structured Output | ✓ | ✓ | ✓ | ✓ | - |
| Creation | TTS | - | - | - | ✓ |
| Timestamps | ✓ | - | ✓ | - | - |
| Segmentation | - | ✓ | - | - | - |

## Model Selection Guide

### Gemini 3 Series (Preview - Latest)
- **gemini-3-pro-preview**: Latest multimodal model, enhanced reasoning, largest context
- **gemini-3-pro-image-preview**: Advanced image generation with superior quality and consistency

### Gemini 2.5 Series (Stable - Recommended)
- **gemini-2.5-pro**: Highest quality, all features, 1M-2M context
- **gemini-2.5-flash**: Best balance, all features, 1M-2M context
- **gemini-2.5-flash-lite**: Lightweight, segmentation support
- **gemini-2.5-flash-image**: Image generation only

### Gemini 2.0 Series
- **gemini-2.0-flash**: Fast processing, object detection
- **gemini-2.0-flash-lite**: Lightweight option

### Feature Requirements
- **Segmentation**: Requires 2.5+ models
- **Object Detection**: Requires 2.0+ models
- **Multi-video**: Requires 2.5+ models
- **Image Generation**: Use `gemini-3-pro-image-preview` (latest) or `gemini-2.5-flash-image` (stable)

### Context Windows
- **2M tokens**: ~6 hours video (low-res) or ~2 hours (default)
- **1M tokens**: ~3 hours video (low-res) or ~1 hour (default)
- **Audio**: 32 tokens/second (1 min = 1,920 tokens)
- **PDF**: 258 tokens/page (fixed)
- **Image**: 258-1,548 tokens based on size

## Quick Start

### Prerequisites
**API Key Setup**: Supports both Google AI Studio and Vertex AI.

The skill checks for `GEMINI_API_KEY` in this order:
1. Process environment: `export GEMINI_API_KEY="your-key"`
2. Project root: `.env`
3. `.claude/.env`
4. `.claude/skills/.env`
5. `.claude/skills/ai-multimodal/.env`

**Get API key**: https://aistudio.google.com/apikey

**For Vertex AI**:
```bash
export GEMINI_USE_VERTEX=true
export VERTEX_PROJECT_ID=your-gcp-project-id
export VERTEX_LOCATION=us-central1  # Optional
```

**Install SDK**:
```bash
pip install google-genai python-dotenv pillow
```

### Common Patterns

**Transcribe Audio**:
```bash
python scripts/gemini_batch_process.py \
  --files audio.mp3 \
  --task transcribe \
  --model gemini-3-pro-preview
```

**Analyze Image**:
```bash
python scripts/gemini_batch_process.py \
  --files image.jpg \
  --task analyze \
  --prompt "Describe this image" \
  --output docs/assets/<output-name>.md \
  --model gemini-3-pro-preview
```

**Process Video**:
```bash
python scripts/gemini_batch_process.py \
  --files video.mp4 \
  --task analyze \
  --prompt "Summarize key points with timestamps" \
  --output docs/assets/<output-name>.md \
  --model gemini-3-pro-preview
```

**Extract from PDF**:
```bash
python scripts/gemini_batch_process.py \
  --files document.pdf \
  --task extract \
  --prompt "Extract table data as JSON" \
  --output docs/assets/<output-name>.md \
  --format json
```

**Generate Image (Gemini 3)**:
```bash
python scripts/gemini_batch_process.py \
  --task generate \
  --prompt "A futuristic city at sunset" \
  --output docs/assets/<output-file-name> \
  --model gemini-3-pro-image-preview \
  --aspect-ratio 16:9
```

**Generate Image (Gemini 2.5 - Stable)**:
```bash
python scripts/gemini_batch_process.py \
  --task generate \
  --prompt "A futuristic city at sunset" \
  --output docs/assets/<output-file-name> \
  --model gemini-2.5-flash-image \
  --aspect-ratio 16:9
```

**Optimize Media**:
```bash
# Prepare large video for processing
python scripts/media_optimizer.py \
  --input large-video.mp4 \
  --output docs/assets/<output-file-name> \
  --target-size 100MB

# Batch optimize multiple files
python scripts/media_optimizer.py \
  --input-dir ./videos \
  --output-dir docs/assets/optimized \
  --quality 85
```

**Convert Documents to Markdown**:
```bash
# Convert to PDF
python scripts/document_converter.py \
  --input document.docx \
  --output docs/assets/document.md

# Extract pages
python scripts/document_converter.py \
  --input large.pdf \
  --output docs/assets/chapter1.md \
  --pages 1-20
```

## Supported Formats

### Audio
- WAV, MP3, AAC, FLAC, OGG Vorbis, AIFF
- Max 9.5 hours per request
- Auto-downsampled to 16 Kbps mono

### Images
- PNG, JPEG, WEBP, HEIC, HEIF
- Max 3,600 images per request
- Resolution: ≤384px = 258 tokens, larger = tiled

### Video
- MP4, MPEG, MOV, AVI, FLV, MPG, WebM, WMV, 3GPP
- Max 6 hours (low-res) or 2 hours (default)
- YouTube URLs supported (public only)

### Documents
- PDF only for vision processing
- Max 1,000 pages
- TXT, HTML, Markdown supported (text-only)

### Size Limits
- **Inline**: <20MB total request
- **File API**: 2GB per file, 20GB project quota
- **Retention**: 48 hours auto-delete

## Reference Navigation
For detailed implementation guidance, see:

### Audio Processing
- `references/audio-processing.md` - Transcription, analysis, TTS
  - Timestamp handling and segment analysis
  - Multi-speaker identification
  - Non-speech audio analysis
  - Text-to-speech generation

### Image Understanding
- `references/vision-understanding.md` - Captioning, detection, OCR
  - Object detection and localization
  - Pixel-level segmentation
  - Visual question answering
  - Multi-image comparison

### Video Analysis
- `references/video-analysis.md` - Scene detection, temporal understanding
  - YouTube URL processing
  - Timestamp-based queries
  - Video clipping and FPS control
  - Long video optimization

### Document Extraction
- `references/document-extraction.md` - PDF processing, structured output
  - Table and form extraction
  - Chart and diagram analysis
  - JSON schema validation
  - Multi-page handling

### Image Generation
- `references/image-generation.md` - Text-to-image, editing
  - Prompt engineering strategies
  - Image editing and composition
  - Aspect ratio selection
  - Safety settings

## Cost Optimization

### Token Costs
**Input Pricing**:
- Gemini 2.5 Flash: $1.00/1M input, $0.10/1M output
- Gemini 2.5 Pro: $3.00/1M input, $12.00/1M output
- Gemini 1.5 Flash: $0.70/1M input, $0.175/1M output

**Token Rates**:
- Audio: 32 tokens/second (1 min = 1,920 tokens)
- Video: ~300 tokens/second (default) or ~100 (low-res)
- PDF: 258 tokens/page (fixed)
- Image: 258-1,548 tokens based on size

**TTS Pricing**:
- Flash TTS: $10/1M tokens
- Pro TTS: $20/1M tokens

### Best Practices
1. Use `gemini-2.5-flash` for most tasks (best price/performance)
2. Use `gemini-3-pro-preview` for enhanced reasoning tasks
3. Use `gemini-3-pro-image-preview` for highest quality image generation
4. Use File API for files >20MB or repeated queries
5. Optimize media before upload (see `media_optimizer.py`)
6. Process specific segments instead of full videos
7. Use lower FPS for static content
8. Implement context caching for repeated queries
9. Batch process multiple files in parallel

## Rate Limits
**Free Tier**:
- 10-15 RPM (requests per minute)
- 1M-4M TPM (tokens per minute)
- 1,500 RPD (requests per day)

**YouTube Limits**:
- Free tier: 8 hours/day
- Paid tier: No length limits
- Public videos only

**Storage Limits**:
- 20GB per project
- 2GB per file
- 48-hour retention

## Error Handling
Common errors and solutions:
- **400**: Invalid format/size - validate before upload
- **401**: Invalid API key - check configuration
- **403**: Permission denied - verify API key restrictions
- **404**: File not found - ensure file uploaded and active
- **429**: Rate limit exceeded - implement exponential backoff
- **500**: Server error - retry with backoff

## Scripts Overview
All scripts support unified API key detection and error handling:

**gemini_batch_process.py**: Batch process multiple media files
- Supports all modalities (audio, image, video, PDF)
- Progress tracking and error recovery
- Output formats: JSON, Markdown, CSV
- Rate limiting and retry logic
- Dry-run mode

**media_optimizer.py**: Prepare media for Gemini API
- Compress videos/audio for size limits
- Resize images appropriately
- Split long videos into chunks
- Format conversion
- Quality vs size optimization

**document_converter.py**: Convert documents to PDF
- Convert DOCX, XLSX, PPTX to PDF
- Extract page ranges
- Optimize PDFs for Gemini
- Extract images from PDFs
- Batch conversion support

Run any script with `--help` for detailed usage.

## Resources
- [Audio API Docs](https://ai.google.dev/gemini-api/docs/audio)
- [Image API Docs](https://ai.google.dev/gemini-api/docs/image-understanding)
- [Video API Docs](https://ai.google.dev/gemini-api/docs/video-understanding)
- [Document API Docs](https://ai.google.dev/gemini-api/docs/document-processing)
- [Image Gen Docs](https://ai.google.dev/gemini-api/docs/image-generation)
- [Get API Key](https://aistudio.google.com/apikey)
- [Pricing](https://ai.google.dev/pricing)


# Examples

## Ví dụ 1: Transcribe audio

**Input:** `python scripts/gemini_batch_process.py --files audio.mp3 --task transcribe`n**Output:** Transcript với timestamps, speaker identification

## Ví dụ 2: Generate image

**Input:** `python scripts/gemini_batch_process.py --task generate --prompt 'A futuristic city' --model gemini-3-pro-image-preview`n**Output:** High-quality AI-generated image saved to output path

# Constraints

- KHÔNG ĐƯỢC upload file >2GB (File API limit)
- KHÔNG ĐƯỢC dùng Gemini 1.5 cho segmentation (requires 2.5+)
- LUÔN LUÔN check GEMINI_API_KEY trước khi gọi API
- LUÔN LUÔN optimize media trước upload nếu >20MB
- LUÔN LUÔN handle rate limits với exponential backoff

---

📦 Upgraded by Skill Generator v4.0 Audit

