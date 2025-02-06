"""Recipe provider exceptions."""

from __future__ import annotations


class RecipeProviderError(Exception):
    """Base exception for recipe provider errors."""

    def __init__(self, message: str, status_code: int | None = None) -> None:
        """Initialize the exception.

        Args:
            message: Error message
            status_code: Optional HTTP status code from provider
        """
        super().__init__(message)
        self.status_code = status_code


class RecipeNotFoundError(RecipeProviderError):
    """Raised when a recipe cannot be found."""


class RecipeProviderTimeout(RecipeProviderError):
    """Raised when a provider request times out."""


class RecipeProviderAuthError(RecipeProviderError):
    """Raised when there are authentication/authorization issues."""


class RecipeProviderRateLimitError(RecipeProviderError):
    """Raised when rate limits are exceeded."""


class RecipeProviderValidationError(RecipeProviderError):
    """Raised when provider rejects request due to validation."""


class RecipeProviderParseError(RecipeProviderError):
    """Raised when provider response cannot be parsed."""
