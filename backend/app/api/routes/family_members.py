"""Family members router.

This module provides endpoints for managing family members.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from app.database.session import get_async_db
from app.models.models import FamilyMember
from app.schemas.models import FamilyMember as FamilyMemberSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.schemas.models import FamilyMemberCreate

router = APIRouter(
    prefix="/family-members",
    tags=["family-members"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Family member not found",
            "content": {"application/json": {"example": {"detail": "Family member not found"}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": "Family member already exists",
            "content": {"application/json": {"example": {"detail": "Family member with this name already exists"}}},
        },
    },
)


@router.post(
    "/",
    response_model=FamilyMemberSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "Family member created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "member_id": 1,
                        "name": "John Doe",
                        "birth_date": "1990-01-01",
                        "notes": "Allergic to peanuts",
                    },
                },
            },
        },
    },
)
async def create_family_member(
    family_member: FamilyMemberCreate,
    db: AsyncSession = Depends(get_async_db),
) -> FamilyMember:
    """Create a new family member.

    Args:
        family_member: Family member data
        db: Database session

    Returns:
        FamilyMember: Created family member

    Raises:
        HTTPException: If family member already exists
    """
    try:
        db_family_member = FamilyMember(**family_member.model_dump())
        db.add(db_family_member)
        await db.commit()
        await db.refresh(db_family_member)
        return db_family_member
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Family member with this name already exists",
        )


@router.get(
    "/",
    response_model=list[FamilyMemberSchema],
    responses={status.HTTP_200_OK: {"description": "List of family members retrieved successfully"}},
)
async def get_family_members(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_db),
) -> list[FamilyMember]:
    """Get a list of family members with pagination."""
    result = await db.execute(select(FamilyMember).offset(skip).limit(limit))
    return list(result.scalars().all())


@router.get(
    "/{member_id}",
    response_model=FamilyMemberSchema,
    responses={
        status.HTTP_200_OK: {
            "description": "Family member retrieved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "member_id": 1,
                        "name": "John Doe",
                        "birth_date": "1990-01-01",
                        "notes": "Allergic to peanuts",
                    },
                },
            },
        },
    },
)
async def get_family_member(member_id: int, db: AsyncSession = Depends(get_async_db)) -> FamilyMember:
    """Get a specific family member by ID.

    Args:
        member_id: ID of the family member
        db: Database session

    Returns:
        FamilyMember: Family member

    Raises:
        HTTPException: If family member not found
    """
    result = await db.execute(FamilyMember.__table__.select().where(FamilyMember.member_id == member_id))
    db_family_member = result.scalar_one_or_none()
    if db_family_member is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Family member not found",
        )
    return db_family_member


@router.put(
    "/{member_id}",
    response_model=FamilyMemberSchema,
    responses={
        status.HTTP_200_OK: {
            "description": "Family member updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "member_id": 1,
                        "name": "John Doe",
                        "birth_date": "1990-01-01",
                        "notes": "Allergic to peanuts",
                    },
                },
            },
        },
    },
)
async def update_family_member(
    member_id: int,
    family_member: FamilyMemberCreate,
    db: AsyncSession = Depends(get_async_db),
) -> FamilyMember:
    """Update a specific family member.

    Args:
        member_id: ID of the family member to update
        family_member: Updated family member data
        db: Database session

    Returns:
        FamilyMember: Updated family member

    Raises:
        HTTPException: If family member not found or if update violates constraints
    """
    try:
        result = await db.execute(FamilyMember.__table__.select().where(FamilyMember.member_id == member_id))
        db_family_member = result.scalar_one_or_none()
        if db_family_member is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Family member not found",
            )

        update_data = family_member.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_family_member, key, value)

        await db.commit()
        await db.refresh(db_family_member)
        return db_family_member
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Family member with this name already exists",
        )


@router.delete(
    "/{member_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {
            "description": "Family member deleted successfully",
        },
        status.HTTP_409_CONFLICT: {
            "description": "Cannot delete family member that has associated data",
            "content": {
                "application/json": {"example": {"detail": "Cannot delete family member that has associated data"}},
            },
        },
    },
)
async def delete_family_member(member_id: int, db: AsyncSession = Depends(get_async_db)) -> None:
    """Delete a specific family member.

    Args:
        member_id: ID of the family member to delete
        db: Database session

    Raises:
        HTTPException: If family member not found or if deletion violates constraints
    """
    try:
        result = await db.execute(FamilyMember.__table__.select().where(FamilyMember.member_id == member_id))
        db_family_member = result.scalar_one_or_none()
        if db_family_member is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Family member not found",
            )

        await db.delete(db_family_member)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cannot delete family member that has associated data",
        )
