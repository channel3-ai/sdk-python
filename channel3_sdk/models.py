"""Pydantic models for the Channel3 API."""

from enum import Enum
from typing import List, Optional, Union, Literal
from pydantic import BaseModel, Field


class AvailabilityStatus(str, Enum):
    """Availability status of a product."""

    IN_STOCK = "InStock"
    OUT_OF_STOCK = "OutOfStock"
    PRE_ORDER = "PreOrder"
    LIMITED_AVAILABILITY = "LimitedAvailability"
    BACK_ORDER = "BackOrder"
    DISCONTINUED = "Discontinued"
    SOLD_OUT = "SoldOut"
    UNKNOWN = "Unknown"


class Price(BaseModel):
    """Price information for a product."""

    price: float = Field(
        ..., description="The current price of the product, including any discounts."
    )
    compare_at_price: Optional[float] = Field(
        None, description="The original price of the product before any discounts."
    )
    currency: str = Field(..., description="The currency code of the product.")


class Brand(BaseModel):
    """A brand."""

    id: str = Field(..., description="Unique identifier for the brand")
    name: str = Field(..., description="Name of the brand")
    logo_url: Optional[str] = Field(None, description="Logo URL for the brand")
    description: Optional[str] = Field(None, description="Description of the brand")


class Variant(BaseModel):
    """A product variant."""

    product_id: str = Field(..., description="Unique identifier for the product")
    title: str = Field(..., description="Title of the variant")
    image_url: str = Field(..., description="Image URL for the variant")


class Product(BaseModel):
    """A product returned from search."""

    id: str = Field(..., description="Unique identifier for the product")
    score: float = Field(..., description="Relevance score for the search query")
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    brand_name: str = Field(..., description="Brand name of the product")
    image_url: str = Field(..., description="Main product image URL")
    price: Price = Field(..., description="Price information")
    availability: AvailabilityStatus = Field(
        ..., description="Product availability status"
    )
    variants: List[Variant] = Field(
        default_factory=list, description="Product variants"
    )


class ProductDetail(BaseModel):
    """Detailed information about a product."""

    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    brand_id: Optional[str] = Field(None, description="Unique identifier for the brand")
    brand_name: Optional[str] = Field(None, description="Brand name of the product")
    image_urls: Optional[List[str]] = Field(
        None, description="List of product image URLs"
    )
    price: Price = Field(..., description="Price information")
    availability: AvailabilityStatus = Field(
        ..., description="Product availability status"
    )
    key_features: Optional[List[str]] = Field(
        None, description="List of key product features"
    )
    variants: List[Variant] = Field(
        default_factory=list, description="Product variants"
    )


class SearchFilterPrice(BaseModel):
    """Price filter for product search."""

    min_price: Optional[float] = Field(None, description="Minimum price filter")
    max_price: Optional[float] = Field(None, description="Maximum price filter")


class SearchFilters(BaseModel):
    """Search filters for product search."""

    brand_ids: Optional[List[str]] = Field(
        None, description="List of brand IDs to filter by"
    )
    gender: Optional[Literal["male", "female", "unisex"]] = Field(
        None, description="Gender to filter by"
    )
    price: Optional[SearchFilterPrice] = Field(
        None, description="Price range to filter by"
    )
    availability: Optional[List[AvailabilityStatus]] = Field(
        None, description="Availability statuses to filter by"
    )


class SearchRequest(BaseModel):
    """Request model for product search."""

    query: Optional[str] = Field(None, description="Text search query")
    image_url: Optional[str] = Field(None, description="URL of image for visual search")
    base64_image: Optional[str] = Field(
        None, description="Base64-encoded image for visual search"
    )
    limit: Optional[int] = Field(
        default=20, description="Maximum number of results to return"
    )
    filters: Optional[SearchFilters] = Field(default=None, description="Search filters")
