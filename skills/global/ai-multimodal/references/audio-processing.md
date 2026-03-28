# Audio Processing Reference

Complete guide for audio understanding, transcription, and text-to-speech using Gemini API.

## Audio Understanding

### Supported Formats
- WAV, MP3, AAC, FLAC, OGG Vorbis, AIFF
- Maximum 9.5 hours per request
- Auto-downsampled to 16 Kbps mono

### Specifications
- Token rate: 32 tokens/second
- 1 minute = 1,920 tokens
- No silence detection (all audio tokenized)

## Transcription

### Basic Transcription
```python
from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

# Upload audio file
audio_file = client.files.upload(file='audio.mp3')

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Transcribe this audio accurately',
        audio_file
    ]
)

print(response.text)
```

### With Timestamps
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Transcribe this audio with timestamps in [MM:SS] format',
        audio_file
    ]
)
```

### Multi-Speaker Identification
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        '''Transcribe this conversation. Identify different speakers 
        and label them as Speaker 1, Speaker 2, etc. Include timestamps.''',
        audio_file
    ]
)
```

### Segment-Specific Transcription
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Transcribe only the segment from 2:00 to 5:00',
        audio_file
    ]
)
```

## Audio Analysis

### Summarization
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Summarize the key points discussed in this audio',
        audio_file
    ]
)
```

### Non-Speech Audio Analysis
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Analyze this audio and describe all sounds, instruments, and music elements',
        audio_file
    ]
)
```

### Timestamp-Based Analysis
```python
response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'What is happening at timestamp 3:45?',
        audio_file
    ]
)
```

## Input Methods

### File Upload (>20MB or Reuse)
```python
# Upload once, use multiple times
audio_file = client.files.upload(file='large_audio.mp3')

# Use in multiple requests
response1 = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=['Transcribe this', audio_file]
)

response2 = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=['Summarize this', audio_file]
)
```

### Inline Data (<20MB)
```python
with open('short_audio.mp3', 'rb') as f:
    audio_bytes = f.read()

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents=[
        'Transcribe this audio',
        types.Part.from_bytes(data=audio_bytes, mime_type='audio/mp3')
    ]
)
```

## Speech Generation (TTS)

### Available Models
- **Gemini 2.5 Flash TTS**: $10/1M tokens
- **Gemini 2.5 Pro TTS**: $20/1M tokens

### Basic TTS
```python
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Say: Hello, welcome to our service!',
    config=types.GenerateContentConfig(
        response_modalities=['Audio']
    )
)

# Save audio
for part in response.candidates[0].content.parts:
    if part.inline_data:
        with open('output.mp3', 'wb') as f:
            f.write(part.inline_data.data)
```

### Controllable Voice Style
```python
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        'Say the following with a warm, friendly tone: Hi there! How can I help you today?',
    ],
    config=types.GenerateContentConfig(
        response_modalities=['Audio'],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name='Aoede'
                )
            )
        )
    )
)
```

### Voice Control Parameters
- Speed: Adjust speaking rate
- Pitch: Higher or lower voice
- Emotion: Cheerful, serious, calm

## Best Practices

### File Management
1. Use File API for files >20MB
2. Files auto-delete after 48 hours
3. Upload once, use multiple times

### Prompt Engineering
1. Be specific about output format
2. Request timestamps when needed
3. Specify language expectations

### Cost Optimization
1. Use inline data for small files
2. Process specific segments instead of full audio
3. Batch multiple queries on same upload

### Error Handling
```python
try:
    response = client.models.generate_content(...)
except Exception as e:
    if '429' in str(e):
        # Rate limit - wait and retry
        time.sleep(60)
    elif '400' in str(e):
        # Invalid format - check file
        pass
```

## Common Use Cases

### 1. Meeting Transcription
```python
prompt = '''Create a structured meeting transcript with:
- Attendee identification (Speaker 1, Speaker 2...)
- Timestamps every 30 seconds
- Action items highlighted
- Key decisions summarized at the end'''
```

### 2. Podcast Summary
```python
prompt = '''Analyze this podcast episode and provide:
- Episode summary (2-3 paragraphs)
- Key topics discussed with timestamps
- Notable quotes
- Main takeaways'''
```

### 3. Interview Analysis
```python
prompt = '''Analyze this interview:
- Identify interviewer and interviewee
- Extract main questions asked
- Summarize answers
- Note any interesting insights'''
```

### 4. Content Verification
```python
prompt = '''Listen to this audio and verify:
- Are there any factual inaccuracies?
- Are claims properly supported?
- What sources are mentioned?'''
```

### 5. Multilingual Transcription
```python
prompt = '''Transcribe this audio. 
The audio may contain multiple languages.
Identify the language for each segment.
Translate non-English segments to English.'''
```

## Token Costs
- Audio: 32 tokens/second
- 1 minute = 1,920 tokens
- 1 hour = 115,200 tokens

## Limitations
- Maximum 9.5 hours per request
- No real-time streaming
- Auto-downsampled quality
- Some accents may have lower accuracy
