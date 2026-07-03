# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrandSearchParams"]


class BrandSearchParams(TypedDict, total=False):
    query: Required[str]
    """Free-text query (e.g. 'Nike', 'lululemon')."""

    country: Optional[
        Literal[
            "US",
            "GB",
            "EU",
            "AU",
            "CA",
            "IE",
            "DE",
            "AT",
            "FR",
            "BE",
            "IT",
            "ES",
            "NL",
            "SE",
            "FI",
            "PT",
            "CZ",
            "GR",
            "RO",
        ]
    ]
    """ISO 3166-1 alpha-2 country code that `best_commission_rate` is scoped to.

    Defaults to 'US' when unset.
    """

    limit: int
    """Maximum number of brands to return."""
