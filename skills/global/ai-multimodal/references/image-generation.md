# Image Generation Reference

Comprehensive guide for image creation, editing, and composition using Gemini API.

## Core Capabilities
- **Text-to-Image**: Generate images from text prompts
- **Image Editing**: Modify existing images with text instructions
- **Multi-Image Composition**: Combine up to 3 images
- **Iterative Refinement**: Refine images conversationally
- **Aspect Ratios**: Multiple formats (1:1, 16:9, 9:16, 4:3, 3:4)
- **Style Control**: Control artistic style and quality
- **Text in Images**: Limited text rendering (max 25 chars)

## Model

**gemini-3-pro-image-preview** - Latest image generation (Preview)
- Advanced quality and consistency
- Enhanced text rendering
- Better prompt understanding

**gemini-2.5-flash-image** - Specialized for image generation (Stable)
- Input tokens: 65,536
- Output tokens: 32,768
- Knowledge cutoff: June 2025
- Supports: Text and image inputs, image outputs

## Quick Start

### Basic Generation
```python
from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

# Using Gemini 3 (latest)
response = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents='A serene mountain landscape at sunset with snow-capped peaks',
    config=types.GenerateContentConfig(
        response_modalities=['Image'],
        image_config=types.ImageConfig(aspect_ratio='16:9')
    )
)

# Save image
for i, part in enumerate(response.candidates[0].content.parts):
    if part.inline_data:
        with open(f'output-{i}.png', 'wb') as f:
            f.write(part.inline_data.data)
```

## Aspect Ratios

| Ratio | Use Case |
|-------|----------|
| 1:1 | Square, social media profile |
| 16:9 | Landscape, widescreen displays |
| 9:16 | Portrait, mobile stories |
| 4:3 | Standard photos |
| 3:4 | Portrait photos |

## Response Modalities

### Image Only
```python
config=types.GenerateContentConfig(
    response_modalities=['Image']
)
```

### Text Only (No Image)
```python
config=types.GenerateContentConfig(
    response_modalities=['Text']
)
```

### Both Image and Text
```python
config=types.GenerateContentConfig(
    response_modalities=['Image', 'Text']
)
```

## Image Editing

### Modify Existing Image
```python
from PIL import Image as PILImage

img = PILImage.open('photo.jpg')
response = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents=[
        'Change the sky to sunset colors',
        img
    ],
    config=types.GenerateContentConfig(
        response_modalities=['Image']
    )
)
```

### Style Transfer
```python
response = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents=[
        'Apply a watercolor painting style to this image',
        img
    ],
    config=types.GenerateContentConfig(
        response_modalities=['Image']
    )
)
```

### Object Addition/Removal
```python
# Add object
response = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents=[
        'Add a hot air balloon in the sky',
        img
    ],
    config=types.GenerateContentConfig(
        response_modalities=['Image']
    )
)

# Remove object
response = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents=[
        'Remove the person from this image',
        img
    ],
    config=types.GenerateContentConfig(
        response_modalities=['Image']
    )
)
```

## Multi-Image Composition

### Combine Multiple Images
```python
img1 = PILImage.open('background.jpg')
img2 = PILImage.open('subject.jpg')
img3 = PILImage.open('overlay.png')

response = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents=[
        'Create a composite: place the subject from the second image onto the background from the first image, with the overlay from the third',
        img1, img2, img3
    ],
    config=types.GenerateContentConfig(
        response_modalities=['Image']
    )
)
```

## Prompt Engineering

### Effective Prompt Structure
1. **Subject**: What is the main focus
2. **Environment**: Where/when is it
3. **Style**: Artistic style or medium
4. **Quality**: Technical specifications
5. **Mood**: Emotional tone

### Quality Modifiers
- `high quality`, `detailed`, `sharp focus`
- `professional photograph`, `studio lighting`
- `8k`, `ultra detailed`, `photorealistic`

### Style Keywords
- `photorealistic`, `cinematic`, `artistic`
- `oil painting`, `watercolor`, `digital art`
- `minimalist`, `vintage`, `modern`

