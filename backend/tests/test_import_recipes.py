"""Unit tests for recipe import functionality."""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Recipe

# from app.services.recipe_manager import RecipeManager


@pytest.fixture
def mock_session():
    """Create a mock database session."""
    session = AsyncMock(spec=AsyncSession)
    session.begin = AsyncMock(return_value=AsyncMock(__aenter__=AsyncMock(), __aexit__=AsyncMock()))
    return session


# @pytest.fixture
# def recipe_manager(mock_session):
#     """Create a RecipeManager instance with a mock session."""
#     return RecipeManager(mock_session)


@pytest.fixture
def sample_recipe_data():
    """Create sample recipe data for testing."""
    return {
        "title": "Test Recipe",
        "source": "test",
        "source_url": "https://test.com/recipe",
        "servings": 4,
        "ready_in_minutes": 30,
        "ingredients": ["ingredient1", "ingredient2"],
        "instructions": ["step1", "step2"],
    }


def test_normalize_cooking_method():
    assert normalize_cooking_method("Bake in oven") == "bake"
    assert normalize_cooking_method("Simmer in pan") == "stovetop"
    assert normalize_cooking_method("Grill until done") == "grill"
    assert normalize_cooking_method("Slow cooker") == "slow_cooker"
    assert normalize_cooking_method("") is None
    assert normalize_cooking_method("unknown method") == "stovetop"


def test_detect_allergens():
    title = "Dairy-Free and Soy-Free Chicken (Gluten-Free, Nut-Free)"
    allergens = detect_allergens_from_title(title)

    assert allergens["is_dairy_free"] is True
    assert allergens["is_soy_free"] is True
    assert allergens["is_gluten_free"] is True
    assert allergens["is_nut_free"] is True
    assert allergens["is_egg_free"] is False


def test_import_recipes(app, sample_csv):
    with app.app_context():
        import_recipes(sample_csv)

        # Check recipes were imported
        recipes = Recipe.query.all()
        assert len(recipes) == 2

        # Check regular recipe
        dinner = Recipe.query.filter_by(meal_type="dinner").first()
        assert dinner is not None
        assert dinner.title == "Dairy-Free Chicken Curry"
        assert dinner.prep_time == 10
        assert dinner.cook_time == 30
        assert dinner.cooking_method == "stovetop"
        assert dinner.is_dairy_free is True
        assert dinner.image_url == "https://example.com/image.jpg"
        assert dinner.image_preview_url == "https://example.com/preview.jpg"

        # Check collection
        collection = Recipe.query.filter_by(meal_type="collection").first()
        assert collection is not None
        assert collection.is_collection is True
        assert collection.title == "Gluten-Free Collection"
        assert collection.is_gluten_free is True
