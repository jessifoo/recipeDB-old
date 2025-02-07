"""Main application module."""

from __future__ import annotations

import json
from contextlib import asynccontextmanager
from pathlib import Path
from typing import TYPE_CHECKING

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes.routes import router as recipe_router

if TYPE_CHECKING:
    from collections.abc import AsyncIterator


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Handle application lifespan events.

    Args:
        app: The FastAPI application instance
    """
    # Startup
    yield
    # Shutdown
    if app.openapi():
        openapi_path = Path(__file__).parent.parent / "openapi.json"
        with openapi_path.open("w", encoding="utf-8") as f:
            json.dump(app.openapi(), f, indent=2)


app = FastAPI(
    title="RecipeDB",
    description="Recipe Database API",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=getattr(settings, "ALLOWED_ORIGINS", ["*"]),  # Safely access setting
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(recipe_router)
