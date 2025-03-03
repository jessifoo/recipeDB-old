"""Error message templates with i18n support.

This module provides a centralized location for all error message templates
with support for internationalization (i18n). Messages are organized by
domain and support multiple languages.

Example:
    .. code-block:: python

        from app.core.error_messages import ErrorMessages, Language

        msg = ErrorMessages.RESOURCE_NOT_FOUND.get_message(
            lang=Language.EN,
            resource_type="Recipe",
            identifier="123"
        )
"""

from __future__ import annotations

import gettext
from dataclasses import dataclass
from enum import Enum
from typing import Any


class Language(str, Enum):
    """Supported languages for error messages."""

    EN = "en"  # English
    ES = "es"  # Spanish


@dataclass
class ErrorMessageTemplate:
    """Template for error messages with translations.

    Attributes:
        key: Unique identifier for the message template
        en: English version of the message
        es: Spanish version of the message (optional)
    """

    key: str
    en: str
    es: str = ""

    def get_message(self, lang: Language = Language.EN, **kwargs: Any) -> str:
        """Get message in specified language with formatting.

        Args:
            lang: Target language for the message
            **kwargs: Format parameters for the message template

        Returns:
            Formatted message in the specified language
        """
        template = getattr(self, lang.value, self.en)
        return template.format(**kwargs)


