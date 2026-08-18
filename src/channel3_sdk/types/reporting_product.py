# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ReportingProduct"]


class ReportingProduct(BaseModel):
    """Compact product reference on click/transaction items."""

    id: str
    """Canonical product ID."""

    image_url: Optional[str] = None
    """Product image URL."""

    title: Optional[str] = None
    """Product title."""
