"""Recipe search router.

This module provides endpoints for searching and filtering recipes.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.schemas.recipe import RecipeResponse
from app.services.recipe_search import RecipeSearchService
from backend.app.api.deps import get_db

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.schemas.recipe import RecipeSearchFilters

router = APIRouter(
    prefix="/search",
    tags=["recipe-search"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal server error",
            "content": {"application/json": {"example": {"detail": "An error occurred during the search"}}},
        },
    },
)


@router.get(
    "/",
    response_model=list[RecipeResponse],
    responses={
        status.HTTP_200_OK: {
            "description": "Successfully retrieved search results",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "title": "Spaghetti Carbonara",
                            "description": "Classic Italian pasta dish",
                            "cooking_time": 30,
                            "servings": 4,
                            "difficulty": "medium",
                            "ingredients": ["pasta", "eggs", "pecorino", "guanciale"],
                            "instructions": ["Step 1...", "Step 2..."],
                            "tags": ["italian", "pasta", "quick"],
                        },
                    ],
                },
            },
        },
    },
)
async def search_recipes(
    query: str = Query(..., description="Search query string"),
    filters: RecipeSearchFilters | None = None,
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_db),
) -> list[RecipeResponse]:
    """Search for recipes with filters and pagination.

    Args:
        query: Search query string
        filters: Optional search filters
        page: Page number for pagination
        page_size: Number of items per page
        db: Database session

    Returns:
        List[RecipeResponse]: List of matching recipes

    Raises:
        HTTPException: If search fails or returns invalid results
    """
    try:
        search_service = RecipeSearchService(db)
        recipes = await search_service.search(
            query=query,
            filters=filters.dict() if filters else {},
            offset=(page - 1) * page_size,
            limit=page_size,
        )
        return [RecipeResponse.from_orm(recipe) for recipe in recipes]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to search recipes: {e!s}",
        )
