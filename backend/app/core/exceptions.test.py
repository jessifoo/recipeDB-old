from __future__ import annotations

import unittest
from http import HTTPStatus
from typing import Never

import pytest
from fastapi import status

from app.core.exceptions import (
    AppErrorDetail,
    AppHTTPException,
    ErrorCode,
    ExternalServiceTimeoutError,
    NotFoundError,
    ValidationError,
)


class TestExceptions(unittest.TestCase):
    def test_app_error_detail(self) -> None:
        detail = AppErrorDetail(ErrorCode.UNKNOWN_ERROR, "Test error", HTTPStatus.BAD_REQUEST, {"key": "value"})
        assert detail.code == ErrorCode.UNKNOWN_ERROR
        assert detail.message == "Test error"
        assert detail.status_code == HTTPStatus.BAD_REQUEST
        assert detail.details == {"key": "value"}
        assert detail.to_dict()["code"] == ErrorCode.UNKNOWN_ERROR

    def test_app_http_exception(self) -> Never:
        with pytest.raises(AppHTTPException) as context:
            msg = "Test message"
            raise AppHTTPException(
                msg, status.HTTP_400_BAD_REQUEST, {"X-Custom": "value"}, {"detail_key": "detail_value"}
            )
        assert context.exception.status_code == status.HTTP_400_BAD_REQUEST
        assert context.exception.detail == {"message": "Test message", "details": {"detail_key": "detail_value"}}
        assert context.exception.headers == {"X-Custom": "value"}

    def test_validation_error(self) -> Never:
        with pytest.raises(ValidationError) as context:
            msg = "Validation failed"
            raise ValidationError(msg, {"field": "invalid"})
        assert context.exception.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert context.exception.detail == {"message": "Validation failed", "details": {"field": "invalid"}}

    def test_not_found_error(self) -> Never:
        with pytest.raises(NotFoundError) as context:
            msg = "Resource not found"
            raise NotFoundError(msg, {"id": 123})
        assert context.exception.status_code == status.HTTP_404_NOT_FOUND
        assert context.exception.detail == {"message": "Resource not found", "details": {"id": 123}}

    def test_external_service_timeout_error(self) -> Never:
        with pytest.raises(ExternalServiceTimeoutError) as context:
            msg = "Timeout"
            raise ExternalServiceTimeoutError(msg, {"service": "test"})
        assert context.exception.status_code == status.HTTP_504_GATEWAY_TIMEOUT
        assert context.exception.detail == {"message": "Timeout", "details": {"service": "test"}}
