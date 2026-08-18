# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImagePartParam"]


class ImagePartParam(TypedDict, total=False):
    """An image by URL. ``data:`` URIs are uploaded and rewritten server-side."""

    url: Required[str]

    type: Literal["image"]
