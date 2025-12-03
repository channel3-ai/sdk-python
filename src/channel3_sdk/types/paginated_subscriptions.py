# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .subscription import Subscription

__all__ = ["PaginatedSubscriptions"]


class PaginatedSubscriptions(BaseModel):
    subscriptions: List[Subscription]

    next_page_token: Optional[str] = None
