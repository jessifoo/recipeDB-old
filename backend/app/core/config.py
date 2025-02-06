"""Application configuration."""

from __future__ import annotations

from functools import lru_cache
from typing import TYPE_CHECKING

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

if TYPE_CHECKING:
    from pydantic import ValidationInfo


class ConfigurationError(Exception):
    """Raised when there is a configuration error."""


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    # FastAPI
    FASTAPI_ENV: str = Field("development", description="FastAPI environment (development/production)")
    SECRET_KEY: str = Field("dev_secret_key", description="Secret key for JWT token generation")
    PROJECT_NAME: str = Field("Recipe Database API", description="Project name")
    API_V1_STR: str = Field("/api/v1", description="API version 1 prefix")
    BACKEND_CORS_ORIGINS: list[str] = Field(
        default_factory=lambda: ["http://localhost:3000"],
        description="List of origins that are allowed to make cross-site HTTP requests",
    )

    # Database
    POSTGRES_SERVER: str = Field("localhost", description="PostgreSQL server hostname")
    POSTGRES_USER: str = Field("postgres", description="PostgreSQL username")
    POSTGRES_PASSWORD: str = Field("password", description="PostgreSQL password")
    POSTGRES_DB: str = Field("recipe_db", description="PostgreSQL database name")
    SQLALCHEMY_DATABASE_URI: str | None = None

    # Redis
    REDIS_URL: str = Field("redis://localhost", description="Redis URL")

    # Logging
    LOG_LEVEL: str = Field("INFO", description="Logging level")

    # External APIs
    SPOONACULAR_API_KEY: str = Field("dummy_key", description="Spoonacular API key")
    EDAMAM_APP_ID: str = Field("dummy_id", description="Edamam API app ID")
    EDAMAM_APP_KEY: str = Field("dummy_key", description="Edamam API key")
    API_NINJAS_API_KEY: str = Field("dummy_key", description="API Ninjas API key")
    TASTY_API_KEY: str = Field("dummy_key", description="Tasty API key")

    # Recipe Provider Settings
    DEFAULT_RECIPE_PROVIDER: str = Field("local", description="Default recipe provider to use")
    ENABLE_EXTERNAL_PROVIDERS: bool = Field(False, description="Enable external recipe providers")

    # Users
    FIRST_SUPERUSER: str = Field("admin@example.com", description="First superuser email")
    FIRST_SUPERUSER_PASSWORD: str = Field("admin", description="First superuser password")

    @property
    def database_url(self) -> str | None:
        """Get the database URL."""
        return self.SQLALCHEMY_DATABASE_URI

    def assemble_db_connection(
        self,
        v: str | None,
        info: ValidationInfo,
    ) -> str | None:
        """Assemble database connection URL.

        Args:
            v: Current value
            info: Validation context

        Returns:
            Assembled database URL
        """
        if isinstance(v, str):
            return v

        values = info.data
        return f"postgresql+asyncpg://{values.get('POSTGRES_USER')}:{values.get('POSTGRES_PASSWORD')}@{values.get('POSTGRES_SERVER')}/{values.get('POSTGRES_DB')}"

    def assemble_cors_origins(
        self,
        v: str | list[str] | None,
        info: ValidationInfo,
    ) -> list[str]:
        """Assemble CORS origins.

        Args:
            v: Current value
            info: Validation context

        Returns:
            List of CORS origins
        """
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        if isinstance(v, list):
            return v
        return []


@lru_cache
def get_settings() -> Settings:
    """Get application settings.

    Returns:
        Application settings
    """
    return Settings()


settings = get_settings()
