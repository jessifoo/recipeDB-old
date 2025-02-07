"""Main application module."""

from __future__ import annotations

import os

from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    msg = "DATABASE_URL environment variable is not set"
    raise ValueError(msg)

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, class_=AsyncSession, expire_on_commit=False
).configure(bind=engine)

# Register routes
from backend.app.api.routes.protein_types import router as protein_types_router

app.include_router(protein_types_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
