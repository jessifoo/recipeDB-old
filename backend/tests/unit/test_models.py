"""Unit tests for database models."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from sqlalchemy import select

from app.models.models import Recipe, RecipeInstruction, User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
async def test_user(test_session_factory: AsyncSession) -> User:
    """Create a test user."""
    user = User(
        email="test@example.com",
        hashed_password="hashed_password",
        is_active=True,
    )
    test_session_factory.add(user)
    await test_session_factory.commit()
    await test_session_factory.refresh(user)
    return user


@pytest.fixture
async def test_recipe(test_session_factory: AsyncSession, test_user: User) -> Recipe:
    """Create a test recipe."""
    recipe = Recipe(
        title="Test Recipe",
        description="A test recipe description",
        prep_time_minutes=15,
        cook_time_minutes=30,
        servings=4,
        user_id=test_user.id,
        instructions=[
            RecipeInstruction(step_number=1, instruction="Step 1"),
            RecipeInstruction(step_number=2, instruction="Step 2"),
        ],
    )
    test_session_factory.add(recipe)
    await test_session_factory.commit()
    await test_session_factory.refresh(recipe)
    return recipe


@pytest.mark.asyncio
class TestRecipeModel:
    """Test suite for Recipe model."""

    async def test_create_recipe(self, test_session_factory: AsyncSession, test_user: User) -> None:
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
        recipe = Recipe(user_id=test_user.id, **recipe_data)
        test_session_factory.add(recipe)
        await test_session_factory.commit()
        await test_session_factory.refresh(recipe)

        assert recipe.id is not None
        assert recipe.title == recipe_data["title"]
        assert recipe.user_id == test_user.id
        assert len(recipe.instructions) == 2

    async def test_recipe_relationships(self, test_recipe: Recipe, test_user: User) -> None:
        """Test recipe relationships."""
        assert test_recipe.user_id == test_user.id
        assert len(test_recipe.instructions) == 2
        assert all(isinstance(instr, RecipeInstruction) for instr in test_recipe.instructions)

    async def test_cascade_delete(self, test_session_factory: AsyncSession, test_recipe: Recipe) -> None:
        """Test cascade deletion of recipe instructions."""
        # Store instruction IDs
        instruction_ids = [instr.id for instr in test_recipe.instructions]

        # Delete recipe
        await test_session_factory.delete(test_recipe)
        await test_session_factory.commit()

        # Check that instructions were also deleted
        for instr_id in instruction_ids:
            stmt = select(RecipeInstruction).where(RecipeInstruction.id == instr_id)
            result = await test_session_factory.execute(stmt)
            assert result.scalar_one_or_none() is None

    async def test_recipe_validation(self, test_session_factory: AsyncSession, test_user: User) -> None:
        """Test recipe model validation."""
        # Test invalid prep time
        with pytest.raises(ValueError):
            Recipe(
                title="Invalid Recipe",
                prep_time_minutes=-1,
                cook_time_minutes=30,
                servings=4,
                user_id=test_user.id,
            )

        # Test invalid cook time
        with pytest.raises(ValueError):
            Recipe(
                title="Invalid Recipe",
                prep_time_minutes=15,
                cook_time_minutes=-1,
                servings=4,
                user_id=test_user.id,
            )

        # Test invalid servings
        with pytest.raises(ValueError):
            Recipe(
                title="Invalid Recipe",
                prep_time_minutes=15,
                cook_time_minutes=30,
                servings=0,
                user_id=test_user.id,
            )


@pytest.mark.asyncio
class TestUserModel:
    """Test suite for User model."""

    async def test_create_user(self, test_session_factory: AsyncSession) -> None:
        """Test creating a user."""
        user = User(
            email="new@example.com",
            hashed_password="hashed_password",
            is_active=True,
        )
        test_session_factory.add(user)
        await test_session_factory.commit()
        await test_session_factory.refresh(user)

        assert user.id is not None
        assert user.email == "new@example.com"
        assert user.is_active is True

    async def test_user_recipes(self, test_session_factory: AsyncSession, test_user: User) -> None:
        """Test user-recipe relationship."""
        # Create multiple recipes for the user
        recipes = [
            Recipe(
                title=f"Recipe {i}",
                description=f"Description {i}",
                prep_time_minutes=15,
                cook_time_minutes=30,
                servings=4,
                user_id=test_user.id,
            )
            for i in range(3)
        ]
        for recipe in recipes:
            test_session_factory.add(recipe)
        await test_session_factory.commit()

        # Query user's recipes
        stmt = select(Recipe).where(Recipe.user_id == test_user.id)
        result = await test_session_factory.execute(stmt)
        user_recipes = result.scalars().all()

        assert len(user_recipes) == 3
        assert all(recipe.user_id == test_user.id for recipe in user_recipes)

    async def test_unique_email(self, test_session_factory: AsyncSession, test_user: User) -> None:
        """Test email uniqueness constraint."""
        # Try to create user with same email
        duplicate_user = User(
            email=test_user.email,
            hashed_password="different_password",
            is_active=True,
        )
        test_session_factory.add(duplicate_user)

        with pytest.raises(Exception):  # SQLAlchemy will raise an integrity error
            await test_session_factory.commit()

    async def test_user_active_status(self, test_session_factory: AsyncSession) -> None:
        """Test user active status."""
        # Create inactive user
        inactive_user = User(
            email="inactive@example.com",
            hashed_password="hashed_password",
            is_active=False,
        )
        test_session_factory.add(inactive_user)
        await test_session_factory.commit()
        await test_session_factory.refresh(inactive_user)

        assert inactive_user.is_active is False

        # Activate user
        inactive_user.is_active = True
        await test_session_factory.commit()
        await test_session_factory.refresh(inactive_user)

        assert inactive_user.is_active is True
