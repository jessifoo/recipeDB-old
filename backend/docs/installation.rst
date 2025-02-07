Installation Guide
=================

This guide will help you set up RecipeDB on your system.

Prerequisites
------------

Before installing RecipeDB, ensure you have the following prerequisites:

* Python 3.11 or higher
* Poetry (Python package manager)
* PostgreSQL 14 or higher
* Redis (for caching)

System Requirements
-----------------

* Operating System: Linux, macOS, or Windows
* Memory: 4GB RAM minimum
* Storage: 1GB free disk space

Installation Steps
----------------

1. Clone the Repository
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/yourusername/recipedb.git
   cd recipedb

2. Install Dependencies
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd backend
   poetry install

3. Configure Environment Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a `.env` file in the project root with the following variables:

.. code-block:: bash

   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/recipedb
   REDIS_URL=redis://localhost:6379/0
   SECRET_KEY=your-secret-key
   ENVIRONMENT=development

4. Initialize the Database
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   poetry run alembic upgrade head

5. Start the Development Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   poetry run uvicorn app.main:app --reload

The API will be available at ``http://localhost:8000``.

Docker Installation
-----------------

Alternatively, you can use Docker Compose:

.. code-block:: bash

   docker-compose up -d

This will start all required services:

* API server
* PostgreSQL database
* Redis cache
* Documentation server

Troubleshooting
-------------

Common Issues
~~~~~~~~~~~~

1. Database Connection Issues

   * Ensure PostgreSQL is running
   * Verify database credentials in `.env`
   * Check network connectivity

2. Dependencies Installation Fails

   * Update Poetry to the latest version
   * Clear Poetry cache: ``poetry cache clear . --all``
   * Try with a fresh virtual environment

3. Port Conflicts

   * Check if ports 8000 (API) or 5432 (PostgreSQL) are in use
   * Modify port mappings in `docker-compose.yml` if needed

Getting Help
~~~~~~~~~~

If you encounter any issues:

1. Check the :doc:`troubleshooting` guide
2. Search existing GitHub issues
3. Create a new issue with detailed information about your problem

Next Steps
---------

After installation:

* Follow the :doc:`quickstart` guide
* Read the :doc:`api` documentation
* Review :doc:`contributing` if you want to contribute
