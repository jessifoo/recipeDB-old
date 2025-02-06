"""Tests for user API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from httpx import AsyncClient

    from app.models.models import User


@pytest.mark.asyncio
class TestUserAPI:
    """Test suite for user API endpoints."""

    async def test_create_user(self, test_client: AsyncClient):
        """Test user registration."""
        user_data = {
            "email": "new@example.com",
            "password": "newpassword123",
        }
        response = await test_client.post("/api/users/", json=user_data)
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == user_data["email"]
        assert "id" in data
        assert "password" not in data

    async def test_create_user_validation(self, test_client: AsyncClient):
        """Test user registration validation."""
        # Test invalid email
        invalid_data = {
            "email": "notanemail",
            "password": "password123",
        }
        response = await test_client.post("/api/users/", json=invalid_data)
        assert response.status_code == 422

        # Test password too short
        invalid_data = {
            "email": "test@example.com",
            "password": "short",
        }
        response = await test_client.post("/api/users/", json=invalid_data)
        assert response.status_code == 422

    async def test_create_duplicate_user(self, test_client: AsyncClient, test_user: User):
        """Test creating user with existing email."""
        user_data = {
            "email": test_user.email,
            "password": "password123",
        }
        response = await test_client.post("/api/users/", json=user_data)
        assert response.status_code == 400

    async def test_login(self, test_client: AsyncClient, test_user: User):
        """Test user login."""
        login_data = {
            "username": test_user.email,  # OAuth2 form expects 'username'
            "password": "testpassword",
        }
        response = await test_client.post("/api/auth/token", data=login_data)
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    async def test_login_invalid_credentials(self, test_client: AsyncClient):
        """Test login with invalid credentials."""
        login_data = {
            "username": "wrong@example.com",
            "password": "wrongpassword",
        }
        response = await test_client.post("/api/auth/token", data=login_data)
        assert response.status_code == 401

    async def test_get_current_user(self, authorized_client: AsyncClient, test_user: User):
        """Test getting current user information."""
        response = await authorized_client.get("/api/users/me")
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == test_user.email
        assert "password" not in data

    async def test_update_user(self, authorized_client: AsyncClient, test_user: User):
        """Test updating user information."""
        update_data = {
            "email": "updated@example.com",
            "password": "newpassword123",
        }
        response = await authorized_client.put("/api/users/me", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == update_data["email"]
        assert "password" not in data

    async def test_update_user_validation(self, authorized_client: AsyncClient):
        """Test user update validation."""
        # Test invalid email
        invalid_data = {"email": "notanemail"}
        response = await authorized_client.put("/api/users/me", json=invalid_data)
        assert response.status_code == 422

        # Test password too short
        invalid_data = {"password": "short"}
        response = await authorized_client.put("/api/users/me", json=invalid_data)
        assert response.status_code == 422

    async def test_delete_user(self, authorized_client: AsyncClient, test_user: User):
        """Test user deletion."""
        response = await authorized_client.delete("/api/users/me")
        assert response.status_code == 204

        # Verify user is deleted by trying to login
        login_data = {
            "username": test_user.email,
            "password": "testpassword",
        }
        response = await authorized_client.post("/api/auth/token", data=login_data)
        assert response.status_code == 401

    async def test_password_reset_request(self, test_client: AsyncClient, test_user: User):
        """Test password reset request."""
        response = await test_client.post(
            "/api/users/password-reset",
            json={"email": test_user.email},
        )
        assert response.status_code == 200

    async def test_password_reset_nonexistent_user(self, test_client: AsyncClient):
        """Test password reset request for non-existent user."""
        response = await test_client.post(
            "/api/users/password-reset",
            json={"email": "nonexistent@example.com"},
        )
        assert response.status_code == 404

    async def test_verify_email(self, test_client: AsyncClient, test_user: User):
        """Test email verification."""
        # Note: This test assumes you have a way to generate valid verification tokens
        token = "valid_verification_token"  # You should generate this properly
        response = await test_client.post(
            "/api/users/verify-email",
            json={"token": token},
        )
        assert response.status_code == 200

    async def test_verify_email_invalid_token(self, test_client: AsyncClient):
        """Test email verification with invalid token."""
        response = await test_client.post(
            "/api/users/verify-email",
            json={"token": "invalid_token"},
        )
        assert response.status_code == 400

    async def test_unauthorized_access(self, test_client: AsyncClient):
        """Test unauthorized access to protected endpoints."""
        endpoints = [
            ("GET", "/api/users/me"),
            ("PUT", "/api/users/me"),
            ("DELETE", "/api/users/me"),
        ]

        for method, endpoint in endpoints:
            response = await test_client.request(method, endpoint)
            assert response.status_code == 401
