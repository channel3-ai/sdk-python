# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .availability_status import AvailabilityStatus

__all__ = ["SearchPerformParams", "Config", "Filters", "FiltersPrice"]


class SearchPerformParams(TypedDict, total=False):
    base64_image: Optional[str]
    """Base64 encoded image"""

    config: Config
    """Optional configuration"""

    context: Optional[str]
    """Optional customer information to personalize search results"""

    filters: Filters
    """Optional filters.

    Search will only consider products that match all of the filters.
    """

    image_url: Optional[str]
    """Image URL"""

    limit: Optional[int]
    """Optional limit on the number of results"""

    query: Optional[str]
    """Search query"""


class Config(TypedDict, total=False):
    enrich_query: bool
    """
    If True, search will use AI to enrich the query, for example pulling the gender,
    brand, and price range from the query.
    """

    monetizable_only: bool
    """If True, search will only consider products that offer commission."""

    redirect_mode: Optional[Literal["brand", "price", "commission"]]
    """
    "price" redirects to the product page with the lowest price "commission"
    redirects to the product page with the highest commission rate "brand" redirects
    to the brand's product page
    """


class FiltersPrice(TypedDict, total=False):
    max_price: Optional[float]
    """Maximum price, in dollars and cents"""

    min_price: Optional[float]
    """Minimum price, in dollars and cents"""


class Filters(TypedDict, total=False):
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

    price: Optional[FiltersPrice]
    """Price filter. Values are inclusive."""

    website_ids: Optional[SequenceNotStr[str]]
    """If provided, only products from these websites will be returned"""
