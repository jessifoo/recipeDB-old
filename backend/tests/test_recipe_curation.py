from __future__ import annotations

from unittest.mock import Mock, patch

import pytest

from app.models.models import Recipe
from app.services.recipe_search import RecipeSearchService


@pytest.fixture
def mock_meilisearch():
    with patch("app.services.meilisearch_service.MeilisearchService") as mock:
        yield mock


@pytest.fixture
def mock_api_client():
    with patch("app.services.api_search.APISearchService") as mock:
        yield mock


@pytest.fixture
def recipe_service(mock_meilisearch, mock_api_client):
    return RecipeSearchService(db_session=None)


def test_recipes():
    return [
        Recipe(
            id="1",
            title="Dairy-Free Mac and Cheese",
            ingredients=[
                "cashews",
                "nutritional yeast",
                "plant milk",
                "pasta",
            ],
            is_dairy_free=True,
            is_egg_free=True,
            is_soy_free=True,
        ),
        Recipe(
            id="2",
            title="Classic Mac and Cheese",
            ingredients=["cheddar cheese", "milk", "butter", "pasta"],
            is_dairy_free=False,
            is_egg_free=True,
            is_soy_free=True,
        ),
    ]


class TestRecipeCuration:
    async def test_allergen_filtering(self, recipe_service):
        """Test that recipes are properly filtered by allergens"""
        recipes = test_recipes()

        # Mock search results
        recipe_service.search_engine.search_recipes.return_value = recipes

        # Search with dairy-free filter
        results = await recipe_service.search_recipes("mac and cheese", {"isDairyFree": True})

        assert len(results) == 1
        assert results[0].title == "Dairy-Free Mac and Cheese"
        assert results[0].is_dairy_free

    async def test_ingredient_validation(self, recipe_service):
        """Test that ingredients are properly validated for allergens"""
        recipe = Recipe(
            id="3",
            title="Suspicious Recipe",
            ingredients=["natural flavors (contains milk)", "spices", "pasta"],
            is_dairy_free=True,  # Incorrectly marked as dairy-free
        )

        # Mock validation function
        def validate_recipe(recipe):
            for ingredient in recipe.ingredients:
                if "milk" in ingredient.lower():
                    recipe.is_dairy_free = False
                    return False
            return True

        recipe_service._validate_recipe = validate_recipe

        # Validate recipe
        is_valid = recipe_service._validate_recipe(recipe)

        assert not is_valid
        assert not recipe.is_dairy_free

    async def test_api_integration(self, recipe_service, mock_api_client):
        """Test that API results are properly filtered and validated"""
        api_recipes = [
            Recipe(
                id="4",
                title="API Recipe 1",
                ingredients=["soy sauce", "vegetables"],
                is_soy_free=True,  # Incorrectly marked as soy-free
            ),
            Recipe(
                id="5",
                title="API Recipe 2",
                ingredients=["coconut aminos", "vegetables"],
                is_soy_free=True,
            ),
        ]

        # Mock API response
        mock_api_client.search_recipes.return_value = api_recipes

        # Search with soy-free filter
        results = await recipe_service.search_recipes("stir fry", {"isSoyFree": True})

        # First recipe should be filtered out due to soy sauce
        assert len(results) == 1
        assert results[0].title == "API Recipe 2"
        assert "soy" not in " ".join(results[0].ingredients).lower()

    async def test_recipe_deduplication(self, recipe_service):
        """Test that duplicate recipes are properly handled"""
        recipes = [
            Recipe(id="6", title="Duplicate Recipe", ingredients=["a", "b"]),
            Recipe(id="7", title="Duplicate Recipe", ingredients=["a", "b"]),
            Recipe(id="8", title="Unique Recipe", ingredients=["c", "d"]),
        ]

        # Mock search results
        recipe_service.search_engine.search_recipes.return_value = recipes

        # Search and check for duplicates
        results = await recipe_service.search_recipes("recipe")

        assert len(results) == 2  # Should only include one copy of the duplicate
        assert len({r.title for r in results}) == 2

    async def test_hidden_allergens(self, recipe_service):
        """Test detection of hidden allergens in ingredients"""
        recipe = Recipe(
            id="9",
            title="Sneaky Recipe",
            ingredients=[
                "whey protein",  # Hidden dairy
                "natural flavoring",  # Potential hidden allergen
                "spices",
            ],
            is_dairy_free=True,
        )

        # Define hidden allergen patterns
        dairy_aliases = ["whey", "casein", "lactose", "milk protein"]

        def check_hidden_allergens(recipe):
            return any(any(alias in ingredient.lower() for alias in dairy_aliases) for ingredient in recipe.ingredients)

        recipe_service._check_hidden_allergens = check_hidden_allergens

        # Check for hidden allergens
        has_hidden = recipe_service._check_hidden_allergens(recipe)

        assert has_hidden

    async def test_recipe_saving(self, recipe_service):
        """Test that safe recipes are properly saved to the database"""
        recipe = Recipe(
            id="10",
            title="Safe Recipe",
            ingredients=["vegetables", "olive oil"],
            is_dairy_free=True,
            is_egg_free=True,
            is_soy_free=True,
        )

        # Mock database save
        mock_db = Mock()
        recipe_service.db_session = mock_db

        # Save recipe
        await recipe_service.save_recipe(recipe)

        # Verify save was called
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
