# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    product_lookup_params,
    product_search_params,
    product_retrieve_params,
    product_find_similar_params,
    product_search_by_image_params,
)
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
from ..pagination import SyncSearchPage, AsyncSearchPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.product_detail import ProductDetail
from ..types.lookup_response import LookupResponse
from ..types.locale_config_param import LocaleConfigParam
from ..types.search_config_param import SearchConfigParam
from ..types.search_filters_param import SearchFiltersParam

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
        country: Optional[
            Literal[
                "US", "GB", "EU", "AU", "CA", "IE", "DE", "AT", "FR", "BE", "IT", "ES", "NL", "SE", "FI", "PT", "CZ"
            ]
        ]
        | Omit = omit,
        currency: Optional[Literal["USD", "CAD", "AUD", "GBP", "EUR", "SEK", "CZK"]] | Omit = omit,
        language: Optional[Literal["en", "de", "fr", "it", "es", "nl", "sv", "fi", "pt", "cs"]] | Omit = omit,
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
          country: ISO 3166-1 alpha-2 country code. Matches any country when unset; defaults to
              'US' only when language and currency are also unset.

          currency: ISO 4217 currency code. When unset, inferred from `country` (e.g. GB -> GBP);
              falls back to 'USD' only when all three locale fields are unset.

          language: ISO 639-1 language code. Matches any language when unset; defaults to 'en' only
              when country and currency are also unset.

          website_ids: Optional list of website IDs to constrain the buy URL to, relevant if multiple
              merchants exist. Accepts website IDs or domains (e.g. "nike.com").

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
                query=maybe_transform(
                    {
                        "country": country,
                        "currency": currency,
                        "language": language,
                        "website_ids": website_ids,
                    },
                    product_retrieve_params.ProductRetrieveParams,
                ),
            ),
            cast_to=ProductDetail,
        )

    def find_similar(
        self,
        *,
        product_id: str,
        config: LocaleConfigParam | Omit = omit,
        filters: SearchFiltersParam | Omit = omit,
        limit: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSearchPage[ProductDetail]:
        """
        Find products similar to a given product.

        Consider setting `filters` to narrow results to the same gender, brand,
        category, price range, etc. when you only want similar items within a specific
        slice of the catalog.

        Args:
          product_id: Canonical product ID to find similar products for.

          config: Optional locale configuration.

          filters: Optional filters. Search will only consider products that match all of the
              filters.

          limit: Optional limit on the number of results. Default is 20, max is 30.

          page_token: Opaque token from a previous similar response to fetch the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/similar",
            page=SyncSearchPage[ProductDetail],
            body=maybe_transform(
                {
                    "product_id": product_id,
                    "config": config,
                    "filters": filters,
                    "limit": limit,
                    "page_token": page_token,
                },
                product_find_similar_params.ProductFindSimilarParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProductDetail,
            method="post",
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

    def search(
        self,
        *,
        base64_image: Optional[str] | Omit = omit,
        config: SearchConfigParam | Omit = omit,
        filters: SearchFiltersParam | Omit = omit,
        image_url: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSearchPage[ProductDetail]:
        """
        Search for products with pagination support.

        At least one of `query`, `image_url`, or `base64_image` must be provided;
        requests with none of these will return 422.

        Args:
          base64_image: Base64 encoded image. At least one of `query`, `image_url`, or `base64_image`
              must be provided.

          config: Optional configuration

          filters: Optional filters. Search will only consider products that match all of the
              filters.

          image_url: Image URL. At least one of `query`, `image_url`, or `base64_image` must be
              provided.

          limit: Optional limit on the number of results. Default is 20, max is 30.

          page_token: Opaque token from a previous search response to fetch the next page of results.

          query: Search query. At least one of `query`, `image_url`, or `base64_image` must be
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/search",
            page=SyncSearchPage[ProductDetail],
            body=maybe_transform(
                {
                    "base64_image": base64_image,
                    "config": config,
                    "filters": filters,
                    "image_url": image_url,
                    "limit": limit,
                    "page_token": page_token,
                    "query": query,
                },
                product_search_params.ProductSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProductDetail,
            method="post",
        )

    def search_by_image(
        self,
        *,
        base64_image: Optional[str] | Omit = omit,
        config: LocaleConfigParam | Omit = omit,
        filters: SearchFiltersParam | Omit = omit,
        image_url: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSearchPage[ProductDetail]:
        """
        Search the catalog by image (URL or base64), with pagination support.

        Provide exactly one of `image_url` or `base64_image`. For text or text+image
        search, use `POST /v1/search`.

        Args:
          base64_image: Base64 encoded image bytes (no data URI prefix).

          config: Optional locale configuration.

          filters: Optional filters. Search will only consider products that match all of the
              filters.

          image_url: Publicly accessible URL of the image to search with.

          limit: Optional limit on the number of results. Default is 20, max is 30.

          page_token: Opaque token from a previous image-search response to fetch the next page of
              results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/image-search",
            page=SyncSearchPage[ProductDetail],
            body=maybe_transform(
                {
                    "base64_image": base64_image,
                    "config": config,
                    "filters": filters,
                    "image_url": image_url,
                    "limit": limit,
                    "page_token": page_token,
                },
                product_search_by_image_params.ProductSearchByImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProductDetail,
            method="post",
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
        country: Optional[
            Literal[
                "US", "GB", "EU", "AU", "CA", "IE", "DE", "AT", "FR", "BE", "IT", "ES", "NL", "SE", "FI", "PT", "CZ"
            ]
        ]
        | Omit = omit,
        currency: Optional[Literal["USD", "CAD", "AUD", "GBP", "EUR", "SEK", "CZK"]] | Omit = omit,
        language: Optional[Literal["en", "de", "fr", "it", "es", "nl", "sv", "fi", "pt", "cs"]] | Omit = omit,
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
          country: ISO 3166-1 alpha-2 country code. Matches any country when unset; defaults to
              'US' only when language and currency are also unset.

          currency: ISO 4217 currency code. When unset, inferred from `country` (e.g. GB -> GBP);
              falls back to 'USD' only when all three locale fields are unset.

          language: ISO 639-1 language code. Matches any language when unset; defaults to 'en' only
              when country and currency are also unset.

          website_ids: Optional list of website IDs to constrain the buy URL to, relevant if multiple
              merchants exist. Accepts website IDs or domains (e.g. "nike.com").

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
                    {
                        "country": country,
                        "currency": currency,
                        "language": language,
                        "website_ids": website_ids,
                    },
                    product_retrieve_params.ProductRetrieveParams,
                ),
            ),
            cast_to=ProductDetail,
        )

    def find_similar(
        self,
        *,
        product_id: str,
        config: LocaleConfigParam | Omit = omit,
        filters: SearchFiltersParam | Omit = omit,
        limit: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProductDetail, AsyncSearchPage[ProductDetail]]:
        """
        Find products similar to a given product.

        Consider setting `filters` to narrow results to the same gender, brand,
        category, price range, etc. when you only want similar items within a specific
        slice of the catalog.

        Args:
          product_id: Canonical product ID to find similar products for.

          config: Optional locale configuration.

          filters: Optional filters. Search will only consider products that match all of the
              filters.

          limit: Optional limit on the number of results. Default is 20, max is 30.

          page_token: Opaque token from a previous similar response to fetch the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/similar",
            page=AsyncSearchPage[ProductDetail],
            body=maybe_transform(
                {
                    "product_id": product_id,
                    "config": config,
                    "filters": filters,
                    "limit": limit,
                    "page_token": page_token,
                },
                product_find_similar_params.ProductFindSimilarParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProductDetail,
            method="post",
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

    def search(
        self,
        *,
        base64_image: Optional[str] | Omit = omit,
        config: SearchConfigParam | Omit = omit,
        filters: SearchFiltersParam | Omit = omit,
        image_url: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProductDetail, AsyncSearchPage[ProductDetail]]:
        """
        Search for products with pagination support.

        At least one of `query`, `image_url`, or `base64_image` must be provided;
        requests with none of these will return 422.

        Args:
          base64_image: Base64 encoded image. At least one of `query`, `image_url`, or `base64_image`
              must be provided.

          config: Optional configuration

          filters: Optional filters. Search will only consider products that match all of the
              filters.

          image_url: Image URL. At least one of `query`, `image_url`, or `base64_image` must be
              provided.

          limit: Optional limit on the number of results. Default is 20, max is 30.

          page_token: Opaque token from a previous search response to fetch the next page of results.

          query: Search query. At least one of `query`, `image_url`, or `base64_image` must be
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/search",
            page=AsyncSearchPage[ProductDetail],
            body=maybe_transform(
                {
                    "base64_image": base64_image,
                    "config": config,
                    "filters": filters,
                    "image_url": image_url,
                    "limit": limit,
                    "page_token": page_token,
                    "query": query,
                },
                product_search_params.ProductSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProductDetail,
            method="post",
        )

    def search_by_image(
        self,
        *,
        base64_image: Optional[str] | Omit = omit,
        config: LocaleConfigParam | Omit = omit,
        filters: SearchFiltersParam | Omit = omit,
        image_url: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProductDetail, AsyncSearchPage[ProductDetail]]:
        """
        Search the catalog by image (URL or base64), with pagination support.

        Provide exactly one of `image_url` or `base64_image`. For text or text+image
        search, use `POST /v1/search`.

        Args:
          base64_image: Base64 encoded image bytes (no data URI prefix).

          config: Optional locale configuration.

          filters: Optional filters. Search will only consider products that match all of the
              filters.

          image_url: Publicly accessible URL of the image to search with.

          limit: Optional limit on the number of results. Default is 20, max is 30.

          page_token: Opaque token from a previous image-search response to fetch the next page of
              results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/image-search",
            page=AsyncSearchPage[ProductDetail],
            body=maybe_transform(
                {
                    "base64_image": base64_image,
                    "config": config,
                    "filters": filters,
                    "image_url": image_url,
                    "limit": limit,
                    "page_token": page_token,
                },
                product_search_by_image_params.ProductSearchByImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProductDetail,
            method="post",
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.retrieve = to_raw_response_wrapper(
            products.retrieve,
        )
        self.find_similar = to_raw_response_wrapper(
            products.find_similar,
        )
        self.lookup = to_raw_response_wrapper(
            products.lookup,
        )
        self.search = to_raw_response_wrapper(
            products.search,
        )
        self.search_by_image = to_raw_response_wrapper(
            products.search_by_image,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.retrieve = async_to_raw_response_wrapper(
            products.retrieve,
        )
        self.find_similar = async_to_raw_response_wrapper(
            products.find_similar,
        )
        self.lookup = async_to_raw_response_wrapper(
            products.lookup,
        )
        self.search = async_to_raw_response_wrapper(
            products.search,
        )
        self.search_by_image = async_to_raw_response_wrapper(
            products.search_by_image,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.retrieve = to_streamed_response_wrapper(
            products.retrieve,
        )
        self.find_similar = to_streamed_response_wrapper(
            products.find_similar,
        )
        self.lookup = to_streamed_response_wrapper(
            products.lookup,
        )
        self.search = to_streamed_response_wrapper(
            products.search,
        )
        self.search_by_image = to_streamed_response_wrapper(
            products.search_by_image,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.retrieve = async_to_streamed_response_wrapper(
            products.retrieve,
        )
        self.find_similar = async_to_streamed_response_wrapper(
            products.find_similar,
        )
        self.lookup = async_to_streamed_response_wrapper(
            products.lookup,
        )
        self.search = async_to_streamed_response_wrapper(
            products.search,
        )
        self.search_by_image = async_to_streamed_response_wrapper(
            products.search_by_image,
        )
