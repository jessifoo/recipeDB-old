"""Unit tests for recipe service."""

from __future__ import annotations

from unittest.mock import AsyncMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ValidationError
from app.models.models import Recipe, RecipeInstruction
from app.schemas.recipe import RecipeCreate, RecipeUpdate
from app.services.recipe_service import RecipeService


@pytest.fixture
def mock_db_session():
    """Create a mock database session."""
    session = AsyncMock(spec=AsyncSession)
    session.begin = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.close = AsyncMock()
    return session


@pytest.fixture
def recipe_service(mock_db_session):
    """Create a recipe service instance with a mock session."""
    return RecipeService(mock_db_session)


@pytest.fixture
def sample_recipe_data():
    """Create sample recipe data for testing."""
    return {
        "title": "Test Recipe",
        "description": "A test recipe",
        "prep_time_minutes": 15,
        "cook_time_minutes": 30,
        "servings": 4,
        "instructions": [
            {"step_number": 1, "instruction": "Step 1"},
            {"step_number": 2, "instruction": "Step 2"},
        ],
    }


@pytest.mark.asyncio
class TestRecipeService:
    """Test suite for RecipeService."""

    async def test_create_recipe(self, recipe_service, sample_recipe_data, mock_db_session):
        """Test creating a new recipe."""
        # Arrange
        recipe_create = RecipeCreate(**sample_recipe_data)
        mock_db_session.add = AsyncMock()
        mock_db_session.flush = AsyncMock()

        # Act
        created_recipe = await recipe_service.create_recipe(recipe_create)

        # Assert
        assert created_recipe.title == sample_recipe_data["title"]
        assert created_recipe.prep_time_minutes == sample_recipe_data["prep_time_minutes"]
        assert len(created_recipe.instructions) == len(sample_recipe_data["instructions"])
        mock_db_session.add.assert_called_once()
        mock_db_session.commit.assert_called_once()

    async def test_get_recipe(self, recipe_service, mock_db_session):
        """Test retrieving a recipe by ID."""
        # Arrange
        recipe_id = 1
        mock_recipe = Recipe(recipe_id=recipe_id, title="Test Recipe")
        mock_db_session.get = AsyncMock(return_value=mock_recipe)

        # Act
        result = await recipe_service.get_recipe(recipe_id)

        # Assert
        assert result == mock_recipe
        mock_db_session.get.assert_called_once_with(Recipe, recipe_id)

    async def test_get_recipe_not_found(self, recipe_service, mock_db_session):
        """Test retrieving a non-existent recipe."""
        # Arrange
        recipe_id = 999
        mock_db_session.get = AsyncMock(return_value=None)

        # Act & Assert
        with pytest.raises(ValidationError):
            await recipe_service.get_recipe(recipe_id)

    async def test_update_recipe(self, recipe_service, mock_db_session):
        """Test updating a recipe."""
        # Arrange
        recipe_id = 1
        existing_recipe = Recipe(
            recipe_id=recipe_id,
            title="Old Title",
            instructions=[RecipeInstruction(step_number=1, instruction="Old Step")],
        )
        update_data = RecipeUpdate(title="New Title", instructions=[{"step_number": 1, "instruction": "New Step"}])
        mock_db_session.get = AsyncMock(return_value=existing_recipe)

        # Act
        updated_recipe = await recipe_service.update_recipe(recipe_id, update_data)

        # Assert
        assert updated_recipe.title == "New Title"
        assert updated_recipe.instructions[0].instruction == "New Step"
        mock_db_session.commit.assert_called_once()

    async def test_delete_recipe(self, recipe_service, mock_db_session):
        """Test deleting a recipe."""
        # Arrange
        recipe_id = 1
        mock_recipe = Recipe(recipe_id=recipe_id, title="Test Recipe")
        mock_db_session.get = AsyncMock(return_value=mock_recipe)

        # Act
        await recipe_service.delete_recipe(recipe_id)

        # Assert
        mock_db_session.delete.assert_called_once_with(mock_recipe)
        mock_db_session.commit.assert_called_once()

    async def test_list_recipes(self, recipe_service, mock_db_session):
        """Test listing recipes with pagination."""
        # Arrange
        mock_recipes = [Recipe(recipe_id=1, title="Recipe 1"), Recipe(recipe_id=2, title="Recipe 2")]
        mock_db_session.execute = AsyncMock()
        mock_db_session.execute.return_value.scalars.return_value.all.return_value = mock_recipes

        # Act
        recipes = await recipe_service.list_recipes(skip=0, limit=10)

        # Assert
        assert len(recipes) == 2
        assert recipes[0].title == "Recipe 1"
        assert recipes[1].title == "Recipe 2"
