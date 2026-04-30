# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .category_summary import CategorySummary

__all__ = ["SearchCategoriesResponse"]


class SearchCategoriesResponse(BaseModel):
    categories: List[CategorySummary]
    """Categories matching the query, ordered by relevance."""
