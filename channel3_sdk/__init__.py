"""Channel3 SDK for Python - Official SDK for the Channel3 AI Shopping API."""

from .client import Channel3Client, AsyncChannel3Client
from .models import (
    Product,
    ProductDetail,
    SearchFilters,
    SearchRequest,
    MerchantOffering,
    FamilyMember,
    Price,
    AvailabilityStatus,
)
from .exceptions import (
    Channel3Error,
    Channel3AuthenticationError,
    Channel3ValidationError,
    Channel3NotFoundError,
    Channel3ServerError,
    Channel3ConnectionError,
)

__version__ = "0.1.0"
__all__ = [
    # Clients
    "Channel3Client",
    "AsyncChannel3Client",
    # Models
    "Product",
    "ProductDetail",
    "SearchFilters",
    "SearchRequest",
    "MerchantOffering",
    "FamilyMember",
    "Price",
    "AvailabilityStatus",
    # Exceptions
    "Channel3Error",
    "Channel3AuthenticationError",
    "Channel3ValidationError",
    "Channel3NotFoundError",
    "Channel3ServerError",
    "Channel3ConnectionError",
]
