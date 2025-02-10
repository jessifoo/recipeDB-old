"""Protein types router.

This module provides endpoints for managing protein types in the recipe database.
It supports CRUD operations for protein types with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.protein_types import router as protein_types_router
        app.include_router(protein_types_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import ProteinType
from app.schemas.models import ProteinType as ProteinTypeSchema, ProteinTypeCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/protein-types",
    tags=["protein-types"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Protein type not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "PROTEIN_TYPE_NOT_FOUND",
                        "message": "Protein type not found",
                        "details": {"protein_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Protein type already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "PROTEIN_TYPE_EXISTS",
                        "message": "Protein type with this name already exists",
                        "details": {"name": "Chicken"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=ProteinTypeSchema, status_code=status.HTTP_201_CREATED)
async def create_protein_type(
    protein_type: ProteinTypeCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> ProteinType:
    """Create a new protein type.

    This endpoint creates a new protein type in the database. It validates
    the input data and ensures uniqueness of the protein type name.

    Args:
        protein_type (:class:`~app.schemas.models.ProteinTypeCreate`):
            The protein type data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.ProteinType`: The created protein type.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a protein type with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            protein = await create_protein_type(
                ProteinTypeCreate(name="Chicken", description="Poultry protein"),
                db_session
            )
    """
    try:
        db_protein_type = ProteinType(**protein_type.model_dump())
        db.add(db_protein_type)
        await db.commit()
        await db.refresh(db_protein_type)
        return db_protein_type
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="ProteinType", identifier=protein_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_protein_type", details={"protein_type_data": protein_type.model_dump()}
        ) from err


@router.get("/", response_model=list[ProteinTypeSchema])
async def get_protein_types(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[ProteinType]:
    """Retrieve a list of protein types.

    This endpoint returns a paginated list of protein types.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.ProteinType`]:
            List of protein types.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            proteins = await get_protein_types(skip=0, limit=10, db_session)
            for protein in proteins:
                print(protein.name)
    """
    try:
        stmt: Select[tuple[ProteinType]] = select(ProteinType).order_by(ProteinType.name).offset(skip).limit(limit)
        result: Result[tuple[ProteinType]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_protein_types", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{protein_id}", response_model=ProteinTypeSchema)
async def get_protein_type(
    protein_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> ProteinType:
    """Retrieve a specific protein type by ID.

    This endpoint returns a single protein type identified by its ID.

    Args:
        protein_id (int):
            The unique identifier of the protein type.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.ProteinType`:
            The requested protein type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the protein type is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            protein = await get_protein_type(1, db_session)
            print(f"Found protein: {protein.name}")
    """
    try:
        stmt: Select[tuple[ProteinType]] = select(ProteinType).filter(ProteinType.protein_id == protein_id)
        result: Result[tuple[ProteinType]] = await db.execute(stmt)
        db_protein_type = result.scalar_one_or_none()

        if db_protein_type is None:
            raise ResourceNotFoundError(resource_type="ProteinType", identifier=protein_id, lang=lang)

        return db_protein_type
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_protein_type", details={"protein_id": protein_id}
        ) from err


@router.put("/{protein_id}", response_model=ProteinTypeSchema)
async def update_protein_type(
    protein_id: int,
    protein_type: ProteinTypeCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> ProteinType:
    """Update a specific protein type.

    This endpoint updates an existing protein type with new data.
    It validates the input and ensures uniqueness of the protein type name.

    Args:
        protein_id (int):
            The unique identifier of the protein type to update.
        protein_type (:class:`~app.schemas.models.ProteinTypeCreate`):
            The updated protein type data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.ProteinType`:
            The updated protein type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the protein type is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_protein_type(
                1,
                ProteinTypeCreate(name="Free-range Chicken", description="Updated description"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = protein_type.model_dump(exclude_unset=True)
        stmt = (
            update(ProteinType).where(ProteinType.protein_id == protein_id).values(**update_data).returning(ProteinType)
        )
        result = await db.execute(stmt)
        db_protein_type = result.scalar_one_or_none()

        if db_protein_type is None:
            raise ResourceNotFoundError(resource_type="ProteinType", identifier=protein_id, lang=lang)

        await db.commit()
        return db_protein_type

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="ProteinType", identifier=protein_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_protein_type",
            details={"protein_id": protein_id, "update_data": protein_type.model_dump()},
        ) from err


@router.delete("/{protein_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_protein_type(
    protein_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific protein type.

    This endpoint removes a protein type from the database.
    It fails if the protein type is referenced by any recipes.

    Args:
        protein_id (int):
            The unique identifier of the protein type to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the protein type is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the protein type is referenced by recipes.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_protein_type(1, db_session)
            # The protein type is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(ProteinType).where(ProteinType.protein_id == protein_id).returning(ProteinType.protein_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="ProteinType", identifier=protein_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="ProteinType", identifier=protein_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_protein_type", details={"protein_id": protein_id}
        ) from err
