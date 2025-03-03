"""Meal types router.

This module provides endpoints for managing meal types in the recipe database.
It supports CRUD operations for meal types (breakfast, lunch, dinner, etc.) with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.meal_types import router as meal_types_router
        app.include_router(meal_types_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import MealType
from app.schemas.models import MealType as MealTypeSchema, MealTypeCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/meal-types",
    tags=["meal-types"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Meal type not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "MEAL_TYPE_NOT_FOUND",
                        "message": "Meal type not found",
                        "details": {"type_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Meal type already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "MEAL_TYPE_EXISTS",
                        "message": "Meal type with this name already exists",
                        "details": {"name": "Breakfast"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=MealTypeSchema, status_code=status.HTTP_201_CREATED)
async def create_meal_type(
    meal_type: MealTypeCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealType:
    """Create a new meal type.

    This endpoint creates a new meal type in the database. It validates
    the input data and ensures uniqueness of the meal type name.

    Args:
        meal_type (:class:`~app.schemas.models.MealTypeCreate`):
            The meal type data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealType`: The created meal type.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a meal type with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            meal_type = await create_meal_type(
                MealTypeCreate(name="Breakfast"),
                db_session
            )
    """
    try:
        db_meal_type = MealType(**meal_type.model_dump())
        db.add(db_meal_type)
        await db.commit()
        await db.refresh(db_meal_type)
        return db_meal_type
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="MealType", identifier=meal_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_meal_type", details={"meal_type_data": meal_type.model_dump()}
        ) from err


@router.get("/", response_model=list[MealTypeSchema])
async def get_meal_types(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[MealType]:
    """Retrieve a list of meal types.

    This endpoint returns a paginated list of meal types.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.MealType`]:
            List of meal types.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            meal_types = await get_meal_types(skip=0, limit=10, db_session)
            for meal_type in meal_types:
                print(meal_type.name)
    """
    try:
        stmt: Select[tuple[MealType]] = select(MealType).order_by(MealType.name).offset(skip).limit(limit)
        result: Result[tuple[MealType]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_meal_types", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{type_id}", response_model=MealTypeSchema)
async def get_meal_type(
    type_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealType:
    """Retrieve a specific meal type by ID.

    This endpoint returns a single meal type identified by its ID.

    Args:
        type_id (int):
            The unique identifier of the meal type.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealType`:
            The requested meal type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal type is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            meal_type = await get_meal_type(1, db_session)
            print(f"Found meal type: {meal_type.name}")
    """
    try:
        stmt: Select[tuple[MealType]] = select(MealType).filter(MealType.meal_type_id == type_id)
        result: Result[tuple[MealType]] = await db.execute(stmt)
        db_meal_type = result.scalar_one_or_none()

        if db_meal_type is None:
            raise ResourceNotFoundError(resource_type="MealType", identifier=type_id, lang=lang)

        return db_meal_type
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="get_meal_type", details={"type_id": type_id}) from err


@router.put("/{type_id}", response_model=MealTypeSchema)
async def update_meal_type(
    type_id: int, meal_type: MealTypeCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealType:
    """Update a specific meal type.

    This endpoint updates an existing meal type with new data.
    It validates the input and ensures uniqueness of the meal type name.

    Args:
        type_id (int):
            The unique identifier of the meal type to update.
        meal_type (:class:`~app.schemas.models.MealTypeCreate`):
            The updated meal type data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealType`:
            The updated meal type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal type is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_meal_type(
                1,
                MealTypeCreate(name="Early Breakfast"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = meal_type.model_dump(exclude_unset=True)
        stmt = update(MealType).where(MealType.meal_type_id == type_id).values(**update_data).returning(MealType)
        result = await db.execute(stmt)
        db_meal_type = result.scalar_one_or_none()

        if db_meal_type is None:
            raise ResourceNotFoundError(resource_type="MealType", identifier=type_id, lang=lang)

        await db.commit()
        return db_meal_type

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="MealType", identifier=meal_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="update_meal_type", details={"type_id": type_id, "update_data": meal_type.model_dump()}
        ) from err


@router.delete("/{type_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_meal_type(
    type_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific meal type.

    This endpoint removes a meal type from the database.
    It fails if the meal type is referenced by any meal plans.

    Args:
        type_id (int):
            The unique identifier of the meal type to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal type is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the meal type is referenced by meal plans.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_meal_type(1, db_session)
            # The meal type is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(MealType).where(MealType.meal_type_id == type_id).returning(MealType.meal_type_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="MealType", identifier=type_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="MealType", identifier=type_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_meal_type", details={"type_id": type_id}
        ) from err
