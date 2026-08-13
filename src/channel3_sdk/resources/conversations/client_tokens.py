# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.conversations import client_token_create_params, client_token_revoke_params
from ...types.conversations.client_token_response import ClientTokenResponse

__all__ = ["ClientTokensResource", "AsyncClientTokensResource"]


class ClientTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ClientTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return ClientTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        conversation_id: Optional[str] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientTokenResponse:
        """Mint a short-lived, browser-safe client token for the conversations API.

        Pass
        `session_id` for a session token that can create and continue conversations for
        that session, or `conversation_id` for a token bound to one existing
        conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/conversations/client_tokens",
            body=maybe_transform(
                {
                    "conversation_id": conversation_id,
                    "session_id": session_id,
                    "ttl_seconds": ttl_seconds,
                },
                client_token_create_params.ClientTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientTokenResponse,
        )

    def revoke(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revoke a client token immediately.

        The token travels in the request body, not
        the URL, so it stays out of access logs; only the minting vendor can revoke it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/conversations/client_tokens/revoke",
            body=maybe_transform({"token": token}, client_token_revoke_params.ClientTokenRevokeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncClientTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncClientTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        conversation_id: Optional[str] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientTokenResponse:
        """Mint a short-lived, browser-safe client token for the conversations API.

        Pass
        `session_id` for a session token that can create and continue conversations for
        that session, or `conversation_id` for a token bound to one existing
        conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/conversations/client_tokens",
            body=await async_maybe_transform(
                {
                    "conversation_id": conversation_id,
                    "session_id": session_id,
                    "ttl_seconds": ttl_seconds,
                },
                client_token_create_params.ClientTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientTokenResponse,
        )

    async def revoke(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revoke a client token immediately.

        The token travels in the request body, not
        the URL, so it stays out of access logs; only the minting vendor can revoke it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/conversations/client_tokens/revoke",
            body=await async_maybe_transform({"token": token}, client_token_revoke_params.ClientTokenRevokeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ClientTokensResourceWithRawResponse:
    def __init__(self, client_tokens: ClientTokensResource) -> None:
        self._client_tokens = client_tokens

        self.create = to_raw_response_wrapper(
            client_tokens.create,
        )
        self.revoke = to_raw_response_wrapper(
            client_tokens.revoke,
        )


class AsyncClientTokensResourceWithRawResponse:
    def __init__(self, client_tokens: AsyncClientTokensResource) -> None:
        self._client_tokens = client_tokens

        self.create = async_to_raw_response_wrapper(
            client_tokens.create,
        )
        self.revoke = async_to_raw_response_wrapper(
            client_tokens.revoke,
        )


class ClientTokensResourceWithStreamingResponse:
    def __init__(self, client_tokens: ClientTokensResource) -> None:
        self._client_tokens = client_tokens

        self.create = to_streamed_response_wrapper(
            client_tokens.create,
        )
        self.revoke = to_streamed_response_wrapper(
            client_tokens.revoke,
        )


class AsyncClientTokensResourceWithStreamingResponse:
    def __init__(self, client_tokens: AsyncClientTokensResource) -> None:
        self._client_tokens = client_tokens

        self.create = async_to_streamed_response_wrapper(
            client_tokens.create,
        )
        self.revoke = async_to_streamed_response_wrapper(
            client_tokens.revoke,
        )