class ErrorMessages:
    """Centralized error message templates.

    This class organizes error messages by domain and provides templates
    for all possible error scenarios in the application.
    """

    # Generic System Errors (1-999)
    UNKNOWN_ERROR = ErrorMessageTemplate(
        key="unknown_error", en="An unexpected error occurred", es="Se produjo un error inesperado"
    )
    INTERNAL_ERROR = ErrorMessageTemplate(
        key="internal_error", en="Internal server error: {details}", es="Error interno del servidor: {details}"
    )
    CONFIG_ERROR = ErrorMessageTemplate(
        key="config_error", en="Configuration error: {details}", es="Error de configuración: {details}"
    )
    CONFIG_MISSING_KEY = ErrorMessageTemplate(
        key="config_missing_key",
        en="Missing required configuration key: {key}",
        es="Falta la clave de configuración requerida: {key}",
    )
    CONFIG_INVALID_VALUE = ErrorMessageTemplate(
        key="config_invalid_value",
        en="Invalid configuration value for {key}: {details}",
        es="Valor de configuración inválido para {key}: {details}",
    )

    # Authentication/Authorization Errors (1000-1999)
    UNAUTHORIZED = ErrorMessageTemplate(key="unauthorized", en="Unauthorized access", es="Acceso no autorizado")
    FORBIDDEN = ErrorMessageTemplate(key="forbidden", en="Access forbidden", es="Acceso prohibido")
    INVALID_CREDENTIALS = ErrorMessageTemplate(
        key="invalid_credentials", en="Invalid credentials", es="Credenciales inválidas"
    )
    TOKEN_EXPIRED = ErrorMessageTemplate(key="token_expired", en="Token has expired", es="El token ha expirado")
    INVALID_TOKEN = ErrorMessageTemplate(key="invalid_token", en="Invalid token", es="Token inválido")

    # Resource Errors (2000-2999)
    RESOURCE_NOT_FOUND = ErrorMessageTemplate(
        key="resource_not_found",
        en="{resource_type} not found: {identifier}",
        es="{resource_type} no encontrado: {identifier}",
    )
    RESOURCE_EXISTS = ErrorMessageTemplate(
        key="resource_exists",
        en="{resource_type} already exists: {identifier}",
        es="{resource_type} ya existe: {identifier}",
    )
    RESOURCE_IN_USE = ErrorMessageTemplate(
        key="resource_in_use",
        en="{resource_type} is in use and cannot be modified: {identifier}",
        es="{resource_type} está en uso y no se puede modificar: {identifier}",
    )

    # Database Errors (3000-3999)
    DATABASE_ERROR = ErrorMessageTemplate(
        key="database_error",
        en="Database operation failed: {details}",
        es="Error en la operación de base de datos: {details}",
    )
    DATABASE_CONNECTION_ERROR = ErrorMessageTemplate(
        key="database_connection_error",
        en="Failed to connect to database: {details}",
        es="Error al conectar con la base de datos: {details}",
    )
    DATABASE_QUERY_ERROR = ErrorMessageTemplate(
        key="database_query_error",
        en="Failed to execute query: {details}",
        es="Error al ejecutar la consulta: {details}",
    )

    # External Service Errors (4000-4999)
    EXTERNAL_SERVICE_ERROR = ErrorMessageTemplate(
        key="external_service_error", en="{service} API error: {details}", es="Error en la API de {service}: {details}"
    )
    EXTERNAL_SERVICE_TIMEOUT = ErrorMessageTemplate(
        key="external_service_timeout",
        en="Request to {service} timed out",
        es="Tiempo de espera agotado para {service}",
    )
    EXTERNAL_SERVICE_UNAVAILABLE = ErrorMessageTemplate(
        key="external_service_unavailable",
        en="{service} is currently unavailable",
        es="{service} no está disponible actualmente",
    )
    RATE_LIMIT_EXCEEDED = ErrorMessageTemplate(
        key="rate_limit_exceeded",
        en="Rate limit exceeded for {service}",
        es="Límite de velocidad excedido para {service}",
    )

    # Recipe Domain Errors (5000-5999)
    RECIPE_NOT_FOUND = ErrorMessageTemplate(
        key="recipe_not_found", en="Recipe not found: {identifier}", es="Receta no encontrada: {identifier}"
    )
    RECIPE_EXISTS = ErrorMessageTemplate(
        key="recipe_exists",
        en="Recipe with title '{title}' already exists",
        es="Ya existe una receta con el título '{title}'",
    )
    RECIPE_IN_USE = ErrorMessageTemplate(
        key="recipe_in_use",
        en="Cannot delete recipe that is referenced by meal plans",
        es="No se puede eliminar la receta porque está siendo utilizada en planes de comida",
    )
    RECIPE_CONTAINS_ALLERGENS = ErrorMessageTemplate(
        key="recipe_contains_allergens",
        en="Recipe contains allergens: {allergens}",
        es="La receta contiene alérgenos: {allergens}",
    )
    RECIPE_SEARCH_FAILED = ErrorMessageTemplate(
        key="recipe_search_failed", en="Failed to search recipes: {details}", es="Error al buscar recetas: {details}"
    )
    RECIPE_FETCH_FAILED = ErrorMessageTemplate(
        key="recipe_fetch_failed", en="Failed to get recipe: {details}", es="Error al obtener la receta: {details}"
    )
    RECIPE_PROVIDER_INIT_FAILED = ErrorMessageTemplate(
        key="recipe_provider_init_failed",
        en="Failed to initialize {provider} provider: {details}",
        es="Error al inicializar el proveedor {provider}: {details}",
    )

    # Validation Errors (6000-6999)
    INVALID_SEARCH_PARAMS = ErrorMessageTemplate(
        key="invalid_search_params",
        en="Invalid search parameters: {details}",
        es="Parámetros de búsqueda inválidos: {details}",
    )
    INVALID_RECIPE_ID = ErrorMessageTemplate(
        key="invalid_recipe_id",
        en="Invalid recipe ID format: {details}",
        es="Formato de ID de receta inválido: {details}",
    )
    INVALID_DATA = ErrorMessageTemplate(
        key="invalid_data", en="Invalid {resource} data: {details}", es="Datos inválidos para {resource}: {details}"
    )
    INVALID_FILTER_PARAMS = ErrorMessageTemplate(
        key="invalid_filter_params",
        en="Invalid filter parameters: {details}",
        es="Parámetros de filtro inválidos: {details}",
    )
    OPERATION_NOT_SUPPORTED = ErrorMessageTemplate(
        key="operation_not_supported",
        en="Operation '{operation}' is not supported by {provider}: {reason}",
        es="La operación '{operation}' no está soportada por {provider}: {reason}",
    )
    INVALID_OPERATION = ErrorMessageTemplate(
        key="invalid_operation", en="Invalid operation: {details}", es="Operación inválida: {details}"
    )

    # Business Rule Errors (7000-7999)
    BUSINESS_RULE_VIOLATION = ErrorMessageTemplate(
        key="business_rule_violation",
        en="Business rule violation: {details}",
        es="Violación de regla de negocio: {details}",
    )
    INVALID_STATE = ErrorMessageTemplate(
        key="invalid_state", en="Invalid state: {details}", es="Estado inválido: {details}"
    )

    # Entity-Specific Errors (8000-8999)
    ALLERGEN_NOT_FOUND = ErrorMessageTemplate(
        key="allergen_not_found", en="Allergen not found: {identifier}", es="Alérgeno no encontrado: {identifier}"
    )
    ALLERGEN_EXISTS = ErrorMessageTemplate(
        key="allergen_exists",
        en="Allergen with name '{name}' already exists",
        es="Ya existe un alérgeno con el nombre '{name}'",
    )
    ALLERGEN_IN_USE = ErrorMessageTemplate(
        key="allergen_in_use",
        en="Cannot delete allergen '{name}' as it is referenced by recipes",
        es="No se puede eliminar el alérgeno '{name}' porque está siendo utilizado por recetas",
    )
    MEAL_TYPE_NOT_FOUND = ErrorMessageTemplate(
        key="meal_type_not_found",
        en="Meal type not found: {identifier}",
        es="Tipo de comida no encontrado: {identifier}",
    )
    MEAL_TYPE_EXISTS = ErrorMessageTemplate(
        key="meal_type_exists",
        en="Meal type with name '{name}' already exists",
        es="Ya existe un tipo de comida con el nombre '{name}'",
    )
    MEAL_TYPE_IN_USE = ErrorMessageTemplate(
        key="meal_type_in_use",
        en="Cannot delete meal type that is referenced by recipes",
        es="No se puede eliminar el tipo de comida porque está siendo utilizado por recetas",
    )

    @classmethod
    def setup_translations(cls, locale_dir: str) -> None:
        """Set up translations for the application.

        Args:
            locale_dir: Directory containing translation files
        """
        for lang in Language:
            try:
                translations = gettext.translation("messages", localedir=locale_dir, languages=[lang.value])
                translations.install()
            except FileNotFoundError:
                # Fallback to null translations if files not found
                gettext.NullTranslations().install()


__version__ = "1.0.0"

__all__ = ["ErrorMessageTemplate", "ErrorMessages", "Language"]
