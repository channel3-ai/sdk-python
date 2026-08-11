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
    """ISO 3166-1 alpha-2 country code (plus the pan-region `EU`)."""

    currency: Optional[Literal["USD", "CAD", "AUD", "GBP", "EUR", "SEK", "CZK", "RON"]]
    """ISO 4217 currency code."""

    language: Optional[Literal["en", "de", "fr", "it", "es", "nl", "sv", "fi", "pt", "cs", "el", "ro"]]
    """ISO 639-1 language code."""

    length_unit: Optional[Literal["mm", "cm", "m", "in", "ft"]]
    """Preferred unit for length dimensions (length/width/height) in responses.

    A request dimension filter's unit for the field takes precedence; when neither
    is set, the merchant's stated unit is returned.
    """

    mode: Literal["keyword", "default", "agentic"]
    """Search strategy.

    `default` (recommended) combines lexical + semantic search and is right for most
    use cases. `keyword` is lexical only — use it for real-time, low-latency needs
    like ad targeting. `agentic` uses an LLM to plan multiple structured
    sub-searches for complex queries, with higher latency than the other modes.
    """

    weight_unit: Optional[Literal["mg", "g", "kg", "oz", "lb"]]
    """Preferred unit for weight dimensions in responses.

    A request dimension filter's weight unit takes precedence; when neither is set,
    the merchant's stated unit is returned.
    """
