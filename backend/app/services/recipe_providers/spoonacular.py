"""Spoonacular recipe provider."""

from __future__ import annotations

from typing import Any

import httpx

from app.core.config import settings
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.exceptions import ExternalAPIError, RecipeFilterError, RecipeProviderError

from .base import RecipeProvider


class SpoonacularProvider(RecipeProvider):
    """Spoonacular recipe provider implementation."""

    BASE_URL = "https://api.spoonacular.com"

    def __init__(self) -> None:
        """Initialize the Spoonacular provider."""
        super().__init__(api_key=settings.SPOONACULAR_API_KEY)
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            params={"apiKey": self.api_key} if self.api_key else {},
            timeout=30.0,
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
        """Search for recipes using the Spoonacular API."""
        # Build intolerances string from default allergens
        intolerances = ["dairy", "egg"]  # Spoonacular supports these directly

        params: dict[str, Any] = {
            "query": query,
            "offset": offset,
            "number": limit,
            "intolerances": ",".join(intolerances),
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
            data = response.json()
            recipes = data.get("results", [])

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply additional allergen filtering for soy and any missed items
            results = self._apply_allergen_filtering(results)

            return RecipeList(
                total=data.get("totalResults", len(results)),
                results=results[:limit],
                source=self.source_name,
            )

        except httpx.HTTPStatusError as e:
            raise ExternalAPIError(
                f"Spoonacular API error: {e!s}",
                status_code=e.response.status_code,
            ) from e
        except Exception as e:
            raise RecipeProviderError(f"Failed to search recipes: {e!s}") from e

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID."""
        try:
            response = await self.client.get(
                f"/recipes/{recipe_id}/information",
                params={
                    "includeNutrition": False,  # Skip nutrition data to reduce API points
                },
            )
            response.raise_for_status()
            recipe_data = response.json()

            recipe = self._normalize_recipe(recipe_data)

            # Check for allergens
            if not self._filter_allergens(recipe):
                raise RecipeFilterError("Recipe contains allergens")

            return recipe

        except httpx.HTTPStatusError as e:
            raise ExternalAPIError(
                f"Spoonacular API error: {e!s}",
                status_code=e.response.status_code,
            ) from e
        except RecipeFilterError:
            raise
        except Exception as e:
            raise RecipeProviderError(f"Failed to get recipe: {e!s}") from e

    def _normalize_recipe(self, raw_recipe: dict[str, Any]) -> RecipeSearchResult:
        """Convert Spoonacular recipe data to standard format."""
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
