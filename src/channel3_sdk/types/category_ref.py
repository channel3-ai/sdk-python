# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CategoryRef"]


class CategoryRef(BaseModel):
    """Lean reference to a category, used in path and children arrays."""

    slug: str
    """URL-friendly slug (e.g. 'sofas')"""

    title: str
    """Human-readable category title"""
