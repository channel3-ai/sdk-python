# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .availability_status import AvailabilityStatus
from .search_filter_price_param import SearchFilterPriceParam

__all__ = ["SearchFiltersParam", "Colors", "ColorsPalette"]


class ColorsPalette(TypedDict, total=False):
    """A single color requirement for the color filter."""

    hex: Required[str]
    """sRGB hex string, e.g. '#a1b2c3'"""

    percentage: Optional[float]
    """Percentage of color, where 1.0 is 100%"""


class Colors(TypedDict, total=False):
    """[Beta] Color filter wrapper.

    Holds the list of required colors today;
    reserved for future filter-level options (e.g. match modes, tolerance overrides).
    """

    palette: Required[Iterable[ColorsPalette]]
    """Colors required in matching products. Treated as an AND condition."""


class SearchFiltersParam(TypedDict, total=False):
    """Search filters for the search API."""

    age: Optional[List[Literal["newborn", "infant", "toddler", "kids", "adult"]]]
    """Filter by age group. Age-agnostic products are treated as adult products."""

    attributes: Optional[Dict[str, SequenceNotStr[str]]]
    """
    If provided, only products whose extracted attributes match these key/value
    constraints will be returned. Keys are attribute handles (e.g. 'color',
    'material') and values are lists of allowed values (OR within a key, AND across
    keys). When a category filter is also supplied, all keys must be valid
    attributes of at least one of the requested categories. See
    `Category.attributes` for the valid keys/values per category.
    """

    availability: Optional[List[AvailabilityStatus]]
    """If provided, only products with these availability statuses will be returned"""

    brand_ids: Optional[SequenceNotStr[str]]
    """If provided, only products from these brands will be returned"""

    category_ids: Optional[SequenceNotStr[str]]
    """If provided, only products from these categories will be returned.

    Accepts category slugs.
    """

    colors: Optional[Colors]
    """[Beta] Color filter wrapper.

    Holds the list of required colors today; reserved for future filter-level
    options (e.g. match modes, tolerance overrides).
    """

    condition: Optional[Literal["new", "refurbished", "used"]]
    """Filter by product condition.

    Incubating: condition data is currently incomplete; products without condition
    data will be included in all condition filter results.
    """

    exclude_brand_ids: Optional[SequenceNotStr[str]]
    """If provided, products from these brands will be excluded from the results"""

    exclude_category_ids: Optional[SequenceNotStr[str]]
    """
    If provided, products in these categories (or their descendants) will be
    excluded from the results. Accepts category slugs.
    """

    exclude_website_ids: Optional[SequenceNotStr[str]]
    """If provided, products from these websites will be excluded from the results.

    Accepts website IDs or domains (e.g. "nike.com").
    """

    gender: Optional[Literal["male", "female"]]

    price: Optional[SearchFilterPriceParam]
    """Price filter for search. Values are inclusive."""

    website_ids: Optional[SequenceNotStr[str]]
    """If provided, only products from these websites will be returned.

    Accepts website IDs or domains (e.g. "nike.com").
    """
