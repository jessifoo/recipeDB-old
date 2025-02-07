"""Tests for authentication API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from jose import jwt

from app.core.config import settings
from app.core.security import create_access_token, get_password_hash
from app.models.models import User

if TYPE_CHECKING:
    from httpx import AsyncClient


@pytest.fixture
async def test_user_with_password(test_session_factory):
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
class TestAuthAPI:
    """Test suite for authentication API endpoints."""

    async def test_login_success(self, test_client: AsyncClient, test_user_with_password):
        """Test successful login."""
        user, password = test_user_with_password
        login_data = {
            "username": user.email,  # OAuth2 form expects 'username'
            "password": password,
        }
        response = await test_client.post("/api/auth/token", data=login_data)
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

        # Verify token contents
        token = data["access_token"]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        assert payload["sub"] == user.email

    async def test_login_invalid_password(self, test_client: AsyncClient, test_user_with_password):
        """Test login with invalid password."""
        user, _ = test_user_with_password
        login_data = {
            "username": user.email,
            "password": "wrongpassword",
        }
        response = await test_client.post("/api/auth/token", data=login_data)
        assert response.status_code == 401
        data = response.json()
        assert "detail" in data

    async def test_login_nonexistent_user(self, test_client: AsyncClient):
        """Test login with non-existent user."""
        login_data = {
            "username": "nonexistent@example.com",
            "password": "password123",
        }
        response = await test_client.post("/api/auth/token", data=login_data)
        assert response.status_code == 401
        data = response.json()
        assert "detail" in data

    async def test_login_inactive_user(self, test_client: AsyncClient, test_session_factory):
        """Test login with inactive user."""
        # Create inactive user
        password = "testpassword123"
        hashed_password = get_password_hash(password)
        user = User(
            email="inactive@example.com",
            hashed_password=hashed_password,
            is_active=False,
        )
        test_session_factory.add(user)
        await test_session_factory.commit()

        login_data = {
            "username": user.email,
            "password": password,
        }
        response = await test_client.post("/api/auth/token", data=login_data)
        assert response.status_code == 401
        data = response.json()
        assert "detail" in data

    async def test_token_validation(self, test_client: AsyncClient, test_user_with_password):
        """Test token validation."""
        user, _ = test_user_with_password
        # Create token with invalid signature
        invalid_token = create_access_token(
            {"sub": user.email},
            secret_key="invalid_secret",
        )

        headers = {"Authorization": f"Bearer {invalid_token}"}
        response = await test_client.get("/api/users/me", headers=headers)
        assert response.status_code == 401

    async def test_token_expiration(self, test_client: AsyncClient, test_user_with_password):
        """Test expired token."""
        user, _ = test_user_with_password
        # Create expired token
        expired_token = create_access_token(
            {"sub": user.email, "exp": 1},  # Unix timestamp from past
        )

        headers = {"Authorization": f"Bearer {expired_token}"}
        response = await test_client.get("/api/users/me", headers=headers)
        assert response.status_code == 401

    async def test_invalid_token_format(self, test_client: AsyncClient):
        """Test invalid token format."""
        invalid_headers = [
            {"Authorization": "Bearer"},  # Missing token
            {"Authorization": "Bearer "},  # Empty token
            {"Authorization": "Bearer invalid.token.format"},  # Invalid format
            {"Authorization": "Token validtoken"},  # Wrong scheme
        ]

        for headers in invalid_headers:
            response = await test_client.get("/api/users/me", headers=headers)
            assert response.status_code == 401

    async def test_refresh_token(self, test_client: AsyncClient, test_user_with_password):
        """Test token refresh."""
        user, password = test_user_with_password
        # First login to get tokens
        login_data = {
            "username": user.email,
            "password": password,
        }
        response = await test_client.post("/api/auth/token", data=login_data)
        assert response.status_code == 200
        tokens = response.json()

        # Use refresh token to get new access token
        refresh_data = {
            "refresh_token": tokens["refresh_token"],
        }
        response = await test_client.post("/api/auth/refresh", json=refresh_data)
        assert response.status_code == 200
        new_tokens = response.json()
        assert "access_token" in new_tokens
        assert new_tokens["access_token"] != tokens["access_token"]

    async def test_logout(self, authorized_client: AsyncClient):
        """Test logout endpoint."""
        response = await authorized_client.post("/api/auth/logout")
        assert response.status_code == 200

        # Verify token is invalidated
        response = await authorized_client.get("/api/users/me")
        assert response.status_code == 401
