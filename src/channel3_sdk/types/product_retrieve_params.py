# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .redirect_mode import RedirectMode

__all__ = ["ProductRetrieveParams"]


class ProductRetrieveParams(TypedDict, total=False):
    redirect_mode: Optional[RedirectMode]
    """
    "price" redirects to the product page with the lowest price "commission"
    redirects to the product page with the highest commission rate "brand" redirects
    to the brand's product page
    """

    website_ids: Optional[SequenceNotStr[str]]
    """
    Optional list of website IDs to constrain the buy URL to, relevant if multiple
    merchants exist
    """
