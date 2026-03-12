# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .product_brand import ProductBrand
from .product_image import ProductImage
from .product_offer import ProductOffer

__all__ = ["ProductDetail"]


class ProductDetail(BaseModel):
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
