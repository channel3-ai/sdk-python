# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..affiliate_product import AffiliateProduct
from .public_transaction_status import PublicTransactionStatus

__all__ = ["Transaction"]


class Transaction(BaseModel):
    """A single affiliate CPA transaction."""

    id: str
    """Transaction ID."""

    commission_amount: float
    """Vendor net commission (after Channel3 take rate)."""

    order_amount: float
    """Order amount in the transaction currency."""

    purchased_at: datetime
    """Purchase timestamp, returned with a UTC offset (Z)."""

    status: PublicTransactionStatus
    """pending (includes network-approved) or paid."""

    brand_name: Optional[str] = None
    """Brand name, if known."""

    city: Optional[str] = None
    """Purchase city, if available."""

    country: Optional[str] = None
    """Purchase country, if available."""

    product: Optional[AffiliateProduct] = None
    """Compact product reference on click/transaction items."""
