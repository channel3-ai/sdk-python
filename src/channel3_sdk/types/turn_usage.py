# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TurnUsage"]


class TurnUsage(BaseModel):
    credits_charged: int
    """API credits charged for this turn (turn fee plus catalog searches)."""

    searches_run: int
    """Catalog searches executed during this turn."""
