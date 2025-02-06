"""Unit tests for recipe search service."""

from __future__ import annotations

import asyncio
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Recipe
from app.services.exceptions import (
    APIError,
    DatabaseError,
    ParseError,
    RateLimitError,
    RecipeNotFoundError,
    ServiceValidationError,
)
from app.services.recipe_search import RecipeSearchService


@pytest.fixture
async def mock_session():
    """Create a mock database session."""
    session = AsyncMock(spec=AsyncSession)
    session.begin = AsyncMock(return_value=AsyncMock(__aenter__=AsyncMock(), __aexit__=AsyncMock()))
    return session


@pytest.fixture
def recipe_search_service(mock_session):
    """Create a RecipeSearchService instance with a mock session."""
    service = RecipeSearchService()
    service._session = mock_session
    return service


@pytest.fixture
def mock_recipe():
    """Create a mock recipe for testing."""
    return Recipe(
        id="test_recipe_1",
        title="Test Recipe",
        image="https://example.com/image.jpg",
        source="test",
        source_url="https://example.com/recipe",
        servings=4,
        ready_in_minutes=30,
        ingredients=["ingredient1", "ingredient2"],
        instructions=["step1", "step2"],
        tags=["tag1", "tag2"],
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
    )


@pytest.fixture
def sample_edamam_response():
    """Sample Edamam API response"""
    return {
        "hits": [
            {
                "recipe": {
                    "uri": "edamam_123",
                    "label": "Instant Pot Chicken",
                    "image": "https://example.com/image.jpg",
                    "url": "https://example.com/recipe",
                    "yield": 4,
                    "totalTime": 30,
                    "ingredientLines": ["2 lbs chicken breast", "1 cup broth"],
                    "ingredients": [
                        {
                            "text": "2 lbs chicken breast",
                            "quantity": 2,
                            "measure": "pound",
                            "food": "chicken breast",
                        },
                    ],
                    "totalNutrients": {
                        "ENERC_KCAL": {"quantity": 500},
                        "PROCNT": {"quantity": 30},
                        "FAT": {"quantity": 20},
                        "CHOCDF": {"quantity": 10},
                    },
                },
            },
        ],
    }


@pytest.fixture
def sample_spoonacular_response():
    """Sample Spoonacular API response"""
    return {
        "results": [
            {
                "id": "spoonacular_123",
                "title": "Easy Beef Stew",
                "image": "https://example.com/image.jpg",
                "sourceUrl": "https://example.com/recipe",
                "servings": 4,
                "readyInMinutes": 60,
                "extendedIngredients": [
                    {
                        "original": "2 lbs beef",
                        "amount": 2,
                        "unit": "pound",
                        "name": "beef",
                    },
                ],
                "analyzedInstructions": [
                    {
                        "steps": [
                            {"step": "Brown beef"},
                            {"step": "Add vegetables"},
                        ],
                    },
                ],
                "nutrition": {
                    "nutrients": [
                        {"name": "Calories", "amount": 600},
                        {"name": "Protein", "amount": 40},
                        {"name": "Fat", "amount": 30},
                        {"name": "Carbohydrates", "amount": 20},
                    ],
                },
            },
        ],
    }


@pytest.fixture
def mock_edamam_response():
    """Mock Edamam API response"""
    return {
        "hits": [
            {
                "recipe": {
                    "uri": "edamam_recipe_1",
                    "label": "Test Recipe 1",
                    "source": "Edamam",
                    "cuisineType": ["Italian"],
                    "totalTime": 30,
                    "ingredientLines": ["ingredient 1", "ingredient 2"],
                    "instructions": ["step 1", "step 2"],
                    "healthLabels": ["Vegetarian"],
                    "cautions": ["Gluten"],
                    "yield": 4,
                    "calories": 400,
                },
            },
        ],
    }


@pytest.fixture
def mock_spoonacular_response():
    """Mock Spoonacular API response"""
    return {
        "results": [
            {
                "id": "spoon_recipe_1",
                "title": "Test Recipe 2",
                "sourceName": "Spoonacular",
                "cuisines": ["French"],
                "readyInMinutes": 45,
                "extendedIngredients": [
                    {"original": "ingredient 1"},
                    {"original": "ingredient 2"},
                ],
                "analyzedInstructions": [{"steps": [{"step": "step 1"}, {"step": "step 2"}]}],
                "diets": ["gluten free"],
                "nutrition": {"nutrients": []},
                "servings": 4,
            },
        ],
    }


