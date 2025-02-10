"""Dietary restrictions router.

This module provides endpoints for managing dietary restrictions in the recipe database.
It supports CRUD operations for dietary restrictions with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.dietary_restrictions import router as dietary_restrictions_router
        app.include_router(dietary_restrictions_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import DietaryRestriction
from app.schemas.models import DietaryRestriction as DietaryRestrictionSchema, DietaryRestrictionCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/dietary-restrictions",
    tags=["dietary-restrictions"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Dietary restriction not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "DIETARY_RESTRICTION_NOT_FOUND",
                        "message": "Dietary restriction not found",
                        "details": {"restriction_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Dietary restriction already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "DIETARY_RESTRICTION_EXISTS",
                        "message": "Dietary restriction with this name already exists",
                        "details": {"name": "Vegan"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=DietaryRestrictionSchema, status_code=status.HTTP_201_CREATED)
async def create_dietary_restriction(
    dietary_restriction: DietaryRestrictionCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> DietaryRestriction:
    """Create a new dietary restriction.

    This endpoint creates a new dietary restriction in the database. It validates
    the input data and ensures uniqueness of the restriction name.

    Args:
        dietary_restriction (:class:`~app.schemas.models.DietaryRestrictionCreate`):
            The dietary restriction data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.DietaryRestriction`: The created dietary restriction.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a dietary restriction with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            restriction = await create_dietary_restriction(
                DietaryRestrictionCreate(name="Vegan", description="No animal products"),
                db_session
            )
    """
    try:
        db_dietary_restriction = DietaryRestriction(**dietary_restriction.model_dump())
        db.add(db_dietary_restriction)
        await db.commit()
        await db.refresh(db_dietary_restriction)
        return db_dietary_restriction
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(
            resource_type="DietaryRestriction", identifier=dietary_restriction.name, lang=lang
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="create_dietary_restriction",
            details={"dietary_restriction_data": dietary_restriction.model_dump()},
        ) from err


@router.get("/", response_model=list[DietaryRestrictionSchema])
async def get_dietary_restrictions(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[DietaryRestriction]:
    """Retrieve a list of dietary restrictions.

    This endpoint returns a paginated list of dietary restrictions, ordered by ID.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.DietaryRestriction`]:
            List of dietary restrictions.

    Raises:
        ValueError: If skip or limit is negative.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            restrictions = await get_dietary_restrictions(skip=0, limit=10, db_session)
            for restriction in restrictions:
                print(restriction.name)
    """
    if skip < 0 or limit < 0:
        msg = "Skip and limit must be non-negative integers"
        raise ValueError(msg)
    try:
        stmt: Select[tuple[DietaryRestriction]] = (
            select(DietaryRestriction).order_by(DietaryRestriction.restriction_id).offset(skip).limit(limit)
        )
        result: Result[tuple[DietaryRestriction]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_dietary_restrictions", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{restriction_id}", response_model=DietaryRestrictionSchema)
async def get_dietary_restriction(
    restriction_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> DietaryRestriction:
    """Retrieve a specific dietary restriction by ID.

    This endpoint returns a single dietary restriction identified by its ID.

    Args:
        restriction_id (int):
            The unique identifier of the dietary restriction.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.DietaryRestriction`:
            The requested dietary restriction.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the dietary restriction is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            restriction = await get_dietary_restriction(1, db_session)
            print(f"Found restriction: {restriction.name}")
    """
    try:
        stmt: Select[tuple[DietaryRestriction]] = select(DietaryRestriction).filter(
            DietaryRestriction.restriction_id == restriction_id
        )
        result: Result[tuple[DietaryRestriction]] = await db.execute(stmt)
        db_dietary_restriction = result.scalar_one_or_none()

        if db_dietary_restriction is None:
            raise ResourceNotFoundError(resource_type="DietaryRestriction", identifier=restriction_id, lang=lang)

        return db_dietary_restriction
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_dietary_restriction", details={"restriction_id": restriction_id}
        ) from err


@router.put("/{restriction_id}", response_model=DietaryRestrictionSchema)
async def update_dietary_restriction(
    restriction_id: int,
    dietary_restriction: DietaryRestrictionCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> DietaryRestriction:
    """Update a specific dietary restriction.

    This endpoint updates an existing dietary restriction with new data.
    It validates the input and ensures uniqueness of the restriction name.

    Args:
        restriction_id (int):
            The unique identifier of the dietary restriction to update.
        dietary_restriction (:class:`~app.schemas.models.DietaryRestrictionCreate`):
            The updated dietary restriction data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.DietaryRestriction`:
            The updated dietary restriction.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the dietary restriction is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_dietary_restriction(
                1,
                DietaryRestrictionCreate(name="Strict Vegan", description="Updated description"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = dietary_restriction.model_dump(exclude_unset=True)
        stmt = (
            update(DietaryRestriction)
            .where(DietaryRestriction.restriction_id == restriction_id)
            .values(**update_data)
            .returning(DietaryRestriction)
        )
        result = await db.execute(stmt)
        db_dietary_restriction = result.scalar_one_or_none()

        if db_dietary_restriction is None:
            raise ResourceNotFoundError(resource_type="DietaryRestriction", identifier=restriction_id, lang=lang)

        await db.commit()
        return db_dietary_restriction

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(
            resource_type="DietaryRestriction", identifier=dietary_restriction.name, lang=lang
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_dietary_restriction",
            details={"restriction_id": restriction_id, "update_data": dietary_restriction.model_dump()},
        ) from err


@router.delete("/{restriction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dietary_restriction(
    restriction_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific dietary restriction.

    This endpoint removes a dietary restriction from the database.
    It fails if the restriction is referenced by any family members.

    Args:
        restriction_id (int):
            The unique identifier of the dietary restriction to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the dietary restriction is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the dietary restriction is referenced by family members.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_dietary_restriction(1, db_session)
            # The restriction is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = (
            delete(DietaryRestriction)
            .where(DietaryRestriction.restriction_id == restriction_id)
            .returning(DietaryRestriction.restriction_id)
        )
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="DietaryRestriction", identifier=restriction_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="DietaryRestriction", identifier=restriction_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_dietary_restriction", details={"restriction_id": restriction_id}
        ) from err
