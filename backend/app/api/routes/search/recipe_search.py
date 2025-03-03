"""Recipe search router.

This module provides endpoints for searching and filtering recipes in the database.
It supports advanced search functionality with filters for cuisine, diet, ingredients,
cooking time, and more.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.search.recipe_search import router as recipe_search_router
        app.include_router(recipe_search_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.exc import SQLAlchemyError

from app.core.error_messages import ErrorMessages, Language
from app.core.exceptions import BusinessError, DatabaseError
from app.database.session import get_async_db
from app.schemas.recipe import RecipeList, RecipeSearchFilter
from app.services.recipe_search import RecipeSearchService

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/search",
    tags=["recipe-search"],
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid search parameters",
            "content": {
                "application/json": {
                    "example": {
                        "code": "VALIDATION_ERROR",
                        "message": "Invalid search parameters",
                        "details": {"query": "Search query must not be empty"},
                    }
                }
            },
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid filter parameters",
            "content": {
                "application/json": {
                    "example": {
                        "code": "VALIDATION_ERROR",
                        "message": "Invalid filter parameters",
                        "details": {"max_cooking_time": "Must be a positive integer"},
                    }
                }
            },
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Database error during search",
            "content": {
                "application/json": {
                    "example": {
                        "code": "DATABASE_ERROR",
                        "message": "Failed to execute recipe search",
                        "details": {"error": "Database connection error"},
                    }
                }
            },
        },
    },
)


@router.get("/", response_model=RecipeList)
async def search_recipes(
    query: str = Query(..., description="Search query string", min_length=1),
    filters: RecipeSearchFilter | None = None,
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> RecipeList:
    """Search for recipes with filters and pagination.

    This endpoint provides advanced recipe search functionality with support for
    filtering by cuisine, diet, ingredients, cooking time, and more. Results are
    paginated and ordered by relevance.

    Args:
        query (str):
            Search query string. Must not be empty.
        filters (:class:`~app.schemas.recipe.RecipeSearchFilter`, optional):
            Optional search filters for cuisine, diet, ingredients, etc.
        page (int, optional):
            Page number for pagination. Must be positive. Defaults to 1.
        page_size (int, optional):
            Number of items per page. Must be between 1 and 100. Defaults to 20.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.schemas.recipe.RecipeList`:
            List of matching recipes with total count and source information.

    Raises:
        :exc:`~app.core.exceptions.BusinessError`:
            If the search parameters are invalid.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            # Search for Italian vegetarian recipes
            result = await search_recipes(
                query="pasta",
                filters=RecipeSearchFilter(
                    cuisine="Italian",
                    diet="vegetarian",
                    max_cooking_time=30
                ),
                page=1,
                page_size=20,
                db_session
            )
            print(f"Found {result.total} recipes")
            for recipe in result.results:
                print(f"{recipe.title} - {recipe.cooking_time} minutes")
    """
    filter_dict: dict[str, Any] = {}
    try:
        if not query.strip():
            raise BusinessError(
                message_template=ErrorMessages.SEARCH_QUERY_EMPTY,
                details={"query": "A non-empty search query is required"},
                lang=lang,
            )

        search_service = RecipeSearchService(db)
        if filters:
            filter_dict = filters.model_dump()

        # Calculate offset from page and page_size
        offset = (page - 1) * page_size

        # Perform search with pagination
        return await search_service.search(query=query, filters=filter_dict, offset=offset, limit=page_size)

    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="search_recipes",
            details={"query": query, "filters": filter_dict, "pagination": {"page": page, "page_size": page_size}},
        ) from err
    except ValueError as err:
        raise BusinessError(
            message_template=ErrorMessages.INVALID_FILTER_PARAMS,
            details={"error": str(err), "filters": filter_dict},
            lang=lang,
        ) from err