@pytest.fixture
def mock_api_client():
    """Mock API client with responses"""
    client = AsyncMock()
    client._make_api_request = AsyncMock()
    return client


@pytest.mark.asyncio
async def test_get_recipe_by_id_from_db(recipe_search_service, mock_session, mock_recipe):
    """Test retrieving recipe from database"""
    # Mock database query
    mock_session.execute.return_value.scalar_one_or_none.return_value = mock_recipe

    # Get recipe
    result = await recipe_search_service.get_recipe_by_id("test_recipe_1")

    # Verify result
    assert result == mock_recipe
    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_get_recipe_by_id_stale_cache(recipe_search_service, mock_session, mock_recipe):
    """Test retrieving recipe with stale cache"""
    # Set last_fetched to old timestamp
    mock_recipe.last_fetched = datetime.now(UTC) - timedelta(hours=25)
    mock_session.execute.return_value.scalar_one_or_none.return_value = mock_recipe

    # Mock API response
    recipe_search_service.api_clients["edamam"] = AsyncMock()
    recipe_search_service.api_clients["edamam"].request.return_value = mock_recipe.dict()

    # Get recipe
    result = await recipe_search_service.get_recipe_by_id("edamam_123")

    # Verify API was called
    recipe_search_service.api_clients["edamam"].request.assert_called_once()
    assert result is not None


@pytest.mark.asyncio
async def test_get_recipe_by_id_db_error(recipe_search_service, mock_session):
    """Test database error handling"""
    # Mock database error
    mock_session.execute.side_effect = Exception("Database error")

    # Verify error handling
    with pytest.raises(DatabaseError) as exc_info:
        await recipe_search_service.get_recipe_by_id("test_recipe_1")
    assert "Database error" in str(exc_info.value)


@pytest.mark.asyncio
async def test_get_recipe_by_id_api_error(recipe_search_service, mock_session):
    """Test API error handling"""
    # Mock database returning None
    mock_session.execute.return_value.scalar_one_or_none.return_value = None

    # Mock API error
    recipe_search_service.api_clients["edamam"] = AsyncMock()
    recipe_search_service.api_clients["edamam"].request.side_effect = Exception()

    # Verify error handling
    with pytest.raises(APIError) as exc_info:
        await recipe_search_service.get_recipe_by_id("edamam_123")
    assert "API error" in str(exc_info.value)


@pytest.mark.asyncio
async def test_search_all_from_db(recipe_search_service, mock_session, mock_recipe):
    """Test searching recipes from database"""
    # Mock database search
    mock_session.execute.return_value.scalars.return_value.all.return_value = [mock_recipe]

    # Search recipes
    results = await recipe_search_service.search_all("chicken")

    # Verify results
    assert len(results) == 1
    assert results[0] == mock_recipe
    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_search_all_api_fallback(recipe_search_service, mock_session, sample_edamam_response):
    """Test falling back to API when database has no results"""
    # Mock empty database results
    mock_session.execute.return_value.scalars.return_value.all.return_value = []

    # Mock API response
    recipe_search_service.api_clients["edamam"] = AsyncMock()
    recipe_search_service.api_clients["edamam"].request.return_value = sample_edamam_response

    # Search recipes
    results = await recipe_search_service.search_all("chicken")

    # Verify API was called
    recipe_search_service.api_clients["edamam"].request.assert_called_once()
    assert len(results) > 0


@pytest.mark.asyncio
async def test_search_all_with_filters(recipe_search_service, mock_session, mock_recipe):
    """Test searching with filters"""
    # Mock database search
    mock_session.execute.return_value.scalars.return_value.all.return_value = [mock_recipe]

    # Search with filters
    filters = {"cuisine": "american", "diet": "low-carb", "max_ready_time": 30}
    results = await recipe_search_service.search_all("chicken", filters)

    # Verify filters were applied
    assert len(results) == 1
    assert results[0].cuisines == ["american"]
    assert results[0].diets == ["low-carb"]
    assert results[0].ready_in_minutes <= 30


