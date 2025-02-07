"""Database session management."""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.db.base import get_db as base_get_db

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """Get async database session.

    This is a convenience wrapper around the base get_db function
    to make it clearer that we're using async sessions.
    """
    async with base_get_db() as session:
        yield session


# Alias for backward compatibility
get_db = get_async_db
