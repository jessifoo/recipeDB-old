Configuration
=============

The RecipeDB application uses a centralized configuration system based on environment
variables and Pydantic settings management. This ensures type safety, validation,
and easy configuration across different environments.

Environment Setup
---------------

Development
~~~~~~~~~~

For development, create a `.env.development` file:

.. code-block:: bash

   cp .env.example .env.development
   # Edit .env.development with your development settings

Production
~~~~~~~~~

For production, use the main `.env` file:

.. code-block:: bash

   cp .env.example .env
   # Edit .env with production settings
   export ENVIRONMENT=production

Configuration Reference
--------------------

Core Settings
~~~~~~~~~~~

.. code-block:: python

   from app.config import settings

   # Environment and API
   settings.ENVIRONMENT  # Literal["development", "production", "test"]
   settings.PROJECT_NAME  # str: API project name
   settings.API_V1_STR  # str: API version prefix
   settings.VERSION  # str: API version number

Database Configuration
~~~~~~~~~~~~~~~~~~

The database connection can be configured either through individual components or a complete URL:

.. code-block:: python

   # Individual components
   settings.POSTGRES_HOST  # str: Database host
   settings.POSTGRES_PORT  # str: Database port
   settings.POSTGRES_USER  # str: Database user
   settings.POSTGRES_DB  # str: Database name
   settings.POSTGRES_PASSWORD  # str: Database password

   # Complete URL (constructed automatically if not provided)
   settings.DATABASE_URL  # PostgresDsn: Full database URL

Recipe Provider APIs
~~~~~~~~~~~~~~~~

API keys and configuration for external recipe providers:

.. code-block:: python

   # API Keys
   settings.SPOONACULAR_API_KEY  # str: Spoonacular API key
   settings.EDAMAM_APP_ID  # str: Edamam application ID
   settings.EDAMAM_APP_KEY  # str: Edamam application key
   settings.API_NINJAS_API_KEY  # str: API Ninjas key
   settings.TASTY_API_KEY  # str: Tasty API key

   # Rate Limits
   settings.SPOONACULAR_POINTS_PER_DAY  # int: Daily points limit
   settings.SPOONACULAR_REQUESTS_PER_MINUTE  # int: Rate limit
   settings.EDAMAM_REQUESTS_PER_MINUTE  # int: Rate limit
   settings.API_NINJAS_REQUESTS_PER_MINUTE  # int: Rate limit
   settings.TASTY_REQUESTS_PER_MINUTE  # int: Rate limit

Allergen Configuration
~~~~~~~~~~~~~~~~~~

The application includes built-in allergen configuration with API mappings:

.. code-block:: python

   # Get all allergen configurations
   allergens = settings.allergens  # list[AllergenConfig]

   # Get keywords for specific allergen
   dairy_keywords = settings.get_allergen_keywords("dairy")
   # Returns: ["milk", "cream", "cheese", "butter", "yogurt", "casein", "whey"]

   # Get API-specific parameter
   dairy_param = settings.get_allergen_api_param("dairy", "edamam")
   # Returns: "dairy-free"

Each allergen configuration includes:

- Name: Allergen identifier
- Keywords: List of terms indicating allergen presence
- API Mappings: Provider-specific parameter values

Cache Settings
~~~~~~~~~~~

Redis cache configuration:

.. code-block:: python

   settings.REDIS_URL  # str: Redis connection URL
   settings.CACHE_TTL  # int: Cache time-to-live in seconds

Service Configuration
~~~~~~~~~~~~~~~~~

General service settings:

.. code-block:: python

   settings.MAX_CONCURRENT_REQUESTS  # int: Concurrent API requests
   settings.LOG_LEVEL  # str: Logging level (INFO, DEBUG, etc.)
   settings.LOG_FORMAT  # Literal["json", "text"]: Log format
   settings.LOG_FILE  # str: Log file path
   settings.MOCK_RESPONSES  # bool: Use mock API responses
   settings.MOCK_DELAY  # int: Mock response delay
   settings.DEFAULT_RECIPE_PROVIDER  # str: Default provider

Security
~~~~~~~

Security-related settings:

.. code-block:: python

   settings.SECRET_KEY  # str: JWT secret key
   settings.ACCESS_TOKEN_EXPIRE_MINUTES  # int: Token expiry
   settings.ALGORITHM  # str: JWT algorithm (default: "HS256")

CORS Configuration
~~~~~~~~~~~~~~

Cross-Origin Resource Sharing settings:

.. code-block:: python

   # Raw CORS origins string
   settings.BACKEND_CORS_ORIGINS  # str: Comma-separated origins

   # Parsed CORS origins
   origins = settings.cors_origins  # list[AnyHttpUrl]

User Management
~~~~~~~~~~~~

Initial user setup:

.. code-block:: python

   settings.FIRST_SUPERUSER  # str: Admin email
   settings.FIRST_SUPERUSER_PASSWORD  # str: Admin password

Environment Variables
------------------

Required Variables
~~~~~~~~~~~~~~~

These environment variables must be set:

.. code-block:: bash

   # Security
   SECRET_KEY=your_secret_key_here

   # Database
   POSTGRES_PASSWORD=your_database_password

   # API Keys
   SPOONACULAR_API_KEY=your_spoonacular_key
   EDAMAM_APP_ID=your_edamam_id
   EDAMAM_APP_KEY=your_edamam_key
   API_NINJAS_API_KEY=your_api_ninjas_key
   TASTY_API_KEY=your_tasty_key

Optional Variables
~~~~~~~~~~~~~~

These have default values but can be overridden:

.. code-block:: bash

   # Environment
   ENVIRONMENT=development  # or production, test

   # API Settings
   PROJECT_NAME="Recipe Database API"
   API_V1_STR=/api/v1
   VERSION=0.1.0

   # Database
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   POSTGRES_USER=postgres
   POSTGRES_DB=recipe_db

   # Service Configuration
   LOG_LEVEL=INFO
   LOG_FORMAT=json
   CACHE_TTL=3600
   MAX_CONCURRENT_REQUESTS=5

   # Development Options
   MOCK_RESPONSES=false
   MOCK_DELAY=0

Type Safety
---------

The configuration system uses Pydantic for type safety and validation:

.. code-block:: python

   from typing import Literal
   from pydantic import BaseModel, PostgresDsn

   class AllergenConfig(BaseModel):
       name: str
       keywords: list[str]
       api_mappings: dict[str, str]

   class Settings(BaseSettings):
       ENVIRONMENT: Literal["development", "production", "test"]
       DATABASE_URL: PostgresDsn | None
       # ... other typed settings

This ensures:

- Type checking at runtime
- Automatic type conversion
- Validation of values
- IDE support and autocompletion
