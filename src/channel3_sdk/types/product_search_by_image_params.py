# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .locale_config_param import LocaleConfigParam
from .search_filters_param import SearchFiltersParam

__all__ = ["ProductSearchByImageParams"]


class ProductSearchByImageParams(TypedDict, total=False):
    base64_image: Optional[str]
    """Base64 encoded image bytes (no data URI prefix)."""

    config: LocaleConfigParam
    """Optional locale configuration."""

    filters: SearchFiltersParam
    """Optional filters.

    Search will only consider products that match all of the filters.
    """

    image_url: Optional[str]
    """Publicly accessible URL of the image to search with."""

    limit: Optional[int]
    """Optional limit on the number of results. Default is 20, max is 30."""

    page_token: Optional[str]
    """
    Opaque token from a previous image-search response to fetch the next page of
    results.
    """
