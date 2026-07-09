# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LocaleConfigParam"]


class LocaleConfigParam(TypedDict, total=False):
    """Locale options for API requests.

    Locale fields are optional; the server infers missing values. Details are
    on ``language``, ``country``, and ``currency`` below.
    """

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

    language: Optional[Literal["en", "de", "fr", "it", "es", "nl", "sv", "fi", "pt", "cs", "el", "ro"]]
    """ISO 639-1 language code.

    When unset, inferred from `country` (preferred) then `currency`, defaulting to
    `en`.
    """

    preferred_length_unit: Optional[Literal["mm", "cm", "m", "in", "ft"]]
    """Preferred unit for length dimensions (length/width/height) in responses.

    A request dimension filter's unit for the field takes precedence; when neither
    is set, the merchant's stated unit is returned.
    """

    preferred_weight_unit: Optional[Literal["mg", "g", "kg", "oz", "lb"]]
    """Preferred unit for weight dimensions in responses.

    A request dimension filter's weight unit takes precedence; when neither is set,
    the merchant's stated unit is returned.
    """
