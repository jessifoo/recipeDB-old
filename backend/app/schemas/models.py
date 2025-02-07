"""Pydantic schemas for database models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from datetime import date, datetime


# --- Recipe Schemas ---
class RecipeInstructionBase(BaseModel):
    step_number: int
    instruction: str


class RecipeInstructionCreate(RecipeInstructionBase):
    pass


class RecipeInstruction(RecipeInstructionBase):
    instruction_id: int
    recipe_id: int

    class Config:
        from_attributes = True


class RecipeBase(BaseModel):
    title: str
    image_url: str | None = None
    source_url: str | None = None
    prep_time_minutes: int | None = None
    cook_time_minutes: int | None = None
    servings: int | None = None
    is_favorite: bool = False
    variations: str | None = None


class RecipeCreate(RecipeBase):
    instructions: list[RecipeInstructionCreate] = []


class RecipeUpdate(BaseModel):
    """Schema for updating a recipe. All fields are optional."""

    title: str | None = None
    image_url: str | None = None
    source_url: str | None = None
    prep_time_minutes: int | None = None
    cook_time_minutes: int | None = None
    servings: int | None = None
    is_favorite: bool | None = None
    variations: str | None = None
    instructions: list[RecipeInstructionCreate] | None = None


class Recipe(RecipeBase):
    recipe_id: int
    last_made_date: date | None = None
    created_at: datetime
    updated_at: datetime
    instructions: list[RecipeInstruction] = []

    class Config:
        from_attributes = True


# --- Ingredient Schemas ---
class IngredientCategoryBase(BaseModel):
    name: str


class IngredientCategoryCreate(IngredientCategoryBase):
    pass


class IngredientCategory(IngredientCategoryBase):
    category_id: int

    class Config:
        orm_mode = True


class IngredientBase(BaseModel):
    name: str
    category_id: int


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(BaseModel):
    """Schema for updating an ingredient. All fields are optional."""

    name: str | None = None
    category_id: int | None = None


class Ingredient(IngredientBase):
    ingredient_id: int

    class Config:
        orm_mode = True


# --- Allergen Schemas ---
class AllergenBase(BaseModel):
    name: str
    severity: str | None = None


class AllergenCreate(AllergenBase):
    pass


class Allergen(AllergenBase):
    allergen_id: int

    class Config:
        orm_mode = True


# --- Cook Method Schemas ---
class CookMethodBase(BaseModel):
    name: str


class CookMethodCreate(CookMethodBase):
    pass


class CookMethod(CookMethodBase):
    method_id: int

    class Config:
        orm_mode = True


# --- Protein Type Schemas ---
class ProteinTypeBase(BaseModel):
    name: str


class ProteinTypeCreate(ProteinTypeBase):
    pass


class ProteinType(ProteinTypeBase):
    protein_id: int

    class Config:
        orm_mode = True


# --- Meal Type Schemas ---
class MealTypeBase(BaseModel):
    name: str


class MealTypeCreate(MealTypeBase):
    pass


class MealType(MealTypeBase):
    meal_type_id: int

    class Config:
        orm_mode = True


# --- Cuisine Type Schemas ---
class CuisineTypeBase(BaseModel):
    name: str
    last_used_date: date | None = None


class CuisineTypeCreate(CuisineTypeBase):
    pass


class CuisineType(CuisineTypeBase):
    cuisine_id: int

    class Config:
        orm_mode = True


# --- Dietary Restriction Schemas ---
class DietaryRestrictionBase(BaseModel):
    name: str


class DietaryRestrictionCreate(DietaryRestrictionBase):
    pass


class DietaryRestriction(DietaryRestrictionBase):
    restriction_id: int

    class Config:
        orm_mode = True


# --- Family Member Schemas ---
class FamilyMemberBase(BaseModel):
    name: str
    birth_date: date | None = None
    notes: str | None = None


class FamilyMemberCreate(FamilyMemberBase):
    pass


class FamilyMember(FamilyMemberBase):
    member_id: int

    class Config:
        orm_mode = True


# --- Allergen Substitution Schemas ---
class AllergenSubstitutionBase(BaseModel):
    allergen_id: int
    substitute_ingredient_id: int
    notes: str | None = None


class AllergenSubstitutionCreate(AllergenSubstitutionBase):
    pass


class AllergenSubstitution(AllergenSubstitutionBase):
    substitution_id: int

    class Config:
        orm_mode = True


# --- Meal Plan Schemas ---
class MealPlanBase(BaseModel):
    recipe_id: int
    planned_date: date
    meal_type_id: int
    notes: str | None = None
    member_id: int


class MealPlanCreate(MealPlanBase):
    pass


class MealPlan(MealPlanBase):
    plan_id: int

    class Config:
        orm_mode = True


# --- Recipe Rating Schemas ---
class RecipeRatingBase(BaseModel):
    recipe_id: int
    member_id: int
    rating: int
    review: str | None = None


class RecipeRatingCreate(RecipeRatingBase):
    pass


class RecipeRating(RecipeRatingBase):
    rating_id: int
    created_at: datetime

    class Config:
        orm_mode = True
