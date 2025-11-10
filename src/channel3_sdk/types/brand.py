# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Brand"]


class Brand(BaseModel):
    id: str

    name: str

    best_commission_rate: Optional[float] = None
    """The maximum commission rate for the brand, as a percentage"""

    description: Optional[str] = None

    logo_url: Optional[str] = None
