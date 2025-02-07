"""Recipe provider factory."""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.core.config import settings
from app.core.constants import ErrorMessages
from app.core.exceptions import ConfigurationError
from app.services.recipe_providers.api_ninjas import APINinjasProvider
from app.services.recipe_providers.edamam import EdamamProvider
from app.services.recipe_providers.mealdb import TheMealDBProvider
from app.services.recipe_providers.recipe_puppy import RecipePuppyProvider
from app.services.recipe_providers.spoonacular import SpoonacularProvider
from app.services.recipe_providers.tasty import TastyProvider

if TYPE_CHECKING:
    from collections.abc import Mapping

    from app.services.recipe_providers.base import RecipeProvider


class RecipeProviderFactory:
    """Factory for creating recipe providers."""

    PROVIDERS: Mapping[str, type[RecipeProvider]] = {
        "spoonacular": SpoonacularProvider,
        "tasty": TastyProvider,
        "edamam": EdamamProvider,
        "mealdb": TheMealDBProvider,
        "recipe_puppy": RecipePuppyProvider,
        "api_ninjas": APINinjasProvider,
    }

    def __init__(self) -> None:
        """Initialize the factory."""
        self._providers: dict[str, RecipeProvider] = {}

    def get_provider(self, provider_name: str) -> RecipeProvider:
        """Get a recipe provider by name.

        Args:
            provider_name: Name of the provider to get

        Returns:
            Recipe provider instance

        Raises:
            ConfigurationError: If provider initialization fails
        """
        if provider_name not in self._providers:
            if provider_name not in self.PROVIDERS:
                raise ConfigurationError(
                    ErrorMessages.CONFIG_INVALID_VALUE.format(
                        key="provider_name", details=f"Unknown provider: {provider_name}"
                    )
                )

            try:
                provider_class = self.PROVIDERS[provider_name]
                self._providers[provider_name] = provider_class()
            except Exception as e:
                raise ConfigurationError(
                    ErrorMessages.RECIPE_PROVIDER_INIT_FAILED.format(provider=provider_name, details=str(e))
                ) from e

        return self._providers[provider_name]

    def get_all_providers(self) -> list[RecipeProvider]:
        """Get all configured recipe providers.

        Returns:
            List of recipe provider instances
        """
        if not settings.ENABLE_EXTERNAL_PROVIDERS:
            return []

        providers: list[RecipeProvider] = []
        for provider_name in self.PROVIDERS:
            try:
                providers.append(self.get_provider(provider_name))
            except ConfigurationError:
                continue  # Skip providers that fail to initialize

        return providers
