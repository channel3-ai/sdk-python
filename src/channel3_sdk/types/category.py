# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .category_ref import CategoryRef
from .category_attribute import CategoryAttribute

__all__ = ["Category"]


class Category(BaseModel):
    """Full category representation used in detail responses."""

    has_children: bool
    """Whether this category has subcategories"""

    slug: str
    """URL-friendly slug (e.g. 'sofas')"""

    title: str
    """Human-readable category title"""

    attributes: Optional[List[CategoryAttribute]] = None
    """Structured attributes applicable to this category"""

    children: Optional[List[CategoryRef]] = None
    """Direct subcategories only (one level)"""

    description: Optional[str] = None
    """Natural-language description of products in this category"""

    path: Optional[List[CategoryRef]] = None
    """
    Hierarchical path as a structured list, root first; the last entry is this
    category itself
    """
