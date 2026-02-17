"""
Data Loader Service for JSON configuration files.
"""
import json
import os
import logging
from functools import lru_cache
from django.conf import settings

logger = logging.getLogger('generator')


# ------------------------------------------------------------------
# Lazy-loaded JSON data
# ------------------------------------------------------------------
@lru_cache(maxsize=1)
def get_office_order_data():
    """Load office order configuration data."""
    path = os.path.join(settings.BASE_DIR, "config", "office_order.json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("office_order.json not found at %s", path)
        return {}


@lru_cache(maxsize=1)
def get_circular_data():
    """Load circular configuration data."""
    path = os.path.join(settings.BASE_DIR, "config", "circular.json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("circular.json not found at %s", path)
        return {}


@lru_cache(maxsize=1)
def get_policy_data():
    """Load policy configuration data."""
    path = os.path.join(settings.BASE_DIR, "config", "policy.json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("policy.json not found at %s", path)
        return {}


@lru_cache(maxsize=1)
def get_advertisement_data():
    """Load advertisement configuration data."""
    path = os.path.join(settings.BASE_DIR, "config", "advertisement.json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("advertisement.json not found at %s", path)
        return {}


@lru_cache(maxsize=1)
def get_purchase_order_data():
    """Load purchase order configuration data."""
    path = os.path.join(settings.BASE_DIR, "config", "purschase_order.json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("purschase_order.json not found at %s", path)
        return {}

