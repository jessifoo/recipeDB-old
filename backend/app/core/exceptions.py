"""Core exception handling for the application.

This module provides a comprehensive exception hierarchy for handling all types
of errors in the application. It includes base classes for different error
categories and utility functions for error handling.

Example:
    .. code-block:: python

        from app.core.exceptions import BusinessError
        from app.core.error_messages import ErrorMessages
        from app.core.error_codes import ErrorCode

        try:
            # Some business logic
            if invalid_state:
                raise BusinessError(
                    message_template=ErrorMessages.INVALID_STATE,
                    code=ErrorCode.INVALID_STATE,
                    details={"current": state, "allowed": valid_states}
                )
        except BusinessError as err:
            # Handle business rule violation
            logger.error(f"Business rule violated: {err.context.message}")

Note:
    All exceptions in this module inherit from DomainError, which provides
    a consistent interface for error handling and logging.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from fastapi import status

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessageTemplate, Language


@dataclass
class ErrorContext:
    """Structured context for errors.

    This class provides a standardized way to capture error context including
    the error code, message, and additional details for debugging.

    Attributes:
        code: Error code identifying the type of error
        message: Human-readable error message
        details: Additional context about the error
        original_error: Original exception that caused this error
        debug_info: Additional debugging information
    """

    code: ErrorCode
    message: str
    details: dict[str, Any]
    original_error: Exception | None = None
    debug_info: dict[str, Any] | None = None


class DomainError(Exception):
    """Base exception for all domain errors.

    This is the root of our exception hierarchy. All other exceptions
    should inherit from this class.

    Attributes:
        context: Error context containing code, message, and details
        status_code: HTTP status code to use when converting to response
    """

    status_code: ClassVar[int] = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(
        self,
        message_template: ErrorMessageTemplate,
        code: ErrorCode,
        details: dict[str, Any] | None = None,
        original_error: Exception | None = None,
        debug_info: dict[str, Any] | None = None,
        lang: Language = Language.EN,
        **kwargs: Any,
    ) -> None:
        """Initialize domain error.

        Args:
            message_template: Template for error message
            code: Error code
            details: Additional error details
            original_error: Original exception
            debug_info: Debug information
            lang: Message language
            **kwargs: Additional format parameters for message
        """
        self.context = ErrorContext(
            code=code,
            message=message_template.get_message(lang, **kwargs),
            details=details or {},
            original_error=original_error,
            debug_info=debug_info,
        )
        super().__init__(self.context.message)

    def to_dict(self) -> dict[str, Any]:
        """Convert error to dict for response.

        Returns:
            Dictionary representation of error
        """
        return {
            "code": self.context.code,
            "message": self.context.message,
            "details": self.context.details,
            "error_type": self.__class__.__name__,
        }


class ConfigurationError(DomainError):
    """Configuration-related errors.

    Raised when there are issues with application configuration.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


class AuthenticationError(DomainError):
    """Authentication-related errors.

    Raised when there are issues with user authentication.
    """

    status_code = status.HTTP_401_UNAUTHORIZED


class AuthorizationError(DomainError):
    """Authorization-related errors.

    Raised when user lacks permission for an operation.
    """

    status_code = status.HTTP_403_FORBIDDEN


class ResourceError(DomainError):
    """Base for resource-related errors.

    Provides common functionality for handling resource errors.
    """

    def __init__(
        self,
        resource_type: str,
        identifier: Any,
        message_template: ErrorMessageTemplate,
        code: ErrorCode,
        **kwargs: Any,
    ) -> None:
        """Initialize resource error.

        Args:
            resource_type: Type of resource (e.g., "Recipe", "Allergen")
            identifier: Resource identifier
            message_template: Template for error message
            code: Error code
            **kwargs: Additional parameters
        """
        details = {"resource_type": resource_type, "identifier": identifier, **kwargs.get("details", {})}
        super().__init__(message_template=message_template, code=code, details=details, **kwargs)


class ResourceNotFoundError(ResourceError):
    """Resource does not exist."""

    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, resource_type: str, identifier: Any, **kwargs: Any) -> None:
        """Initialize not found error.

        Args:
            resource_type: Type of resource
            identifier: Resource identifier
            **kwargs: Additional parameters
        """
        from app.core.error_messages import ErrorMessages

        super().__init__(
            resource_type=resource_type,
            identifier=identifier,
            message_template=ErrorMessages.RESOURCE_NOT_FOUND,
            code=ErrorCode.NOT_FOUND,
            **kwargs,
        )


