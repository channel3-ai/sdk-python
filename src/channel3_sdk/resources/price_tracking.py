# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    price_tracking_stop_params,
    price_tracking_start_params,
    price_tracking_get_history_params,
    price_tracking_list_subscriptions_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.subscription import Subscription
from ..types.price_history import PriceHistory
from ..types.paginated_subscriptions import PaginatedSubscriptions

__all__ = ["PriceTrackingResource", "AsyncPriceTrackingResource"]


class PriceTrackingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PriceTrackingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PriceTrackingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PriceTrackingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return PriceTrackingResourceWithStreamingResponse(self)

    def get_history(
        self,
        canonical_product_id: str,
        *,
        days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceHistory:
        """
        Get price history for a canonical product.

        Args:
          days: Number of days of history to fetch (max 30)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not canonical_product_id:
            raise ValueError(
                f"Expected a non-empty value for `canonical_product_id` but received {canonical_product_id!r}"
            )
        return self._get(
            f"/v0/price-tracking/history/{canonical_product_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"days": days}, price_tracking_get_history_params.PriceTrackingGetHistoryParams),
            ),
            cast_to=PriceHistory,
        )

    def list_subscriptions(
        self,
        *,
        limit: int | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedSubscriptions:
        """
        List your active price tracking subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v0/price-tracking/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page_token": page_token,
                    },
                    price_tracking_list_subscriptions_params.PriceTrackingListSubscriptionsParams,
                ),
            ),
            cast_to=PaginatedSubscriptions,
        )

    def start(
        self,
        *,
        canonical_product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """
        Start tracking prices for a canonical product.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v0/price-tracking/start",
            body=maybe_transform(
                {"canonical_product_id": canonical_product_id}, price_tracking_start_params.PriceTrackingStartParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    def stop(
        self,
        *,
        canonical_product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """
        Stop tracking prices for a canonical product.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v0/price-tracking/stop",
            body=maybe_transform(
                {"canonical_product_id": canonical_product_id}, price_tracking_stop_params.PriceTrackingStopParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )


class AsyncPriceTrackingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPriceTrackingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPriceTrackingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPriceTrackingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncPriceTrackingResourceWithStreamingResponse(self)

    async def get_history(
        self,
        canonical_product_id: str,
        *,
        days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceHistory:
        """
        Get price history for a canonical product.

        Args:
          days: Number of days of history to fetch (max 30)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not canonical_product_id:
            raise ValueError(
                f"Expected a non-empty value for `canonical_product_id` but received {canonical_product_id!r}"
            )
        return await self._get(
            f"/v0/price-tracking/history/{canonical_product_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"days": days}, price_tracking_get_history_params.PriceTrackingGetHistoryParams
                ),
            ),
            cast_to=PriceHistory,
        )

    async def list_subscriptions(
        self,
        *,
        limit: int | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedSubscriptions:
        """
        List your active price tracking subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v0/price-tracking/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page_token": page_token,
                    },
                    price_tracking_list_subscriptions_params.PriceTrackingListSubscriptionsParams,
                ),
            ),
            cast_to=PaginatedSubscriptions,
        )

    async def start(
        self,
        *,
        canonical_product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """
        Start tracking prices for a canonical product.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v0/price-tracking/start",
            body=await async_maybe_transform(
                {"canonical_product_id": canonical_product_id}, price_tracking_start_params.PriceTrackingStartParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    async def stop(
        self,
        *,
        canonical_product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """
        Stop tracking prices for a canonical product.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v0/price-tracking/stop",
            body=await async_maybe_transform(
                {"canonical_product_id": canonical_product_id}, price_tracking_stop_params.PriceTrackingStopParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )


class PriceTrackingResourceWithRawResponse:
    def __init__(self, price_tracking: PriceTrackingResource) -> None:
        self._price_tracking = price_tracking

        self.get_history = to_raw_response_wrapper(
            price_tracking.get_history,
        )
        self.list_subscriptions = to_raw_response_wrapper(
            price_tracking.list_subscriptions,
        )
        self.start = to_raw_response_wrapper(
            price_tracking.start,
        )
        self.stop = to_raw_response_wrapper(
            price_tracking.stop,
        )


class AsyncPriceTrackingResourceWithRawResponse:
    def __init__(self, price_tracking: AsyncPriceTrackingResource) -> None:
        self._price_tracking = price_tracking

        self.get_history = async_to_raw_response_wrapper(
            price_tracking.get_history,
        )
        self.list_subscriptions = async_to_raw_response_wrapper(
            price_tracking.list_subscriptions,
        )
        self.start = async_to_raw_response_wrapper(
            price_tracking.start,
        )
        self.stop = async_to_raw_response_wrapper(
            price_tracking.stop,
        )


class PriceTrackingResourceWithStreamingResponse:
    def __init__(self, price_tracking: PriceTrackingResource) -> None:
        self._price_tracking = price_tracking

        self.get_history = to_streamed_response_wrapper(
            price_tracking.get_history,
        )
        self.list_subscriptions = to_streamed_response_wrapper(
            price_tracking.list_subscriptions,
        )
        self.start = to_streamed_response_wrapper(
            price_tracking.start,
        )
        self.stop = to_streamed_response_wrapper(
            price_tracking.stop,
        )


class AsyncPriceTrackingResourceWithStreamingResponse:
    def __init__(self, price_tracking: AsyncPriceTrackingResource) -> None:
        self._price_tracking = price_tracking

        self.get_history = async_to_streamed_response_wrapper(
            price_tracking.get_history,
        )
        self.list_subscriptions = async_to_streamed_response_wrapper(
            price_tracking.list_subscriptions,
        )
        self.start = async_to_streamed_response_wrapper(
            price_tracking.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            price_tracking.stop,
        )
