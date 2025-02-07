"""Script for importing recipes from CSV files into the database."""

from __future__ import annotations

import asyncio
import csv
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from sqlalchemy import delete

from app.db.base import get_db
from app.models.models import Recipe

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def normalize_cooking_method(method: str) -> str | None:
    """Normalize cooking method to match our enum."""
    if not method:
        return None

    method = method.lower()
    if "bake" in method:
        return "bake"
    if "stovetop" in method or "simmer" in method or "fry" in method or "pan" in method:
        return "stovetop"
    if "grill" in method:
        return "grill"
    if "slow cooker" in method or "crockpot" in method:
        return "slow_cooker"
    if "instant pot" in method:
        return "instant_pot"
    if "air fry" in method:
        return "air_fryer"
    if "refrigerate" in method:
        return "refrigerate"
    if "freeze" in method:
        return "freeze"
    return "stovetop"  # default


def detect_allergens_from_title(title: str) -> dict[str, bool]:
    """Detect allergen information from recipe title."""
    title = title.lower()
    return {
        "is_dairy_free": "dairy-free" in title or "dairy free" in title,
        "is_soy_free": "soy-free" in title or "soy free" in title,
        "is_gluten_free": "gluten-free" in title or "gluten free" in title,
        "is_nut_free": "nut-free" in title or "nut free" in title,
        "is_egg_free": "egg-free" in title or "egg free" in title,
    }


def read_csv_file(file_path: Path) -> list[dict[str, str]]:
    """Read recipes from a CSV file.

    Args:
        file_path: Path to the CSV file

    Returns:
        List of recipe dictionaries
    """
    recipes = []
    with open(file_path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Recipe Title"] and "Collection" not in row["Recipe Title"]:
                recipes.append(row)
    return recipes


def parse_recipe_data(row: dict[str, str]) -> dict[str, Any] | None:
    """Parse recipe data from a CSV row.

    Args:
        row: CSV row data

    Returns:
        Parsed recipe data or None if invalid
    """
    try:
        prep_time = int(row.get("prep time", 0))
        cook_time = int(row.get("cook time", 0))
        return {
            "title": row["Recipe Title"],
            "meal_type": (row["Meal Type"].lower() if row["Meal Type"] else "other"),
            "is_collection": row["Meal Type"].lower() == "collection",
            "source_url": row["URL"],
            "image_url": row.get("Image", ""),
            "image_preview_url": row.get("Image Preview URL", ""),
            "ingredients": [],  # We'll need to scrape these from the source URL
            "instructions": [],  # We'll need to scrape these from the source URL
            "prep_time": prep_time,
            "cook_time": cook_time,
            "cooking_method": normalize_cooking_method(row["cook method"]),
            "date_added": datetime.utcnow(),
            **detect_allergens_from_title(row["Recipe Title"]),
        }
    except (ValueError, KeyError) as e:
        logger.warning(f"Error parsing recipe: {e}")
        return None


async def import_recipes(csv_path: str) -> None:
    """Import recipes from CSV file."""
    async with get_db() as db:
        # First, clear existing recipes
        await db.execute(delete(Recipe))
        await db.commit()

        # Read and import recipes
        recipes = read_csv_file(Path(csv_path))
        count = 0
        for row in recipes:
            recipe_data = parse_recipe_data(row)
            if recipe_data:
                recipe = Recipe(**recipe_data)
                db.add(recipe)
                count += 1

                # Commit in batches to avoid memory issues
                if count % 10 == 0:
                    await db.commit()

        # Final commit for remaining recipes
        await db.commit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    csv_path = sys.argv[1]
    if not os.path.exists(csv_path):
        sys.exit(1)

    asyncio.run(import_recipes(csv_path))
