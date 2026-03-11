# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .product_brand import ProductBrand
from .product_offer import ProductOffer

__all__ = ["SearchResponse", "Product", "ProductImage"]


class ProductImage(BaseModel):
    """Product image with metadata."""

    url: str

    alt_text: Optional[str] = None

    is_main_image: Optional[bool] = None

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


class Product(BaseModel):
    """Product with detailed information."""

    id: str

    title: str

    brands: Optional[List[ProductBrand]] = None
    """Ordered list of brands."""

    categories: Optional[List[str]] = None

    description: Optional[str] = None

    gender: Optional[Literal["male", "female", "unisex"]] = None

    images: Optional[List[ProductImage]] = None

    key_features: Optional[List[str]] = None

    materials: Optional[List[str]] = None

    offers: Optional[List[ProductOffer]] = None
    """All merchant offers for this product in the requested locale."""


class SearchResponse(BaseModel):
    """v1 paginated search response."""

    products: List[Product]

    next_page_token: Optional[str] = None
    """Token to fetch the next page. Null when no more results."""
