# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import product_lookup_params, product_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.product_detail import ProductDetail
from ..types.lookup_response import LookupResponse

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        product_id: str,
        *,
        website_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductDetail:
        """
        Get detailed information about a specific product by its ID.

        Args:
          website_ids: Optional list of website IDs to constrain the buy URL to, relevant if multiple
              merchants exist

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._get(
            path_template("/v1/products/{product_id}", product_id=product_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"website_ids": website_ids}, product_retrieve_params.ProductRetrieveParams),
            ),
            cast_to=ProductDetail,
        )

    def lookup(
        self,
        *,
        url: str,
        max_staleness_hours: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LookupResponse:
        """
        Retrieve product information for any supported product URL.

        Returns the same Product model as GET /v1/products/{product_id}. The product_id
        in the response can be used with the Product Detail endpoint.

        Args:
          url: The URL of the product to look up

          max_staleness_hours: Maximum age (in hours) of cached product data before forcing a fresh lookup.
              Defaults to 3 hours.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/lookup",
            body=maybe_transform(
                {
                    "url": url,
                    "max_staleness_hours": max_staleness_hours,
                },
                product_lookup_params.ProductLookupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LookupResponse,
        )


class AsyncProductsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        product_id: str,
        *,
        website_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductDetail:
        """
        Get detailed information about a specific product by its ID.

        Args:
          website_ids: Optional list of website IDs to constrain the buy URL to, relevant if multiple
              merchants exist

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._get(
            path_template("/v1/products/{product_id}", product_id=product_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"website_ids": website_ids}, product_retrieve_params.ProductRetrieveParams
                ),
            ),
            cast_to=ProductDetail,
        )

    async def lookup(
        self,
        *,
        url: str,
        max_staleness_hours: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LookupResponse:
        """
        Retrieve product information for any supported product URL.

        Returns the same Product model as GET /v1/products/{product_id}. The product_id
        in the response can be used with the Product Detail endpoint.

        Args:
          url: The URL of the product to look up

          max_staleness_hours: Maximum age (in hours) of cached product data before forcing a fresh lookup.
              Defaults to 3 hours.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/lookup",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "max_staleness_hours": max_staleness_hours,
                },
                product_lookup_params.ProductLookupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LookupResponse,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.retrieve = to_raw_response_wrapper(
            products.retrieve,
        )
        self.lookup = to_raw_response_wrapper(
            products.lookup,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.retrieve = async_to_raw_response_wrapper(
            products.retrieve,
        )
        self.lookup = async_to_raw_response_wrapper(
            products.lookup,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.retrieve = to_streamed_response_wrapper(
            products.retrieve,
        )
        self.lookup = to_streamed_response_wrapper(
            products.lookup,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.retrieve = async_to_streamed_response_wrapper(
            products.retrieve,
        )
        self.lookup = async_to_streamed_response_wrapper(
            products.lookup,
        )
