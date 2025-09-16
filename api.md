# PublicSDK

Methods:

- <code title="get /">client.<a href="./src/public_sdk/_client.py">retrieve</a>() -> object</code>

# Search

Types:

```python
from public_sdk.types import SearchPerformResponse
```

Methods:

- <code title="post /v0/search">client.search.<a href="./src/public_sdk/resources/search.py">perform</a>(\*\*<a href="src/public_sdk/types/search_perform_params.py">params</a>) -> <a href="./src/public_sdk/types/search_perform_response.py">SearchPerformResponse</a></code>

# Products

Types:

```python
from public_sdk.types import AvailabilityStatus, Price, Variant, ProductRetrieveResponse
```

Methods:

- <code title="get /v0/products/{product_id}">client.products.<a href="./src/public_sdk/resources/products.py">retrieve</a>(product_id) -> <a href="./src/public_sdk/types/product_retrieve_response.py">ProductRetrieveResponse</a></code>

# Brands

Types:

```python
from public_sdk.types import Brand, BrandListResponse
```

Methods:

- <code title="get /v0/brands/{brand_id}">client.brands.<a href="./src/public_sdk/resources/brands.py">retrieve</a>(brand_id) -> <a href="./src/public_sdk/types/brand.py">Brand</a></code>
- <code title="get /v0/brands">client.brands.<a href="./src/public_sdk/resources/brands.py">list</a>(\*\*<a href="src/public_sdk/types/brand_list_params.py">params</a>) -> <a href="./src/public_sdk/types/brand_list_response.py">BrandListResponse</a></code>

# Enrich

Types:

```python
from public_sdk.types import EnrichEnrichURLResponse
```

Methods:

- <code title="post /v0/enrich">client.enrich.<a href="./src/public_sdk/resources/enrich.py">enrich_url</a>(\*\*<a href="src/public_sdk/types/enrich_enrich_url_params.py">params</a>) -> <a href="./src/public_sdk/types/enrich_enrich_url_response.py">EnrichEnrichURLResponse</a></code>
