"""
AI Generation Service using Google Gemini.
"""
import logging
from django.conf import settings
import google.generativeai as genai

logger = logging.getLogger('generator')

# ------------------------------------------------------------------
# Lazy-loaded Gemini model
# ------------------------------------------------------------------
_gemini_model = None


def get_gemini_model():
    """Return (and lazily initialise) the Gemini generative model."""
    global _gemini_model
    if _gemini_model is None:
        api_key = getattr(settings, 'GEMINI_API_KEY', '')
        if not api_key:
            logger.warning("GEMINI_API_KEY is not set – AI generation will fail.")
        genai.configure(api_key=api_key)
        _gemini_model = genai.GenerativeModel("gemini-2.5-flash-lite")
        logger.info("Gemini model initialised.")
    return _gemini_model

