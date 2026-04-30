# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from ..._models import BaseModel

__all__ = ["ErrorResponse"]


class ErrorResponse(BaseModel):
    detail: Union[str, List[Dict[str, object]]]