### Subject Description
- Be specific about appearance, pose, expression
- Include relevant details (clothing, accessories)
- Specify relationships between elements

### Composition and Framing
- `close-up`, `wide shot`, `bird's eye view`
- `centered composition`, `rule of thirds`
- `depth of field`, `bokeh background`

### Text in Images
- Maximum 25 characters recommended
- Use quotes for specific text: `"Hello World"`
- Simple fonts work best

## Advanced Techniques

### Iterative Refinement
```python
# Initial generation
response = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents='A fantasy castle on a hill',
    config=types.GenerateContentConfig(
        response_modalities=['Image']
    )
)

# Refine the result
refined = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents=[
        'Add more dramatic storm clouds and lightning',
        response.candidates[0].content.parts[0]
    ],
    config=types.GenerateContentConfig(
        response_modalities=['Image']
    )
)
```

### Negative Prompts (Indirect)
Instead of negative prompts, be explicit about what you want:
- Instead of "no blur", use "sharp focus, crisp details"
- Instead of "no people", use "empty landscape"

### Consistent Style Across Images
Use detailed style descriptors:
```python
style = "cyberpunk aesthetic, neon lighting, dark atmosphere, rain-slicked streets"
prompt1 = f"A futuristic motorcycle, {style}"
prompt2 = f"A street vendor stall, {style}"
```

## Safety Settings

### Configure Safety Filters
```python
from google.genai import types

config = types.GenerateContentConfig(
    response_modalities=['Image'],
    safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        )
    ]
)
```

### Available Categories
- `HARM_CATEGORY_HARASSMENT`
- `HARM_CATEGORY_HATE_SPEECH`
- `HARM_CATEGORY_SEXUALLY_EXPLICIT`
- `HARM_CATEGORY_DANGEROUS_CONTENT`

### Thresholds
- `BLOCK_NONE`
- `BLOCK_LOW_AND_ABOVE`
- `BLOCK_MEDIUM_AND_ABOVE`
- `BLOCK_ONLY_HIGH`

## Common Use Cases

### 1. Marketing Assets
```python
prompt = """Product photography of a luxury watch:
- Clean white background
- Dramatic lighting from top-left
- Watch at 10:10 position
- Sharp focus on dial details
- High-end magazine style
"""
```

### 2. Concept Art
```python
prompt = """Concept art of a futuristic city:
- Flying vehicles between towering buildings
- Holographic advertisements
- Sunset lighting with warm orange tones
- Detailed architecture with glass and steel
- Digital painting style
"""
```

### 3. Social Media Graphics
```python
prompt = """Instagram post design:
- Minimalist gradient background (blue to purple)
- Bold text "NEW ARRIVAL"
- Modern sans-serif typography
- Centered composition
- Square format
"""
```

### 4. Illustration
```python
prompt = """Children's book illustration:
- Friendly cartoon fox in a forest
- Warm autumn colors
- Soft watercolor style
- Cheerful expression
- Whimsical environment
"""
```

### 5. UI/UX Mockups
```python
prompt = """Mobile app login screen mockup:
- Dark mode interface
- Glassmorphism card design
- Social login buttons
- Gradient accent colors
- Modern iOS style
"""
```

## Best Practices

### Prompt Quality
1. Be specific and detailed
2. Use consistent terminology
3. Reference real-world examples when helpful
4. Include technical specifications

### File Management
1. Save outputs with descriptive names
2. Organize by project/category
3. Keep original prompts with generated images

### Cost Optimization
1. Use Gemini 2.5 Flash for drafts, Gemini 3 for finals
2. Iterate on text prompt before generating
3. Use appropriate aspect ratios to minimize unused space

## Error Handling

### Safety Filter Blocking
If generation is blocked, try:
1. Rewording the prompt
2. Removing potentially sensitive terms
3. Being more abstract in descriptions

### Token Limit Exceeded
1. Shorten the prompt
2. Reduce number of input images
3. Lower resolution requirements

## Limitations
- Maximum 3 input images for composition
- Text rendering limited to ~25 characters
- Some subjects may trigger safety filters
- Consistency across multiple generations not guaranteed
- Real person likenesses not supported
