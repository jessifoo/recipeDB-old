"""Ingredients router.

This module provides endpoints for managing ingredients in the recipe database.
It supports CRUD operations for ingredients with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.ingredients import router as ingredients_router
        app.include_router(ingredients_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import Ingredient
from app.schemas.models import Ingredient as IngredientSchema, IngredientCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Ingredient not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "INGREDIENT_NOT_FOUND",
                        "message": "Ingredient not found",
                        "details": {"ingredient_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Ingredient already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "INGREDIENT_EXISTS",
                        "message": "Ingredient with this name already exists",
                        "details": {"name": "Salt"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=IngredientSchema, status_code=status.HTTP_201_CREATED)
async def create_ingredient(
    ingredient: IngredientCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> Ingredient:
    """Create a new ingredient.

    This endpoint creates a new ingredient in the database. It validates
    the input data and ensures uniqueness of the ingredient name.

    Args:
        ingredient (:class:`~app.schemas.models.IngredientCreate`):
            The ingredient data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.Ingredient`: The created ingredient.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If an ingredient with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            ingredient = await create_ingredient(
                IngredientCreate(name="Salt", description="Table salt"),
                db_session
            )
    """
    try:
        db_ingredient = Ingredient(**ingredient.model_dump())
        db.add(db_ingredient)
        await db.commit()
        await db.refresh(db_ingredient)
        return db_ingredient
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="Ingredient", identifier=ingredient.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_ingredient", details={"ingredient_data": ingredient.model_dump()}
        ) from err


@router.get("/", response_model=list[IngredientSchema])
async def get_ingredients(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[Ingredient]:
    """Retrieve a list of ingredients.

    This endpoint returns a paginated list of ingredients.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.Ingredient`]:
            List of ingredients.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            ingredients = await get_ingredients(skip=0, limit=10, db_session)
            for ingredient in ingredients:
                print(ingredient.name)
    """
    try:
        stmt: Select[tuple[Ingredient]] = select(Ingredient).offset(skip).limit(limit)
        result: Result[tuple[Ingredient]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_ingredients", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{ingredient_id}", response_model=IngredientSchema)
async def get_ingredient(
    ingredient_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> Ingredient:
    """Retrieve a specific ingredient by ID.

    This endpoint returns a single ingredient identified by its ID.

    Args:
        ingredient_id (int):
            The unique identifier of the ingredient.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.Ingredient`:
            The requested ingredient.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the ingredient is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            ingredient = await get_ingredient(1, db_session)
            print(f"Found ingredient: {ingredient.name}")
    """
    try:
        stmt: Select[tuple[Ingredient]] = select(Ingredient).filter(Ingredient.ingredient_id == ingredient_id)
        result: Result[tuple[Ingredient]] = await db.execute(stmt)
        db_ingredient = result.scalar_one_or_none()

        if db_ingredient is None:
            raise ResourceNotFoundError(resource_type="Ingredient", identifier=ingredient_id, lang=lang)

        return db_ingredient
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_ingredient", details={"ingredient_id": ingredient_id}
        ) from err


@router.put("/{ingredient_id}", response_model=IngredientSchema)
async def update_ingredient(
    ingredient_id: int,
    ingredient: IngredientCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> Ingredient:
    """Update a specific ingredient.

    This endpoint updates an existing ingredient with new data.
    It validates the input and ensures uniqueness of the ingredient name.

    Args:
        ingredient_id (int):
            The unique identifier of the ingredient to update.
        ingredient (:class:`~app.schemas.models.IngredientCreate`):
            The updated ingredient data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.Ingredient`:
            The updated ingredient.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the ingredient is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_ingredient(
                1,
                IngredientCreate(name="Sea Salt", description="Updated description"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = ingredient.model_dump(exclude_unset=True)
        stmt = (
            update(Ingredient)
            .where(Ingredient.ingredient_id == ingredient_id)
            .values(**update_data)
            .returning(Ingredient)
        )
        result = await db.execute(stmt)
        db_ingredient = result.scalar_one_or_none()

        if db_ingredient is None:
            raise ResourceNotFoundError(resource_type="Ingredient", identifier=ingredient_id, lang=lang)

        await db.commit()
        return db_ingredient

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="Ingredient", identifier=ingredient.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_ingredient",
            details={"ingredient_id": ingredient_id, "update_data": ingredient.model_dump()},
        ) from err


@router.delete("/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ingredient(
    ingredient_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific ingredient.

    This endpoint removes an ingredient from the database.
    It fails if the ingredient is referenced by any recipes.

    Args:
        ingredient_id (int):
            The unique identifier of the ingredient to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the ingredient is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the ingredient is referenced by recipes.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_ingredient(1, db_session)
            # The ingredient is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(Ingredient).where(Ingredient.ingredient_id == ingredient_id).returning(Ingredient.ingredient_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="Ingredient", identifier=ingredient_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="Ingredient", identifier=ingredient_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_ingredient", details={"ingredient_id": ingredient_id}
        ) from err
