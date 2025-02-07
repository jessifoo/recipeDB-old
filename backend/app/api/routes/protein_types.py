"""Protein type routes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError

from app.core.constants import DUPLICATE_PROTEIN_TYPE, PROTEIN_TYPE_IN_USE, PROTEIN_TYPE_NOT_FOUND
from app.database.session import get_db
from app.models.models import ProteinType as ProteinTypeModel
from app.schemas.models import ProteinType as ProteinTypeSchema

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

    from app.schemas.models import ProteinTypeCreate

router = APIRouter(
    prefix="/protein-types",
    tags=["protein-types"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": PROTEIN_TYPE_NOT_FOUND,
            "content": {"application/json": {"example": {"detail": PROTEIN_TYPE_NOT_FOUND}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": DUPLICATE_PROTEIN_TYPE,
            "content": {"application/json": {"example": {"detail": DUPLICATE_PROTEIN_TYPE}}},
        },
    },
)


@router.post(
    "/",
    response_model=ProteinTypeSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Protein type created successfully"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid protein type data"},
        status.HTTP_409_CONFLICT: {"description": DUPLICATE_PROTEIN_TYPE},
    },
)
async def create_protein_type(
    protein_type: ProteinTypeCreate,
    db: Session = Depends(get_db),
) -> ProteinTypeModel:
    """Create a new protein type."""
    try:
        db_protein_type = ProteinTypeModel(**protein_type.model_dump())
        db.add(db_protein_type)
        db.commit()
        db.refresh(db_protein_type)
        return db_protein_type
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_PROTEIN_TYPE,
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[ProteinTypeSchema],
    summary="Get protein types",
    description="Get a list of protein types with pagination.",
    responses={
        200: {
            "description": "List of protein types",
            "content": {
                "application/json": {
                    "example": [{"protein_id": 1, "name": "Chicken", "description": "Poultry protein"}],
                },
            },
        },
    },
)
async def get_protein_types(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[ProteinTypeModel]:
    """Get a list of protein types with pagination."""
    query = db.query(ProteinTypeModel).offset(skip).limit(limit)
    return list(query.all())


@router.get(
    "/{protein_id}",
    response_model=ProteinTypeSchema,
    responses={
        status.HTTP_200_OK: {"description": "Protein type retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": PROTEIN_TYPE_NOT_FOUND},
    },
)
async def get_protein_type(protein_id: int, db: Session = Depends(get_db)) -> ProteinTypeModel:
    """Get a specific protein type by ID."""
    db_protein_type = db.query(ProteinTypeModel).filter(ProteinTypeModel.protein_id == protein_id).first()
    if db_protein_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=PROTEIN_TYPE_NOT_FOUND,
        )
    return db_protein_type


@router.put(
    "/{protein_id}",
    response_model=ProteinTypeSchema,
    responses={
        status.HTTP_200_OK: {"description": "Protein type updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": PROTEIN_TYPE_NOT_FOUND},
        status.HTTP_409_CONFLICT: {"description": DUPLICATE_PROTEIN_TYPE},
    },
)
async def update_protein_type(
    protein_id: int,
    protein_type: ProteinTypeCreate,
    db: Session = Depends(get_db),
) -> ProteinTypeModel:
    """Update a specific protein type."""
    try:
        db_protein_type = db.query(ProteinTypeModel).filter(ProteinTypeModel.protein_id == protein_id).first()
        if db_protein_type is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=PROTEIN_TYPE_NOT_FOUND,
            )

        update_data = protein_type.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_protein_type, key, value)

        db.commit()
        db.refresh(db_protein_type)
        return db_protein_type
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DUPLICATE_PROTEIN_TYPE,
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete(
    "/{protein_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Protein type deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": PROTEIN_TYPE_NOT_FOUND},
        status.HTTP_409_CONFLICT: {"description": PROTEIN_TYPE_IN_USE},
    },
)
async def delete_protein_type(protein_id: int, db: Session = Depends(get_db)) -> None:
    """Delete a specific protein type."""
    db_protein_type = db.query(ProteinTypeModel).filter(ProteinTypeModel.protein_id == protein_id).first()
    if db_protein_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=PROTEIN_TYPE_NOT_FOUND,
        )

    try:
        db.delete(db_protein_type)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=PROTEIN_TYPE_IN_USE,
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
