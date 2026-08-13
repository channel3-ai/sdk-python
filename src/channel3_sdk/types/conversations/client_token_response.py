# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ClientTokenResponse"]


class ClientTokenResponse(BaseModel):
    token: str

    expires_at: int

    token_type: Optional[Literal["Bearer"]] = None
