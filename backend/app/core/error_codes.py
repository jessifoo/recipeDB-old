"""Error codes for the application.

This module defines error codes that map to standard HTTP status codes where possible,
with additional specific codes for database, business rules, and integration errors.

Example:
    .. code-block:: python

        from app.core.error_codes import ErrorCode

        if not recipe:
            raise ResourceNotFoundError(
                resource_type="Recipe",
                identifier=recipe_id,
                code=ErrorCode.NOT_FOUND
            )

Note:
    Error codes are organized into ranges to maintain clarity and avoid conflicts:
    - 1-99: Standard HTTP-mapped errors
    - 100-199: Database errors
    - 200-299: Authentication/Authorization
    - 300-399: Business rules
    - 400-499: Integration/External services
    - 500-599: Recipe-specific errors
    - 600-699: Allergen-specific errors
    - 700-799: Validation errors
"""

from __future__ import annotations

from enum import IntEnum


class ErrorCode(IntEnum):
    """Application error codes aligned with HTTP status codes where possible.

    Attributes:
        BAD_REQUEST (int): Invalid request format or parameters (400)
        UNAUTHORIZED (int): Authentication required (401)
        FORBIDDEN (int): Permission denied (403)
        NOT_FOUND (int): Resource not found (404)
        CONFLICT (int): Resource conflict (409)
        UNPROCESSABLE (int): Validation failed (422)
        TOO_MANY_REQUESTS (int): Rate limit exceeded (429)
        INTERNAL_ERROR (int): Server error (500)
        SERVICE_UNAVAILABLE (int): Service unavailable (503)
        UNKNOWN (int): Unknown error (500)
    """

    # Standard HTTP-Mapped Errors (1-99)
    BAD_REQUEST = 1  # 400
    UNAUTHORIZED = 2  # 401
    FORBIDDEN = 3  # 403
    NOT_FOUND = 4  # 404
    CONFLICT = 5  # 409
    UNPROCESSABLE = 6  # 422
    TOO_MANY_REQUESTS = 7  # 429
    INTERNAL_ERROR = 8  # 500
    SERVICE_UNAVAILABLE = 9  # 503
    UNKNOWN = 10  # 500
    ALREADY_EXISTS = 11  # 409
    IN_USE = 12  # 409
    BUSINESS_RULE_VIOLATION = 13  # 400

    # Database Errors (100-199)
    DATABASE_ERROR = 100
    DATABASE_CONNECTION_ERROR = 101
    DATABASE_CONSTRAINT = 102
    DATABASE_DEADLOCK = 103
    DATABASE_TIMEOUT = 104
    DATABASE_STALE_DATA = 105

    # Authentication/Authorization (200-299)
    TOKEN_EXPIRED = 200
    TOKEN_INVALID = 201
    TOKEN_MISSING = 202
    INSUFFICIENT_PERMISSIONS = 203
    SESSION_EXPIRED = 204

    # Business Rules (300-399)
    VALIDATION_ERROR = 300
    INVALID_STATE = 301
    RESOURCE_LOCKED = 302
    RESOURCE_IN_USE = 303
    ALLERGEN_CONFLICT = 304
    RECIPE_IN_MEALPLAN = 305
    DUPLICATE_ENTRY = 306
    INVALID_OPERATION = 307

    # Integration/External (400-499)
    EXTERNAL_SERVICE_ERROR = 400
    EXTERNAL_SERVICE_TIMEOUT = 401
    EXTERNAL_SERVICE_UNAVAILABLE = 402
    API_ERROR = 403
    API_TIMEOUT = 404
    API_RATE_LIMIT = 405
    API_RESPONSE_INVALID = 406

    # Recipe-specific errors (500-599)
    RECIPE_EXISTS = 500
    RECIPE_NOT_FOUND = 501
    RECIPE_IN_USE = 502
    RECIPE_INVALID = 503
    RECIPE_ALLERGEN_CONFLICT = 504

    # Allergen-specific errors (600-699)
    ALLERGEN_EXISTS = 600
    ALLERGEN_NOT_FOUND = 601
    ALLERGEN_IN_USE = 602
    ALLERGEN_INVALID = 603

    # Validation errors (700-799)
    VALIDATION = 700
    VALIDATION_MISSING_FIELD = 701
    VALIDATION_INVALID_TYPE = 702
    VALIDATION_CONSTRAINT = 703

    @property
    def http_status_code(self) -> int:
        """Map error code to HTTP status code.

        Returns:
            int: Corresponding HTTP status code
        """
        if self == self.BAD_REQUEST:
            return 400
        elif self == self.UNAUTHORIZED:
            return 401
        elif self == self.FORBIDDEN:
            return 403
        elif self == self.NOT_FOUND:
            return 404
        elif self == self.CONFLICT:
            return 409
        elif self == self.UNPROCESSABLE:
            return 422
        elif self == self.TOO_MANY_REQUESTS:
            return 429
        elif self == self.SERVICE_UNAVAILABLE:
            return 503
        elif self in (self.TOKEN_EXPIRED, self.TOKEN_INVALID) or self == self.TOKEN_MISSING:
            return 401
        elif self == self.INSUFFICIENT_PERMISSIONS:
            return 403
        elif self == self.SESSION_EXPIRED:
            return 401
        elif self == self.API_RATE_LIMIT:
            return 429
        elif self == self.EXTERNAL_SERVICE_UNAVAILABLE:
            return 503
        # Default to 500 for unknown/internal errors
        return 500

    @property
    def is_retryable(self) -> bool:
        """Indicate if operation can be retried.

        Returns:
            bool: True if the error is transient and the operation can be retried
        """
        return self in {
            self.DATABASE_DEADLOCK,
            self.DATABASE_TIMEOUT,
            self.DATABASE_CONNECTION_ERROR,
            self.EXTERNAL_SERVICE_TIMEOUT,
            self.EXTERNAL_SERVICE_UNAVAILABLE,
            self.API_TIMEOUT,
            self.API_RATE_LIMIT,
            self.SERVICE_UNAVAILABLE,
        }

    @property
    def is_client_error(self) -> bool:
        """Indicate if error was caused by client.

        Returns:
            bool: True if the error was caused by client input or request
        """
        return self.http_status_code < 500

    @property
    def should_log_error(self) -> bool:
        """Indicate if error should be logged at ERROR level.

        Returns:
            bool: True if the error should be logged at ERROR level
        """
        return not self.is_client_error or self in {
            self.DATABASE_ERROR,
            self.DATABASE_CONSTRAINT,
            self.DATABASE_DEADLOCK,
            self.EXTERNAL_SERVICE_ERROR,
            self.API_ERROR,
        }


__version__ = "1.0.0"

__all__ = ["ErrorCode"]
