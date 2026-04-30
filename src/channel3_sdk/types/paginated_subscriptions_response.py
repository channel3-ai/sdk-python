# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .subscription import Subscription

__all__ = ["PaginatedSubscriptionsResponse"]


class PaginatedSubscriptionsResponse(BaseModel):
    items: List[Subscription]

    next_cursor: Optional[str] = None
