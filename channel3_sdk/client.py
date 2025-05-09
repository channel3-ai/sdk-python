# channel3_sdk/client.py
import os
import requests
from typing import List, Optional, Dict, Any, Union


class Channel3Client:
    def __init__(self, api_key: str = None):
        """
        Initialize a Channel3 API client.

        The client provides methods to interact with Channel3's product search and retrieval API.

        Args:
            api_key: Your Channel3 API key. If not provided, will look for CHANNEL3_API_KEY in environment.

        Raises:
            ValueError: If no API key is provided and none is found in environment variables.

        Example:
            ```python
            # Initialize with explicit API key
            client = Channel3Client(api_key="your_api_key")

            # Or use environment variable
            # os.environ["CHANNEL3_API_KEY"] = "your_api_key"
            # client = Channel3Client()
            ```
        """
        self.api_key = api_key or os.getenv("CHANNEL3_API_KEY")
        if not self.api_key:
            raise ValueError("No API key provided for Channel3Client")
        self.headers = {"x-api-key": self.api_key}
        self.api_version = "v0"
        self.base_url = f"https://api.channel3.com/{self.api_version}"

    def search(
        self,
        query: Optional[str] = None,
        image_url: Optional[str] = None,
        base64_image: Optional[str] = None,
        filters: Optional[Dict[str, Any]] = None,
        limit: int = 20,
    ) -> List[Dict[str, Any]]:
        """
        Search for products using text query, image, or both with optional filters.

        Args:
            query: Text search query
            image_url: URL to an image to use for visual search
            base64_image: Base64-encoded image to use for visual search
            filters: Dict containing optional filters with these possible keys:
                - colors: List of color strings
                - materials: List of material strings
                - min_price: Minimum price (float)
                - max_price: Maximum price (float)
            limit: Maximum number of products to return (default: 20)

        Returns:
            List of product dictionaries containing:
                id, url, score, price, brand_id, brand_name, title, description, image_url, variants

        Examples:
            ```python
            # Text search
            products = client.search(query="blue denim jacket")

            # Image search
            products = client.search(image_url="https://example.com/image.jpg")

            # Multimodal search
            products = client.search(
                query="blue denim jacket",
                base64_image="data:image/jpeg;base64,...",
            )

            # Search with filters
            products = client.search(
                query="running shoes",
                filters={
                    "colors": ["black", "white"],
                    "min_price": 50.0,
                    "max_price": 150.0
                },
                limit=10
            )
            ```
        """
        payload = {
            "query": query,
            "image_url": image_url,
            "base64_image": base64_image,
            "limit": limit,
        }

        if filters:
            payload["filters"] = filters

        response = requests.post(
            f"{self.base_url}/search",
            json={k: v for k, v in payload.items() if v is not None},
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()

    def get_product(self, product_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific product by its ID.

        Args:
            product_id: The unique identifier of the product

        Returns:
            Dictionary containing detailed product information:
                url, brand_id, brand_name, title, description, image_urls, variants,
                price, gender, materials, key_features

        Raises:
            requests.HTTPError: If the product does not exist or other API errors occur

        Example:
            ```python
            product_detail = client.get_product("prod_123456")
            print(product_detail["title"])
            print(product_detail["price"]["price"])
            ```
        """
        response = requests.get(
            f"{self.base_url}/products/{product_id}",
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()