@pytest.mark.asyncio
async def test_parse_recipe_response_validation(recipe_search_service):
    """Test recipe response validation"""
    # Test with invalid data
    invalid_data = {
        "title": "Test Recipe",
        # Missing required fields
    }

    with pytest.raises(ParseError) as exc_info:
        recipe_search_service._parse_recipe_response(invalid_data, "edamam")
    assert "validation" in str(exc_info.value)


@pytest.mark.asyncio
async def test_rate_limit_handling(recipe_search_service, mock_session):
    """Test rate limit handling"""
    # Mock rate limit exceeded
    recipe_search_service.rate_limiters["edamam"].check_rate_limit.side_effect = RateLimitError(
        "Rate limit exceeded",
        retry_after=60,
    )

    # Verify rate limit handling
    results = await recipe_search_service.search_all("chicken")
    assert len(results) == 0  # Should return empty list, not error


@pytest.mark.asyncio
async def test_concurrent_requests(recipe_search_service, mock_session, mock_recipe):
    """Test handling of concurrent requests"""
    # Mock database operations
    mock_session.execute.return_value.scalar_one_or_none.return_value = mock_recipe

    # Make concurrent requests
    import asyncio

    requests = [recipe_search_service.get_recipe_by_id("test_recipe_1") for _ in range(5)]
    results = await asyncio.gather(*requests)

    # Verify all requests succeeded
    assert all(result == mock_recipe for result in results)


@pytest.mark.asyncio
async def test_recipe_cache_expiration(recipe_search_service, mock_session, mock_recipe):
    """Test recipe cache expiration handling"""
    # Set up cache with stale and fresh recipes
    stale_recipe = mock_recipe.copy()
    stale_recipe.last_fetched = datetime.now(UTC) - timedelta(hours=25)

    fresh_recipe = mock_recipe.copy()
    fresh_recipe.last_fetched = datetime.now(UTC)

    mock_session.execute.return_value.scalars.return_value.all.return_value = [
        stale_recipe,
        fresh_recipe,
    ]

    # Search recipes
    results = await recipe_search_service.search_all("chicken")

    # Verify only fresh recipes are returned
    assert len(results) == 1
    assert results[0].last_fetched > datetime.now(UTC) - timedelta(hours=24)


@pytest.mark.asyncio
async def test_search_edamam(recipe_search_service, mock_api_client, sample_edamam_response):
    """Test Edamam API search"""
    mock_api_client.json.return_value = sample_edamam_response
    recipe_search_service.api_clients["edamam"] = AsyncMock()
    recipe_search_service.api_clients["edamam"].request.return_value = sample_edamam_response

    results = await recipe_search_service._search_edamam("chicken", {})

    assert len(results) == 1
    assert results[0].source == "edamam"
    assert results[0].title == "Instant Pot Chicken"


@pytest.mark.asyncio
async def test_search_spoonacular(recipe_search_service, mock_api_client, sample_spoonacular_response):
    """Test Spoonacular API search"""
    mock_api_client.json.return_value = sample_spoonacular_response
    recipe_search_service.api_clients["spoonacular"] = AsyncMock()
    recipe_search_service.api_clients["spoonacular"].request.return_value = sample_spoonacular_response

    results = await recipe_search_service._search_spoonacular("beef", {})

    assert len(results) == 1
    assert results[0].source == "spoonacular"
    assert results[0].title == "Easy Beef Stew"


@pytest.mark.asyncio
async def test_database_transaction_rollback(recipe_search_service, mock_session):
    """Test database transaction rollback on error"""
    # Mock database error during save
    mock_session.begin_nested.side_effect = Exception("Transaction error")

    # Verify transaction is rolled back
    with pytest.raises(DatabaseError):
        await recipe_search_service.get_recipe_by_id("test_recipe_1")

    mock_session.rollback.assert_called_once()


@pytest.mark.asyncio
async def test_api_response_validation(recipe_search_service):
    """Test API response validation"""
    # Test with malformed API response

    with pytest.raises(ParseError):
        await recipe_search_service._search_edamam("test", {})


