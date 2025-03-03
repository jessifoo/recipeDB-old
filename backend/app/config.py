"""Application configuration.

This module provides a single source of truth for all application configuration,
using environment variables loaded from .env files.

Configuration Hierarchy:
    1. Environment variables (highest priority)
    2. Environment-specific .env file (.env.development or .env.production)
    3. Default .env file (lowest priority)

Example:
    .. code-block:: python

        from app.config import settings

        # Access configuration
        db_url = settings.DATABASE_URL
        api_key = settings.SPOONACULAR_API_KEY

Note:
    This module uses Pydantic for validation and type safety.
    All configuration is loaded lazily and cached.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any, Literal
from urllib.parse import quote_plus

from pydantic import AnyHttpUrl, BaseModel, PostgresDsn, validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AllergenConfig(BaseModel):
    """Allergen configuration with API mappings."""

    name: str
    keywords: list[str]
    api_mappings: dict[str, str]


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # Environment and API Settings
    ENVIRONMENT: Literal["development", "production", "test"] = "development"
    PROJECT_NAME: str = "Recipe Database API"
    API_V1_STR: str = "/api/v1"
    VERSION: str = "0.1.0"

    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 11520  # 8 days
    ALGORITHM: str = "HS256"

    # Database
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = "recipe_db"
    DATABASE_URL: PostgresDsn | None = None

    # CORS Origins as comma-separated string in .env
    BACKEND_CORS_ORIGINS: str = ""

    # Recipe API Keys
    SPOONACULAR_API_KEY: str
    EDAMAM_APP_ID: str
    EDAMAM_APP_KEY: str
    API_NINJAS_API_KEY: str
    TASTY_API_KEY: str

    # API Rate Limits
    SPOONACULAR_POINTS_PER_DAY: int = 150
    SPOONACULAR_REQUESTS_PER_MINUTE: int = 10
    EDAMAM_REQUESTS_PER_MINUTE: int = 10
    API_NINJAS_REQUESTS_PER_MINUTE: int = 10
    TASTY_REQUESTS_PER_MINUTE: int = 10

    # Cache Settings
    REDIS_URL: str = "redis://localhost"
    CACHE_TTL: int = 3600

    # Service Configuration
    MAX_CONCURRENT_REQUESTS: int = 5
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: Literal["json", "text"] = "json"
    LOG_FILE: str = "logs/recipe_service.log"
    MOCK_RESPONSES: bool = False
    MOCK_DELAY: int = 0
    DEFAULT_RECIPE_PROVIDER: str = "spoonacular"

    # User Management
    FIRST_SUPERUSER: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin"

    # Pydantic Config
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="allow")

    # Computed Properties and Validators
    @validator("DATABASE_URL", pre=True)
    def assemble_db_url(self, v: str | None, values: dict[str, Any]) -> Any:
        """Construct database URL from components if not provided directly."""
        if isinstance(v, str):
            return v

        password = quote_plus(values.get("POSTGRES_PASSWORD", ""))
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.get("POSTGRES_USER"),
            password=password,
            host=values.get("POSTGRES_HOST"),
            port=int(values.get("POSTGRES_PORT", 5432)),
            path=f"/{values.get('POSTGRES_DB', '')}",
        )

    @property
    def cors_origins(self) -> list[AnyHttpUrl]:
        """Get list of allowed CORS origins."""
        origins = self.BACKEND_CORS_ORIGINS.split(",")
        return [origin.strip() for origin in origins if origin.strip()]

    @property
    def allergens(self) -> list[AllergenConfig]:
        """Get list of configured allergens with API mappings."""
        return [
            AllergenConfig(
                name="dairy",
                keywords=["milk", "cream", "cheese", "butter", "yogurt", "casein", "whey"],
                api_mappings={"edamam": "dairy-free"},
            ),
            AllergenConfig(
                name="soy",
                keywords=["soy", "soya", "tofu", "tempeh", "miso", "edamame"],
                api_mappings={"edamam": "soy-free"},
            ),
            AllergenConfig(
                name="egg",
                keywords=["egg", "eggs", "albumin", "globulin", "lecithin", "livetin"],
                api_mappings={"edamam": "egg-free"},
            ),
        ]

    def get_allergen_keywords(self, allergen_name: str) -> list[str]:
        """Get keywords for a specific allergen."""
        for allergen in self.allergens:
            if allergen.name.lower() == allergen_name.lower():
                return allergen.keywords
        return []

    def get_allergen_api_param(self, allergen_name: str, api_name: str) -> str | None:
        """Get API-specific parameter for an allergen."""
        for allergen in self.allergens:
            if allergen.name.lower() == allergen_name.lower():
                return allergen.api_mappings.get(api_name.lower())
        return None


@lru_cache
def get_settings() -> Settings:
    """Get application settings singleton."""
    return Settings()


settings = get_settings()
