"""Edamam recipe provider."""

from __future__ import annotations

from typing import Any

import httpx

from app.core.config import settings
from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, DomainError, ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult

from .base import RecipeProvider


class EdamamProvider(RecipeProvider):
    """Edamam recipe provider implementation."""

    BASE_URL = "https://api.edamam.com"

    def __init__(self) -> None:
        """Initialize the Edamam provider.

        Raises:
            ValidationError: If API credentials are not configured.
        """
        super().__init__()
        if not settings.EDAMAM_APP_ID or not settings.EDAMAM_APP_KEY:
            raise ValidationError(
                message_template=ErrorMessages.INVALID_CREDENTIALS,
                code=ErrorCode.VALIDATION_ERROR,
                details={"provider": self.source_name},
            )
        self.app_id = settings.EDAMAM_APP_ID
        self.app_key = settings.EDAMAM_APP_KEY
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
        """Search for recipes using the Edamam API.

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
        # Build health labels for allergen filtering
        health_labels = ["dairy-free", "egg-free"]

        params: dict[str, Any] = {
            "q": query,
            "app_id": self.app_id,
            "app_key": self.app_key,
            "from": offset,
            "to": offset + limit,
            "health": health_labels,  # Apply allergen filters at API level
        }

        if cuisine:
            params["cuisineType"] = cuisine
        if diet:
            params["diet"] = diet
        if exclude:
            params["excluded"] = exclude
        if max_time:
            params["time"] = f"1-{max_time}"  # Format: min-max minutes

        try:
            response = await self.client.get("/api/recipes/v2", params=params)
            response.raise_for_status()
            data = response.json()
            hits = data.get("hits", [])

            # Convert recipes to standard format
            results = [self._normalize_recipe(hit["recipe"]) for hit in hits]

            # Apply additional allergen filtering for soy and any missed items
            results = self._apply_allergen_filtering(results)

            return RecipeList(total=data.get("count", len(results)), results=results[:limit], source=self.source_name)

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "Edamam", "status_code": e.response.status_code, "error": str(e)},
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
        try:
            # Edamam uses URLs as IDs, so we need to decode it
            response = await self.client.get(
                recipe_id,  # Full URL from search results
                params={"app_id": self.app_id, "app_key": self.app_key, "type": "public"},
            )
            response.raise_for_status()
            recipe_data = response.json()["recipe"]

            recipe = self._normalize_recipe(recipe_data)

            # Check for allergens
            if not self._filter_allergens(recipe):
                raise BusinessError(
                    message_template=ErrorMessages.RECIPE_CONTAINS_ALLERGENS,
                    code=ErrorCode.ALLERGEN_CONFLICT,
                    details={"recipe_id": recipe_id, "allergens": self.DEFAULT_ALLERGENS},
                )

            return recipe

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise ValidationError(
                    message_template=ErrorMessages.RECIPE_NOT_FOUND,
                    code=ErrorCode.RECIPE_NOT_FOUND,
                    details={"recipe_id": recipe_id},
                ) from e
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "Edamam", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except BusinessError:
            raise
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_FETCH_FAILED,
                code=ErrorCode.API_ERROR,
                details={"recipe_id": recipe_id, "error": str(e)},
            ) from e

    def _normalize_recipe(self, raw_recipe: dict[str, Any]) -> RecipeSearchResult:
        """Convert Edamam recipe data to standard format."""
        # Extract cooking time
        total_time = raw_recipe.get("totalTime")
        if total_time and total_time > 0:
            prep_time = total_time * 0.3  # Estimate prep time as 30% of total
            cook_time = total_time * 0.7  # Estimate cook time as 70% of total
        else:
            prep_time = None
            cook_time = None

        # Extract diet labels
        diets: list[str] = []
        if raw_recipe.get("healthLabels"):
            for label in raw_recipe["healthLabels"]:
                label = label.lower()
                if any(d in label for d in ["vegetarian", "vegan", "pescatarian", "paleo", "keto"]):
                    diets.append(label)

        # Extract cuisine type
        cuisines = raw_recipe.get("cuisineType", [])
        cuisine = cuisines[0] if cuisines else None

        return RecipeSearchResult(
            id=raw_recipe.get("uri", "").split("#recipe_")[-1],  # Extract ID from URI
            title=raw_recipe.get("label", ""),
            description=raw_recipe.get("summary"),
            image_url=raw_recipe.get("image"),
            source_url=raw_recipe.get("url"),
            prep_time=prep_time,
            cook_time=cook_time,
            total_time=total_time if total_time and total_time > 0 else None,
            servings=raw_recipe.get("yield"),
            cuisine=cuisine,
            diet=diets,
            ingredients=[ing.get("text", "") for ing in raw_recipe.get("ingredients", [])],
            instructions=raw_recipe.get("instructionLines", []),  # Some recipes might not have instructions
            source=self.source_name,
        )
