# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..affiliate_product import AffiliateProduct

__all__ = ["Click"]


class Click(BaseModel):
    """A single affiliate click event."""

    id: str
    """Click event ID."""

    timestamp: datetime
    """When the click occurred, returned with a UTC offset (Z)."""

    city: Optional[str] = None
    """Click city, if available."""

    country: Optional[str] = None
    """Click country, if available."""

    product: Optional[AffiliateProduct] = None
    """Compact product reference on click/transaction items."""
