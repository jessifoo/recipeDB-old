"""TheMealDB recipe provider implementation."""

from __future__ import annotations

from typing import Any

import httpx
from fastapi import HTTPException

from app.schemas.recipe import RecipeList, RecipeSearchResult

from .base import RecipeProvider


class MealDBProvider(RecipeProvider):
    """TheMealDB recipe provider implementation."""

    BASE_URL = "https://www.themealdb.com/api/json/v1/1"  # Free tier API

    def __init__(self) -> None:
        """Initialize TheMealDB provider."""
        super().__init__()
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL,
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
        """Search for recipes using TheMealDB API."""
        try:
            # TheMealDB only supports name search
            response = await self.client.get("/search.php", params={"s": query})
            response.raise_for_status()
            data = response.json()
            recipes = data.get("meals", []) or []

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply allergen filtering
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

            # Apply pagination
            start = offset
            end = offset + limit
            paginated_results = results[start:end]

            return RecipeList(
                total=len(results),
                results=paginated_results,
                source=self.source_name,
            )

        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code
            raise HTTPException(
                status_code=status_code,
                detail=f"TheMealDB API error: {e!s}",
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to search recipes: {e!s}",
            )

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID."""
        try:
            response = await self.client.get("/lookup.php", params={"i": recipe_id})
            response.raise_for_status()
            data = response.json()

            if not data.get("meals"):
                raise HTTPException(
                    status_code=404,
                    detail=f"Recipe not found: {recipe_id}",
                )

            recipe = self._normalize_recipe(data["meals"][0])

            # Check for allergens
            if not self._filter_allergens(recipe):
                raise HTTPException(
                    status_code=404,
                    detail="Recipe contains allergens",
                )

            return recipe

        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code
            raise HTTPException(
                status_code=status_code,
                detail=f"TheMealDB API error: {e!s}",
            )
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to get recipe: {e!s}",
            )

    def _normalize_recipe(self, raw_recipe: dict[str, Any]) -> RecipeSearchResult:
        """Convert TheMealDB recipe data to standard format."""
        # Extract ingredients and measurements
        ingredients = []
        for i in range(1, 21):  # TheMealDB has up to 20 ingredients
            ingredient = raw_recipe.get(f"strIngredient{i}")
            measure = raw_recipe.get(f"strMeasure{i}")
            if ingredient and ingredient.strip():
                ingredients.append(f"{measure} {ingredient}".strip())

        # Split instructions into steps
        instructions = [step.strip() for step in raw_recipe.get("strInstructions", "").split(".") if step.strip()]

        # Extract tags
        tags = []
        if raw_tags := raw_recipe.get("strTags"):
            tags = [tag.strip() for tag in raw_tags.split(",")]

        # Map category to diet if possible
        category = raw_recipe.get("strCategory", "").lower()
        diets = []
        if "vegetarian" in category or "vegetarian" in tags:
            diets.append("vegetarian")
        if "vegan" in category or "vegan" in tags:
            diets.append("vegan")

        return RecipeSearchResult(
            id=str(raw_recipe.get("idMeal", "")),
            title=raw_recipe.get("strMeal", ""),
            description=None,  # TheMealDB doesn't provide descriptions
            image_url=raw_recipe.get("strMealThumb"),
            source_url=raw_recipe.get("strSource"),
            prep_time=None,  # TheMealDB doesn't provide timing info
            cook_time=None,
            total_time=None,
            servings=None,  # TheMealDB doesn't provide serving info
            cuisine=raw_recipe.get("strArea"),  # Geographic origin
            diet=diets,
            ingredients=ingredients,
            instructions=instructions,
            source=self.source_name,
        )
