# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .conversation_context import ConversationContext

__all__ = ["Conversation"]


class Conversation(BaseModel):
    id: str

    created_at: int

    context: Optional[ConversationContext] = None
    """Partner-supplied context pinned to the top of a conversation thread."""

    metadata: Optional[Dict[str, object]] = None
    """Free-form key/value pairs the caller attached to the thread."""

    user_id: Optional[str] = None
