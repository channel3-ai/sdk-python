# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .price import Price
from .._models import BaseModel
from .product_brand import ProductBrand
from .product_offer import ProductOffer

__all__ = ["EnrichEnrichURLResponse", "Image", "Variant"]


class Image(BaseModel):
    """v0 product image with deprecated photo_quality field."""

    url: str

    alt_text: Optional[str] = None

    is_main_image: Optional[bool] = None

    photo_quality: Optional[Literal["professional", "ugc", "poor"]] = None
    """Photo quality classification for API responses."""

    shot_type: Optional[
        Literal[
            "hero",
            "lifestyle",
            "on_model",
            "detail",
            "scale_reference",
            "angle_view",
            "flat_lay",
            "in_use",
            "packaging",
            "size_chart",
            "product_information",
            "merchant_information",
        ]
    ] = None
    """Product image type classification for API responses."""


class Variant(BaseModel):
    image_url: str

    product_id: str

    title: str


class EnrichEnrichURLResponse(BaseModel):
    """v0 product detail with deprecated fields."""

    id: str

    availability: Literal["InStock", "OutOfStock"]
    """Deprecated, use offers field"""

    price: Price
    """Deprecated, use offers field"""

    title: str

    url: str
    """Deprecated, use offers field"""

    brand_id: Optional[str] = None

    brand_name: Optional[str] = None

    brands: Optional[List[ProductBrand]] = None
    """Ordered list of brands."""

    categories: Optional[List[str]] = None

    description: Optional[str] = None

    gender: Optional[Literal["male", "female", "unisex"]] = None

    image_urls: Optional[List[str]] = None
    """List of image URLs (deprecated, use images field)"""

    images: Optional[List[Image]] = None

    key_features: Optional[List[str]] = None

    materials: Optional[List[str]] = None

    offers: Optional[List[ProductOffer]] = None
    """All merchant offers for this product in the requested locale."""

    variants: Optional[List[Variant]] = None
    """Legacy variant list, always empty. Use v1 API for variant dimensions."""
