"""Test module for database models."""

import pytest
from app.models.models import Recipe
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio()
async def test_create_recipe(async_session: AsyncSession):
    """Test creating a recipe."""
    recipe = Recipe(
        title="Test Recipe",
        description="A test recipe",
        instructions="Test instructions",
    )
    async_session.add(recipe)
    await async_session.commit()

    assert recipe.recipe_id is not None
    assert recipe.title == "Test Recipe"
