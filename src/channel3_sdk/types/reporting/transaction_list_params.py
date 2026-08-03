# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Inclusive end of the window (ISO 8601 datetime with optional offset, e.g.

    2026-08-01T23:59:59-04:00). Offset-aware values are converted to UTC; naive
    values are treated as UTC.
    """

    limit: int
    """Items per page (max 100)."""

    page: int
    """Page number (1-indexed)."""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Inclusive start of the window (ISO 8601 datetime with optional offset, e.g.

    2026-08-01T00:00:00-04:00). Offset-aware values are converted to UTC; naive
    values are treated as UTC.
    """