class ResourceExistsError(ResourceError):
    """Resource already exists."""

    status_code = status.HTTP_409_CONFLICT

    def __init__(self, resource_type: str, identifier: Any, **kwargs: Any) -> None:
        """Initialize exists error.

        Args:
            resource_type: Type of resource
            identifier: Resource identifier
            **kwargs: Additional parameters
        """
        from app.core.error_messages import ErrorMessages

        super().__init__(
            resource_type=resource_type,
            identifier=identifier,
            message_template=ErrorMessages.RESOURCE_EXISTS,
            code=ErrorCode.ALREADY_EXISTS,
            **kwargs,
        )


class ResourceInUseError(ResourceError):
    """Resource is in use and cannot be modified/deleted."""

    status_code = status.HTTP_409_CONFLICT

    def __init__(self, resource_type: str, identifier: Any, **kwargs: Any) -> None:
        """Initialize in use error.

        Args:
            resource_type: Type of resource
            identifier: Resource identifier
            **kwargs: Additional parameters
        """
        from app.core.error_messages import ErrorMessages

        super().__init__(
            resource_type=resource_type,
            identifier=identifier,
            message_template=ErrorMessages.RESOURCE_IN_USE,
            code=ErrorCode.IN_USE,
            **kwargs,
        )


class DatabaseError(DomainError):
    """Database operation failed."""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    @classmethod
    def from_sqlalchemy(cls, error: Exception, operation: str | None = None, **kwargs: Any) -> DatabaseError:
        """Create from SQLAlchemy error.

        Args:
            error: Original SQLAlchemy error
            operation: Database operation that failed
            **kwargs: Additional parameters

        Returns:
            DatabaseError instance
        """
        from app.core.error_messages import ErrorMessages

        details = {"operation": operation, "error_type": error.__class__.__name__, **kwargs.get("details", {})}

        # Add debug info in development
        debug_info = {"sql": getattr(error, "statement", None), "params": getattr(error, "params", None)}

        return cls(
            message_template=ErrorMessages.DATABASE_ERROR,
            code=ErrorCode.DATABASE_ERROR,
            details=details,
            original_error=error,
            debug_info=debug_info,
            **kwargs,
        )


class ValidationError(DomainError):
    """Validation error."""

    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY


class BusinessError(DomainError):
    """Business rule violation."""

    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(
        self, message_template: ErrorMessageTemplate, code: ErrorCode = ErrorCode.BUSINESS_RULE_VIOLATION, **kwargs: Any
    ) -> None:
        """Initialize business error.

        Args:
            message_template: Template for error message
            code: Error code
            **kwargs: Additional parameters
        """
        super().__init__(message_template=message_template, code=code, **kwargs)


class ExternalServiceError(DomainError):
    """External service error."""

    status_code = status.HTTP_502_BAD_GATEWAY


class ServiceUnavailableError(ExternalServiceError):
    """Service is unavailable."""

    status_code = status.HTTP_503_SERVICE_UNAVAILABLE


class ServiceTimeoutError(ExternalServiceError):
    """Service request timed out."""

    status_code = status.HTTP_504_GATEWAY_TIMEOUT


class RateLimitError(ExternalServiceError):
    """Rate limit exceeded."""

    status_code = status.HTTP_429_TOO_MANY_REQUESTS


def get_status_code(error: DomainError) -> int:
    """Map error codes to HTTP status codes.

    Args:
        error: Domain error instance

    Returns:
        HTTP status code
    """
    return error.status_code


__version__ = "1.0.0"

__all__ = [
    "AuthenticationError",
    "AuthorizationError",
    "BusinessError",
    "ConfigurationError",
    "DatabaseError",
    "DomainError",
    "ErrorContext",
    "ExternalServiceError",
    "RateLimitError",
    "ResourceError",
    "ResourceExistsError",
    "ResourceInUseError",
    "ResourceNotFoundError",
    "ServiceTimeoutError",
    "ServiceUnavailableError",
    "ValidationError",
    "get_status_code",
]
