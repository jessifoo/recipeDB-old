.. RecipeDB documentation master file, created by
   sphinx-quickstart on Thu Feb  6 13:27:12 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

RecipeDB Documentation
=====================

RecipeDB is a FastAPI-based recipe management system with features for searching,
storing, and managing recipes, meal plans, and related data. It includes robust
allergen filtering and integration with multiple recipe providers.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   installation
   quickstart
   configuration
   api
   contributing
   changelog

Features
--------

* Recipe search with allergen filtering
* Multiple recipe provider integrations (Edamam, Spoonacular, etc.)
* Meal planning and organization
* User dietary preferences and restrictions
* Ingredient substitutions
* Recipe scaling and unit conversion
* API-first design with OpenAPI/Swagger documentation

Quick Start
----------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/yourusername/recipedb.git
      cd recipedb/backend

2. Set up environment:

   .. code-block:: bash

      cp .env.example .env.development
      # Edit .env.development with your settings

3. Install dependencies:

   .. code-block:: bash

      poetry install

4. Run the development server:

   .. code-block:: bash

      poetry run uvicorn app.main:app --reload

5. Visit the API documentation:

   http://localhost:8000/docs

Configuration
------------

The application uses a centralized configuration system based on environment variables.
See the :doc:`configuration` section for detailed settings and options.

Example usage:

.. code-block:: python

   from app.config import settings

   # Access configuration
   db_url = settings.DATABASE_URL
   api_key = settings.SPOONACULAR_API_KEY

   # Get allergen information
   allergens = settings.allergens
   dairy_param = settings.get_allergen_api_param("dairy", "edamam")

API Reference
------------

The API documentation provides detailed information about available endpoints,
request/response formats, and authentication. See the :doc:`api` section.

Contributing
-----------

We welcome contributions! Please see our :doc:`contributing` guide for details
on how to get involved.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
