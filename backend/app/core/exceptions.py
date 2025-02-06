"""Core application exceptions."""

from __future__ import annotations


class ApplicationError(Exception):
    """Base class for application exceptions."""


class ConfigurationError(ApplicationError):
    """Raised when there is a configuration error."""


class ValidationError(ApplicationError):
    """Raised when validation fails."""


class AuthenticationError(ApplicationError):
    """Raised when authentication fails."""


class AuthorizationError(ApplicationError):
    """Raised when authorization fails."""
