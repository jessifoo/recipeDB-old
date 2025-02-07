"""Unit tests for recipe search service."""

from __future__ import annotations

from unittest.mock import AsyncMock

import pytest

from app.core.exceptions import ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.exceptions import APIError
from app.services.recipe_search import RecipeSearchService


@pytest.fixture
def mock_db_session():
    """Create a mock database session."""
    session = AsyncMock()
    session.begin = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.close = AsyncMock()
    return session


@pytest.fixture
def mock_recipe_provider():
    """Create a mock recipe provider."""
    provider = AsyncMock()
    provider.search_recipes = AsyncMock()
    provider.get_recipe_by_id = AsyncMock()
    return provider


@pytest.fixture
def recipe_search_service(mock_db_session, mock_recipe_provider):
    """Create a recipe search service instance with mocks."""
    service = RecipeSearchService(mock_db_session)
    service.provider = mock_recipe_provider
    return service


@pytest.fixture
def sample_recipe_result():
    """Create a sample recipe search result."""
    return RecipeSearchResult(
        id="test_1",
        title="Test Recipe",
        description="A test recipe",
        image_url="https://example.com/image.jpg",
        source_url="https://example.com/recipe",
        prep_time=15,
        cook_time=30,
        total_time=45,
        servings=4,
        cuisine="Italian",
        diet=["vegetarian"],
        ingredients=["ingredient 1", "ingredient 2"],
        instructions=["step 1", "step 2"],
        source="test_provider",
    )


@pytest.mark.asyncio
class TestRecipeSearchService:
    """Test suite for RecipeSearchService."""

    async def test_search_recipes(self, recipe_search_service, mock_recipe_provider, sample_recipe_result):
        """Test searching for recipes."""
        # Arrange
        query = "pasta"
        mock_recipe_provider.search_recipes.return_value = RecipeList(
            total=1,
            results=[sample_recipe_result],
            source="test_provider",
        )

        # Act
        results = await recipe_search_service.search(query)

        # Assert
        assert results.total == 1
        assert len(results.results) == 1
        assert results.results[0].title == sample_recipe_result.title
        mock_recipe_provider.search_recipes.assert_called_once_with(
            query=query,
            offset=None,
            limit=None,
            cuisine=None,
            diet=None,
            exclude=None,
            max_time=None,
        )

    async def test_search_recipes_with_filters(self, recipe_search_service, mock_recipe_provider):
        """Test searching for recipes with filters."""
        # Arrange
        query = "pasta"
        filters = {"cuisine": "Italian", "diet": "vegetarian", "max_time": 30}

        # Act
        await recipe_search_service.search(query, filters=filters)

        # Assert
        mock_recipe_provider.search_recipes.assert_called_once_with(
            query=query,
            offset=None,
            limit=None,
            cuisine="Italian",
            diet="vegetarian",
            exclude=None,
            max_time=30,
        )

    async def test_get_recipe_by_id(self, recipe_search_service, mock_recipe_provider, sample_recipe_result):
        """Test retrieving a recipe by ID."""
        # Arrange
        recipe_id = "test_1"
        mock_recipe_provider.get_recipe_by_id.return_value = sample_recipe_result

        # Act
        result = await recipe_search_service.get_recipe_by_id(recipe_id)

        # Assert
        assert result.id == recipe_id
        assert result.title == sample_recipe_result.title
        mock_recipe_provider.get_recipe_by_id.assert_called_once_with(recipe_id)

    async def test_search_recipes_api_error(self, recipe_search_service, mock_recipe_provider):
        """Test handling API errors during search."""
        # Arrange
        mock_recipe_provider.search_recipes.side_effect = APIError("API error")

        # Act & Assert
        with pytest.raises(APIError):
            await recipe_search_service.search("pasta")

    async def test_search_recipes_validation_error(self, recipe_search_service):
        """Test validation of search parameters."""
        # Act & Assert
        with pytest.raises(ValidationError):
            await recipe_search_service.search("")  # Empty query

    async def test_get_recipe_not_found(self, recipe_search_service, mock_recipe_provider):
        """Test handling non-existent recipe ID."""
        # Arrange
        recipe_id = "nonexistent"
        mock_recipe_provider.get_recipe_by_id.return_value = None

        # Act & Assert
        with pytest.raises(ValidationError):
            await recipe_search_service.get_recipe_by_id(recipe_id)
