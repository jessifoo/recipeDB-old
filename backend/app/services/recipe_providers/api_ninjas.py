"""API Ninjas recipe provider implementation."""

from __future__ import annotations

from typing import Any

import httpx
from fastapi import HTTPException

from app.core.config import settings
from app.schemas.recipe import RecipeList, RecipeSearchResult

from .base import RecipeProvider


class APINinjasProvider(RecipeProvider):
    """API Ninjas recipe provider implementation."""

    BASE_URL = "https://api.api-ninjas.com/v1"

    def __init__(self) -> None:
        """Initialize the API Ninjas provider."""
        super().__init__(api_key=settings.API_NINJAS_API_KEY)
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers={"X-Api-Key": self.api_key} if self.api_key else {},
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
        """Search for recipes using the API Ninjas API."""
        params: dict[str, Any] = {
            "query": query,
            "offset": offset,
            "limit": limit,
        }

        try:
            response = await self.client.get("/recipes", params=params)
            response.raise_for_status()
            recipes = response.json()

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

            return RecipeList(
                total=len(results),
                results=results[:limit],
                source=self.source_name,
            )

        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code
            raise HTTPException(
                status_code=status_code,
                detail=f"API Ninjas API error: {e!s}",
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to search recipes: {e!s}",
            )

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Note: API Ninjas doesn't support retrieving recipes by ID,
        so we'll search by title and return the first match.
        """
        try:
            response = await self.client.get("/recipes", params={"query": recipe_id})
            response.raise_for_status()
            recipes = response.json()

            if not recipes:
                raise HTTPException(
                    status_code=404,
                    detail=f"Recipe not found: {recipe_id}",
                )

            return self._normalize_recipe(recipes[0])

        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code
            raise HTTPException(
                status_code=status_code,
                detail=f"API Ninjas API error: {e!s}",
            )
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to get recipe: {e!s}",
            )

    def _normalize_recipe(self, raw_recipe: dict[str, Any]) -> RecipeSearchResult:
        """Convert API Ninjas recipe data to standard format."""
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
