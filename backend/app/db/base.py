"""Database session management."""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from app.core.config import settings

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession

if not settings.SQLALCHEMY_DATABASE_URI:
    raise ValueError("Database URI is not configured")

# Create async engine with optimized settings
engine = create_async_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    pool_pre_ping=True,
    pool_size=20,  # Maximum number of connections in the pool
    max_overflow=10,  # Maximum number of connections that can be created beyond pool_size
    pool_timeout=30,  # Seconds to wait before giving up on getting a connection from the pool
    pool_recycle=1800,  # Recycle connections after 30 minutes
    echo=settings.LOG_LEVEL.upper() == "DEBUG",
    echo_pool=False,  # Don't log pool checkouts/checkins unless debugging
    future=True,  # Enable SQLAlchemy 2.0 behavior
    execution_options={
        "isolation_level": "REPEATABLE READ",  # Default isolation level
        "postgresql_readonly": False,  # Default to read-write transactions
        "postgresql_synchronous_commit": True,  # Ensure writes are durable
    },
)

# Create async session factory with explicit transaction control
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,  # Don't auto-flush for better control and performance
)


@asynccontextmanager
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Get database session with transaction management.

    This context manager ensures proper handling of transactions:
    - Automatically rolls back uncommitted changes on exceptions
    - Closes the session when done
    - Provides transaction isolation
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


@asynccontextmanager
async def get_db_readonly() -> AsyncGenerator[AsyncSession, None]:
    """Get read-only database session.

    This context manager is optimized for read-only operations:
    - Sets transaction isolation level to READ COMMITTED
    - Disables autoflush and expire_on_commit
    - Automatically rolls back at the end to release locks quickly
    """
    async with AsyncSessionLocal() as session:
        try:
            # Set read-only mode and optimized isolation level
            await session.connection(
                execution_options={
                    "isolation_level": "READ COMMITTED",
                    "postgresql_readonly": True,
                },
            )
            yield session
            await session.rollback()  # Always rollback read-only transactions
        except Exception:
            await session.rollback()
            raise


async def dispose_engine() -> None:
    """Dispose of the engine and connection pool.

    Call this when shutting down the application to clean up resources.
    """
    if isinstance(engine, AsyncEngine):
        await engine.dispose()
