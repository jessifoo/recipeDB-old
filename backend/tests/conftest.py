"""Test configuration and fixtures."""

from __future__ import annotations

import asyncio
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from dotenv import load_dotenv
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import Settings
from app.core.security import create_access_token
from app.db.base_class import Base
from app.db.session import get_db
from app.main import app
from app.models.models import User

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from fastapi import FastAPI
    from sqlalchemy.ext.asyncio import AsyncEngine

# Load test environment variables
test_env_path = Path(__file__).parent / ".env.test"
load_dotenv(test_env_path)

DATABASE_URL = "@TODO"


# Override settings for testing
@pytest.fixture(scope="session")
def test_settings() -> Settings:
    """Get test settings."""
    return Settings(
        FASTAPI_ENV="test",
        SECRET_KEY="test_secret_key",
        PROJECT_NAME="Recipe Database API Test",
        API_V1_STR="/api/v1",
        POSTGRES_SERVER="localhost",
        POSTGRES_USER="postgres",
        POSTGRES_PASSWORD="password",
        POSTGRES_DB="test_recipe_db",
        REDIS_URL="redis://localhost",
        LOG_LEVEL="DEBUG",
        SPOONACULAR_API_KEY="test_key",
        EDAMAM_APP_ID="test_id",
        EDAMAM_APP_KEY="test_key",
        API_NINJAS_API_KEY="test_key",
        TASTY_API_KEY="test_key",
        DEFAULT_RECIPE_PROVIDER="mock",
        ENABLE_EXTERNAL_PROVIDERS=False,
        FIRST_SUPERUSER="admin@example.com",
        FIRST_SUPERUSER_PASSWORD="admin",
    )


# Create async engine for testing
@pytest.fixture(scope="session")
def test_engine(test_settings: Settings) -> AsyncEngine:
    """Create a test database engine."""
    return create_async_engine(
        f"postgresql+asyncpg://{test_settings.POSTGRES_USER}:{test_settings.POSTGRES_PASSWORD}@{test_settings.POSTGRES_SERVER}/{test_settings.POSTGRES_DB}",
        echo=False,
        future=True,
    )


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def init_db(test_engine: AsyncEngine):
    """Initialize test database."""
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture
async def db_session(init_db, test_engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
    """Create a new database session for a test."""
    session_factory = async_sessionmaker(
        bind=test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with session_factory() as session:
        yield session
        await session.rollback()
        await session.close()


@pytest.fixture
async def test_app(db_session: AsyncSession) -> FastAPI:
    """Create a test FastAPI application."""
    app.dependency_overrides = {
        get_db: lambda: db_session,
    }
    return app


@pytest.fixture
async def test_client(test_app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Create a test client for making API requests."""
    async with AsyncClient(app=test_app, base_url="http://test") as client:
        yield client


@pytest.fixture
async def test_user(db_session: AsyncSession) -> User:
    """Create a test user."""
    user = User(
        email="test@example.com",
        hashed_password="hashed_test_password",
        is_active=True,
    )
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)
    return user


@pytest.fixture
def test_user_token(test_user: User) -> str:
    """Create an access token for the test user."""
    return create_access_token({"sub": test_user.email})


@pytest.fixture
async def authorized_client(test_client: AsyncClient, test_user_token: str) -> AsyncClient:
    """Create an authorized test client with user token."""
    test_client.headers["Authorization"] = f"Bearer {test_user_token}"
    return test_client
