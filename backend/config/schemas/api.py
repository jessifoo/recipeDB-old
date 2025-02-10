"""API configuration schemas.

This module defines Pydantic models for validating API configuration.
It preserves type safety while allowing configuration via YAML.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, HttpUrl

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import ConfigurationError


class APIEndpoint(BaseModel):
    """Configuration for an API endpoint.

    Attributes:
        name: Name of the API provider
        base_url: Base URL for the API
        timeout: Request timeout in seconds
        required_keys: Set of required API keys
        optional_keys: Set of optional API keys
        rate_limit: Maximum requests per minute
    """

    name: str
    base_url: HttpUrl
    timeout: int = Field(default=30, ge=1)
    required_keys: set[str]
    optional_keys: set[str] = Field(default_factory=set)
    rate_limit: int = Field(default=60, ge=1)

    def validate_keys(self, available_keys: dict[str, str | None]) -> None:
        """Validate that all required API keys are present.

        Args:
            available_keys: Dictionary of available API keys

        Raises:
            ConfigurationError: If any required keys are missing
        """
        missing = self.required_keys - set(available_keys.keys())
        if missing:
            raise ConfigurationError(
                message_template=ErrorMessages.CONFIG_MISSING_KEY,
                code=ErrorCode.CONFIGURATION_ERROR,
                details={"provider": self.name, "missing_keys": list(missing)},
            )


class APIConfig(BaseModel):
    """API configuration settings.

    Attributes:
        endpoints: Dictionary of API endpoint configurations
        cache_ttl: Cache time-to-live in seconds
        max_concurrent: Maximum concurrent API requests
        retry_attempts: Number of retry attempts for failed requests
        retry_delay: Delay between retries in seconds
    """

    endpoints: dict[str, APIEndpoint]
    cache_ttl: int = Field(default=3600, ge=1)
    max_concurrent: int = Field(default=5, ge=1)
    retry_attempts: int = Field(default=3, ge=0)
    retry_delay: float = Field(default=1.0, ge=0.1)

    def get_endpoint(self, name: str) -> APIEndpoint:
        """Get endpoint configuration by name.

        Args:
            name: Name of the API endpoint

        Returns:
            APIEndpoint configuration

        Raises:
            ConfigurationError: If endpoint doesn't exist
        """
        try:
            return self.endpoints[name]
        except KeyError:
            raise ConfigurationError(
                message_template=ErrorMessages.CONFIG_INVALID_VALUE,
                code=ErrorCode.CONFIGURATION_ERROR,
                details={"key": "api_endpoint", "value": name},
            )
