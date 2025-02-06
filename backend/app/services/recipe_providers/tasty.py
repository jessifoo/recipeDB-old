"""Tasty recipe provider implementation."""

from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx
from fastapi import HTTPException

from app.core.config import settings
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.base import RecipeProvider


class TastyProvider(RecipeProvider):
    """Tasty recipe provider implementation."""

    BASE_URL = "https://tasty.p.rapidapi.com"

    def __init__(self) -> None:
        """Initialize the Tasty provider."""
        super().__init__(api_key=settings.TASTY_API_KEY)
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers=(
                {
                    "X-RapidAPI-Key": self.api_key,
                    "X-RapidAPI-Host": "tasty.p.rapidapi.com",
                }
                if self.api_key
                else {}
            ),
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
        """Search for recipes using the Tasty API."""
        params: dict[str, Any] = {
            "q": query,
            "from": offset,
            "size": limit,
            # Add dietary tags to API request for better filtering
            "tags": "dairy-free,egg-free",  # Tasty supports some dietary filters
        }

        try:
            response = await self.client.get("/recipes/list", params=params)
            response.raise_for_status()
            data = response.json()
            recipes = data.get("results", [])

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply allergen filtering as a safety check
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
                total=data.get("count", len(results)),
                results=results[:limit],
                source=self.source_name,
            )

        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code
            raise HTTPException(
                status_code=status_code,
                detail=f"Tasty API error: {e!s}",
            ) from e
        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=f"Failed to search recipes: {e!s}",
            ) from e

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID."""
        try:
            response = await self.client.get("/recipes/get-more-info", params={"id": recipe_id})
            response.raise_for_status()
            recipe_data = response.json()

            return self._normalize_recipe(recipe_data)

        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code
            raise HTTPException(
                status_code=status_code,
                detail=f"Tasty API error: {e!s}",
            ) from e
        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=f"Failed to get recipe: {e!s}",
            ) from e

    def _normalize_recipe(self, raw_recipe: dict[str, Any]) -> RecipeSearchResult:
        """Convert Tasty recipe data to standard format."""
        # Extract instructions from components and instructions
        instructions: list[str] = []
        for section in raw_recipe.get("instructions", []):
            if step := section.get("display_text"):
                instructions.append(step)

        # Extract ingredients from components and measurements
        ingredients: list[str] = []
        for section in raw_recipe.get("sections", []):
            for component in section.get("components", []):
                if ingredient := component.get("raw_text"):
                    ingredients.append(ingredient)

        # Calculate total time from prep and cook time
        prep_time = raw_recipe.get("prep_time_minutes")
        cook_time = raw_recipe.get("cook_time_minutes")
        total_time = (prep_time or 0) + (cook_time or 0) if prep_time or cook_time else None

        # Extract cuisine and diet tags
        tags = raw_recipe.get("tags", [])
        cuisine_tags = [tag.get("display_name") for tag in tags if tag.get("type") == "cuisine"]
        diet_tags: list[str] = [tag.get("display_name") for tag in tags if tag.get("type") == "dietary"]

        return RecipeSearchResult(
            id=str(raw_recipe.get("id", "")),
            title=raw_recipe.get("name", ""),
            description=raw_recipe.get("description"),
            image_url=raw_recipe.get("thumbnail_url"),
            source_url=raw_recipe.get("original_video_url"),  # Tasty focuses on video content
            prep_time=prep_time,
            cook_time=cook_time,
            total_time=total_time,
            servings=raw_recipe.get("num_servings"),
            cuisine=cuisine_tags[0] if cuisine_tags else None,
            diet=diet_tags,
            ingredients=ingredients,
            instructions=instructions,
            source=self.source_name,
        )
