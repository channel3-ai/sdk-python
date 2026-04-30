# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .brand import Brand
from .._models import BaseModel

__all__ = ["SearchBrandsResponse"]


class SearchBrandsResponse(BaseModel):
    brands: List[Brand]
    """Brands matching the query, ordered by relevance."""
