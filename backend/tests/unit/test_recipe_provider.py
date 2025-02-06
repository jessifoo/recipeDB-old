"""Unit tests for recipe providers."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest
from httpx import AsyncClient, Response

from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.exceptions import APIError
from app.services.recipe_providers.spoonacular import SpoonacularProvider


@pytest.fixture
def mock_http_client():
    """Create a mock HTTP client."""
    with patch("httpx.AsyncClient") as mock:
        client = AsyncMock(spec=AsyncClient)
        mock.return_value = client
        yield client


@pytest.fixture
def spoonacular_provider(mock_http_client):
    """Create a Spoonacular provider instance with a mock client."""
    provider = SpoonacularProvider()
    provider.client = mock_http_client
    return provider


@pytest.fixture
def mock_spoonacular_response():
    """Create a mock Spoonacular API response."""
    return {
        "results": [
            {
                "id": 123,
                "title": "Test Recipe",
                "summary": "A test recipe description",
                "image": "https://example.com/image.jpg",
                "sourceUrl": "https://example.com/recipe",
                "readyInMinutes": 45,
                "servings": 4,
                "cuisines": ["Italian"],
                "diets": ["vegetarian"],
                "extendedIngredients": [{"original": "1 cup test ingredient"}],
                "analyzedInstructions": [{"steps": [{"step": "Test step 1"}, {"step": "Test step 2"}]}],
            },
        ],
        "totalResults": 1,
        "number": 10,
        "offset": 0,
    }


@pytest.mark.asyncio
class TestSpoonacularProvider:
    """Test suite for SpoonacularProvider."""

    async def test_search_recipes(self, spoonacular_provider, mock_http_client, mock_spoonacular_response):
        """Test searching for recipes."""
        # Arrange
        mock_response = AsyncMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = mock_spoonacular_response
        mock_http_client.get.return_value = mock_response

        # Act
        result = await spoonacular_provider.search_recipes("pasta")

        # Assert
        assert isinstance(result, RecipeList)
        assert result.total == 1
        assert len(result.results) == 1
        recipe = result.results[0]
        assert recipe.title == "Test Recipe"
        assert recipe.total_time == 45
        mock_http_client.get.assert_called_once()

    async def test_search_recipes_with_filters(self, spoonacular_provider, mock_http_client, mock_spoonacular_response):
        """Test searching for recipes with filters."""
        # Arrange
        mock_response = AsyncMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = mock_spoonacular_response
        mock_http_client.get.return_value = mock_response

        # Act
        result = await spoonacular_provider.search_recipes("pasta", cuisine="Italian", diet="vegetarian", max_time=30)

        # Assert
        assert isinstance(result, RecipeList)
        mock_http_client.get.assert_called_once()
        call_args = mock_http_client.get.call_args[1]["params"]
        assert "cuisine" in call_args
        assert "diet" in call_args
        assert "maxReadyTime" in call_args

    async def test_search_recipes_api_error(self, spoonacular_provider, mock_http_client):
        """Test handling API errors during search."""
        # Arrange
        mock_response = AsyncMock(spec=Response)
        mock_response.status_code = 401
        mock_response.json.return_value = {"message": "Invalid API key"}
        mock_http_client.get.return_value = mock_response

        # Act & Assert
        with pytest.raises(APIError):
            await spoonacular_provider.search_recipes("pasta")

    async def test_get_recipe_by_id(self, spoonacular_provider, mock_http_client):
        """Test retrieving a recipe by ID."""
        # Arrange
        recipe_id = "123"
        mock_response = AsyncMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 123,
            "title": "Test Recipe",
            "summary": "A test recipe",
            "image": "https://example.com/image.jpg",
            "sourceUrl": "https://example.com/recipe",
            "readyInMinutes": 45,
            "servings": 4,
            "cuisines": ["Italian"],
            "diets": ["vegetarian"],
            "extendedIngredients": [{"original": "1 cup test ingredient"}],
            "analyzedInstructions": [{"steps": [{"step": "Test step 1"}]}],
        }
        mock_http_client.get.return_value = mock_response

        # Act
        result = await spoonacular_provider.get_recipe_by_id(recipe_id)

        # Assert
        assert isinstance(result, RecipeSearchResult)
        assert str(result.id) == recipe_id
        assert result.title == "Test Recipe"
        mock_http_client.get.assert_called_once()

    async def test_normalize_recipe(self, spoonacular_provider):
        """Test recipe normalization."""
        # Arrange
        raw_recipe = {
            "id": 123,
            "title": "Test Recipe",
            "summary": "A test recipe",
            "image": "https://example.com/image.jpg",
            "sourceUrl": "https://example.com/recipe",
            "readyInMinutes": 45,
            "servings": 4,
            "cuisines": ["Italian"],
            "diets": ["vegetarian"],
            "extendedIngredients": [{"original": "1 cup test ingredient"}],
            "analyzedInstructions": [{"steps": [{"step": "Test step 1"}]}],
        }

        # Act
        result = spoonacular_provider._normalize_recipe(raw_recipe)

        # Assert
        assert isinstance(result, RecipeSearchResult)
        assert result.title == "Test Recipe"
        assert result.total_time == 45
        assert result.servings == 4
        assert result.cuisine == "Italian"
        if result.diet is not None:
            assert "vegetarian" in result.diet
        if result.ingredients is not None:
            assert len(result.ingredients) == 1
        if result.instructions is not None:
            assert len(result.instructions) == 1

    async def test_api_error_handling(self, spoonacular_provider, mock_http_client):
        """Test handling of various API errors."""
        error_cases = [
            (401, "Unauthorized"),
            (403, "Forbidden"),
            (404, "Not Found"),
            (429, "Too Many Requests"),
            (500, "Internal Server Error"),
        ]

        for status_code, error_message in error_cases:
            # Arrange
            mock_response = AsyncMock(spec=Response)
            mock_response.status_code = status_code
            mock_response.json.return_value = {"message": error_message}
            mock_http_client.get.return_value = mock_response

            # Act & Assert
            with pytest.raises(APIError) as exc_info:
                await spoonacular_provider.search_recipes("pasta")
            assert error_message.lower() in str(exc_info.value).lower()

    async def test_malformed_response(self, spoonacular_provider, mock_http_client):
        """Test handling of malformed API responses."""
        # Arrange
        mock_response = AsyncMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {"invalid": "response"}
        mock_http_client.get.return_value = mock_response

        # Act & Assert
        with pytest.raises(APIError):
            await spoonacular_provider.search_recipes("pasta")
