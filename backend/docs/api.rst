API Documentation
================

This section contains detailed API documentation for the RecipeDB project.

Core API
-------

.. toctree::
   :maxdepth: 2

   autoapi/app/index

REST API
-------

.. openapi:: ../openapi.json
   :encoding: utf-8
   :examples:

Module Documentation
------------------

Models
~~~~~~

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   app.models

Schemas
~~~~~~~

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   app.schemas

Services
~~~~~~~~

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   app.services

API Routes
~~~~~~~~~

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   app.routes

Utilities
~~~~~~~~

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   app.utils

Configuration
=============

Environment Variables
-------------------

The application uses environment variables for configuration. These can be set in `.env` files or directly in the environment.

Development Setup
~~~~~~~~~~~~~~~~

Copy the example environment file and modify it for development:

.. code-block:: bash

   cp .env.example .env.development
   # Edit .env.development with your settings

Production Setup
~~~~~~~~~~~~~~~

For production, use the main `.env` file:

.. code-block:: bash

   cp .env.example .env
   # Edit .env with production settings
   export ENVIRONMENT=production

Configuration Settings
--------------------

Core Settings
~~~~~~~~~~~~

.. code-block:: python

   from app.config import settings

   # Environment and API
   settings.ENVIRONMENT  # "development", "production", or "test"
   settings.PROJECT_NAME  # API project name
   settings.API_V1_STR  # API version prefix
   settings.VERSION  # API version number

Database Settings
~~~~~~~~~~~~~~~

.. code-block:: python

   # Database configuration
   settings.POSTGRES_HOST  # Database host
   settings.POSTGRES_PORT  # Database port
   settings.POSTGRES_USER  # Database user
   settings.POSTGRES_DB  # Database name
   settings.DATABASE_URL  # Full database URL (constructed automatically)

API Keys
~~~~~~~

.. code-block:: python

   # Recipe API keys
   settings.SPOONACULAR_API_KEY
   settings.EDAMAM_APP_ID
   settings.EDAMAM_APP_KEY
   settings.API_NINJAS_API_KEY
   settings.TASTY_API_KEY

Rate Limits
~~~~~~~~~~

.. code-block:: python

   # API rate limits
   settings.SPOONACULAR_POINTS_PER_DAY
   settings.SPOONACULAR_REQUESTS_PER_MINUTE
   settings.EDAMAM_REQUESTS_PER_MINUTE
   settings.API_NINJAS_REQUESTS_PER_MINUTE
   settings.TASTY_REQUESTS_PER_MINUTE

Cache Settings
~~~~~~~~~~~~

.. code-block:: python

   # Cache configuration
   settings.REDIS_URL  # Redis connection URL
   settings.CACHE_TTL  # Cache time-to-live in seconds

Service Configuration
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Service settings
   settings.MAX_CONCURRENT_REQUESTS
   settings.LOG_LEVEL
   settings.LOG_FORMAT
   settings.LOG_FILE
   settings.MOCK_RESPONSES
   settings.MOCK_DELAY
   settings.DEFAULT_RECIPE_PROVIDER

Allergen Configuration
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get allergen information
   allergens = settings.allergens  # List of AllergenConfig objects

   # Get allergen keywords
   dairy_keywords = settings.get_allergen_keywords("dairy")

   # Get API-specific allergen parameter
   dairy_param = settings.get_allergen_api_param("dairy", "edamam")  # Returns "dairy-free"

CORS Configuration
~~~~~~~~~~~~~~~

.. code-block:: python

   # CORS settings
   settings.BACKEND_CORS_ORIGINS  # Comma-separated list of allowed origins
   origins = settings.cors_origins  # List of parsed URLs

Security
~~~~~~~

.. code-block:: python

   # Security settings
   settings.SECRET_KEY  # JWT secret key
   settings.ACCESS_TOKEN_EXPIRE_MINUTES  # Token expiry time
   settings.ALGORITHM  # JWT algorithm

User Management
~~~~~~~~~~~~~

.. code-block:: python

   # User management
   settings.FIRST_SUPERUSER  # Initial admin email
   settings.FIRST_SUPERUSER_PASSWORD  # Initial admin password

API Reference
============

Recipe Search
------------

.. http:get:: /api/v1/recipe-search

   Search for recipes with allergen filtering.

   **Example request**:

   .. sourcecode:: http

      GET /api/v1/recipe-search?query=chicken&allergens=dairy,soy,egg HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "results": [
          {
            "id": "123",
            "title": "Allergen-Free Chicken Recipe",
            "ingredients": [...],
            "instructions": [...],
            "allergens": {
              "dairy_free": true,
              "soy_free": true,
              "egg_free": true
            }
          }
        ],
        "total": 1
      }

   :query query: Recipe search query
   :query allergens: Comma-separated list of allergens to exclude
   :query cuisine: Optional cuisine type filter
   :query meal_type: Optional meal type filter
   :statuscode 200: No error
   :statuscode 400: Invalid request parameters
   :statuscode 401: Authentication required
   :statuscode 429: Rate limit exceeded
