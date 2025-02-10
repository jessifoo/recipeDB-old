"""Schemas package.

This package contains Pydantic models used for request/response validation
and data serialization. Each schema defines the structure and validation
rules for API data.

Example:
    .. code-block:: python

        from app.schemas import RecipeCreate

        # Validate recipe data
        recipe_data = RecipeCreate(
            title="Spaghetti",
            prep_time_minutes=15,
            cook_time_minutes=20
        )
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.schemas.models import (
    Allergen,
    AllergenCreate,
    CookMethod,
    CookMethodCreate,
    CuisineType,
    CuisineTypeCreate,
    DietaryRestriction,
    DietaryRestrictionCreate,
    FamilyMember,
    FamilyMemberCreate,
    Ingredient,
    IngredientCreate,
    MealPlan,
    MealPlanCreate,
    MealType,
    MealTypeCreate,
    ProteinType,
    ProteinTypeCreate,
    Recipe,
    RecipeCreate,
)
from app.schemas.recipe import RecipeList, RecipeSearchFilter, RecipeSearchResult

if TYPE_CHECKING:
    from pydantic import BaseModel

    # Type hints for exported schemas
    Allergen: type[BaseModel]
    AllergenCreate: type[BaseModel]
    CookMethod: type[BaseModel]
    CookMethodCreate: type[BaseModel]
    CuisineType: type[BaseModel]
    CuisineTypeCreate: type[BaseModel]
    DietaryRestriction: type[BaseModel]
    DietaryRestrictionCreate: type[BaseModel]
    FamilyMember: type[BaseModel]
    FamilyMemberCreate: type[BaseModel]
    Ingredient: type[BaseModel]
    IngredientCreate: type[BaseModel]
    MealPlan: type[BaseModel]
    MealPlanCreate: type[BaseModel]
    MealType: type[BaseModel]
    MealTypeCreate: type[BaseModel]
    ProteinType: type[BaseModel]
    ProteinTypeCreate: type[BaseModel]
    Recipe: type[BaseModel]
    RecipeCreate: type[BaseModel]
    RecipeList: type[BaseModel]
    RecipeSearchFilter: type[BaseModel]
    RecipeSearchResult: type[BaseModel]

__version__ = "1.0.0"

__all__ = [
    "Allergen",
    "AllergenCreate",
    "CookMethod",
    "CookMethodCreate",
    "CuisineType",
    "CuisineTypeCreate",
    "DietaryRestriction",
    "DietaryRestrictionCreate",
    "FamilyMember",
    "FamilyMemberCreate",
    "Ingredient",
    "IngredientCreate",
    "MealPlan",
    "MealPlanCreate",
    "MealType",
    "MealTypeCreate",
    "ProteinType",
    "ProteinTypeCreate",
    "Recipe",
    "RecipeCreate",
    "RecipeList",
    "RecipeSearchFilter",
    "RecipeSearchResult",
]
