"""Recipe endpoints."""
"""what the fuck is this file? don't be creating shit int he wrong spot, we have routes/"""
from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, ValidationError
from app.models.models import Recipe, RecipeRating
from app.schemas.recipe import (
    RecipeCreate,
    RecipeList,
    RecipeRatingCreate,
    RecipeResponse,
    RecipeSearchResult,
)
from app.services.recipe_search import RecipeSearchService

router = APIRouter()


@router.get("/search", response_model=RecipeList)
async def search_recipes(
    query: Annotated[str, Query(description="Search query string")],
    offset: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    cuisine: Annotated[str | None, Query(description="Filter by cuisine type")] = None,
    diet: Annotated[str | None, Query(description="Filter by diet type")] = None,
    exclude: Annotated[list[str] | None, Query(description="Ingredients to exclude")] = None,
    max_time: Annotated[int | None, Query(ge=0, description="Maximum cooking time in minutes")] = None,
    service: Annotated[str | None, Query(description="Specific service to search")] = None,
    cooking_method: Annotated[str | None, Query(description="Filter by cooking method")] = None,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> RecipeList:
    """Search for recipes across all providers.

    Args:
        query: Search query string
        offset: Number of results to skip
        limit: Maximum number of results to return
        cuisine: Filter by cuisine type
        diet: Filter by diet type
        exclude: List of ingredients to exclude
        max_time: Maximum cooking time in minutes
        service: Specific service to search
        cooking_method: Filter by cooking method
        db: Database session

    Returns:
        RecipeList: List of recipes matching the search criteria

    Raises:
        BusinessError: If no recipes match the criteria
    """
    search_service = RecipeSearchService(db)
    return await search_service.search(
        query=query,
        offset=offset,
        limit=limit,
        cuisine=cuisine,
        diet=diet,
        exclude=exclude,
        max_time=max_time,
        service=service,
        cooking_method=cooking_method,
    )


@router.post("/save", response_model=RecipeResponse)
async def save_recipe(
    recipe: Annotated[RecipeSearchResult, "Recipe to save"],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> Recipe:
    """Save a recipe to the local database.

    This endpoint saves a recipe from an external provider to the local database
    for future reference. It performs allergen checks and normalizes the data
    before saving.

    Args:
        recipe: Recipe to save
        db: Database session

    Returns:
        Recipe: Saved recipe model

    Raises:
        BusinessError: If the recipe contains allergens
        ValidationError: If the recipe data is invalid
    """
    search_service = RecipeSearchService(db)
    return await search_service.save_recipe(recipe)


@router.post("/{recipe_id}/rate", response_model=RecipeRating)
async def rate_recipe(
    recipe_id: Annotated[int, Path(description="Recipe ID")],
    rating: Annotated[RecipeRatingCreate, "Rating details"],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> RecipeRating:
    """Rate a recipe and optionally add a review.

    Args:
        recipe_id: ID of the recipe to rate
        rating: Rating details
        db: Database session

    Returns:
        RecipeRating: Created rating

    Raises:
        ValidationError: If the recipe ID is invalid
        BusinessError: If the recipe is not found
    """
    # Verify recipe exists
    recipe = await db.get(Recipe, recipe_id)
    if not recipe:
        raise ValidationError(
            message_template=ErrorMessages.RECIPE_NOT_FOUND,
            code=ErrorCode.NOT_FOUND,
            details={"recipe_id": recipe_id},
        )

    # Create rating
    db_rating = RecipeRating(
        recipe_id=recipe_id,
        member_id=rating.member_id,
        rating=rating.rating,
        review=rating.review,
    )

    try:
        db.add(db_rating)
        await db.commit()
        await db.refresh(db_rating)
        return db_rating

    except Exception as e:
        raise BusinessError(
            message_template=ErrorMessages.RATING_FAILED,
            code=ErrorCode.DATABASE_ERROR,
            details={"recipe_id": recipe_id, "error": str(e)},
        )


@router.get("/{recipe_id}/ratings", response_model=list[RecipeRating])
async def get_recipe_ratings(
    recipe_id: Annotated[int, Path(description="Recipe ID")],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> list[RecipeRating]:
    """Get all ratings for a recipe.

    Args:
        recipe_id: ID of the recipe
        db: Database session

    Returns:
        list[RecipeRating]: List of ratings for the recipe

    Raises:
        ValidationError: If the recipe ID is invalid
        BusinessError: If the recipe is not found
    """
    # Verify recipe exists
    recipe = await db.get(Recipe, recipe_id)
    if not recipe:
        raise ValidationError(
            message_template=ErrorMessages.RECIPE_NOT_FOUND,
            code=ErrorCode.NOT_FOUND,
            details={"recipe_id": recipe_id},
        )

    # Get ratings
    from sqlalchemy import select

    stmt = select(RecipeRating).where(RecipeRating.recipe_id == recipe_id)
    result = await db.execute(stmt)
    return result.scalars().all()
