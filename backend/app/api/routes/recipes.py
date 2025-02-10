"""Recipes router.

This module provides endpoints for managing recipes in the database, including CRUD operations
and relationship management.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.recipes import router as recipe_router
        app.include_router(recipe_router)

Note:
    All endpoints in this module require database access and handle common error cases
    such as duplicate recipes, constraint violations, and missing resources.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages, Language
from app.core.exceptions import BusinessError, DatabaseError, ResourceNotFoundError
from app.models.models import Recipe
from app.schemas.models import Recipe as RecipeSchema

if TYPE_CHECKING:
    from app.api.deps import DatabaseSession
    from app.schemas.models import RecipeCreate

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Recipe not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.RESOURCE_NOT_FOUND.get_message(
                            lang=Language.EN, details={"resource_type": "Recipe", "identifier": "123"}
                        )
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Recipe operation failed due to constraint violation",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.BUSINESS_RULE_VIOLATION.get_message(
                            lang=Language.EN, details={"error": "Recipe with this title already exists"}
                        )
                    }
                }
            },
        },
    },
)


@router.post(
    "/",
    response_model=RecipeSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Recipe created successfully"},
        status.HTTP_409_CONFLICT: {"description": "Recipe with this title already exists"},
    },
)
async def create_recipe(recipe: RecipeCreate, db: DatabaseSession) -> Recipe:
    """Create a new recipe.

    This endpoint creates a new recipe in the database with the provided details.
    It ensures that no duplicate recipes exist with the same title.

    Args:
        recipe: Recipe data including title, times, servings, etc.
        db: Injected database session for the operation

    Returns:
        Recipe: The newly created recipe with all fields populated

    Raises:
        BusinessError: If a recipe with the same title already exists
        DatabaseError: If the database operation fails
    """
    try:
        db_recipe = Recipe(**recipe.model_dump())
        db.add(db_recipe)
        await db.commit()
        await db.refresh(db_recipe)
        return db_recipe
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.RECIPE_EXISTS,
            details={"error": "Recipe with this title already exists"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="create_recipe") from err


@router.get(
    "/",
    response_model=list[RecipeSchema],
    responses={
        status.HTTP_200_OK: {"description": "List of recipes retrieved successfully"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Database operation failed",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.DATABASE_ERROR.get_message(
                            lang=Language.EN, details={"operation": "list_recipes"}
                        )
                    }
                }
            },
        },
    },
)
async def get_recipes(db: DatabaseSession, skip: int = 0, limit: int = 100) -> list[Recipe]:
    """Get a list of recipes with pagination.

    This endpoint retrieves a paginated list of recipes from the database.

    Args:
        db: Injected database session for the operation
        skip: Number of recipes to skip (for pagination)
        limit: Maximum number of recipes to return

    Returns:
        list[Recipe]: List of recipes within the specified range

    Raises:
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Recipe).offset(skip).limit(limit))
        return list(result.scalars().all())
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="list_recipes") from err


@router.get(
    "/{recipe_id}",
    response_model=RecipeSchema,
    responses={
        status.HTTP_200_OK: {"description": "Recipe retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Recipe not found"},
    },
)
async def get_recipe(recipe_id: int, db: DatabaseSession) -> Recipe:
    """Get a specific recipe by ID.

    This endpoint retrieves detailed information about a specific recipe.

    Args:
        recipe_id: ID of the recipe to retrieve
        db: Injected database session for the operation

    Returns:
        Recipe: The requested recipe's details

    Raises:
        ResourceNotFoundError: If the recipe does not exist
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Recipe).where(Recipe.recipe_id == recipe_id))
        db_recipe = result.scalar_one_or_none()
        if db_recipe is None:
            raise ResourceNotFoundError(resource_type="Recipe", identifier=str(recipe_id))
        return db_recipe
    except ResourceNotFoundError:
        raise
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="get_recipe") from err


@router.put(
    "/{recipe_id}",
    response_model=RecipeSchema,
    responses={
        status.HTTP_200_OK: {"description": "Recipe updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Recipe not found"},
        status.HTTP_409_CONFLICT: {"description": "Update violates unique constraints"},
    },
)
async def update_recipe(recipe_id: int, recipe: RecipeCreate, db: DatabaseSession) -> Recipe:
    """Update a specific recipe.

    This endpoint updates an existing recipe with new data while maintaining
    data integrity constraints.

    Args:
        recipe_id: ID of the recipe to update
        recipe: Updated recipe data
        db: Injected database session for the operation

    Returns:
        Recipe: The updated recipe with all changes applied

    Raises:
        ResourceNotFoundError: If the recipe does not exist
        BusinessError: If the update violates unique constraints
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Recipe).where(Recipe.recipe_id == recipe_id))
        db_recipe = result.scalar_one_or_none()
        if db_recipe is None:
            raise ResourceNotFoundError(resource_type="Recipe", identifier=str(recipe_id))

        update_data = recipe.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_recipe, key, value)

        await db.commit()
        await db.refresh(db_recipe)
        return db_recipe
    except ResourceNotFoundError:
        raise
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.RECIPE_EXISTS,
            details={"error": "Recipe with this title already exists"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="update_recipe") from err


@router.delete(
    "/{recipe_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Recipe deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Recipe not found"},
        status.HTTP_409_CONFLICT: {"description": "Cannot delete recipe that is referenced by meal plans"},
    },
)
async def delete_recipe(recipe_id: int, db: DatabaseSession) -> None:
    """Delete a specific recipe.

    This endpoint removes a recipe from the database if it is not referenced by any meal plans.

    Args:
        recipe_id: ID of the recipe to delete
        db: Injected database session for the operation

    Raises:
        ResourceNotFoundError: If the recipe does not exist
        BusinessError: If the recipe is referenced by meal plans
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Recipe).where(Recipe.recipe_id == recipe_id))
        db_recipe = result.scalar_one_or_none()
        if db_recipe is None:
            raise ResourceNotFoundError(resource_type="Recipe", identifier=str(recipe_id))

        await db.delete(db_recipe)
        await db.commit()
    except ResourceNotFoundError:
        raise
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.RECIPE_IN_USE,
            details={"error": "Cannot delete recipe that is referenced by meal plans"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="delete_recipe") from err
