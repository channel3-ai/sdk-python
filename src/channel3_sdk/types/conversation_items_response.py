# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ConversationItemsResponse", "Item", "ItemPart"]


class ItemPart(BaseModel):
    type: Literal["text", "tool", "image"]

    input: Optional[Dict[str, object]] = None

    api_model_only: Optional[bool] = FieldInfo(alias="modelOnly", default=None)
    """Tool call kept in conversation history for model context only.

    Not streamed to the UI and not exposed as a conversation item.
    """

    output: Optional[Dict[str, object]] = None

    suggested_replies: Optional[List[str]] = FieldInfo(alias="suggestedReplies", default=None)

    text: Optional[str] = None

    tool_call_id: Optional[str] = FieldInfo(alias="toolCallId", default=None)

    tool_name: Optional[str] = FieldInfo(alias="toolName", default=None)

    url: Optional[str] = None


class Item(BaseModel):
    role: str

    parts: Optional[List[ItemPart]] = None


class ConversationItemsResponse(BaseModel):
    items: List[Item]
