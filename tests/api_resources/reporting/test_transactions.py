# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from channel3_sdk import Channel3, AsyncChannel3
from channel3_sdk._utils import parse_datetime
from channel3_sdk.pagination import SyncAnalyticsPage, AsyncAnalyticsPage
from channel3_sdk.types.reporting import Transaction

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Channel3) -> None:
        transaction = client.reporting.transactions.list()
        assert_matches_type(SyncAnalyticsPage[Transaction], transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Channel3) -> None:
        transaction = client.reporting.transactions.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            page=1,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncAnalyticsPage[Transaction], transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Channel3) -> None:
        response = client.reporting.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(SyncAnalyticsPage[Transaction], transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Channel3) -> None:
        with client.reporting.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(SyncAnalyticsPage[Transaction], transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncChannel3) -> None:
        transaction = await async_client.reporting.transactions.list()
        assert_matches_type(AsyncAnalyticsPage[Transaction], transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncChannel3) -> None:
        transaction = await async_client.reporting.transactions.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            page=1,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncAnalyticsPage[Transaction], transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncChannel3) -> None:
        response = await async_client.reporting.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(AsyncAnalyticsPage[Transaction], transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncChannel3) -> None:
        async with async_client.reporting.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(AsyncAnalyticsPage[Transaction], transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
