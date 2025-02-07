"""Unit tests for database session management."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.db.base_class import Base

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncEngine


@pytest.fixture
async def test_engine() -> AsyncEngine:
    """Create a test database engine."""
    engine = create_async_engine(
        "postgresql+asyncpg://postgres:password@localhost/test_db",
        echo=False,
        future=True,
    )

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    # Cleanup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest.fixture
async def test_session_factory(test_engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
    """Create a test session factory."""
    async_session = sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with async_session() as session:
        yield session


@pytest.mark.asyncio
class TestDatabase:
    """Test suite for database functionality."""

    async def test_get_db(self, test_session_factory: AsyncSession) -> None:
        """Test database session creation and cleanup."""
        # Test that we can get a session
        async with test_session_factory as session:
            assert isinstance(session, AsyncSession)
            # Test that we can execute a query
            result = await session.execute(text("SELECT 1"))
            assert result.scalar() == 1

    async def test_session_rollback(self, test_session_factory: AsyncSession) -> None:
        """Test session rollback on error."""
        try:
            async with test_session_factory as session:
                await session.execute(text("SELECT * FROM nonexistent_table"))
                await session.commit()
        except Exception:
            # Should reach here due to invalid SQL
            pass

        # Session should be closed after error
        assert session.is_active is False

    async def test_concurrent_sessions(self, test_session_factory: AsyncSession) -> None:
        """Test multiple concurrent database sessions."""

        async def get_session() -> int:
            async with test_session_factory as session:
                result = await session.execute(text("SELECT 1"))
                return result.scalar()

        # Create multiple concurrent sessions
        results = await asyncio.gather(*[get_session() for _ in range(5)])
        assert all(result == 1 for result in results)

    async def test_session_isolation(self, test_session_factory: AsyncSession) -> None:
        """Test session isolation level."""
        async with test_session_factory as session1, test_session_factory as session2:
            # Sessions should be independent
            await session1.begin()
            await session2.begin()

            # Changes in session1 should not be visible in session2
            await session1.execute(text("CREATE TEMPORARY TABLE IF NOT EXISTS test (id INT)"))
            await session1.commit()

            # Should raise an error as table doesn't exist in session2
            with pytest.raises(Exception):
                await session2.execute(text("SELECT * FROM test"))

    async def test_session_cleanup(self, test_session_factory: AsyncSession) -> None:
        """Test proper session cleanup."""
        session = None
        async with test_session_factory as db_session:
            session = db_session
            assert session.is_active is True

        # Session should be closed after context exit
        assert session.is_active is False
