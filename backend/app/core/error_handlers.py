"""FastAPI error handlers.

This module provides FastAPI exception handlers for converting domain errors
into HTTP responses. It includes handlers for all error types and provides
proper error logging.

Example:
    .. code-block:: python

        from fastapi import FastAPI
        from app.core.error_handlers import setup_error_handlers

        app = FastAPI()
        setup_error_handlers(app)

Note:
    The error handlers in this module are registered as FastAPI exception handlers
    and are not meant to be called directly. They are used by FastAPI's middleware
    to handle exceptions that occur during request processing.

Attributes:
    logger: Logger instance for error handling
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError as PydanticValidationError
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, DatabaseError, DomainError, ValidationError, get_status_code

if TYPE_CHECKING:
    from fastapi import FastAPI, Request

logger = logging.getLogger(__name__)


def setup_error_handlers(app: FastAPI) -> None:
    """Set up FastAPI error handlers.

    This function registers exception handlers for various error types
    and ensures proper error responses are returned.

    Args:
        app: FastAPI application instance

    Note:
        The handlers are registered using FastAPI's exception_handler decorator
        and are called automatically when exceptions occur during request processing.
    """

    @app.exception_handler(DomainError)  # type: ignore
    async def domain_error_handler(request: Request, error: DomainError) -> JSONResponse:  # type: ignore
        """Convert domain errors to HTTP responses.

        Args:
            request: FastAPI request
            error: Domain error instance

        Returns:
            JSON response with error details
        """
        # Log error with appropriate severity
        log_error(error, request)

        response_data = error.to_dict()

        # Add debug info in development environment
        if settings.FASTAPI_ENV == "development":
            if error.context.debug_info:
                response_data["debug"] = error.context.debug_info
            if error.context.original_error:
                response_data["debug"]["original_error"] = {
                    "type": error.context.original_error.__class__.__name__,
                    "message": str(error.context.original_error),
                }

        return JSONResponse(status_code=get_status_code(error), content=response_data)

    @app.exception_handler(RequestValidationError)  # type: ignore
    async def validation_error_handler(request: Request, error: RequestValidationError) -> JSONResponse:  # type: ignore
        """Handle FastAPI request validation errors.

        Args:
            request: FastAPI request
            error: Validation error

        Returns:
            JSON response with validation error details
        """
        logger.warning(f"Request validation failed: {error.errors()}")

        return JSONResponse(
            status_code=422,
            content={
                "code": ErrorCode.VALIDATION,
                "message": ErrorMessages.INVALID_DATA.get_message(
                    resource="request", details={"errors": error.errors()}
                ),
                "details": {"errors": error.errors()},
            },
        )

    @app.exception_handler(PydanticValidationError)  # type: ignore
    async def pydantic_validation_handler(request: Request, error: PydanticValidationError) -> JSONResponse:  # type: ignore
        """Handle Pydantic validation errors.

        Args:
            request: FastAPI request
            error: Validation error

        Returns:
            JSON response with validation error details
        """
        logger.warning(f"Pydantic validation failed: {error.errors()}")

        return JSONResponse(
            status_code=422,
            content={
                "code": ErrorCode.VALIDATION,
                "message": ErrorMessages.INVALID_DATA.get_message(resource="data", details={"errors": error.errors()}),
                "details": {"errors": error.errors()},
            },
        )

    @app.exception_handler(SQLAlchemyError)  # type: ignore
    async def db_error_handler(request: Request, error: SQLAlchemyError) -> JSONResponse:  # type: ignore
        """Handle unexpected SQLAlchemy errors.

        Args:
            request: FastAPI request
            error: SQLAlchemy error

        Returns:
            JSON response with database error details
        """
        db_error = DatabaseError.from_sqlalchemy(error=error)
        return await domain_error_handler(request, db_error)

    @app.exception_handler(Exception)  # type: ignore
    async def fallback_error_handler(request: Request, error: Exception) -> JSONResponse:  # type: ignore
        """Handle any unhandled exceptions.

        Args:
            request: FastAPI request
            error: Unhandled exception

        Returns:
            JSON response with error details
        """
        logger.exception("Unhandled exception occurred", exc_info=error)

        return JSONResponse(
            status_code=500,
            content={
                "code": ErrorCode.UNKNOWN,
                "message": ErrorMessages.UNKNOWN_ERROR.get_message(),
                "details": {"error": str(error)} if settings.FASTAPI_ENV == "development" else {},
            },
        )


def log_error(error: DomainError, request: Request) -> None:
    """Log error with appropriate severity level.

    Args:
        error: Domain error instance
        request: FastAPI request
    """
    # Determine log level based on error type and status code
    log_level = get_log_level(error)

    # Build log message
    log_msg = build_log_message(error, request)

    # Log with determined severity
    logger.log(log_level, log_msg, extra={"error_context": error.context})


def get_log_level(error: DomainError) -> int:
    """Determine appropriate log level for error.

    Args:
        error: Domain error instance

    Returns:
        Logging level to use
    """
    if isinstance(error, ValidationError | BusinessError):
        return logging.WARNING
    if get_status_code(error) >= 500:
        return logging.ERROR
    return logging.INFO


def build_log_message(error: DomainError, request: Request) -> str:
    """Build detailed log message for error.

    Args:
        error: Domain error instance
        request: FastAPI request

    Returns:
        Formatted log message
    """
    return (
        f"Error occurred processing {request.method} {request.url.path}\n"
        f"Error Type: {error.__class__.__name__}\n"
        f"Error Code: {error.context.code}\n"
        f"Message: {error.context.message}\n"
        f"Details: {error.context.details}"
    )


__version__ = "1.0.0"

__all__ = ["setup_error_handlers"]
