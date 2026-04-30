# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .price_statistics import PriceStatistics
from .price_history_point import PriceHistoryPoint

__all__ = ["PriceHistory"]


class PriceHistory(BaseModel):
    canonical_product_id: str

    history: Optional[List[PriceHistoryPoint]] = None

    product_title: Optional[str] = None

    statistics: Optional[PriceStatistics] = None
