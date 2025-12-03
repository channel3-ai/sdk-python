# Search

Types:

```python
from channel3_sdk.types import (
    RedirectMode,
    SearchConfig,
    SearchFilterPrice,
    SearchFilters,
    SearchRequest,
    SearchPerformResponse,
)
```

Methods:

- <code title="post /v0/search">client.search.<a href="./src/channel3_sdk/resources/search.py">perform</a>(\*\*<a href="src/channel3_sdk/types/search_perform_params.py">params</a>) -> <a href="./src/channel3_sdk/types/search_perform_response.py">SearchPerformResponse</a></code>

# Products

Types:

```python
from channel3_sdk.types import AvailabilityStatus, Price, Product, ProductDetail, Variant
```

Methods:

- <code title="get /v0/products/{product_id}">client.products.<a href="./src/channel3_sdk/resources/products.py">retrieve</a>(product_id) -> <a href="./src/channel3_sdk/types/product_detail.py">ProductDetail</a></code>

# Brands

Types:

```python
from channel3_sdk.types import Brand
```

Methods:

- <code title="get /v0/brands">client.brands.<a href="./src/channel3_sdk/resources/brands.py">find</a>(\*\*<a href="src/channel3_sdk/types/brand_find_params.py">params</a>) -> <a href="./src/channel3_sdk/types/brand.py">Brand</a></code>

# Websites

Types:

```python
from channel3_sdk.types import Website
```

Methods:

- <code title="get /v0/websites">client.websites.<a href="./src/channel3_sdk/resources/websites.py">find</a>(\*\*<a href="src/channel3_sdk/types/website_find_params.py">params</a>) -> <a href="./src/channel3_sdk/types/website.py">Optional[Website]</a></code>

# Enrich

Types:

```python
from channel3_sdk.types import EnrichRequest
```

Methods:

- <code title="post /v0/enrich">client.enrich.<a href="./src/channel3_sdk/resources/enrich.py">enrich_url</a>(\*\*<a href="src/channel3_sdk/types/enrich_enrich_url_params.py">params</a>) -> <a href="./src/channel3_sdk/types/product_detail.py">ProductDetail</a></code>

# PriceTracking

Types:

```python
from channel3_sdk.types import PaginatedSubscriptions, PriceHistory, Subscription
```

Methods:

- <code title="get /v0/price-tracking/history/{canonical_product_id}">client.price_tracking.<a href="./src/channel3_sdk/resources/price_tracking.py">get_history</a>(canonical_product_id, \*\*<a href="src/channel3_sdk/types/price_tracking_get_history_params.py">params</a>) -> <a href="./src/channel3_sdk/types/price_history.py">PriceHistory</a></code>
- <code title="get /v0/price-tracking/subscriptions">client.price_tracking.<a href="./src/channel3_sdk/resources/price_tracking.py">list_subscriptions</a>(\*\*<a href="src/channel3_sdk/types/price_tracking_list_subscriptions_params.py">params</a>) -> <a href="./src/channel3_sdk/types/paginated_subscriptions.py">PaginatedSubscriptions</a></code>
- <code title="post /v0/price-tracking/start">client.price_tracking.<a href="./src/channel3_sdk/resources/price_tracking.py">start</a>(\*\*<a href="src/channel3_sdk/types/price_tracking_start_params.py">params</a>) -> <a href="./src/channel3_sdk/types/subscription.py">Subscription</a></code>
- <code title="post /v0/price-tracking/stop">client.price_tracking.<a href="./src/channel3_sdk/resources/price_tracking.py">stop</a>(\*\*<a href="src/channel3_sdk/types/price_tracking_stop_params.py">params</a>) -> <a href="./src/channel3_sdk/types/subscription.py">Subscription</a></code>
