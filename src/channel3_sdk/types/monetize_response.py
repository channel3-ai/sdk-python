# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .monetize_offer import MonetizeOffer

__all__ = ["MonetizeResponse"]


class MonetizeResponse(BaseModel):
    """Response from the /v1/monetize endpoint — just the list of offers."""

    offers: Optional[List[MonetizeOffer]] = None
    """Monetizable offers, sorted by max_commission_rate descending."""
