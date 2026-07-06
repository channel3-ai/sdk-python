# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MonetizeOffer"]


class MonetizeOffer(BaseModel):
    domain: str
    """Merchant domain, e.g. nordstrom.com"""

    url: str
    """buy.trychannel3.com deeplink.

    Clicks are tracked and routed through the highest-paying affiliate network for
    the merchant.
    """

    max_commission_rate: Optional[float] = None
    """Maximum post-take-rate commission for the merchant, as a decimal (0.05 = 5%).

    'Max' because the realized rate may be lower.
    """
