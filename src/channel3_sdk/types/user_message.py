# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .text_part import TextPart
from .image_part import ImagePart

__all__ = ["UserMessage", "Part"]

Part: TypeAlias = Annotated[Union[TextPart, ImagePart], PropertyInfo(discriminator="type")]


class UserMessage(BaseModel):
    parts: Optional[List[Part]] = None

    role: Optional[Literal["user"]] = None
