"""Recipe Puppy provider implementation."""

from __future__ import annotations

from typing import Any

import httpx
from fastapi import HTTPException

from app.schemas.recipe import RecipeList, RecipeSearchResult

from .base import RecipeProvider


class RecipePuppyProvider(RecipeProvider):
    """Recipe Puppy provider implementation."""

    BASE_URL = "http://www.recipepuppy.com/api"

    def __init__(self) -> None:
        """Initialize Recipe Puppy provider."""
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
        """Search for recipes using Recipe Puppy API."""
        # Calculate page number (Recipe Puppy uses 10 results per page)
        page = (offset // 10) + 1

        params: dict[str, Any] = {
            "q": query,
            "p": page,
        }

        # Add ingredients to exclude
        if exclude:
            params["excludedIngredients"] = ",".join(exclude)

        try:
            response = await self.client.get("/", params=params)
            response.raise_for_status()
            data = response.json()
            recipes = data.get("results", [])

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
            status_code = e.response.status_code
            raise HTTPException(
                status_code=status_code,
                detail=f"Recipe Puppy API error: {e!s}",
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to search recipes: {e!s}",
            )

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Note: Recipe Puppy doesn't support retrieving recipes by ID,
        so we'll search by title and return the first match.
        """
        try:
            response = await self.client.get("/", params={"q": recipe_id})
            response.raise_for_status()
            data = response.json()
            recipes = data.get("results", [])

            if not recipes:
                raise HTTPException(
                    status_code=404,
                    detail=f"Recipe not found: {recipe_id}",
                )

            recipe = self._normalize_recipe(recipes[0])

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
                detail=f"Recipe Puppy API error: {e!s}",
            )
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to get recipe: {e!s}",
            )

    def _normalize_recipe(self, raw_recipe: dict[str, Any]) -> RecipeSearchResult:
        """Convert Recipe Puppy data to standard format."""
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
