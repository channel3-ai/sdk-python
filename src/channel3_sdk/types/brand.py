# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Brand"]


class Brand(BaseModel):
    id: str

    name: str

    description: Optional[str] = None

    logo_url: Optional[str] = None
