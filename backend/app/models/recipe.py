"""Recipe domain models."""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from datetime import datetime

    from pydantic import HttpUrl


class CuisineType(str, Enum):
    """Standardized cuisine types across providers."""

    AMERICAN = "american"
    ASIAN = "asian"
    MEDITERRANEAN = "mediterranean"
    ITALIAN = "italian"
    MEXICAN = "mexican"
    INDIAN = "indian"
    FRENCH = "french"
    CHINESE = "chinese"
    JAPANESE = "japanese"
    THAI = "thai"
    VIETNAMESE = "vietnamese"
    KOREAN = "korean"
    MIDDLE_EASTERN = "middle_eastern"
    GREEK = "greek"
    SPANISH = "spanish"
    OTHER = "other"


class DietType(str, Enum):
    """Standardized diet types across providers."""

    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    GLUTEN_FREE = "gluten_free"
    DAIRY_FREE = "dairy_free"
    KETO = "keto"
    PALEO = "paleo"
    LOW_CARB = "low_carb"
    LOW_FAT = "low_fat"
    OTHER = "other"


class CookingMethod(str, Enum):
    """Standardized cooking methods across providers."""

    BAKE = "bake"
    GRILL = "grill"
    FRY = "fry"
    ROAST = "roast"
    BOIL = "boil"
    STEAM = "steam"
    SLOW_COOK = "slow_cook"
    PRESSURE_COOK = "pressure_cook"
    SAUTE = "saute"
    OTHER = "other"


class Ingredient(BaseModel):
    """Standardized ingredient model."""

    name: str
    amount: float | None = None
    unit: str | None = None
    notes: str | None = None
    is_allergen: bool = False


class Instruction(BaseModel):
    """Standardized instruction model."""

    step_number: int
    description: str
    time_minutes: int | None = None
    temperature: float | None = None
    temperature_unit: str | None = None


class NutritionalInfo(BaseModel):
    """Standardized nutritional information."""

    calories: float | None = None
    protein_g: float | None = None
    carbohydrates_g: float | None = None
    fat_g: float | None = None
    fiber_g: float | None = None
    sugar_g: float | None = None
    sodium_mg: float | None = None


class Recipe(BaseModel):
    """Core recipe model that all providers map to."""

    id: str = Field(..., description="Unique identifier for the recipe")
    source_id: str = Field(..., description="Original ID from the provider")
    provider: str = Field(..., description="Name of the recipe provider")

    # Basic Information
    title: str
    description: str | None = None
    image_url: HttpUrl | None = None
    source_url: HttpUrl | None = None
    author: str | None = None
    date_published: datetime | None = None
    date_updated: datetime | None = None

    # Recipe Details
    cuisine: CuisineType | None = None
    diets: list[DietType] = Field(default_factory=list)
    cooking_method: CookingMethod | None = None

    # Time and Servings
    prep_time_minutes: int | None = None
    cook_time_minutes: int | None = None
    total_time_minutes: int | None = None
    servings: int | None = None

    # Ingredients and Instructions
    ingredients: list[Ingredient] = Field(..., min_items=1)
    instructions: list[Instruction] = Field(..., min_items=1)

    # Additional Information
    difficulty_level: int | None = Field(None, ge=1, le=5)
    rating: float | None = Field(None, ge=0, le=5)
    review_count: int | None = Field(None, ge=0)
    nutritional_info: NutritionalInfo | None = None

    # Allergen Information
    is_dairy_free: bool = False
    is_gluten_free: bool = False
    is_egg_free: bool = False
    is_nut_free: bool = False
    is_soy_free: bool = False

    # Tags and Categories
    tags: list[str] = Field(default_factory=list)
    equipment_needed: list[str] = Field(default_factory=list)

    class Config:
        """Pydantic model configuration."""

        json_schema_extra = {
            "example": {
                "id": "recipe_123",
                "source_id": "spoonacular_456",
                "provider": "spoonacular",
                "title": "Spaghetti Carbonara",
                "description": "Classic Italian pasta dish",
                "cuisine": "italian",
                "diets": ["dairy_free"],
                "cooking_method": "boil",
                "prep_time_minutes": 15,
                "cook_time_minutes": 20,
                "ingredients": [
                    {
                        "name": "spaghetti",
                        "amount": 500,
                        "unit": "g",
                    },
                ],
                "instructions": [
                    {
                        "step_number": 1,
                        "description": "Boil water and cook pasta",
                    },
                ],
            },
        }
