"""Core exception handling for the application."""

from __future__ import annotations

from enum import IntEnum
from http import HTTPStatus
from typing import Any

from fastapi import HTTPException, status


class ErrorCode(IntEnum):
    """Application error codes."""

    # Generic errors (1000-1999)
    UNKNOWN_ERROR = 1000
    VALIDATION_ERROR = 1001
    DATABASE_ERROR = 1002
    NOT_FOUND = 1003
    ALREADY_EXISTS = 1005
    INVALID_STATE = 1006

    # Authentication/Authorization errors (2000-2999)
    UNAUTHORIZED = 2000
    FORBIDDEN = 2001
    INVALID_CREDENTIALS = 2002
    TOKEN_EXPIRED = 2003
    INVALID_TOKEN = 2004

    # External service errors (3000-3999)
    EXTERNAL_SERVICE_ERROR = 3000
    EXTERNAL_SERVICE_TIMEOUT = 3001
    EXTERNAL_SERVICE_UNAVAILABLE = 3002
    RATE_LIMIT_EXCEEDED = 3003
    INVALID_RESPONSE = 3004

    # Recipe specific errors (4000-4999)
    RECIPE_NOT_FOUND = 4000
    RECIPE_VALIDATION_ERROR = 4001
    RECIPE_ALREADY_EXISTS = 4002
    RECIPE_PROVIDER_ERROR = 4003
    RECIPE_FILTER_ERROR = 4004


class AppErrorDetail:
    """Error detail structure."""

    def __init__(
        self: AppErrorDetail,
        code: ErrorCode,
        message: str,
        status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Initialize error detail.

        Args:
            code: Application error code
            message: Error message
            status_code: HTTP status code
            details: Additional error details
        """
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details or {}

    def to_dict(self: AppErrorDetail) -> dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dictionary with error details
        """
        return {"code": self.code, "message": self.message, "status_code": self.status_code, "details": self.details}


class AppHTTPException(HTTPException):
    """Base HTTP exception for application errors."""

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        headers: dict[str, str] | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the exception.

        Args:
            message: Error message
            status_code: HTTP status code
            headers: Optional response headers
            details: Additional error details
        """
        super().__init__(
            status_code=status_code, detail={"message": message, "details": details or {}}, headers=headers
        )


class ValidationError(AppHTTPException):
    """Validation error."""

    def __init__(
        self, message: str, details: dict[str, Any] | None = None, headers: dict[str, str] | None = None
    ) -> None:
        """Initialize validation error.

        Args:
            message: Error message
            details: Validation error details
            headers: Optional response headers
        """
        super().__init__(
            message=message, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, headers=headers, details=details
        )


class NotFoundError(AppHTTPException):
    """Resource not found error."""

    def __init__(
        self, message: str, details: dict[str, Any] | None = None, headers: dict[str, str] | None = None
    ) -> None:
        """Initialize not found error.

        Args:
            message: Error message
            details: Additional error details
            headers: Optional response headers
        """
        super().__init__(message=message, status_code=status.HTTP_404_NOT_FOUND, headers=headers, details=details)


class DatabaseError(AppHTTPException):
    """Database error."""

    def __init__(
        self, message: str, details: dict[str, Any] | None = None, headers: dict[str, str] | None = None
    ) -> None:
        """Initialize database error.

        Args:
            message: Error message
            details: Additional error details
            headers: Optional response headers
        """
        super().__init__(
            message=message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=headers, details=details
        )


class ExternalServiceError(AppHTTPException):
    """External service error."""

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_502_BAD_GATEWAY,
        details: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize external service error.

        Args:
            message: Error message
            status_code: HTTP status code from external service
            details: Additional error details
            headers: Optional response headers
        """
        super().__init__(message=message, status_code=status_code, headers=headers, details=details)


class ExternalServiceTimeoutError(ExternalServiceError):
    """External service timeout error."""

    def __init__(
        self, message: str, details: dict[str, Any] | None = None, headers: dict[str, str] | None = None
    ) -> None:
        """Initialize external service timeout error.

        Args:
            message: Error message
            details: Additional error details
            headers: Optional response headers
        """
        super().__init__(message=message, status_code=status.HTTP_504_GATEWAY_TIMEOUT, headers=headers, details=details)


class RateLimitError(ExternalServiceError):
    """Rate limit exceeded error."""

    def __init__(
        self, message: str, details: dict[str, Any] | None = None, headers: dict[str, str] | None = None
    ) -> None:
        """Initialize rate limit error.

        Args:
            message: Error message
            details: Additional error details
            headers: Optional response headers
        """
        super().__init__(
            message=message, status_code=status.HTTP_429_TOO_MANY_REQUESTS, headers=headers, details=details
        )


class RecipeError(AppHTTPException):
    """Base recipe error."""

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        details: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize recipe error.

        Args:
            message: Error message
            status_code: HTTP status code
            details: Additional error details
            headers: Optional response headers
        """
        super().__init__(message=message, status_code=status_code, headers=headers, details=details)


class RecipeNotFoundError(NotFoundError):
    """Recipe not found error."""


class RecipeFilterError(RecipeError):
    """Recipe filter error (e.g., allergens)."""

    def __init__(
        self,
        message: str = "Recipe does not meet filter criteria",
        details: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize filter error.

        Args:
            message: Error message
            details: Additional error details
            headers: Optional response headers
        """
        super().__init__(
            message=message,
            status_code=status.HTTP_404_NOT_FOUND,  # Use 404 when recipe is filtered out
            headers=headers,
            details=details,
        )


class RecipeProviderError(ExternalServiceError):
    """Recipe provider error."""
