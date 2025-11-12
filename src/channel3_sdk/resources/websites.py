# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import website_find_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.website import Website

__all__ = ["WebsitesResource", "AsyncWebsitesResource"]


class WebsitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebsitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return WebsitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebsitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return WebsitesResourceWithStreamingResponse(self)

    def find(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Website]:
        """
        Find a website by URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v0/websites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, website_find_params.WebsiteFindParams),
            ),
            cast_to=Website,
        )


class AsyncWebsitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebsitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebsitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebsitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncWebsitesResourceWithStreamingResponse(self)

    async def find(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Website]:
        """
        Find a website by URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v0/websites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, website_find_params.WebsiteFindParams),
            ),
            cast_to=Website,
        )


class WebsitesResourceWithRawResponse:
    def __init__(self, websites: WebsitesResource) -> None:
        self._websites = websites

        self.find = to_raw_response_wrapper(
            websites.find,
        )


class AsyncWebsitesResourceWithRawResponse:
    def __init__(self, websites: AsyncWebsitesResource) -> None:
        self._websites = websites

        self.find = async_to_raw_response_wrapper(
            websites.find,
        )


class WebsitesResourceWithStreamingResponse:
    def __init__(self, websites: WebsitesResource) -> None:
        self._websites = websites

        self.find = to_streamed_response_wrapper(
            websites.find,
        )


class AsyncWebsitesResourceWithStreamingResponse:
    def __init__(self, websites: AsyncWebsitesResource) -> None:
        self._websites = websites

        self.find = async_to_streamed_response_wrapper(
            websites.find,
        )
