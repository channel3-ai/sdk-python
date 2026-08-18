# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ImagePart"]


class ImagePart(BaseModel):
    """An image by URL. ``data:`` URIs are uploaded and rewritten server-side."""

    url: str

    type: Optional[Literal["image"]] = None
