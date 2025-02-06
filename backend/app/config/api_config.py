from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
from pydantic import BaseModel

from backend.app.core.config import ConfigurationError


class APIEndpoint(BaseModel):
    """Configuration for an API endpoint."""

    base_url: str
    timeout: int = 30
    required_keys: set[str]
    optional_keys: set[str] = set()


# Define API endpoints
ENDPOINTS: dict[str, APIEndpoint] = {
    "spoonacular": APIEndpoint(
        base_url="https://api.spoonacular.com",
        required_keys={"SPOONACULAR_API_KEY"},
    ),
    "edamam": APIEndpoint(
        base_url="https://api.edamam.com",
        required_keys={"EDAMAM_APP_ID", "EDAMAM_APP_KEY"},
    ),
    "api_ninjas": APIEndpoint(
        base_url="https://api.api-ninjas.com/v1",
        required_keys={"API_NINJAS_API_KEY"},
    ),
    "tasty": APIEndpoint(
        base_url="https://tasty.p.rapidapi.com",
        required_keys={"TASTY_API_KEY"},
    ),
}


class APIConfig(BaseModel):
    """API configuration settings."""

    dev_mode: bool = False
    cache_ttl: int = 3600
    max_concurrent_requests: int = 5

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        load_dotenv()
        self.dev_mode = os.getenv("FLASK_ENV") == "development"
        self.cache_ttl = int(os.getenv("CACHE_TTL", "3600"))
        max_requests: str = os.getenv("MAX_CONCURRENT_REQUESTS", "5")
        self.max_concurrent_requests = int(max_requests)
        self._validate_env_vars()

    def _validate_env_vars(self) -> None:
        """Validate that all required API keys are present in environment.

        Raises:
            ConfigurationError: If any required API keys are missing
        """
        missing_keys: list[str] = []
        for _endpoint_name, endpoint in ENDPOINTS.items():
            for key in endpoint.required_keys:
                env_key: str = key  # assumes the key in required_keys matches the env var
                if not os.getenv(env_key) and not self.dev_mode:
                    missing_keys.append(env_key)

        if missing_keys:
            missing_str: str = ", ".join(missing_keys)
            raise ConfigurationError(
                f"Missing required API keys: {missing_str}. Please set these environment variables.",
            )

    def get_endpoint(self, api_name: str) -> APIEndpoint:
        """Get endpoint configuration for an API."""
        if api_name not in ENDPOINTS:
            raise ConfigurationError(f"Unknown API: {api_name}")
        return ENDPOINTS[api_name]

    def get_api_key(self, api_name: str, key_name: str) -> str | None:
        """Get API key from environment."""
        api_key: str | None = os.getenv(key_name)
        if not api_key and not self.dev_mode:
            raise ConfigurationError(f"Missing API key for {api_name}. Please set {key_name} environment variable.")
        return api_key

    def get_required_keys(self) -> list[str]:
        """Get all required API keys.

        Returns:
            List of required API key names
        """
        missing_keys: list[str] = []
        for _endpoint_name, endpoint in ENDPOINTS.items():
            for key in endpoint.required_keys:
                env_key: str = key  # assumes the key in required_keys matches the env var
                if env_key not in missing_keys:
                    missing_keys.append(env_key)
        return missing_keys


# Global instance
ENDPOINTS = APIConfig()
