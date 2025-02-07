Quickstart Guide
===============

This guide will help you get started with using RecipeDB.

First Steps
----------

After :doc:`installation`, you can start using RecipeDB. Here's a quick overview of the basic operations.

Authentication
-------------

1. Create a new user account:

.. code-block:: bash

   curl -X POST "http://localhost:8000/api/v1/auth/register" \
   -H "Content-Type: application/json" \
   -d '{
       "email": "user@example.com",
       "password": "securepassword",
       "username": "foodlover"
   }'

2. Login to get an access token:

.. code-block:: bash

   curl -X POST "http://localhost:8000/api/v1/auth/login" \
   -H "Content-Type: application/json" \
   -d '{
       "email": "user@example.com",
       "password": "securepassword"
   }'

Managing Recipes
--------------

Create a Recipe
~~~~~~~~~~~~~

.. code-block:: bash

   curl -X POST "http://localhost:8000/api/v1/recipes" \
   -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{
       "title": "Chocolate Chip Cookies",
       "description": "Classic homemade chocolate chip cookies",
       "ingredients": [
           {
               "name": "all-purpose flour",
               "amount": 2.25,
               "unit": "cups"
           },
           {
               "name": "chocolate chips",
               "amount": 2,
               "unit": "cups"
           }
       ],
       "instructions": [
           "Preheat oven to 375°F",
           "Mix ingredients",
           "Bake for 10-12 minutes"
       ],
       "prep_time": 15,
       "cook_time": 12,
       "servings": 24
   }'

List Recipes
~~~~~~~~~~

.. code-block:: bash

   curl "http://localhost:8000/api/v1/recipes" \
   -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

Search Recipes
~~~~~~~~~~~~

Search by title or ingredients:

.. code-block:: bash

   curl "http://localhost:8000/api/v1/recipes/search?query=chocolate" \
   -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

Filter recipes:

.. code-block:: bash

   curl "http://localhost:8000/api/v1/recipes/search?prep_time_max=30&cuisine=italian" \
   -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

User Profile
-----------

View Profile
~~~~~~~~~~

.. code-block:: bash

   curl "http://localhost:8000/api/v1/users/me" \
   -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

Update Profile
~~~~~~~~~~~~

.. code-block:: bash

   curl -X PATCH "http://localhost:8000/api/v1/users/me" \
   -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{
       "name": "John Doe",
       "bio": "Food enthusiast and home chef"
   }'

Using the Web Interface
---------------------

The web interface is available at ``http://localhost:3000`` and provides a user-friendly way to:

1. Browse and search recipes
2. Create and edit your recipes
3. Manage your profile
4. Interact with other users

Next Steps
---------

* Explore the complete :doc:`api` documentation
* Learn about :doc:`advanced_features`
* Join our community and :doc:`contributing`
