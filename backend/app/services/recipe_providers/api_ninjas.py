"""API Ninjas recipe provider implementation."""

from __future__ import annotations

from typing import Any, cast

import httpx

from app.core.config import settings
from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import DomainError, ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.base import ProviderRecipeData, RecipeProvider


class APINinjasProvider(RecipeProvider):
    """API Ninjas recipe provider implementation."""

    BASE_URL = "https://api.api-ninjas.com/v1"

    def __init__(self) -> None:
        """Initialize the API Ninjas provider.

        Raises:
            ValidationError: If API key is not configured.
        """
        if not settings.API_NINJAS_API_KEY:
            raise ValidationError(
                message_template=ErrorMessages.INVALID_CREDENTIALS,
                code=ErrorCode.VALIDATION_ERROR,
                details={"provider": "api_ninjas"},
            )

        super().__init__(api_key=settings.API_NINJAS_API_KEY)
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL, headers={"X-Api-Key": self.api_key} if self.api_key else {}, timeout=30.0
        )

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
        """Search for recipes using the API Ninjas API.

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
        params: dict[str, Any] = {"query": query, "offset": offset, "limit": limit}

        try:
            response = await self.client.get("/recipes", params=params)
            response.raise_for_status()
            recipes = cast(list[ProviderRecipeData], response.json())

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply allergen filtering first
            results = self._apply_allergen_filtering(results)

            # Apply additional filters
            if cuisine:
                results = [r for r in results if r.cuisine and cuisine.lower() in r.cuisine.lower()]
            if diet:
                results = [r for r in results if r.diet and diet in r.diet]
            if exclude:
                results = [
                    r
                    for r in results
                    if not any(excluded in " ".join(r.ingredients or []).lower() for excluded in exclude)
                ]
            if max_time:
                results = [r for r in results if r.total_time and r.total_time <= max_time]

            return RecipeList(total=len(results), results=results[:limit], source=self.source_name)

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "API Ninjas", "status_code": e.response.status_code, "error": str(e)},
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
        # API Ninjas doesn't support direct recipe lookup by ID
        raise ValidationError(
            message_template=ErrorMessages.OPERATION_NOT_SUPPORTED,
            code=ErrorCode.INVALID_OPERATION,
            details={
                "operation": "get_recipe_by_id",
                "provider": self.source_name,
                "reason": "API Ninjas does not support direct recipe lookup",
            },
        )

    def _normalize_recipe(self, raw_recipe: ProviderRecipeData) -> RecipeSearchResult:
        """Convert API Ninjas recipe data to standard format.

        Args:
            raw_recipe: Raw recipe data from API Ninjas API

        Returns:
            RecipeSearchResult: Normalized recipe data
        """
        # Split instructions into steps
        instructions = [step.strip() for step in raw_recipe.get("instructions", "").split(".") if step.strip()]

        # Split ingredients into list
        ingredients = [ing.strip() for ing in raw_recipe.get("ingredients", "").split(",") if ing.strip()]

        return RecipeSearchResult(
            id=str(hash(raw_recipe.get("title", ""))),  # Generate stable ID from title
            title=raw_recipe.get("title", ""),
            description=None,  # API Ninjas doesn't provide descriptions
            image_url=None,  # API Ninjas doesn't provide images
            source_url=None,  # API Ninjas doesn't provide source URLs
            prep_time=None,  # API Ninjas doesn't separate prep/cook time
            cook_time=raw_recipe.get("cooking_time"),
            total_time=raw_recipe.get("cooking_time"),
            servings=raw_recipe.get("servings"),
            cuisine=None,  # API Ninjas doesn't provide cuisine info
            diet=None,  # API Ninjas doesn't provide diet info
            ingredients=ingredients,
            instructions=instructions,
            source=self.source_name,
        )
