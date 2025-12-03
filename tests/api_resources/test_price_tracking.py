# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from channel3_sdk import Channel3, AsyncChannel3
from channel3_sdk.types import (
    PriceHistory,
    Subscription,
    PaginatedSubscriptions,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPriceTracking:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_history(self, client: Channel3) -> None:
        price_tracking = client.price_tracking.get_history(
            canonical_product_id="canonical_product_id",
        )
        assert_matches_type(PriceHistory, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_history_with_all_params(self, client: Channel3) -> None:
        price_tracking = client.price_tracking.get_history(
            canonical_product_id="canonical_product_id",
            days=1,
        )
        assert_matches_type(PriceHistory, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_history(self, client: Channel3) -> None:
        response = client.price_tracking.with_raw_response.get_history(
            canonical_product_id="canonical_product_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_tracking = response.parse()
        assert_matches_type(PriceHistory, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_history(self, client: Channel3) -> None:
        with client.price_tracking.with_streaming_response.get_history(
            canonical_product_id="canonical_product_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_tracking = response.parse()
            assert_matches_type(PriceHistory, price_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_history(self, client: Channel3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `canonical_product_id` but received ''"):
            client.price_tracking.with_raw_response.get_history(
                canonical_product_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_subscriptions(self, client: Channel3) -> None:
        price_tracking = client.price_tracking.list_subscriptions()
        assert_matches_type(PaginatedSubscriptions, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_subscriptions_with_all_params(self, client: Channel3) -> None:
        price_tracking = client.price_tracking.list_subscriptions(
            limit=1,
            page_token="page_token",
        )
        assert_matches_type(PaginatedSubscriptions, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_subscriptions(self, client: Channel3) -> None:
        response = client.price_tracking.with_raw_response.list_subscriptions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_tracking = response.parse()
        assert_matches_type(PaginatedSubscriptions, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_subscriptions(self, client: Channel3) -> None:
        with client.price_tracking.with_streaming_response.list_subscriptions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_tracking = response.parse()
            assert_matches_type(PaginatedSubscriptions, price_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start(self, client: Channel3) -> None:
        price_tracking = client.price_tracking.start(
            canonical_product_id="canonical_product_id",
        )
        assert_matches_type(Subscription, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Channel3) -> None:
        response = client.price_tracking.with_raw_response.start(
            canonical_product_id="canonical_product_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_tracking = response.parse()
        assert_matches_type(Subscription, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Channel3) -> None:
        with client.price_tracking.with_streaming_response.start(
            canonical_product_id="canonical_product_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_tracking = response.parse()
            assert_matches_type(Subscription, price_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop(self, client: Channel3) -> None:
        price_tracking = client.price_tracking.stop(
            canonical_product_id="canonical_product_id",
        )
        assert_matches_type(Subscription, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: Channel3) -> None:
        response = client.price_tracking.with_raw_response.stop(
            canonical_product_id="canonical_product_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_tracking = response.parse()
        assert_matches_type(Subscription, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: Channel3) -> None:
        with client.price_tracking.with_streaming_response.stop(
            canonical_product_id="canonical_product_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_tracking = response.parse()
            assert_matches_type(Subscription, price_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPriceTracking:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_history(self, async_client: AsyncChannel3) -> None:
        price_tracking = await async_client.price_tracking.get_history(
            canonical_product_id="canonical_product_id",
        )
        assert_matches_type(PriceHistory, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_history_with_all_params(self, async_client: AsyncChannel3) -> None:
        price_tracking = await async_client.price_tracking.get_history(
            canonical_product_id="canonical_product_id",
            days=1,
        )
        assert_matches_type(PriceHistory, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_history(self, async_client: AsyncChannel3) -> None:
        response = await async_client.price_tracking.with_raw_response.get_history(
            canonical_product_id="canonical_product_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_tracking = await response.parse()
        assert_matches_type(PriceHistory, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_history(self, async_client: AsyncChannel3) -> None:
        async with async_client.price_tracking.with_streaming_response.get_history(
            canonical_product_id="canonical_product_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_tracking = await response.parse()
            assert_matches_type(PriceHistory, price_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_history(self, async_client: AsyncChannel3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `canonical_product_id` but received ''"):
            await async_client.price_tracking.with_raw_response.get_history(
                canonical_product_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_subscriptions(self, async_client: AsyncChannel3) -> None:
        price_tracking = await async_client.price_tracking.list_subscriptions()
        assert_matches_type(PaginatedSubscriptions, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_subscriptions_with_all_params(self, async_client: AsyncChannel3) -> None:
        price_tracking = await async_client.price_tracking.list_subscriptions(
            limit=1,
            page_token="page_token",
        )
        assert_matches_type(PaginatedSubscriptions, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_subscriptions(self, async_client: AsyncChannel3) -> None:
        response = await async_client.price_tracking.with_raw_response.list_subscriptions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_tracking = await response.parse()
        assert_matches_type(PaginatedSubscriptions, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_subscriptions(self, async_client: AsyncChannel3) -> None:
        async with async_client.price_tracking.with_streaming_response.list_subscriptions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_tracking = await response.parse()
            assert_matches_type(PaginatedSubscriptions, price_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncChannel3) -> None:
        price_tracking = await async_client.price_tracking.start(
            canonical_product_id="canonical_product_id",
        )
        assert_matches_type(Subscription, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncChannel3) -> None:
        response = await async_client.price_tracking.with_raw_response.start(
            canonical_product_id="canonical_product_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_tracking = await response.parse()
        assert_matches_type(Subscription, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncChannel3) -> None:
        async with async_client.price_tracking.with_streaming_response.start(
            canonical_product_id="canonical_product_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_tracking = await response.parse()
            assert_matches_type(Subscription, price_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncChannel3) -> None:
        price_tracking = await async_client.price_tracking.stop(
            canonical_product_id="canonical_product_id",
        )
        assert_matches_type(Subscription, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncChannel3) -> None:
        response = await async_client.price_tracking.with_raw_response.stop(
            canonical_product_id="canonical_product_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_tracking = await response.parse()
        assert_matches_type(Subscription, price_tracking, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncChannel3) -> None:
        async with async_client.price_tracking.with_streaming_response.stop(
            canonical_product_id="canonical_product_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_tracking = await response.parse()
            assert_matches_type(Subscription, price_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True
