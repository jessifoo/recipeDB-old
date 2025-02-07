"""Recipe search router.

This module provides endpoints for searching recipes from various sources.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi_cache.decorator import cache

from app.database.session import get_async_db
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.exceptions import APIError, DatabaseError
from app.services.recipe_search import RecipeSearchService

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/recipe-search",
    tags=["recipe-search"],
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid search parameters",
            "content": {"application/json": {"example": {"detail": "Invalid search parameters"}}},
        },
        status.HTTP_503_SERVICE_UNAVAILABLE: {
            "description": "External recipe service unavailable",
            "content": {"application/json": {"example": {"detail": "Recipe service is currently unavailable"}}},
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
    query: str = Query(..., description="Search query string"),
    cuisine: str | None = Query(None, description="Cuisine type filter"),
    diet: str | None = Query(None, description="Dietary restriction filter"),
    exclude: list[str] | None = Query(None, description="Ingredients to exclude"),
    max_time: int | None = Query(None, description="Maximum total time in minutes"),
    service: str | None = Query(None, description="Specific recipe service to use"),
    db: AsyncSession = Depends(get_async_db),
) -> RecipeList:
    """Search for recipes across multiple services.

    This endpoint searches for recipes using the specified criteria across multiple
    recipe services (Spoonacular, Edamam, etc.) and returns a unified list of results.
    """
    try:
        search_service = RecipeSearchService(db)
        return await search_service.search(
            query=query,
            cuisine=cuisine,
            diet=diet,
            exclude=exclude,
            max_time=max_time,
            service=service,
        )
    except APIError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e),
        ) from e
    except DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        ) from e


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
async def get_recipe(recipe_id: str, db: AsyncSession = Depends(get_async_db)) -> RecipeSearchResult:
    """Get detailed information for a specific recipe.

    Args:
        recipe_id: ID of the recipe to retrieve
        db: Database session

    Returns:
        Detailed recipe information

    Raises:
        HTTPException: If recipe not found or other error occurs
    """
    try:
        search_service = RecipeSearchService(db)
        results = await search_service.search(query=f"id:{recipe_id}", limit=1)
        if not results.total:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Recipe with ID {recipe_id} not found",
            )
        return results.results[0]
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid recipe ID format",
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve recipe: {e}",
        ) from e
