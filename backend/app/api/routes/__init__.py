"""API route handlers package.

This package contains all the API route handlers for the application. Each module
provides a FastAPI router with endpoints for specific domain entities.

Available Routers:
    - allergens: Endpoints for managing allergen records
    - cook_methods: Endpoints for managing cooking methods
    - cuisine_types: Endpoints for managing cuisine types
    - dietary_restrictions: Endpoints for managing dietary restrictions
    - family_members: Endpoints for managing family members
    - ingredients: Endpoints for managing ingredients
    - meal_plans: Endpoints for managing meal plans
    - meal_types: Endpoints for managing meal types
    - protein_types: Endpoints for managing protein types
    - recipe_search: Endpoints for searching recipes
    - recipes: Endpoints for managing recipes

Example:
    .. code-block:: python

        from fastapi import FastAPI
        from app.api.routes import recipes

        app = FastAPI()
        app.include_router(recipes.router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

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

if TYPE_CHECKING:
    from fastapi import APIRouter

    # Type hints for exported routers
    allergens: APIRouter
    cook_methods: APIRouter
    cuisine_types: APIRouter
    dietary_restrictions: APIRouter
    family_members: APIRouter
    ingredients: APIRouter
    meal_plans: APIRouter
    meal_types: APIRouter
    protein_types: APIRouter
    recipe_search: APIRouter
    recipes: APIRouter

__version__ = "1.0.0"

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
