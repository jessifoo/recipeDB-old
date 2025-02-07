"""Recipe schemas for request/response models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from datetime import datetime


class RecipeBase(BaseModel):
    """Base recipe attributes."""

    title: str = Field(description="Recipe title")
    description: str | None = Field(default=None, description="Recipe description")
    cooking_time: int = Field(description="Total cooking time in minutes", ge=0)
    servings: int = Field(description="Number of servings", ge=1)
    difficulty: str = Field(description="Recipe difficulty level")
    instructions: list[str] = Field(description="List of cooking instructions")
    ingredients: list[str] = Field(description="List of ingredients")
    tags: list[str] = Field(default_factory=list, description="Recipe tags")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Spaghetti Carbonara",
                "description": "Classic Italian pasta dish",
                "cooking_time": 30,
                "servings": 4,
                "difficulty": "medium",
                "instructions": ["Boil pasta", "Cook pancetta", "Mix eggs and cheese", "Combine all ingredients"],
                "ingredients": ["400g spaghetti", "200g pancetta", "4 eggs", "100g pecorino cheese"],
                "tags": ["pasta", "italian", "quick"],
            }
        }
    )


class RecipeCreate(RecipeBase):
    """Recipe creation attributes."""


class RecipeUpdate(BaseModel):
    """Recipe update attributes."""

    title: str | None = Field(default=None, description="Recipe title")
    description: str | None = Field(default=None, description="Recipe description")
    cooking_time: int | None = Field(default=None, description="Total cooking time in minutes", ge=0)
    servings: int | None = Field(default=None, description="Number of servings", ge=1)
    difficulty: str | None = Field(default=None, description="Recipe difficulty level")
    instructions: list[str] | None = Field(default=None, description="List of cooking instructions")
    ingredients: list[str] | None = Field(default=None, description="List of ingredients")
    tags: list[str] | None = Field(default=None, description="Recipe tags")

    model_config = ConfigDict(
        json_schema_extra={"example": {"title": "Updated Spaghetti Carbonara", "cooking_time": 25, "servings": 2}}
    )


class RecipeResponse(RecipeBase):
    """Recipe response attributes."""

    id: int = Field(description="Recipe ID")
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RecipeSearchFilter(BaseModel):
    """Recipe search filter parameters."""

    cuisine_type: str | None = Field(default=None, description="Filter by cuisine type")
    difficulty: str | None = Field(default=None, description="Filter by difficulty level")
    max_cooking_time: int | None = Field(default=None, description="Maximum cooking time in minutes", ge=0)
    tags: list[str] | None = Field(default=None, description="Filter by tags")
    ingredients: list[str] | None = Field(default=None, description="Filter by ingredients")
    allergens_exclude: list[str] | None = Field(default=None, description="Allergens to exclude")
    dietary_restrictions: list[str] | None = Field(default=None, description="Dietary restrictions")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "cuisine_type": "italian",
                "max_cooking_time": 30,
                "tags": ["quick", "easy"],
                "allergens_exclude": ["nuts", "dairy"],
            }
        }
    )


class RecipeSearchResult(BaseModel):
    """Recipe search result."""

    id: str = Field(..., description="Recipe ID")
    title: str = Field(..., description="Recipe title")
    description: str | None = Field(None, description="Recipe description")
    image_url: str | None = Field(None, description="URL to recipe image")
    source_url: str | None = Field(None, description="URL to recipe source")
    prep_time: int | None = Field(None, description="Preparation time in minutes")
    cook_time: int | None = Field(None, description="Cooking time in minutes")
    total_time: int | None = Field(None, description="Total time in minutes")
    servings: int | None = Field(None, description="Number of servings")
    cuisine: str | None = Field(None, description="Cuisine type")
    diet: list[str] | None = Field(None, description="Dietary restrictions")
    ingredients: list[str] | None = Field(None, description="List of ingredients")
    instructions: list[str] | None = Field(None, description="List of instructions")
    source: str = Field(..., description="Source of the recipe (e.g., 'spoonacular', 'edamam')")


class RecipeList(BaseModel):
    """List of recipe search results."""

    total: int = Field(..., description="Total number of results")
    results: list[RecipeSearchResult] = Field(..., description="List of recipe results")
    source: str = Field(..., description="Source of the results")
