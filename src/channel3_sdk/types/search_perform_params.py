# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .search_config_param import SearchConfigParam
from .search_filters_param import SearchFiltersParam

__all__ = ["SearchPerformParams"]


class SearchPerformParams(TypedDict, total=False):
    base64_image: Optional[str]
    """Base64 encoded image.

    At least one of `query`, `image_url`, or `base64_image` must be provided.
    """

    config: SearchConfigParam
    """Optional configuration"""

    filters: SearchFiltersParam
    """Optional filters.

    Search will only consider products that match all of the filters.
    """

    image_url: Optional[str]
    """Image URL.

    At least one of `query`, `image_url`, or `base64_image` must be provided.
    """

    limit: Optional[int]
    """Optional limit on the number of results. Default is 20, max is 30."""

    page_token: Optional[str]
    """Opaque token from a previous search response to fetch the next page of results."""

    query: Optional[str]
    """Search query.

    At least one of `query`, `image_url`, or `base64_image` must be provided.
    """
