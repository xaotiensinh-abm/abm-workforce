# Vision Understanding Reference

Comprehensive guide for image analysis, object detection, OCR, and visual Q&A using Gemini API.

## Core Capabilities
- Image captioning and description
- Object detection with bounding boxes (2.0+)
- Pixel-level segmentation (2.5+)
- Visual question answering
- Multi-image comparison (up to 3,600 images)
- OCR and text extraction

## Supported Formats
- PNG, JPEG, WEBP, HEIC, HEIF
- Maximum 3,600 images per request
- Resolution: ≤384px = 258 tokens, larger = tiled

## Model Selection

### Gemini 3 Series (Preview)
- **gemini-3-pro-preview**: Latest multimodal, enhanced reasoning

### Gemini 2.5 Series (Stable)
- **gemini-2.5-pro**: All features, highest quality
- **gemini-2.5-flash**: Best balance, all features
- **gemini-2.5-flash-lite**: Lightweight, segmentation support

### Gemini 2.0 Series
- **gemini-2.0-flash**: Fast processing, object detection

### Feature Requirements
- **Segmentation**: Requires 2.5+ models
- **Object Detection**: Requires 2.0+ models

## Basic Image Analysis

### Image Captioning
```python
from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

# Inline image
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Describe this image in detail',
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')
    ]
)

print(response.text)
```

### Image Classification
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Classify this image into one of these categories: nature, urban, portrait, product, food, art',
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')
    ]
)
```

### Visual Question Answering
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'How many people are in this image and what are they doing?',
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')
    ]
)
```

## Advanced Features

### Object Detection (2.0+)
```python
response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[
        '''Detect all objects in this image.
        For each object provide:
        - Object name
        - Bounding box coordinates [x1, y1, x2, y2]
        - Confidence score''',
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')
    ]
)
```

### Segmentation (2.5+)
```python
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        '''Segment this image into distinct regions.
        For each segment provide:
        - Region description
        - Approximate area percentage
        - Color characteristics''',
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')
    ]
)
```

### Multi-Image Comparison
```python
with open('image1.jpg', 'rb') as f:
    img1_bytes = f.read()
with open('image2.jpg', 'rb') as f:
    img2_bytes = f.read()

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Compare these two images and describe the differences',
        types.Part.from_bytes(data=img1_bytes, mime_type='image/jpeg'),
        types.Part.from_bytes(data=img2_bytes, mime_type='image/jpeg')
    ]
)
```

### OCR and Text Extraction
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Extract all text from this image, preserving layout structure',
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')
    ]
)
```

## Input Methods

### Inline Data (<20MB)
```python
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Analyze this image',
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')
    ]
)
```

### PIL Image
```python
from PIL import Image as PILImage

img = PILImage.open('image.jpg')

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Describe this image',
        img
    ]
)
```

### File API (>20MB or Reuse)
```python
# Upload once, use multiple times
image_file = client.files.upload(file='large_image.jpg')

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Analyze this image',
        image_file
    ]
)
```

### URL (Public Images)
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        types.Part.from_uri(
            file_uri='https://example.com/image.jpg',
            mime_type='image/jpeg'
        ),
        'Describe this image'
    ]
)
```

## Token Calculation

| Image Size | Tokens |
|-----------|--------|
| ≤384px | 258 |
| ~512px | 516 |
| ~768px | 774 |
| ≥1024px | 1,548 (tiled) |

## Structured Output

### JSON Schema Output
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        '''Analyze this product image and return JSON:
        {
            "product_name": "",
            "brand": "",
            "colors": [],
            "material": "",
            "condition": "",
            "estimated_price_range": ""
        }''',
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')
    ],
    config=types.GenerateContentConfig(
        response_mime_type='application/json'
    )
)

import json
data = json.loads(response.text)
```

## Multi-Image Analysis

### Batch Processing
```python
images = []
for img_path in ['img1.jpg', 'img2.jpg', 'img3.jpg']:
    with open(img_path, 'rb') as f:
        images.append(types.Part.from_bytes(
            data=f.read(), 
            mime_type='image/jpeg'
        ))

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Analyze each image and provide a summary',
        *images
    ]
)
```

### Image Comparison
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        '''Compare these images and identify:
        - Similarities
        - Differences
        - Which is better quality and why''',
        types.Part.from_bytes(data=img1, mime_type='image/jpeg'),
        types.Part.from_bytes(data=img2, mime_type='image/jpeg')
    ]
)
```

### Visual Search
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Find the same product in these catalog images',
        reference_image,
        catalog_image_1,
        catalog_image_2,
        catalog_image_3
    ]
)
```

## Best Practices

### Image Quality
1. Use clear, well-lit images
2. Avoid excessive compression
3. Crop to relevant content
4. Maintain reasonable resolution

### Prompt Engineering
1. Be specific about what to analyze
2. Request structured output when needed
3. Provide context for ambiguous images
4. Use examples for complex tasks

### File Management
1. Use inline data for small images
2. Upload large images to File API
3. Reuse uploaded files for multiple queries
4. Clean up after batch processing

### Cost Optimization
1. Resize images appropriately
2. Use batch requests for multiple images
3. Select appropriate model for task complexity
4. Cache results for repeated analysis

## Common Use Cases

### 1. Product Analysis
```python
prompt = '''Analyze this product image:
- Product type and category
- Brand identification
- Color and material
- Condition assessment
- Key features visible'''
```

### 2. Screenshot Analysis
```python
prompt = '''Analyze this screenshot:
- Application/website shown
- Main content visible
- UI elements present
- Any errors or issues
- Text content extraction'''
```

### 3. Medical Imaging (Informational Only)
```python
prompt = '''Describe what you observe in this medical image.
Note: This is for informational purposes only,
not for medical diagnosis.'''
```

### 4. Chart/Graph Reading
```python
prompt = '''Extract data from this chart:
- Chart type
- X and Y axis labels
- Data points or trends
- Key findings
- Return as structured data'''
```

### 5. Scene Understanding
```python
prompt = '''Describe this scene:
- Location type (indoor/outdoor)
- Time of day/lighting
- People and their activities
- Objects and their arrangement
- Mood or atmosphere'''
```

## Error Handling
```python
try:
    response = client.models.generate_content(...)
except Exception as e:
    if '400' in str(e):
        # Invalid image format
        print("Image format not supported")
    elif '413' in str(e):
        # Image too large
        print("Image exceeds size limit")
```

## Limitations
- Maximum 3,600 images per request
- Some image types may have reduced accuracy
- Handwriting recognition varies by clarity
- Small text may require higher resolution
- Real person identification not supported
