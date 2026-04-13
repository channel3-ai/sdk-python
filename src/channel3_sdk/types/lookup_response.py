# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .product_detail import ProductDetail

__all__ = ["LookupResponse"]


class LookupResponse(BaseModel):
    """Response from the /v1/lookup endpoint."""

    product: ProductDetail
    """Product with detailed information."""
