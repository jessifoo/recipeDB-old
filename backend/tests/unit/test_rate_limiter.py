"""Unit tests for rate limiter functionality"""

from __future__ import annotations

import time

import pytest

from app.services.rate_limiter import APIRateLimiter, RateLimitError


def test_rate_limiter_init():
    """Test rate limiter initialization"""
    limiter = APIRateLimiter("test_api")
    assert limiter.api_name == "test_api"
    assert len(limiter.windows) == 0


def test_add_limit():
    """Test adding rate limit window"""
    limiter = APIRateLimiter("test_api")
    limiter.add_limit("test_window", 2, 60)
    assert "test_window" in limiter.windows
    assert limiter.windows["test_window"].max_requests == 2
    assert limiter.windows["test_window"].window_seconds == 60


def test_rate_limit_not_exceeded():
    """Test requests within rate limit"""
    limiter = APIRateLimiter("test_api")
    limiter.add_limit("test_window", 2, 60)

    # Make two requests
    limiter.check_rate_limit()
    limiter.record_request()
    limiter.check_rate_limit()
    limiter.record_request()


def test_rate_limit_exceeded():
    """Test rate limit exceeded"""
    limiter = APIRateLimiter("test_api")
    limiter.add_limit("test_window", 2, 60)

    # Make two requests
    limiter.check_rate_limit()
    limiter.record_request()
    limiter.check_rate_limit()
    limiter.record_request()

    # Third request should fail
    with pytest.raises(RateLimitError) as exc_info:
        limiter.check_rate_limit()
    assert "Rate limit exceeded" in str(exc_info.value)
    assert exc_info.value.source == "test_api"


def test_window_cleanup():
    """Test old requests are cleaned up"""
    limiter = APIRateLimiter("test_api")
    window_seconds = 1
    limiter.add_limit("test_window", 2, window_seconds)

    # Make two requests
    limiter.check_rate_limit()
    limiter.record_request()
    limiter.check_rate_limit()
    limiter.record_request()

    # Wait for window to expire
    time.sleep(window_seconds + 0.1)

    # Should be able to make new requests
    limiter.check_rate_limit()
    limiter.record_request()


def test_multiple_windows():
    """Test multiple rate limit windows"""
    limiter = APIRateLimiter("test_api")
    limiter.add_limit("per_second", 2, 1)
    limiter.add_limit("per_minute", 5, 60)

    # Make requests within both limits
    for _ in range(2):
        limiter.check_rate_limit()
        limiter.record_request()

    # Third request should fail due to per_second limit
    with pytest.raises(RateLimitError) as exc_info:
        limiter.check_rate_limit()
    assert "Rate limit exceeded" in str(exc_info.value)


def test_retry_after():
    """Test retry_after calculation"""
    limiter = APIRateLimiter("test_api")
    window_seconds = 5
    limiter.add_limit("test_window", 1, window_seconds)

    # Make one request
    limiter.check_rate_limit()
    limiter.record_request()

    # Next request should fail with retry_after
    with pytest.raises(RateLimitError) as exc_info:
        limiter.check_rate_limit()
    assert exc_info.value.retry_after > 0
    assert exc_info.value.retry_after <= window_seconds
