# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProductLookupParams"]


class ProductLookupParams(TypedDict, total=False):
    url: Required[str]
    """The URL of the product to look up"""

    max_staleness_hours: int
    """Maximum age (in hours) of cached product data before forcing a fresh lookup.

    Defaults to 3 hours.
    """
