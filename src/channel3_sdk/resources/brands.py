# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Optional

import httpx

from ..types import brand_find_params, brand_list_params, brand_search_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from ..types.brand import Brand
from .._base_client import AsyncPaginator, make_request_options
from ..types.search_brands_response import SearchBrandsResponse

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

    def retrieve(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Get detailed information about a specific brand by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._get(
            path_template("/v1/brands/{brand_id}", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Brand]:
        """
        Paginated list of brands, capped at the top 5,000.

        Args:
          cursor: Pagination cursor returned by a prior call. Omit for the first page.

          limit: Max items per page (1-100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/brands",
            page=SyncCursorPage[Brand],
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
                    brand_list_params.BrandListParams,
                ),
            ),
            model=Brand,
        )

    @typing_extensions.deprecated("use `search` (returns a list) instead; will be removed in the next major version")
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
                query=maybe_transform({"query": query}, brand_find_params.BrandFindParams),
            ),
            cast_to=Brand,
        )

    def search(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchBrandsResponse:
        """Search brands by free-text query.

        Args:
          query: Free-text query (e.g.

        'Nike', 'lululemon').

          limit: Maximum number of brands to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/brands/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "limit": limit,
                    },
                    brand_search_params.BrandSearchParams,
                ),
            ),
            cast_to=SearchBrandsResponse,
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

    async def retrieve(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Get detailed information about a specific brand by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._get(
            path_template("/v1/brands/{brand_id}", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Brand, AsyncCursorPage[Brand]]:
        """
        Paginated list of brands, capped at the top 5,000.

        Args:
          cursor: Pagination cursor returned by a prior call. Omit for the first page.

          limit: Max items per page (1-100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/brands",
            page=AsyncCursorPage[Brand],
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
                    brand_list_params.BrandListParams,
                ),
            ),
            model=Brand,
        )

    @typing_extensions.deprecated("use `search` (returns a list) instead; will be removed in the next major version")
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
                query=await async_maybe_transform({"query": query}, brand_find_params.BrandFindParams),
            ),
            cast_to=Brand,
        )

    async def search(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchBrandsResponse:
        """Search brands by free-text query.

        Args:
          query: Free-text query (e.g.

        'Nike', 'lululemon').

          limit: Maximum number of brands to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/brands/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "limit": limit,
                    },
                    brand_search_params.BrandSearchParams,
                ),
            ),
            cast_to=SearchBrandsResponse,
        )


class BrandsResourceWithRawResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.retrieve = to_raw_response_wrapper(
            brands.retrieve,
        )
        self.list = to_raw_response_wrapper(
            brands.list,
        )
        self.find = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                brands.find,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = to_raw_response_wrapper(
            brands.search,
        )


class AsyncBrandsResourceWithRawResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.retrieve = async_to_raw_response_wrapper(
            brands.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            brands.list,
        )
        self.find = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                brands.find,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = async_to_raw_response_wrapper(
            brands.search,
        )


class BrandsResourceWithStreamingResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.retrieve = to_streamed_response_wrapper(
            brands.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            brands.list,
        )
        self.find = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                brands.find,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = to_streamed_response_wrapper(
            brands.search,
        )


class AsyncBrandsResourceWithStreamingResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.retrieve = async_to_streamed_response_wrapper(
            brands.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            brands.list,
        )
        self.find = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                brands.find,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = async_to_streamed_response_wrapper(
            brands.search,
        )
