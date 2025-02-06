"""Test fixtures for the RecipeDB application."""

import asyncio
from typing import AsyncGenerator

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models.models import Base

# Create async engine for testing
test_engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)

# Create async session factory
async_session_maker = sessionmaker(
    test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def init_db():
    """Initialize test database."""
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture
async def async_session(init_db) -> AsyncGenerator[AsyncSession, None]:
    """Create a new database session for a test."""
    async with async_session_maker() as session:
        yield session
        await session.rollback()
