# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CategorySearchParams"]


class CategorySearchParams(TypedDict, total=False):
    query: Required[str]
    """Free-text query (e.g. 'sofas', 'yoga mats')."""

    limit: int
    """Maximum number of categories to return."""
