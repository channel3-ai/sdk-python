# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .price import Price
from .variant import Variant
from .._models import BaseModel
from .availability_status import AvailabilityStatus

__all__ = ["SearchPerformResponse", "SearchPerformResponseItem"]


class SearchPerformResponseItem(BaseModel):
    id: str

    availability: AvailabilityStatus

    brand_name: str

    image_url: str

    price: Price

    score: int

    title: str

    url: str

    description: Optional[str] = None

    variants: Optional[List[Variant]] = None


SearchPerformResponse: TypeAlias = List[SearchPerformResponseItem]
