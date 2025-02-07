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
