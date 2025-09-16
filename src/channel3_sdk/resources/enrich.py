# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import enrich_enrich_url_params
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
from ..types.enrich_enrich_url_response import EnrichEnrichURLResponse

__all__ = ["EnrichResource", "AsyncEnrichResource"]


class EnrichResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnrichResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return EnrichResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnrichResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return EnrichResourceWithStreamingResponse(self)

    def enrich_url(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnrichEnrichURLResponse:
        """
        Enrich a product URL with additional information.

        Args:
          url: The URL of the product to enrich

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v0/enrich",
            body=maybe_transform({"url": url}, enrich_enrich_url_params.EnrichEnrichURLParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrichEnrichURLResponse,
        )


class AsyncEnrichResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnrichResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnrichResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnrichResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncEnrichResourceWithStreamingResponse(self)

    async def enrich_url(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnrichEnrichURLResponse:
        """
        Enrich a product URL with additional information.

        Args:
          url: The URL of the product to enrich

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v0/enrich",
            body=await async_maybe_transform({"url": url}, enrich_enrich_url_params.EnrichEnrichURLParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrichEnrichURLResponse,
        )


class EnrichResourceWithRawResponse:
    def __init__(self, enrich: EnrichResource) -> None:
        self._enrich = enrich

        self.enrich_url = to_raw_response_wrapper(
            enrich.enrich_url,
        )


class AsyncEnrichResourceWithRawResponse:
    def __init__(self, enrich: AsyncEnrichResource) -> None:
        self._enrich = enrich

        self.enrich_url = async_to_raw_response_wrapper(
            enrich.enrich_url,
        )


class EnrichResourceWithStreamingResponse:
    def __init__(self, enrich: EnrichResource) -> None:
        self._enrich = enrich

        self.enrich_url = to_streamed_response_wrapper(
            enrich.enrich_url,
        )


class AsyncEnrichResourceWithStreamingResponse:
    def __init__(self, enrich: AsyncEnrichResource) -> None:
        self._enrich = enrich

        self.enrich_url = async_to_streamed_response_wrapper(
            enrich.enrich_url,
        )
