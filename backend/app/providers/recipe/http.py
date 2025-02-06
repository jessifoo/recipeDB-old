"""Base HTTP client for recipe providers."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import httpx
from pydantic import BaseModel

from app.providers.recipe.exceptions import RecipeNotFoundError, RecipeProviderError, RecipeProviderTimeout

if TYPE_CHECKING:
    from collections.abc import Mapping


class APIResponse(BaseModel):
    """API response wrapper."""

    status_code: int
    data: Any
    headers: Mapping[str, str]


class RecipeHTTPClient:
    """Base HTTP client for recipe providers."""

    def __init__(
        self,
        base_url: str,
        api_key: str | None = None,
        timeout: float = 30.0,
        headers: dict[str, str] | None = None,
    ) -> None:
        """Initialize the HTTP client.

        Args:
            base_url: Base URL for the API
            api_key: Optional API key
            timeout: Request timeout in seconds
            headers: Additional headers to include
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.headers = headers or {}
        self._client: httpx.AsyncClient | None = None

    @property
    def client(self) -> httpx.AsyncClient:
        """Get the HTTP client, creating it if necessary."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=self.timeout,
                headers=self.headers,
                follow_redirects=True,
            )
        return self._client

    async def get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
    ) -> APIResponse:
        """Make a GET request.

        Args:
            path: API endpoint path
            params: Query parameters

        Returns:
            Wrapped API response

        Raises:
            RecipeProviderError: On API errors
            RecipeNotFoundError: When resource doesn't exist
            RecipeProviderTimeout: On timeout
        """
        try:
            response = await self.client.get(
                path.lstrip("/"),
                params=params,
            )
            response.raise_for_status()

            return APIResponse(
                status_code=response.status_code,
                data=response.json(),
                headers=dict(response.headers),
            )

        except httpx.TimeoutException as e:
            raise RecipeProviderTimeout("Request timed out") from e

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise RecipeNotFoundError("Recipe not found") from e
            raise RecipeProviderError(
                f"API request failed: {e.response.text}",
                status_code=e.response.status_code,
            ) from e

        except httpx.HTTPError as e:
            raise RecipeProviderError(f"HTTP error: {e}") from e

        except Exception as e:
            raise RecipeProviderError(f"Unexpected error: {e}") from e

    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> RecipeHTTPClient:
        """Enter async context."""
        return self

    async def __aexit__(self, *_: Any) -> None:
        """Exit async context."""
        await self.close()
