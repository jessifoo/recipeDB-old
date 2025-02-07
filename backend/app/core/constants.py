"""Application constants."""

from __future__ import annotations


class ErrorMessages:
    """Error message constants."""

    # Generic Errors
    UNKNOWN_ERROR = "An unknown error occurred"
    INTERNAL_ERROR = "Internal server error: {details}"

    # External Service Errors
    EXTERNAL_SERVICE_ERROR = "{service} API error: {details}"
    EXTERNAL_SERVICE_TIMEOUT = "Request to {service} timed out"
    EXTERNAL_SERVICE_UNAVAILABLE = "{service} is currently unavailable"
    RATE_LIMIT_EXCEEDED = "Rate limit exceeded for {service}"
    API_REQUEST_FAILED = "API request failed: {details}"
    HTTP_ERROR = "HTTP error: {details}"

    # Recipe Errors
    RECIPE_NOT_FOUND = "Recipe not found: {recipe_id}"
    RECIPE_SEARCH_FAILED = "Failed to search recipes: {details}"
    RECIPE_FETCH_FAILED = "Failed to get recipe: {details}"
    RECIPE_CONTAINS_ALLERGENS = "Recipe contains allergens"
    RECIPE_PROVIDER_INIT_FAILED = "Failed to initialize {provider} provider: {details}"
    RECIPE_ALREADY_EXISTS = "Recipe with this title already exists"
    RECIPE_IN_USE = "Cannot delete recipe that is referenced by meal plans"

    # Resource Not Found Errors
    ALLERGEN_NOT_FOUND = "Allergen not found"
    MEAL_TYPE_NOT_FOUND = "Meal type not found"
    INGREDIENT_NOT_FOUND = "Ingredient not found"
    CUISINE_TYPE_NOT_FOUND = "Cuisine type not found"
    DIETARY_RESTRICTION_NOT_FOUND = "Dietary restriction not found"
    FAMILY_MEMBER_NOT_FOUND = "Family member not found"
    PROTEIN_TYPE_NOT_FOUND = "Protein type not found"
    COOK_METHOD_NOT_FOUND = "Cook method not found"
    MEAL_PLAN_NOT_FOUND = "Meal plan not found"

    # Resource Already Exists Errors
    ALLERGEN_EXISTS = "Allergen with this name already exists"
    MEAL_TYPE_EXISTS = "Meal type with this name already exists"
    INGREDIENT_EXISTS = "Ingredient with this name already exists"
    CUISINE_TYPE_EXISTS = "Cuisine type with this name already exists"
    DIETARY_RESTRICTION_EXISTS = "Dietary restriction with this name already exists"
    FAMILY_MEMBER_EXISTS = "Family member with this name already exists"
    PROTEIN_TYPE_EXISTS = "Protein type with this name already exists"
    COOK_METHOD_EXISTS = "Cook method with this name already exists"
    MEAL_PLAN_EXISTS = "Meal plan with this name already exists"

    # Resource In Use Errors
    ALLERGEN_IN_USE = "Cannot delete allergen that is referenced by other records"
    MEAL_TYPE_IN_USE = "Cannot delete meal type that is referenced by recipes"
    INGREDIENT_IN_USE = "Cannot delete ingredient that is referenced by recipes"
    CUISINE_TYPE_IN_USE = "Cannot delete cuisine type that is referenced by recipes"
    DIETARY_RESTRICTION_IN_USE = "Cannot delete dietary restriction that is referenced by family members"
    FAMILY_MEMBER_IN_USE = "Cannot delete family member that has associated data"
    PROTEIN_TYPE_IN_USE = "Cannot delete protein type that is referenced by other records"
    COOK_METHOD_IN_USE = "Cannot delete cook method that is referenced by recipes"
    MEAL_PLAN_IN_USE = "Cannot delete meal plan that is referenced by other records"

    # Validation Errors
    INVALID_SEARCH_PARAMS = "Invalid search parameters"
    INVALID_RECIPE_ID = "Invalid recipe ID format"
    INVALID_DATA = "Invalid {resource} data"

    # Database Errors
    DATABASE_ERROR = "Database error: {details}"
    DATABASE_CONNECTION_ERROR = "Failed to connect to database: {details}"
    DATABASE_QUERY_ERROR = "Failed to execute query: {details}"

    # Authentication Errors
    UNAUTHORIZED = "Unauthorized access"
    FORBIDDEN = "Access forbidden"
    INVALID_CREDENTIALS = "Invalid credentials"
    TOKEN_EXPIRED = "Token has expired"
    INVALID_TOKEN = "Invalid token"

    # Configuration Errors
    CONFIG_ERROR = "Configuration error: {details}"
    CONFIG_MISSING_KEY = "Missing required configuration key: {key}"
    CONFIG_INVALID_VALUE = "Invalid configuration value for {key}: {details}"
