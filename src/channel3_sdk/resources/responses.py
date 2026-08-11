# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import response_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.search_filters_param import SearchFiltersParam
from ..types.response_create_response import ResponseCreateResponse
from ..types.conversation_context_param import ConversationContextParam

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        attachments: Optional[Iterable[response_create_params.Attachment]] | Omit = omit,
        context: Optional[ConversationContextParam] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        debug: bool | Omit = omit,
        filters: Optional[SearchFiltersParam] | Omit = omit,
        image: Optional[response_create_params.Image] | Omit = omit,
        message: Optional[response_create_params.Message] | Omit = omit,
        messages: Iterable[response_create_params.Message] | Omit = omit,
        x_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ResponseCreateResponse]:
        """
        Run a shopping conversation turn.

        Args:
          context: Partner-supplied context pinned to the top of a conversation thread.

          filters: Search filters for the search API.

          x_user_id: Optional user identifier to attribute clicks and sales to a user in your system.
              Channel3 appends it to buy URLs in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-user-id": x_user_id}), **(extra_headers or {})}
        return self._post(
            "/v1/responses",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "context": context,
                    "conversation_id": conversation_id,
                    "debug": debug,
                    "filters": filters,
                    "image": image,
                    "message": message,
                    "messages": messages,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[ResponseCreateResponse],
        )


class AsyncResponsesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        attachments: Optional[Iterable[response_create_params.Attachment]] | Omit = omit,
        context: Optional[ConversationContextParam] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        debug: bool | Omit = omit,
        filters: Optional[SearchFiltersParam] | Omit = omit,
        image: Optional[response_create_params.Image] | Omit = omit,
        message: Optional[response_create_params.Message] | Omit = omit,
        messages: Iterable[response_create_params.Message] | Omit = omit,
        x_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ResponseCreateResponse]:
        """
        Run a shopping conversation turn.

        Args:
          context: Partner-supplied context pinned to the top of a conversation thread.

          filters: Search filters for the search API.

          x_user_id: Optional user identifier to attribute clicks and sales to a user in your system.
              Channel3 appends it to buy URLs in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-user-id": x_user_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/responses",
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "context": context,
                    "conversation_id": conversation_id,
                    "debug": debug,
                    "filters": filters,
                    "image": image,
                    "message": message,
                    "messages": messages,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[ResponseCreateResponse],
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
