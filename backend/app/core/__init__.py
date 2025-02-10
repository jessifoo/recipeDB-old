"""Core application components.

This package contains core application components like configuration,
error handling, and shared utilities.

Example:
    .. code-block:: python

        from app.core import Settings, ErrorCode, ConfigurationError
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, Final, TypeVar

from pydantic import BaseModel as PydanticBaseModel, Field as PydanticField, validator as PydanticValidator
from pydantic_settings import BaseSettings as PydanticBaseSettings, SettingsConfigDict as PydanticSettingsConfigDict

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages, ErrorMessageTemplate
from app.core.exceptions import ConfigurationError

# Type aliases for better IDE support and consistency
PydanticModel = PydanticBaseModel
PydanticField = PydanticField
PydanticValidator = PydanticValidator
PydanticSettings = PydanticBaseSettings
PydanticSettingsConfig = PydanticSettingsConfigDict

# Reusable type variables
T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

# Public API
__all__: Final[list[str]] = [
    # Core types
    "T",
    "T_co",
    "T_contra",
    "Callable",
    "Any",
    # Pydantic aliases
    "PydanticModel",
    "PydanticField",
    "PydanticValidator",
    "PydanticSettings",
    "PydanticSettingsConfig",
    # Error handling
    "ConfigurationError",
    "ErrorCode",
    "ErrorMessages",
    "ErrorMessageTemplate",
]

# Version
__version__: Final[str] = "1.0.0"