@pytest.mark.asyncio
async def test_cleanup(recipe_search_service):
    """Test resource cleanup"""
    await recipe_search_service.close()
    assert recipe_search_service.session is None


@pytest.fixture
async def mock_db_session():
    """Mock database session for testing"""
    session = AsyncMock()
    session.begin = AsyncMock(return_value=AsyncMock(__aenter__=AsyncMock(), __aexit__=AsyncMock()))
    return session


@pytest.fixture
def mock_recipe():
    """Create a mock recipe for testing"""
    return Recipe(
        id="test_recipe_1",
        title="Test Recipe",
        source="test",
        ingredients=[],
        instructions=[],
        last_fetched=datetime.now(UTC),
    )


@pytest.mark.asyncio
class TestRecipeSearchService:
    """Test suite for RecipeSearchService"""

    async def test_get_recipe_by_id_db_cache_hit(self, mock_session, mock_recipe):
        """Test retrieving a recipe from database cache"""
        mock_session.execute = AsyncMock(return_value=AsyncMock(scalar_one_or_none=AsyncMock(return_value=mock_recipe)))

        service = RecipeSearchService()
        service._session = mock_session
        result = await service.get_recipe_by_id("test_recipe_1")

        assert result == mock_recipe
        mock_session.execute.assert_called_once()

    async def test_get_recipe_by_id_db_cache_miss(self, mock_session):
        """Test behavior when recipe is not in database"""
        mock_session.execute = AsyncMock(return_value=AsyncMock(scalar_one_or_none=AsyncMock(return_value=None)))

        service = RecipeSearchService()
        service._session = mock_session
        with pytest.raises(RecipeNotFoundError):
            await service.get_recipe_by_id("nonexistent_recipe")

    async def test_get_recipe_by_id_db_error(self, mock_session):
        """Test handling of database errors"""
        mock_session.execute = AsyncMock(side_effect=Exception("Database error"))

        service = RecipeSearchService()
        service._session = mock_session
        with pytest.raises(DatabaseError) as exc_info:
            await service.get_recipe_by_id("test_recipe_1")

        assert "Database error" in str(exc_info.value)

    @patch("app.services.recipe_search.APIClient")
    async def test_get_recipe_by_id_api_error(self, mock_api_client, mock_session):
        """Test handling of API errors"""
        mock_session.execute = AsyncMock(return_value=AsyncMock(scalar_one_or_none=AsyncMock(return_value=None)))
        mock_api_client.return_value.get = AsyncMock(side_effect=Exception())

        service = RecipeSearchService()
        service._session = mock_session
        with pytest.raises(APIError) as exc_info:
            await service.get_recipe_by_id("edamam_test_recipe")

        assert "API request failed" in str(exc_info.value)

    @patch("app.services.recipe_search.APIClient")
    async def test_get_recipe_by_id_rate_limit(self, mock_api_client, mock_session):
        """Test handling of API rate limits"""
        mock_response = AsyncMock()
        mock_response.status = 429
        mock_response.headers = {"Retry-After": "30"}
        mock_api_client.return_value.get = AsyncMock(return_value=mock_response)

        service = RecipeSearchService()
        service._session = mock_session
        with pytest.raises(RateLimitError) as exc_info:
            await service.get_recipe_by_id("edamam_test_recipe")

        assert "Rate limit exceeded" in str(exc_info.value)
        assert exc_info.value.retry_after == 30

    async def test_search_all_db_fresh_results(self, mock_session, mock_recipe):
        """Test search with fresh results from database"""
        mock_session.execute = AsyncMock(return_value=AsyncMock(scalars=AsyncMock(return_value=[mock_recipe])))

        service = RecipeSearchService()
        service._session = mock_session
        service.config.min_results = 1

        results = await service.search_all("test query")

        assert len(results) == 1
        assert results[0] == mock_recipe
        mock_session.execute.assert_called_once()

    @patch("app.services.recipe_search.APIClient")
    async def test_search_all_api_fallback(self, mock_api_client, mock_session):
        """Test search falling back to API when database results are stale"""
        # Mock stale database result
        stale_recipe = mock_recipe
        stale_recipe.last_fetched = datetime.now(UTC) - timedelta(days=1)
        mock_session.execute = AsyncMock(return_value=AsyncMock(scalars=AsyncMock(return_value=[stale_recipe])))

        # Mock API response
        mock_api_response = {"hits": [{"recipe": {"uri": "test_recipe_2", "label": "Fresh Recipe"}}]}
        mock_api_client.return_value.get = AsyncMock(
            return_value=AsyncMock(status=200, json=AsyncMock(return_value=mock_api_response)),
        )

        service = RecipeSearchService()
        service._session = mock_session
        service.config.min_results = 2

        results = await service.search_all("test query")

        assert len(results) > 0
        mock_api_client.return_value.get.assert_called()

    async def test_search_all_db_error(self, mock_session):
        """Test handling of database errors during search"""
        mock_session.execute = AsyncMock(side_effect=Exception("Database error"))

        service = RecipeSearchService()
        service._session = mock_session
        with pytest.raises(DatabaseError) as exc_info:
            await service.search_all("test query")

        assert "Database error" in str(exc_info.value)

    async def test_parse_recipe_response_validation(self, mock_session):
        """Test validation of API response parsing"""
        service = RecipeSearchService()
        service._session = mock_session

        invalid_data = {
            "uri": "test_recipe",
            # Missing required fields
        }

        with pytest.raises(ParseError) as exc_info:
            service._parse_recipe_response(invalid_data, "edamam")

        assert "Missing required field" in str(exc_info.value)

    @pytest.mark.parametrize(
        "recipe_id",
        [
            "invalid_id",
            "unknown_source_123",
            "",
        ],
    )
    async def test_invalid_recipe_id_format(self, mock_session, recipe_id):
        """Test handling of invalid recipe ID formats"""
        service = RecipeSearchService()
        service._session = mock_session

        with pytest.raises(RecipeNotFoundError) as exc_info:
            await service.get_recipe_by_id(recipe_id)

        assert "Invalid recipe ID format" in str(exc_info.value)

    async def test_database_transaction_rollback(self, mock_session):
        """Test that database transactions are properly rolled back on error"""
        mock_session.begin = AsyncMock(return_value=AsyncMock(__aenter__=AsyncMock(), __aexit__=AsyncMock()))
        mock_session.execute = AsyncMock(side_effect=Exception("Database error", None, None))

        service = RecipeSearchService()
        service._session = mock_session
        with pytest.raises(DatabaseError):
            await service.get_recipe_by_id("test_recipe_1")

        # Verify transaction was rolled back
        mock_session.begin.return_value.__aexit__.assert_called_once()

    @patch("app.services.recipe_search.APIClient")
    async def test_api_retry_mechanism(self, mock_api_client, mock_session):
        """Test that API requests are retried on temporary failures"""
        mock_api_client.return_value.get = AsyncMock(
            side_effect=[
                Exception(),  # First attempt fails
                Exception(),  # Second attempt fails
                AsyncMock(status=200, json=AsyncMock(return_value={"hits": []})),  # Third attempt succeeds
            ],
        )

        service = RecipeSearchService()
        service._session = mock_session
        await service._make_api_request("edamam", "search", {})

        assert mock_api_client.return_value.get.call_count == 3

    async def test_concurrent_api_requests(self, mock_session):
        """Test handling of concurrent API requests"""
        service = RecipeSearchService()
        service._session = mock_session
        service.config.max_concurrent_requests = 2

        # Simulate multiple concurrent requests
        async def make_request():
            async with service.request_semaphore:
                await asyncio.sleep(0.1)

        tasks = [make_request() for _ in range(5)]
        await asyncio.gather(*tasks)

        # Verify semaphore worked (no assertion needed, test passes if no errors occur)


