# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConversationContext"]


class ConversationContext(BaseModel):
    """Partner-supplied context pinned to the top of a conversation thread."""

    application_context: Optional[str] = None
    """What platform or surface is hosting this conversation."""

    user_context: Optional[str] = None
    """Who the conversation is with (profile, preferences, session facts)."""
