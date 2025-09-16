# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from public_sdk import PublicSDK, AsyncPublicSDK
from tests.utils import assert_matches_type
from public_sdk.types import Brand, BrandListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrands:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PublicSDK) -> None:
        brand = client.brands.retrieve(
            "brand_id",
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PublicSDK) -> None:
        response = client.brands.with_raw_response.retrieve(
            "brand_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PublicSDK) -> None:
        with client.brands.with_streaming_response.retrieve(
            "brand_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(Brand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PublicSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brands.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PublicSDK) -> None:
        brand = client.brands.list()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PublicSDK) -> None:
        brand = client.brands.list(
            page=0,
            query="query",
            size=0,
        )
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PublicSDK) -> None:
        response = client.brands.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PublicSDK) -> None:
        with client.brands.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandListResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBrands:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPublicSDK) -> None:
        brand = await async_client.brands.retrieve(
            "brand_id",
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPublicSDK) -> None:
        response = await async_client.brands.with_raw_response.retrieve(
            "brand_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPublicSDK) -> None:
        async with async_client.brands.with_streaming_response.retrieve(
            "brand_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(Brand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPublicSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brands.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPublicSDK) -> None:
        brand = await async_client.brands.list()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPublicSDK) -> None:
        brand = await async_client.brands.list(
            page=0,
            query="query",
            size=0,
        )
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPublicSDK) -> None:
        response = await async_client.brands.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPublicSDK) -> None:
        async with async_client.brands.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandListResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True
