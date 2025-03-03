"""Recipe Database Application.

This package provides a FastAPI-based recipe management system with features
for searching, storing, and managing recipes, meal plans, and related data.

Example:
    .. code-block:: python

        from fastapi import FastAPI
        from app import create_application

        app = create_application()
"""

from __future__ import annotations

from typing import Final

from app.main import create_application

# Package version - should match backend/__version__
__version__: Final[str] = "1.0.0"

# Public API
__all__: Final[list[str]] = ["create_application", "__version__"]
