"""Backend package initialization.

This module initializes the backend package by:
1. Loading environment variables
2. Setting up logging
3. Initializing error tracking (if configured)
4. Setting up any other global services
"""

from __future__ import annotations

import logging
import os
from collections.abc import Sequence
from pathlib import Path
from typing import Final

# Initialize logging early
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger: Final[logging.Logger] = logging.getLogger(__name__)

# Import runtime dependencies
import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.base import Integration
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

# Initialize environment variables
env_path: Final[Path] = Path(__file__).parent / ".env"
env_development: Final[Path] = Path(__file__).parent / ".env.development"

# Load development env if it exists, otherwise try default .env
if os.getenv("ENVIRONMENT") != "production":
    if env_development.exists():
        logger.info("Loading development environment from .env.development")
        load_dotenv(str(env_development))
    elif env_path.exists():
        logger.info("Loading development environment from .env")
        load_dotenv(str(env_path))
elif env_path.exists():
    logger.info("Loading production environment from .env")
    load_dotenv(str(env_path))
else:
    logger.warning("No .env file found in production environment")

# Initialize Sentry if DSN is provided
sentry_dsn: str | None = os.getenv("SENTRY_DSN")
if sentry_dsn:
    try:
        integrations: Sequence[Integration] = [
            LoggingIntegration(level=logging.INFO, event_level=logging.ERROR),
            FastApiIntegration(),
            SqlalchemyIntegration(),
        ]

        sentry_sdk.init(
            dsn=sentry_dsn,
            send_default_pii=True,
            integrations=integrations,
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
            environment=os.getenv("ENVIRONMENT", "development"),
        )
        logger.info("Sentry initialized successfully")
    except ImportError as e:
        logger.warning(f"Sentry SDK not installed. Error tracking disabled: {e}")
    except Exception as e:
        logger.exception(f"Failed to initialize Sentry: {e}")

# Package version
__version__: Final[str] = "1.0.0"
