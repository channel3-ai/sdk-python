# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .locale_config_param import LocaleConfigParam
from .search_filters_param import SearchFiltersParam

__all__ = ["ProductFindSimilarParams"]


class ProductFindSimilarParams(TypedDict, total=False):
    product_id: Required[str]
    """Canonical product ID to find similar products for."""

    config: LocaleConfigParam
    """Optional locale configuration."""

    filters: SearchFiltersParam
    """Optional filters.

    Search will only consider products that match all of the filters.
    """

    limit: Optional[int]
    """Optional limit on the number of results. Default is 20, max is 30."""

    page_token: Optional[str]
    """
    Opaque token from a previous similar response to fetch the next page of results.
    """
