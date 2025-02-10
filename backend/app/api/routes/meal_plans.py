"""Meal plans router.

This module provides endpoints for managing meal plans in the recipe database.
It supports CRUD operations for meal plans with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.meal_plans import router as meal_plans_router
        app.include_router(meal_plans_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import MealPlan
from app.schemas.models import MealPlan as MealPlanSchema, MealPlanCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/meal-plans",
    tags=["meal-plans"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Meal plan not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "MEAL_PLAN_NOT_FOUND",
                        "message": "Meal plan not found",
                        "details": {"plan_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Meal plan conflicts with existing plan",
            "content": {
                "application/json": {
                    "example": {
                        "code": "MEAL_PLAN_EXISTS",
                        "message": "A meal plan already exists for this date and meal type",
                        "details": {"date": "2024-03-20", "meal_type": "Dinner"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=MealPlanSchema, status_code=status.HTTP_201_CREATED)
async def create_meal_plan(
    meal_plan: MealPlanCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealPlan:
    """Create a new meal plan.

    This endpoint creates a new meal plan in the database. It validates
    the input data and ensures no conflicts with existing plans.

    Args:
        meal_plan (:class:`~app.schemas.models.MealPlanCreate`):
            The meal plan data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealPlan`: The created meal plan.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a meal plan already exists for the same date and meal type.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            plan = await create_meal_plan(
                MealPlanCreate(
                    recipe_id=1,
                    planned_date="2024-03-20",
                    meal_type_id=1,
                    member_id=1,
                    notes="Family dinner"
                ),
                db_session
            )
    """
    try:
        db_meal_plan = MealPlan(**meal_plan.model_dump())
        db.add(db_meal_plan)
        await db.commit()
        await db.refresh(db_meal_plan)
        return db_meal_plan
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(
            resource_type="MealPlan", identifier=f"{meal_plan.planned_date}-{meal_plan.meal_type_id}", lang=lang
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_meal_plan", details={"meal_plan_data": meal_plan.model_dump()}
        ) from err


@router.get("/", response_model=list[MealPlanSchema])
async def get_meal_plans(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[MealPlan]:
    """Get a list of meal plans with pagination.

    This endpoint returns a paginated list of meal plans, ordered by date.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.MealPlan`]:
            List of meal plans.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            plans = await get_meal_plans(skip=0, limit=10, db_session)
            for plan in plans:
                print(f"{plan.planned_date}: {plan.recipe_id}")
    """
    try:
        stmt: Select[tuple[MealPlan]] = (
            select(MealPlan).order_by(MealPlan.planned_date.desc()).offset(skip).limit(limit)
        )
        result: Result[tuple[MealPlan]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_meal_plans", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{plan_id}", response_model=MealPlanSchema)
async def get_meal_plan(
    plan_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealPlan:
    """Get a specific meal plan by ID.

    This endpoint returns a single meal plan identified by its ID.

    Args:
        plan_id (int):
            The unique identifier of the meal plan.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealPlan`:
            The requested meal plan.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal plan is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            plan = await get_meal_plan(1, db_session)
            print(f"Found plan for {plan.planned_date}")
    """
    try:
        stmt: Select[tuple[MealPlan]] = select(MealPlan).filter(MealPlan.plan_id == plan_id)
        result: Result[tuple[MealPlan]] = await db.execute(stmt)
        db_meal_plan = result.scalar_one_or_none()

        if db_meal_plan is None:
            raise ResourceNotFoundError(resource_type="MealPlan", identifier=plan_id, lang=lang)

        return db_meal_plan
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="get_meal_plan", details={"plan_id": plan_id}) from err


@router.put("/{plan_id}", response_model=MealPlanSchema)
async def update_meal_plan(
    plan_id: int, meal_plan: MealPlanCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealPlan:
    """Update a specific meal plan.

    This endpoint updates an existing meal plan with new data.
    It validates the input and ensures no conflicts with other plans.

    Args:
        plan_id (int):
            The unique identifier of the meal plan to update.
        meal_plan (:class:`~app.schemas.models.MealPlanCreate`):
            The updated meal plan data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealPlan`:
            The updated meal plan.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal plan is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a conflict with another plan.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_meal_plan(
                1,
                MealPlanCreate(
                    recipe_id=2,
                    planned_date="2024-03-21",
                    meal_type_id=1,
                    member_id=1,
                    notes="Updated dinner plan"
                ),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = meal_plan.model_dump(exclude_unset=True)
        stmt = update(MealPlan).where(MealPlan.plan_id == plan_id).values(**update_data).returning(MealPlan)
        result = await db.execute(stmt)
        db_meal_plan = result.scalar_one_or_none()

        if db_meal_plan is None:
            raise ResourceNotFoundError(resource_type="MealPlan", identifier=plan_id, lang=lang)

        await db.commit()
        return db_meal_plan

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(
            resource_type="MealPlan", identifier=f"{meal_plan.planned_date}-{meal_plan.meal_type_id}", lang=lang
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="update_meal_plan", details={"plan_id": plan_id, "update_data": meal_plan.model_dump()}
        ) from err


@router.delete("/{plan_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_meal_plan(
    plan_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific meal plan.

    This endpoint removes a meal plan from the database.

    Args:
        plan_id (int):
            The unique identifier of the meal plan to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal plan is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_meal_plan(1, db_session)
            # The meal plan is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(MealPlan).where(MealPlan.plan_id == plan_id).returning(MealPlan.plan_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="MealPlan", identifier=plan_id, lang=lang)

        await db.commit()

    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_meal_plan", details={"plan_id": plan_id}
        ) from err
