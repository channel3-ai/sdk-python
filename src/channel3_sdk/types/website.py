# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Website"]


class Website(BaseModel):
    id: str

    url: str

    best_commission_rate: Optional[float] = None
    """The maximum commission rate for the website, as a percentage"""
