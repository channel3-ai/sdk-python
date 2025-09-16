# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from channel3_sdk import Channel3, AsyncChannel3
from channel3_sdk.types import SearchPerformResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_perform(self, client: Channel3) -> None:
        search = client.search.perform()
        assert_matches_type(SearchPerformResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_perform_with_all_params(self, client: Channel3) -> None:
        search = client.search.perform(
            base64_image="base64_image",
            config={
                "enrich_query": True,
                "semantic_search": True,
            },
            context="context",
            filters={
                "availability": ["InStock"],
                "brand_ids": ["string"],
                "gender": "male",
                "price": {
                    "max_price": 0,
                    "min_price": 0,
                },
            },
            image_url="image_url",
            limit=0,
            query="query",
        )
        assert_matches_type(SearchPerformResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_perform(self, client: Channel3) -> None:
        response = client.search.with_raw_response.perform()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchPerformResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_perform(self, client: Channel3) -> None:
        with client.search.with_streaming_response.perform() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchPerformResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_perform(self, async_client: AsyncChannel3) -> None:
        search = await async_client.search.perform()
        assert_matches_type(SearchPerformResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_perform_with_all_params(self, async_client: AsyncChannel3) -> None:
        search = await async_client.search.perform(
            base64_image="base64_image",
            config={
                "enrich_query": True,
                "semantic_search": True,
            },
            context="context",
            filters={
                "availability": ["InStock"],
                "brand_ids": ["string"],
                "gender": "male",
                "price": {
                    "max_price": 0,
                    "min_price": 0,
                },
            },
            image_url="image_url",
            limit=0,
            query="query",
        )
        assert_matches_type(SearchPerformResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_perform(self, async_client: AsyncChannel3) -> None:
        response = await async_client.search.with_raw_response.perform()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchPerformResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_perform(self, async_client: AsyncChannel3) -> None:
        async with async_client.search.with_streaming_response.perform() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchPerformResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
