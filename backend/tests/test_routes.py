"""Test module for API routes.

This module contains test cases for the recipe API routes.
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from app.api.dependencies import get_db
from app.db.database import get_test_db
from app.main import app

client = TestClient(app)


@pytest.fixture
def override_get_db():
    """Override the database dependency for testing."""

    def override_db():
        db = get_test_db()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_db
    yield
    app.dependency_overrides = {}


@pytest.fixture
def test_db():
    """Create a test database session."""
    db = get_test_db()
    try:
        yield db
    finally:
        db.close()


@pytest.mark.asyncio
async def test_create_recipe_success(override_get_db):
    """Test successful recipe creation."""
    recipe_data = {
        "title": "Test Recipe",
        "ingredients": ["ingredient1", "ingredient2"],
        "instructions": ["step1", "step2"],
        "cooking_time": 30,
        "tags": [],
    }

    response = client.post("/api/recipes/", json=recipe_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Recipe"
    assert data["ingredients"] == ["ingredient1", "ingredient2"]


@pytest.mark.asyncio
async def test_create_recipe_missing_fields(override_get_db):
    """Test recipe creation with missing required fields."""
    recipe_data = {
        "title": "Test Recipe",
        "ingredients": ["ingredient1", "ingredient2"],
        "instructions": ["step1", "step2"],
        "cooking_time": 30,
    }

    response = client.post("/api/recipes/", json=recipe_data)
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_recipe_success(override_get_db):
    """Test successful recipe retrieval."""
    recipe_data = {
        "title": "Test Recipe",
        "ingredients": ["ingredient1", "ingredient2"],
        "instructions": ["step1", "step2"],
        "cooking_time": 30,
        "tags": [],
    }

    create_response = client.post("/api/recipes/", json=recipe_data)
    recipe_id = create_response.json()["id"]

    response = client.get(f"/api/recipes/{recipe_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Recipe"
    assert data["ingredients"] == ["ingredient1", "ingredient2"]


@pytest.mark.asyncio
async def test_get_recipe_not_found(override_get_db):
    """Test recipe retrieval with non-existent ID."""
    response = client.get("/api/recipes/999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_recipe_success(override_get_db):
    """Test successful recipe update."""
    recipe_data = {
        "title": "Test Recipe",
        "ingredients": ["ingredient1", "ingredient2"],
        "instructions": ["step1", "step2"],
        "cooking_time": 30,
        "tags": [],
    }

    create_response = client.post("/api/recipes/", json=recipe_data)
    recipe_id = create_response.json()["id"]

    updated_data = {
        "title": "Updated Recipe",
        "ingredients": ["updated_ingredient1", "updated_ingredient2"],
        "instructions": ["updated_step1", "updated_step2"],
        "cooking_time": 45,
        "tags": [],
    }

    response = client.put(f"/api/recipes/{recipe_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Recipe"
    assert data["ingredients"] == [
        "updated_ingredient1",
        "updated_ingredient2",
    ]


@pytest.mark.asyncio
async def test_update_recipe_not_found(override_get_db):
    """Test recipe update with non-existent ID."""
    updated_data = {
        "title": "Updated Recipe",
        "ingredients": ["updated_ingredient1", "updated_ingredient2"],
        "instructions": ["updated_step1", "updated_step2"],
        "cooking_time": 45,
        "tags": [],
    }

    response = client.put("/api/recipes/999", json=updated_data)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_recipe_success(override_get_db):
    """Test successful recipe deletion."""
    recipe_data = {
        "title": "Test Recipe",
        "ingredients": ["ingredient1", "ingredient2"],
        "instructions": ["step1", "step2"],
        "cooking_time": 30,
        "tags": [],
    }

    create_response = client.post("/api/recipes/", json=recipe_data)
    recipe_id = create_response.json()["id"]

    response = client.delete(f"/api/recipes/{recipe_id}")
    assert response.status_code == 200

    get_response = client.get(f"/api/recipes/{recipe_id}")
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_delete_recipe_not_found(override_get_db):
    """Test recipe deletion with non-existent ID."""
    response = client.delete("/api/recipes/999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_search_recipes(override_get_db):
    """Test recipe search functionality."""
    # Create test recipes
    recipes = [
        {
            "title": "Pasta Recipe",
            "cuisine": "Italian",
            "diet": "vegetarian",
            "cooking_time": 20,
            "tags": [],
        },
        {
            "title": "Steak Recipe",
            "cuisine": "American",
            "diet": "non-vegetarian",
            "cooking_time": 40,
            "tags": [],
        },
    ]

    for recipe in recipes:
        client.post("/api/recipes/", json=recipe)

    # Test search with filters
    response = client.get("/api/recipes/search?cuisine=Italian&diet=vegetarian")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Pasta Recipe"
