# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .availability_status import AvailabilityStatus
from .search_filter_price_param import SearchFilterPriceParam

__all__ = [
    "SearchFiltersParam",
    "Colors",
    "ColorsPalette",
    "Dimensions",
    "DimensionsHeight",
    "DimensionsLength",
    "DimensionsWeight",
    "DimensionsWidth",
]


class ColorsPalette(TypedDict, total=False):
    """A single color requirement for the color filter."""

    hex: Required[str]
    """sRGB hex string, e.g. '#a1b2c3'"""

    percentage: Optional[float]
    """Percentage of color, where 1.0 is 100%"""


class Colors(TypedDict, total=False):
    """[Beta] Color filter wrapper. Holds required colors and optional match mode."""

    palette: Required[Iterable[ColorsPalette]]
    """Colors required in matching products. Treated as an AND condition."""

    match: Literal["strict", "standard", "loose"]
    """How tightly colors must match: 'strict', 'standard', or 'loose'."""


class DimensionsHeight(TypedDict, total=False):
    unit: Required[Literal["mm", "cm", "m", "in", "ft"]]
    """Unit that min/max are expressed in"""

    max: Optional[float]
    """Maximum value, in `unit`. Inclusive."""

    min: Optional[float]
    """Minimum value, in `unit`. Inclusive."""


class DimensionsLength(TypedDict, total=False):
    unit: Required[Literal["mm", "cm", "m", "in", "ft"]]
    """Unit that min/max are expressed in"""

    max: Optional[float]
    """Maximum value, in `unit`. Inclusive."""

    min: Optional[float]
    """Minimum value, in `unit`. Inclusive."""


class DimensionsWeight(TypedDict, total=False):
    unit: Required[Literal["mg", "g", "kg", "oz", "lb"]]
    """Unit that min/max are expressed in"""

    max: Optional[float]
    """Maximum value, in `unit`. Inclusive."""

    min: Optional[float]
    """Minimum value, in `unit`. Inclusive."""


class DimensionsWidth(TypedDict, total=False):
    unit: Required[Literal["mm", "cm", "m", "in", "ft"]]
    """Unit that min/max are expressed in"""

    max: Optional[float]
    """Maximum value, in `unit`. Inclusive."""

    min: Optional[float]
    """Minimum value, in `unit`. Inclusive."""


class Dimensions(TypedDict, total=False):
    """Physical-dimension range filters, matched against the same offer.

    Matching products have at least one offer satisfying every provided
    range (alongside any locale/price/availability filters). Values are
    compared with a small relative tolerance. An offer with no dimension data
    for a filtered field does not match; note that when a single merchant on a
    product reports a dimension it is shared across that product's offers, so a
    matching offer may not itself surface that dimension in the response.
    """

    height: Optional[DimensionsHeight]

    length: Optional[DimensionsLength]

    weight: Optional[DimensionsWeight]

    width: Optional[DimensionsWidth]


class SearchFiltersParam(TypedDict, total=False):
    """Search filters for the search API."""

    age: Optional[List[Literal["newborn", "infant", "toddler", "kids", "adult"]]]
    """Filter by age group. Age-agnostic products are treated as adult products."""

    attributes: Optional[Dict[str, SequenceNotStr[str]]]
    """If provided, only products matching these key/value constraints will be
    returned.

    Keys are attribute handles (e.g. 'color', 'material') and values are lists of
    allowed values (OR within a key, AND across keys). When a category filter is
    also supplied, all keys must be valid attributes of at least one of the
    requested categories. See `Category.attributes` for the valid keys and values
    per category.
    """

    availability: List[AvailabilityStatus]
    """Offer availability statuses to match (OR).

    Defaults to ['InStock']. An offer with no availability data counts as 'InStock'.
    Pass every value to disable availability filtering.
    """

    brand_ids: Optional[SequenceNotStr[str]]
    """If provided, only products from these brands will be returned"""

    category_ids: Optional[SequenceNotStr[str]]
    """If provided, only products from these categories will be returned.

    Accepts category slugs.
    """

    colors: Optional[Colors]
    """[Beta] Color filter wrapper. Holds required colors and optional match mode."""

    conditions: List[Literal["new", "used"]]
    """Offer conditions to match (OR).

    Defaults to ['new'], which also matches offers whose condition is unknown. Pass
    every value to disable condition filtering.
    """

    dimensions: Optional[Dimensions]
    """Physical-dimension range filters, matched against the same offer.

    Matching products have at least one offer satisfying every provided range
    (alongside any locale/price/availability filters). Values are compared with a
    small relative tolerance. An offer with no dimension data for a filtered field
    does not match; note that when a single merchant on a product reports a
    dimension it is shared across that product's offers, so a matching offer may not
    itself surface that dimension in the response.
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
    """Product gender.

    'unisex' is deprecated: coerced to None on input, never emitted.
    """

    price: Optional[SearchFilterPriceParam]
    """Price filter for search. Values are inclusive."""

    sale: Optional[Literal["on_sale"]]
    """
    If 'on_sale', only products with at least one on-sale offer (priced below its
    compare-at price) for the requested locale are returned. If omitted, no filter.
    """

    website_ids: Optional[SequenceNotStr[str]]
    """If provided, only products from these websites will be returned.

    Accepts website IDs or domains (e.g. "nike.com").
    """
