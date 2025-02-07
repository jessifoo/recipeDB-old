"""Base recipe provider interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, TypeVar

from app.models.recipe import Recipe

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

T = TypeVar("T", bound=Recipe)


class RecipeProvider(ABC):
    """Base class for recipe providers."""

    def __init__(self, api_key: str | None = None) -> None:
        """Initialize the provider.

        Args:
            api_key: Optional API key for the provider
        """
        self.api_key = api_key

    @property
    @abstractmethod
    def name(self) -> str:
        """Get the provider name."""
        ...

    @abstractmethod
    async def search_recipes(
        self,
        query: str,
        *,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude_ingredients: list[str] | None = None,
        max_time: int | None = None,
    ) -> AsyncIterator[T]:
        """Search for recipes.

        Args:
            query: Search query string
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude_ingredients: List of ingredients to exclude
            max_time: Maximum total time in minutes

        Yields:
            Recipe objects matching the search criteria
        """
        ...

    @abstractmethod
    async def get_recipe(self, recipe_id: str) -> T:
        """Get a specific recipe by ID.

        Args:
            recipe_id: The recipe ID from this provider

        Returns:
            The recipe details

        Raises:
            RecipeNotFoundError: If the recipe doesn't exist
            RecipeProviderError: If there's an error fetching the recipe
        """
        ...

    @abstractmethod
    async def get_random_recipes(self, *, limit: int = 20, tags: list[str] | None = None) -> AsyncIterator[T]:
        """Get random recipes.

        Args:
            limit: Maximum number of recipes to return
            tags: Optional list of tags to filter by

        Yields:
            Random recipe objects
        """
        ...

    async def __aenter__(self) -> RecipeProvider:
        """Enter async context."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit async context and cleanup resources."""
        await self.close()

    async def close(self) -> None:
        """Close any open connections."""
        # Override if provider needs cleanup
