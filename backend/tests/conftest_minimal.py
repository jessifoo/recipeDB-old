from __future__ import annotations

from typing import Any

import pytest


@pytest.fixture
def mock_db():
    class MockDB:
        def __init__(self):
            self.recipes = {}
            self.next_id = 1

        def add_recipe(self, recipe: dict[str, Any]) -> int:
            recipe_id = self.next_id
            self.recipes[recipe_id] = recipe
            self.next_id += 1
            return recipe_id

        def get_recipe(self, recipe_id: int) -> dict[str, Any]:
            return self.recipes.get(recipe_id)

        def list_recipes(self) -> list[dict[str, Any]]:
            return list(self.recipes.values())

    return MockDB()
