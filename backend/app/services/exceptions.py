"""Recipe service exceptions."""

from __future__ import annotations


class RecipeServiceError(Exception):
    """Base exception for recipe service errors."""


class RecipeProviderError(RecipeServiceError):
    """Exception raised when a recipe provider encounters an error."""


class RecipeNotFoundError(RecipeServiceError):
    """Exception raised when a recipe cannot be found."""


class RecipeFilterError(RecipeServiceError):
    """Exception raised when a recipe fails filtering criteria (e.g., allergens)."""


class ExternalAPIError(RecipeServiceError):
    """Exception raised when an external API request fails."""

    def __init__(self, message: str, status_code: int | None = None) -> None:
        """Initialize the exception.

        Args:
            message: The error message
            status_code: The HTTP status code from the external API
        """
        super().__init__(message)
        self.status_code = status_code
