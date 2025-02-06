"""SQLAlchemy models for the recipe database."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Table, Text, func
from sqlalchemy.orm import mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from datetime import date, datetime

    from sqlalchemy.orm import Mapped

# Association tables for many-to-many relationships
recipe_allergens = Table(
    "recipe_allergens",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("allergen_id", Integer, ForeignKey("allergens.allergen_id"), primary_key=True),
)

recipe_ingredients = Table(
    "recipe_ingredients",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("ingredient_id", Integer, ForeignKey("ingredients.ingredient_id"), primary_key=True),
)

recipe_meal_types = Table(
    "recipe_meal_types",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("meal_type_id", Integer, ForeignKey("meal_types.meal_type_id"), primary_key=True),
)

recipe_cook_methods = Table(
    "recipe_cook_methods",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("method_id", Integer, ForeignKey("cook_methods.method_id"), primary_key=True),
)

recipe_protein_types = Table(
    "recipe_protein_types",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("protein_id", Integer, ForeignKey("protein_types.protein_id"), primary_key=True),
)

recipe_cuisine_types = Table(
    "recipe_cuisine_types",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("cuisine_id", Integer, ForeignKey("cuisine_types.cuisine_id"), primary_key=True),
)

family_member_dietary_restrictions = Table(
    "family_member_dietary_restrictions",
    Base.metadata,
    Column("member_id", Integer, ForeignKey("family_members.member_id"), primary_key=True),
    Column(
        "restriction_id",
        Integer,
        ForeignKey("dietary_restrictions.restriction_id"),
        primary_key=True,
    ),
)


class RecipeInstruction(Base):
    """Recipe instruction model."""

    __tablename__ = "recipe_instructions"

    instruction_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.recipe_id"), nullable=False)
    step_number: Mapped[int] = mapped_column(Integer, nullable=False)
    instruction: Mapped[str] = mapped_column(Text, nullable=False)

    # Relationship
    recipe: Mapped[Recipe] = relationship("Recipe", back_populates="instructions")


class Recipe(Base):
    """Recipe model."""

    __tablename__ = "recipes"

    recipe_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    image_url: Mapped[str | None] = mapped_column(String(1024))
    source_url: Mapped[str | None] = mapped_column(String(1024))
    prep_time_minutes: Mapped[int | None] = mapped_column(Integer)
    cook_time_minutes: Mapped[int | None] = mapped_column(Integer)
    servings: Mapped[int | None] = mapped_column(Integer)
    is_favorite: Mapped[bool] = mapped_column(Boolean, default=False)
    variations: Mapped[str | None] = mapped_column(Text)
    last_made_date: Mapped[date | None] = mapped_column(Date)

    # Relationships
    instructions: Mapped[list[RecipeInstruction]] = relationship(
        "RecipeInstruction",
        back_populates="recipe",
        cascade="all, delete-orphan",
    )
    allergens: Mapped[list[Allergen]] = relationship("Allergen", secondary=recipe_allergens, back_populates="recipes")
    ingredients: Mapped[list[Ingredient]] = relationship(
        "Ingredient",
        secondary=recipe_ingredients,
        back_populates="recipes",
    )
    meal_types: Mapped[list[MealType]] = relationship(
        "MealType",
        secondary=recipe_meal_types,
        back_populates="recipes",
    )
    cook_methods: Mapped[list[CookMethod]] = relationship(
        "CookMethod",
        secondary=recipe_cook_methods,
        back_populates="recipes",
    )
    protein_types: Mapped[list[ProteinType]] = relationship(
        "ProteinType",
        secondary=recipe_protein_types,
        back_populates="recipes",
    )
    cuisine_types: Mapped[list[CuisineType]] = relationship(
        "CuisineType",
        secondary=recipe_cuisine_types,
        back_populates="recipes",
    )

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    def __repr__(self) -> str:
        """String representation of the recipe."""
        return f"<Recipe {self.title}>"


class IngredientCategory(Base):
    """Ingredient category model."""

    __tablename__ = "ingredient_categories"

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationships
    ingredients: Mapped[list[Ingredient]] = relationship("Ingredient", back_populates="category")


class Ingredient(Base):
    """Ingredient model."""

    __tablename__ = "ingredients"

    ingredient_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("ingredient_categories.category_id"))

    # Relationships
    category: Mapped[IngredientCategory] = relationship("IngredientCategory", back_populates="ingredients")
    recipes: Mapped[list[Recipe]] = relationship("Recipe", secondary=recipe_ingredients, back_populates="ingredients")


class Allergen(Base):
    """Allergen model."""

    __tablename__ = "allergens"

    allergen_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    severity: Mapped[str | None] = mapped_column(String(50))

    # Relationships
    recipes: Mapped[list[Recipe]] = relationship("Recipe", secondary=recipe_allergens, back_populates="allergens")


class CookMethod(Base):
    """Cook method model."""

    __tablename__ = "cook_methods"

    method_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationships
    recipes: Mapped[list[Recipe]] = relationship(
        "Recipe",
        secondary=recipe_cook_methods,
        back_populates="cook_methods",
    )


class ProteinType(Base):
    """Protein type model."""

    __tablename__ = "protein_types"

    protein_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationships
    recipes: Mapped[list[Recipe]] = relationship(
        "Recipe",
        secondary=recipe_protein_types,
        back_populates="protein_types",
    )


class MealType(Base):
    """Meal type model."""

    __tablename__ = "meal_types"

    meal_type_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationships
    recipes: Mapped[list[Recipe]] = relationship("Recipe", secondary=recipe_meal_types, back_populates="meal_types")
    meal_plans: Mapped[list[MealPlan]] = relationship("MealPlan", back_populates="meal_type")


class CuisineType(Base):
    """Cuisine type model."""

    __tablename__ = "cuisine_types"

    cuisine_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    last_used_date: Mapped[date | None] = mapped_column(Date)

    # Relationships
    recipes: Mapped[list[Recipe]] = relationship(
        "Recipe",
        secondary=recipe_cuisine_types,
        back_populates="cuisine_types",
    )


class DietaryRestriction(Base):
    """Dietary restriction model."""

    __tablename__ = "dietary_restrictions"

    restriction_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationships
    family_members: Mapped[list[FamilyMember]] = relationship(
        "FamilyMember",
        secondary=family_member_dietary_restrictions,
        back_populates="dietary_restrictions",
    )


class FamilyMember(Base):
    """Family member model."""

    __tablename__ = "family_members"

    member_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_date: Mapped[date | None] = mapped_column(Date)
    notes: Mapped[str | None] = mapped_column(Text)

    # Relationships
    meal_plans: Mapped[list[MealPlan]] = relationship("MealPlan", back_populates="family_member")
    ratings: Mapped[list[RecipeRating]] = relationship("RecipeRating", back_populates="family_member")
    dietary_restrictions: Mapped[list[DietaryRestriction]] = relationship(
        "DietaryRestriction",
        secondary=family_member_dietary_restrictions,
        back_populates="family_members",
    )


class AllergenSubstitution(Base):
    """Allergen substitution model."""

    __tablename__ = "allergen_substitutions"

    substitution_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    allergen_id: Mapped[int] = mapped_column(ForeignKey("allergens.allergen_id"), nullable=False)
    substitute_ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.ingredient_id"), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text)


class MealPlan(Base):
    """Meal plan model."""

    __tablename__ = "meal_plans"

    plan_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.recipe_id"), nullable=False)
    planned_date: Mapped[date] = mapped_column(Date, nullable=False)
    meal_type_id: Mapped[int] = mapped_column(ForeignKey("meal_types.meal_type_id"), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text)
    member_id: Mapped[int] = mapped_column(ForeignKey("family_members.member_id"), nullable=False)

    # Relationships
    recipe: Mapped[Recipe] = relationship("Recipe")
    meal_type: Mapped[MealType] = relationship("MealType", back_populates="meal_plans")
    family_member: Mapped[FamilyMember] = relationship("FamilyMember", back_populates="meal_plans")


class RecipeRating(Base):
    """Recipe rating model."""

    __tablename__ = "recipe_ratings"

    rating_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.recipe_id"), nullable=False)
    member_id: Mapped[int] = mapped_column(ForeignKey("family_members.member_id"), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Relationships
    recipe: Mapped[Recipe] = relationship("Recipe")
    family_member: Mapped[FamilyMember] = relationship("FamilyMember", back_populates="ratings")
