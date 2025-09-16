# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AvailabilityStatus"]

AvailabilityStatus: TypeAlias = Literal[
    "InStock", "LimitedAvailability", "PreOrder", "BackOrder", "SoldOut", "OutOfStock", "Discontinued", "Unknown"
]