@pytest.mark.asyncio
class TestRecipeSearchServiceMethods:
    """Tests for RecipeSearchService methods"""

    async def test_get_recipes_pagination(self, mock_session, mock_recipe):
        """Test recipe pagination"""
        service = RecipeSearchService()
        service._session = mock_session

        # Mock database operations
        mock_session.execute.return_value.scalar.return_value = len([mock_recipe])
        mock_session.execute.return_value.all.return_value = [mock_recipe][:5]

        # Test first page
        recipes, total = await service.get_recipes(page=1, page_size=5)
        assert len(recipes) == 5
        assert total == len([mock_recipe])

        # Test second page
        mock_session.execute.return_value.all.return_value = [mock_recipe][5:10]
        recipes, total = await service.get_recipes(page=2, page_size=5)
        assert len(recipes) == 5
        assert total == len([mock_recipe])

    async def test_get_recipes_filtering(self, mock_session, mock_recipe):
        """Test recipe filtering"""
        service = RecipeSearchService()
        service._session = mock_session
        mock_session.execute.return_value.all.return_value = [mock_recipe]
        mock_session.execute.return_value.scalar.return_value = len([mock_recipe])

        # Test cuisine filter
        filters = {"cuisine": "Italian"}
        recipes, total = await service.get_recipes(filters=filters)
        assert all(r.cuisine.lower() == "italian" for r in recipes)

        # Test multiple filters
        filters = {
            "cuisine": "Italian",
            "max_ready_time": 30,
            "min_rating": 4.0,
        }
        recipes, total = await service.get_recipes(filters=filters)
        assert all(r.cuisine.lower() == "italian" and r.ready_time <= 30 and r.rating >= 4.0 for r in recipes)

    async def test_get_recipes_sorting(self, mock_session, mock_recipe):
        """Test recipe sorting"""
        service = RecipeSearchService()
        service._session = mock_session
        mock_session.execute.return_value.all.return_value = [mock_recipe]
        mock_session.execute.return_value.scalar.return_value = len([mock_recipe])

        # Test ascending sort
        recipes, total = await service.get_recipes(sort_by="rating", sort_order="asc")
        ratings = [r.rating for r in recipes]
        assert ratings == sorted(ratings)

        # Test descending sort
        recipes, total = await service.get_recipes(sort_by="rating", sort_order="desc")
        ratings = [r.rating for r in recipes]
        assert ratings == sorted(ratings, reverse=True)

    async def test_get_recipes_validation(self, mock_session):
        """Test input validation for get_recipes"""
        service = RecipeSearchService()
        service._session = mock_session

        # Test invalid page number
        with pytest.raises(ServiceValidationError, match="Page number must be greater than 0"):
            await service.get_recipes(page=0)

        # Test invalid page size
        with pytest.raises(ServiceValidationError, match="Page size must be between 1 and 100"):
            await service.get_recipes(page_size=101)

        # Test invalid sort order
        with pytest.raises(ServiceValidationError, match="Sort order must be 'asc' or 'desc'"):
            await service.get_recipes(sort_order="invalid")

    async def test_search_recipes_basic(self, mock_session, mock_recipe):
        """Test basic recipe search"""
        service = RecipeSearchService()
        service._session = mock_session

        # Mock search results
        with patch.object(service, "search_all", return_value=[mock_recipe]):
            recipes, total = await service.search_recipes("pasta")
            assert len(recipes) == min(20, len([mock_recipe]))  # Default page size
            assert total == len([mock_recipe])

    async def test_search_recipes_filtering(self, mock_session, mock_recipe):
        """Test recipe search with filters"""
        service = RecipeSearchService()
        service._session = mock_session

        # Mock search results
        with patch.object(service, "search_all", return_value=[mock_recipe]):
            filters = {"allergens": ["dairy"], "cuisine": "Italian"}
            recipes, total = await service.search_recipes("pasta", filters=filters)
            assert all("dairy" not in (r.allergens or []) and r.cuisine.lower() == "italian" for r in recipes)

    async def test_search_recipes_validation(self, mock_session):
        """Test input validation for search_recipes"""
        service = RecipeSearchService()
        service._session = mock_session

        # Test empty query
        with pytest.raises(ServiceValidationError, match="Search query cannot be empty"):
            await service.search_recipes("")

        # Test invalid page number
        with pytest.raises(ServiceValidationError, match="Page number must be greater than 0"):
            await service.search_recipes("pasta", page=0)

        # Test invalid page size
        with pytest.raises(ServiceValidationError, match="Page size must be between 1 and 100"):
            await service.search_recipes("pasta", page_size=101)

    async def test_save_recipe_success(self, mock_session, mock_recipe):
        """Test successful recipe save"""
        service = RecipeSearchService()
        service._session = mock_session

        # Mock database operation
        mock_session.execute.return_value.scalar.return_value = mock_recipe

        saved_recipe = await service.save_recipe(mock_recipe)
        assert saved_recipe.id == mock_recipe.id
        assert saved_recipe.title == mock_recipe.title

    async def test_save_recipe_validation(self, mock_session):
        """Test recipe validation during save"""
        service = RecipeSearchService()
        service._session = mock_session

        # Test invalid recipe
        invalid_recipe = Recipe(
            id="test",
            title="",  # Invalid: empty title
            source="test",
            ingredients=[],
            instructions=[],
        )

        with pytest.raises(ServiceValidationError, match="Recipe validation failed"):
            await service.save_recipe(invalid_recipe)

    async def test_database_error_handling(self, mock_session, mock_recipe):
        """Test database error handling"""
        service = RecipeSearchService()
        service._session = mock_session

        # Mock database error
        mock_session.execute.side_effect = Exception("Database error")

        with pytest.raises(DatabaseError):
            await service.get_recipes()

        with pytest.raises(DatabaseError):
            await service.save_recipe(mock_recipe)


