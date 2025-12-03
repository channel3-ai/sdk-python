# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Subscription"]


class Subscription(BaseModel):
    canonical_product_id: str

    created_at: datetime

    subscription_status: Literal["active", "cancelled"]
