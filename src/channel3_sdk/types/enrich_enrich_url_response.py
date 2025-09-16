# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .price import Price
from .._models import BaseModel

__all__ = ["EnrichEnrichURLResponse"]


class EnrichEnrichURLResponse(BaseModel):
    main_image_url: str

    other_image_urls: List[str]

    price: Price

    title: str

    url: str
