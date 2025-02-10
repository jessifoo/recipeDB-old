"""TheMealDB recipe provider implementation."""

from __future__ import annotations

from typing import TypedDict, cast

import httpx

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, DomainError, ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.base import ProviderRecipeData, RecipeProvider


class MealDBRecipe(TypedDict, total=False):
    """Type definition for TheMealDB recipe data."""

    idMeal: str
    strMeal: str
    strDrinkAlternate: str | None
    strCategory: str
    strArea: str
    strInstructions: str
    strMealThumb: str
    strTags: str
    strYoutube: str
    strSource: str
    strImageSource: str
    strCreativeCommonsConfirmed: str | None
    dateModified: str | None
    # Dynamic fields for ingredients and measures (1-20)
    strIngredient1: str
    strIngredient2: str
    strIngredient3: str
    strIngredient4: str
    strIngredient5: str
    strIngredient6: str
    strIngredient7: str
    strIngredient8: str
    strIngredient9: str
    strIngredient10: str
    strIngredient11: str
    strIngredient12: str
    strIngredient13: str
    strIngredient14: str
    strIngredient15: str
    strIngredient16: str
    strIngredient17: str
    strIngredient18: str
    strIngredient19: str
    strIngredient20: str
    strMeasure1: str
    strMeasure2: str
    strMeasure3: str
    strMeasure4: str
    strMeasure5: str
    strMeasure6: str
    strMeasure7: str
    strMeasure8: str
    strMeasure9: str
    strMeasure10: str
    strMeasure11: str
    strMeasure12: str
    strMeasure13: str
    strMeasure14: str
    strMeasure15: str
    strMeasure16: str
    strMeasure17: str
    strMeasure18: str
    strMeasure19: str
    strMeasure20: str


class MealDBProvider(RecipeProvider):
    """TheMealDB recipe provider implementation."""

    BASE_URL = "https://www.themealdb.com/api/json/v1/1"  # Free tier API

    def __init__(self) -> None:
        """Initialize TheMealDB provider."""
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
        """Search for recipes using TheMealDB API.

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
        try:
            # TheMealDB only supports name search
            response = await self.client.get("/search.php", params={"s": query})
            response.raise_for_status()
            data = response.json()
            recipes = cast(list[ProviderRecipeData], data.get("meals", []) or [])

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

            return RecipeList(total=len(results), results=paginated_results, source=self.source_name)

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "TheMealDB", "status_code": e.response.status_code, "error": str(e)},
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
            response = await self.client.get("/lookup.php", params={"i": recipe_id})
            response.raise_for_status()
            data = response.json()

            if not data.get("meals"):
                raise ValidationError(
                    message_template=ErrorMessages.RECIPE_NOT_FOUND,
                    code=ErrorCode.RECIPE_NOT_FOUND,
                    details={"recipe_id": recipe_id},
                )

            recipe = cast(ProviderRecipeData, data["meals"][0])
            recipe_result = self._normalize_recipe(recipe)

            # Check for allergens
            if not self._filter_allergens(recipe_result):
                raise BusinessError(
                    message_template=ErrorMessages.RECIPE_CONTAINS_ALLERGENS,
                    code=ErrorCode.ALLERGEN_CONFLICT,
                    details={"recipe_id": recipe_id, "allergens": self.DEFAULT_ALLERGENS},
                )

            return recipe_result

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "TheMealDB", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except (ValidationError, BusinessError):
            raise
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_FETCH_FAILED,
                code=ErrorCode.API_ERROR,
                details={"recipe_id": recipe_id, "error": str(e)},
            ) from e

    def _normalize_recipe(self, raw_recipe: ProviderRecipeData) -> RecipeSearchResult:
        """Convert TheMealDB recipe data to standard format.

        Args:
            raw_recipe: Raw recipe data from TheMealDB API

        Returns:
            RecipeSearchResult: Normalized recipe data
        """
        # Extract ingredients and measurements
        ingredients: list[str] = []
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
        diets: list[str] = []
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
