# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import search_perform_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.search_perform_response import SearchPerformResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def perform(
        self,
        *,
        base64_image: Optional[str] | NotGiven = NOT_GIVEN,
        config: search_perform_params.Config | NotGiven = NOT_GIVEN,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        filters: search_perform_params.Filters | NotGiven = NOT_GIVEN,
        image_url: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        query: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchPerformResponse:
        """
        Search for products.

        Args:
          base64_image: Base64 encoded image

          config: Optional configuration

          context: Optional customer information to personalize search results

          filters: Optional filters

          image_url: Image URL

          limit: Optional limit on the number of results

          query: Search query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v0/search",
            body=maybe_transform(
                {
                    "base64_image": base64_image,
                    "config": config,
                    "context": context,
                    "filters": filters,
                    "image_url": image_url,
                    "limit": limit,
                    "query": query,
                },
                search_perform_params.SearchPerformParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchPerformResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def perform(
        self,
        *,
        base64_image: Optional[str] | NotGiven = NOT_GIVEN,
        config: search_perform_params.Config | NotGiven = NOT_GIVEN,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        filters: search_perform_params.Filters | NotGiven = NOT_GIVEN,
        image_url: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        query: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchPerformResponse:
        """
        Search for products.

        Args:
          base64_image: Base64 encoded image

          config: Optional configuration

          context: Optional customer information to personalize search results

          filters: Optional filters

          image_url: Image URL

          limit: Optional limit on the number of results

          query: Search query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v0/search",
            body=await async_maybe_transform(
                {
                    "base64_image": base64_image,
                    "config": config,
                    "context": context,
                    "filters": filters,
                    "image_url": image_url,
                    "limit": limit,
                    "query": query,
                },
                search_perform_params.SearchPerformParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchPerformResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.perform = to_raw_response_wrapper(
            search.perform,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.perform = async_to_raw_response_wrapper(
            search.perform,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.perform = to_streamed_response_wrapper(
            search.perform,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.perform = async_to_streamed_response_wrapper(
            search.perform,
        )
