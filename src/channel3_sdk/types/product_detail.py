# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .product_brand import ProductBrand
from .product_image import ProductImage
from .product_offer import ProductOffer
from .category_summary import CategorySummary
from .availability_status import AvailabilityStatus

__all__ = ["ProductDetail", "Variants", "VariantsOption", "VariantsOptionValue", "VariantsSelected"]


class VariantsOptionValue(BaseModel):
    """One value of one variant option (e.g. 'Blue' under 'Color')"""

    exists: bool
    """
    Whether the option value exists on the product, or is a configuration only
    present on another variant of the same product. For example, a shirt that comes
    in multiple colors, but only one color is available in Size XL.
    """

    label: str
    """The display value of the option value (e.g. 'Blue')"""

    available: Optional[AvailabilityStatus] = None
    """The availability status of the option value.

    None when returned on search results, hydrated only on get product detail
    requests.
    """

    product_id: Optional[str] = None
    """The product id that represents this value.

    Variants that point to different products will have this field set, as well as
    thumbnail_url for displaying selector icons.
    """

    thumbnail_url: Optional[str] = None
    """
    For options that reference different products, this is the URL of the thumbnail
    image for the option value. E.g., a shoe that comes in multiple colors will have
    an OptionValue for each color with a thumbnail_url set.
    """


class VariantsOption(BaseModel):
    """One dimension of a product family (e.g. 'Color', 'Size')."""

    name: str
    """The name of the option (e.g. 'Color', 'Size')"""

    values: List[VariantsOptionValue]
    """The values of the option (e.g. ['Blue', 'Red', 'Green'])"""


class VariantsSelected(BaseModel):
    """One effective selection on a product, post server-side relaxation."""

    label: str
    """The display value of the selected option (e.g. 'Blue', 'XL')"""

    name: str
    """The name of the selected option (e.g. 'Color', 'Size')"""


class Variants(BaseModel):
    """Wrapper for variant-interaction state on a Product.

    Holds `options` and `selected`. `options` represent all of the
    configuration options for the product. `selected` represents the
    currently selected option values.
    """

    options: List[VariantsOption]

    selected: List[VariantsSelected]


class ProductDetail(BaseModel):
    """Product with detailed information."""

    id: str

    title: str

    age: Optional[Literal["newborn", "infant", "toddler", "kids", "adult"]] = None
    """Target age group. Age-agnostic products are typically returned as 'adult'."""

    brands: Optional[List[ProductBrand]] = None
    """Ordered list of brands."""

    categories: Optional[List[str]] = None

    category: Optional[CategorySummary] = None
    """Lean category representation used in search hits and list rows."""

    description: Optional[str] = None

    gender: Optional[Literal["male", "female", "unisex"]] = None

    images: Optional[List[ProductImage]] = None

    key_features: Optional[List[str]] = None

    materials: Optional[List[str]] = None

    offers: Optional[List[ProductOffer]] = None
    """All merchant offers for this product in the requested locale."""

    structured_attributes: Optional[Dict[str, List[str]]] = None
    """Structured attributes extracted for this product, keyed by attribute handle
    (e.g.

    'color', 'material'). Values are the canonical allowed values for that handle.
    """

    variants: Optional[Variants] = None
    """Wrapper for variant-interaction state on a Product.

    Holds `options` and `selected`. `options` represent all of the configuration
    options for the product. `selected` represents the currently selected option
    values.
    """
