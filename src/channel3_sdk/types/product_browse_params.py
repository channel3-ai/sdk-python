# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .search_filters_param import SearchFiltersParam

__all__ = ["ProductBrowseParams"]


class ProductBrowseParams(TypedDict, total=False):
    filters: SearchFiltersParam
    """Filters to browse by.

    At least one of `brand_ids`, `category_ids`, or `website_ids` must be provided.
    """

    limit: Optional[int]
    """Optional limit on the number of results. Default is 20, max is 30."""

    page_token: Optional[str]
    """Opaque token from a previous browse response to fetch the next page."""
