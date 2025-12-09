# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SearchFilterPriceParam"]


class SearchFilterPriceParam(TypedDict, total=False):
    """Price filter. Values are inclusive."""

    max_price: Optional[float]
    """Maximum price, in dollars and cents"""

    min_price: Optional[float]
    """Minimum price, in dollars and cents"""
