"""Cook methods router.

This module provides endpoints for managing cooking methods in the recipe database.
It supports CRUD operations for cooking methods with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.cook_methods import router as cook_methods_router
        app.include_router(cook_methods_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import CookMethod
from app.schemas.models import CookMethod as CookMethodSchema, CookMethodCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/cook-methods",
    tags=["cook-methods"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Cook method not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "COOK_METHOD_NOT_FOUND",
                        "message": "Cook method not found",
                        "details": {"method_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Cook method already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "COOK_METHOD_EXISTS",
                        "message": "Cook method with this name already exists",
                        "details": {"name": "Baking"},
                    }
                }
            },
        },
    },
)
# amazonq-ignore-next-line


@router.post("/", response_model=CookMethodSchema, status_code=status.HTTP_201_CREATED)
async def create_cook_method(
    cook_method: CookMethodCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> CookMethod:
    """Create a new cooking method.

    This endpoint creates a new cooking method in the database. It validates
    the input data and ensures uniqueness of the method name.

    Args:
        cook_method (:class:`~app.schemas.models.CookMethodCreate`):
            The cooking method data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CookMethod`: The created cooking method.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a cooking method with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            method = await create_cook_method(
                CookMethodCreate(name="Baking", description="Cooking in an oven"),
                db_session
            )
    """
    try:
        db_cook_method = CookMethod(**cook_method.model_dump())
        db.add(db_cook_method)
        await db.commit()
        await db.refresh(db_cook_method)
        return db_cook_method
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="CookMethod", identifier=cook_method.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_cook_method", details={"cook_method_data": cook_method.model_dump()}
        ) from err


@router.get("/", response_model=list[CookMethodSchema])
async def get_cook_methods(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[CookMethod]:
    """Retrieve a list of cooking methods.

    This endpoint returns a paginated list of cooking methods.
    It supports pagination through skip and limit parameters.
    # amazonq-ignore-next-line

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.CookMethod`]:
            List of cooking methods.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            # amazonq-ignore-next-line
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            methods = await get_cook_methods(skip=0, limit=10, db_session)
            for method in methods:
                print(method.name)
    """
    try:
        stmt: Select[tuple[CookMethod]] = select(CookMethod).offset(skip).limit(limit)
        result: Result[tuple[CookMethod]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_cook_methods", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{method_id}", response_model=CookMethodSchema)
async def get_cook_method(
    method_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> CookMethod:
    """Retrieve a specific cooking method by ID.

    This endpoint returns a single cooking method identified by its ID.

    Args:
        method_id (int):
            The unique identifier of the cooking method.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CookMethod`:
            The requested cooking method.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cooking method is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            method = await get_cook_method(1, db_session)
            print(f"Found method: {method.name}")
    """
    try:
        stmt: Select[tuple[CookMethod]] = select(CookMethod).filter(CookMethod.method_id == method_id)
        result: Result[tuple[CookMethod]] = await db.execute(stmt)
        db_cook_method = result.scalar_one_or_none()

        if db_cook_method is None:
            raise ResourceNotFoundError(resource_type="CookMethod", identifier=method_id, lang=lang)

        return db_cook_method
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_cook_method", details={"method_id": method_id}
        ) from err


@router.put("/{method_id}", response_model=CookMethodSchema)
async def update_cook_method(
    method_id: int,
    cook_method: CookMethodCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> CookMethod:
    """Update a specific cooking method.

    This endpoint updates an existing cooking method with new data.
    It validates the input and ensures uniqueness of the method name.

    Args:
        method_id (int):
            The unique identifier of the cooking method to update.
        cook_method (:class:`~app.schemas.models.CookMethodCreate`):
            The updated cooking method data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CookMethod`:
            The updated cooking method.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cooking method is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_cook_method(
                1,
                CookMethodCreate(name="Deep Frying", description="Updated description"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = cook_method.model_dump(exclude_unset=True)
        stmt = update(CookMethod).where(CookMethod.method_id == method_id).values(**update_data).returning(CookMethod)
        result = await db.execute(stmt)
        db_cook_method = result.scalar_one_or_none()

        if db_cook_method is None:
            raise ResourceNotFoundError(resource_type="CookMethod", identifier=method_id, lang=lang)

        await db.commit()
        return db_cook_method

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="CookMethod", identifier=cook_method.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_cook_method",
            details={"method_id": method_id, "update_data": cook_method.model_dump()},
        ) from err


@router.delete("/{method_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cook_method(
    method_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific cooking method.

    This endpoint removes a cooking method from the database.
    It fails if the method is referenced by any recipes.

    Args:
        method_id (int):
            The unique identifier of the cooking method to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cooking method is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the cooking method is referenced by recipes.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_cook_method(1, db_session)
            # The cooking method is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(CookMethod).where(CookMethod.method_id == method_id).returning(CookMethod.method_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="CookMethod", identifier=method_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="CookMethod", identifier=method_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_cook_method", details={"method_id": method_id}
        ) from err
