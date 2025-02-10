"""API router registration.

This module provides the main API router that combines all route modules
into a single FastAPI router. It handles the registration and organization
of all API endpoints.

Example:
    .. code-block:: python

        from fastapi import FastAPI
        from app.api import api_router

        app = FastAPI()
        app.include_router(api_router)
"""

from __future__ import annotations

from typing import Final

from fastapi import APIRouter

from app.api.routes.allergens import router as allergens_router
from app.api.routes.cook_methods import router as cook_methods_router
from app.api.routes.cuisine_types import router as cuisine_types_router
from app.api.routes.dietary_restrictions import router as dietary_restrictions_router
from app.api.routes.family_members import router as family_members_router
from app.api.routes.ingredients import router as ingredients_router
from app.api.routes.meal_plans import router as meal_plans_router
from app.api.routes.meal_types import router as meal_types_router
from app.api.routes.protein_types import router as protein_types_router
from app.api.routes.recipe_search import router as recipe_search_router
from app.api.routes.recipes import router as recipes_router

# Package version
__version__: Final[str] = "1.0.0"

# Create the main API router
api_router: Final[APIRouter] = APIRouter(prefix="/api")

# Include all route modules
api_router.include_router(allergens_router, prefix="/allergens", tags=["allergens"])
api_router.include_router(cook_methods_router, prefix="/cook-methods", tags=["cook-methods"])
api_router.include_router(cuisine_types_router, prefix="/cuisine-types", tags=["cuisine-types"])
api_router.include_router(dietary_restrictions_router, prefix="/dietary-restrictions", tags=["dietary-restrictions"])
api_router.include_router(family_members_router, prefix="/family-members", tags=["family-members"])
api_router.include_router(ingredients_router, prefix="/ingredients", tags=["ingredients"])
api_router.include_router(meal_plans_router, prefix="/meal-plans", tags=["meal-plans"])
api_router.include_router(meal_types_router, prefix="/meal-types", tags=["meal-types"])
api_router.include_router(protein_types_router, prefix="/protein-types", tags=["protein-types"])
api_router.include_router(recipe_search_router, prefix="/recipe-search", tags=["recipe-search"])
api_router.include_router(recipes_router, prefix="/recipes", tags=["recipes"])

# Public API
__all__: Final[list[str]] = ["api_router", "__version__"]
