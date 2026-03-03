# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .price import Price
from .variant import Variant
from .._models import BaseModel
from .product_brand import ProductBrand
from .product_image import ProductImage
from .product_offer import ProductOffer

__all__ = ["Product"]


class Product(BaseModel):
    """A search result that includes product details and a relevance score."""

    id: str

    availability: Literal["InStock", "OutOfStock"]
    """Deprecated, use offers field"""

    image_url: str
    """Main product image (deprecated, use images field)"""

    price: Price
    """Deprecated, use offers field"""

    score: int

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

    images: Optional[List[ProductImage]] = None

    key_features: Optional[List[str]] = None

    materials: Optional[List[str]] = None

    offers: Optional[List[ProductOffer]] = None
    """All merchant offers for this product in the requested locale."""

    variants: Optional[List[Variant]] = None
