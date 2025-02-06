"""API dependencies."""

from __future__ import annotations

from app.db.database import get_db

# Re-export get_db for convenience
__all__ = ["get_db"]
