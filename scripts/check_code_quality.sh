#!/bin/bash

# Set error handling
set -e

# Function to print section headers
print_header() {
    echo -e "\n📋 $1"
    echo "----------------------------------------"
}

echo "🔍 Running code quality checks..."

# Check and activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Python code quality checks
if [ -d "backend" ]; then
    print_header "Running Python checks"

    # First pass: Auto-fixes
    echo "Running autoflake to remove unused imports..."
    find backend/ -type f -name "*.py" ! -path "*/migrations/*" ! -path "*/.pytest_cache/*" ! -path "*/venv/*" ! -path "*/.git/*" -exec autoflake --in-place --remove-all-unused-imports --remove-unused-variables {} \;

    echo "Running pyupgrade to modernize Python syntax..."
    find backend/ -type f -name "*.py" ! -path "*/migrations/*" ! -path "*/.pytest_cache/*" ! -path "*/venv/*" ! -path "*/.git/*" -exec pyupgrade --py311-plus {} \;

    echo "Running isort..."
    isort backend/ --skip venv --skip .git

    # Final formatting pass with Black
    echo "Running Black formatter..."
    black backend/ --exclude="venv|\.git" --line-length 79

    # Linting and type checking
    echo "Running Flake8 linter..."
    flake8 backend/ --exclude=venv,.git

    echo "Running MyPy type checker..."
    mypy backend/

    echo "Running Pylint..."
    pylint backend/app/ backend/tests/

    print_header "Running Python tests"
    python -m pytest
else
    echo "⚠️ No backend directory found"
fi

# Frontend checks
if [ -d "frontend" ]; then
    print_header "Running frontend checks"

    # Run Biome formatter and linter
    if command -v biome >/dev/null 2>&1; then
        echo "Running Biome..."
        biome check frontend/
        biome format --write frontend/
    else
        echo "⚠️ Biome not found, skipping frontend checks"
    fi

    # Run TypeScript type checking
    if [ -f "frontend/tsconfig.json" ]; then
        echo "Running TypeScript type checker..."
        cd frontend && npm run type-check && cd ..
    else
        echo "⚠️ No TypeScript configuration found"
    fi

    # Run frontend tests
    if [ -f "frontend/package.json" ]; then
        echo "Running frontend tests..."
        cd frontend && npm test && cd ..
    else
        echo "⚠️ No frontend tests found"
    fi
else
    echo "⚠️ No frontend directory found"
fi

echo -e "\n✅ All checks completed!"
