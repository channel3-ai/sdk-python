# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ProductRetrieveParams"]


class ProductRetrieveParams(TypedDict, total=False):
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

    Matches any country when unset; defaults to 'US' only when language and currency
    are also unset.
    """

    currency: Optional[Literal["USD", "CAD", "AUD", "GBP", "EUR", "SEK", "CZK", "RON"]]
    """ISO 4217 currency code.

    When unset, inferred from `country` (e.g. GB -> GBP); falls back to 'USD' only
    when all three locale fields are unset.
    """

    language: Optional[Literal["en", "de", "fr", "it", "es", "nl", "sv", "fi", "pt", "cs", "el", "ro"]]
    """ISO 639-1 language code.

    Matches any language when unset; defaults to 'en' only when country and currency
    are also unset.
    """

    website_ids: Optional[SequenceNotStr[str]]
    """
    Optional list of website IDs to constrain the buy URL to, relevant if multiple
    merchants exist. Accepts website IDs or domains (e.g. "nike.com").
    """
