# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .category_summary import CategorySummary

__all__ = ["PaginatedListCategoriesResponse"]


class PaginatedListCategoriesResponse(BaseModel):
    items: List[CategorySummary]
    """Categories in this page"""

    page: int
    """1-indexed page number returned"""

    page_size: int
    """Number of items per page"""

    total: int
    """Total number of categories matching the query"""
