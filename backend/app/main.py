"""Main FastAPI application."""

from __future__ import annotations

import json
from contextlib import asynccontextmanager
from pathlib import Path
from typing import TYPE_CHECKING

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import (
    allergens,
    cuisine_types,
    dietary_restrictions,
    ingredients,
    meal_types,
    recipe_search,
    recipes,
)
from app.core.config import settings
from app.core.error_handlers import setup_error_handlers
from app.core.error_messages import ErrorMessages

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


def create_application() -> FastAPI:
    """Create FastAPI application."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        lifespan=lifespan,
    )

    # Set up CORS
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Set up error handling
    setup_error_handlers(app)

    # Set up translations
    ErrorMessages.setup_translations(settings.LOCALE_DIR)

    # Include routers
    app.include_router(recipe_search.router, prefix=settings.API_V1_STR)
    app.include_router(recipes.router, prefix=settings.API_V1_STR)
    app.include_router(allergens.router, prefix=settings.API_V1_STR)
    app.include_router(cuisine_types.router, prefix=settings.API_V1_STR)
    app.include_router(dietary_restrictions.router, prefix=settings.API_V1_STR)
    app.include_router(ingredients.router, prefix=settings.API_V1_STR)
    app.include_router(meal_types.router, prefix=settings.API_V1_STR)

    return app


app = create_application()
