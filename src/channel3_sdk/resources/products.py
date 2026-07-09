# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    product_browse_params,
    product_lookup_params,
    product_search_params,
    product_monetize_params,
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
from ..types.monetize_response import MonetizeResponse
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
                "US",
                "GB",
                "EU",
                "AU",
                "CA",
                "IE",
                "DE",
                "AT",
                "FR",
                "BE",
                "IT",
                "ES",
                "NL",
                "SE",
                "FI",
                "PT",
                "CZ",
                "GR",
                "RO",
            ]
        ]
        | Omit = omit,
        currency: Optional[Literal["USD", "CAD", "AUD", "GBP", "EUR", "SEK", "CZK", "RON"]] | Omit = omit,
        language: Optional[Literal["en", "de", "fr", "it", "es", "nl", "sv", "fi", "pt", "cs", "el", "ro"]]
        | Omit = omit,
        preferred_length_unit: Optional[Literal["mm", "cm", "m", "in", "ft"]] | Omit = omit,
        preferred_weight_unit: Optional[Literal["mg", "g", "kg", "oz", "lb"]] | Omit = omit,
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

          preferred_length_unit: Preferred unit for length dimensions (length/width/height). When unset,
              dimensions are returned in the unit the merchant stated.

          preferred_weight_unit: Preferred unit for weight dimensions. When unset, weight is returned in the unit
              the merchant stated.

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
                        "preferred_length_unit": preferred_length_unit,
                        "preferred_weight_unit": preferred_weight_unit,
                        "website_ids": website_ids,
                    },
                    product_retrieve_params.ProductRetrieveParams,
                ),
            ),
            cast_to=ProductDetail,
        )

    def browse(
        self,
        *,
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
        List and page through products for a set of filters.

        Useful for a static, grid view of products for a brand, website, or category.

        At least one of `filters.brand_ids`, `filters.category_ids`, or
        `filters.website_ids` must be provided.

        Access to this endpoint is restricted. If you think your use-case requires it,
        please contact us.

        Args:
          filters: Filters to browse by. At least one of `brand_ids`, `category_ids`, or
              `website_ids` must be provided.

          limit: Optional limit on the number of results. Default is 20, max is 30.

          page_token: Opaque token from a previous browse response to fetch the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/browse",
            page=SyncSearchPage[ProductDetail],
            body=maybe_transform(
                {
                    "filters": filters,
                    "limit": limit,
                    "page_token": page_token,
                },
                product_browse_params.ProductBrowseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProductDetail,
            method="post",
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

    def monetize(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizeResponse:
        """
        Return monetizable offers (with max commission rate) for a product URL.

        Access to this endpoint is restricted. If you think your use-case requires it,
        please contact us. Usually, developers actually want search. This is helpful for
        migrating to Channel3.

        Args:
          url: The URL of the product to monetize

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/monetize",
            body=maybe_transform({"url": url}, product_monetize_params.ProductMonetizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonetizeResponse,
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

        At least one of `query`, `image_url`, `base64_image`, or `page_token` must be
        provided; requests with none of these will return 422.

        Args:
          base64_image: Base64 encoded image. At least one of `query`, `image_url`, `base64_image`, or
              `page_token` must be provided.

          config: Optional configuration

          filters: Optional filters. Search will only consider products that match all of the
              filters.

          image_url: Image URL. At least one of `query`, `image_url`, `base64_image`, or `page_token`
              must be provided.

          limit: Optional limit on the number of results. Default is 20, max is 30.

          page_token: Opaque token from a previous search response to fetch the next page of results.

          query: Search query. At least one of `query`, `image_url`, `base64_image`, or
              `page_token` must be provided.

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
        segment: Optional[str] | Omit = omit,
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

          segment: Image segmentation mode. None (default) disables segmentation. "AUTO" segments
              and crops the main product automatically. A custom string (e.g. "shoe", "mug")
              segments the specified object.

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
                    "segment": segment,
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
                "US",
                "GB",
                "EU",
                "AU",
                "CA",
                "IE",
                "DE",
                "AT",
                "FR",
                "BE",
                "IT",
                "ES",
                "NL",
                "SE",
                "FI",
                "PT",
                "CZ",
                "GR",
                "RO",
            ]
        ]
        | Omit = omit,
        currency: Optional[Literal["USD", "CAD", "AUD", "GBP", "EUR", "SEK", "CZK", "RON"]] | Omit = omit,
        language: Optional[Literal["en", "de", "fr", "it", "es", "nl", "sv", "fi", "pt", "cs", "el", "ro"]]
        | Omit = omit,
        preferred_length_unit: Optional[Literal["mm", "cm", "m", "in", "ft"]] | Omit = omit,
        preferred_weight_unit: Optional[Literal["mg", "g", "kg", "oz", "lb"]] | Omit = omit,
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

          preferred_length_unit: Preferred unit for length dimensions (length/width/height). When unset,
              dimensions are returned in the unit the merchant stated.

          preferred_weight_unit: Preferred unit for weight dimensions. When unset, weight is returned in the unit
              the merchant stated.

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
                        "preferred_length_unit": preferred_length_unit,
                        "preferred_weight_unit": preferred_weight_unit,
                        "website_ids": website_ids,
                    },
                    product_retrieve_params.ProductRetrieveParams,
                ),
            ),
            cast_to=ProductDetail,
        )

    def browse(
        self,
        *,
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
        List and page through products for a set of filters.

        Useful for a static, grid view of products for a brand, website, or category.

        At least one of `filters.brand_ids`, `filters.category_ids`, or
        `filters.website_ids` must be provided.

        Access to this endpoint is restricted. If you think your use-case requires it,
        please contact us.

        Args:
          filters: Filters to browse by. At least one of `brand_ids`, `category_ids`, or
              `website_ids` must be provided.

          limit: Optional limit on the number of results. Default is 20, max is 30.

          page_token: Opaque token from a previous browse response to fetch the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/browse",
            page=AsyncSearchPage[ProductDetail],
            body=maybe_transform(
                {
                    "filters": filters,
                    "limit": limit,
                    "page_token": page_token,
                },
                product_browse_params.ProductBrowseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ProductDetail,
            method="post",
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

    async def monetize(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizeResponse:
        """
        Return monetizable offers (with max commission rate) for a product URL.

        Access to this endpoint is restricted. If you think your use-case requires it,
        please contact us. Usually, developers actually want search. This is helpful for
        migrating to Channel3.

        Args:
          url: The URL of the product to monetize

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/monetize",
            body=await async_maybe_transform({"url": url}, product_monetize_params.ProductMonetizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonetizeResponse,
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

        At least one of `query`, `image_url`, `base64_image`, or `page_token` must be
        provided; requests with none of these will return 422.

        Args:
          base64_image: Base64 encoded image. At least one of `query`, `image_url`, `base64_image`, or
              `page_token` must be provided.

          config: Optional configuration

          filters: Optional filters. Search will only consider products that match all of the
              filters.

          image_url: Image URL. At least one of `query`, `image_url`, `base64_image`, or `page_token`
              must be provided.

          limit: Optional limit on the number of results. Default is 20, max is 30.

          page_token: Opaque token from a previous search response to fetch the next page of results.

          query: Search query. At least one of `query`, `image_url`, `base64_image`, or
              `page_token` must be provided.

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
        segment: Optional[str] | Omit = omit,
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

          segment: Image segmentation mode. None (default) disables segmentation. "AUTO" segments
              and crops the main product automatically. A custom string (e.g. "shoe", "mug")
              segments the specified object.

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
                    "segment": segment,
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
        self.browse = to_raw_response_wrapper(
            products.browse,
        )
        self.find_similar = to_raw_response_wrapper(
            products.find_similar,
        )
        self.lookup = to_raw_response_wrapper(
            products.lookup,
        )
        self.monetize = to_raw_response_wrapper(
            products.monetize,
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
        self.browse = async_to_raw_response_wrapper(
            products.browse,
        )
        self.find_similar = async_to_raw_response_wrapper(
            products.find_similar,
        )
        self.lookup = async_to_raw_response_wrapper(
            products.lookup,
        )
        self.monetize = async_to_raw_response_wrapper(
            products.monetize,
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
        self.browse = to_streamed_response_wrapper(
            products.browse,
        )
        self.find_similar = to_streamed_response_wrapper(
            products.find_similar,
        )
        self.lookup = to_streamed_response_wrapper(
            products.lookup,
        )
        self.monetize = to_streamed_response_wrapper(
            products.monetize,
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
        self.browse = async_to_streamed_response_wrapper(
            products.browse,
        )
        self.find_similar = async_to_streamed_response_wrapper(
            products.find_similar,
        )
        self.lookup = async_to_streamed_response_wrapper(
            products.lookup,
        )
        self.monetize = async_to_streamed_response_wrapper(
            products.monetize,
        )
        self.search = async_to_streamed_response_wrapper(
            products.search,
        )
        self.search_by_image = async_to_streamed_response_wrapper(
            products.search_by_image,
        )
