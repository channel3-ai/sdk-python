# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from .transaction import Transaction
from .transactions_summary import TransactionsSummary

__all__ = ["TransactionsResponse"]


class TransactionsResponse(BaseModel):
    """Paginated transactions for a vendor over a date range."""

    end_date: datetime
    """Inclusive end of the resolved query window.

    Always returned with a UTC offset (Z); request values with other offsets are
    converted.
    """

    has_more: bool
    """Whether more pages are available."""

    items: List[Transaction]

    limit: int
    """Page size."""

    page: int
    """Current page (1-indexed)."""

    start_date: datetime
    """Inclusive start of the resolved query window.

    Always returned with a UTC offset (Z); request values with other offsets are
    converted.
    """

    summary: TransactionsSummary
    """Aggregate transaction stats for the requested date range."""

    total_count: int
    """Total matching transactions in the date range."""
