# channel3_sdk/client.py
import os
import requests
from typing import List, Optional, Dict, Any, Union
import aiohttp
import asyncio
from pydantic import ValidationError

from .models import Product, ProductDetail, SearchFilters, SearchRequest, Brand
from .exceptions import (
    Channel3Error,
    Channel3AuthenticationError,
    Channel3ValidationError,
    Channel3NotFoundError,
    Channel3ServerError,
    Channel3ConnectionError,
)


class BaseChannel3Client:
    """Base client with common functionality."""

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize the base Channel3 client.

        Args:
            api_key: Your Channel3 API key. If not provided, will look for CHANNEL3_API_KEY in environment.
            base_url: Base URL for the API. Defaults to https://api.trychannel3.com/v0

        Raises:
            ValueError: If no API key is provided and none is found in environment variables.
        """
        self.api_key = api_key or os.getenv("CHANNEL3_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No API key provided. Set CHANNEL3_API_KEY environment variable or pass api_key parameter."
            )

        self.base_url = base_url or "https://api.trychannel3.com/v0"
        self.headers = {"x-api-key": self.api_key, "Content-Type": "application/json"}

    def _handle_error_response(
        self, status_code: int, response_data: Dict[str, Any], url: str
    ) -> None:
        """Handle error responses and raise appropriate exceptions."""
        error_message = response_data.get(
            "detail", f"Request failed with status {status_code}"
        )

        if status_code == 401:
            raise Channel3AuthenticationError(
                "Invalid or missing API key",
                status_code=status_code,
                response_data=response_data,
            )
        elif status_code == 404:
            raise Channel3NotFoundError(
                error_message, status_code=status_code, response_data=response_data
            )
        elif status_code == 422:
            raise Channel3ValidationError(
                f"Validation error: {error_message}",
                status_code=status_code,
                response_data=response_data,
            )
        elif status_code == 500:
            raise Channel3ServerError(
                "Internal server error",
                status_code=status_code,
                response_data=response_data,
            )
        else:
            raise Channel3Error(
                f"Request to {url} failed: {error_message}",
                status_code=status_code,
                response_data=response_data,
            )


class Channel3Client(BaseChannel3Client):
    """Synchronous Channel3 API client."""

    def search(
        self,
        query: Optional[str] = None,
        image_url: Optional[str] = None,
        base64_image: Optional[str] = None,
        filters: Optional[SearchFilters] = None,
        limit: int = 20,
    ) -> List[Product]:
        """
        Search for products using text query, image, or both with optional filters.

        Args:
            query: Text search query
            image_url: URL to an image to use for visual search
            base64_image: Base64-encoded image to use for visual search
            filters: Search filters (SearchFilters object)
            limit: Maximum number of products to return (default: 20)

        Returns:
            List of Product objects

        Raises:
            Channel3AuthenticationError: If API key is invalid
            Channel3ValidationError: If request parameters are invalid
            Channel3ServerError: If server encounters an error
            Channel3ConnectionError: If there are connection issues

        Examples:
            ```python
            # Text search
            products = client.search(query="blue denim jacket")

            # Image search
            products = client.search(image_url="https://example.com/image.jpg")

            # Multimodal search with filters
            from channel3_sdk.models import SearchFilters
            filters = SearchFilters(min_price=50.0, max_price=150.0)
            products = client.search(query="denim jacket", filters=filters)
            ```
        """
        # Build request payload
        search_request = SearchRequest(
            query=query,
            image_url=image_url,
            base64_image=base64_image,
            filters=filters,
            limit=limit,
        )

        url = f"{self.base_url}/search"

        try:
            response = requests.post(
                url,
                json=search_request.model_dump(exclude_none=True),
                headers=self.headers,
                timeout=30,
            )

            response_data = response.json()

            if response.status_code != 200:
                self._handle_error_response(response.status_code, response_data, url)

            # Parse and validate response
            return [Product(**item) for item in response_data]

        except requests.exceptions.ConnectionError as e:
            raise Channel3ConnectionError(
                f"Failed to connect to Channel3 API: {str(e)}"
            )
        except requests.exceptions.Timeout as e:
            raise Channel3ConnectionError(f"Request timed out: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise Channel3Error(f"Request failed: {str(e)}")
        except ValidationError as e:
            raise Channel3Error(f"Invalid response format: {str(e)}")

    def get_product(self, product_id: str) -> ProductDetail:
        """
        Get detailed information about a specific product by its ID.

        Args:
            product_id: The unique identifier of the product

        Returns:
            ProductDetail object with detailed product information

        Raises:
            Channel3AuthenticationError: If API key is invalid
            Channel3NotFoundError: If product is not found
            Channel3ValidationError: If product_id is invalid
            Channel3ServerError: If server encounters an error
            Channel3ConnectionError: If there are connection issues

        Example:
            ```python
            product_detail = client.get_product("prod_123456")
            print(f"Product: {product_detail.title}")
            print(f"Brand: {product_detail.brand_name}")
            ```
        """
        if not product_id or not product_id.strip():
            raise ValueError("product_id cannot be empty")

        url = f"{self.base_url}/products/{product_id}"

        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response_data = response.json()

            if response.status_code != 200:
                self._handle_error_response(response.status_code, response_data, url)

            # Parse and validate response
            return ProductDetail(**response_data)

        except requests.exceptions.ConnectionError as e:
            raise Channel3ConnectionError(
                f"Failed to connect to Channel3 API: {str(e)}"
            )
        except requests.exceptions.Timeout as e:
            raise Channel3ConnectionError(f"Request timed out: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise Channel3Error(f"Request failed: {str(e)}")
        except ValidationError as e:
            raise Channel3Error(f"Invalid response format: {str(e)}")

    def get_brands(
        self,
        query: Optional[str] = None,
        page: int = 1,
        size: int = 100,
    ) -> List[Brand]:
        """
        Get all brands that the vendor currently sells.

        Args:
            query: Optional text query to filter brands
            page: Page number for pagination (default: 1)
            size: Number of brands per page (default: 100)

        Returns:
            List of Brand objects

        Raises:
            Channel3AuthenticationError: If API key is invalid
            Channel3ValidationError: If request parameters are invalid
            Channel3ServerError: If server encounters an error
            Channel3ConnectionError: If there are connection issues

        Example:
            ```python
            brands = client.get_brands()
            for brand in brands:
                print(f"Brand: {brand.name}")
            ```
        """
        url = f"{self.base_url}/brands"
        params = {}

        if query is not None:
            params["query"] = query
        if page != 1:
            params["page"] = page
        if size != 100:
            params["size"] = size

        try:
            response = requests.get(
                url, headers=self.headers, params=params, timeout=30
            )
            response_data = response.json()

            if response.status_code != 200:
                self._handle_error_response(response.status_code, response_data, url)

            # Parse and validate response
            return [Brand(**item) for item in response_data]

        except requests.exceptions.ConnectionError as e:
            raise Channel3ConnectionError(
                f"Failed to connect to Channel3 API: {str(e)}"
            )
        except requests.exceptions.Timeout as e:
            raise Channel3ConnectionError(f"Request timed out: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise Channel3Error(f"Request failed: {str(e)}")
        except ValidationError as e:
            raise Channel3Error(f"Invalid response format: {str(e)}")

    def get_brand(self, brand_id: str) -> Brand:
        """
        Get detailed information for a specific brand by its ID.

        Args:
            brand_id: The unique identifier of the brand

        Returns:
            Brand object with detailed brand information

        Raises:
            Channel3AuthenticationError: If API key is invalid
            Channel3NotFoundError: If brand is not found
            Channel3ValidationError: If brand_id is invalid
            Channel3ServerError: If server encounters an error
            Channel3ConnectionError: If there are connection issues

        Example:
            ```python
            brand = client.get_brand("brand_123456")
            print(f"Brand: {brand.name}")
            print(f"Description: {brand.description}")
            ```
        """
        if not brand_id or not brand_id.strip():
            raise ValueError("brand_id cannot be empty")

        url = f"{self.base_url}/brands/{brand_id}"

        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response_data = response.json()

            if response.status_code != 200:
                self._handle_error_response(response.status_code, response_data, url)

            # Parse and validate response
            return Brand(**response_data)

        except requests.exceptions.ConnectionError as e:
            raise Channel3ConnectionError(
                f"Failed to connect to Channel3 API: {str(e)}"
            )
        except requests.exceptions.Timeout as e:
            raise Channel3ConnectionError(f"Request timed out: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise Channel3Error(f"Request failed: {str(e)}")
        except ValidationError as e:
            raise Channel3Error(f"Invalid response format: {str(e)}")


class AsyncChannel3Client(BaseChannel3Client):
    """Asynchronous Channel3 API client."""

    async def search(
        self,
        query: Optional[str] = None,
        image_url: Optional[str] = None,
        base64_image: Optional[str] = None,
        filters: Optional[Union[SearchFilters, Dict[str, Any]]] = None,
        limit: int = 20,
    ) -> List[Product]:
        """
        Search for products using text query, image, or both with optional filters.

        Args:
            query: Text search query
            image_url: URL to an image to use for visual search
            base64_image: Base64-encoded image to use for visual search
            filters: Search filters (SearchFilters object or dict)
            limit: Maximum number of products to return (default: 20)

        Returns:
            List of Product objects

        Raises:
            Channel3AuthenticationError: If API key is invalid
            Channel3ValidationError: If request parameters are invalid
            Channel3ServerError: If server encounters an error
            Channel3ConnectionError: If there are connection issues

        Examples:
            ```python
            # Text search
            products = await async_client.search(query="blue denim jacket")

            # Image search
            products = await async_client.search(image_url="https://example.com/image.jpg")
            ```
        """
        # Build request payload
        search_request = SearchRequest(
            query=query,
            image_url=image_url,
            base64_image=base64_image,
            filters=filters or SearchFilters(),
            limit=limit,
        )

        url = f"{self.base_url}/search"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url,
                    json=search_request.model_dump(exclude_none=True),
                    headers=self.headers,
                    timeout=aiohttp.ClientTimeout(total=30),
                ) as response:
                    response_data = await response.json()

                    if response.status != 200:
                        self._handle_error_response(response.status, response_data, url)

                    # Parse and validate response
                    return [Product(**item) for item in response_data]

        except aiohttp.ClientConnectionError as e:
            raise Channel3ConnectionError(
                f"Failed to connect to Channel3 API: {str(e)}"
            )
        except asyncio.TimeoutError as e:
            raise Channel3ConnectionError(f"Request timed out: {str(e)}")
        except aiohttp.ClientError as e:
            raise Channel3Error(f"Request failed: {str(e)}")
        except ValidationError as e:
            raise Channel3Error(f"Invalid response format: {str(e)}")

    async def get_product(self, product_id: str) -> ProductDetail:
        """
        Get detailed information about a specific product by its ID.

        Args:
            product_id: The unique identifier of the product

        Returns:
            ProductDetail object with detailed product information

        Raises:
            Channel3AuthenticationError: If API key is invalid
            Channel3NotFoundError: If product is not found
            Channel3ValidationError: If product_id is invalid
            Channel3ServerError: If server encounters an error
            Channel3ConnectionError: If there are connection issues

        Example:
            ```python
            product_detail = await async_client.get_product("prod_123456")
            print(f"Product: {product_detail.title}")
            ```
        """
        if not product_id or not product_id.strip():
            raise ValueError("product_id cannot be empty")

        url = f"{self.base_url}/products/{product_id}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    url, headers=self.headers, timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    response_data = await response.json()

                    if response.status != 200:
                        self._handle_error_response(response.status, response_data, url)

                    # Parse and validate response
                    return ProductDetail(**response_data)

        except aiohttp.ClientConnectionError as e:
            raise Channel3ConnectionError(
                f"Failed to connect to Channel3 API: {str(e)}"
            )
        except asyncio.TimeoutError as e:
            raise Channel3ConnectionError(f"Request timed out: {str(e)}")
        except aiohttp.ClientError as e:
            raise Channel3Error(f"Request failed: {str(e)}")
        except ValidationError as e:
            raise Channel3Error(f"Invalid response format: {str(e)}")

    async def get_brands(
        self,
        query: Optional[str] = None,
        page: int = 1,
        size: int = 100,
    ) -> List[Brand]:
        """
        Get all brands that the vendor currently sells.

        Args:
            query: Optional text query to filter brands
            page: Page number for pagination (default: 1)
            size: Number of brands per page (default: 100)

        Returns:
            List of Brand objects

        Raises:
            Channel3AuthenticationError: If API key is invalid
            Channel3ValidationError: If request parameters are invalid
            Channel3ServerError: If server encounters an error
            Channel3ConnectionError: If there are connection issues

        Example:
            ```python
            brands = await async_client.get_brands()
            for brand in brands:
                print(f"Brand: {brand.name}")
            ```
        """
        url = f"{self.base_url}/brands"
        params = {}

        if query is not None:
            params["query"] = query
        if page != 1:
            params["page"] = page
        if size != 100:
            params["size"] = size

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    url,
                    headers=self.headers,
                    params=params,
                    timeout=aiohttp.ClientTimeout(total=30),
                ) as response:
                    response_data = await response.json()

                    if response.status != 200:
                        self._handle_error_response(response.status, response_data, url)

                    # Parse and validate response
                    return [Brand(**item) for item in response_data]

        except aiohttp.ClientConnectionError as e:
            raise Channel3ConnectionError(
                f"Failed to connect to Channel3 API: {str(e)}"
            )
        except asyncio.TimeoutError as e:
            raise Channel3ConnectionError(f"Request timed out: {str(e)}")
        except aiohttp.ClientError as e:
            raise Channel3Error(f"Request failed: {str(e)}")
        except ValidationError as e:
            raise Channel3Error(f"Invalid response format: {str(e)}")

    async def get_brand(self, brand_id: str) -> Brand:
        """
        Get detailed information for a specific brand by its ID.

        Args:
            brand_id: The unique identifier of the brand

        Returns:
            Brand object with detailed brand information

        Raises:
            Channel3AuthenticationError: If API key is invalid
            Channel3NotFoundError: If brand is not found
            Channel3ValidationError: If brand_id is invalid
            Channel3ServerError: If server encounters an error
            Channel3ConnectionError: If there are connection issues

        Example:
            ```python
            brand = await async_client.get_brand("brand_123456")
            print(f"Brand: {brand.name}")
            print(f"Description: {brand.description}")
            ```
        """
        if not brand_id or not brand_id.strip():
            raise ValueError("brand_id cannot be empty")

        url = f"{self.base_url}/brands/{brand_id}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    url, headers=self.headers, timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    response_data = await response.json()

                    if response.status != 200:
                        self._handle_error_response(response.status, response_data, url)

                    # Parse and validate response
                    return Brand(**response_data)

        except aiohttp.ClientConnectionError as e:
            raise Channel3ConnectionError(
                f"Failed to connect to Channel3 API: {str(e)}"
            )
        except asyncio.TimeoutError as e:
            raise Channel3ConnectionError(f"Request timed out: {str(e)}")
        except aiohttp.ClientError as e:
            raise Channel3Error(f"Request failed: {str(e)}")
        except ValidationError as e:
            raise Channel3Error(f"Invalid response format: {str(e)}")
