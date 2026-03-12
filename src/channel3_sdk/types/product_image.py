# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProductImage"]


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
