"""Common constants used across the application."""

# Error Messages
from __future__ import annotations

ALLERGEN_NOT_FOUND = "Allergen not found"
DUPLICATE_ALLERGEN = "Allergen with this name already exists"
ALLERGEN_IN_USE = "Cannot delete allergen that is referenced by other records"

MEAL_TYPE_NOT_FOUND = "Meal type not found"
DUPLICATE_MEAL_TYPE = "Meal type with this name already exists"
MEAL_TYPE_IN_USE = "Cannot delete meal type that is referenced by recipes"

RECIPE_NOT_FOUND = "Recipe not found"
DUPLICATE_RECIPE = "Recipe with this name already exists"
RECIPE_IN_USE = "Cannot delete recipe that is referenced by other records"

INGREDIENT_NOT_FOUND = "Ingredient not found"
DUPLICATE_INGREDIENT = "Ingredient with this name already exists"
INGREDIENT_IN_USE = "Cannot delete ingredient that is referenced by recipes"

CUISINE_TYPE_NOT_FOUND = "Cuisine type not found"
DUPLICATE_CUISINE_TYPE = "Cuisine type with this name already exists"
CUISINE_TYPE_IN_USE = "Cannot delete cuisine type that is referenced by recipes"

DIETARY_RESTRICTION_NOT_FOUND = "Dietary restriction not found"
DUPLICATE_DIETARY_RESTRICTION = "Dietary restriction with this name already exists"
DIETARY_RESTRICTION_IN_USE = "Cannot delete dietary restriction that is referenced by family members"

FAMILY_MEMBER_NOT_FOUND = "Family member not found"
DUPLICATE_FAMILY_MEMBER = "Family member with this name already exists"
FAMILY_MEMBER_IN_USE = "Cannot delete family member that is referenced by other records"

PROTEIN_TYPE_NOT_FOUND = "Protein type not found"
DUPLICATE_PROTEIN_TYPE = "Protein type with this name already exists"
PROTEIN_TYPE_IN_USE = "Cannot delete protein type that is referenced by other records"

COOK_METHOD_NOT_FOUND = "Cook method not found"
DUPLICATE_COOK_METHOD = "Cook method with this name already exists"
COOK_METHOD_IN_USE = "Cannot delete cook method that is referenced by recipes"

MEAL_PLAN_NOT_FOUND = "Meal plan not found"
DUPLICATE_MEAL_PLAN = "Meal plan with this name already exists"
MEAL_PLAN_IN_USE = "Cannot delete meal plan that is referenced by other records"
