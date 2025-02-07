"""Recipe provider exceptions."""

from __future__ import annotations

from http import HTTPStatus

from app.core.exceptions import ExternalServiceError, NotFoundError


class RecipeProviderError(ExternalServiceError):
    """Base exception for recipe provider errors."""

    def __init__(self, message: str, status_code: int | None = None) -> None:
        """Initialize the exception.

        Args:
            message: Error message
            status_code: Optional HTTP status code from provider
        """
        super().__init__(message=message)
        self.status_code = status_code or HTTPStatus.BAD_GATEWAY


class RecipeNotFoundError(NotFoundError):
    """Raised when a recipe cannot be found."""


class RecipeProviderTimeout(RecipeProviderError):
    """Raised when a provider request times out."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: Error message
        """
        super().__init__(message=message, status_code=HTTPStatus.GATEWAY_TIMEOUT)


class RecipeProviderAuthError(RecipeProviderError):
    """Raised when there are authentication/authorization issues."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: Error message
        """
        super().__init__(message=message, status_code=HTTPStatus.UNAUTHORIZED)


class RecipeProviderRateLimitError(RecipeProviderError):
    """Raised when rate limits are exceeded."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: Error message
        """
        super().__init__(message=message, status_code=HTTPStatus.TOO_MANY_REQUESTS)


class RecipeProviderValidationError(RecipeProviderError):
    """Raised when provider rejects request due to validation."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: Error message
        """
        super().__init__(message=message, status_code=HTTPStatus.BAD_REQUEST)


class RecipeProviderParseError(RecipeProviderError):
    """Raised when provider response cannot be parsed."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: Error message
        """
        super().__init__(message=message, status_code=HTTPStatus.BAD_GATEWAY)
