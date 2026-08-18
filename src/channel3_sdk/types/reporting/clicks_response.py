# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .click import Click
from ..._models import BaseModel
from .clicks_summary import ClicksSummary

__all__ = ["ClicksResponse"]


class ClicksResponse(BaseModel):
    """Paginated clicks for a vendor over a date range."""

    end_date: datetime
    """Inclusive end of the resolved query window."""

    has_more: bool
    """Whether more pages are available."""

    items: List[Click]

    limit: int
    """Page size."""

    page: int
    """Current page (1-indexed)."""

    start_date: datetime
    """Inclusive start of the resolved query window."""

    summary: ClicksSummary
    """Aggregate click stats for the requested date range."""

    total_count: int
    """Total matching clicks in the date range."""
