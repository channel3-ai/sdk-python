# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncAnalyticsPage, AsyncAnalyticsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.reporting import click_list_params
from ...types.reporting.click import Click

__all__ = ["ClicksResource", "AsyncClicksResource"]


class ClicksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClicksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ClicksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClicksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return ClicksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_date: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start_date: Union[str, datetime, None] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncAnalyticsPage[Click]:
        """
        List clicks for your account over a datetime window.

        Defaults to the last 30 days ending now. Maximum window is 90 days. Pass an
        offset-aware ISO datetime to express local time (e.g. last 6 hours). Returns a
        summary plus a paginated list of click events (most recent first).

        Args:
          end_date: Inclusive end of the window (ISO 8601 datetime with optional offset, e.g.
              2026-08-01T23:59:59-04:00). Offset-aware values are converted to UTC; naive
              values are treated as UTC.

          limit: Items per page (max 100).

          page: Page number (1-indexed).

          start_date: Inclusive start of the window (ISO 8601 datetime with optional offset, e.g.
              2026-08-01T00:00:00-04:00). Offset-aware values are converted to UTC; naive
              values are treated as UTC.

          user_id: Filter results to clicks or transactions for this user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/reporting/clicks",
            page=SyncAnalyticsPage[Click],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "page": page,
                        "start_date": start_date,
                        "user_id": user_id,
                    },
                    click_list_params.ClickListParams,
                ),
            ),
            model=Click,
        )


class AsyncClicksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClicksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClicksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClicksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncClicksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_date: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start_date: Union[str, datetime, None] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Click, AsyncAnalyticsPage[Click]]:
        """
        List clicks for your account over a datetime window.

        Defaults to the last 30 days ending now. Maximum window is 90 days. Pass an
        offset-aware ISO datetime to express local time (e.g. last 6 hours). Returns a
        summary plus a paginated list of click events (most recent first).

        Args:
          end_date: Inclusive end of the window (ISO 8601 datetime with optional offset, e.g.
              2026-08-01T23:59:59-04:00). Offset-aware values are converted to UTC; naive
              values are treated as UTC.

          limit: Items per page (max 100).

          page: Page number (1-indexed).

          start_date: Inclusive start of the window (ISO 8601 datetime with optional offset, e.g.
              2026-08-01T00:00:00-04:00). Offset-aware values are converted to UTC; naive
              values are treated as UTC.

          user_id: Filter results to clicks or transactions for this user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/reporting/clicks",
            page=AsyncAnalyticsPage[Click],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "page": page,
                        "start_date": start_date,
                        "user_id": user_id,
                    },
                    click_list_params.ClickListParams,
                ),
            ),
            model=Click,
        )


class ClicksResourceWithRawResponse:
    def __init__(self, clicks: ClicksResource) -> None:
        self._clicks = clicks

        self.list = to_raw_response_wrapper(
            clicks.list,
        )


class AsyncClicksResourceWithRawResponse:
    def __init__(self, clicks: AsyncClicksResource) -> None:
        self._clicks = clicks

        self.list = async_to_raw_response_wrapper(
            clicks.list,
        )


class ClicksResourceWithStreamingResponse:
    def __init__(self, clicks: ClicksResource) -> None:
        self._clicks = clicks

        self.list = to_streamed_response_wrapper(
            clicks.list,
        )


class AsyncClicksResourceWithStreamingResponse:
    def __init__(self, clicks: AsyncClicksResource) -> None:
        self._clicks = clicks

        self.list = async_to_streamed_response_wrapper(
            clicks.list,
        )
