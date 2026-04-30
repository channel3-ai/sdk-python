# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .category_ref import CategoryRef

__all__ = ["CategorySummary"]


class CategorySummary(BaseModel):
    """Lean category representation used in search hits and list rows."""

    has_children: bool
    """Whether this category has subcategories"""

    slug: str
    """URL-friendly slug (e.g. 'sofas')"""

    title: str
    """Human-readable category title"""

    path: Optional[List[CategoryRef]] = None
    """
    Hierarchical path as a structured list, root first; the last entry is this
    category itself
    """
