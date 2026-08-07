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
from ...types.reporting import transaction_list_params
from ...types.reporting.transaction import Transaction

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return TransactionsResourceWithStreamingResponse(self)

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
    ) -> SyncAnalyticsPage[Transaction]:
        """
        List transactions for your account over a datetime window.

        Defaults to the last 30 days ending now. Maximum window is 90 days. Pass an
        offset-aware ISO datetime to express local time (e.g. last 6 hours). Returns a
        summary of net commission (after take rate) plus a paginated list of
        transactions (most recent first). Network-approved commissions appear as
        pending.

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
            "/v1/reporting/transactions",
            page=SyncAnalyticsPage[Transaction],
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
                    transaction_list_params.TransactionListParams,
                ),
            ),
            model=Transaction,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncTransactionsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[Transaction, AsyncAnalyticsPage[Transaction]]:
        """
        List transactions for your account over a datetime window.

        Defaults to the last 30 days ending now. Maximum window is 90 days. Pass an
        offset-aware ISO datetime to express local time (e.g. last 6 hours). Returns a
        summary of net commission (after take rate) plus a paginated list of
        transactions (most recent first). Network-approved commissions appear as
        pending.

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
            "/v1/reporting/transactions",
            page=AsyncAnalyticsPage[Transaction],
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
                    transaction_list_params.TransactionListParams,
                ),
            ),
            model=Transaction,
        )


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.list = to_raw_response_wrapper(
            transactions.list,
        )


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.list = async_to_raw_response_wrapper(
            transactions.list,
        )


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.list = to_streamed_response_wrapper(
            transactions.list,
        )


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.list = async_to_streamed_response_wrapper(
            transactions.list,
        )
