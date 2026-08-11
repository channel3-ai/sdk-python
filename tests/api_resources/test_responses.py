# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from channel3_sdk import Channel3, AsyncChannel3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Channel3) -> None:
        response_stream = client.responses.create()
        response_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Channel3) -> None:
        response_stream = client.responses.create(
            attachments=[
                {
                    "url": "url",
                    "key": "key",
                }
            ],
            context={
                "application_context": "application_context",
                "user_context": "user_context",
            },
            conversation_id="conversation_id",
            debug=True,
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
            image={
                "base64": "base64",
                "url": "url",
            },
            message={
                "role": "role",
                "parts": [
                    {
                        "type": "text",
                        "input": {"foo": "bar"},
                        "model_only": True,
                        "output": {"foo": "bar"},
                        "suggested_replies": ["string"],
                        "text": "text",
                        "tool_call_id": "toolCallId",
                        "tool_name": "toolName",
                        "url": "url",
                    }
                ],
            },
            messages=[
                {
                    "role": "role",
                    "parts": [
                        {
                            "type": "text",
                            "input": {"foo": "bar"},
                            "model_only": True,
                            "output": {"foo": "bar"},
                            "suggested_replies": ["string"],
                            "text": "text",
                            "tool_call_id": "toolCallId",
                            "tool_name": "toolName",
                            "url": "url",
                        }
                    ],
                }
            ],
            x_user_id="x-user-id",
        )
        response_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Channel3) -> None:
        response = client.responses.with_raw_response.create()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Channel3) -> None:
        with client.responses.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncChannel3) -> None:
        response_stream = await async_client.responses.create()
        await response_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncChannel3) -> None:
        response_stream = await async_client.responses.create(
            attachments=[
                {
                    "url": "url",
                    "key": "key",
                }
            ],
            context={
                "application_context": "application_context",
                "user_context": "user_context",
            },
            conversation_id="conversation_id",
            debug=True,
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
            image={
                "base64": "base64",
                "url": "url",
            },
            message={
                "role": "role",
                "parts": [
                    {
                        "type": "text",
                        "input": {"foo": "bar"},
                        "model_only": True,
                        "output": {"foo": "bar"},
                        "suggested_replies": ["string"],
                        "text": "text",
                        "tool_call_id": "toolCallId",
                        "tool_name": "toolName",
                        "url": "url",
                    }
                ],
            },
            messages=[
                {
                    "role": "role",
                    "parts": [
                        {
                            "type": "text",
                            "input": {"foo": "bar"},
                            "model_only": True,
                            "output": {"foo": "bar"},
                            "suggested_replies": ["string"],
                            "text": "text",
                            "tool_call_id": "toolCallId",
                            "tool_name": "toolName",
                            "url": "url",
                        }
                    ],
                }
            ],
            x_user_id="x-user-id",
        )
        await response_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncChannel3) -> None:
        response = await async_client.responses.with_raw_response.create()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncChannel3) -> None:
        async with async_client.responses.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
