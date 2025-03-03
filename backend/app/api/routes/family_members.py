"""Family members router.

This module provides endpoints for managing family members in the recipe database.
It supports CRUD operations for family members with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.family_members import router as family_members_router
        app.include_router(family_members_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import FamilyMember
from app.schemas.models import FamilyMember as FamilyMemberSchema, FamilyMemberCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/family-members",
    tags=["family-members"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Family member not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "FAMILY_MEMBER_NOT_FOUND",
                        "message": "Family member not found",
                        "details": {"member_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Family member already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "FAMILY_MEMBER_EXISTS",
                        "message": "Family member with this name already exists",
                        "details": {"name": "John Doe"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=FamilyMemberSchema, status_code=status.HTTP_201_CREATED)
async def create_family_member(
    family_member: FamilyMemberCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> FamilyMember:
    """Create a new family member.

    This endpoint creates a new family member in the database. It validates
    the input data and ensures uniqueness of the member name.

    Args:
        family_member (:class:`~app.schemas.models.FamilyMemberCreate`):
            The family member data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.FamilyMember`: The created family member.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a family member with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            member = await create_family_member(
                FamilyMemberCreate(
                    name="John Doe",
                    birth_date="1990-01-01",
                    notes="Allergic to peanuts"
                ),
                db_session
            )
    """
    try:
        db_family_member = FamilyMember(**family_member.model_dump())
        db.add(db_family_member)
        await db.commit()
        await db.refresh(db_family_member)
        return db_family_member
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="FamilyMember", identifier=family_member.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_family_member", details={"family_member_data": family_member.model_dump()}
        ) from err


@router.get("/", response_model=list[FamilyMemberSchema])
async def get_family_members(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[FamilyMember]:
    """Retrieve a list of family members.

    This endpoint returns a paginated list of family members.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.FamilyMember`]:
            List of family members.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            members = await get_family_members(skip=0, limit=10, db_session)
            for member in members:
                print(member.name)
    """
    try:
        stmt: Select[tuple[FamilyMember]] = select(FamilyMember).offset(skip).limit(limit)
        result: Result[tuple[FamilyMember]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_family_members", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{member_id}", response_model=FamilyMemberSchema)
async def get_family_member(
    member_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> FamilyMember:
    """Retrieve a specific family member by ID.

    This endpoint returns a single family member identified by their ID.

    Args:
        member_id (int):
            The unique identifier of the family member.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.FamilyMember`:
            The requested family member.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the family member is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            member = await get_family_member(1, db_session)
            print(f"Found member: {member.name}")
    """
    try:
        stmt: Select[tuple[FamilyMember]] = select(FamilyMember).filter(FamilyMember.member_id == member_id)
        result: Result[tuple[FamilyMember]] = await db.execute(stmt)
        db_family_member = result.scalar_one_or_none()

        if db_family_member is None:
            raise ResourceNotFoundError(resource_type="FamilyMember", identifier=member_id, lang=lang)

        return db_family_member
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_family_member", details={"member_id": member_id}
        ) from err


@router.put("/{member_id}", response_model=FamilyMemberSchema)
async def update_family_member(
    member_id: int,
    family_member: FamilyMemberCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> FamilyMember:
    """Update a specific family member.

    This endpoint updates an existing family member with new data.
    It validates the input and ensures uniqueness of the member name.

    Args:
        member_id (int):
            The unique identifier of the family member to update.
        family_member (:class:`~app.schemas.models.FamilyMemberCreate`):
            The updated family member data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.FamilyMember`:
            The updated family member.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the family member is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_family_member(
                1,
                FamilyMemberCreate(
                    name="John Smith",
                    birth_date="1990-01-01",
                    notes="Updated notes"
                ),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = family_member.model_dump(exclude_unset=True)
        stmt = (
            update(FamilyMember)
            .where(FamilyMember.member_id == member_id)
            .values(**update_data)
            .returning(FamilyMember)
        )
        result = await db.execute(stmt)
        db_family_member = result.scalar_one_or_none()

        if db_family_member is None:
            raise ResourceNotFoundError(resource_type="FamilyMember", identifier=member_id, lang=lang)

        await db.commit()
        return db_family_member

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="FamilyMember", identifier=family_member.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_family_member",
            details={"member_id": member_id, "update_data": family_member.model_dump()},
        ) from err


@router.delete("/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_family_member(
    member_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific family member.

    This endpoint removes a family member from the database.
    It fails if the member has associated data (e.g., meal plans, preferences).

    Args:
        member_id (int):
            The unique identifier of the family member to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the family member is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the family member has associated data.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_family_member(1, db_session)
            # The family member is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(FamilyMember).where(FamilyMember.member_id == member_id).returning(FamilyMember.member_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="FamilyMember", identifier=member_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="FamilyMember", identifier=member_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_family_member", details={"member_id": member_id}
        ) from err
