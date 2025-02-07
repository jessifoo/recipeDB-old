Contributing Guide
=================

We love your input! We want to make contributing to RecipeDB as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

Development Process
-----------------

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. Fork the repo and create your branch from ``main``.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

Pull Request Process
------------------

1. Update the README.md with details of changes to the interface, if applicable.
2. Update the docs/ folder with any new documentation.
3. The PR will be merged once you have the sign-off of two other developers.

Development Setup
---------------

1. Clone your fork:

   .. code-block:: bash

      git clone git@github.com:your-username/recipedb.git

2. Add the main repository as remote:

   .. code-block:: bash

      git remote add upstream https://github.com/original/recipedb.git

3. Install development dependencies:

   .. code-block:: bash

      cd backend
      poetry install --with dev

4. Install pre-commit hooks:

   .. code-block:: bash

      pre-commit install

Code Style
---------

We use several tools to maintain code quality:

* ``ruff`` for linting and formatting
* ``mypy`` for type checking
* ``black`` for code formatting
* ``isort`` for import sorting

Run the following before committing:

.. code-block:: bash

   poetry run ruff check .
   poetry run mypy .
   poetry run black .
   poetry run isort .

Testing
-------

We use pytest for testing. To run tests:

.. code-block:: bash

   poetry run pytest

For coverage report:

.. code-block:: bash

   poetry run pytest --cov=app --cov-report=html

Documentation
------------

We use Sphinx for documentation. To build docs:

.. code-block:: bash

   cd docs
   poetry run make html

View the built documentation in ``docs/_build/html/index.html``.

Reporting Bugs
------------

We use GitHub issues to track public bugs. Report a bug by opening a new issue.

Write bug reports with detail, background, and sample code:

* A quick summary and/or background
* Steps to reproduce
  - Be specific!
  - Give sample code if you can.
* What you expected would happen
* What actually happens
* Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

Feature Requests
--------------

We love feature requests! Please use GitHub issues to suggest features:

1. Check if the feature has already been requested
2. Provide a clear and detailed explanation of the feature
3. Explain why this enhancement would be useful
4. Be aware that features may not get implemented immediately

License
-------

By contributing, you agree that your contributions will be licensed under its MIT License.
