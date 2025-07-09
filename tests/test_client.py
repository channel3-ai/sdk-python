"""Tests for the Channel3 SDK client."""

import pytest
from unittest.mock import Mock, patch, AsyncMock
import json

from channel3_sdk import (
    Channel3Client,
    AsyncChannel3Client,
    Product,
    ProductDetail,
    SearchFilters,
    Brand,
    Channel3AuthenticationError,
    Channel3NotFoundError,
)


class TestChannel3Client:
    """Tests for the synchronous client."""

    def test_client_initialization_with_api_key(self):
        """Test client initialization with explicit API key."""
        client = Channel3Client(api_key="test_key")
        assert client.api_key == "test_key"
        assert "x-api-key" in client.headers
        assert client.headers["x-api-key"] == "test_key"

    def test_client_initialization_without_api_key_raises_error(self):
        """Test that missing API key raises ValueError."""
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="No API key provided"):
                Channel3Client()

    @patch.dict("os.environ", {"CHANNEL3_API_KEY": "env_key"})
    def test_client_initialization_from_env(self):
        """Test client initialization from environment variable."""
        client = Channel3Client()
        assert client.api_key == "env_key"

    @patch("requests.post")
    def test_search_success(self, mock_post):
        """Test successful search request."""
        # Mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "id": "prod_123",
                "score": 0.95,
                "title": "Test Product",
                "description": "Test Description",
                "brand_name": "Test Brand",
                "image_url": "https://example.com/image.jpg",
                "price": {"price": 99.99, "currency": "USD"},
                "availability": "InStock",
                "variants": [],
            }
        ]
        mock_post.return_value = mock_response

        client = Channel3Client(api_key="test_key")
        products = client.search(query="test")

        assert len(products) == 1
        assert isinstance(products[0], Product)
        assert products[0].id == "prod_123"
        assert products[0].brand_name == "Test Brand"

    @patch("requests.post")
    def test_search_with_filters(self, mock_post):
        """Test search with filters."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_post.return_value = mock_response

        client = Channel3Client(api_key="test_key")
        filters = SearchFilters(brand_ids=["brand_123"], gender="male")

        client.search(query="test", filters=filters)

        # Verify the request was made with filters
        call_args = mock_post.call_args
        request_data = call_args[1]["json"]
        assert "filters" in request_data
        assert request_data["filters"]["brand_ids"] == ["brand_123"]
        assert request_data["filters"]["gender"] == "male"

    @patch("requests.get")
    def test_get_product_success(self, mock_get):
        """Test successful get product request."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "title": "Test Product",
            "description": "Test Description",
            "brand_id": "brand_123",
            "brand_name": "Test Brand",
            "image_urls": ["https://example.com/image.jpg"],
            "price": {"price": 99.99, "currency": "USD"},
            "availability": "InStock",
            "key_features": ["comfortable"],
            "variants": [],
        }
        mock_get.return_value = mock_response

        client = Channel3Client(api_key="test_key")
        product = client.get_product("prod_123")

        assert isinstance(product, ProductDetail)
        assert product.brand_id == "brand_123"
        assert product.title == "Test Product"

    @patch("requests.get")
    def test_get_brands_success(self, mock_get):
        """Test successful get brands request."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "id": "brand_123",
                "name": "Test Brand",
                "logo_url": "https://example.com/logo.jpg",
                "description": "Test brand description",
            }
        ]
        mock_get.return_value = mock_response

        client = Channel3Client(api_key="test_key")
        brands = client.get_brands()

        assert len(brands) == 1
        assert isinstance(brands[0], Brand)
        assert brands[0].id == "brand_123"
        assert brands[0].name == "Test Brand"

    @patch("requests.get")
    def test_get_brand_success(self, mock_get):
        """Test successful get brand request."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "brand_123",
            "name": "Test Brand",
            "logo_url": "https://example.com/logo.jpg",
            "description": "Test brand description",
        }
        mock_get.return_value = mock_response

        client = Channel3Client(api_key="test_key")
        brand = client.get_brand("brand_123")

        assert isinstance(brand, Brand)
        assert brand.id == "brand_123"
        assert brand.name == "Test Brand"

    @patch("requests.post")
    def test_authentication_error(self, mock_post):
        """Test authentication error handling."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"detail": "Invalid API key"}
        mock_post.return_value = mock_response

        client = Channel3Client(api_key="invalid_key")

        with pytest.raises(Channel3AuthenticationError):
            client.search(query="test")

    @patch("requests.get")
    def test_not_found_error(self, mock_get):
        """Test not found error handling."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"detail": "Product not found"}
        mock_get.return_value = mock_response

        client = Channel3Client(api_key="test_key")

        with pytest.raises(Channel3NotFoundError):
            client.get_product("nonexistent")

    def test_empty_product_id_raises_error(self):
        """Test that empty product ID raises ValueError."""
        client = Channel3Client(api_key="test_key")

        with pytest.raises(ValueError, match="product_id cannot be empty"):
            client.get_product("")

    def test_empty_brand_id_raises_error(self):
        """Test that empty brand ID raises ValueError."""
        client = Channel3Client(api_key="test_key")

        with pytest.raises(ValueError, match="brand_id cannot be empty"):
            client.get_brand("")


class TestAsyncChannel3Client:
    """Tests for the asynchronous client."""

    def test_async_client_initialization_with_api_key(self):
        """Test async client initialization with explicit API key."""
        client = AsyncChannel3Client(api_key="test_key")
        assert client.api_key == "test_key"
        assert "x-api-key" in client.headers
        assert client.headers["x-api-key"] == "test_key"

    def test_async_client_initialization_without_api_key_raises_error(self):
        """Test that missing API key raises ValueError."""
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="No API key provided"):
                AsyncChannel3Client()

    def test_async_empty_product_id_raises_error(self):
        """Test that empty product ID raises ValueError."""
        client = AsyncChannel3Client(api_key="test_key")

        with pytest.raises(ValueError, match="product_id cannot be empty"):
            # We can test this without making actual async calls
            import asyncio

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                loop.run_until_complete(client.get_product(""))
            finally:
                loop.close()

    def test_async_empty_brand_id_raises_error(self):
        """Test that empty brand ID raises ValueError."""
        client = AsyncChannel3Client(api_key="test_key")

        with pytest.raises(ValueError, match="brand_id cannot be empty"):
            # We can test this without making actual async calls
            import asyncio

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                loop.run_until_complete(client.get_brand(""))
            finally:
                loop.close()
