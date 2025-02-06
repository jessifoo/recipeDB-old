"""Tests for recipe search API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest

from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.exceptions import APIError

if TYPE_CHECKING:
    from httpx import AsyncClient


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


@pytest.mark.asyncio
class TestRecipeSearchAPI:
    """Test suite for recipe search API endpoints."""

    async def test_search_recipes(self, authorized_client: AsyncClient, mock_recipe_list: RecipeList):
        """Test recipe search endpoint."""
        with patch("app.services.recipe_search.RecipeSearchService.search") as mock_search:
            mock_search.return_value = mock_recipe_list
            response = await authorized_client.get("/api/recipes/search/?query=pasta&cuisine=Italian&diet=vegetarian")

            assert response.status_code == 200
            data = response.json()
            assert data["total"] == mock_recipe_list.total
            assert len(data["results"]) == len(mock_recipe_list.results)
            recipe = data["results"][0]
            assert recipe["title"] == mock_recipe_list.results[0].title

            # Verify search parameters
            mock_search.assert_called_once_with(
                "pasta",
                filters={"cuisine": "Italian", "diet": "vegetarian"},
            )

    async def test_search_recipes_validation(self, authorized_client: AsyncClient):
        """Test recipe search validation."""
        # Test empty query
        response = await authorized_client.get("/api/recipes/search/?query=")
        assert response.status_code == 422

        # Test invalid max_time
        response = await authorized_client.get("/api/recipes/search/?query=pasta&max_time=-1")
        assert response.status_code == 422

    async def test_search_recipes_api_error(self, authorized_client: AsyncClient):
        """Test handling API errors during search."""
        with patch("app.services.recipe_search.RecipeSearchService.search") as mock_search:
            mock_search.side_effect = APIError("API error")
            response = await authorized_client.get("/api/recipes/search/?query=pasta")
            assert response.status_code == 503
            data = response.json()
            assert "detail" in data

    async def test_get_recipe_by_id(self, authorized_client: AsyncClient, mock_recipe_result: RecipeSearchResult):
        """Test getting recipe by ID."""
        with patch("app.services.recipe_search.RecipeSearchService.get_recipe_by_id") as mock_get:
            mock_get.return_value = mock_recipe_result
            response = await authorized_client.get("/api/recipes/external/test_1")

            assert response.status_code == 200
            data = response.json()
            assert data["id"] == mock_recipe_result.id
            assert data["title"] == mock_recipe_result.title

    async def test_get_nonexistent_recipe(self, authorized_client: AsyncClient):
        """Test getting non-existent recipe."""
        with patch("app.services.recipe_search.RecipeSearchService.get_recipe_by_id") as mock_get:
            mock_get.return_value = None
            response = await authorized_client.get("/api/recipes/external/nonexistent")
            assert response.status_code == 404

    async def test_search_recipes_with_filters(self, authorized_client: AsyncClient, mock_recipe_list: RecipeList):
        """Test recipe search with various filters."""
        test_cases = [
            {
                "params": {"query": "pasta", "cuisine": "Italian"},
                "expected_filters": {"cuisine": "Italian"},
            },
            {
                "params": {"query": "curry", "diet": "vegetarian"},
                "expected_filters": {"diet": "vegetarian"},
            },
            {
                "params": {"query": "quick", "max_time": "30"},
                "expected_filters": {"max_time": 30},
            },
            {
                "params": {
                    "query": "healthy",
                    "cuisine": "Asian",
                    "diet": "vegan",
                    "max_time": "45",
                },
                "expected_filters": {
                    "cuisine": "Asian",
                    "diet": "vegan",
                    "max_time": 45,
                },
            },
        ]

        with patch("app.services.recipe_search.RecipeSearchService.search") as mock_search:
            mock_search.return_value = mock_recipe_list

            for case in test_cases:
                # Build query string
                query_params = "&".join(f"{k}={v}" for k, v in case["params"].items())
                response = await authorized_client.get(f"/api/recipes/search/?{query_params}")

                assert response.status_code == 200
                mock_search.assert_called_with(
                    case["params"]["query"],
                    filters=case["expected_filters"],
                )

    async def test_search_recipes_pagination(self, authorized_client: AsyncClient, mock_recipe_list: RecipeList):
        """Test recipe search pagination."""
        with patch("app.services.recipe_search.RecipeSearchService.search") as mock_search:
            mock_search.return_value = mock_recipe_list

            # Test different page sizes
            for limit in [10, 20, 50]:
                response = await authorized_client.get(f"/api/recipes/search/?query=pasta&limit={limit}")
                assert response.status_code == 200
                mock_search.assert_called_with(
                    "pasta",
                    filters={},
                    limit=limit,
                )

            # Test different pages
            for skip in [0, 10, 20]:
                response = await authorized_client.get(f"/api/recipes/search/?query=pasta&skip={skip}")
                assert response.status_code == 200
                mock_search.assert_called_with(
                    "pasta",
                    filters={},
                    skip=skip,
                )

    async def test_unauthorized_access(self, test_client: AsyncClient):
        """Test unauthorized access to protected endpoints."""
        endpoints = [
            "/api/recipes/search/?query=pasta",
            "/api/recipes/external/123",
        ]

        for endpoint in endpoints:
            response = await test_client.get(endpoint)
            assert response.status_code == 401
