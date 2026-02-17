"""
Shared helpers used across all document-type views.
DEPRECATED: This file is kept for backwards compatibility.
Please use the new structure:
- generator.services.ai_service for AI functions
- generator.services.data_loader for JSON data loading
- generator.utils_new.formatters for formatting functions
"""
import logging

logger = logging.getLogger('generator')

# Re-export from new locations for backward compatibility
from ..services.ai_service import get_gemini_model  # noqa: F401
from ..services.data_loader import (  # noqa: F401
    get_office_order_data,
    get_circular_data,
    get_policy_data,
)
from ..utils_new.formatters import (  # noqa: F401
    format_date_ddmmyyyy,
    safe_designation,
)
