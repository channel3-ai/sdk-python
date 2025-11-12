# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .redirect_mode import RedirectMode

__all__ = ["SearchConfigParam"]


class SearchConfigParam(TypedDict, total=False):
    enrich_query: bool
    """
    If True, search will use AI to enrich the query, for example pulling the gender,
    brand, and price range from the query.
    """

    redirect_mode: Optional[RedirectMode]
    """
    "price" redirects to the product page with the lowest price "commission"
    redirects to the product page with the highest commission rate "brand" redirects
    to the brand's product page
    """
