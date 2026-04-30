# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CategoryAttribute"]


class CategoryAttribute(BaseModel):
    """A structured attribute (e.g. Color, Size) applicable to a category."""

    name: str
    """Human-readable attribute name (e.g. 'Color')"""

    slug: str
    """URL-friendly identifier (e.g. 'color', 'frame-color')"""

    values: Optional[List[str]] = None
    """Allowed values for this attribute.

    May be empty when no enumerated value set is defined.
    """
