"""Allergen routes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from app.core.constants import ALLERGEN_IN_USE, ALLERGEN_NOT_FOUND, DUPLICATE_ALLERGEN
from app.database.session import get_async_db
from app.models.models import Allergen as AllergenModel
from app.schemas.models import Allergen as AllergenSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.schemas.models import AllergenCreate

router = APIRouter(
    prefix="/allergens",
    tags=["allergens"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Allergen not found",
            "content": {"application/json": {"example": {"detail": ALLERGEN_NOT_FOUND}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": "Allergen already exists",
            "content": {"application/json": {"example": {"detail": DUPLICATE_ALLERGEN}}},
        },
    },
)


@router.post(
    "/",
    response_model=AllergenSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Allergen created successfully"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid allergen data"},
        status.HTTP_409_CONFLICT: {"description": "Allergen with this name already exists"},
    },
)
async def create_allergen(
    allergen: AllergenCreate,
    db: AsyncSession = Depends(get_async_db),
) -> AllergenModel:
    """Create a new allergen."""
    try:
        db_allergen = AllergenModel(**allergen.model_dump())
        db.add(db_allergen)
        await db.commit()
        await db.refresh(db_allergen)
        return db_allergen
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_ALLERGEN,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[AllergenSchema],
    responses={status.HTTP_200_OK: {"description": "List of allergens retrieved successfully"}},
)
async def get_allergens(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_db),
) -> list[AllergenModel]:
    """Get a list of allergens with pagination."""
    result = await db.execute(select(AllergenModel).offset(skip).limit(limit))
    return list(result.scalars().all())


@router.get(
    "/{allergen_id}",
    response_model=AllergenSchema,
    responses={
        status.HTTP_200_OK: {"description": "Allergen retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Allergen not found"},
    },
)
async def get_allergen(allergen_id: int, db: AsyncSession = Depends(get_async_db)) -> AllergenModel:
    """Get a specific allergen by ID."""
    result = await db.execute(select(AllergenModel).filter(AllergenModel.allergen_id == allergen_id))
    db_allergen = result.scalar_one_or_none()
    if db_allergen is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ALLERGEN_NOT_FOUND,
        )
    return db_allergen


@router.put(
    "/{allergen_id}",
    response_model=AllergenSchema,
    responses={
        status.HTTP_200_OK: {"description": "Allergen updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Allergen not found"},
        status.HTTP_409_CONFLICT: {"description": "Allergen with this name already exists"},
    },
)
async def update_allergen(
    allergen_id: int,
    allergen: AllergenCreate,
    db: AsyncSession = Depends(get_async_db),
) -> AllergenModel:
    """Update a specific allergen."""
    result = await db.execute(select(AllergenModel).filter(AllergenModel.allergen_id == allergen_id))
    db_allergen = result.scalar_one_or_none()
    if db_allergen is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ALLERGEN_NOT_FOUND,
        )

    try:
        update_data = allergen.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_allergen, key, value)

        await db.commit()
        await db.refresh(db_allergen)
        return db_allergen
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_ALLERGEN,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete(
    "/{allergen_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Allergen deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Allergen not found"},
        status.HTTP_409_CONFLICT: {"description": "Cannot delete allergen that is referenced by other records"},
    },
)
async def delete_allergen(allergen_id: int, db: AsyncSession = Depends(get_async_db)) -> None:
    """Delete a specific allergen."""
    result = await db.execute(select(AllergenModel).filter(AllergenModel.allergen_id == allergen_id))
    db_allergen = result.scalar_one_or_none()
    if db_allergen is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ALLERGEN_NOT_FOUND,
        )

    try:
        await db.delete(db_allergen)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=ALLERGEN_IN_USE,
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
