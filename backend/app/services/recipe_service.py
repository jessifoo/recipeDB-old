"""Recipe service layer."""

from __future__ import annotations

from app.core.config import settings
from app.core.error_messages import RECIPE_FETCH_FAILED, RECIPE_SEARCH_FAILED
from app.core.exceptions import ExternalServiceError, NotFoundError, RecipeFilterError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.factory import RecipeProviderFactory


class RecipeService:
    """Service layer for recipe operations."""

    ENABLED_PROVIDERS = ["edamam", "spoonacular", "mealdb"]  # Default providers

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
            recipe_provider = self.provider_factory.get_provider(provider) if provider else None
            if recipe_provider:
                return await recipe_provider.search_recipes(
                    query=query,
                    offset=offset,
                    limit=limit,
                    cuisine=cuisine,
                    diet=diet,
                    exclude=exclude,
                    max_time=max_time,
                )

            # If no specific provider, search across all providers
            results: list[RecipeSearchResult] = []
            total = 0
            enabled_providers = self.ENABLED_PROVIDERS if settings.ENABLE_EXTERNAL_PROVIDERS else ["local"]

            for provider_name in enabled_providers:
                try:
                    provider_instance = self.provider_factory.get_provider(provider_name)
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
                except Exception:
                    # Log error but continue with other providers
                    continue

            # Sort and paginate combined results
            start = offset
            end = offset + limit
            paginated_results = results[start:end]

            return RecipeList(total=total, results=paginated_results, source="all")

        except ExternalServiceError:
            raise
        except Exception as e:
            raise ExternalServiceError(message=RECIPE_SEARCH_FAILED.format(details=str(e)))

    async def get_recipe_by_id(self, recipe_id: str, provider: str) -> RecipeSearchResult:
        """Get a recipe by ID from a specific provider."""
        try:
            recipe_provider = self.provider_factory.get_provider(provider)
            return await recipe_provider.get_recipe_by_id(recipe_id)

        except (ExternalServiceError, NotFoundError, RecipeFilterError):
            raise
        except Exception as e:
            raise ExternalServiceError(message=RECIPE_FETCH_FAILED.format(details=str(e)))
