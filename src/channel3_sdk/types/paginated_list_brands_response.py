# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .brand import Brand
from .._models import BaseModel

__all__ = ["PaginatedListBrandsResponse"]


class PaginatedListBrandsResponse(BaseModel):
    items: List[Brand]
    """List of brands"""

    paging_token: Optional[str] = None
    """Cursor to fetch the next page of results. Null if no more results."""
