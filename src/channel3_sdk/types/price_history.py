# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PriceHistory", "History", "Statistics"]


class History(BaseModel):
    currency: str

    price: float

    timestamp: datetime


class Statistics(BaseModel):
    currency: str

    current_price: float

    current_status: Literal["low", "typical", "high"]

    max_price: float

    mean: float

    min_price: float

    std_dev: float


class PriceHistory(BaseModel):
    canonical_product_id: str

    history: Optional[List[History]] = None

    product_title: Optional[str] = None

    statistics: Optional[Statistics] = None
