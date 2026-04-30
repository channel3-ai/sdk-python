# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrandSearchParams"]


class BrandSearchParams(TypedDict, total=False):
    query: Required[str]
    """Free-text query (e.g. 'Nike', 'lululemon')."""

    limit: int
    """Maximum number of brands to return."""
