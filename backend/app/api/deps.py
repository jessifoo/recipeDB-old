"""API dependencies.

This module provides reusable FastAPI dependencies for route handlers.
Dependencies handle common concerns like database sessions, authentication,
and request validation.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.deps import get_db

        @router.get("/items")
        async def get_items(db: AsyncSession = Depends(get_db)):
            # Use db session here
            pass
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_async_db

# Type-annotated dependencies for better IDE support
DatabaseSession = Annotated[AsyncSession, Depends(get_async_db)]

__version__ = "1.0.0"

__all__ = ["DatabaseSession", "get_async_db"]
