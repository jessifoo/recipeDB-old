"""Recipe service layer."""

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

from fastapi import HTTPException

from app.schemas.recipe import RecipeList
from app.services.exceptions import (
    ExternalAPIError,
    RecipeFilterError,
    RecipeNotFoundError,
    RecipeProviderError,
    RecipeServiceError,
)
from app.services.recipe_providers.factory import RecipeProviderFactory

if TYPE_CHECKING:
    from app.schemas.recipe import RecipeSearchResult


class RecipeService:
    """Service layer for recipe operations."""

    def __init__(self) -> None:
        """Initialize the recipe service."""
        self.provider_factory = RecipeProviderFactory()

    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
        provider: str | None = None,
    ) -> RecipeList:
        """Search for recipes across all providers or a specific provider."""
        try:
            if provider:
                recipe_provider = self.provider_factory.get_provider(provider)
                return await recipe_provider.search_recipes(
                    query=query,
                    offset=offset,
                    limit=limit,
                    cuisine=cuisine,
                    diet=diet,
                    exclude=exclude,
                    max_time=max_time,
                )

            # If no specific provider, aggregate results from all providers
            results = []
            total = 0
            for provider_instance in self.provider_factory.get_all_providers():
                try:
                    provider_results = await provider_instance.search_recipes(
                        query=query,
                        offset=offset,
                        limit=limit,
                        cuisine=cuisine,
                        diet=diet,
                        exclude=exclude,
                        max_time=max_time,
                    )
                    results.extend(provider_results.results)
                    total += provider_results.total
                except RecipeServiceError:
                    # Log error but continue with other providers
                    continue

            return RecipeList(
                total=total,
                results=results[:limit],
                source="aggregated",
            )

        except ExternalAPIError as e:
            raise HTTPException(
                status_code=e.status_code or HTTPStatus.BAD_GATEWAY,
                detail=str(e),
            ) from e
        except RecipeProviderError as e:
            raise HTTPException(
                status_code=HTTPStatus.BAD_GATEWAY,
                detail=str(e),
            ) from e
        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=f"Recipe search failed: {e!s}",
            ) from e

    async def get_recipe_by_id(self, recipe_id: str, provider: str) -> RecipeSearchResult:
        """Get a recipe by ID from a specific provider."""
        try:
            recipe_provider = self.provider_factory.get_provider(provider)
            return await recipe_provider.get_recipe_by_id(recipe_id)

        except ExternalAPIError as e:
            raise HTTPException(
                status_code=e.status_code or HTTPStatus.BAD_GATEWAY,
                detail=str(e),
            ) from e
        except RecipeFilterError as e:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=str(e),
            ) from e
        except RecipeNotFoundError as e:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=str(e),
            ) from e
        except RecipeProviderError as e:
            raise HTTPException(
                status_code=HTTPStatus.BAD_GATEWAY,
                detail=str(e),
            ) from e
        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=f"Failed to get recipe: {e!s}",
            ) from e
