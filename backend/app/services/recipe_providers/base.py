"""Base recipe provider class.

This module provides the base class for all recipe providers, implementing
common functionality like allergen filtering and error handling.

Example:
    .. code-block:: python

        class SpoonacularProvider(RecipeProvider):
            async def search_recipes(self, query: str, **kwargs) -> RecipeList:
                # Provider-specific implementation
                results = await self._search_api(query, **kwargs)
                return self._apply_allergen_filtering(results)

Note:
    All recipe providers must implement the abstract methods and should use
    the provided allergen filtering utilities for consistency.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, ClassVar, Final

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, ValidationError

if TYPE_CHECKING:
    from app.schemas.recipe import RecipeList, RecipeSearchResult


# Type alias for provider-specific recipe data
ProviderRecipeData = dict[str, Any]


class RecipeProvider(ABC):
    """Base class for recipe providers.

    This class provides common functionality for recipe providers including:
    - Allergen filtering (dairy, soy, egg by default)
    - Error handling
    - Data normalization

    Attributes:
        DEFAULT_ALLERGENS: List of allergens to exclude by default
        ALLERGEN_KEYWORDS: Dictionary mapping allergens to their indicator keywords
        ALLERGEN_FILTERING_REQUIRED: Whether allergen filtering can be disabled
    """

    # Default allergens that must be excluded
    DEFAULT_ALLERGENS: ClassVar[list[str]] = ["dairy", "soy", "egg"]

    # Whether allergen filtering can be disabled
    ALLERGEN_FILTERING_REQUIRED: ClassVar[bool] = True

    # Common allergen keywords to check
    ALLERGEN_KEYWORDS: Final[dict[str, list[str]]] = {
        "dairy": [
            "milk",
            "cheese",
            "cream",
            "butter",
            "yogurt",
            "whey",
            "casein",
            "lactose",
            "dairy",
            "ghee",
            "buttermilk",
            "cottage cheese",
            "sour cream",
            "half and half",
            "creamy",
            "milky",
            "parmesan",
            "mozzarella",
            "ricotta",
            "cheddar",
        ],
        "soy": [
            "soy",
            "soya",
            "edamame",
            "tofu",
            "tempeh",
            "miso",
            "natto",
            "tamari",
            "shoyu",
            "soy sauce",
            "soy lecithin",
            "soybean",
            "textured vegetable protein",
            "tvp",
            "soy protein",
        ],
        "egg": [
            "egg",
            "eggs",
            "mayonnaise",
            "mayo",
            "meringue",
            "albumen",
            "albumin",
            "lysozyme",
            "ovalbumin",
            "surimi",
            "lecithin",
            "eggnog",
            "custard",
            "hollandaise",
            "aioli",
        ],
    }

    # Cooking method keywords
    COOKING_METHOD_KEYWORDS: Final[dict[str, list[str]]] = {
        "instant_pot": ["instant pot", "pressure cook", "pressure cooker", "instant-pot", "instantpot"],
        "slow_cooker": ["slow cook", "slow cooker", "crockpot", "crock pot", "crock-pot", "slow-cooker"],
        "air_fryer": ["air fry", "air fryer", "air-fry", "air-fryer"],
        "grill": ["grill", "grilled", "grilling", "barbecue", "bbq", "charcoal", "broil"],
        "bake": ["bake", "baked", "baking", "roast", "roasted", "roasting", "oven"],
        "stovetop": ["stovetop", "stove top", "stove-top", "pan fry", "sauté", "saute", "simmer", "boil"],
    }

    def __init__(self, api_key: str | None = None, disable_allergen_filter: bool = False) -> None:
        """Initialize the recipe provider.

        Args:
            api_key: Optional API key for authentication
            disable_allergen_filter: Whether to disable allergen filtering
                (only if ALLERGEN_FILTERING_REQUIRED is False)

        Raises:
            ValidationError: If trying to disable required allergen filtering
        """
        self.api_key = api_key
        self.source_name = self.__class__.__name__.replace("Provider", "").lower()

        if disable_allergen_filter and self.ALLERGEN_FILTERING_REQUIRED:
            raise ValidationError(
                message_template=ErrorMessages.INVALID_OPERATION,
                code=ErrorCode.INVALID_OPERATION,
                details={
                    "error": "Allergen filtering cannot be disabled for this provider",
                    "provider": self.source_name,
                },
            )
        self.allergen_filter_enabled = not disable_allergen_filter

    @abstractmethod
    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search for recipes using the provider's API.

        Args:
            query: Search query string
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude: List of ingredients to exclude
            max_time: Maximum cooking time in minutes

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            DomainError: If the API request fails
            ValidationError: If the search parameters are invalid
            BusinessError: If no recipes match the filters
        """

    @abstractmethod
    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Args:
            recipe_id: Recipe ID from the provider

        Returns:
            RecipeSearchResult: Detailed recipe information

        Raises:
            DomainError: If the API request fails
            ValidationError: If the recipe ID is invalid
            BusinessError: If the recipe contains allergens
        """

    def _normalize_recipe(self, raw_recipe: ProviderRecipeData) -> RecipeSearchResult:
        """Convert provider-specific recipe data to standard format.

        This method should be overridden by each provider to handle their specific data format.

        Args:
            raw_recipe: Raw recipe data from the provider

        Returns:
            RecipeSearchResult: Normalized recipe data

        Raises:
            NotImplementedError: If the provider hasn't implemented normalization
        """
        msg = f"Provider {self.source_name} must implement recipe normalization"
        raise NotImplementedError(msg)

    def _contains_allergen(self, text: str, allergen: str) -> bool:
        """Check if text contains any keywords for a specific allergen.

        Args:
            text: Text to check (ingredient list, title, etc.)
            allergen: Allergen type to check for

        Returns:
            bool: True if allergen keywords are found

        Raises:
            ValidationError: If checking an unknown allergen type
        """
        if allergen not in self.ALLERGEN_KEYWORDS:
            raise ValidationError(
                message_template=ErrorMessages.INVALID_FILTER_PARAMS,
                code=ErrorCode.VALIDATION_ERROR,
                details={
                    "error": "Unknown allergen type",
                    "allergen": allergen,
                    "valid_allergens": list(self.ALLERGEN_KEYWORDS.keys()),
                },
            )

        text = text.lower()
        return any(keyword in text for keyword in self.ALLERGEN_KEYWORDS[allergen])

    def _detect_cooking_method(self, text: str) -> str | None:
        """Detect cooking method from recipe text.

        Args:
            text: Text to analyze (title, instructions, etc.)

        Returns:
            str | None: Detected cooking method or None if not found
        """
        text = text.lower()
        for method, keywords in self.COOKING_METHOD_KEYWORDS.items():
            if any(keyword in text for keyword in keywords):
                return method
        return None

    def _filter_allergens(self, recipe: RecipeSearchResult) -> bool:
        """Check if recipe is safe according to default allergen profile.

        Args:
            recipe: Recipe to check

        Returns:
            bool: True if recipe is safe (contains no default allergens)
        """
        if not self.allergen_filter_enabled:
            return True

        # Combine all text fields that might mention allergens
        text_to_check = " ".join(
            filter(
                None,
                [
                    recipe.title,
                    recipe.description or "",
                    " ".join(recipe.ingredients or []),
                    " ".join(recipe.instructions or []),
                ],
            )
        ).lower()

        # Check for each default allergen
        return all(not self._contains_allergen(text_to_check, allergen) for allergen in self.DEFAULT_ALLERGENS)

    def _apply_allergen_filtering(
        self, results: list[RecipeSearchResult], raise_on_empty: bool = False
    ) -> list[RecipeSearchResult]:
        """Filter out recipes that contain default allergens.

        Args:
            results: List of recipes to filter
            raise_on_empty: Whether to raise an error if no recipes pass filtering

        Returns:
            List[RecipeSearchResult]: Filtered list of recipes

        Raises:
            BusinessError: If raise_on_empty is True and no recipes pass filtering
        """
        if not self.allergen_filter_enabled:
            return results

        filtered = [recipe for recipe in results if self._filter_allergens(recipe)]

        if not filtered and raise_on_empty:
            raise BusinessError(
                message_template=ErrorMessages.RECIPE_CONTAINS_ALLERGENS,
                code=ErrorCode.ALLERGEN_CONFLICT,
                details={"allergens": self.DEFAULT_ALLERGENS, "total_recipes": len(results)},
            )

        return filtered
