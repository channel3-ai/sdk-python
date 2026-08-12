# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TurnErrorCode"]

TurnErrorCode: TypeAlias = Literal[
    "invalid_request",
    "unauthorized",
    "insufficient_credits",
    "conversation_not_found",
    "turn_conflict",
    "rate_limited",
    "model_unavailable",
    "internal",
]
