# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .clicks import (
    ClicksResource,
    AsyncClicksResource,
    ClicksResourceWithRawResponse,
    AsyncClicksResourceWithRawResponse,
    ClicksResourceWithStreamingResponse,
    AsyncClicksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .transactions import (
    TransactionsResource,
    AsyncTransactionsResource,
    TransactionsResourceWithRawResponse,
    AsyncTransactionsResourceWithRawResponse,
    TransactionsResourceWithStreamingResponse,
    AsyncTransactionsResourceWithStreamingResponse,
)

__all__ = ["ReportingResource", "AsyncReportingResource"]


class ReportingResource(SyncAPIResource):
    @cached_property
    def clicks(self) -> ClicksResource:
        return ClicksResource(self._client)

    @cached_property
    def transactions(self) -> TransactionsResource:
        return TransactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReportingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return ReportingResourceWithStreamingResponse(self)


class AsyncReportingResource(AsyncAPIResource):
    @cached_property
    def clicks(self) -> AsyncClicksResource:
        return AsyncClicksResource(self._client)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        return AsyncTransactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/channel3-ai/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/channel3-ai/sdk-python#with_streaming_response
        """
        return AsyncReportingResourceWithStreamingResponse(self)


class ReportingResourceWithRawResponse:
    def __init__(self, reporting: ReportingResource) -> None:
        self._reporting = reporting

    @cached_property
    def clicks(self) -> ClicksResourceWithRawResponse:
        return ClicksResourceWithRawResponse(self._reporting.clicks)

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self._reporting.transactions)


class AsyncReportingResourceWithRawResponse:
    def __init__(self, reporting: AsyncReportingResource) -> None:
        self._reporting = reporting

    @cached_property
    def clicks(self) -> AsyncClicksResourceWithRawResponse:
        return AsyncClicksResourceWithRawResponse(self._reporting.clicks)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        return AsyncTransactionsResourceWithRawResponse(self._reporting.transactions)


class ReportingResourceWithStreamingResponse:
    def __init__(self, reporting: ReportingResource) -> None:
        self._reporting = reporting

    @cached_property
    def clicks(self) -> ClicksResourceWithStreamingResponse:
        return ClicksResourceWithStreamingResponse(self._reporting.clicks)

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self._reporting.transactions)


class AsyncReportingResourceWithStreamingResponse:
    def __init__(self, reporting: AsyncReportingResource) -> None:
        self._reporting = reporting

    @cached_property
    def clicks(self) -> AsyncClicksResourceWithStreamingResponse:
        return AsyncClicksResourceWithStreamingResponse(self._reporting.clicks)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self._reporting.transactions)
