"""Recipe provider factory."""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.core.config import settings
from app.core.exceptions import ConfigurationError

from .api_ninjas import APINinjasProvider
from .edamam import EdamamProvider
from .mock import MockRecipeProvider
from .recipe_puppy import RecipePuppyProvider
from .spoonacular import SpoonacularProvider
from .tasty import TastyProvider
from .themealdb import MealDBProvider

if TYPE_CHECKING:
    from .base import RecipeProvider


class RecipeProviderFactory:
    """Factory for creating recipe providers."""

    _providers: dict[str, type[RecipeProvider]] = {
        "spoonacular": SpoonacularProvider,
        "edamam": EdamamProvider,
        "api_ninjas": APINinjasProvider,
        "tasty": TastyProvider,
        "mealdb": MealDBProvider,
        "recipe_puppy": RecipePuppyProvider,
        "mock": MockRecipeProvider,
        "local": MockRecipeProvider,  # Use mock provider as local for testing
    }

    @classmethod
    def get_provider(cls, provider_name: str = "local") -> RecipeProvider:
        """Get a recipe provider instance.

        Args:
            provider_name: Name of the provider to get

        Returns:
            RecipeProvider: Instance of the requested provider

        Raises:
            ConfigurationError: If the provider is not found or not configured
        """
        # Don't initialize external providers unless enabled
        if provider_name not in ("local", "mock") and not settings.ENABLE_EXTERNAL_PROVIDERS:
            raise ConfigurationError("External recipe providers are disabled")

        provider_class = cls._providers.get(provider_name)
        if not provider_class:
            raise ConfigurationError(f"Unknown recipe provider: {provider_name}")

        try:
            return provider_class()
        except Exception as e:
            raise ConfigurationError(f"Failed to initialize {provider_name} provider: {e!s}")

    @classmethod
    def get_all_providers(cls) -> list[RecipeProvider]:
        """Get instances of all configured providers.

        Returns:
            List[RecipeProvider]: List of provider instances
        """
        providers = []
        for provider_name in cls._providers:
            try:
                provider = cls.get_provider(provider_name)
                providers.append(provider)
            except ConfigurationError:
                # Skip providers that aren't properly configured
                continue
        return providers
