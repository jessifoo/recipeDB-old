"""Cuisine types router.

This module provides endpoints for managing cuisine types.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from app.core.constants import CUISINE_TYPE_IN_USE, CUISINE_TYPE_NOT_FOUND, DUPLICATE_CUISINE_TYPE
from app.database.session import get_async_db
from app.models.models import CuisineType
from app.schemas.models import CuisineType as CuisineTypeSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.schemas.models import CuisineTypeCreate

router = APIRouter(
    prefix="/cuisine-types",
    tags=["cuisine-types"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Cuisine type not found",
            "content": {"application/json": {"example": {"detail": CUISINE_TYPE_NOT_FOUND}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": "Cuisine type already exists",
            "content": {"application/json": {"example": {"detail": DUPLICATE_CUISINE_TYPE}}},
        },
    },
)


@router.post(
    "/",
    response_model=CuisineTypeSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "Cuisine type created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "cuisine_id": 1,
                        "name": "Italian",
                        "description": "Traditional Italian cuisine",
                        "region": "Mediterranean",
                    },
                },
            },
        },
    },
)
async def create_cuisine_type(
    cuisine_type: CuisineTypeCreate,
    db: AsyncSession = Depends(get_async_db),
) -> CuisineType:
    """Create a new cuisine type.

    Args:
        cuisine_type: Cuisine type data
        db: Database session

    Returns:
        CuisineType: Created cuisine type

    Raises:
        HTTPException: If cuisine type already exists
    """
    try:
        db_cuisine_type = CuisineType(**cuisine_type.model_dump())
        db.add(db_cuisine_type)
        await db.commit()
        await db.refresh(db_cuisine_type)
        return db_cuisine_type
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_CUISINE_TYPE,
        )


@router.get(
    "/",
    response_model=list[CuisineTypeSchema],
    responses={
        status.HTTP_200_OK: {
            "description": "List of cuisine types retrieved successfully",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "cuisine_id": 1,
                            "name": "Italian",
                            "description": "Traditional Italian cuisine",
                            "region": "Mediterranean",
                        },
                    ],
                },
            },
        },
    },
)
async def get_cuisine_types(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_db),
) -> list[CuisineType]:
    """Get a list of cuisine types.

    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
        db: Database session

    Returns:
        List[CuisineType]: List of cuisine types
    """
    result = await db.execute(select(CuisineType).offset(skip).limit(limit))
    return list(result.scalars().all())


@router.get(
    "/{cuisine_id}",
    response_model=CuisineTypeSchema,
    responses={
        status.HTTP_200_OK: {
            "description": "Cuisine type retrieved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "cuisine_id": 1,
                        "name": "Italian",
                        "description": "Traditional Italian cuisine",
                        "region": "Mediterranean",
                    },
                },
            },
        },
    },
)
async def get_cuisine_type(cuisine_id: int, db: AsyncSession = Depends(get_async_db)) -> CuisineType:
    """Get a specific cuisine type by ID.

    Args:
        cuisine_id: ID of the cuisine type
        db: Database session

    Returns:
        CuisineType: Cuisine type

    Raises:
        HTTPException: If cuisine type not found
    """
    result = await db.execute(select(CuisineType).filter(CuisineType.cuisine_id == cuisine_id))
    db_cuisine_type = result.scalar_one_or_none()
    if db_cuisine_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=CUISINE_TYPE_NOT_FOUND,
        )
    return db_cuisine_type


@router.put(
    "/{cuisine_id}",
    response_model=CuisineTypeSchema,
    responses={
        status.HTTP_200_OK: {
            "description": "Cuisine type updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "cuisine_id": 1,
                        "name": "Italian",
                        "description": "Traditional Italian cuisine",
                        "region": "Mediterranean",
                    },
                },
            },
        },
    },
)
async def update_cuisine_type(
    cuisine_id: int,
    cuisine_type: CuisineTypeCreate,
    db: AsyncSession = Depends(get_async_db),
) -> CuisineType:
    """Update a specific cuisine type.

    Args:
        cuisine_id: ID of the cuisine type to update
        cuisine_type: Updated cuisine type data
        db: Database session

    Returns:
        CuisineType: Updated cuisine type

    Raises:
        HTTPException: If cuisine type not found or if update violates constraints
    """
    try:
        result = await db.execute(select(CuisineType).filter(CuisineType.cuisine_id == cuisine_id))
        db_cuisine_type = result.scalar_one_or_none()
        if db_cuisine_type is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=CUISINE_TYPE_NOT_FOUND,
            )

        update_data = cuisine_type.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_cuisine_type, key, value)

        await db.commit()
        await db.refresh(db_cuisine_type)
        return db_cuisine_type
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_CUISINE_TYPE,
        )


@router.delete(
    "/{cuisine_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {
            "description": "Cuisine type deleted successfully",
        },
        status.HTTP_409_CONFLICT: {
            "description": "Cannot delete cuisine type that is referenced by recipes",
            "content": {"application/json": {"example": {"detail": CUISINE_TYPE_IN_USE}}},
        },
    },
)
async def delete_cuisine_type(cuisine_id: int, db: AsyncSession = Depends(get_async_db)) -> None:
    """Delete a specific cuisine type.

    Args:
        cuisine_id: ID of the cuisine type to delete
        db: Database session

    Raises:
        HTTPException: If cuisine type not found or if deletion violates constraints
    """
    result = await db.execute(select(CuisineType).filter(CuisineType.cuisine_id == cuisine_id))
    db_cuisine_type = result.scalar_one_or_none()
    if db_cuisine_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=CUISINE_TYPE_NOT_FOUND,
        )

    try:
        await db.delete(db_cuisine_type)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=CUISINE_TYPE_IN_USE,
        )
