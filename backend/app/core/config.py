"""Application configuration.

This module provides a single source of truth for all application configuration,
combining settings from YAML files and environment variables.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseSettings, Field, validator
from pydantic_settings import SettingsConfigDict

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import ConfigurationError


class Settings(BaseSettings):
    """Application settings combining YAML config and environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=True)

    # Environment
    ENVIRONMENT: str = Field("development", description="Application environment")

    # Core settings loaded from YAML
    _config: dict[str, Any] = {}

    # Required environment variables (secrets, etc.)
    POSTGRES_PASSWORD: str = Field(..., description="PostgreSQL password")
    SECRET_KEY: str = Field(..., description="Secret key for JWT")
    SPOONACULAR_API_KEY: str = Field(..., description="Spoonacular API key")

    @validator("ENVIRONMENT")
    def validate_environment(self, v: str) -> str:
        """Validate environment name and load corresponding config."""
        if v not in {"development", "production", "test"}:
            raise ConfigurationError(
                message_template=ErrorMessages.CONFIG_INVALID_VALUE,
                code=ErrorCode.VALIDATION_ERROR,
                details={"environment": v},
            )
        return v

    def __init__(self, **kwargs: Any) -> None:
        """Initialize settings and load YAML config."""
        super().__init__(**kwargs)
        self._load_yaml_config()

    def _load_yaml_config(self) -> None:
        """Load configuration from YAML files."""
        try:
            config_dir = Path(__file__).parent.parent.parent / "config"

            # Load default config
            with (config_dir / "default.yaml").open() as f:
                self._config = yaml.safe_load(f)

            # Load environment overrides
            env_config = config_dir / f"{self.ENVIRONMENT}.yaml"
            if env_config.exists():
                with env_config.open() as f:
                    self._config.update(yaml.safe_load(f))

        except Exception as e:
            raise ConfigurationError(
                message_template=ErrorMessages.CONFIG_LOAD_FAILED,
                code=ErrorCode.CONFIGURATION_ERROR,
                details={"error": str(e)},
            )

    @property
    def allergens(self) -> list[dict[str, Any]]:
        """Get allergen configuration."""
        return self._config.get("allergens", [])

    @property
    def database_url(self) -> str:
        """Get database URL with credentials."""
        db_config = self._config.get("database", {})
        return (
            f"postgresql+asyncpg://{db_config.get('user')}:{self.POSTGRES_PASSWORD}"
            f"@{db_config.get('host')}/{db_config.get('name')}"
        )

    @property
    def api_config(self) -> dict[str, Any]:
        """Get API configuration."""
        return self._config.get("api", {})


@lru_cache
def get_settings() -> Settings:
    """Get application settings singleton.

    Returns:
        Settings: Application settings instance
    """
    return Settings()


settings = get_settings()
