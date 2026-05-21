# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from channel3_sdk import Channel3, AsyncChannel3
from channel3_sdk.types import (
    ProductDetail,
    LookupResponse,
)
from channel3_sdk.pagination import SyncSearchPage, AsyncSearchPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Channel3) -> None:
        product = client.products.retrieve(
            product_id="product_id",
        )
        assert_matches_type(ProductDetail, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Channel3) -> None:
        product = client.products.retrieve(
            product_id="product_id",
            country="US",
            currency="USD",
            language="en",
            website_ids=["string"],
        )
        assert_matches_type(ProductDetail, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Channel3) -> None:
        response = client.products.with_raw_response.retrieve(
            product_id="product_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductDetail, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Channel3) -> None:
        with client.products.with_streaming_response.retrieve(
            product_id="product_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductDetail, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Channel3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.with_raw_response.retrieve(
                product_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_similar(self, client: Channel3) -> None:
        product = client.products.find_similar(
            product_id="product_id",
        )
        assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_similar_with_all_params(self, client: Channel3) -> None:
        product = client.products.find_similar(
            product_id="product_id",
            config={
                "country": "US",
                "currency": "USD",
                "language": "en",
            },
            filters={
                "age": ["newborn"],
                "attributes": {"foo": ["string"]},
                "availability": ["InStock"],
                "brand_ids": ["string"],
                "category_ids": ["string"],
                "colors": {
                    "palette": [
                        {
                            "hex": "hex",
                            "percentage": 0,
                        }
                    ]
                },
                "condition": "new",
                "exclude_brand_ids": ["string"],
                "exclude_category_ids": ["string"],
                "exclude_website_ids": ["string"],
                "gender": "male",
                "price": {
                    "max_price": 0,
                    "min_price": 0,
                },
                "website_ids": ["string"],
            },
            limit=1,
            page_token="page_token",
        )
        assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_similar(self, client: Channel3) -> None:
        response = client.products.with_raw_response.find_similar(
            product_id="product_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_similar(self, client: Channel3) -> None:
        with client.products.with_streaming_response.find_similar(
            product_id="product_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup(self, client: Channel3) -> None:
        product = client.products.lookup(
            url="url",
        )
        assert_matches_type(LookupResponse, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_with_all_params(self, client: Channel3) -> None:
        product = client.products.lookup(
            url="url",
            max_staleness_hours=1,
        )
        assert_matches_type(LookupResponse, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup(self, client: Channel3) -> None:
        response = client.products.with_raw_response.lookup(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(LookupResponse, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup(self, client: Channel3) -> None:
        with client.products.with_streaming_response.lookup(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(LookupResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Channel3) -> None:
        product = client.products.search()
        assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Channel3) -> None:
        product = client.products.search(
            base64_image="base64_image",
            config={
                "country": "US",
                "currency": "USD",
                "keyword_search_only": True,
                "language": "en",
            },
            filters={
                "age": ["newborn"],
                "attributes": {"foo": ["string"]},
                "availability": ["InStock"],
                "brand_ids": ["string"],
                "category_ids": ["string"],
                "colors": {
                    "palette": [
                        {
                            "hex": "hex",
                            "percentage": 0,
                        }
                    ]
                },
                "condition": "new",
                "exclude_brand_ids": ["string"],
                "exclude_category_ids": ["string"],
                "exclude_website_ids": ["string"],
                "gender": "male",
                "price": {
                    "max_price": 0,
                    "min_price": 0,
                },
                "website_ids": ["string"],
            },
            image_url="image_url",
            limit=1,
            page_token="page_token",
            query="query",
        )
        assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Channel3) -> None:
        response = client.products.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Channel3) -> None:
        with client.products.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_by_image(self, client: Channel3) -> None:
        product = client.products.search_by_image()
        assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_by_image_with_all_params(self, client: Channel3) -> None:
        product = client.products.search_by_image(
            base64_image="base64_image",
            config={
                "country": "US",
                "currency": "USD",
                "language": "en",
            },
            filters={
                "age": ["newborn"],
                "attributes": {"foo": ["string"]},
                "availability": ["InStock"],
                "brand_ids": ["string"],
                "category_ids": ["string"],
                "colors": {
                    "palette": [
                        {
                            "hex": "hex",
                            "percentage": 0,
                        }
                    ]
                },
                "condition": "new",
                "exclude_brand_ids": ["string"],
                "exclude_category_ids": ["string"],
                "exclude_website_ids": ["string"],
                "gender": "male",
                "price": {
                    "max_price": 0,
                    "min_price": 0,
                },
                "website_ids": ["string"],
            },
            image_url="image_url",
            limit=1,
            page_token="page_token",
        )
        assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_by_image(self, client: Channel3) -> None:
        response = client.products.with_raw_response.search_by_image()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_by_image(self, client: Channel3) -> None:
        with client.products.with_streaming_response.search_by_image() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(SyncSearchPage[ProductDetail], product, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncChannel3) -> None:
        product = await async_client.products.retrieve(
            product_id="product_id",
        )
        assert_matches_type(ProductDetail, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncChannel3) -> None:
        product = await async_client.products.retrieve(
            product_id="product_id",
            country="US",
            currency="USD",
            language="en",
            website_ids=["string"],
        )
        assert_matches_type(ProductDetail, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncChannel3) -> None:
        response = await async_client.products.with_raw_response.retrieve(
            product_id="product_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductDetail, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncChannel3) -> None:
        async with async_client.products.with_streaming_response.retrieve(
            product_id="product_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductDetail, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncChannel3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.with_raw_response.retrieve(
                product_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_similar(self, async_client: AsyncChannel3) -> None:
        product = await async_client.products.find_similar(
            product_id="product_id",
        )
        assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_similar_with_all_params(self, async_client: AsyncChannel3) -> None:
        product = await async_client.products.find_similar(
            product_id="product_id",
            config={
                "country": "US",
                "currency": "USD",
                "language": "en",
            },
            filters={
                "age": ["newborn"],
                "attributes": {"foo": ["string"]},
                "availability": ["InStock"],
                "brand_ids": ["string"],
                "category_ids": ["string"],
                "colors": {
                    "palette": [
                        {
                            "hex": "hex",
                            "percentage": 0,
                        }
                    ]
                },
                "condition": "new",
                "exclude_brand_ids": ["string"],
                "exclude_category_ids": ["string"],
                "exclude_website_ids": ["string"],
                "gender": "male",
                "price": {
                    "max_price": 0,
                    "min_price": 0,
                },
                "website_ids": ["string"],
            },
            limit=1,
            page_token="page_token",
        )
        assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_similar(self, async_client: AsyncChannel3) -> None:
        response = await async_client.products.with_raw_response.find_similar(
            product_id="product_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_similar(self, async_client: AsyncChannel3) -> None:
        async with async_client.products.with_streaming_response.find_similar(
            product_id="product_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup(self, async_client: AsyncChannel3) -> None:
        product = await async_client.products.lookup(
            url="url",
        )
        assert_matches_type(LookupResponse, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_with_all_params(self, async_client: AsyncChannel3) -> None:
        product = await async_client.products.lookup(
            url="url",
            max_staleness_hours=1,
        )
        assert_matches_type(LookupResponse, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncChannel3) -> None:
        response = await async_client.products.with_raw_response.lookup(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(LookupResponse, product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncChannel3) -> None:
        async with async_client.products.with_streaming_response.lookup(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(LookupResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncChannel3) -> None:
        product = await async_client.products.search()
        assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncChannel3) -> None:
        product = await async_client.products.search(
            base64_image="base64_image",
            config={
                "country": "US",
                "currency": "USD",
                "keyword_search_only": True,
                "language": "en",
            },
            filters={
                "age": ["newborn"],
                "attributes": {"foo": ["string"]},
                "availability": ["InStock"],
                "brand_ids": ["string"],
                "category_ids": ["string"],
                "colors": {
                    "palette": [
                        {
                            "hex": "hex",
                            "percentage": 0,
                        }
                    ]
                },
                "condition": "new",
                "exclude_brand_ids": ["string"],
                "exclude_category_ids": ["string"],
                "exclude_website_ids": ["string"],
                "gender": "male",
                "price": {
                    "max_price": 0,
                    "min_price": 0,
                },
                "website_ids": ["string"],
            },
            image_url="image_url",
            limit=1,
            page_token="page_token",
            query="query",
        )
        assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncChannel3) -> None:
        response = await async_client.products.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncChannel3) -> None:
        async with async_client.products.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_by_image(self, async_client: AsyncChannel3) -> None:
        product = await async_client.products.search_by_image()
        assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_by_image_with_all_params(self, async_client: AsyncChannel3) -> None:
        product = await async_client.products.search_by_image(
            base64_image="base64_image",
            config={
                "country": "US",
                "currency": "USD",
                "language": "en",
            },
            filters={
                "age": ["newborn"],
                "attributes": {"foo": ["string"]},
                "availability": ["InStock"],
                "brand_ids": ["string"],
                "category_ids": ["string"],
                "colors": {
                    "palette": [
                        {
                            "hex": "hex",
                            "percentage": 0,
                        }
                    ]
                },
                "condition": "new",
                "exclude_brand_ids": ["string"],
                "exclude_category_ids": ["string"],
                "exclude_website_ids": ["string"],
                "gender": "male",
                "price": {
                    "max_price": 0,
                    "min_price": 0,
                },
                "website_ids": ["string"],
            },
            image_url="image_url",
            limit=1,
            page_token="page_token",
        )
        assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_by_image(self, async_client: AsyncChannel3) -> None:
        response = await async_client.products.with_raw_response.search_by_image()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_by_image(self, async_client: AsyncChannel3) -> None:
        async with async_client.products.with_streaming_response.search_by_image() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(AsyncSearchPage[ProductDetail], product, path=["response"])

        assert cast(Any, response.is_closed) is True
