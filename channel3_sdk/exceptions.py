"""Custom exceptions for the Channel3 SDK."""

from typing import Optional, Dict, Any


class Channel3Error(Exception):
    """Base exception for all Channel3 SDK errors."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        response_data: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data or {}


class Channel3AuthenticationError(Channel3Error):
    """Raised when authentication fails (401)."""

    pass


class Channel3ValidationError(Channel3Error):
    """Raised when request validation fails (422)."""

    pass


class Channel3NotFoundError(Channel3Error):
    """Raised when a resource is not found (404)."""

    pass


class Channel3ServerError(Channel3Error):
    """Raised when the server encounters an error (500)."""

    pass


class Channel3ConnectionError(Channel3Error):
    """Raised when there are connection issues."""

    pass
