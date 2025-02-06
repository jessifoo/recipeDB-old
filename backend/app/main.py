"""Main FastAPI application module."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

import sentry_sdk
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqlalchemy.sql import text

from app.api import api_router
from app.core.config import settings
from app.db.base import get_db

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

# Initialize Sentry
sentry_sdk.init(
    dsn="https://1b7918ad1ae2fa53f9e00a676e7ef195@o4508765460430848.ingest.us.sentry.io/4508765464625152",
    send_default_pii=True,
    traces_sample_rate=1.0,
    _experiments={
        "continuous_profiling_auto_start": True,
    },
    environment=settings.FASTAPI_ENV,  # Add environment information
)

# Initialize FastAPI app
app = FastAPI(
    title="Recipe Database API",
    description="API for managing and searching recipes",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all API routes
app.include_router(api_router)


@app.on_event("startup")
async def startup_event() -> None:
    """Initialize API configuration and database on startup."""
    try:
        redis = aioredis.from_url(
            settings.REDIS_URL,
            encoding="utf8",
            decode_responses=True,
        )
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to initialize service: {e!s}",
        ) from e


@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)) -> dict[str, Any]:
    """Health check endpoint that verifies the service's dependencies.

    Returns:
        Dict containing health status of various components
    """
    try:
        # Check database connection
        await db.execute(text("SELECT 1"))
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {e!s}"

    try:
        # Check Redis connection
        redis = await aioredis.from_url(
            settings.REDIS_URL,
            encoding="utf8",
            decode_responses=True,
        )
        await redis.ping()
        cache_status = "healthy"
    except Exception as e:
        cache_status = f"unhealthy: {e!s}"

    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "database": db_status,
        "cache": cache_status,
    }
