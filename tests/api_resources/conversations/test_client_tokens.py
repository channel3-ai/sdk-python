# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from channel3_sdk import Channel3, AsyncChannel3
from channel3_sdk.types.conversations import ClientTokenResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClientTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Channel3) -> None:
        client_token = client.conversations.client_tokens.create()
        assert_matches_type(ClientTokenResponse, client_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Channel3) -> None:
        client_token = client.conversations.client_tokens.create(
            conversation_id="conversation_id",
            session_id="session_id",
            ttl_seconds=60,
        )
        assert_matches_type(ClientTokenResponse, client_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Channel3) -> None:
        response = client.conversations.client_tokens.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_token = response.parse()
        assert_matches_type(ClientTokenResponse, client_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Channel3) -> None:
        with client.conversations.client_tokens.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_token = response.parse()
            assert_matches_type(ClientTokenResponse, client_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: Channel3) -> None:
        client_token = client.conversations.client_tokens.revoke(
            token="token",
        )
        assert client_token is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Channel3) -> None:
        response = client.conversations.client_tokens.with_raw_response.revoke(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_token = response.parse()
        assert client_token is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Channel3) -> None:
        with client.conversations.client_tokens.with_streaming_response.revoke(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_token = response.parse()
            assert client_token is None

        assert cast(Any, response.is_closed) is True


class TestAsyncClientTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncChannel3) -> None:
        client_token = await async_client.conversations.client_tokens.create()
        assert_matches_type(ClientTokenResponse, client_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncChannel3) -> None:
        client_token = await async_client.conversations.client_tokens.create(
            conversation_id="conversation_id",
            session_id="session_id",
            ttl_seconds=60,
        )
        assert_matches_type(ClientTokenResponse, client_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncChannel3) -> None:
        response = await async_client.conversations.client_tokens.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_token = await response.parse()
        assert_matches_type(ClientTokenResponse, client_token, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncChannel3) -> None:
        async with async_client.conversations.client_tokens.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_token = await response.parse()
            assert_matches_type(ClientTokenResponse, client_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncChannel3) -> None:
        client_token = await async_client.conversations.client_tokens.revoke(
            token="token",
        )
        assert client_token is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncChannel3) -> None:
        response = await async_client.conversations.client_tokens.with_raw_response.revoke(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_token = await response.parse()
        assert client_token is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncChannel3) -> None:
        async with async_client.conversations.client_tokens.with_streaming_response.revoke(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_token = await response.parse()
            assert client_token is None

        assert cast(Any, response.is_closed) is True
