from __future__ import annotations

import unittest
from http import HTTPStatus

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
    def test_app_error_detail(self):
        detail = AppErrorDetail(ErrorCode.UNKNOWN_ERROR, "Test error", HTTPStatus.BAD_REQUEST, {"key": "value"})
        self.assertEqual(detail.code, ErrorCode.UNKNOWN_ERROR)
        self.assertEqual(detail.message, "Test error")
        self.assertEqual(detail.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(detail.details, {"key": "value"})
        self.assertEqual(detail.to_dict()["code"], ErrorCode.UNKNOWN_ERROR)

    def test_app_http_exception(self):
        with self.assertRaises(AppHTTPException) as context:
            raise AppHTTPException(
                "Test message", status.HTTP_400_BAD_REQUEST, {"X-Custom": "value"}, {"detail_key": "detail_value"}
            )
        self.assertEqual(context.exception.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            context.exception.detail, {"message": "Test message", "details": {"detail_key": "detail_value"}}
        )
        self.assertEqual(context.exception.headers, {"X-Custom": "value"})

    def test_validation_error(self):
        with self.assertRaises(ValidationError) as context:
            raise ValidationError("Validation failed", {"field": "invalid"})
        self.assertEqual(context.exception.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(context.exception.detail, {"message": "Validation failed", "details": {"field": "invalid"}})

    def test_not_found_error(self):
        with self.assertRaises(NotFoundError) as context:
            raise NotFoundError("Resource not found", {"id": 123})
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(context.exception.detail, {"message": "Resource not found", "details": {"id": 123}})

    def test_external_service_timeout_error(self):
        with self.assertRaises(ExternalServiceTimeoutError) as context:
            raise ExternalServiceTimeoutError("Timeout", {"service": "test"})
        self.assertEqual(context.exception.status_code, status.HTTP_504_GATEWAY_TIMEOUT)
        self.assertEqual(context.exception.detail, {"message": "Timeout", "details": {"service": "test"}})
