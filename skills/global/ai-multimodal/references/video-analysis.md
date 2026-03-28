# Video Analysis Reference

Comprehensive guide for video understanding, scene analysis, and temporal queries using Gemini API.

## Core Capabilities
- Scene detection and summarization
- Video Q&A with temporal understanding
- Transcription with visual descriptions
- YouTube URL support (public videos)
- Long video processing (up to 6 hours)
- Frame-level analysis

## Supported Formats
- MP4, MPEG, MOV, AVI, FLV, MPG, WebM, WMV, 3GPP
- Maximum 6 hours (low-res) or 2 hours (default)
- YouTube URLs (public only)

## Model Selection

### Gemini 3 Series (Preview)
- **gemini-3-pro-preview**: Latest multimodal, enhanced reasoning

### Gemini 2.5 Series (Stable)
- **gemini-2.5-pro**: Highest quality, all features, 1M-2M context
- **gemini-2.5-flash**: Best balance, all features, 1M-2M context

### Gemini 2.0 Series
- **gemini-2.0-flash**: Fast processing, object detection

### Context Windows
- 2M tokens: ~6 hours video (low-res) or ~2 hours (default)
- 1M tokens: ~3 hours video (low-res) or ~1 hour (default)

## Basic Video Analysis

### Local Video
```python
from google import genai
from google.genai import types
import os
import time

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

# Upload video
video_file = client.files.upload(file='video.mp4')

# Wait for processing
while video_file.state.name == 'PROCESSING':
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Describe what happens in this video',
        video_file
    ]
)

print(response.text)
```

### YouTube Video
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        types.Part.from_uri(
            file_uri='https://www.youtube.com/watch?v=VIDEO_ID',
            mime_type='video/*'
        ),
        'Summarize the main points of this video'
    ]
)
```

### Inline Video (<20MB)
```python
with open('short_video.mp4', 'rb') as f:
    video_bytes = f.read()

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'What happens in this video?',
        types.Part.from_bytes(data=video_bytes, mime_type='video/mp4')
    ]
)
```

## Advanced Features

### Video Clipping
```python
# Analyze specific segment
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Describe what happens between 2:00 and 5:00',
        video_file
    ]
)
```

### Custom Frame Rate
```python
# Reduce frame rate for faster processing
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Analyze this video at 1 frame per second',
        video_file
    ]
)
```

### Multiple Videos (2.5+)
```python
video1 = client.files.upload(file='video1.mp4')
video2 = client.files.upload(file='video2.mp4')

# Wait for both to process
# ...

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        'Compare these two videos',
        video1,
        video2
    ]
)
```

## Temporal Understanding

### Timestamp-Based Questions
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'What is happening at 3:45?',
        video_file
    ]
)
```

### Timeline Creation
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        '''Create a timeline of events in this video with timestamps:
        - Format: [MM:SS] - Event description
        - Include all significant moments''',
        video_file
    ]
)
```

### Scene Detection
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        '''Identify all distinct scenes in this video.
        For each scene provide:
        - Start timestamp
        - End timestamp
        - Scene description
        - Key elements visible''',
        video_file
    ]
)
```

## Transcription

### Basic Transcription
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Transcribe all spoken dialogue',
        video_file
    ]
)
```

### With Visual Descriptions
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        '''Create a complete transcript that includes:
        - Spoken dialogue with speaker identification
        - Visual descriptions in [brackets]
        - Timestamps every 30 seconds''',
        video_file
    ]
)
```

### Speaker Identification
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        '''Transcribe with speaker labels.
        Identify each unique speaker and label consistently as:
        - Speaker 1, Speaker 2, etc.
        - Or by name if mentioned''',
        video_file
    ]
)
```

## Common Use Cases

### 1. Video Summarization
```python
prompt = '''Provide a comprehensive summary:
- Overview (2-3 sentences)
- Key points with timestamps
- Main conclusions or takeaways'''
```

### 2. Educational Content
```python
prompt = '''Analyze this educational video:
- Main topics covered
- Key concepts explained
- Learning objectives
- Suggested follow-up topics'''
```

### 3. Action Detection
```python
prompt = '''Identify all actions performed in this video:
- List each action with timestamp
- Describe the subject performing it
- Note any tools or objects involved'''
```

### 4. Content Moderation
```python
prompt = '''Review this video for content issues:
- Any inappropriate content?
- Violence or harmful imagery?
- Policy violations?
- Provide timestamps for flagged content'''
```

### 5. Interview Analysis
```python
prompt = '''Analyze this interview:
- Identify interviewer and interviewee
- List questions asked
- Summarize key answers
- Note body language observations'''
```

### 6. Sports Analysis
```python
prompt = '''Analyze this sports clip:
- Identify the sport and teams/players
- Describe key plays with timestamps
- Analyze technique or strategy
- Highlight notable moments'''
```

## YouTube Specific Features

### Public Video Requirements
- Video must be publicly accessible
- No age restrictions
- No geo-restrictions for your region

### Usage Example
```python
youtube_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        types.Part.from_uri(
            file_uri=youtube_url,
            mime_type='video/*'
        ),
        'Summarize this video'
    ]
)
```

### Rate Limits
- Free tier: 8 hours/day
- Paid tier: No length limits

## Token Calculation

| Resolution | Tokens/second | 1 min | 1 hour |
|-----------|---------------|-------|--------|
| Default | ~300 | 18,000 | 1,080,000 |
| Low-res | ~100 | 6,000 | 360,000 |

## Best Practices

### File Management
1. Upload videos using File API for >20MB
2. Files auto-delete after 48 hours
3. Reuse uploaded files for multiple queries

### Optimization Strategies
1. Use low-res mode for long videos
2. Process specific time segments
3. Reduce frame rate for static content
4. Split very long videos into chunks

### Prompt Engineering
1. Be specific about what to look for
2. Request timestamps explicitly
3. Define output format clearly
4. Limit scope when possible

### Error Handling
```python
# Wait for processing to complete
max_wait = 300  # 5 minutes
elapsed = 0
while video_file.state.name == 'PROCESSING' and elapsed < max_wait:
    time.sleep(5)
    elapsed += 5
    video_file = client.files.get(name=video_file.name)

if video_file.state.name == 'FAILED':
    raise ValueError("Video processing failed")
```

## Cost Optimization
1. Use `gemini-2.5-flash` for most tasks
2. Use low-res mode when visual detail isn't critical
3. Query specific segments instead of full video
4. Batch questions in single requests

## Limitations
- Maximum 6 hours at low-res, 2 hours at default
- Processing time proportional to length
- Some dynamic content may be missed at low FPS
- Private YouTube videos not supported
- Real-time streaming not available
