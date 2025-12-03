# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PriceTrackingListSubscriptionsParams"]


class PriceTrackingListSubscriptionsParams(TypedDict, total=False):
    limit: int

    page_token: Optional[str]
