"""API router registration."""

from __future__ import annotations

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

# Create the main API router
api_router = APIRouter(prefix="/api")

# Include all route modules
api_router.include_router(allergens_router)
api_router.include_router(cook_methods_router)
api_router.include_router(cuisine_types_router)
api_router.include_router(dietary_restrictions_router)
api_router.include_router(family_members_router)
api_router.include_router(ingredients_router)
api_router.include_router(meal_plans_router)
api_router.include_router(meal_types_router)
api_router.include_router(protein_types_router)
api_router.include_router(recipes_router)
api_router.include_router(recipe_search_router)
