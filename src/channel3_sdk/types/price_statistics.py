# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PriceStatistics"]


class PriceStatistics(BaseModel):
    currency: str

    current_price: float

    current_status: Literal["low", "typical", "high"]

    max_price: float

    mean: float

    min_price: float

    std_dev: float
