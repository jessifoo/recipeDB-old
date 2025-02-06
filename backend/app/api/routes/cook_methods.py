"""Cook methods router.

This module provides endpoints for managing cooking methods.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from app.core.constants import COOK_METHOD_IN_USE, COOK_METHOD_NOT_FOUND, DUPLICATE_COOK_METHOD
from app.database.session import get_async_db
from app.models.models import CookMethod
from app.schemas.models import CookMethod as CookMethodSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.schemas.models import CookMethodCreate

router = APIRouter(
    prefix="/cook-methods",
    tags=["cook-methods"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Cook method not found",
            "content": {"application/json": {"example": {"detail": COOK_METHOD_NOT_FOUND}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": "Cook method already exists",
            "content": {"application/json": {"example": {"detail": DUPLICATE_COOK_METHOD}}},
        },
    },
)


@router.post(
    "/",
    response_model=CookMethodSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Cook method created successfully"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid cook method data"},
        status.HTTP_409_CONFLICT: {"description": "Cook method with this name already exists"},
    },
)
async def create_cook_method(cook_method: CookMethodCreate, db: AsyncSession = Depends(get_async_db)) -> CookMethod:
    """Create a new cook method."""
    try:
        db_cook_method = CookMethod(**cook_method.model_dump())
        db.add(db_cook_method)
        await db.commit()
        await db.refresh(db_cook_method)
        return db_cook_method
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_COOK_METHOD,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[CookMethodSchema],
    responses={status.HTTP_200_OK: {"description": "List of cook methods retrieved successfully"}},
)
async def get_cook_methods(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_db),
) -> list[CookMethod]:
    """Get a list of cook methods with pagination."""
    result = await db.execute(select(CookMethod).offset(skip).limit(limit))
    return list(result.scalars().all())


@router.get(
    "/{method_id}",
    response_model=CookMethodSchema,
    responses={
        status.HTTP_200_OK: {"description": "Cook method retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Cook method not found"},
    },
)
async def get_cook_method(method_id: int, db: AsyncSession = Depends(get_async_db)) -> CookMethod:
    """Get a specific cook method by ID."""
    result = await db.execute(select(CookMethod).filter(CookMethod.method_id == method_id))
    db_cook_method = result.scalar_one_or_none()
    if db_cook_method is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=COOK_METHOD_NOT_FOUND,
        )
    return db_cook_method


@router.put(
    "/{method_id}",
    response_model=CookMethodSchema,
    responses={
        status.HTTP_200_OK: {"description": "Cook method updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Cook method not found"},
        status.HTTP_409_CONFLICT: {"description": "Cook method with this name already exists"},
    },
)
async def update_cook_method(
    method_id: int,
    cook_method: CookMethodCreate,
    db: AsyncSession = Depends(get_async_db),
) -> CookMethod:
    """Update a specific cook method."""
    try:
        result = await db.execute(select(CookMethod).filter(CookMethod.method_id == method_id))
        db_cook_method = result.scalar_one_or_none()
        if db_cook_method is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=COOK_METHOD_NOT_FOUND,
            )

        update_data = cook_method.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_cook_method, key, value)

        await db.commit()
        await db.refresh(db_cook_method)
        return db_cook_method
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_COOK_METHOD,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete(
    "/{method_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Cook method deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Cook method not found"},
        status.HTTP_409_CONFLICT: {
            "description": "Cannot delete cook method that is referenced by recipes",
            "content": {"application/json": {"example": {"detail": COOK_METHOD_IN_USE}}},
        },
    },
)
async def delete_cook_method(method_id: int, db: AsyncSession = Depends(get_async_db)) -> None:
    """Delete a specific cook method."""
    result = await db.execute(select(CookMethod).filter(CookMethod.method_id == method_id))
    db_cook_method = result.scalar_one_or_none()
    if db_cook_method is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=COOK_METHOD_NOT_FOUND,
        )

    try:
        await db.delete(db_cook_method)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=COOK_METHOD_IN_USE,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
