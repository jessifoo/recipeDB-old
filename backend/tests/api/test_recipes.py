"""Tests for recipe API endpoints."""

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

import pytest

from app.models.models import Recipe

if TYPE_CHECKING:
    from httpx import AsyncClient


@pytest.fixture
async def test_recipe(test_session_factory, test_user):
    """Create a test recipe."""
    recipe = Recipe(
        title="Test Recipe",
        description="A test recipe description",
        prep_time_minutes=15,
        cook_time_minutes=30,
        servings=4,
        user_id=test_user.id,
        instructions=[
            {"step_number": 1, "instruction": "Step 1"},
            {"step_number": 2, "instruction": "Step 2"},
        ],
    )
    test_session_factory.add(recipe)
    await test_session_factory.commit()
    await test_session_factory.refresh(recipe)
    return recipe


@pytest.mark.asyncio
class TestRecipeAPI:
    """Test suite for recipe API endpoints."""

    async def test_create_recipe(self, authorized_client: AsyncClient):
        """Test creating a recipe."""
        recipe_data = {
            "title": "New Recipe",
            "description": "A new recipe description",
            "prep_time_minutes": 20,
            "cook_time_minutes": 40,
            "servings": 6,
            "instructions": [
                {"step_number": 1, "instruction": "First step"},
                {"step_number": 2, "instruction": "Second step"},
            ],
        }

        response = await authorized_client.post("/api/recipes/", json=recipe_data)
        assert response.status_code == HTTPStatus.CREATED
        data = response.json()
        assert data["title"] == recipe_data["title"]
        assert len(data["instructions"]) == len(recipe_data["instructions"])

    async def test_create_recipe_validation(self, authorized_client: AsyncClient):
        """Test recipe creation validation."""
        # Test missing required field
        invalid_data = {
            "description": "Missing title",
            "prep_time_minutes": 20,
            "cook_time_minutes": 40,
            "servings": 6,
        }
        response = await authorized_client.post("/api/recipes/", json=invalid_data)
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

        # Test invalid prep time
        invalid_data = {
            "title": "Invalid Recipe",
            "description": "Invalid prep time",
            "prep_time_minutes": -1,
            "cook_time_minutes": 40,
            "servings": 6,
        }
        response = await authorized_client.post("/api/recipes/", json=invalid_data)
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    async def test_get_recipe(self, authorized_client: AsyncClient, test_recipe: Recipe):
        """Test getting a recipe by ID."""
        response = await authorized_client.get(f"/api/recipes/{test_recipe.id}")
        assert response.status_code == HTTPStatus.OK
        data = response.json()
        assert data["title"] == test_recipe.title
        assert data["user_id"] == test_recipe.user_id

    async def test_get_nonexistent_recipe(self, authorized_client: AsyncClient):
        """Test getting a non-existent recipe."""
        response = await authorized_client.get("/api/recipes/999")

        assert response.status_code == HTTPStatus.NOT_FOUND

    async def test_update_recipe(self, authorized_client: AsyncClient, test_recipe: Recipe):
        """Test updating a recipe."""
        update_data = {
            "title": "Updated Recipe",
            "description": "Updated description",
            "instructions": [
                {"step_number": 1, "instruction": "Updated step"},
            ],
        }

        response = await authorized_client.put(
            f"/api/recipes/{test_recipe.id}",
            json=update_data,
        )
        assert response.status_code == HTTPStatus.OK
        data = response.json()
        assert data["title"] == update_data["title"]
        assert len(data["instructions"]) == len(update_data["instructions"])
        assert data["instructions"][0]["step_number"] == 1
        assert data["instructions"][0]["instruction"] == "Updated step"

    async def test_update_other_user_recipe(
        self,
        authorized_client: AsyncClient,
        test_session_factory,
        test_recipe: Recipe,
    ):
        """Test updating another user's recipe."""
        # Create recipe owned by different user
        other_recipe = Recipe(
            title="Other User's Recipe",
            description="This recipe belongs to another user",
            prep_time_minutes=15,
            cook_time_minutes=30,
            servings=4,
            user_id=test_recipe.user_id + 1,
        )
        test_session_factory.add(other_recipe)
        await test_session_factory.commit()

        update_data = {"title": "Trying to update"}
        response = await authorized_client.put(
            f"/api/recipes/{other_recipe.id}",
            json=update_data,
        )
        assert response.status_code == HTTPStatus.FORBIDDEN

    async def test_delete_recipe(self, authorized_client: AsyncClient, test_recipe: Recipe):
        """Test deleting a recipe."""
        response = await authorized_client.delete(f"/api/recipes/{test_recipe.id}")
        assert response.status_code == HTTPStatus.NO_CONTENT

        # Verify recipe is deleted
        response = await authorized_client.get(f"/api/recipes/{test_recipe.id}")
        assert response.status_code == HTTPStatus.NOT_FOUND

    async def test_list_recipes(self, authorized_client: AsyncClient, test_recipe: Recipe):
        """Test listing recipes with pagination."""
        # Create additional recipes
        recipe_data = {
            "title": "Another Recipe",
            "description": "Another recipe description",
            "prep_time_minutes": 20,
            "cook_time_minutes": 40,
            "servings": 6,
            "instructions": [{"step_number": 1, "instruction": "Step"}],
        }
        await authorized_client.post("/api/recipes/", json=recipe_data)

        # Test pagination
        response = await authorized_client.get("/api/recipes/?skip=0&limit=1")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1

        response = await authorized_client.get("/api/recipes/?skip=1&limit=1")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1

    async def test_search_recipes(self, authorized_client: AsyncClient):
        """Test searching recipes."""
        response = await authorized_client.get("/api/recipes/search/?query=pasta&cuisine=Italian&diet=vegetarian")
        assert response.status_code == 200
        data = response.json()
        assert "total" in data
        assert "results" in data

    async def test_search_recipes_validation(self, authorized_client: AsyncClient):
        """Test recipe search validation."""
        # Test empty query
        response = await authorized_client.get("/api/recipes/search/?query=")
        assert response.status_code == 422

        # Test invalid max_time
        response = await authorized_client.get("/api/recipes/search/?query=pasta&max_time=-1")
        assert response.status_code == 422

    async def test_unauthorized_access(self, test_client: AsyncClient):
        """Test unauthorized access to protected endpoints."""
        endpoints = [
            ("POST", "/api/recipes/"),
            ("PUT", "/api/recipes/1"),
            ("DELETE", "/api/recipes/1"),
        ]

        for method, endpoint in endpoints:
            response = await test_client.request(method, endpoint)
            assert response.status_code == 401
