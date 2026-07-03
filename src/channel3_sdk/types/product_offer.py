# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .price import Price
from .._models import BaseModel

__all__ = ["ProductOffer"]


class ProductOffer(BaseModel):
    availability: Literal["InStock", "OutOfStock"]

    domain: str

    price: Price

    url: str

    condition: Optional[Literal["new", "refurbished", "used"]] = None
    """Condition of this merchant offer (new, used, or refurbished).

    Null when condition is unknown.
    """

    max_commission_rate: Optional[float] = None
    """
    The maximum commission rate for the merchant, as a decimal fraction: 0 is no
    commission, 0.5 is 50% commission. 'Max' because the actual commission rate may
    be lower due to vendor-specific affiliate rules.
    """
