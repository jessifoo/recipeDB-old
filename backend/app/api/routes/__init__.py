"""API route handlers package."""

from __future__ import annotations

from app.api.routes.allergens import router as allergens
from app.api.routes.cook_methods import router as cook_methods
from app.api.routes.cuisine_types import router as cuisine_types
from app.api.routes.dietary_restrictions import router as dietary_restrictions
from app.api.routes.family_members import router as family_members
from app.api.routes.ingredients import router as ingredients
from app.api.routes.meal_plans import router as meal_plans
from app.api.routes.meal_types import router as meal_types
from app.api.routes.protein_types import router as protein_types
from app.api.routes.recipe_search import router as recipe_search
from app.api.routes.recipes import router as recipes

__all__ = [
    "allergens",
    "cook_methods",
    "cuisine_types",
    "dietary_restrictions",
    "family_members",
    "ingredients",
    "meal_plans",
    "meal_types",
    "protein_types",
    "recipe_search",
    "recipes",
]
