# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Price"]


class Price(BaseModel):
    currency: str
    """The currency code of the product, like USD, EUR, GBP, etc."""

    price: float
    """The current price of the product, including any discounts."""

    compare_at_price: Optional[float] = None
    """The original price of the product before any discounts."""
