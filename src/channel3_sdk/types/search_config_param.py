# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SearchConfigParam"]


class SearchConfigParam(TypedDict, total=False):
    """Search and locale options for a search request."""

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
    """ISO 3166-1 alpha-2 country code.

    May stay unset for pan-region storefronts (e.g. `currency=EUR` with no specific
    country).
    """

    currency: Optional[Literal["USD", "CAD", "AUD", "GBP", "EUR", "SEK", "CZK", "RON"]]
    """ISO 4217 currency code.

    When unset, inferred from `country` (e.g. `GB` → `GBP`), defaulting to `USD`.
    """

    keyword_search_only: bool
    """If True, search will only use keyword search and not vector search.

    Keyword-only search is not supported with image input.
    """

    language: Optional[Literal["en", "de", "fr", "it", "es", "nl", "sv", "fi", "pt", "cs", "el", "ro"]]
    """ISO 639-1 language code.

    When unset, inferred from `country` (preferred) then `currency`, defaulting to
    `en`.
    """
