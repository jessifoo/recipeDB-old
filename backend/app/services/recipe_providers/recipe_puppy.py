"""Recipe Puppy provider implementation."""

from __future__ import annotations

from typing import Any, cast

import httpx

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import DomainError, ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.base import ProviderRecipeData, RecipeProvider


class RecipePuppyProvider(RecipeProvider):
    """Recipe Puppy provider implementation."""

    BASE_URL = "http://www.recipepuppy.com/api"

    def __init__(self) -> None:
        """Initialize Recipe Puppy provider."""
        super().__init__()
        self.client = httpx.AsyncClient(base_url=self.BASE_URL, timeout=30.0)

    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search for recipes using Recipe Puppy API.

        Args:
            query: Search query string
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude: List of ingredients to exclude
            max_time: Maximum cooking time in minutes

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            DomainError: If the API request fails
            ValidationError: If the search parameters are invalid
            BusinessError: If no recipes match the filters
        """
        # Calculate page number (Recipe Puppy uses 10 results per page)
        page = (offset // 10) + 1

        params: dict[str, Any] = {"q": query, "p": page}

        # Add ingredients to exclude
        if exclude:
            params["excludedIngredients"] = ",".join(exclude)

        try:
            response = await self.client.get("/", params=params)
            response.raise_for_status()
            data = response.json()
            recipes = cast(list[ProviderRecipeData], data.get("results", []))

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply allergen filtering
            results = self._apply_allergen_filtering(results)

            # Apply additional filters
            if cuisine:
                results = [r for r in results if r.cuisine and cuisine.lower() in r.cuisine.lower()]
            if diet:
                results = [r for r in results if r.diet and diet in r.diet]
            if max_time:
                results = [r for r in results if r.total_time and r.total_time <= max_time]

            # Handle pagination
            start = offset % 10  # Offset within the current page
            paginated_results = results[start : start + limit]

            return RecipeList(
                total=len(results),  # Recipe Puppy doesn't provide total count
                results=paginated_results,
                source=self.source_name,
            )

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "Recipe Puppy", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_SEARCH_FAILED, code=ErrorCode.API_ERROR, details={"error": str(e)}
            ) from e

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Args:
            recipe_id: Recipe ID from the provider

        Returns:
            RecipeSearchResult: Detailed recipe information

        Raises:
            DomainError: If the API request fails
            ValidationError: If the recipe ID is invalid
            BusinessError: If the recipe contains allergens
        """
        # Recipe Puppy doesn't support direct recipe lookup by ID
        # We would need to search and filter by our generated ID
        raise ValidationError(
            message_template=ErrorMessages.OPERATION_NOT_SUPPORTED,
            code=ErrorCode.INVALID_OPERATION,
            details={
                "operation": "get_recipe_by_id",
                "provider": self.source_name,
                "reason": "Recipe Puppy API does not support direct recipe lookup",
            },
        )

    def _normalize_recipe(self, raw_recipe: ProviderRecipeData) -> RecipeSearchResult:
        """Convert Recipe Puppy data to standard format.

        Args:
            raw_recipe: Raw recipe data from Recipe Puppy API

        Returns:
            RecipeSearchResult: Normalized recipe data
        """
        # Split ingredients string into list
        ingredients = [ing.strip() for ing in raw_recipe.get("ingredients", "").split(",") if ing.strip()]

        # Generate a stable ID from the title and URL
        recipe_id = str(hash(f"{raw_recipe.get('title', '')}{raw_recipe.get('href', '')}"))

        return RecipeSearchResult(
            id=recipe_id,
            title=raw_recipe.get("title", ""),
            description=None,  # Recipe Puppy doesn't provide descriptions
            image_url=raw_recipe.get("thumbnail"),
            source_url=raw_recipe.get("href"),
            prep_time=None,  # Recipe Puppy doesn't provide timing info
            cook_time=None,
            total_time=None,
            servings=None,  # Recipe Puppy doesn't provide serving info
            cuisine=None,  # Recipe Puppy doesn't provide cuisine info
            diet=None,  # Recipe Puppy doesn't provide diet info
            ingredients=ingredients,
            instructions=[],  # Recipe Puppy doesn't provide instructions
            source=self.source_name,
        )
