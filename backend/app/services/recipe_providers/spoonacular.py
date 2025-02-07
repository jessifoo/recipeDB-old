"""Spoonacular recipe provider implementation.

This module provides integration with the Spoonacular Recipe API.
It handles recipe search, retrieval, and data normalization.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final, cast

import httpx
from typing_extensions import override

from app.core.config import settings
from app.core.constants import ErrorMessages
from app.core.http_exceptions import ExternalServiceException, ValidationException
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.base import RecipeProvider

if TYPE_CHECKING:
    from collections.abc import Sequence


class SpoonacularProvider(RecipeProvider):
    """Spoonacular recipe provider implementation.

    This class implements the RecipeProvider interface for the Spoonacular API.
    It provides methods for searching recipes and retrieving recipe details.

    Attributes:
        BASE_URL: The base URL for the Spoonacular API.
        source_name: The name identifier for this provider.
        _SUPPORTED_ALLERGENS: List of allergens directly supported by Spoonacular.
        _DEFAULT_TIMEOUT: Default timeout for API requests in seconds.
    """

    BASE_URL: Final[str] = "https://api.spoonacular.com"
    source_name: Final[str] = "spoonacular"

    _SUPPORTED_ALLERGENS: Final[list[str]] = ["dairy", "egg"]
    _DEFAULT_TIMEOUT: Final[float] = 30.0

    def __init__(self) -> None:
        """Initialize the Spoonacular provider.

        Raises:
            ValueError: If the Spoonacular API key is not configured.
        """
        if not settings.SPOONACULAR_API_KEY:
            raise ValueError(ErrorMessages.INVALID_CREDENTIALS)

        super().__init__(api_key=settings.SPOONACULAR_API_KEY)
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL, params={"apiKey": self.api_key}, timeout=self._DEFAULT_TIMEOUT
        )

    @override
    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: Sequence[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search for recipes using the Spoonacular API.

        Args:
            query: Search query string.
            offset: Number of results to skip.
            limit: Maximum number of results to return.
            cuisine: Filter by cuisine type.
            diet: Filter by diet type.
            exclude: List of ingredients to exclude.
            max_time: Maximum total cooking time in minutes.

        Returns:
            RecipeList containing search results.

        Raises:
            ExternalServiceException: If the API request fails.
        """
        params: dict[str, Any] = {
            "query": query,
            "offset": offset,
            "number": limit,
            "intolerances": ",".join(self._SUPPORTED_ALLERGENS),
            "addRecipeInformation": True,  # Get full recipe details
            "fillIngredients": True,  # Get detailed ingredient info
            "instructionsRequired": True,  # Only recipes with instructions
        }

        if cuisine:
            params["cuisine"] = cuisine
        if diet:
            params["diet"] = diet
        if exclude:
            params["excludeIngredients"] = ",".join(exclude)
        if max_time:
            params["maxReadyTime"] = max_time

        try:
            response = await self.client.get("/recipes/complexSearch", params=params)
            response.raise_for_status()
            data = cast(dict[str, Any], response.json())
            recipes = data.get("results", [])

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply additional allergen filtering for soy and any missed items
            results = self._apply_allergen_filtering(results)

            return RecipeList(
                total=data.get("totalResults", len(results)), results=results[:limit], source=self.source_name
            )

        except httpx.HTTPStatusError as e:
            raise ExternalServiceException(
                ErrorMessages.EXTERNAL_SERVICE_ERROR.format(service="Spoonacular", details=str(e)),
                status_code=e.response.status_code,
            ) from e
        except Exception as e:
            raise ExternalServiceException(ErrorMessages.RECIPE_SEARCH_FAILED.format(details=str(e))) from e

    @override
    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Args:
            recipe_id: The Spoonacular recipe ID.

        Returns:
            RecipeSearchResult containing the recipe details.

        Raises:
            ExternalServiceException: If the API request fails.
            ValidationException: If the recipe contains allergens.
        """
        try:
            response = await self.client.get(
                f"/recipes/{recipe_id}/information",
                params={
                    "includeNutrition": False  # Skip nutrition data to reduce API points
                },
            )
            response.raise_for_status()
            recipe_data = cast(dict[str, Any], response.json())

            recipe = self._normalize_recipe(recipe_data)

            # Check for allergens
            if not self._filter_allergens(recipe):
                raise ValidationException(ErrorMessages.RECIPE_CONTAINS_ALLERGENS)

            return recipe

        except httpx.HTTPStatusError as e:
            raise ExternalServiceException(
                ErrorMessages.EXTERNAL_SERVICE_ERROR.format(service="Spoonacular", details=str(e)),
                status_code=e.response.status_code,
            ) from e
        except ValidationException:
            raise
        except Exception as e:
            raise ExternalServiceException(ErrorMessages.RECIPE_FETCH_FAILED.format(details=str(e))) from e

    def _normalize_recipe(self, raw_recipe: dict[str, Any]) -> RecipeSearchResult:
        """Convert Spoonacular recipe data to standard format.

        Args:
            raw_recipe: Raw recipe data from Spoonacular API.

        Returns:
            Normalized RecipeSearchResult object.
        """
        # Extract ingredients
        ingredients: list[str] = []
        for ingredient in raw_recipe.get("extendedIngredients", []):
            if original := ingredient.get("original"):
                ingredients.append(original)

        # Extract instructions
        instructions: list[str] = []
        for step in raw_recipe.get("analyzedInstructions", []):
            for step_detail in step.get("steps", []):
                if step_text := step_detail.get("step"):
                    instructions.append(step_text)

        # Extract diets
        diets: list[str] = []
        if raw_recipe.get("vegetarian"):
            diets.append("vegetarian")
        if raw_recipe.get("vegan"):
            diets.append("vegan")
        if raw_recipe.get("glutenFree"):
            diets.append("gluten-free")
        if raw_recipe.get("dairyFree"):
            diets.append("dairy-free")

        return RecipeSearchResult(
            id=str(raw_recipe.get("id", "")),
            title=raw_recipe.get("title", ""),
            description=raw_recipe.get("summary"),  # HTML summary
            image_url=raw_recipe.get("image"),
            source_url=raw_recipe.get("sourceUrl"),
            prep_time=raw_recipe.get("preparationMinutes"),
            cook_time=raw_recipe.get("cookingMinutes"),
            total_time=raw_recipe.get("readyInMinutes"),
            servings=raw_recipe.get("servings"),
            cuisine=raw_recipe.get("cuisines", [None])[0],  # Take first cuisine if available
            diet=diets,
            ingredients=ingredients,
            instructions=instructions,
            source=self.source_name,
        )
