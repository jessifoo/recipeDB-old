"""Dietary restrictions router.

This module provides endpoints for managing dietary restrictions.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from app.core.constants import DIETARY_RESTRICTION_IN_USE, DIETARY_RESTRICTION_NOT_FOUND, DUPLICATE_DIETARY_RESTRICTION
from app.database.session import get_async_db
from app.models.models import DietaryRestriction
from app.schemas.models import DietaryRestriction as DietaryRestrictionSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.schemas.models import DietaryRestrictionCreate

router = APIRouter(
    prefix="/dietary-restrictions",
    tags=["dietary-restrictions"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Dietary restriction not found",
            "content": {"application/json": {"example": {"detail": DIETARY_RESTRICTION_NOT_FOUND}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": "Dietary restriction already exists",
            "content": {"application/json": {"example": {"detail": DUPLICATE_DIETARY_RESTRICTION}}},
        },
    },
)


@router.post(
    "/",
    response_model=DietaryRestrictionSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Dietary restriction created successfully"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid dietary restriction data"},
        status.HTTP_409_CONFLICT: {"description": "Dietary restriction with this name already exists"},
    },
)
async def create_dietary_restriction(
    dietary_restriction: DietaryRestrictionCreate,
    db: AsyncSession = Depends(get_async_db),
) -> DietaryRestriction:
    """Create a new dietary restriction."""
    try:
        db_dietary_restriction = DietaryRestriction(**dietary_restriction.model_dump())
        db.add(db_dietary_restriction)
        await db.commit()
        await db.refresh(db_dietary_restriction)
        return db_dietary_restriction
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_DIETARY_RESTRICTION,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[DietaryRestrictionSchema],
    responses={status.HTTP_200_OK: {"description": "List of dietary restrictions retrieved successfully"}},
)
async def get_dietary_restrictions(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_db),
) -> list[DietaryRestriction]:
    """Get a list of dietary restrictions with pagination."""
    result = await db.execute(select(DietaryRestriction).offset(skip).limit(limit))
    return list(result.scalars().all())


@router.get(
    "/{restriction_id}",
    response_model=DietaryRestrictionSchema,
    responses={
        status.HTTP_200_OK: {"description": "Dietary restriction retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Dietary restriction not found"},
    },
)
async def get_dietary_restriction(restriction_id: int, db: AsyncSession = Depends(get_async_db)) -> DietaryRestriction:
    """Get a specific dietary restriction by ID."""
    result = await db.execute(select(DietaryRestriction).filter(DietaryRestriction.restriction_id == restriction_id))
    db_dietary_restriction = result.scalar_one_or_none()
    if db_dietary_restriction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=DIETARY_RESTRICTION_NOT_FOUND,
        )
    return db_dietary_restriction


@router.put(
    "/{restriction_id}",
    response_model=DietaryRestrictionSchema,
    responses={
        status.HTTP_200_OK: {"description": "Dietary restriction updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Dietary restriction not found"},
        status.HTTP_409_CONFLICT: {"description": "Dietary restriction with this name already exists"},
    },
)
async def update_dietary_restriction(
    restriction_id: int,
    dietary_restriction: DietaryRestrictionCreate,
    db: AsyncSession = Depends(get_async_db),
) -> DietaryRestriction:
    """Update a specific dietary restriction."""
    try:
        result = await db.execute(
            select(DietaryRestriction).filter(DietaryRestriction.restriction_id == restriction_id),
        )
        db_dietary_restriction = result.scalar_one_or_none()
        if db_dietary_restriction is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=DIETARY_RESTRICTION_NOT_FOUND,
            )

        update_data = dietary_restriction.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_dietary_restriction, key, value)

        await db.commit()
        await db.refresh(db_dietary_restriction)
        return db_dietary_restriction
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_DIETARY_RESTRICTION,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete(
    "/{restriction_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Dietary restriction deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Dietary restriction not found"},
        status.HTTP_409_CONFLICT: {
            "description": "Cannot delete dietary restriction that is referenced by family members",
            "content": {"application/json": {"example": {"detail": DIETARY_RESTRICTION_IN_USE}}},
        },
    },
)
async def delete_dietary_restriction(restriction_id: int, db: AsyncSession = Depends(get_async_db)) -> None:
    """Delete a specific dietary restriction."""
    result = await db.execute(select(DietaryRestriction).filter(DietaryRestriction.restriction_id == restriction_id))
    db_dietary_restriction = result.scalar_one_or_none()
    if db_dietary_restriction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=DIETARY_RESTRICTION_NOT_FOUND,
        )

    try:
        await db.delete(db_dietary_restriction)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DIETARY_RESTRICTION_IN_USE,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
