"""Ingredients router.

This module provides endpoints for managing ingredients.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from app.core.constants import DUPLICATE_INGREDIENT, INGREDIENT_IN_USE, INGREDIENT_NOT_FOUND
from app.database.session import get_async_db
from app.models.models import Ingredient
from app.schemas.models import Ingredient as IngredientSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.schemas.models import IngredientCreate

router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Ingredient not found",
            "content": {"application/json": {"example": {"detail": INGREDIENT_NOT_FOUND}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": "Ingredient already exists",
            "content": {"application/json": {"example": {"detail": DUPLICATE_INGREDIENT}}},
        },
    },
)


@router.post(
    "/",
    response_model=IngredientSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Ingredient created successfully"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid ingredient data"},
        status.HTTP_409_CONFLICT: {"description": "Ingredient with this name already exists"},
    },
)
async def create_ingredient(
    ingredient: IngredientCreate,
    db: AsyncSession = Depends(get_async_db),
) -> Ingredient:
    """Create a new ingredient."""
    try:
        db_ingredient = Ingredient(**ingredient.model_dump())
        db.add(db_ingredient)
        await db.commit()
        await db.refresh(db_ingredient)
        return db_ingredient
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_INGREDIENT,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[IngredientSchema],
    responses={status.HTTP_200_OK: {"description": "List of ingredients retrieved successfully"}},
)
async def get_ingredients(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_db),
) -> list[Ingredient]:
    """Get a list of ingredients with pagination."""
    result = await db.execute(select(Ingredient).offset(skip).limit(limit))
    return list(result.scalars().all())


@router.get(
    "/{ingredient_id}",
    response_model=IngredientSchema,
    responses={
        status.HTTP_200_OK: {"description": "Ingredient retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Ingredient not found"},
    },
)
async def get_ingredient(ingredient_id: int, db: AsyncSession = Depends(get_async_db)) -> Ingredient:
    """Get a specific ingredient by ID."""
    result = await db.execute(select(Ingredient).filter(Ingredient.ingredient_id == ingredient_id))
    db_ingredient = result.scalar_one_or_none()
    if db_ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=INGREDIENT_NOT_FOUND,
        )
    return db_ingredient


@router.put(
    "/{ingredient_id}",
    response_model=IngredientSchema,
    responses={
        status.HTTP_200_OK: {"description": "Ingredient updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Ingredient not found"},
        status.HTTP_409_CONFLICT: {"description": "Ingredient with this name already exists"},
    },
)
async def update_ingredient(
    ingredient_id: int,
    ingredient: IngredientCreate,
    db: AsyncSession = Depends(get_async_db),
) -> Ingredient:
    """Update a specific ingredient."""
    try:
        result = await db.execute(select(Ingredient).filter(Ingredient.ingredient_id == ingredient_id))
        db_ingredient = result.scalar_one_or_none()
        if db_ingredient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=INGREDIENT_NOT_FOUND,
            )

        update_data = ingredient.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_ingredient, key, value)

        await db.commit()
        await db.refresh(db_ingredient)
        return db_ingredient
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_INGREDIENT,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete(
    "/{ingredient_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Ingredient deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Ingredient not found"},
        status.HTTP_409_CONFLICT: {
            "description": "Cannot delete ingredient that is referenced by recipes",
            "content": {"application/json": {"example": {"detail": INGREDIENT_IN_USE}}},
        },
    },
)
async def delete_ingredient(ingredient_id: int, db: AsyncSession = Depends(get_async_db)) -> None:
    """Delete a specific ingredient."""
    result = await db.execute(select(Ingredient).filter(Ingredient.ingredient_id == ingredient_id))
    db_ingredient = result.scalar_one_or_none()
    if db_ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=INGREDIENT_NOT_FOUND,
        )

    try:
        await db.delete(db_ingredient)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=INGREDIENT_IN_USE,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
