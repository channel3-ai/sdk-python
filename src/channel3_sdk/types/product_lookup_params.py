# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProductLookupParams"]


class ProductLookupParams(TypedDict, total=False):
    url: Required[str]
    """The URL of the product to look up"""

    max_staleness_hours: int
    """Maximum age (in hours) of cached product data before forcing a fresh lookup.

    Defaults to 3 hours.
    """

    x_user_id: Annotated[str, PropertyInfo(alias="x-user-id")]
    """Optional user identifier to attribute clicks and sales to a user in your system.

    Channel3 appends it to buy URLs in the response.
    """
