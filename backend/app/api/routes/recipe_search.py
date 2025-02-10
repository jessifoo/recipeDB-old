"""Recipe search router.

This module provides endpoints for searching recipes from various sources.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.recipe_search import router as recipe_search_router
        app.include_router(recipe_search_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx
from fastapi import APIRouter, Query, status
from fastapi_cache.decorator import cache
from sqlalchemy.exc import SQLAlchemyError

from app.core.error_messages import ErrorMessages, Language
from app.core.exceptions import BusinessError, DatabaseError, DomainError, ResourceNotFoundError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_search import RecipeSearchService

if TYPE_CHECKING:
    from app.api.deps import DatabaseSession

router = APIRouter(
    prefix="/recipe-search",
    tags=["recipe-search"],
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid search parameters",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.INVALID_FILTER_PARAMS.get_message(
                            lang=Language.EN, details="Invalid search parameters"
                        )
                    }
                }
            },
        },
        status.HTTP_503_SERVICE_UNAVAILABLE: {
            "description": "External recipe service unavailable",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.BUSINESS_RULE_VIOLATION.get_message(
                            lang=Language.EN, details="Recipe service is currently unavailable"
                        )
                    }
                }
            },
        },
    },
)


@router.get(
    "/",
    response_model=RecipeList,
    responses={
        status.HTTP_200_OK: {"description": "Recipe search results retrieved successfully"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid search parameters"},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"description": "External recipe service unavailable"},
    },
)
async def search_recipes(
    db: DatabaseSession,
    query: str = Query(..., description="Search query string"),
    cuisine: str | None = Query(None, description="Cuisine type filter"),
    diet: str | None = Query(None, description="Dietary restriction filter"),
    exclude: list[str] | None = Query(None, description="Ingredients to exclude"),
    max_time: int | None = Query(None, description="Maximum total time in minutes"),
    service: str | None = Query(None, description="Specific recipe service to use"),
) -> RecipeList:
    """Search for recipes across multiple services.

    This endpoint searches for recipes using the specified criteria across multiple
    recipe services (Spoonacular, Edamam, etc.) and returns a unified list of results.

    Args:
        db: Injected database session for the operation
        query: Search query string
        cuisine: Filter by cuisine type
        diet: Filter by dietary restriction
        exclude: List of ingredients to exclude
        max_time: Maximum total cooking time in minutes
        service: Specific recipe service to use (optional)

    Returns:
        RecipeList: List of recipes matching the search criteria

    Raises:
        BusinessError: If search parameters are invalid
        BusinessError: If recipe service is unavailable
        DatabaseError: If database operation fails
    """
    try:
        search_service = RecipeSearchService(db)
        return await search_service.search(
            query=query, cuisine=cuisine, diet=diet, exclude=exclude, max_time=max_time, service=service
        )
    except BusinessError:
        # Re-raise business errors (validation, service unavailable) as is
        raise
    except DatabaseError as err:
        # Re-raise database errors with operation context preserved
        raise DatabaseError.from_sqlalchemy(
            error=err.context.original_error or err, operation="recipe_search", details=err.context.details
        ) from err
    except httpx.HTTPStatusError as err:
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            details={"error": f"External service error: {err.response.status_code} - {err!s}"},
        ) from err
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="recipe_search") from err
    except DomainError as err:
        raise BusinessError(message_template=ErrorMessages.INVALID_FILTER_PARAMS, details={"error": str(err)}) from err


@router.get(
    "/{recipe_id}",
    response_model=RecipeSearchResult,
    responses={
        status.HTTP_200_OK: {"description": "Recipe details retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Recipe not found"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid recipe ID format"},
    },
)
@cache(expire=3600)
async def get_recipe(recipe_id: str, db: DatabaseSession) -> RecipeSearchResult:
    """Get detailed information for a specific recipe.

    Args:
        recipe_id: ID of the recipe to retrieve
        db: Injected database session for the operation

    Returns:
        RecipeSearchResult: Detailed recipe information

    Raises:
        BusinessError: If recipe ID format is invalid
        BusinessError: If recipe service is unavailable
        DatabaseError: If database operation fails
        ResourceNotFoundError: If recipe is not found
    """
    try:
        search_service = RecipeSearchService(db)
        results = await search_service.search(query=f"id:{recipe_id}", limit=1)
        if not results.total:
            raise ResourceNotFoundError(resource_type="Recipe", identifier=recipe_id)
        return results.results[0]
    except BusinessError:
        # Re-raise business errors (validation, service unavailable) as is
        raise
    except DatabaseError as err:
        # Re-raise database errors with operation context preserved
        raise DatabaseError.from_sqlalchemy(
            error=err.context.original_error or err, operation="get_recipe", details=err.context.details
        ) from err
    except ResourceNotFoundError:
        # Re-raise not found errors as is
        raise
    except httpx.HTTPStatusError as err:
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            details={"error": f"External service error: {err.response.status_code} - {err!s}"},
        ) from err
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="get_recipe") from err
    except ValueError as err:
        raise BusinessError(
            message_template=ErrorMessages.INVALID_FILTER_PARAMS, details={"error": "Invalid recipe ID format"}
        ) from err
