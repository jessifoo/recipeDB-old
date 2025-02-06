"""Unit tests for user service."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from sqlalchemy import select

from app.core.security import get_password_hash
from app.models.models import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.exceptions import ValidationError
from app.services.user import UserService

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
def user_service(test_session_factory: AsyncSession) -> UserService:
    """Create a user service instance."""
    return UserService(test_session_factory)


@pytest.fixture
async def test_user(test_session_factory: AsyncSession) -> User:
    """Create a test user."""
    user = User(
        email="test@example.com",
        hashed_password=get_password_hash("testpassword"),
        is_active=True,
    )
    test_session_factory.add(user)
    await test_session_factory.commit()
    await test_session_factory.refresh(user)
    return user


@pytest.mark.asyncio
class TestUserService:
    """Test suite for UserService."""

    async def test_create_user(self, user_service: UserService):
        """Test creating a new user."""
        user_data = UserCreate(
            email="new@example.com",
            password="newpassword123",
        )
        user = await user_service.create_user(user_data)

        assert user.email == user_data.email
        assert user.is_active is True
        assert user.hashed_password != user_data.password  # Password should be hashed

    async def test_create_duplicate_user(self, user_service: UserService, test_user: User):
        """Test creating a user with existing email."""
        user_data = UserCreate(
            email=test_user.email,
            password="newpassword123",
        )
        with pytest.raises(ValidationError):
            await user_service.create_user(user_data)

    async def test_get_user(self, user_service: UserService, test_user: User):
        """Test getting a user by ID."""
        user = await user_service.get_user(test_user.id)
        assert user is not None
        assert user.email == test_user.email

    async def test_get_user_by_email(self, user_service: UserService, test_user: User):
        """Test getting a user by email."""
        user = await user_service.get_user_by_email(test_user.email)
        assert user is not None
        assert user.id == test_user.id

    async def test_get_nonexistent_user(self, user_service: UserService):
        """Test getting a non-existent user."""
        user = await user_service.get_user(999)
        assert user is None

    async def test_update_user(self, user_service: UserService, test_user: User):
        """Test updating a user."""
        update_data = UserUpdate(
            email="updated@example.com",
            password="newpassword123",
        )
        updated_user = await user_service.update_user(test_user.id, update_data)

        assert updated_user.email == update_data.email
        assert updated_user.hashed_password != test_user.hashed_password

    async def test_update_nonexistent_user(self, user_service: UserService):
        """Test updating a non-existent user."""
        update_data = UserUpdate(email="new@example.com")
        with pytest.raises(ValidationError):
            await user_service.update_user(999, update_data)

    async def test_delete_user(self, user_service: UserService, test_user: User, test_session_factory: AsyncSession):
        """Test deleting a user."""
        await user_service.delete_user(test_user.id)

        # Verify user is deleted
        stmt = select(User).where(User.id == test_user.id)
        result = await test_session_factory.execute(stmt)
        assert result.scalar_one_or_none() is None

    async def test_delete_nonexistent_user(self, user_service: UserService):
        """Test deleting a non-existent user."""
        with pytest.raises(ValidationError):
            await user_service.delete_user(999)

    async def test_get_users(self, user_service: UserService, test_session_factory: AsyncSession):
        """Test getting multiple users with pagination."""
        # Create additional users
        users = []
        for i in range(3):
            user = User(
                email=f"user{i}@example.com",
                hashed_password=get_password_hash("password"),
                is_active=True,
            )
            test_session_factory.add(user)
            users.append(user)
        await test_session_factory.commit()

        # Test pagination
        result = await user_service.get_users(skip=0, limit=2)
        assert len(result) == 2

        result = await user_service.get_users(skip=2, limit=2)
        assert len(result) == 2

    async def test_deactivate_user(self, user_service: UserService, test_user: User):
        """Test deactivating a user."""
        updated_user = await user_service.update_user(
            test_user.id,
            UserUpdate(is_active=False),
        )
        assert updated_user.is_active is False

    async def test_validate_password(self, user_service: UserService):
        """Test password validation rules."""
        # Test password too short
        with pytest.raises(ValidationError):
            await user_service.create_user(UserCreate(email="test@example.com", password="short"))

        # Test password without numbers
        with pytest.raises(ValidationError):
            await user_service.create_user(UserCreate(email="test@example.com", password="noNumbers"))

    async def test_validate_email(self, user_service: UserService):
        """Test email validation rules."""
        invalid_emails = [
            "",  # Empty
            "notanemail",  # No @ symbol
            "@nodomain",  # No local part
            "no@domain",  # Invalid domain
            "spaces in@email.com",  # Spaces in local part
        ]

        for email in invalid_emails:
            with pytest.raises(ValidationError):
                await user_service.create_user(UserCreate(email=email, password="validPass123"))
