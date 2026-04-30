# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["PriceHistoryPoint"]


class PriceHistoryPoint(BaseModel):
    currency: str

    price: float

    timestamp: datetime
