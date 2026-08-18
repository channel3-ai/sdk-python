# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .turn_usage import TurnUsage
from .assistant_message import AssistantMessage

__all__ = ["TurnResult"]


class TurnResult(BaseModel):
    """Buffered equivalent of a streamed turn (``stream: false``)."""

    conversation_id: str

    message: AssistantMessage

    turn_id: str

    usage: TurnUsage
