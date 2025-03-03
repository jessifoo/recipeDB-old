"""Allergens router.

This module provides endpoints for managing allergen records in the database.
It supports CRUD operations with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import FastAPI
        from app.api.routes.allergens import router as allergens_router
        app.include_router(allergens_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages, Language
from app.core.exceptions import BusinessError, DatabaseError, ResourceNotFoundError
from app.models.models import Allergen
from app.schemas.models import Allergen as AllergenSchema

if TYPE_CHECKING:
    from app.api.deps import DatabaseSession
    from app.schemas.models import AllergenCreate

router = APIRouter(
    prefix="/allergens",
    tags=["allergens"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Allergen not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.RESOURCE_NOT_FOUND.get_message(
                            lang=Language.EN, details={"resource_type": "Allergen", "identifier": "123"}
                        )
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Allergen operation failed due to constraint violation",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.BUSINESS_RULE_VIOLATION.get_message(
                            lang=Language.EN, details={"error": "Allergen with this name already exists"}
                        )
                    }
                }
            },
        },
    },
)


@router.post(
    "/",
    response_model=AllergenSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Allergen created successfully"},
        status.HTTP_409_CONFLICT: {"description": "Allergen with this name already exists"},
    },
)
async def create_allergen(allergen: AllergenCreate, db: DatabaseSession) -> Allergen:
    """Create a new allergen.

    This endpoint creates a new allergen record in the database.
    It ensures that no duplicate allergens exist with the same name.

    Args:
        allergen: Allergen data including name and description
        db: Injected database session for the operation

    Returns:
        Allergen: The newly created allergen with all fields populated

    Raises:
        BusinessError: If an allergen with the same name already exists
        DatabaseError: If the database operation fails
    """
    try:
        db_allergen = Allergen(**allergen.model_dump())
        db.add(db_allergen)
        await db.commit()
        await db.refresh(db_allergen)
        return db_allergen
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.ALLERGEN_EXISTS,
            details={"error": "Allergen with this name already exists"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="create_allergen") from err


@router.get(
    "/",
    response_model=list[AllergenSchema],
    responses={
        status.HTTP_200_OK: {"description": "List of allergens retrieved successfully"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Database operation failed",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.DATABASE_ERROR.get_message(
                            lang=Language.EN, details={"operation": "list_allergens"}
                        )
                    }
                }
            },
        },
    },
)
async def get_allergens(db: DatabaseSession, skip: int = 0, limit: int = 100) -> list[Allergen]:
    """Get a list of allergens with pagination.

    This endpoint retrieves a paginated list of allergens from the database.

    Args:
        db: Injected database session for the operation
        skip: Number of allergens to skip (for pagination)
        limit: Maximum number of allergens to return

    Returns:
        list[Allergen]: List of allergens within the specified range

    Raises:
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Allergen).offset(skip).limit(limit))
        return list(result.scalars().all())
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="list_allergens") from err


@router.get(
    "/{allergen_id}",
    response_model=AllergenSchema,
    responses={
        status.HTTP_200_OK: {"description": "Allergen retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Allergen not found"},
    },
)
async def get_allergen(allergen_id: int, db: DatabaseSession) -> Allergen:
    """Get a specific allergen by ID.

    This endpoint retrieves detailed information about a specific allergen.

    Args:
        allergen_id: ID of the allergen to retrieve
        db: Injected database session for the operation

    Returns:
        Allergen: The requested allergen's details

    Raises:
        ResourceNotFoundError: If the allergen does not exist
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Allergen).where(Allergen.allergen_id == allergen_id))
        db_allergen = result.scalar_one_or_none()
        if db_allergen is None:
            raise ResourceNotFoundError(resource_type="Allergen", identifier=str(allergen_id))
        return db_allergen
    except ResourceNotFoundError:
        raise
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="get_allergen") from err


@router.put(
    "/{allergen_id}",
    response_model=AllergenSchema,
    responses={
        status.HTTP_200_OK: {"description": "Allergen updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Allergen not found"},
        status.HTTP_409_CONFLICT: {"description": "Update violates unique constraints"},
    },
)
async def update_allergen(allergen_id: int, allergen: AllergenCreate, db: DatabaseSession) -> Allergen:
    """Update a specific allergen.

    This endpoint updates an existing allergen with new data while maintaining
    data integrity constraints.

    Args:
        allergen_id: ID of the allergen to update
        allergen: Updated allergen data
        db: Injected database session for the operation

    Returns:
        Allergen: The updated allergen with all changes applied

    Raises:
        ResourceNotFoundError: If the allergen does not exist
        BusinessError: If the update violates unique constraints
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Allergen).where(Allergen.allergen_id == allergen_id))
        db_allergen = result.scalar_one_or_none()
        if db_allergen is None:
            raise ResourceNotFoundError(resource_type="Allergen", identifier=str(allergen_id))

        update_data = allergen.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_allergen, key, value)

        await db.commit()
        await db.refresh(db_allergen)
        return db_allergen
    except ResourceNotFoundError:
        raise
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.ALLERGEN_EXISTS,
            details={"error": "Allergen with this name already exists"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="update_allergen") from err


@router.delete(
    "/{allergen_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Allergen deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Allergen not found"},
        status.HTTP_409_CONFLICT: {"description": "Cannot delete allergen that is referenced by recipes"},
    },
)
async def delete_allergen(allergen_id: int, db: DatabaseSession) -> None:
    """Delete a specific allergen.

    This endpoint removes an allergen from the database if it is not referenced by any recipes.

    Args:
        allergen_id: ID of the allergen to delete
        db: Injected database session for the operation

    Raises:
        ResourceNotFoundError: If the allergen does not exist
        BusinessError: If the allergen is referenced by recipes
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Allergen).where(Allergen.allergen_id == allergen_id))
        db_allergen = result.scalar_one_or_none()
        if db_allergen is None:
            raise ResourceNotFoundError(resource_type="Allergen", identifier=str(allergen_id))

        await db.delete(db_allergen)
        await db.commit()
    except ResourceNotFoundError:
        raise
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.ALLERGEN_IN_USE,
            details={"error": "Cannot delete allergen that is referenced by recipes"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="delete_allergen") from err
