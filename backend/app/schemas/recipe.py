"""Recipe schemas."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field, ValidationInfo, field_validator

from app.schemas.base import BaseSchema

if TYPE_CHECKING:
    from datetime import datetime


class RecipeBase(BaseSchema):
    """Base recipe schema."""

    title: str = Field(..., description="Recipe title", min_length=1, max_length=255)
    description: str | None = Field(None, description="Recipe description")
    prep_time: int | None = Field(None, description="Preparation time in minutes", ge=0)
    cook_time: int | None = Field(None, description="Cooking time in minutes", ge=0)
    servings: int | None = Field(None, description="Number of servings", ge=1)
    difficulty: str | None = Field(None, description="Recipe difficulty level")
    source_url: str | None = Field(None, description="Original recipe URL")
    image_url: str | None = Field(None, description="Recipe image URL")
    notes: str | None = Field(None, description="Additional notes")
    is_favorite: bool = Field(False, description="Whether the recipe is marked as favorite")
    is_private: bool = Field(False, description="Whether the recipe is private")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Spaghetti Carbonara",
                "description": "Classic Italian pasta dish",
                "prep_time": 10,
                "cook_time": 30,
                "servings": 4,
                "difficulty": "medium",
                "source_url": "https://www.example.com/spaghetti-carbonara",
                "image_url": "https://www.example.com/spaghetti-carbonara.jpg",
                "notes": "This recipe is a classic Italian dish made with spaghetti, pancetta, eggs, and pecorino cheese. It's quick and easy to make, and it's perfect for a weeknight dinner.",
                "is_favorite": True,
                "is_private": False,
            }
        }
    )


class RecipeCreate(RecipeBase):
    """Recipe creation schema."""

    ingredients: list[str] = Field(..., description="List of ingredients")
    instructions: list[str] = Field(..., description="List of instructions")
    cuisine_type_id: int | None = Field(None, description="Cuisine type ID")
    cook_method_id: int | None = Field(None, description="Cooking method ID")
    protein_type_id: int | None = Field(None, description="Protein type ID")
    meal_type_id: int | None = Field(None, description="Meal type ID")
    allergens: list[int] = Field(default_factory=list, description="List of allergen IDs")
    dietary_restrictions: list[int] = Field(default_factory=list, description="List of dietary restriction IDs")


class RecipeUpdate(RecipeBase):
    """Recipe update schema."""

    ingredients: list[str] | None = Field(None, description="List of ingredients")
    instructions: list[str] | None = Field(None, description="List of instructions")
    cuisine_type_id: int | None = Field(None, description="Cuisine type ID")
    cook_method_id: int | None = Field(None, description="Cooking method ID")
    protein_type_id: int | None = Field(None, description="Protein type ID")
    meal_type_id: int | None = Field(None, description="Meal type ID")
    allergens: list[int] | None = Field(None, description="List of allergen IDs")
    dietary_restrictions: list[int] | None = Field(None, description="List of dietary restriction IDs")

    model_config = ConfigDict(
        json_schema_extra={"example": {"title": "Updated Spaghetti Carbonara", "cook_time": 25, "servings": 2}}
    )


class RecipeResponse(RecipeBase):
    """Recipe response schema."""

    model_config = ConfigDict(from_attributes=True)

    recipe_id: int = Field(..., description="Recipe ID")
    ingredients: list[str] = Field(..., description="List of ingredients")
    instructions: list[str] = Field(..., description="List of instructions")
    cuisine_type: str | None = Field(None, description="Cuisine type name")
    cook_method: str | None = Field(None, description="Cooking method name")
    protein_type: str | None = Field(None, description="Protein type name")
    meal_type: str | None = Field(None, description="Meal type name")
    allergens: list[str] = Field(default_factory=list, description="List of allergen names")
    dietary_restrictions: list[str] = Field(default_factory=list, description="List of dietary restriction names")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")


class RecipeSearchFilter(BaseModel):
    """Recipe search filter schema."""

    cuisine: str | None = Field(None, description="Filter by cuisine type")
    diet: str | None = Field(None, description="Filter by dietary restriction")
    allergens: list[str] | None = Field(None, description="Exclude recipes with these allergens")
    max_time: int | None = Field(None, description="Maximum total cooking time in minutes", ge=0)
    difficulty: str | None = Field(None, description="Filter by difficulty level")
    meal_type: str | None = Field(None, description="Filter by meal type")
    protein_type: str | None = Field(None, description="Filter by protein type")
    cook_method: str | None = Field(None, description="Filter by cooking method")
    is_favorite: bool | None = Field(None, description="Filter by favorite status")
    exclude_ingredients: list[str] | None = Field(None, description="Exclude recipes with these ingredients")
    include_ingredients: list[str] | None = Field(None, description="Include recipes with these ingredients")

    @field_validator("max_time")
    @classmethod
    def validate_max_time(cls, v: int | None) -> int | None:
        """Validate max_time is positive."""
        if v is not None and v < 0:
            msg = "max_time must be non-negative"
            raise ValueError(msg)
        return v


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


class PaginatedRecipeResponse(BaseModel):
    """Paginated recipe response schema."""

    items: list[RecipeResponse] = Field(..., description="List of recipes")
    total: int = Field(..., description="Total number of recipes matching the query")
    page: int = Field(..., description="Current page number")
    page_size: int = Field(..., description="Number of items per page")
    pages: int = Field(..., description="Total number of pages")

    @field_validator("pages")
    @classmethod
    def validate_pages(cls, v: int, info: ValidationInfo) -> int:
        """Validate pages is at least 1."""
        if v < 1:
            total = info.data.get("total", 0)
            page_size = info.data.get("page_size", 1)
            return max(1, (total + page_size - 1) // page_size)
        return v
