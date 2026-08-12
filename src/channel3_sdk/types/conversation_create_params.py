# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .user_message_param import UserMessageParam
from .search_filters_param import SearchFiltersParam
from .conversation_context_param import ConversationContextParam

__all__ = ["ConversationCreateParams"]


class ConversationCreateParams(TypedDict, total=False):
    message: Required[UserMessageParam]

    context: Optional[ConversationContextParam]
    """Partner-supplied context pinned to the top of a conversation thread."""

    conversation_id: Optional[str]
    """Existing thread to continue; when omitted, a new thread is created."""

    filters: Optional[SearchFiltersParam]
    """Search filters for the search API."""

    stream: bool
    """Stream turn events over SSE (default) or return the assembled turn as JSON."""

    x_user_id: Annotated[str, PropertyInfo(alias="x-user-id")]
    """Optional user identifier to attribute clicks and sales to a user in your system.

    Channel3 appends it to buy URLs in the response.
    """
