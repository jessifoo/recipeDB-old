"""API route handlers package."""

from __future__ import annotations

from backend.app.api.routes.allergens import router as allergens
from backend.app.api.routes.cook_methods import router as cook_methods
from backend.app.api.routes.cuisine_types import router as cuisine_types
from backend.app.api.routes.dietary_restrictions import router as dietary_restrictions
from backend.app.api.routes.family_members import router as family_members
from backend.app.api.routes.ingredients import router as ingredients
from backend.app.api.routes.meal_plans import router as meal_plans
from backend.app.api.routes.meal_types import router as meal_types
from backend.app.api.routes.protein_types import router as protein_types
from backend.app.api.routes.recipe_search import router as recipe_search
from backend.app.api.routes.recipes import router as recipes

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
