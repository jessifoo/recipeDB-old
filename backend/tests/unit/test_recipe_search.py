"""Unit tests for recipe search service."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.exceptions import APIError
from app.services.recipe_search import RecipeSearchService

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
def mock_recipe_result() -> RecipeSearchResult:
    """Create a mock recipe search result."""
    return RecipeSearchResult(
        id="test_1",
        title="Test Recipe",
        description="A test recipe description",
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


@pytest.fixture
def mock_recipe_list(mock_recipe_result: RecipeSearchResult) -> RecipeList:
    """Create a mock recipe list."""
    return RecipeList(
        total=1,
        results=[mock_recipe_result],
        source="test_provider",
    )


@pytest.fixture
def mock_provider(mock_recipe_list: RecipeList, mock_recipe_result: RecipeSearchResult):
    """Create a mock recipe provider."""

    class MockProvider:
        async def search_recipes(self, query: str, **kwargs):
            if query == "error":
                raise APIError("Test error")
            if query == "empty":
                return RecipeList(total=0, results=[], source="test_provider")
            return mock_recipe_list

        async def get_recipe_by_id(self, recipe_id: str):
            if recipe_id == "error":
                raise APIError("Test error")
            if recipe_id == "nonexistent":
                return None
            return mock_recipe_result

    return MockProvider()


@pytest.fixture
def recipe_search_service(test_session_factory: AsyncSession, mock_provider) -> RecipeSearchService:
    """Create a recipe search service with mock provider."""
    service = RecipeSearchService(test_session_factory)
    # Using setattr to bypass type checking for testing
    service._provider = mock_provider
    return service


@pytest.mark.asyncio
class TestRecipeSearchService:
    """Test suite for RecipeSearchService."""

    async def test_search_recipes_success(
        self,
        recipe_search_service: RecipeSearchService,
        mock_recipe_list: RecipeList,
    ):
        """Test successful recipe search."""
        result = await recipe_search_service.search("pasta")
        assert isinstance(result, RecipeList)
        assert result.total == mock_recipe_list.total
        assert len(result.results) == len(mock_recipe_list.results)
        assert result.source == mock_recipe_list.source

    async def test_search_recipes_with_filters(
        self,
        recipe_search_service: RecipeSearchService,
        mock_recipe_list: RecipeList,
    ):
        """Test recipe search with filters."""
        filters = {
            "cuisine": "Italian",
            "diet": "vegetarian",
            "max_time": 30,
        }
        result = await recipe_search_service.search("pasta", filters=filters)
        assert isinstance(result, RecipeList)
        assert result.total == mock_recipe_list.total

    async def test_search_recipes_empty_results(self, recipe_search_service: RecipeSearchService):
        """Test recipe search with no results."""
        result = await recipe_search_service.search("empty")
        assert isinstance(result, RecipeList)
        assert result.total == 0
        assert len(result.results) == 0

    async def test_search_recipes_api_error(self, recipe_search_service: RecipeSearchService):
        """Test recipe search with API error."""
        with pytest.raises(APIError):
            await recipe_search_service.search("error")

    async def test_get_recipe_by_id_success(
        self,
        recipe_search_service: RecipeSearchService,
        mock_recipe_result: RecipeSearchResult,
    ):
        """Test successful recipe retrieval by ID."""
        # Using getattr to bypass type checking for testing
        get_recipe_func = recipe_search_service.get_recipe_by_id
        result = await get_recipe_func("test_1")
        assert isinstance(result, RecipeSearchResult)
        assert result.id == mock_recipe_result.id
        assert result.title == mock_recipe_result.title

    async def test_get_recipe_by_id_nonexistent(self, recipe_search_service: RecipeSearchService):
        """Test getting non-existent recipe by ID."""
        # Using getattr to bypass type checking for testing
        get_recipe_func = recipe_search_service.get_recipe_by_id
        result = await get_recipe_func("nonexistent")
        assert result is None

    async def test_get_recipe_by_id_api_error(self, recipe_search_service: RecipeSearchService):
        """Test getting recipe by ID with API error."""
        # Using getattr to bypass type checking for testing
        get_recipe_func = recipe_search_service.get_recipe_by_id
        with pytest.raises(APIError):
            await get_recipe_func("error")

    async def test_search_validation(self, recipe_search_service: RecipeSearchService):
        """Test search input validation."""
        # Test empty query
        with pytest.raises(ValueError):
            await recipe_search_service.search("")

        # Test invalid max_time
        with pytest.raises(ValueError):
            await recipe_search_service.search("pasta", filters={"max_time": -1})

    async def test_recipe_normalization(self, mock_recipe_result: RecipeSearchResult):
        """Test recipe result normalization."""
        # Ensure prep_time and cook_time are not None before adding
        if mock_recipe_result.prep_time is not None and mock_recipe_result.cook_time is not None:
            assert mock_recipe_result.total_time == mock_recipe_result.prep_time + mock_recipe_result.cook_time
        assert isinstance(mock_recipe_result.ingredients, list)
        assert isinstance(mock_recipe_result.instructions, list)
        assert mock_recipe_result.source == "test_provider"
