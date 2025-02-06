"""Recipe search service.

This module provides functionality for searching recipes across multiple external services.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sqlalchemy import and_, or_, select

from app.models.models import Recipe
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.exceptions import APIError
from app.services.recipe_providers.factory import RecipeProviderFactory

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class RecipeSearchService:
    """Service for searching recipes across multiple sources."""

    def __init__(self, db: AsyncSession):
        """Initialize the recipe search service.

        Args:
            db: Database session
        """
        self.db = db
        self.provider_factory = RecipeProviderFactory()

    async def search(
        self,
        query: str,
        filters: dict[str, Any] | None = None,
        offset: int | None = None,
        limit: int | None = 100,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
        service: str | None = None,
    ) -> RecipeList:
        """Search for recipes across multiple services.

        Args:
            query: Search query string
            filters: Additional filters to apply
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude: List of ingredients to exclude
            max_time: Maximum cooking time in minutes
            service: Specific service to search (e.g., 'spoonacular', 'edamam')

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            APIError: If the recipe search fails
        """
        try:
            # If a specific service is requested, use only that provider
            if service:
                provider = self.provider_factory.get_provider(service)
                return await provider.search_recipes(
                    query=query,
                    offset=offset or 0,
                    limit=limit or 100,
                    cuisine=cuisine,
                    diet=diet,
                    exclude=exclude,
                    max_time=max_time,
                )

            # Otherwise, search local database first
            local_results = await self._search_local(
                query=query,
                filters=filters,
                offset=offset,
                limit=limit,
            )

            # If we have enough local results or external providers are disabled,
            # return local results only
            if local_results.total >= (limit or 100):
                return local_results

            # Search external providers
            try:
                providers = self.provider_factory.get_all_providers()
                all_results: list[RecipeSearchResult] = []

                # Add local results first
                all_results.extend(local_results.results)

                # Search each provider
                remaining_limit = (limit or 100) - len(all_results)
                if remaining_limit > 0:
                    for provider in providers:
                        try:
                            provider_results = await provider.search_recipes(
                                query=query,
                                offset=0,  # Start from beginning for each provider
                                limit=remaining_limit,
                                cuisine=cuisine,
                                diet=diet,
                                exclude=exclude,
                                max_time=max_time,
                            )
                            all_results.extend(provider_results.results)
                            remaining_limit -= len(provider_results.results)
                            if remaining_limit <= 0:
                                break
                        except Exception:
                            # Log error but continue with other providers
                            continue

                return RecipeList(
                    total=len(all_results),
                    results=all_results[:limit] if limit else all_results,
                    source="all",
                )

            except Exception:
                # If external search fails, return local results
                return local_results

        except Exception as e:
            raise APIError(f"Recipe search failed: {e!s}")

    async def _search_local(
        self,
        query: str,
        filters: dict[str, Any] | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> RecipeList:
        """Search local database for recipes.

        Args:
            query: Search query string
            filters: Additional filters to apply
            offset: Number of results to skip
            limit: Maximum number of results to return

        Returns:
            RecipeList: List of recipes matching the search criteria
        """
        # Build the base query
        stmt = select(Recipe).where(
            or_(
                Recipe.title.ilike(f"%{query}%"),
                Recipe.variations.ilike(f"%{query}%"),
            ),
        )

        # Apply filters
        if filters:
            if cuisine_type := filters.get("cuisine_type"):
                stmt = stmt.join(Recipe.cuisine_types).filter(Recipe.cuisine_types.any(name=cuisine_type))

            if max_cooking_time := filters.get("max_cooking_time"):
                stmt = stmt.filter(Recipe.cook_time_minutes <= max_cooking_time)

            if allergens_exclude := filters.get("allergens_exclude"):
                # Create a list of conditions for each allergen to exclude
                allergen_conditions = [~Recipe.allergens.any(name=allergen) for allergen in allergens_exclude]
                # Combine conditions with AND
                if allergen_conditions:
                    stmt = stmt.filter(and_(*allergen_conditions))

        # Apply pagination
        if offset:
            stmt = stmt.offset(offset)
        if limit:
            stmt = stmt.limit(limit)

        # Execute query
        result = await self.db.execute(stmt)
        recipes = result.scalars().all()

        # Convert to search results
        results = [
            RecipeSearchResult(
                id=str(recipe.recipe_id),
                title=recipe.title,
                description=recipe.variations,
                image_url=recipe.image_url,
                source_url=recipe.source_url,
                prep_time=recipe.prep_time_minutes,
                cook_time=recipe.cook_time_minutes,
                total_time=(recipe.prep_time_minutes or 0) + (recipe.cook_time_minutes or 0),
                servings=recipe.servings,
                cuisine=recipe.cuisine_types[0].name if recipe.cuisine_types else None,
                diet=[],  # TODO: Implement diet types
                ingredients=[i.name for i in recipe.ingredients],
                instructions=[i.instruction for i in recipe.instructions],
                source="local",
            )
            for recipe in recipes
        ]

        return RecipeList(
            total=len(results),
            results=results,
            source="local",
        )
