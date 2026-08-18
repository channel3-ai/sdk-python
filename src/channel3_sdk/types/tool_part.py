# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .product_ids_input import ProductIDsInput
from .catalog_tool_error import CatalogToolError
from .search_products_input import SearchProductsInput
from .catalog_display_payload import CatalogDisplayPayload

__all__ = ["ToolPart", "Input", "Output"]

Input: TypeAlias = Union[SearchProductsInput, ProductIDsInput]

Output: TypeAlias = Union[CatalogDisplayPayload, CatalogToolError, None]


class ToolPart(BaseModel):
    """One catalog tool call and its display payload from an assistant turn."""

    tool_call_id: str

    tool_name: str

    input: Optional[Input] = None

    output: Optional[Output] = None
    """Client-facing catalog tool result shown on the stream and on `ToolPart`."""

    type: Optional[Literal["tool"]] = None
