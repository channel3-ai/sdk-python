# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CategoryListParams"]


class CategoryListParams(TypedDict, total=False):
    page: int
    """1-indexed page number."""

    page_size: int
    """Items per page."""

    roots_only: bool
    """If true, return only top-level (root) categories."""
