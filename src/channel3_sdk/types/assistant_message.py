# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .text_part import TextPart
from .tool_part import ToolPart

__all__ = ["AssistantMessage", "Part"]

Part: TypeAlias = Annotated[Union[TextPart, ToolPart], PropertyInfo(discriminator="type")]


class AssistantMessage(BaseModel):
    parts: Optional[List[Part]] = None

    role: Optional[Literal["assistant"]] = None

    suggestions: Optional[List[str]] = None
    """Tap-ready follow-up messages offered after this reply."""