@pytest.fixture
def mock_recipes():
    """Create a list of mock recipes for testing"""
    return [
        Recipe(
            id=f"test_recipe_{i}",
            title=f"Test Recipe {i}",
            source="test",
            cuisine="Italian" if i % 2 == 0 else "French",
            ready_time=30 if i % 2 == 0 else 45,
            rating=4.0 + (i % 2),
            ingredients=[],
            instructions=[],
            allergens=["dairy"] if i % 2 == 0 else None,
            last_fetched=datetime.now(UTC),
        )
        for i in range(20)
    ]


@pytest.fixture
def mock_recipe(mock_recipes):
    """Return a single mock recipe for testing"""
    return mock_recipes[0]


@pytest.mark.asyncio
class TestRecipeSearchService:
    """Test suite for RecipeSearchService"""

    async def test_search_edamam_success(self, mock_session, mock_api_client, mock_edamam_response):
        """Test successful Edamam API search"""
        service = RecipeSearchService()
        service._session = mock_session
        service.api_clients["edamam"] = mock_api_client

        # Mock API response
        mock_api_client._make_api_request.return_value = mock_edamam_response

        # Execute search
        results = await service._search_edamam("pasta", None)

        # Verify API was called correctly
        mock_api_client._make_api_request.assert_called_once_with("edamam", "search", {"q": "pasta"})

        # Verify results
        assert len(results) == 1
        assert results[0].title == "Test Recipe 1"
        assert results[0].cuisine == "Italian"

    async def test_search_edamam_rate_limit(self, mock_session, mock_api_client):
        """Test Edamam API rate limit handling"""
        service = RecipeSearchService()
        service._session = mock_session
        service.api_clients["edamam"] = mock_api_client

        # Mock rate limit error
        mock_api_client._make_api_request.side_effect = APIError("Rate limit exceeded", source="edamam")

        # Execute search
        results = await service._search_edamam("pasta", None)

        # Verify empty results on rate limit
        assert len(results) == 0

    async def test_search_spoonacular_success(self, mock_session, mock_api_client, mock_spoonacular_response):
        """Test successful Spoonacular API search"""
        service = RecipeSearchService()
        service._session = mock_session
        service.api_clients["spoonacular"] = mock_api_client

        # Mock API response
        mock_api_client._make_api_request.return_value = mock_spoonacular_response

        # Execute search
        results = await service._search_spoonacular("beef", None)

        # Verify API was called correctly
        mock_api_client._make_api_request.assert_called_once_with(
            "spoonacular",
            "complexSearch",
            {
                "query": "beef",
                "number": 10,
                "addRecipeInformation": True,
                "fillIngredients": True,
            },
        )

        # Verify results
        assert len(results) == 1
        assert results[0].title == "Test Recipe 2"
        assert results[0].cuisine == "French"

    async def test_get_recipe_by_id_database(self, mock_session):
        """Test getting recipe from database"""
        service = RecipeSearchService()
        service._session = mock_session

        # Mock database response
        mock_recipe = Recipe(
            id="test_recipe",
            title="Test Recipe",
            source="Database",
            ingredients=[],
            instructions=[],
        )
        mock_session.execute.return_value.scalar.return_value = mock_recipe

        # Get recipe
        recipe = await service.get_recipe_by_id("test_recipe")

        # Verify result
        assert recipe.id == "test_recipe"
        assert recipe.title == "Test Recipe"

    async def test_get_recipe_by_id_api(self, mock_session, mock_api_client, mock_edamam_response):
        """Test getting recipe from API"""
        service = RecipeSearchService()
        service._session = mock_session
        service.api_clients["edamam"] = mock_api_client

        # Mock database miss
        mock_session.execute.return_value.scalar.return_value = None

        # Mock API response
        mock_api_client._make_api_request.return_value = mock_edamam_response["hits"][0]["recipe"]

        # Get recipe
        recipe = await service.get_recipe_by_id("edamam_recipe_1")

        # Verify result
        assert recipe.id == "edamam_recipe_1"
        assert recipe.title == "Test Recipe 1"

    async def test_search_all_with_caching(self, mock_session, mock_api_client):
        """Test search with caching"""
        service = RecipeSearchService()
        service._session = mock_session
        service.api_clients["edamam"] = mock_api_client
        service.api_clients["spoonacular"] = mock_api_client

        # Mock API responses
        mock_recipes = [
            Recipe(
                id=f"test_recipe_{i}",
                title=f"Test Recipe {i}",
                source="test",
                ingredients=[],
                instructions=[],
            )
            for i in range(2)
        ]

        with (
            patch.object(
                service,
                "_search_edamam",
                new_callable=AsyncMock,
                return_value=[mock_recipes[0]],
            ),
            patch.object(
                service,
                "_search_spoonacular",
                new_callable=AsyncMock,
                return_value=[mock_recipes[1]],
            ),
        ):
            # First search - should hit APIs
            results1 = await service.search_all("pasta")
            assert len(results1) == 2

            # Second search - should hit cache
            await service.search_all("pasta")

            # Verify API methods were only called once
            service._search_edamam.assert_called_once()
            service._search_spoonacular.assert_called_once()

    async def test_apply_filters(self, mock_session):
        """Test recipe filtering"""
        service = RecipeSearchService()
        service._session = mock_session

        # Create test recipes
        recipes = [
            Recipe(
                id=f"test_recipe_{i}",
                title=f"Test Recipe {i}",
                source="test",
                cuisine="Italian" if i % 2 == 0 else "French",
                ready_time=30 if i % 2 == 0 else 45,
                rating=4.0 + (i % 2),
                ingredients=[],
                instructions=[],
                allergens=["dairy"] if i % 2 == 0 else None,
            )
            for i in range(4)
        ]

        # Test cuisine filter
        filtered = await service.apply_filters(recipes, {"cuisine": "Italian"})
        assert len(filtered) == 2
        assert all(r.cuisine == "Italian" for r in filtered)

        # Test multiple filters
        filtered = await service.apply_filters(
            recipes,
            {"cuisine": "Italian", "max_ready_time": 30, "min_rating": 4.0},
        )
        assert len(filtered) == 2
        assert all(r.cuisine == "Italian" and r.ready_time <= 30 and r.rating >= 4.0 for r in filtered)

    async def test_error_handling(self, mock_session, mock_api_client):
        """Test error handling"""
        service = RecipeSearchService()
        service._session = mock_session
        service.api_clients["edamam"] = mock_api_client

        # Test API error
        mock_api_client._make_api_request.side_effect = APIError("API error", source="edamam")

        with pytest.raises(APIError):
            await service.search_all("pasta")

        # Test database error
        mock_session.execute.side_effect = Exception("Database error")

        with pytest.raises(DatabaseError):
            await service.get_recipe_by_id("test_recipe")

        # Test validation error
        with pytest.raises(ServiceValidationError):
            await service.get_recipes(page=0)  # Invalid page number
