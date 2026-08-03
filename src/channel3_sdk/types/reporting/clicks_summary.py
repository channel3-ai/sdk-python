# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ClicksSummary"]


class ClicksSummary(BaseModel):
    """Aggregate click stats for the requested date range."""

    total_clicks: int
    """Total clicks in the date range."""
