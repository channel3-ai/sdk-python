# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .price import Price
from .variant import Variant
from .._models import BaseModel
from .availability_status import AvailabilityStatus

__all__ = ["ProductRetrieveResponse"]


class ProductRetrieveResponse(BaseModel):
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

    key_features: Optional[List[str]] = None

    materials: Optional[List[str]] = None

    variants: Optional[List[Variant]] = None
