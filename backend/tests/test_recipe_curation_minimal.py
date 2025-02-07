from __future__ import annotations

import pytest


class Recipe:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class TestRecipeCuration:
    @pytest.fixture
    def recipes(self):
        return [
            Recipe(
                id="1",
                title="Dairy-Free Mac and Cheese",
                ingredients=[
                    "cashews",
                    "nutritional yeast",
                    "plant milk",
                    "pasta",
                ],
                is_dairy_free=True,
                is_egg_free=True,
                is_soy_free=True,
            ),
            Recipe(
                id="2",
                title="Classic Mac and Cheese",
                ingredients=["cheddar cheese", "milk", "butter", "pasta"],
                is_dairy_free=False,
                is_egg_free=True,
                is_soy_free=True,
            ),
        ]

    def test_allergen_filtering(self, recipes):
        """Test that recipes are properly filtered by allergens"""
        dairy_free_recipes = [r for r in recipes if r.is_dairy_free]
        assert len(dairy_free_recipes) == 1
        assert dairy_free_recipes[0].title == "Dairy-Free Mac and Cheese"

    def test_ingredient_validation(self, recipes):
        """Test that ingredients are properly validated for allergens"""
        suspicious_recipe = Recipe(
            id="3",
            title="Suspicious Recipe",
            ingredients=["natural flavors (contains milk)", "spices", "pasta"],
            is_dairy_free=True,  # Incorrectly marked as dairy-free
        )

        def has_dairy(ingredients: list[str]) -> bool:
            dairy_terms = [
                "milk",
                "cheese",
                "butter",
                "cream",
                "whey",
                "casein",
            ]
            return any(any(term in ingredient.lower() for term in dairy_terms) for ingredient in ingredients)

        assert has_dairy(suspicious_recipe.ingredients)
        assert not suspicious_recipe.is_dairy_free

    def test_hidden_allergens(self, recipes):
        """Test detection of hidden allergens in ingredients"""
        recipe = Recipe(
            id="4",
            title="Sneaky Recipe",
            ingredients=[
                "whey protein",  # Hidden dairy
                "natural flavoring",  # Potential hidden allergen
                "spices",
            ],
            is_dairy_free=True,
        )

        hidden_allergen_terms = [
            "whey",
            "casein",
            "natural flavoring",
            "spices",
            "artificial flavoring",
        ]

        def has_hidden_allergens(ingredients: list[str]) -> bool:
            return any(any(term in ingredient.lower() for term in hidden_allergen_terms) for ingredient in ingredients)

        assert has_hidden_allergens(recipe.ingredients)

    def test_recipe_deduplication(self, recipes):
        """Test that duplicate recipes are properly handled"""
        duplicate_recipes = recipes + [
            Recipe(
                id="5",
                title="Classic Mac and Cheese",  # Duplicate title
                ingredients=["cheddar cheese", "milk", "butter", "pasta"],
                is_dairy_free=False,
                is_egg_free=True,
                is_soy_free=True,
            ),
        ]

        def deduplicate_recipes(recipes: list[Recipe]) -> list[Recipe]:
            seen_titles = set()
            unique_recipes = []

            for recipe in recipes:
                if recipe.title not in seen_titles:
                    seen_titles.add(recipe.title)
                    unique_recipes.append(recipe)

            return unique_recipes

        deduplicated = deduplicate_recipes(duplicate_recipes)
        assert len(deduplicated) == 2  # Should remove one duplicate
        assert len({r.title for r in deduplicated}) == 2  # All titles should be unique
