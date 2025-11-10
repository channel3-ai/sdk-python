# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import brand_list_params
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
from ..types.brand import Brand
from .._base_client import make_request_options

__all__ = ["BrandsResource", "AsyncBrandsResource"]


class BrandsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return BrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return BrandsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Find a brand by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v0/brands",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, brand_list_params.BrandListParams),
            ),
            cast_to=Brand,
        )


class AsyncBrandsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncBrandsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Find a brand by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v0/brands",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, brand_list_params.BrandListParams),
            ),
            cast_to=Brand,
        )


class BrandsResourceWithRawResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.list = to_raw_response_wrapper(
            brands.list,
        )


class AsyncBrandsResourceWithRawResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.list = async_to_raw_response_wrapper(
            brands.list,
        )


class BrandsResourceWithStreamingResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.list = to_streamed_response_wrapper(
            brands.list,
        )


class AsyncBrandsResourceWithStreamingResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.list = async_to_streamed_response_wrapper(
            brands.list,
        )
