"""Mock recipe provider for testing."""

from __future__ import annotations

import random

from app.schemas.recipe import RecipeList, RecipeSearchResult

from .base import RecipeProvider


class MockRecipeProvider(RecipeProvider):
    """Mock recipe provider that returns generated data."""

    def __init__(self) -> None:
        """Initialize the mock provider."""
        super().__init__()
        self._mock_recipes = self._generate_mock_recipes()

    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search mock recipes."""
        # Filter recipes based on query
        results = [
            recipe
            for recipe in self._mock_recipes
            if query.lower() in recipe.title.lower()
            or (recipe.description and query.lower() in recipe.description.lower())
        ]

        # Apply filters
        if cuisine:
            results = [r for r in results if r.cuisine == cuisine]
        if diet:
            results = [r for r in results if diet in (r.diet or [])]
        if exclude:
            results = [r for r in results if not any(ing in " ".join(r.ingredients or []).lower() for ing in exclude)]
        if max_time:
            results = [r for r in results if r.total_time and r.total_time <= max_time]

        # Apply pagination
        paginated_results = results[offset : offset + limit] if limit else results[offset:]

        return RecipeList(total=len(results), results=paginated_results, source=self.source_name)

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get mock recipe by ID."""
        for recipe in self._mock_recipes:
            if recipe.id == recipe_id:
                return recipe
        msg = f"Recipe not found: {recipe_id}"
        raise ValueError(msg)

    def _generate_mock_recipes(self) -> list[RecipeSearchResult]:
        """Generate a list of mock recipes."""
        cuisines = ["Italian", "Mexican", "Chinese", "Indian", "American"]
        diets = ["Vegetarian", "Vegan", "Gluten-Free", "Keto", "Paleo"]

        recipes = []
        for i in range(100):  # Generate 100 mock recipes
            cuisine = random.choice(cuisines)
            recipe_diets = random.sample(diets, random.randint(0, 2))

            recipe = RecipeSearchResult(
                id=f"mock_{i}",
                title=f"Mock {cuisine} Recipe {i}",
                description=f"A delicious {cuisine} recipe with mock ingredients",
                image_url=f"https://example.com/images/recipe_{i}.jpg",
                source_url=f"https://example.com/recipes/{i}",
                prep_time=random.randint(5, 30),
                cook_time=random.randint(10, 60),
                total_time=random.randint(15, 90),
                servings=random.randint(2, 6),
                cuisine=cuisine,
                diet=recipe_diets,
                ingredients=[f"Mock Ingredient {j}" for j in range(random.randint(3, 8))],
                instructions=[f"Mock Step {j}" for j in range(random.randint(3, 6))],
                source=self.source_name,
            )
            recipes.append(recipe)

        return recipes
