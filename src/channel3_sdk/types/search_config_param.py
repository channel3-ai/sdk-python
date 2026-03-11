# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SearchConfigParam"]


class SearchConfigParam(TypedDict, total=False):
    """Search configuration for the search API."""

    keyword_search_only: bool
    """If True, search will only use keyword search and not vector search.

    Keyword-only search is not supported with image input.
    """
