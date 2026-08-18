# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .product_detail import ProductDetail

__all__ = ["CatalogToolError"]


class CatalogToolError(BaseModel):
    error: str

    is_error: Optional[Literal[True]] = None

    products: Optional[List[ProductDetail]] = None
