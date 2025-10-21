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
    """Optional filters"""

    image_url: Optional[str]
    """Image URL"""

    limit: Optional[int]
    """Optional limit on the number of results"""

    query: Optional[str]
    """Search query"""


class Config(TypedDict, total=False):
    enrich_query: bool

    redirect_mode: Optional[Literal["brand", "price", "commission"]]
    """Mode for redirecting to a product page"""

    semantic_search: bool


class FiltersPrice(TypedDict, total=False):
    max_price: Optional[float]
    """Maximum price, in dollars and cents"""

    min_price: Optional[float]
    """Minimum price, in dollars and cents"""


class Filters(TypedDict, total=False):
    availability: Optional[List[AvailabilityStatus]]
    """List of availability statuses"""

    brand_ids: Optional[SequenceNotStr[str]]
    """List of brand IDs"""

    exclude_product_ids: Optional[SequenceNotStr[str]]
    """List of product IDs to exclude"""

    gender: Optional[Literal["male", "female", "unisex"]]

    price: Optional[FiltersPrice]
    """Price filter. Values are inclusive."""
