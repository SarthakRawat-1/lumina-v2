"""
Services module

Re-exports utilities from src.utils for backwards compatibility.
Actual implementations have been moved to src.utils.
"""
# Re-export from utils for backwards compatibility
from src.utils.translation import TranslationService, get_translation_service
from src.utils.llm import LLMService, get_llm_service
from src.utils.vector import VectorService, get_vector_service
from src.utils.tts import TTSService, get_tts_service
from src.utils.pdf import DocumentAIService, get_document_ai_service
from src.utils.video_transcription import VideoTranscriptionService, get_video_intelligence_service
from src.utils.youtube import YouTubeTranscriptService, get_youtube_transcript_service
from src.utils.analytics import AnalyticsService, get_analytics_service

# Actual services (with business logic)
from src.graphs.course import CourseService, get_course_service

__all__ = [
    # Utilities (re-exported for backwards compatibility)
    "TranslationService",
    "get_translation_service",
    "LLMService", 
    "get_llm_service",
    "VectorService",
    "get_vector_service",
    "TTSService",
    "get_tts_service",
    "DocumentAIService",
    "get_document_ai_service",
    "VideoTranscriptionService",
    "get_video_intelligence_service",
    "YouTubeTranscriptService",
    "get_youtube_transcript_service",
    "AnalyticsService",
    "get_analytics_service",
    # Actual services
    "CourseService",
    "get_course_service",
]
