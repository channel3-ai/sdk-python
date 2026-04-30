# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncCursorPage",
    "AsyncCursorPage",
    "SyncSearchPage",
    "AsyncSearchPage",
    "SyncCategoryPage",
    "AsyncCategoryPage",
]

_T = TypeVar("_T")


class SyncCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncSearchPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    products: List[_T]
    next_page_token: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        products = self.products
        if not products:
            return []
        return products

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page_token = self.next_page_token
        if not next_page_token:
            return None

        return PageInfo(json={"page_token": next_page_token})


class AsyncSearchPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    products: List[_T]
    next_page_token: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        products = self.products
        if not products:
            return []
        return products

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page_token = self.next_page_token
        if not next_page_token:
            return None

        return PageInfo(json={"page_token": next_page_token})


class SyncCategoryPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    page: Optional[int] = None
    page_size: Optional[int] = None
    total: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        return PageInfo(params={"page": current_page + 1})


class AsyncCategoryPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    page: Optional[int] = None
    page_size: Optional[int] = None
    total: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        return PageInfo(params={"page": current_page + 1})
