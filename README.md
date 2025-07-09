# Channel3 Python SDK

The official Python SDK for the [Channel3](https://trychannel3.com) AI Shopping API.

## Installation

```bash
pip install channel3-sdk
```

## Quick Start

### Synchronous Client

```python
import os
from channel3_sdk import Channel3Client

# Initialize the client
client = Channel3Client(api_key="your_api_key_here")
# Or use environment variable: CHANNEL3_API_KEY

# Search for products
products = client.search(query="blue denim jacket")

for product in products:
    print(f"Product: {product.title}")
    print(f"Brand: {product.brand_name}")
    print(f"Price: {product.price.currency} {product.price.price}")
    print(f"Availability: {product.availability}")
    print("---")

# Get detailed product information
product_detail = client.get_product("prod_123456")
print(f"Detailed info for: {product_detail.title}")
print(f"Brand: {product_detail.brand_name}")
if product_detail.key_features:
    print(f"Key features: {product_detail.key_features}")

# Get all brands
brands = client.get_brands()
for brand in brands:
    print(f"Brand: {brand.name}")
    if brand.description:
        print(f"Description: {brand.description}")

# Get specific brand details
brand = client.get_brand("brand_123")
print(f"Brand: {brand.name}")
```

### Asynchronous Client

```python
import asyncio
from channel3_sdk import AsyncChannel3Client

async def main():
    # Initialize the async client
    client = AsyncChannel3Client(api_key="your_api_key_here")
    
    # Search for products
    products = await client.search(query="running shoes")
    
    for product in products:
        print(f"Product: {product.title}")
        print(f"Score: {product.score}")
        print(f"Price: {product.price.currency} {product.price.price}")
    
    # Get detailed product information
    if products:
        product_detail = await client.get_product(products[0].id)
        print(f"Availability: {product_detail.availability}")
    
    # Get brands
    brands = await client.get_brands()
    print(f"Found {len(brands)} brands")

# Run the async function
asyncio.run(main())
```

## Advanced Usage

### Visual Search

```python
# Search by image URL
products = client.search(image_url="https://example.com/image.jpg")

# Search by base64 image
with open("image.jpg", "rb") as f:
    import base64
    base64_image = base64.b64encode(f.read()).decode()
    products = client.search(base64_image=base64_image)
```

### Multimodal Search

```python
# Combine text and image search
products = client.search(
    query="blue denim jacket",
    image_url="https://example.com/jacket.jpg"
)
```

### Search with Filters

```python
from channel3_sdk import SearchFilters, AvailabilityStatus

# Create search filters
filters = SearchFilters(
    brand_ids=["brand_123", "brand_456"],
    gender="male",
    availability=[AvailabilityStatus.IN_STOCK],
    price={"min_price": 50.0, "max_price": 200.0}
)

# Search with filters
products = client.search(
    query="jacket",
    filters=filters,
    limit=10
)
```

### Brand Management

```python
# Get all brands with pagination
brands = client.get_brands(page=1, size=50)

# Search for specific brands
nike_brands = client.get_brands(query="nike")

# Get detailed brand information
brand_detail = client.get_brand("brand_123")
print(f"Brand: {brand_detail.name}")
print(f"Logo: {brand_detail.logo_url}")
```

## API Reference

### Client Classes

#### `Channel3Client`
Synchronous client for the Channel3 API.

**Methods:**
- `search(query=None, image_url=None, base64_image=None, filters=None, limit=20)` → `List[Product]`
- `get_product(product_id)` → `ProductDetail`
- `get_brands(query=None, page=1, size=100)` → `List[Brand]`
- `get_brand(brand_id)` → `Brand`

#### `AsyncChannel3Client` 
Asynchronous client for the Channel3 API.

**Methods:**
- `async search(query=None, image_url=None, base64_image=None, filters=None, limit=20)` → `List[Product]`
- `async get_product(product_id)` → `ProductDetail`
- `async get_brands(query=None, page=1, size=100)` → `List[Brand]`
- `async get_brand(brand_id)` → `Brand`

### Models

#### `Product`
- `id: str` - Unique product identifier
- `score: float` - Search relevance score
- `title: str` - Product title
- `description: Optional[str]` - Product description
- `brand_name: str` - Brand name
- `image_url: str` - Main product image URL
- `price: Price` - Price information
- `availability: AvailabilityStatus` - Availability status
- `variants: List[Variant]` - Product variants

#### `ProductDetail`
- `title: str` - Product title
- `description: Optional[str]` - Product description
- `brand_id: Optional[str]` - Brand identifier
- `brand_name: Optional[str]` - Brand name
- `image_urls: Optional[List[str]]` - Product image URLs
- `price: Price` - Price information
- `availability: AvailabilityStatus` - Availability status
- `key_features: Optional[List[str]]` - Key product features
- `variants: List[Variant]` - Product variants

#### `Brand`
- `id: str` - Unique brand identifier
- `name: str` - Brand name
- `logo_url: Optional[str]` - Brand logo URL
- `description: Optional[str]` - Brand description

#### `Variant`
- `product_id: str` - Associated product identifier
- `title: str` - Variant title
- `image_url: str` - Variant image URL

#### `SearchFilters`
- `brand_ids: Optional[List[str]]` - Brand ID filters
- `gender: Optional[Literal["male", "female", "unisex"]]` - Gender filter
- `price: Optional[SearchFilterPrice]` - Price range filter
- `availability: Optional[List[AvailabilityStatus]]` - Availability filters

#### `SearchFilterPrice`
- `min_price: Optional[float]` - Minimum price
- `max_price: Optional[float]` - Maximum price

#### `Price`
- `price: float` - Current price
- `compare_at_price: Optional[float]` - Original price (if discounted)
- `currency: str` - Currency code

#### `AvailabilityStatus`
Enum with values: `IN_STOCK`, `OUT_OF_STOCK`, `PRE_ORDER`, `LIMITED_AVAILABILITY`, `BACK_ORDER`, `DISCONTINUED`, `SOLD_OUT`, `UNKNOWN`

## Error Handling

The SDK provides specific exception types for different error conditions:

```python
from channel3_sdk import (
    Channel3AuthenticationError,
    Channel3ValidationError,
    Channel3NotFoundError,
    Channel3ServerError,
    Channel3ConnectionError
)

try:
    products = client.search(query="shoes")
except Channel3AuthenticationError:
    print("Invalid API key")
except Channel3ValidationError as e:
    print(f"Invalid request: {e.message}")
except Channel3NotFoundError:
    print("Resource not found")
except Channel3ServerError:
    print("Server error - please try again later")
except Channel3ConnectionError:
    print("Connection error - check your internet connection")
```

## Environment Variables

- `CHANNEL3_API_KEY` - Your Channel3 API key

## Requirements

- Python 3.8+
- requests
- aiohttp
- pydantic

## License

MIT License
