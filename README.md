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
    print(f"Price: ${product.offers[0].price.price}")
    print("---")

# Get detailed product information
product_detail = client.get_product("prod_123456")
print(f"Detailed info for: {product_detail.title}")
print(f"Materials: {product_detail.materials}")
print(f"Key features: {product_detail.key_features}")
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
    
    # Get detailed product information
    if products:
        product_detail = await client.get_product(products[0].id)
        print(f"Gender: {product_detail.gender}")

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
from channel3_sdk import SearchFilters

# Create search filters
filters = SearchFilters(
    colors=["blue", "navy"],
    materials=["cotton", "denim"],
    min_price=50.0,
    max_price=200.0
)

# Search with filters
products = client.search(
    query="jacket",
    filters=filters,
    limit=10
)
```

## API Reference

### Client Classes

#### `Channel3Client`
Synchronous client for the Channel3 API.

**Methods:**
- `search(query=None, image_url=None, base64_image=None, filters=None, limit=20)` → `List[Product]`
- `get_product(product_id)` → `ProductDetail`

#### `AsyncChannel3Client` 
Asynchronous client for the Channel3 API.

**Methods:**
- `async search(query=None, image_url=None, base64_image=None, filters=None, limit=20)` → `List[Product]`
- `async get_product(product_id)` → `ProductDetail`

### Models

#### `Product`
- `id: str` - Unique product identifier
- `score: float` - Search relevance score
- `brand_name: str` - Brand name
- `title: str` - Product title
- `description: str` - Product description
- `image_url: str` - Main product image URL
- `offers: List[MerchantOffering]` - Available purchase options
- `family: List[FamilyMember]` - Related products

#### `ProductDetail`
- `brand_id: str` - Brand identifier
- `brand_name: str` - Brand name
- `title: str` - Product title
- `description: str` - Product description
- `image_urls: List[str]` - Product image URLs
- `merchant_offerings: List[MerchantOffering]` - Purchase options
- `gender: Literal["na", "men", "women"]` - Target gender
- `materials: Optional[List[str]]` - Product materials
- `key_features: List[str]` - Key product features
- `family_members: List[FamilyMember]` - Related products

#### `SearchFilters`
- `colors: Optional[List[str]]` - Color filters
- `materials: Optional[List[str]]` - Material filters
- `min_price: Optional[float]` - Minimum price
- `max_price: Optional[float]` - Maximum price

#### `MerchantOffering`
- `url: str` - Purchase URL
- `merchant_name: str` - Merchant name
- `price: Price` - Price information
- `availability: AvailabilityStatus` - Availability status

#### `Price`
- `price: float` - Current price
- `compare_at_price: Optional[float]` - Original price (if discounted)
- `currency: str` - Currency code

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
