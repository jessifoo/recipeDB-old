"""Cuisine types router.

This module provides endpoints for managing cuisine types in the recipe database.
It supports CRUD operations for cuisine types with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.cuisine_types import router as cuisine_types_router
        app.include_router(cuisine_types_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import CuisineType
from app.schemas.models import CuisineType as CuisineTypeSchema, CuisineTypeCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/cuisine-types",
    tags=["cuisine-types"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Cuisine type not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "CUISINE_TYPE_NOT_FOUND",
                        "message": "Cuisine type not found",
                        "details": {"cuisine_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Cuisine type already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "CUISINE_TYPE_EXISTS",
                        "message": "Cuisine type with this name already exists",
                        "details": {"name": "Italian"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=CuisineTypeSchema, status_code=status.HTTP_201_CREATED)
async def create_cuisine_type(
    cuisine_type: CuisineTypeCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> CuisineType:
    """Create a new cuisine type.

    This endpoint creates a new cuisine type in the database. It validates
    the input data and ensures uniqueness of the cuisine type name.

    Args:
        cuisine_type (:class:`~app.schemas.models.CuisineTypeCreate`):
            The cuisine type data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CuisineType`: The created cuisine type.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a cuisine type with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python
    # amazonq-ignore-next-line

            cuisine = await create_cuisine_type(
                CuisineTypeCreate(name="Italian", description="Italian cuisine"),
                db_session
            )
    """
    try:
        db_cuisine_type = CuisineType(**cuisine_type.model_dump())
        db.add(db_cuisine_type)
        await db.commit()
        await db.refresh(db_cuisine_type)
        return db_cuisine_type
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="CuisineType", identifier=cuisine_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_cuisine_type", details={"cuisine_type_data": cuisine_type.model_dump()}
        ) from err


@router.get("/", response_model=list[CuisineTypeSchema])
async def get_cuisine_types(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[CuisineType]:
    """Retrieve a list of cuisine types.

    This endpoint returns a paginated list of cuisine types.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.CuisineType`]:
            List of cuisine types.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            cuisines = await get_cuisine_types(skip=0, limit=10, db_session)
            for cuisine in cuisines:
                print(cuisine.name)
    """
    try:
        stmt: Select[tuple[CuisineType]] = select(CuisineType).offset(skip).limit(limit)
        result: Result[tuple[CuisineType]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_cuisine_types", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{cuisine_id}", response_model=CuisineTypeSchema)
async def get_cuisine_type(
    cuisine_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> CuisineType:
    """Retrieve a specific cuisine type by ID.

    This endpoint returns a single cuisine type identified by its ID.

    Args:
        cuisine_id (int):
            The unique identifier of the cuisine type.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CuisineType`:
            The requested cuisine type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cuisine type is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            cuisine = await get_cuisine_type(1, db_session)
            print(f"Found cuisine: {cuisine.name}")
    """
    try:
        stmt: Select[tuple[CuisineType]] = select(CuisineType).filter(CuisineType.cuisine_id == cuisine_id)
        result: Result[tuple[CuisineType]] = await db.execute(stmt)
        db_cuisine_type = result.scalar_one_or_none()

        if db_cuisine_type is None:
            raise ResourceNotFoundError(resource_type="CuisineType", identifier=cuisine_id, lang=lang)

        return db_cuisine_type
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_cuisine_type", details={"cuisine_id": cuisine_id}
        ) from err


@router.put("/{cuisine_id}", response_model=CuisineTypeSchema)
async def update_cuisine_type(
    cuisine_id: int,
    cuisine_type: CuisineTypeCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> CuisineType:
    """Update a specific cuisine type.

    This endpoint updates an existing cuisine type with new data.
    It validates the input and ensures uniqueness of the cuisine type name.

    Args:
        cuisine_id (int):
            The unique identifier of the cuisine type to update.
        cuisine_type (:class:`~app.schemas.models.CuisineTypeCreate`):
            The updated cuisine type data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CuisineType`:
            The updated cuisine type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cuisine type is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_cuisine_type(
                1,
                CuisineTypeCreate(name="Northern Italian", description="Updated description"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = cuisine_type.model_dump(exclude_unset=True)
        stmt = (
            update(CuisineType).where(CuisineType.cuisine_id == cuisine_id).values(**update_data).returning(CuisineType)
        )
        result = await db.execute(stmt)
        db_cuisine_type = result.scalar_one_or_none()

        if db_cuisine_type is None:
            raise ResourceNotFoundError(resource_type="CuisineType", identifier=cuisine_id, lang=lang)

        await db.commit()
        return db_cuisine_type

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="CuisineType", identifier=cuisine_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_cuisine_type",
            details={"cuisine_id": cuisine_id, "update_data": cuisine_type.model_dump()},
        ) from err


@router.delete("/{cuisine_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cuisine_type(
    cuisine_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific cuisine type.

    This endpoint removes a cuisine type from the database.
    It fails if the cuisine type is referenced by any recipes.

    Args:
        cuisine_id (int):
            The unique identifier of the cuisine type to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cuisine type is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the cuisine type is referenced by recipes.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_cuisine_type(1, db_session)
            # The cuisine type is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(CuisineType).where(CuisineType.cuisine_id == cuisine_id).returning(CuisineType.cuisine_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="CuisineType", identifier=cuisine_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="CuisineType", identifier=cuisine_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_cuisine_type", details={"cuisine_id": cuisine_id}
        ) from err
