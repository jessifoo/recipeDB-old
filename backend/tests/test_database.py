"""Test module for database operations.

This module contains comprehensive test cases for all database operations,
including CRUD operations, search functionality, and error handling.
"""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock

import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import DatabaseError, RecipeDatabase
from app.models.models import Recipe


# Test Data
@pytest.fixture
def sample_recipe_data() -> dict[str, Any]:
    return {
        "id": 1,
        "title": "Test Recipe",
        "meal_type": "dinner",
        "ingredients": ["ingredient1", "ingredient2"],
        "instructions": ["step1", "step2"],
        "prep_time": 30,
        "cook_time": 45,
        "total_time": 75,
        "cooking_method": "bake",
        "protein_type": "chicken",
        "allergens": [],
        "calories": 500,
        "protein": 25,
        "carbs": 45,
        "fat": 20,
    }


@pytest.fixture
def sample_recipes_data() -> list[dict[str, Any]]:
    return [
        {
            "id": i,
            "title": f"Recipe {i}",
            "meal_type": "dinner",
            "ingredients": [f"ingredient{j}" for j in range(1, 4)],
            "instructions": [f"step{j}" for j in range(1, 4)],
            "prep_time": 30,
            "cook_time": 45,
            "total_time": 75,
            "cooking_method": "bake",
            "protein_type": "chicken",
            "allergens": [],
            "calories": 500,
            "protein": 25,
            "carbs": 45,
            "fat": 20,
        }
        for i in range(1, 6)
    ]


@pytest.fixture
def mock_session() -> AsyncSession:
    """Create a mock database session."""
    session = AsyncMock(spec=AsyncSession)
    session.begin = AsyncMock(return_value=AsyncMock(__aenter__=AsyncMock(), __aexit__=AsyncMock()))
    session.commit = AsyncMock()
    session.refresh = AsyncMock()
    session.execute = AsyncMock()
    session.rollback = AsyncMock()
    return session


@pytest.fixture
def recipe_db(mock_session: AsyncSession) -> RecipeDatabase:
    """Create a RecipeDatabase instance with a mock session."""
    return RecipeDatabase(mock_session)


# Basic CRUD Operation Tests
async def test_get_recipe_by_id(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
    sample_recipe_data: dict[str, Any],
) -> None:
    """Test retrieving a recipe by ID."""
    mock_session.execute.return_value.scalar_one_or_none.return_value = Recipe(**sample_recipe_data)
    recipe = await recipe_db.get_recipe_by_id(1)
    assert recipe is not None
    assert recipe.id == 1
    assert recipe.title == "Test Recipe"


async def test_get_recipe_by_id_not_found(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
) -> None:
    """Test retrieving a non-existent recipe."""
    mock_session.execute.return_value.scalar_one_or_none.return_value = None
    recipe = await recipe_db.get_recipe_by_id(999)
    assert recipe is None


async def test_get_recipes_by_ids(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
    sample_recipes_data: list[dict[str, Any]],
) -> None:
    """Test retrieving multiple recipes by IDs."""
    mock_session.execute.return_value.scalars.return_value.all.return_value = [
        Recipe(**data) for data in sample_recipes_data
    ]
    recipes = await recipe_db.get_recipes_by_ids([1, 2, 3, 4, 5])
    assert len(recipes) == 5
    assert all(isinstance(recipe, Recipe) for recipe in recipes)


async def test_save_recipe(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
    sample_recipe_data: dict[str, Any],
) -> None:
    """Test saving a new recipe."""
    mock_session.execute.return_value.scalar_one.return_value = Recipe(**sample_recipe_data)
    recipe = await recipe_db.save_recipe(sample_recipe_data)
    assert recipe is not None
    assert recipe.title == "Test Recipe"
    mock_session.commit.assert_called_once()


async def test_update_recipe(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
    sample_recipe_data: dict[str, Any],
) -> None:
    """Test updating an existing recipe."""
    mock_session.execute.return_value.scalar_one_or_none.return_value = Recipe(**sample_recipe_data)
    updated_data = sample_recipe_data.copy()
    updated_data["title"] = "Updated Recipe"
    recipe = await recipe_db.update_recipe(1, updated_data)
    assert recipe is not None
    assert recipe.title == "Updated Recipe"
    mock_session.commit.assert_called_once()


# Search and Filter Tests
async def test_search_recipes(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
) -> None:
    """Test searching recipes."""
    mock_session.execute.return_value.scalars.return_value.all.return_value = [Recipe(id=1, title="Test Recipe")]
    recipes = await recipe_db.search_recipes(query="test")
    assert len(recipes) == 1
    assert recipes[0].title == "Test Recipe"


async def test_get_recipes_by_filters(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
) -> None:
    """Test filtering recipes."""
    mock_session.execute.return_value.scalars.return_value.all.return_value = [
        Recipe(id=1, title="Test Recipe", cooking_method="bake"),
    ]
    filters = {"cooking_method": "bake"}
    recipes = await recipe_db.get_recipes_by_filters(filters)
    assert len(recipes) == 1
    assert recipes[0].cooking_method == "bake"


# Error Handling Tests
async def test_database_error_handling(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
) -> None:
    """Test database error handling."""
    mock_session.execute.side_effect = SQLAlchemyError("Database error")
    with pytest.raises(DatabaseError):
        await recipe_db.get_recipe_by_id(1)


async def test_invalid_recipe_data(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
) -> None:
    """Test handling invalid recipe data."""
    invalid_data = {"invalid_field": "value"}
    with pytest.raises(Exception):
        await recipe_db.save_recipe(invalid_data)


# Edge Cases Tests
async def test_empty_search_results(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
) -> None:
    """Test handling empty search results."""
    mock_session.execute.return_value.scalars.return_value.all.return_value = []
    recipes = await recipe_db.search_recipes(query="nonexistent")
    assert len(recipes) == 0


async def test_search_with_special_characters(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
) -> None:
    """Test searching with special characters."""
    mock_session.execute.return_value.scalars.return_value.all.return_value = []
    recipes = await recipe_db.search_recipes(query="test!@#$%^&*()")
    assert len(recipes) == 0


async def test_filter_with_multiple_conditions(
    recipe_db: RecipeDatabase,
    mock_session: AsyncSession,
) -> None:
    """Test filtering with multiple conditions."""
    mock_session.execute.return_value.scalars.return_value.all.return_value = [
        Recipe(
            id=1,
            title="Test Recipe",
            cooking_method="bake",
            protein_type="chicken",
            prep_time=30,
        ),
    ]
    filters = {
        "cooking_method": "bake",
        "protein_type": "chicken",
        "prep_time": 30,
    }
    recipes = await recipe_db.get_recipes_by_filters(filters)
    assert len(recipes) == 1
    assert recipes[0].cooking_method == "bake"
    assert recipes[0].protein_type == "chicken"
    assert recipes[0].prep_time == 30
