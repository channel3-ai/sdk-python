# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ProductRetrieveParams"]


class ProductRetrieveParams(TypedDict, total=False):
    website_ids: Optional[SequenceNotStr[str]]
    """
    Optional list of website IDs to constrain the buy URL to, relevant if multiple
    merchants exist
    """
