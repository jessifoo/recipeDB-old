"""Services package.

This package contains service layer modules for business logic. Services handle
complex operations, database interactions, and external API calls while maintaining
separation of concerns.

Example:
    .. code-block:: python

        from app.services import RecipeSearchService

        # Search for recipes
        service = RecipeSearchService(db_session)
        results = await service.search(query="pasta", cuisine="italian")
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.services.recipe_search import RecipeSearchService
from app.services.recipe_service import RecipeService

if TYPE_CHECKING:
    from app.services.recipe_search import RecipeSearchService as RecipeSearchServiceType
    from app.services.recipe_service import RecipeService as RecipeServiceType

    # Type hints for exported services
    RecipeSearchService: type[RecipeSearchServiceType]
    RecipeService: type[RecipeServiceType]

__version__ = "1.0.0"

__all__ = ["RecipeSearchService", "RecipeService"]
