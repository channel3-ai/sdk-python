# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BrandListParams"]


class BrandListParams(TypedDict, total=False):
    limit: int
    """Max results (1-100)"""

    paging_token: Optional[str]
    """Pagination cursor"""
