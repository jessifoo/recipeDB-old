"""Recipes router.

This module provides endpoints for managing recipes.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from app.database.session import get_async_db
from app.models.models import Recipe
from app.schemas.models import Recipe as RecipeSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.schemas.models import RecipeCreate

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Recipe not found",
            "content": {"application/json": {"example": {"detail": "Recipe not found"}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": "Recipe already exists",
            "content": {"application/json": {"example": {"detail": "Recipe with this title already exists"}}},
        },
    },
)


@router.post(
    "/",
    response_model=RecipeSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "Recipe created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "recipe_id": 1,
                        "title": "Spaghetti Carbonara",
                        "image_url": "https://example.com/carbonara.jpg",
                        "source_url": "https://example.com/recipes/carbonara",
                        "prep_time_minutes": 15,
                        "cook_time_minutes": 20,
                        "servings": 4,
                        "is_favorite": False,
                        "variations": "Can substitute pancetta with bacon",
                    },
                },
            },
        },
    },
)
async def create_recipe(
    recipe: RecipeCreate,
    db: AsyncSession = Depends(get_async_db),
) -> Recipe:
    """Create a new recipe.

    Args:
        recipe: Recipe data
        db: Database session

    Returns:
        Recipe: Created recipe

    Raises:
        HTTPException: If recipe already exists
    """
    try:
        db_recipe = Recipe(**recipe.model_dump())
        db.add(db_recipe)
        await db.commit()
        await db.refresh(db_recipe)
        return db_recipe
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Recipe with this title already exists",
        )


@router.get(
    "/",
    response_model=list[RecipeSchema],
    responses={status.HTTP_200_OK: {"description": "List of recipes retrieved successfully"}},
)
async def get_recipes(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_db),
) -> list[Recipe]:
    """Get a list of recipes with pagination."""
    result = await db.execute(select(Recipe).offset(skip).limit(limit))
    return list(result.scalars().all())


@router.get(
    "/{recipe_id}",
    response_model=RecipeSchema,
    responses={
        status.HTTP_200_OK: {
            "description": "Recipe retrieved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "recipe_id": 1,
                        "title": "Spaghetti Carbonara",
                        "image_url": "https://example.com/carbonara.jpg",
                        "source_url": "https://example.com/recipes/carbonara",
                        "prep_time_minutes": 15,
                        "cook_time_minutes": 20,
                        "servings": 4,
                        "is_favorite": False,
                        "variations": "Can substitute pancetta with bacon",
                    },
                },
            },
        },
    },
)
async def get_recipe(recipe_id: int, db: AsyncSession = Depends(get_async_db)) -> Recipe:
    """Get a specific recipe by ID.

    Args:
        recipe_id: ID of the recipe
        db: Database session

    Returns:
        Recipe: Recipe

    Raises:
        HTTPException: If recipe not found
    """
    result = await db.execute(Recipe.__table__.select().where(Recipe.recipe_id == recipe_id))
    db_recipe = result.scalar_one_or_none()
    if db_recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )
    return db_recipe


@router.put(
    "/{recipe_id}",
    response_model=RecipeSchema,
    responses={
        status.HTTP_200_OK: {
            "description": "Recipe updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "recipe_id": 1,
                        "title": "Spaghetti Carbonara",
                        "image_url": "https://example.com/carbonara.jpg",
                        "source_url": "https://example.com/recipes/carbonara",
                        "prep_time_minutes": 15,
                        "cook_time_minutes": 20,
                        "servings": 4,
                        "is_favorite": False,
                        "variations": "Can substitute pancetta with bacon",
                    },
                },
            },
        },
    },
)
async def update_recipe(
    recipe_id: int,
    recipe: RecipeCreate,
    db: AsyncSession = Depends(get_async_db),
) -> Recipe:
    """Update a specific recipe.

    Args:
        recipe_id: ID of the recipe to update
        recipe: Updated recipe data
        db: Database session

    Returns:
        Recipe: Updated recipe

    Raises:
        HTTPException: If recipe not found or if update violates constraints
    """
    try:
        result = await db.execute(Recipe.__table__.select().where(Recipe.recipe_id == recipe_id))
        db_recipe = result.scalar_one_or_none()
        if db_recipe is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recipe not found",
            )

        update_data = recipe.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_recipe, key, value)

        await db.commit()
        await db.refresh(db_recipe)
        return db_recipe
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Recipe with this title already exists",
        )


@router.delete(
    "/{recipe_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {
            "description": "Recipe deleted successfully",
        },
        status.HTTP_409_CONFLICT: {
            "description": "Cannot delete recipe that is referenced by meal plans",
            "content": {
                "application/json": {"example": {"detail": "Cannot delete recipe that is referenced by meal plans"}},
            },
        },
    },
)
async def delete_recipe(recipe_id: int, db: AsyncSession = Depends(get_async_db)) -> None:
    """Delete a specific recipe.

    Args:
        recipe_id: ID of the recipe to delete
        db: Database session

    Raises:
        HTTPException: If recipe not found or if deletion violates constraints
    """
    try:
        result = await db.execute(Recipe.__table__.select().where(Recipe.recipe_id == recipe_id))
        db_recipe = result.scalar_one_or_none()
        if db_recipe is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recipe not found",
            )

        await db.delete(db_recipe)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cannot delete recipe that is referenced by meal plans",
        )
