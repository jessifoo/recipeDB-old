"""Meal plans router.

This module provides endpoints for managing meal plans.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from app.database.session import get_async_db
from app.models.models import MealPlan
from app.schemas.models import MealPlan as MealPlanSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.schemas.models import MealPlanCreate

router = APIRouter(
    prefix="/meal-plans",
    tags=["meal-plans"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Meal plan not found",
            "content": {"application/json": {"example": {"detail": "Meal plan not found"}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": "Meal plan conflicts with existing plan",
            "content": {
                "application/json": {"example": {"detail": "A meal plan already exists for this date and meal type"}},
            },
        },
    },
)


@router.post(
    "/",
    response_model=MealPlanSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "Meal plan created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "plan_id": 1,
                        "recipe_id": 1,
                        "planned_date": "2024-03-20",
                        "meal_type_id": 1,
                        "notes": "Family dinner",
                        "member_id": 1,
                    },
                },
            },
        },
    },
)
async def create_meal_plan(
    meal_plan: MealPlanCreate,
    db: AsyncSession = Depends(get_async_db),
) -> MealPlan:
    """Create a new meal plan.

    Args:
        meal_plan: Meal plan data
        db: Database session

    Returns:
        MealPlan: Created meal plan

    Raises:
        HTTPException: If meal plan conflicts with existing plan or if referenced entities don't exist
    """
    try:
        db_meal_plan = MealPlan(**meal_plan.model_dump())
        db.add(db_meal_plan)
        await db.commit()
        await db.refresh(db_meal_plan)
        return db_meal_plan
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A meal plan already exists for this date and meal type",
        )


@router.get(
    "/",
    response_model=list[MealPlanSchema],
    responses={status.HTTP_200_OK: {"description": "List of meal plans retrieved successfully"}},
)
async def get_meal_plans(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_db),
) -> list[MealPlan]:
    """Get a list of meal plans with pagination."""
    result = await db.execute(select(MealPlan).offset(skip).limit(limit))
    return list(result.scalars().all())


@router.get(
    "/{plan_id}",
    response_model=MealPlanSchema,
    responses={
        status.HTTP_200_OK: {
            "description": "Meal plan retrieved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "plan_id": 1,
                        "recipe_id": 1,
                        "planned_date": "2024-03-20",
                        "meal_type_id": 1,
                        "notes": "Family dinner",
                        "member_id": 1,
                    },
                },
            },
        },
    },
)
async def get_meal_plan(plan_id: int, db: AsyncSession = Depends(get_async_db)) -> MealPlan:
    """Get a specific meal plan by ID.

    Args:
        plan_id: ID of the meal plan
        db: Database session

    Returns:
        MealPlan: Meal plan

    Raises:
        HTTPException: If meal plan not found
    """
    result = await db.execute(MealPlan.__table__.select().where(MealPlan.plan_id == plan_id))
    db_meal_plan = result.scalar_one_or_none()
    if db_meal_plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meal plan not found",
        )
    return db_meal_plan


@router.put(
    "/{plan_id}",
    response_model=MealPlanSchema,
    responses={
        status.HTTP_200_OK: {
            "description": "Meal plan updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "plan_id": 1,
                        "recipe_id": 1,
                        "planned_date": "2024-03-20",
                        "meal_type_id": 1,
                        "notes": "Family dinner",
                        "member_id": 1,
                    },
                },
            },
        },
    },
)
async def update_meal_plan(
    plan_id: int,
    meal_plan: MealPlanCreate,
    db: AsyncSession = Depends(get_async_db),
) -> MealPlan:
    """Update a specific meal plan.

    Args:
        plan_id: ID of the meal plan to update
        meal_plan: Updated meal plan data
        db: Database session

    Returns:
        MealPlan: Updated meal plan

    Raises:
        HTTPException: If meal plan not found or if update violates constraints
    """
    try:
        result = await db.execute(MealPlan.__table__.select().where(MealPlan.plan_id == plan_id))
        db_meal_plan = result.scalar_one_or_none()
        if db_meal_plan is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Meal plan not found",
            )

        update_data = meal_plan.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_meal_plan, key, value)

        await db.commit()
        await db.refresh(db_meal_plan)
        return db_meal_plan
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A meal plan already exists for this date and meal type",
        )


@router.delete(
    "/{plan_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {
            "description": "Meal plan deleted successfully",
        },
    },
)
async def delete_meal_plan(plan_id: int, db: AsyncSession = Depends(get_async_db)) -> None:
    """Delete a specific meal plan.

    Args:
        plan_id: ID of the meal plan to delete
        db: Database session

    Raises:
        HTTPException: If meal plan not found
    """
    result = await db.execute(MealPlan.__table__.select().where(MealPlan.plan_id == plan_id))
    db_meal_plan = result.scalar_one_or_none()
    if db_meal_plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meal plan not found",
        )

    await db.delete(db_meal_plan)
    await db.commit()
