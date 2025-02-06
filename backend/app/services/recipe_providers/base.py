"""Base recipe provider class."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, ClassVar

if TYPE_CHECKING:
    from app.schemas.recipe import RecipeList, RecipeSearchResult


class RecipeProvider(ABC):
    """Base class for recipe providers."""

    # Default allergens to exclude
    DEFAULT_ALLERGENS: ClassVar[list[str]] = ["dairy", "soy", "egg"]

    # Common allergen keywords to check
    ALLERGEN_KEYWORDS: ClassVar[dict[str, list[str]]] = {
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
        ],
    }

    def __init__(self, api_key: str | None = None):
        """Initialize the recipe provider.

        Args:
            api_key: Optional API key for authentication
        """
        self.api_key = api_key
        self.source_name = self.__class__.__name__.replace("Provider", "").lower()

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
        """
        pass

    @abstractmethod
    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get detailed recipe information by ID.

        Args:
            recipe_id: Recipe ID from the provider

        Returns:
            RecipeSearchResult: Detailed recipe information
        """
        pass

    def _normalize_recipe(self, raw_recipe: dict[str, Any]) -> RecipeSearchResult:
        """Convert provider-specific recipe data to standard format.

        This method should be overridden by each provider to handle their specific data format.

        Args:
            raw_recipe: Raw recipe data from the provider

        Returns:
            RecipeSearchResult: Normalized recipe data
        """
        raise NotImplementedError("Each provider must implement recipe normalization")

    def _contains_allergen(self, text: str, allergen: str) -> bool:
        """Check if text contains any keywords for a specific allergen.

        Args:
            text: Text to check (ingredient list, title, etc.)
            allergen: Allergen type to check for

        Returns:
            bool: True if allergen keywords are found
        """
        if allergen not in self.ALLERGEN_KEYWORDS:
            return False

        text = text.lower()
        return any(keyword in text for keyword in self.ALLERGEN_KEYWORDS[allergen])

    def _filter_allergens(self, recipe: RecipeSearchResult) -> bool:
        """Check if recipe is safe according to default allergen profile.

        Args:
            recipe: Recipe to check

        Returns:
            bool: True if recipe is safe (contains no default allergens)
        """
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
            ),
        ).lower()

        # Check for each default allergen
        return all(not self._contains_allergen(text_to_check, allergen) for allergen in self.DEFAULT_ALLERGENS)

    def _apply_allergen_filtering(self, results: list[RecipeSearchResult]) -> list[RecipeSearchResult]:
        """Filter out recipes that contain default allergens.

        Args:
            results: List of recipes to filter

        Returns:
            List[RecipeSearchResult]: Filtered list of recipes
        """
        return [recipe for recipe in results if self._filter_allergens(recipe)]
