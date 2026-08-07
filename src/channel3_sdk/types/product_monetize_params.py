# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProductMonetizeParams"]


class ProductMonetizeParams(TypedDict, total=False):
    url: Required[str]
    """The URL of the product to monetize"""

    x_user_id: Annotated[str, PropertyInfo(alias="x-user-id")]
    """Optional user identifier to attribute clicks and sales to a user in your system.

    Channel3 appends it to buy URLs in the response.
    """
