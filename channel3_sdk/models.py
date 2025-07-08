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


class MerchantOffering(BaseModel):
    """A merchant offering a product."""

    url: str = Field(
        default="https://buy.trychannel3.com", description="URL to purchase the product"
    )
    merchant_name: str = Field(..., description="Name of the merchant")
    price: Price = Field(..., description="Price information")
    availability: AvailabilityStatus = Field(
        ..., description="Product availability status"
    )


class FamilyMember(BaseModel):
    """A family member product."""

    id: str = Field(..., description="Unique identifier for the family member")
    title: str = Field(..., description="Title of the family member product")
    image_url: str = Field(..., description="Image URL for the family member product")


class Product(BaseModel):
    """A product returned from search."""

    id: str = Field(..., description="Unique identifier for the product")
    score: float = Field(..., description="Relevance score for the search query")
    brand_name: str = Field(..., description="Brand name of the product")
    title: str = Field(..., description="Product title")
    description: str = Field(..., description="Product description")
    image_url: str = Field(..., description="Main product image URL")
    offers: List[MerchantOffering] = Field(
        ..., description="List of merchant offerings"
    )
    family: List[FamilyMember] = Field(
        default_factory=list, description="Related family products"
    )


class ProductDetail(BaseModel):
    """Detailed information about a product."""

    brand_id: str = Field(..., description="Unique identifier for the brand")
    brand_name: str = Field(..., description="Brand name of the product")
    title: str = Field(..., description="Product title")
    description: str = Field(..., description="Product description")
    image_urls: List[str] = Field(..., description="List of product image URLs")
    merchant_offerings: List[MerchantOffering] = Field(
        ..., description="List of merchant offerings"
    )
    gender: Literal["na", "men", "women"] = Field(
        default="na", description="Target gender"
    )
    materials: Optional[List[str]] = Field(None, description="List of materials")
    key_features: List[str] = Field(
        default_factory=list, description="List of key product features"
    )
    family_members: List[FamilyMember] = Field(
        default_factory=list, description="Related family products"
    )


class SearchFilterPrice(BaseModel):
    """Price filter for product search."""

    min_price: Optional[float] = Field(None, description="Minimum price filter")
    max_price: Optional[float] = Field(None, description="Maximum price filter")


class SearchFilters(BaseModel):
    """Search filters for product search."""

    brands: Optional[List[str]] = Field(None, description="List of brands to filter by")
    gender: Optional[Literal["male", "female", "unisex"]] = Field(
        None, description="Gender to filter by"
    )
    price: Optional[SearchFilterPrice] = Field(
        None, description="Price range to filter by"
    )
    availability: Optional[AvailabilityStatus] = Field(
        None, description="Availability status to filter by"
    )


class SearchRequest(BaseModel):
    """Request model for product search."""

    query: Optional[str] = Field(None, description="Text search query")
    image_url: Optional[str] = Field(None, description="URL of image for visual search")
    base64_image: Optional[str] = Field(
        None, description="Base64-encoded image for visual search"
    )
    filters: SearchFilters = Field(
        default_factory=SearchFilters, description="Search filters"
    )
    limit: Optional[int] = Field(
        default=20, description="Maximum number of results to return"
    )
