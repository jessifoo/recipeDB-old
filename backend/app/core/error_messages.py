"""Error message constants."""

from __future__ import annotations

# External Service Errors
EXTERNAL_SERVICE_ERROR = "External service error: {details}"
EXTERNAL_SERVICE_TIMEOUT = "External service timed out"
EXTERNAL_SERVICE_UNAVAILABLE = "External service is unavailable"
RATE_LIMIT_EXCEEDED = "Rate limit exceeded"

# Recipe Provider Errors
RECIPE_PROVIDER_ERROR = "Recipe provider error: {details}"
RECIPE_NOT_FOUND = "Recipe not found: {recipe_id}"
RECIPE_SEARCH_FAILED = "Failed to search recipes: {details}"
RECIPE_FETCH_FAILED = "Failed to get recipe: {details}"
RECIPE_CONTAINS_ALLERGENS = "Recipe contains allergens"
RECIPE_VALIDATION_FAILED = "Recipe validation failed: {details}"
RECIPE_PROVIDER_DISABLED = "External recipe providers are disabled"
RECIPE_PROVIDER_UNKNOWN = "Unknown recipe provider: {provider}"
RECIPE_PROVIDER_INIT_FAILED = "Failed to initialize {provider} provider: {details}"

# Database Errors
DATABASE_ERROR = "Database error: {details}"
DATABASE_CONNECTION_ERROR = "Failed to connect to database: {details}"
DATABASE_QUERY_ERROR = "Failed to execute query: {details}"
DATABASE_NOT_CONFIGURED = "Database URI is not configured"

# Configuration Errors
CONFIG_ERROR = "Configuration error: {details}"
CONFIG_MISSING_KEY = "Missing required configuration key: {key}"
CONFIG_INVALID_VALUE = "Invalid configuration value for {key}: {details}"
CONFIG_MISSING_API_KEY = "Missing API key for {service}. Please set {key} environment variable"

# Validation Errors
VALIDATION_ERROR = "Validation error: {details}"
VALIDATION_REQUIRED_FIELD = "Required field missing: {field}"
VALIDATION_INVALID_VALUE = "Invalid value for {field}: {details}"

# Authentication Errors
AUTH_ERROR = "Authentication error: {details}"
AUTH_INVALID_CREDENTIALS = "Invalid credentials"
AUTH_TOKEN_EXPIRED = "Token has expired"
AUTH_TOKEN_INVALID = "Invalid token"
AUTH_INSUFFICIENT_PERMISSIONS = "Insufficient permissions"

# Generic Errors
NOT_FOUND = "Resource not found: {resource}"
ALREADY_EXISTS = "Resource already exists: {resource}"
INVALID_REQUEST = "Invalid request: {details}"
