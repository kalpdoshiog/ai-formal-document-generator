"""
Formatting Utilities for dates, designations, etc.
"""
import logging
from datetime import datetime
from ..data.constants import DESIGNATION_MAP

logger = logging.getLogger('generator')


# ------------------------------------------------------------------
# Date helper
# ------------------------------------------------------------------
def format_date_ddmmyyyy(date_str):
    """Convert YYYY-MM-DD → DD-MM-YYYY; return as-is on failure."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%d-%m-%Y")
    except Exception:
        return date_str


# ------------------------------------------------------------------
# Designation lookup (safe)
# ------------------------------------------------------------------
def safe_designation(key, lang):
    """
    Look up a designation safely.  Returns the translated string or
    the raw key if not found.
    """
    entry = DESIGNATION_MAP.get(key)
    if entry is None:
        logger.warning("Designation key '%s' not found in DESIGNATION_MAP", key)
        return key or ""
    return entry.get(lang, key)

