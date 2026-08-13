# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ClientTokenCreateParams"]


class ClientTokenCreateParams(TypedDict, total=False):
    conversation_id: Optional[str]

    session_id: Optional[str]

    ttl_seconds: int
