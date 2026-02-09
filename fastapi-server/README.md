# Lumina AI Course Engine

AI-powered course generation system for the Lumina education platform.

## Features

- AI-powered course generation from topics
- Multi-language support (English + Indian languages)
- Quiz generation and AI grading
- Chapter-specific AI chat
- Document-based RAG

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Set environment variables in `.env`:
```env
GOOGLE_CLOUD_API=your_google_cloud_api_key
GROQ_API_KEY=your_groq_api_key
MONGODB_URI=your_mongodb_connection_string
CHROMA_API_KEY=your_chroma_api_key
CHROMA_HOST=your_chroma_host
```

3. Run the server:
```bash
uv run uvicorn src.main:app --reload --port 8000
```

## API Endpoints

- `POST /api/courses` - Create a new course
- `GET /api/courses` - List all courses
- `GET /api/courses/{id}` - Get course details
- `GET /api/courses/{id}/chapters` - Get chapters
- `POST /api/chapters/{id}/chat` - Chat with AI about chapter
- `POST /api/chapters/{id}/questions/{q_id}/answer` - Submit quiz answer
