"""Unit tests for authentication service."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings
from app.core.security import create_access_token, get_password_hash, verify_password
from app.models.models import User
from app.services.auth import AuthService, get_current_user
from app.services.exceptions import AuthenticationError

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
def pwd_context():
    """Create password context for testing."""
    return CryptContext(schemes=["bcrypt"], deprecated="auto")


@pytest.fixture
def auth_service(test_session_factory: AsyncSession):
    """Create auth service instance."""
    return AuthService(test_session_factory)


@pytest.fixture
async def test_user_with_password(test_session_factory: AsyncSession):
    """Create a test user with known password."""
    password = "testpassword123"
    hashed_password = get_password_hash(password)
    user = User(
        email="test@example.com",
        hashed_password=hashed_password,
        is_active=True,
    )
    test_session_factory.add(user)
    await test_session_factory.commit()
    await test_session_factory.refresh(user)
    return user, password


@pytest.mark.asyncio
class TestAuthService:
    """Test suite for authentication service."""

    async def test_authenticate_user_success(
        self,
        auth_service: AuthService,
        test_user_with_password: tuple[User, str],
    ):
        """Test successful user authentication."""
        user, password = test_user_with_password
        authenticated_user = await auth_service.authenticate_user(user.email, password)

        assert authenticated_user is not None
        assert authenticated_user.email == user.email

    async def test_authenticate_user_wrong_password(
        self,
        auth_service: AuthService,
        test_user_with_password: tuple[User, str],
    ):
        """Test authentication with wrong password."""
        user, _ = test_user_with_password
        with pytest.raises(AuthenticationError):
            await auth_service.authenticate_user(user.email, "wrongpassword")

    async def test_authenticate_user_nonexistent(self, auth_service: AuthService):
        """Test authentication with non-existent user."""
        with pytest.raises(AuthenticationError):
            await auth_service.authenticate_user("nonexistent@example.com", "password")

    async def test_authenticate_inactive_user(self, auth_service: AuthService, test_session_factory: AsyncSession):
        """Test authentication with inactive user."""
        # Create inactive user
        password = "testpassword123"
        hashed_password = get_password_hash(password)
        inactive_user = User(
            email="inactive@example.com",
            hashed_password=hashed_password,
            is_active=False,
        )
        test_session_factory.add(inactive_user)
        await test_session_factory.commit()

        with pytest.raises(AuthenticationError):
            await auth_service.authenticate_user(inactive_user.email, password)

    async def test_get_current_user_success(
        self,
        test_session_factory: AsyncSession,
        test_user_with_password: tuple[User, str],
    ):
        """Test getting current user from valid token."""
        user, _ = test_user_with_password
        access_token = create_access_token({"sub": user.email})

        current_user = await get_current_user(access_token, test_session_factory)
        assert current_user.email == user.email

    async def test_get_current_user_invalid_token(self, test_session_factory: AsyncSession):
        """Test getting current user with invalid token."""
        with pytest.raises(AuthenticationError):
            await get_current_user("invalid_token", test_session_factory)

    async def test_get_current_user_expired_token(
        self,
        test_session_factory: AsyncSession,
        test_user_with_password: tuple[User, str],
    ):
        """Test getting current user with expired token."""
        user, _ = test_user_with_password
        # Create token that's already expired
        access_token = create_access_token({"sub": user.email, "exp": 1})  # Unix timestamp from past

        with pytest.raises(AuthenticationError):
            await get_current_user(access_token, test_session_factory)

    async def test_password_hashing(self, pwd_context: CryptContext):
        """Test password hashing and verification."""
        password = "testpassword123"
        hashed = get_password_hash(password)

        # Verify hashed password
        assert verify_password(password, hashed)

        # Verify wrong password fails
        assert not verify_password("wrongpassword", hashed)

    async def test_token_creation_and_validation(self, test_user_with_password: tuple[User, str]):
        """Test JWT token creation and validation."""
        user, _ = test_user_with_password
        token_data = {"sub": user.email}
        token = create_access_token(token_data)

        # Decode and verify token
        decoded = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        assert decoded["sub"] == user.email
        assert "exp" in decoded  # Expiration time should be set

    async def test_get_current_user_nonexistent(self, test_session_factory: AsyncSession):
        """Test getting current user with non-existent user in token."""
        access_token = create_access_token({"sub": "nonexistent@example.com"})

        with pytest.raises(AuthenticationError):
            await get_current_user(access_token, test_session_factory)
