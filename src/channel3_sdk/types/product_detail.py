# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .price import Price
from .variant import Variant
from .._models import BaseModel
from .availability_status import AvailabilityStatus

__all__ = ["ProductDetail", "Image"]


class Image(BaseModel):
    """Product image with metadata"""

    url: str

    alt_text: Optional[str] = None

    is_main_image: Optional[bool] = None

    photo_quality: Optional[Literal["professional", "ugc", "poor"]] = None
    """
    Photo quality classification for API responses. Note: This enum is decoupled
    from internal ImageIntelligence types as they may diverge.
    """

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
            "color_swatch",
            "product_information",
            "merchant_information",
        ]
    ] = None
    """
    Product image type classification for API responses. Note: This enum is
    decoupled from internal ImageIntelligence types as they may diverge.
    """


class ProductDetail(BaseModel):
    """A product with detailed information"""

    id: str

    availability: AvailabilityStatus

    price: Price

    title: str

    url: str

    brand_id: Optional[str] = None

    brand_name: Optional[str] = None

    categories: Optional[List[str]] = None

    description: Optional[str] = None

    gender: Optional[Literal["male", "female", "unisex"]] = None

    image_urls: Optional[List[str]] = None
    """List of image URLs (deprecated, use images field)"""

    images: Optional[List[Image]] = None

    key_features: Optional[List[str]] = None

    materials: Optional[List[str]] = None

    variants: Optional[List[Variant]] = None
