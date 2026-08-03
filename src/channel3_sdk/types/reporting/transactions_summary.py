# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TransactionsSummary"]


class TransactionsSummary(BaseModel):
    """Aggregate transaction stats for the requested date range."""

    paid_commission: float
    """Vendor net commission already paid out."""

    pending_commission: float
    """Vendor net commission still pending payout."""

    total_commission: float
    """Sum of vendor net commission (pending + paid) for the date range."""

    total_count: int
    """Total transactions in the date range."""
