"""Database configuration."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if TYPE_CHECKING:
    from collections.abc import Generator

    from sqlalchemy.orm import Session

load_dotenv()  # Load environment variables from .env file

# Get database URL from environment variable with a default for development
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/recipe_db")

# Create database engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Enable connection pool "pre-ping" feature
    echo=os.getenv("SQL_ECHO", "false").lower() == "true",  # Enable SQL logging based on env var
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for declarative models
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Get database session.

    Yields:
        SQLAlchemy Session: Database session that is automatically closed after use.

    This function is designed to be used as a dependency in FastAPI endpoints.
    FastAPI's dependency injection system will automatically call this function
    for each request that needs a database session, ensuring proper session
    creation and closure.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
