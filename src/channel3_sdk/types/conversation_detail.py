# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .user_message import UserMessage
from .assistant_message import AssistantMessage
from .conversation_context import ConversationContext

__all__ = ["ConversationDetail", "Item"]

Item: TypeAlias = Annotated[Union[UserMessage, AssistantMessage], PropertyInfo(discriminator="role")]


class ConversationDetail(BaseModel):
    """Thread metadata plus one page of its message history."""

    id: str

    created_at: int

    items: List[Item]

    context: Optional[ConversationContext] = None
    """Partner-supplied context pinned to the top of a conversation thread."""

    has_more: Optional[bool] = None

    next_cursor: Optional[str] = None
    """Pass as `cursor` to fetch the next page. Null when no more items."""

    user_id: Optional[str] = None
