# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from channel3_sdk import Channel3, AsyncChannel3
from channel3_sdk.types import (
    TurnResult,
    ConversationDetail,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Channel3) -> None:
        conversation = client.conversations.create(
            message={},
        )
        assert_matches_type(TurnResult, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Channel3) -> None:
        conversation = client.conversations.create(
            message={
                "parts": [
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
                "role": "user",
            },
            context={
                "application_context": "application_context",
                "user_context": "user_context",
            },
            conversation_id="conversation_id",
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
                    ],
                    "match": "strict",
                },
                "conditions": ["new"],
                "dimensions": {
                    "height": {
                        "unit": "mm",
                        "max": 0,
                        "min": 0,
                    },
                    "length": {
                        "unit": "mm",
                        "max": 0,
                        "min": 0,
                    },
                    "weight": {
                        "unit": "mg",
                        "max": 0,
                        "min": 0,
                    },
                    "width": {
                        "unit": "mm",
                        "max": 0,
                        "min": 0,
                    },
                },
                "exclude_brand_ids": ["string"],
                "exclude_category_ids": ["string"],
                "exclude_website_ids": ["string"],
                "gender": "male",
                "price": {
                    "max_price": 0,
                    "min_price": 0,
                },
                "sale": "on_sale",
                "website_ids": ["string"],
            },
            stream=True,
            x_user_id="x-user-id",
        )
        assert_matches_type(TurnResult, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Channel3) -> None:
        response = client.conversations.with_raw_response.create(
            message={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(TurnResult, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Channel3) -> None:
        with client.conversations.with_streaming_response.create(
            message={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(TurnResult, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Channel3) -> None:
        conversation = client.conversations.retrieve(
            conversation_id="conversation_id",
        )
        assert_matches_type(ConversationDetail, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Channel3) -> None:
        conversation = client.conversations.retrieve(
            conversation_id="conversation_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(ConversationDetail, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Channel3) -> None:
        response = client.conversations.with_raw_response.retrieve(
            conversation_id="conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationDetail, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Channel3) -> None:
        with client.conversations.with_streaming_response.retrieve(
            conversation_id="conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationDetail, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Channel3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.with_raw_response.retrieve(
                conversation_id="",
            )


class TestAsyncConversations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncChannel3) -> None:
        conversation = await async_client.conversations.create(
            message={},
        )
        assert_matches_type(TurnResult, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncChannel3) -> None:
        conversation = await async_client.conversations.create(
            message={
                "parts": [
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
                "role": "user",
            },
            context={
                "application_context": "application_context",
                "user_context": "user_context",
            },
            conversation_id="conversation_id",
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
                    ],
                    "match": "strict",
                },
                "conditions": ["new"],
                "dimensions": {
                    "height": {
                        "unit": "mm",
                        "max": 0,
                        "min": 0,
                    },
                    "length": {
                        "unit": "mm",
                        "max": 0,
                        "min": 0,
                    },
                    "weight": {
                        "unit": "mg",
                        "max": 0,
                        "min": 0,
                    },
                    "width": {
                        "unit": "mm",
                        "max": 0,
                        "min": 0,
                    },
                },
                "exclude_brand_ids": ["string"],
                "exclude_category_ids": ["string"],
                "exclude_website_ids": ["string"],
                "gender": "male",
                "price": {
                    "max_price": 0,
                    "min_price": 0,
                },
                "sale": "on_sale",
                "website_ids": ["string"],
            },
            stream=True,
            x_user_id="x-user-id",
        )
        assert_matches_type(TurnResult, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncChannel3) -> None:
        response = await async_client.conversations.with_raw_response.create(
            message={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(TurnResult, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncChannel3) -> None:
        async with async_client.conversations.with_streaming_response.create(
            message={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(TurnResult, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncChannel3) -> None:
        conversation = await async_client.conversations.retrieve(
            conversation_id="conversation_id",
        )
        assert_matches_type(ConversationDetail, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncChannel3) -> None:
        conversation = await async_client.conversations.retrieve(
            conversation_id="conversation_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(ConversationDetail, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncChannel3) -> None:
        response = await async_client.conversations.with_raw_response.retrieve(
            conversation_id="conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationDetail, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncChannel3) -> None:
        async with async_client.conversations.with_streaming_response.retrieve(
            conversation_id="conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationDetail, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncChannel3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.with_raw_response.retrieve(
                conversation_id="",
            )
