# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .availability_status import AvailabilityStatus
from .search_filter_price_param import SearchFilterPriceParam

__all__ = ["SearchFiltersParam"]


class SearchFiltersParam(TypedDict, total=False):
    age: Optional[List[Literal["newborn", "infant", "toddler", "kids", "adult"]]]
    """Filter by age group. Age-agnostic products are treated as adult products."""

    availability: Optional[List[AvailabilityStatus]]
    """If provided, only products with these availability statuses will be returned"""

    brand_ids: Optional[SequenceNotStr[str]]
    """If provided, only products from these brands will be returned"""

    category_ids: Optional[SequenceNotStr[str]]
    """If provided, only products from these categories will be returned"""

    condition: Optional[Literal["new", "refurbished", "used"]]
    """Filter by product condition.

    Incubating: condition data is currently incomplete; products without condition
    data will be included in all condition filter results.
    """

    exclude_product_ids: Optional[SequenceNotStr[str]]
    """If provided, products with these IDs will be excluded from the results"""

    gender: Optional[Literal["male", "female", "unisex"]]

    price: Optional[SearchFilterPriceParam]
    """Price filter. Values are inclusive."""

    website_ids: Optional[SequenceNotStr[str]]
    """If provided, only products from these websites will be returned"""
