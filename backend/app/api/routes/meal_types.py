"""Meal types router.

This module provides endpoints for managing meal types (breakfast, lunch, dinner, etc.).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from app.core.constants import DUPLICATE_MEAL_TYPE, MEAL_TYPE_IN_USE, MEAL_TYPE_NOT_FOUND
from app.database.session import get_async_db
from app.models.models import MealType
from app.schemas.models import MealType as MealTypeSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.schemas.models import MealTypeCreate

router = APIRouter(
    prefix="/meal-types",
    tags=["meal-types"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Meal type not found",
            "content": {"application/json": {"example": {"detail": MEAL_TYPE_NOT_FOUND}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": "Meal type already exists",
            "content": {"application/json": {"example": {"detail": DUPLICATE_MEAL_TYPE}}},
        },
    },
)


@router.post(
    "/",
    response_model=MealTypeSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "Meal type created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "meal_type_id": 1,
                        "name": "Breakfast",
                    },
                },
            },
        },
    },
)
async def create_meal_type(
    meal_type: MealTypeCreate,
    db: AsyncSession = Depends(get_async_db),
) -> MealType:
    """Create a new meal type.

    Args:
        meal_type: Meal type data
        db: Database session

    Returns:
        MealType: Created meal type

    Raises:
        HTTPException: If meal type already exists
    """
    try:
        db_meal_type = MealType(**meal_type.model_dump())
        db.add(db_meal_type)
        await db.commit()
        await db.refresh(db_meal_type)
        return db_meal_type
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_MEAL_TYPE,
        )


@router.get(
    "/",
    response_model=list[MealTypeSchema],
    responses={
        status.HTTP_200_OK: {
            "description": "List of meal types retrieved successfully",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "meal_type_id": 1,
                            "name": "Breakfast",
                        },
                    ],
                },
            },
        },
    },
)
async def get_meal_types(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_db),
) -> list[MealType]:
    """Get a list of meal types.

    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
        db: Database session

    Returns:
        List[MealType]: List of meal types
    """
    result = await db.execute(select(MealType).offset(skip).limit(limit))
    return list(result.scalars().all())


@router.get(
    "/{type_id}",
    response_model=MealTypeSchema,
    responses={
        status.HTTP_200_OK: {
            "description": "Meal type retrieved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "meal_type_id": 1,
                        "name": "Breakfast",
                    },
                },
            },
        },
    },
)
async def get_meal_type(type_id: int, db: AsyncSession = Depends(get_async_db)) -> MealType:
    """Get a specific meal type by ID.

    Args:
        type_id: ID of the meal type
        db: Database session

    Returns:
        MealType: Meal type

    Raises:
        HTTPException: If meal type not found
    """
    result = await db.execute(select(MealType).filter(MealType.meal_type_id == type_id))
    db_meal_type = result.scalar_one_or_none()
    if db_meal_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=MEAL_TYPE_NOT_FOUND,
        )
    return db_meal_type


@router.put(
    "/{type_id}",
    response_model=MealTypeSchema,
    responses={
        status.HTTP_200_OK: {
            "description": "Meal type updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "meal_type_id": 1,
                        "name": "Breakfast",
                    },
                },
            },
        },
    },
)
async def update_meal_type(
    type_id: int,
    meal_type: MealTypeCreate,
    db: AsyncSession = Depends(get_async_db),
) -> MealType:
    """Update a specific meal type.

    Args:
        type_id: ID of the meal type to update
        meal_type: Updated meal type data
        db: Database session

    Returns:
        MealType: Updated meal type

    Raises:
        HTTPException: If meal type not found or if update violates constraints
    """
    try:
        result = await db.execute(select(MealType).filter(MealType.meal_type_id == type_id))
        db_meal_type = result.scalar_one_or_none()
        if db_meal_type is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=MEAL_TYPE_NOT_FOUND,
            )

        update_data = meal_type.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_meal_type, key, value)

        await db.commit()
        await db.refresh(db_meal_type)
        return db_meal_type
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_MEAL_TYPE,
        )


@router.delete(
    "/{type_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {
            "description": "Meal type deleted successfully",
        },
        status.HTTP_409_CONFLICT: {
            "description": "Cannot delete meal type that is referenced by recipes",
            "content": {"application/json": {"example": {"detail": MEAL_TYPE_IN_USE}}},
        },
    },
)
async def delete_meal_type(type_id: int, db: AsyncSession = Depends(get_async_db)) -> None:
    """Delete a specific meal type.

    Args:
        type_id: ID of the meal type to delete
        db: Database session

    Raises:
        HTTPException: If meal type not found or if deletion violates constraints
    """
    result = await db.execute(select(MealType).filter(MealType.meal_type_id == type_id))
    db_meal_type = result.scalar_one_or_none()
    if db_meal_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=MEAL_TYPE_NOT_FOUND,
        )

    try:
        await db.delete(db_meal_type)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=MEAL_TYPE_IN_USE,
        )
