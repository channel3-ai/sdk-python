# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .conversation_context_param import ConversationContextParam

__all__ = ["ResponseCreateParams", "Attachment", "Image", "Message", "MessagePart"]


class ResponseCreateParams(TypedDict, total=False):
    attachments: Optional[Iterable[Attachment]]

    context: Optional[ConversationContextParam]
    """Partner-supplied context pinned to the top of a conversation thread."""

    conversation_id: Optional[str]

    debug: bool

    image: Optional[Image]

    message: Optional[Message]

    messages: Iterable[Message]

    x_user_id: Annotated[str, PropertyInfo(alias="x-user-id")]
    """Optional user identifier to attribute clicks and sales to a user in your system.

    Channel3 appends it to buy URLs in the response.
    """


class Attachment(TypedDict, total=False):
    url: Required[str]

    key: Optional[str]


class Image(TypedDict, total=False):
    base64: Optional[str]

    url: Optional[str]


class MessagePart(TypedDict, total=False):
    type: Required[Literal["text", "tool", "image"]]

    input: Optional[Dict[str, object]]

    model_only: Annotated[bool, PropertyInfo(alias="modelOnly")]
    """Tool call kept in conversation history for model context only.

    Not streamed to the UI and not exposed as a conversation item.
    """

    output: Optional[Dict[str, object]]

    suggested_replies: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="suggestedReplies")]

    text: Optional[str]

    tool_call_id: Annotated[Optional[str], PropertyInfo(alias="toolCallId")]

    tool_name: Annotated[Optional[str], PropertyInfo(alias="toolName")]

    url: Optional[str]


class Message(TypedDict, total=False):
    role: Required[str]

    parts: Iterable[MessagePart]
