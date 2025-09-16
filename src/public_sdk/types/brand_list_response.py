# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .brand import Brand
from .._models import BaseModel

__all__ = ["BrandListResponse", "Pagination"]


class Pagination(BaseModel):
    current_page: int

    page_size: int

    total_count: int

    total_pages: int


class BrandListResponse(BaseModel):
    items: List[Brand]

    pagination: Pagination
    """Pagination metadata for responses"""
