# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .product import Product

__all__ = ["SearchPerformResponse"]

SearchPerformResponse: TypeAlias = List[Product]
