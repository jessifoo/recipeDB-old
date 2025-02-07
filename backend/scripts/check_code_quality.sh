#!/bin/bash

# Exit on any error
set -e

echo "Running code quality checks..."

# Run black formatting check
echo "Running black formatting check..."
black --check .

# Run isort import sorting check
echo "Running isort import sorting check..."
isort --check-only .

# Run flake8 linting
echo "Running flake8 linting..."
flake8 .

# Run mypy type checking
echo "Running mypy type checking..."
mypy .

# Run pylint
echo "Running pylint..."
pylint app tests

# Run Python tests
echo "Running Python tests..."
pytest tests/

echo "All code quality checks passed!"
