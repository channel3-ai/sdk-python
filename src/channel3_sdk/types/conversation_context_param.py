# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ConversationContextParam"]


class ConversationContextParam(TypedDict, total=False):
    """Partner-supplied context pinned to the top of a conversation thread."""

    application_context: Optional[str]
    """What platform or surface is hosting this conversation."""

    user_context: Optional[str]
    """Who the conversation is with (profile, preferences, session facts)."""
