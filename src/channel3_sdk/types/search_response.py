# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .product_detail import ProductDetail

__all__ = ["SearchResponse"]


class SearchResponse(BaseModel):
    """v1 paginated search response."""

    products: List[ProductDetail]

    next_page_token: Optional[str] = None
    """Token to fetch the next page. Null when no more results."""
