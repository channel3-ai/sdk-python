# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .search_config_param import SearchConfigParam
from .search_filters_param import SearchFiltersParam

__all__ = ["SearchPerformParams"]


class SearchPerformParams(TypedDict, total=False):
    base64_image: Optional[str]
    """Base64 encoded image"""

    config: SearchConfigParam
    """Optional configuration"""

    context: Optional[str]
    """Optional customer information to personalize search results"""

    filters: SearchFiltersParam
    """Optional filters.

    Search will only consider products that match all of the filters.
    """

    image_url: Optional[str]
    """Image URL"""

    limit: Optional[int]
    """Optional limit on the number of results. Default is 20, max is 30."""

    query: Optional[str]
    """Search query"""
