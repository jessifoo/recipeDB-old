"""Models package.

This package contains SQLAlchemy models that represent database tables
and their relationships. Each model maps to a specific table and defines
its structure and behavior.

Example:
    .. code-block:: python

        from app.models import Recipe

        # Create a new recipe
        recipe = Recipe(title="Spaghetti", prep_time_minutes=15)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.models.models import (
    Allergen,
    CookMethod,
    CuisineType,
    DietaryRestriction,
    FamilyMember,
    Ingredient,
    MealPlan,
    MealType,
    ProteinType,
    Recipe,
)

if TYPE_CHECKING:
    from sqlalchemy.orm import DeclarativeBase

    # Type hints for exported models
    Allergen: type[DeclarativeBase]
    CookMethod: type[DeclarativeBase]
    CuisineType: type[DeclarativeBase]
    DietaryRestriction: type[DeclarativeBase]
    FamilyMember: type[DeclarativeBase]
    Ingredient: type[DeclarativeBase]
    MealPlan: type[DeclarativeBase]
    MealType: type[DeclarativeBase]
    ProteinType: type[DeclarativeBase]
    Recipe: type[DeclarativeBase]

__version__ = "1.0.0"

__all__ = [
    "Allergen",
    "CookMethod",
    "CuisineType",
    "DietaryRestriction",
    "FamilyMember",
    "Ingredient",
    "MealPlan",
    "MealType",
    "ProteinType",
    "Recipe",
]
