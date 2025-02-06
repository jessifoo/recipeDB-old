"""Database session configuration.

This module provides database session factories and dependencies for both
synchronous and asynchronous database operations.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING

from sqlalchemy.engine import create_engine, make_url
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator, Generator

    from sqlalchemy.engine import Engine
    from sqlalchemy.ext.asyncio import AsyncEngine
    from sqlalchemy.orm import Session

# Create declarative base
Base = declarative_base()

# Create engines
if not settings.SQLALCHEMY_DATABASE_URI:
    raise ValueError("Database URI is not configured")

db_url = make_url(settings.SQLALCHEMY_DATABASE_URI)
engine: Engine = create_engine(
    db_url,
    pool_pre_ping=True,  # Enable connection health checks
    pool_recycle=3600,  # Recycle connections after 1 hour
)

# Create async engine with asyncpg driver
async_db_url = db_url.set(drivername="postgresql+asyncpg")
async_engine: AsyncEngine = create_async_engine(
    async_db_url,
    echo=settings.LOG_LEVEL == "DEBUG",  # Enable SQL debugging based on log level
    pool_pre_ping=True,
    pool_recycle=3600,
)

# Create session factories
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
)

AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Bind the async session after creation
AsyncSessionLocal.configure(bind=async_engine)


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Get a database session for synchronous operations.

    Yields:
        Session: SQLAlchemy database session

    Raises:
        Exception: Any database-related exception that occurs during the session
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """Get a database session for asynchronous operations.

    Yields:
        AsyncSession: SQLAlchemy async database session

    Raises:
        Exception: Any database-related exception that occurs during the session
    """
    async with AsyncSessionLocal() as db:
        try:
            yield db
        except Exception as e:
            await db.rollback()
            raise e


async def init_async_db() -> None:
    """Initialize the database asynchronously.

    This function should be called during application startup
    for asynchronous database initialization.
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_async_db() -> None:
    """Close the async database connection pool.

    This function should be called during application shutdown
    to properly close all database connections.
    """
    await async_engine.dispose()
