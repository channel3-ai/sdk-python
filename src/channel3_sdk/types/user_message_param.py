# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, TypeAlias, TypedDict

from .text_part_param import TextPartParam
from .image_part_param import ImagePartParam

__all__ = ["UserMessageParam", "Part"]

Part: TypeAlias = Union[TextPartParam, ImagePartParam]


class UserMessageParam(TypedDict, total=False):
    parts: Iterable[Part]

    role: Literal["user"]
