"""Recipe search service.

This module provides functionality for searching recipes across multiple external services
and storing safe recipes locally.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sqlalchemy import and_, func, or_, select

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, DatabaseError
from app.models.models import CookMethod, Recipe
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.factory import RecipeProviderFactory

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class RecipeSearchService:
    """Service for searching recipes across multiple sources."""

    def __init__(self, db: AsyncSession) -> None:
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
        cooking_method: str | None = None,
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
            cooking_method: Filter by cooking method (e.g., 'instant_pot', 'slow_cooker')

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            DatabaseError: If the database operation fails
            BusinessError: If no recipes match the criteria
        """
        try:
            # Extract cooking method from query if not explicitly provided
            if not cooking_method:
                # Create a temporary provider to use its method detection
                temp_provider = self.provider_factory.get_provider("spoonacular")
                cooking_method = temp_provider._detect_cooking_method(query)

            # If a specific service is requested, use only that provider
            if service:
                provider = self.provider_factory.get_provider(service)
                results = await provider.search_recipes(
                    query=query,
                    offset=offset or 0,
                    limit=limit or 100,
                    cuisine=cuisine,
                    diet=diet,
                    exclude=exclude,
                    max_time=max_time,
                )

                # Apply cooking method filter if specified
                if cooking_method:
                    filtered_results = []
                    for recipe in results.results:
                        recipe_text = " ".join(
                            [recipe.title, recipe.description or "", " ".join(recipe.instructions or [])]
                        )
                        if provider._detect_cooking_method(recipe_text) == cooking_method:
                            filtered_results.append(recipe)
                    results.results = filtered_results
                    results.total = len(filtered_results)

                return results

            # Search local database first
            local_results = await self._search_local(
                query=query, filters=filters, offset=offset, limit=limit, cooking_method=cooking_method
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

                            # Apply cooking method filter if specified
                            if cooking_method:
                                filtered_results = []
                                for recipe in provider_results.results:
                                    recipe_text = " ".join(
                                        [recipe.title, recipe.description or "", " ".join(recipe.instructions or [])]
                                    )
                                    if provider._detect_cooking_method(recipe_text) == cooking_method:
                                        filtered_results.append(recipe)
                                provider_results.results = filtered_results
                                provider_results.total = len(filtered_results)

                            all_results.extend(provider_results.results)
                            remaining_limit -= len(provider_results.results)
                            if remaining_limit <= 0:
                                break
                        except Exception:
                            # Log error but continue with other providers
                            continue

                if not all_results:
                    raise BusinessError(
                        message_template=ErrorMessages.NO_RECIPES_FOUND,
                        code=ErrorCode.NOT_FOUND,
                        details={"query": query, "cooking_method": cooking_method, "filters": filters},
                    )

                return RecipeList(
                    total=len(all_results), results=all_results[:limit] if limit else all_results, source="all"
                )

            except BusinessError:
                raise
            except Exception:
                # If external search fails, return local results
                return local_results

        except BusinessError:
            raise
        except Exception as e:
            raise DatabaseError.from_sqlalchemy(
                error=e,
                operation="search_recipes",
                details={"query": query, "filters": filters, "service": service, "cooking_method": cooking_method},
            ) from e

    async def _search_local(
        self,
        query: str,
        filters: dict[str, Any] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        cooking_method: str | None = None,
    ) -> RecipeList:
        """Search local database for recipes.

        Args:
            query: Search query string
            filters: Additional filters to apply
            offset: Number of results to skip
            limit: Maximum number of results to return
            cooking_method: Filter by cooking method

        Returns:
            RecipeList: List of recipes matching the search criteria
        """
        # Build the base query
        stmt = select(Recipe).where(or_(Recipe.title.ilike(f"%{query}%"), Recipe.variations.ilike(f"%{query}%")))

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

        # Apply cooking method filter
        if cooking_method:
            stmt = stmt.join(Recipe.cook_methods).filter(CookMethod.name == cooking_method)

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

        return RecipeList(total=len(results), results=results, source="local")

    async def save_recipe(self, recipe: RecipeSearchResult) -> Recipe:
        """Save a recipe to the local database.

        Args:
            recipe: Recipe to save

        Returns:
            Recipe: Saved recipe model

        Raises:
            DatabaseError: If the database operation fails
            BusinessError: If the recipe contains allergens
        """
        try:
            # Create a temporary provider to check allergens
            temp_provider = self.provider_factory.get_provider("spoonacular")
            if not temp_provider._filter_allergens(recipe):
                raise BusinessError(
                    message_template=ErrorMessages.RECIPE_CONTAINS_ALLERGENS,
                    code=ErrorCode.ALLERGEN_CONFLICT,
                    details={"recipe_id": recipe.id, "title": recipe.title},
                )

            # Create new recipe
            db_recipe = Recipe(
                title=recipe.title,
                variations=recipe.description,
                image_url=recipe.image_url,
                source_url=recipe.source_url,
                prep_time_minutes=recipe.prep_time,
                cook_time_minutes=recipe.cook_time,
                servings=recipe.servings,
            )

            # Add ingredients
            if recipe.ingredients:
                for ing_name in recipe.ingredients:
                    ingredient = await self._get_or_create_ingredient(ing_name)
                    db_recipe.ingredients.append(ingredient)

            # Add instructions
            if recipe.instructions:
                from app.models import RecipeInstruction

                for i, instruction in enumerate(recipe.instructions, 1):
                    db_recipe.instructions.append(RecipeInstruction(step_number=i, instruction=instruction))

            # Add cuisine type if present
            if recipe.cuisine:
                cuisine = await self._get_or_create_cuisine(recipe.cuisine)
                db_recipe.cuisine_types.append(cuisine)

            # Detect and add cooking method
            recipe_text = " ".join([recipe.title, recipe.description or "", " ".join(recipe.instructions or [])])
            if method := temp_provider._detect_cooking_method(recipe_text):
                cook_method = await self._get_or_create_cook_method(method)
                db_recipe.cook_methods.append(cook_method)

            self.db.add(db_recipe)
            await self.db.commit()
            await self.db.refresh(db_recipe)

            return db_recipe

        except BusinessError:
            raise
        except Exception as e:
            raise DatabaseError.from_sqlalchemy(
                error=e, operation="save_recipe", details={"recipe_id": recipe.id, "title": recipe.title}
            ) from e

    async def _get_or_create_ingredient(self, name: str) -> Any:
        """Get or create an ingredient by name."""
        from app.models import Ingredient

        stmt = select(Ingredient).where(Ingredient.name == name)
        result = await self.db.execute(stmt)
        ingredient = result.scalar_one_or_none()
        if not ingredient:
            ingredient = Ingredient(name=name)
            self.db.add(ingredient)
        return ingredient

    async def _get_or_create_cuisine(self, name: str) -> Any:
        """Get or create a cuisine type by name."""
        from app.models import CuisineType

        stmt = select(CuisineType).where(CuisineType.name == name)
        result = await self.db.execute(stmt)
        cuisine = result.scalar_one_or_none()
        if not cuisine:
            cuisine = CuisineType(name=name)
            self.db.add(cuisine)
        return cuisine

    async def _get_or_create_cook_method(self, name: str) -> Any:
        """Get or create a cooking method by name."""
        from app.models import CookMethod

        stmt = select(CookMethod).where(CookMethod.name == name)
        result = await self.db.execute(stmt)
        method = result.scalar_one_or_none()
        if not method:
            method = CookMethod(name=name)
            self.db.add(method)
        return method

    async def count_search_results(self, query: str, filters: dict[str, Any] | None = None) -> int:
        """Count total number of recipes matching the search criteria.

        Args:
            query: Search query string
            filters: Additional filters to apply

        Returns:
            Total number of matching recipes
        """
        # Build the base query
        stmt = (
            select(func.count())
            .select_from(Recipe)
            .where(or_(Recipe.title.ilike(f"%{query}%"), Recipe.variations.ilike(f"%{query}%")))
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

        # Execute query
        result = await self.db.execute(stmt)
        return result.scalar_one()
