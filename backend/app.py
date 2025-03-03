"""Main application module."""

from __future__ import annotations

import os

from dotenv import load_dotenv

sentry_sdk.init(
    dsn="https://1b7918ad1ae2fa53f9e00a676e7ef195@o4508765460430848.ingest.us.sentry.io/4508765464625152",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)


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
