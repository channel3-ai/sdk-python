# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    conversation_create_params,
    conversation_retrieve_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.turn_result import TurnResult
from ..types.user_message_param import UserMessageParam
from ..types.conversation_detail import ConversationDetail
from ..types.search_filters_param import SearchFiltersParam
from ..types.conversation_context_param import ConversationContextParam

__all__ = ["ConversationsResource", "AsyncConversationsResource"]


class ConversationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        message: UserMessageParam,
        context: Optional[ConversationContextParam] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        filters: Optional[SearchFiltersParam] | Omit = omit,
        stream: bool | Omit = omit,
        x_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TurnResult:
        """Run one conversation turn.

        Omit `conversation_id` to create the thread with this
        turn; pass it to continue an existing thread.

        Args:
          context: Partner-supplied context pinned to the top of a conversation thread.

          conversation_id: Existing thread to continue; when omitted, a new thread is created.

          filters: Search filters for the search API.

          stream: Stream turn events over SSE (default) or return the assembled turn as JSON.

          x_user_id: Optional user identifier to attribute clicks and sales to a user in your system.
              Channel3 appends it to buy URLs in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-user-id": x_user_id}), **(extra_headers or {})}
        return self._post(
            "/v1/conversations",
            body=maybe_transform(
                {
                    "message": message,
                    "context": context,
                    "conversation_id": conversation_id,
                    "filters": filters,
                    "stream": stream,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TurnResult,
        )

    def retrieve(
        self,
        conversation_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationDetail:
        """Thread metadata plus one page of its message history.

        Paginate `items` with
        `limit` and `cursor`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            path_template("/v1/conversations/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    conversation_retrieve_params.ConversationRetrieveParams,
                ),
            ),
            cast_to=ConversationDetail,
        )


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        message: UserMessageParam,
        context: Optional[ConversationContextParam] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        filters: Optional[SearchFiltersParam] | Omit = omit,
        stream: bool | Omit = omit,
        x_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TurnResult:
        """Run one conversation turn.

        Omit `conversation_id` to create the thread with this
        turn; pass it to continue an existing thread.

        Args:
          context: Partner-supplied context pinned to the top of a conversation thread.

          conversation_id: Existing thread to continue; when omitted, a new thread is created.

          filters: Search filters for the search API.

          stream: Stream turn events over SSE (default) or return the assembled turn as JSON.

          x_user_id: Optional user identifier to attribute clicks and sales to a user in your system.
              Channel3 appends it to buy URLs in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-user-id": x_user_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/conversations",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "context": context,
                    "conversation_id": conversation_id,
                    "filters": filters,
                    "stream": stream,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TurnResult,
        )

    async def retrieve(
        self,
        conversation_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationDetail:
        """Thread metadata plus one page of its message history.

        Paginate `items` with
        `limit` and `cursor`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            path_template("/v1/conversations/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    conversation_retrieve_params.ConversationRetrieveParams,
                ),
            ),
            cast_to=ConversationDetail,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_raw_response_wrapper(
            conversations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            conversations.retrieve,
        )


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_raw_response_wrapper(
            conversations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            conversations.retrieve,
        )


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_streamed_response_wrapper(
            conversations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            conversations.retrieve,
        )


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_streamed_response_wrapper(
            conversations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            conversations.retrieve,
        )
