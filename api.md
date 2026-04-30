# Shared Types

```python
from channel3_sdk.types import ErrorResponse
```

# Products

Types:

```python
from channel3_sdk.types import (
    AvailabilityStatus,
    ImageSearchRequest,
    LocaleConfig,
    LookupRequest,
    LookupResponse,
    Price,
    ProductBrand,
    ProductDetail,
    ProductImage,
    ProductOffer,
    SimilarProductsRequest,
)
```

Methods:

- <code title="get /v1/products/{product_id}">client.products.<a href="./src/channel3_sdk/resources/products.py">retrieve</a>(product_id, \*\*<a href="src/channel3_sdk/types/product_retrieve_params.py">params</a>) -> <a href="./src/channel3_sdk/types/product_detail.py">ProductDetail</a></code>
- <code title="post /v1/similar">client.products.<a href="./src/channel3_sdk/resources/products.py">find_similar</a>(\*\*<a href="src/channel3_sdk/types/product_find_similar_params.py">params</a>) -> <a href="./src/channel3_sdk/types/product_detail.py">SyncSearchPage[ProductDetail]</a></code>
- <code title="post /v1/lookup">client.products.<a href="./src/channel3_sdk/resources/products.py">lookup</a>(\*\*<a href="src/channel3_sdk/types/product_lookup_params.py">params</a>) -> <a href="./src/channel3_sdk/types/lookup_response.py">LookupResponse</a></code>
- <code title="post /v1/search">client.products.<a href="./src/channel3_sdk/resources/products.py">search</a>(\*\*<a href="src/channel3_sdk/types/product_search_params.py">params</a>) -> <a href="./src/channel3_sdk/types/product_detail.py">SyncSearchPage[ProductDetail]</a></code>
- <code title="post /v1/image-search">client.products.<a href="./src/channel3_sdk/resources/products.py">search_by_image</a>(\*\*<a href="src/channel3_sdk/types/product_search_by_image_params.py">params</a>) -> <a href="./src/channel3_sdk/types/product_detail.py">SyncSearchPage[ProductDetail]</a></code>

# Brands

Types:

```python
from channel3_sdk.types import Brand, SearchBrandsResponse
```

Methods:

- <code title="get /v1/brands/{brand_id}">client.brands.<a href="./src/channel3_sdk/resources/brands.py">retrieve</a>(brand_id) -> <a href="./src/channel3_sdk/types/brand.py">Brand</a></code>
- <code title="get /v1/brands">client.brands.<a href="./src/channel3_sdk/resources/brands.py">list</a>(\*\*<a href="src/channel3_sdk/types/brand_list_params.py">params</a>) -> <a href="./src/channel3_sdk/types/brand.py">SyncCursorPage[Brand]</a></code>
- <code title="get /v0/brands">client.brands.<a href="./src/channel3_sdk/resources/brands.py">find</a>(\*\*<a href="src/channel3_sdk/types/brand_find_params.py">params</a>) -> <a href="./src/channel3_sdk/types/brand.py">Brand</a></code>
- <code title="get /v1/brands/search">client.brands.<a href="./src/channel3_sdk/resources/brands.py">search</a>(\*\*<a href="src/channel3_sdk/types/brand_search_params.py">params</a>) -> <a href="./src/channel3_sdk/types/search_brands_response.py">SearchBrandsResponse</a></code>

# Categories

Types:

```python
from channel3_sdk.types import (
    Category,
    CategoryAttribute,
    CategoryRef,
    CategorySummary,
    PaginatedListCategoriesResponse,
    SearchCategoriesResponse,
)
```

Methods:

- <code title="get /v1/categories/{slug}">client.categories.<a href="./src/channel3_sdk/resources/categories.py">retrieve</a>(slug) -> <a href="./src/channel3_sdk/types/category.py">Category</a></code>
- <code title="get /v1/categories">client.categories.<a href="./src/channel3_sdk/resources/categories.py">list</a>(\*\*<a href="src/channel3_sdk/types/category_list_params.py">params</a>) -> <a href="./src/channel3_sdk/types/category_summary.py">SyncCategoryPage[CategorySummary]</a></code>
- <code title="get /v1/categories/search">client.categories.<a href="./src/channel3_sdk/resources/categories.py">search</a>(\*\*<a href="src/channel3_sdk/types/category_search_params.py">params</a>) -> <a href="./src/channel3_sdk/types/search_categories_response.py">SearchCategoriesResponse</a></code>

# Websites

Types:

```python
from channel3_sdk.types import Website
```

Methods:

- <code title="get /v0/websites">client.websites.<a href="./src/channel3_sdk/resources/websites.py">retrieve</a>(\*\*<a href="src/channel3_sdk/types/website_retrieve_params.py">params</a>) -> <a href="./src/channel3_sdk/types/website.py">Optional[Website]</a></code>

# PriceTracking

Types:

```python
from channel3_sdk.types import (
    PaginatedSubscriptionsResponse,
    PriceHistory,
    PriceHistoryPoint,
    PriceStatistics,
    StartTrackingRequest,
    StopTrackingRequest,
    Subscription,
    History,
    Statistics,
)
```

Methods:

- <code title="get /v0/price-tracking/subscriptions">client.price_tracking.<a href="./src/channel3_sdk/resources/price_tracking.py">list_subscriptions</a>(\*\*<a href="src/channel3_sdk/types/price_tracking_list_subscriptions_params.py">params</a>) -> <a href="./src/channel3_sdk/types/subscription.py">SyncCursorPage[Subscription]</a></code>
- <code title="get /v0/price-tracking/history/{canonical_product_id}">client.price_tracking.<a href="./src/channel3_sdk/resources/price_tracking.py">retrieve_history</a>(canonical_product_id, \*\*<a href="src/channel3_sdk/types/price_tracking_retrieve_history_params.py">params</a>) -> <a href="./src/channel3_sdk/types/price_history.py">PriceHistory</a></code>
- <code title="post /v0/price-tracking/start">client.price_tracking.<a href="./src/channel3_sdk/resources/price_tracking.py">start</a>(\*\*<a href="src/channel3_sdk/types/price_tracking_start_params.py">params</a>) -> <a href="./src/channel3_sdk/types/subscription.py">Subscription</a></code>
- <code title="post /v0/price-tracking/stop">client.price_tracking.<a href="./src/channel3_sdk/resources/price_tracking.py">stop</a>(\*\*<a href="src/channel3_sdk/types/price_tracking_stop_params.py">params</a>) -> <a href="./src/channel3_sdk/types/subscription.py">Subscription</a></code>

# Search

Types:

```python
from channel3_sdk.types import (
    SearchConfig,
    SearchFilterPrice,
    SearchFilters,
    SearchRequest,
    SearchResponse,
)
```

Methods:

- <code title="post /v1/search">client.search.<a href="./src/channel3_sdk/resources/search.py">perform</a>(\*\*<a href="src/channel3_sdk/types/search_perform_params.py">params</a>) -> <a href="./src/channel3_sdk/types/search_response.py">SearchResponse</a></code>

# Enrich

Types:

```python
from channel3_sdk.types import EnrichRequest, EnrichEnrichURLResponse
```

Methods:

- <code title="post /v0/enrich">client.enrich.<a href="./src/channel3_sdk/resources/enrich.py">enrich_url</a>(\*\*<a href="src/channel3_sdk/types/enrich_enrich_url_params.py">params</a>) -> <a href="./src/channel3_sdk/types/enrich_enrich_url_response.py">EnrichEnrichURLResponse</a></code>
