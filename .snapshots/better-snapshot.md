Enter your prompt here

# Project Structure

├─ 📁 backend
  ├─ 📁 _gemini_code_review
    └─ manifest.json
    └─ app.py.review.json
    └─ setup.py.review.json
  ├─ 📁 config
    ├─ 📁 schemas
      └─ api.py
    └─ default.yaml
    └─ development.yaml
    └─ production.yaml
  ├─ 📁 migrations
    ├─ 📁 versions
      └─ 01afbfc26ab3_initial_migration.py
    └─ README
    └─ env.py
    └─ script.py.mako
  ├─ 📁 app
    ├─ 📁 models
      └─ __init__.py
      └─ models.py
      └─ recipe.py
    ├─ 📁 routes
      └─ routes.py
      └─ __init__.py
    ├─ 📁 services
      ├─ 📁 recipe_providers
        └─ spoonacular.py
        └─ mealdb.py
        └─ base.py
        └─ tasty.py
        └─ mock.py
        └─ recipe_puppy.py
        └─ factory.py
        └─ api_ninjas.py
        └─ __init__.py
        └─ edamam.py
      └─ recipe_service.py
      └─ __init__.py
      └─ recipe_search.py
    ├─ 📁 api
      ├─ 📁 routes
        ├─ 📁 search
          └─ __init__.py
          └─ recipe_search.py
        └─ recipe_search.py
        └─ ingredients.py
        └─ dietary_restrictions.py
        └─ allergens.py
        └─ family_members.py
        └─ recipes.py
        └─ protein_types.py
        └─ meal_types.py
        └─ cook_methods.py
        └─ __init__.py
        └─ cuisine_types.py
        └─ meal_plans.py
      ├─ 📁 endpoints
        └─ recipes.py
      └─ __init__.py
      └─ deps.py
    ├─ 📁 providers
      ├─ 📁 recipe
        └─ base.py
        └─ exceptions.py
        └─ http.py
    ├─ 📁 db
      └─ base.py
      └─ __init__.py
      └─ session.py
      └─ base_class.py
      └─ database.py
    ├─ 📁 schemas
      └─ base.py
      └─ recipe.py
      └─ __init__.py
      └─ models.py
    ├─ 📁 config
      └─ __init__.py
      └─ api_config.py
    ├─ 📁 core
      └─ error_messages.py
      └─ error_codes.py
      └─ error_handlers.py
      └─ exceptions.py
      └─ __init__.py
      └─ constants.py
      └─ config.py
      └─ exceptions.test.py
    ├─ 📁 routers
      └─ __init__.py
    ├─ 📁 database
      └─ __init__.py
      └─ session.py
    └─ main.py
    └─ py.typed
    └─ __init__.py
    └─ config.py
  └─ setup.cfg
  └─ app.py
  └─ .python-version
  └─ README.md
  └─ __init__.py
  └─ pyproject.toml
  └─ Dockerfile
  └─ alembic.ini
  └─ pytest.ini
├─ 📁 frontend
  ├─ 📁 theme
    ├─ 📁 components
      └─ recipe-card.ts
      └─ index.ts
      └─ card.ts
      └─ recipe.ts
    ├─ 📁 foundations
      └─ spacing.ts
      └─ typography.ts
      └─ index.ts
      └─ breakpoints.ts
      └─ colors.ts
    └─ index.ts
  ├─ 📁 services
    ├─ 📁 api
      ├─ 📁 _gemini_code_review
        └─ BaseApiClient.ts.review.json
        └─ manifest.json
      ├─ 📁 errors
        └─ ApiError.ts
      └─ BaseApiClient.ts
      └─ SpoonacularApiClient.ts
    └─ api.ts
  ├─ 📁 stores
    └─ globalStore.ts
    └─ recipeStore.ts
    └─ userPreferencesStore.ts
    └─ apiConfigStore.ts
    └─ uiStore.ts
    └─ mealPlanStore.ts
    └─ familyProfileStore.ts
  ├─ 📁 pages
    ├─ 📁 recipes
      └─ index.tsx
    └─ _app.tsx
    └─ recipes.tsx
  ├─ 📁 .storybook
    └─ preview.tsx
    └─ main.ts
  ├─ 📁 __tests__
    ├─ 📁 utils
      └─ test-utils.tsx
    ├─ 📁 mocks
      └─ mockStores.ts
    ├─ 📁 components
      └─ RecipeCard.test.tsx
    └─ RecipeList.test.tsx
    └─ RecipeCuration.test.tsx
  ├─ 📁 hooks
    ├─ 📁 api
      └─ useIngredients.ts
      └─ useRecipeSearch.ts
      └─ useRecipes.ts
    └─ useRecipeSearch.ts
    └─ useBreakpointValue.ts
    └─ useRecipes.ts
    └─ useAppState.ts
    └─ useThemeTokens.ts
    └─ useFilteredRecipes.ts
  ├─ 📁 components
    ├─ 📁 recipe
      └─ RecipeActions.tsx
      └─ RecipeCardSkeleton.tsx
      └─ RecipeFilters.tsx
      └─ RecipeMetadata.tsx
      └─ RecipeAllergenBadges.tsx
      └─ RecipeDetail.tsx
      └─ RecipeGrid.tsx
      └─ RecipeCard.tsx
      └─ RecipeSearch.tsx
    ├─ 📁 ui
      ├─ 📁 Container
        └─ index.tsx
      ├─ 📁 Card
        └─ index.tsx
      └─ index.ts
      └─ Card.tsx
    ├─ 📁 atoms
      ├─ 📁 Button
        └─ Button.tsx
        └─ index.ts
      ├─ 📁 Image
        └─ RecipeImage.tsx
    ├─ 📁 layout
      └─ PageLayout.tsx
    ├─ 📁 api
      └─ ApiConfigPanel.tsx
    ├─ 📁 family
      └─ FamilyProfileManager.tsx
    ├─ 📁 meal
      └─ MealPlanner.tsx
    └─ RecipeList.tsx
  ├─ 📁 utils
    └─ react-query.ts
    └─ api.ts
    └─ filters.ts
    └─ responsive.ts
  ├─ 📁 app
    ├─ 📁 recipes
      ├─ 📁 [id]
        └─ page.tsx
      └─ page.tsx
    ├─ 📁 components
      ├─ 📁 organisms
        └─ RecipeGrid.tsx
      ├─ 📁 molecules
        └─ RecipeCard.tsx
      ├─ 📁 atoms
        └─ RecipeImage.tsx
        └─ RecipeMetadata.tsx
      └─ RecipeSearch.tsx
    └─ providers.tsx
    └─ page.tsx
    └─ layout.tsx
  ├─ 📁 types
    └─ api.ts
    └─ utils.ts
    └─ recipe.ts
  ├─ 📁 mocks
    ├─ 📁 handlers
      └─ recipes.ts
    ├─ 📁 data
      └─ recipes.ts
    └─ index.ts
    └─ handlers.ts
    └─ browser.ts
    └─ recipeData.ts
  └─ .prettierrc
  └─ .eslintrc.json
  └─ biome.json
  └─ playwright.config.ts
  └─ tsconfig.json
  └─ package.json
  └─ jest.setup.ts
  └─ types.ts
  └─ next-env.d.ts
  └─ jest.config.js
  └─ router.ts
  └─ jest.setup.js
└─ commitlint.config.js
└─ recipe-db.code-workspace
└─ .python-version
└─ package.json
└─ README.md
└─ .editorconfig
└─ .pre-commit-config.yaml


# Project Files

- package.json
- commitlint.config.js
- recipe-db.code-workspace
- .python-version
- README.md
- .editorconfig
- backend/setup.cfg
- backend/app.py
- backend/.python-version
- backend/README.md
- backend/__init__.py
- backend/pyproject.toml
- backend/Dockerfile
- backend/alembic.ini
- backend/_gemini_code_review/manifest.json
- backend/_gemini_code_review/app.py.review.json
- backend/_gemini_code_review/setup.py.review.json
- backend/config/default.yaml
- backend/config/schemas/api.py
- backend/config/development.yaml
- backend/config/production.yaml
- backend/pytest.ini
- backend/app/main.py
- backend/app/py.typed
- backend/app/routes/routes.py
- backend/app/api/routes/ingredients.py
- backend/app/api/routes/dietary_restrictions.py
- backend/app/api/routes/allergens.py
- backend/app/api/routes/family_members.py
- backend/app/api/routes/recipes.py
- backend/app/api/routes/protein_types.py
- backend/app/api/routes/meal_types.py
- backend/app/api/routes/search/__init__.py
- backend/app/api/routes/search/recipe_search.py
- backend/app/api/routes/cook_methods.py
- backend/app/api/routes/__init__.py
- backend/app/api/routes/cuisine_types.py
- backend/app/api/routes/meal_plans.py
- backend/app/api/routes/recipe_search.py
- backend/app/routes/__init__.py
- backend/app/api/__init__.py
- backend/migrations/README
- backend/app/services/recipe_service.py
- backend/app/db/base.py
- backend/app/api/endpoints/recipes.py
- backend/app/db/__init__.py
- backend/app/db/session.py
- backend/app/db/base_class.py
- backend/app/db/database.py
- backend/app/services/__init__.py
- backend/app/services/recipe_search.py
- backend/migrations/env.py
- backend/migrations/script.py.mako
- backend/app/api/deps.py
- backend/app/services/recipe_providers/mock.py
- backend/app/services/recipe_providers/base.py
- backend/app/services/recipe_providers/mealdb.py
- backend/app/services/recipe_providers/spoonacular.py
- backend/app/services/recipe_providers/tasty.py
- backend/app/services/recipe_providers/recipe_puppy.py
- backend/app/services/recipe_providers/factory.py
- backend/app/services/recipe_providers/api_ninjas.py
- backend/app/services/recipe_providers/__init__.py
- backend/app/services/recipe_providers/edamam.py
- backend/migrations/versions/01afbfc26ab3_initial_migration.py
- backend/app/schemas/base.py
- backend/app/schemas/recipe.py
- backend/app/schemas/__init__.py
- backend/app/schemas/models.py
- backend/app/__init__.py
- backend/app/providers/recipe/http.py
- backend/app/models/recipe.py
- backend/app/providers/recipe/base.py
- backend/app/models/__init__.py
- backend/app/models/models.py
- backend/app/providers/recipe/exceptions.py
- backend/app/config/api_config.py
- backend/app/core/error_codes.py
- backend/app/core/error_handlers.py
- backend/app/core/exceptions.py
- backend/app/core/__init__.py
- backend/app/core/constants.py
- backend/app/core/config.py
- backend/app/core/exceptions.test.py
- backend/app/core/error_messages.py
- backend/app/config/__init__.py
- backend/app/config.py
- backend/app/database/__init__.py
- backend/app/database/session.py
- backend/app/routers/__init__.py
- .pre-commit-config.yaml
- frontend/.eslintrc.json
- frontend/__tests__/RecipeList.test.tsx
- frontend/__tests__/RecipeCuration.test.tsx
- frontend/__tests__/utils/test-utils.tsx
- frontend/__tests__/components/RecipeCard.test.tsx
- frontend/services/api.ts
- frontend/services/api/BaseApiClient.ts
- frontend/services/api/SpoonacularApiClient.ts
- frontend/__tests__/mocks/mockStores.ts
- frontend/services/api/errors/ApiError.ts
- frontend/services/api/_gemini_code_review/manifest.json
- frontend/services/api/_gemini_code_review/BaseApiClient.ts.review.json
- frontend/biome.json
- frontend/playwright.config.ts
- frontend/tsconfig.json
- frontend/.prettierrc
- frontend/pages/_app.tsx
- frontend/theme/index.ts
- frontend/theme/components/recipe.ts
- frontend/hooks/useFilteredRecipes.ts
- frontend/theme/components/card.ts
- frontend/hooks/useThemeTokens.ts
- frontend/theme/components/index.ts
- frontend/theme/components/recipe-card.ts
- frontend/hooks/useRecipeSearch.ts
- frontend/hooks/useBreakpointValue.ts
- frontend/hooks/useRecipes.ts
- frontend/hooks/useAppState.ts
- frontend/theme/foundations/spacing.ts
- frontend/theme/foundations/typography.ts
- frontend/theme/foundations/index.ts
- frontend/theme/foundations/breakpoints.ts
- frontend/theme/foundations/colors.ts
- frontend/pages/recipes/index.tsx
- frontend/pages/recipes.tsx
- frontend/hooks/api/useIngredients.ts
- frontend/hooks/api/useRecipeSearch.ts
- frontend/hooks/api/useRecipes.ts
- frontend/package.json
- frontend/jest.setup.ts
- frontend/components/api/ApiConfigPanel.tsx
- frontend/components/meal/MealPlanner.tsx
- frontend/components/RecipeList.tsx
- frontend/components/family/FamilyProfileManager.tsx
- frontend/components/recipe/RecipeActions.tsx
- frontend/components/recipe/RecipeCardSkeleton.tsx
- frontend/components/recipe/RecipeFilters.tsx
- frontend/components/recipe/RecipeMetadata.tsx
- frontend/components/recipe/RecipeAllergenBadges.tsx
- frontend/components/recipe/RecipeDetail.tsx
- frontend/components/recipe/RecipeGrid.tsx
- frontend/components/recipe/RecipeCard.tsx
- frontend/components/recipe/RecipeSearch.tsx
- frontend/components/layout/PageLayout.tsx
- frontend/types.ts
- frontend/next-env.d.ts
- frontend/components/atoms/Button/index.ts
- frontend/components/atoms/Button/Button.tsx
- frontend/components/atoms/Image/RecipeImage.tsx
- frontend/utils/react-query.ts
- frontend/utils/api.ts
- frontend/utils/filters.ts
- frontend/utils/responsive.ts
- frontend/components/ui/index.ts
- frontend/components/ui/Card.tsx
- frontend/components/ui/Container/index.tsx
- frontend/components/ui/Card/index.tsx
- frontend/jest.config.js
- frontend/router.ts
- frontend/jest.setup.js
- frontend/app/providers.tsx
- frontend/app/page.tsx
- frontend/app/layout.tsx
- frontend/app/recipes/page.tsx
- frontend/.storybook/preview.tsx
- frontend/.storybook/main.ts
- frontend/app/recipes/[id]/page.tsx
- frontend/app/components/RecipeSearch.tsx
- frontend/types/api.ts
- frontend/types/utils.ts
- frontend/types/recipe.ts
- frontend/app/components/atoms/RecipeMetadata.tsx
- frontend/app/components/atoms/RecipeImage.tsx
- frontend/app/components/molecules/RecipeCard.tsx
- frontend/app/components/organisms/RecipeGrid.tsx
- frontend/stores/recipeStore.ts
- frontend/stores/globalStore.ts
- frontend/stores/userPreferencesStore.ts
- frontend/stores/apiConfigStore.ts
- frontend/stores/uiStore.ts
- frontend/stores/mealPlanStore.ts
- frontend/stores/familyProfileStore.ts
- frontend/mocks/index.ts
- frontend/mocks/handlers.ts
- frontend/mocks/browser.ts
- frontend/mocks/recipeData.ts
- frontend/mocks/handlers/recipes.ts
- frontend/mocks/data/recipes.ts

## package.json
```
{
  "name": "fpies-recipe-platform",
  "version": "1.0.0",
  "description": "A modern recipe platform for families managing FPIES and food allergies",
  "scripts": {
    "prepare": "cd frontend && npm install && husky install",
    "frontend": "cd frontend && npm run dev",
    "backend:setup": "cd backend && python -m venv venv && . venv/bin/activate && poetry install",
    "backend": "cd backend && . venv/bin/activate && fastapi run",
    "dev": "concurrently \"npm run frontend\" \"npm run backend\"",
    "clean": "rm -rf frontend/node_modules backend/venv",
    "setup": "npm install && npm run backend:setup && npm run prepare",
    "lint": "cd frontend && npm run lint",
    "lint:fix": "cd frontend && npm run lint:fix",
    "test": "npm run test:frontend && npm run test:backend",
    "test:frontend": "cd frontend && npm test",
    "test:backend": "cd backend && pytest",
    "type-check": "cd frontend && npm run type-check",
    "format": "cd frontend && npm run format",
    "format:check": "cd frontend && npm run format:check",
    "precommit": "lint-staged && npm run type-check",
    "commit": "cz"
  },
  "devDependencies": {
    "@commitlint/cli": "^18.4.3",
    "@commitlint/config-conventional": "^18.4.3",
    "@typescript-eslint/eslint-plugin": "^7.18.0",
    "@typescript-eslint/parser": "^7.18.0",
    "commitizen": "^4.3.0",
    "concurrently": "^8.2.2",
    "cz-conventional-changelog": "^3.3.0",
    "eslint-config-airbnb": "^19.0.4",
    "eslint-config-airbnb-typescript": "^18.0.0",
    "eslint-plugin-import": "^2.31.0",
    "eslint-plugin-jsdoc": "^50.6.3",
    "eslint-plugin-jsx-a11y": "^6.10.2",
    "eslint-plugin-react": "^7.37.4",
    "eslint-plugin-react-hooks": "^5.1.0",
    "husky": "^8.0.3",
    "lint-staged": "^15.2.0"
  },
  "config": {
    "commitizen": {
      "path": "./node_modules/cz-conventional-changelog"
    }
  },
  "lint-staged": {
    "frontend/**/*.{js,jsx,ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ]
  }
}

```

## commitlint.config.js
```
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat',     // New feature
        'fix',      // Bug fix
        'docs',     // Documentation
        'style',    // Formatting, missing semi colons, etc
        'refactor', // Code change that neither fixes a bug nor adds a feature
        'perf',     // Performance improvements
        'test',     // Adding tests
        'chore',    // Maintain
        'revert',   // Revert changes
        'wip'       // Work in progress
      ]
    ],
    'subject-case': [0]
  }
};

```

## recipe-db.code-workspace
```
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "codium.codeCompletion.enable": false,
    "codeQL.createQuery.qlPackLocation": "/Users/jessicajohnson/CascadeProjects/windsurf-project",
    "Codegeex.CommitMessageStyle": "Default",
    "Codegeex.SidebarUI.LanguagePreference": "English",
    "Codegeex.Chat.LanguagePreference": "English",
    "Codegeex.Comment.LanguagePreference": "English",
    "Codegeex.CommitMessage.LanguagePreference": "English",
    "Codegeex.RepoIndex": true,
    "python.createEnvironment.contentButton": "show",
    "python.terminal.executeInFileDir": true,
    "python.testing.cwd": "/backend/tests",
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": true,
    "python.terminal.launchArgs": ["zsh"],
    "terminal.integrated.env.osx": {
      "VIRTUAL_ENV": "${workspaceFolder}/backend/.venv"
    },
    "terminal.integrated.accessibleViewFocusOnCommandExecution": false,
    "terminal.integrated.defaultProfile.osx": "zsh (2)",
    "terminal.integrated.sendKeybindingsToShell": true
  }
}

```

## .python-version
```
3.11.0

```

## README.md
```
# FPIES-Friendly Recipe Platform


A modern recipe platform designed for families managing FPIES and food allergies.
Built with Next.js 14 and FastAPi.

## Tech Stack

### Frontend

- Next.js 14 with App Router
- TypeScript for type safety
- Tailwind CSS for styling
- Modern React patterns and hooks

### Backend

- FASTApi for the REST API
- SQLAlchemy for database operations
- PostgreSQL for data storage
- Redis for high-performance caching

## Features

- Search and filter recipes by allergens
- Track liked recipes
- Modern, responsive UI
- Type-safe development
- Fast, server-side rendered pages

## Recipe Management

### Viewing Recipes

The application provides a modern, filterable interface for viewing recipes at `/recipes`. Features include:

- **Recipe Cards**: Each recipe is displayed as a card showing:

  - Title and meal type
  - Cooking method and times
  - Preview image (when available)
  - Allergen information (dairy-free, soy-free, etc.)

- **Filtering Options**:
  - Search by recipe title
  - Filter by meal type (breakfast, lunch, dinner, etc.)
  - Filter by cooking method (stovetop, bake, grill, etc.)
  - Filter by allergens (dairy-free, soy-free, gluten-free, etc.)
  - View recipe collections separately

### Recent Updates

- Added recipe database with support for allergen tracking
- Implemented recipe import functionality
- Created filterable recipe list view with modern UI

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL 15+
- Redis 7.2+
- pip and npm package managers

### Environment Setup

1. **PostgreSQL Database**:

```bash
# Install PostgreSQL
brew install postgresql

# Start PostgreSQL service
brew services start postgresql

# Create database with default user
createdb recipe_db
```

2. **Redis Cache**:

```bash
# Install Redis
brew install redis

# Start Redis service
brew services start redis
```

3. **Environment Variables** (create `.env` in backend directory):

```env
# Database connection (default configuration)
DATABASE_URL="postgresql+asyncpg://postgres:password@localhost:5432/recipe_db"

# Redis connection (default configuration)
REDIS_URL="redis://localhost"

# API Keys for recipe services
EDAMAM_API_KEY="your_edamam_key"
EDAMAM_APP_ID="your_edamam_id"
SPOONACULAR_API_KEY="your_spoonacular_key"
```

### Installation

1. **Backend Setup** (from `/backend`):

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Start the backend server
uvicorn app.main:app --reload --port 5001
```

2. **Frontend Setup** (from `/frontend`):

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

The application will be available at:

- Frontend: http://localhost:3000
- Backend API: http://localhost:5001

## Application Startup

**Backend** (from `/backend`):

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Start the backend server
uvicorn app.main:app --reload --port 5001
```

**Frontend** (from `/frontend`):

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

## Development

### Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### Code Quality

Run the quality check script from the project root:

```bash
./scripts/check_code_quality.sh
```

This will run:

- Black (Python formatting)
- isort (Python import sorting)
- flake8 (Python linting)
- mypy (Python type checking)
- pylint (Python code analysis)
- Frontend linting and type checking

## Key Dependencies

- Python 3.10+
- Node.js 18+
- PostgreSQL 15+
- Redis 7.2+

## Project Structure

```
windsurf-project/
├── backend/           # FAST API
│   ├── app.py        # Application initialization
│   ├── models.py     # Database models
│   ├── config.py     # Configuration
│   └── database.py   # Database operations
└── frontend/         # Next.js Frontend
    ├── src/
    │   ├── app/      # Next.js pages
    │   ├── components/
    │   ├── lib/      # Utilities
    │   └── types/    # TypeScript types
    └── public/       # Static assets
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## Future Enhancements

- Recipe recommendations
- Meal planning
- Shopping lists
- Nutrition information

```

## .editorconfig
```
# EditorConfig is awesome: https://EditorConfig.org

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
end_of_line = lf
insert_final_newline = true
charset = utf-8
trim_trailing_whitespace = true

# Python files
[*.{py,pyi}]
indent_style = space
indent_size = 4
max_line_length = 120

# JavaScript/TypeScript files
[*.{js,jsx,ts,tsx}]
indent_style = space
indent_size = 2
max_line_length = 120

# JSON files
[*.json]
indent_style = space
indent_size = 2

# YAML files
[*.{yml,yaml}]
indent_style = space
indent_size = 2

# Markdown files
[*.md]
trim_trailing_whitespace = false
max_line_length = off

# HTML files
[*.{html,htm}]
indent_style = space
indent_size = 2

# CSS files
[*.{css,scss,sass}]
indent_style = space
indent_size = 2

```

## backend/setup.cfg
```
[flake8]
extend-ignore = E203, W503
max-complexity = 10
docstring-convention = google
import-order-style = google
application-import-names = app
exclude =
    .git,
    __pycache__,
    build,
    dist,
    *.pyc,
    *.egg-info,
    .eggs,
    venv,
    .next,
max-line-length = 120

[isort]
profile = black
multi_line_output = 3
include_trailing_comma = True
force_grid_wrap = 0
use_parentheses = True
ensure_newline_before_comments = True
known_first_party = app
sections = FUTURE,STDLIB,THIRDPARTY,FIRSTPARTY,LOCALFOLDER

[mypy]
python_version = 3.11
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_decorators = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_no_return = True
warn_unreachable = True
strict_optional = True
strict_equality = True
plugins = sqlalchemy.ext.mypy.plugin

[mypy.plugins.sqlalchemy.ext.mypy.plugin]
warn_relationship_base = True
warn_nullable = True

[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test
python_functions = test_*
addopts = --verbose --cov=app --cov-report=term-missing

[coverage:run]
source = app
omit = tests/*

[pylint]
disable = C0111,R0903,C0103
ignore = migrations
ignore-patterns = test_.*?py
good-names = i,j,k,ex,Run,_,id,db

```

## backend/app.py
```
"""Main application module."""

from __future__ import annotations

import os

from dotenv import load_dotenv

sentry_sdk.init(
    dsn="https://1b7918ad1ae2fa53f9e00a676e7ef195@o4508765460430848.ingest.us.sentry.io/4508765464625152",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)


# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    msg = "DATABASE_URL environment variable is not set"
    raise ValueError(msg)

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, class_=AsyncSession, expire_on_commit=False
).configure(bind=engine)

# Register routes
from backend.app.api.routes.protein_types import router as protein_types_router

app.include_router(protein_types_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

```

## backend/.python-version
```
3.11.0

```

## backend/README.md
```
# Recipe Database Backend

A FastAPI-based backend for managing and searching recipes.

## Development Setup

1. Install Poetry (package manager):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

4. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Project Structure

- `app/`: Main application package
  - `main.py`: FastAPI application entry point
  - `db/`: Database models and connection
  - `api/`: API routes and endpoints
  - `services/`: Business logic
  - `schemas/`: Pydantic models
  - `core/`: Core configuration

## Testing

Run tests with:
```bash
pytest
```

```

## backend/__init__.py
```
"""Backend package initialization.

This module initializes the backend package by:
1. Loading environment variables
2. Setting up logging
3. Initializing error tracking (if configured)
4. Setting up any other global services
"""

from __future__ import annotations

import logging
import os
from collections.abc import Sequence
from pathlib import Path
from typing import Final

# Initialize logging early
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger: Final[logging.Logger] = logging.getLogger(__name__)

# Import runtime dependencies
import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.base import Integration
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

# Initialize environment variables
env_path: Final[Path] = Path(__file__).parent / ".env"
env_development: Final[Path] = Path(__file__).parent / ".env.development"

# Load development env if it exists, otherwise try default .env
if os.getenv("ENVIRONMENT") != "production":
    if env_development.exists():
        logger.info("Loading development environment from .env.development")
        load_dotenv(str(env_development))
    elif env_path.exists():
        logger.info("Loading development environment from .env")
        load_dotenv(str(env_path))
elif env_path.exists():
    logger.info("Loading production environment from .env")
    load_dotenv(str(env_path))
else:
    logger.warning("No .env file found in production environment")

# Initialize Sentry if DSN is provided
sentry_dsn: str | None = os.getenv("SENTRY_DSN")
if sentry_dsn:
    try:
        integrations: Sequence[Integration] = [
            LoggingIntegration(level=logging.INFO, event_level=logging.ERROR),
            FastApiIntegration(),
            SqlalchemyIntegration(),
        ]

        sentry_sdk.init(
            dsn=sentry_dsn,
            send_default_pii=True,
            integrations=integrations,
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
            environment=os.getenv("ENVIRONMENT", "development"),
        )
        logger.info("Sentry initialized successfully")
    except ImportError as e:
        logger.warning(f"Sentry SDK not installed. Error tracking disabled: {e}")
    except Exception as e:
        logger.exception(f"Failed to initialize Sentry: {e}")

# Package version
__version__: Final[str] = "1.0.0"

```

## backend/pyproject.toml
```
[tool.poetry]
name = "backend"
version = "0.1.0"
description = "Recipe Database API"
readme = "README.md"
authors = ["Jessica Johnson <jessica.johnson@example.com>"]
packages = [{include = "app"}]

[tool.poetry.dependencies]
python = ">=3.11,<3.13"
fastapi = "^0.115.8"
sqlalchemy = {extras = ["ruff"], version = "^2.0.38"}
asyncpg = "^0.30.0"
alembic = "^1.14.1"
python-dotenv = "^1.0.1"
structlog = "^25.1.0"
tenacity = "^9.0.0"
cachetools = "^5.5.1"
fuzzywuzzy = "^0.18.0"
python-Levenshtein = "^0.23.0"
spoonacular = "^3.0"
redis = "^4.6.0"
uvicorn = "^0.27.1"
email-validator = "^2.1.0"
httpx = "^0.26.0"
python-multipart = "^0.0.6"
pyjwt = "^2.8.0"
psycopg2-binary = "^2.9.9"
aiohttp = "^3.9.1"
fastapi-cache2 = {extras = ["redis"], version = "^0.2.2"}
pydantic = {extras = ["email"], version = "^2.6.1"}
pydantic-settings = "^2.1.0"
python-jose = {extras = ["cryptography"], version = "^3.3.0"}
passlib = {extras = ["bcrypt"], version = "^1.7.4"}
cython = "^3.0.11"
databases = "^0.9.0"
werkzeug = "^3.0.1"
sentry-sdk = {version = "^2.20.0", extras = ["fastapi"]}
pydantic-extra-types = "^2.10.2"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.4"
pytest-asyncio = "^0.23.3"
pytest-cov = "^4.1.0"
coverage = {extras = ["toml"], version = "^7.4.1"}
ruff = "^0.3.3"
types-redis = "^4.6.0.20240106"
types-passlib = "^1.7.7.20240106"
types-python-jose = "^3.3.4.20240106"
types-aiofiles = "^23.2.0.20240106"
types-pytz = "^2024.1.0.20240203"
types-cachetools = "^5.5.0.20240820"
types-sqlalchemy = "^1.4.53.38"
types-setuptools = "^69.1.0.20240310"
# Documentation dependencies
sphinx = "^7.2.6"
sphinx-rtd-theme = "^2.0.0"  # ReadTheDocs theme
sphinx-autodoc-typehints = "^2.0.0"  # Type hints support
sphinx-copybutton = "^0.5.2"  # Copy button for code blocks
sphinx-design = "^0.5.0"  # UI components
sphinx-inline-tabs = "^2023.4.21"  # Tabbed content
sphinx-autoapi = "^3.0.0"  # API documentation
sphinxcontrib-mermaid = "^0.9.2"  # Mermaid diagrams
sphinxcontrib-httpdomain = "^1.8.1"  # HTTP API documentation
sphinxcontrib-openapi = "^0.8.3"  # OpenAPI/Swagger documentation
sphinx-autobuild = "^2024.2.4"  # Live reload server
sphinx-toolbox = "^3.8.1"  # Various utilities
sphinx-book-theme = "^1.1.3"  # Book theme
sphinx-material = "^0.0.36"  # Material theme
sphinx-gallery = "^0.18.0"  # Code examples gallery
sphinx-markdown-builder = "^0.6.8"  # Markdown output
sphinx-hoverxref = "^1.4.2"  # Tooltips on references
sphinx-multiversion = "^0.2.4"  # Multiple doc versions
semgrep = "^1.107.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.ruff]
line-length = 120
indent-width = 4
target-version = "py311"
src = ["app", "tests"]
extend-include = ["backend"]
extend-exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
    "migrations",
    "alembic",
    "tests",
    "test_*.py",
]
fix = true
unsafe-fixes = true
show-fixes = true
namespace-packages = ["types"]
typing-modules = []  # Remove type stubs since we're using inline types

[tool.ruff.lint]
select = [
    "ALL",        # All rules
    "TCH",        # Type checking
    "PYI",        # Type stubs
]
ignore = [
    "D211",       # No blank lines before class docstring
    "D213",       # Multi-line docstring summary should start at the second line
    "D100",       # Missing docstring in public module
    "ANN101",     # Missing type annotation for self in method
    "ANN102",     # Missing type annotation for cls in classmethod
    "PLR0913",    # Too many arguments to function call
    "B008",       # Do not perform function calls in argument defaults
    "COM812",     # Missing trailing comma
    "ISC001",     # Single line implicit string concatenation
    "TRY300",     # Consider moving try-except to context manager
    "TRY301",     # Abstract raise to error boundary
    "TCH001",     # Move application import into a type-checking block
    "TCH002",     # Move third-party import into a type-checking block
    "TCH003",     # Move standard library import into a type-checking block
    "UP007",      # Use X | Y for type annotations
    "TCH004",     # Move third-party import into a type-checking block (sentry-sdk)
    "PGH003",     # Use specific rule codes when ignoring
]

[tool.ruff.lint.isort]
combine-as-imports = true
force-single-line = false
known-first-party = ["app"]
known-third-party = [
    "dotenv",
    "sentry_sdk",
    "fastapi",
    "sqlalchemy",
    "pydantic",
]
extra-standard-library = ["types"]
required-imports = ["from __future__ import annotations"]
section-order = [
    "future",
    "standard-library",
    "third-party",
    "first-party",
    "local-folder",
]
split-on-trailing-comma = true
relative-imports-order = "closest-to-furthest"

[tool.ruff.lint.pydocstyle]
convention = "google"

[tool.ruff.lint.per-file-ignores]
"__init__.py" = [
    "D104",       # Missing docstring in public package
    "F401",       # Imported but unused
    "F403",       # Unable to detect undefined names
    "TCH",        # Type checking related rules
    "RUF100",     # Unused noqa directive
]
"migrations/*" = [
    "D",
    "E",
    "F",
    "I",
    "N",
    "ANN",
    "TCH",
]
"alembic/*" = [
    "D",
    "E",
    "F",
    "I",
    "N",
    "ANN",
    "TCH",
]
"app/api/routes/*" = ["B008"]
"app/models/*" = ["N805"]
"app/schemas/*" = ["N805"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = true
line-ending = "auto"

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
python_classes = ["Test*"]
addopts = "-v --cov=app --cov-report=term-missing --cov-report=html --cov-report=xml --cov-branch"

[tool.coverage.run]
branch = true
source = ["app"]
omit = [
    "*/migrations/*",
    "*/alembic/*",
    "*/tests/*",
    "*/__init__.py",
    "*/scripts/*",
    "*/types/*",
]
dynamic_context = "test_function"

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "pass",
    "raise ImportError",
    "@abstractmethod",
    "@abc.abstractmethod",
]
ignore_errors = true
fail_under = 80
precision = 2
show_missing = true

[tool.coverage.html]
directory = "coverage_html"
show_contexts = true
title = "RecipeDB Coverage Report"

[tool.coverage.xml]
output = "coverage.xml"

```

## backend/Dockerfile
```
# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

```

## backend/alembic.ini
```
# A generic, single database configuration.

[alembic]
# path to migration scripts
script_location = migrations

# template used to generate migration files
# file_template = %%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.
prepend_sys_path = .

# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the python-dateutil library that can be
# installed by adding `alembic[tz]` to the pip requirements
# timezone =

# max length of characters to apply to the
# "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to migrations/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "version_path_separator" below.
# version_locations = %(here)s/bar:%(here)s/bat:migrations/versions

# version path separator; As mentioned above, this is the character used to split
# version_locations. The default within new alembic.ini files is "os", which uses os.pathsep.
# If this key is omitted entirely, it falls back to the legacy behavior of splitting on spaces and/or colons.
# Valid values for version_path_separator are:
#
# version_path_separator = :
# version_path_separator = ;
# version_path_separator = space
version_path_separator = os  # Use os.pathsep. Default configuration used for new projects.

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

sqlalchemy.url = driver://user:pass@localhost/dbname


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the exec runner, execute a binary
# hooks = ruff
# ruff.type = exec
# ruff.executable = %(here)s/ruff
# ruff.options = --fix REVISION_SCRIPT_FILENAME

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S

```

## backend/_gemini_code_review/manifest.json
```
{
  "files": [
    {
      "file": "app.py.review.json"
    },
    {
      "file": "setup.py.review.json"
    }
  ]
}

```

## backend/_gemini_code_review/app.py.review.json
```
{
  "filename": "app.py",
  "category": "Bug Reports",
  "issues": [
    {
      "type": "Runtime Exception",
      "severity": "High",
      "description": "The code uses `render_template` which is not defined in FastAPI. FastAPI does not have built-in support for Jinja2 templating like Flask. This will raise a `NameError` when the `index` route is accessed."
    },
    {
      "type": "Incorrect Usage",
      "severity": "High",
      "description": "The code imports `Migrate` from `alembic` but initializes it incorrectly. The `Migrate` class is part of `flask-migrate`, not `alembic` directly. This might lead to issues with database migrations."
    },
    {
      "type": "Incorrect Usage",
      "severity": "High",
      "description": "The code imports `SQLAlchemy` from `fastapi-sqlalchemy` but initializes it incorrectly. `SQLAlchemy` from `fastapi-sqlalchemy` is a session manager, not a database engine. This will likely cause errors when trying to interact with the database."
    },
    {
      "type": "Incorrect Usage",
      "severity": "High",
      "description": "FastAPI uses `app = FastAPI(...)` to create an application instance, but it uses `app.config` which is a Flask feature. FastAPI does not have a `config` attribute. This will raise an `AttributeError`."
    },
    {
      "type": "Incorrect Usage",
      "severity": "High",
      "description": "FastAPI uses `app.include_router(recipes_bp)` to register a router, not `app.register_blueprint(recipes_bp)`. This will prevent the routes defined in `recipes_bp` from being registered."
    },
    {
      "type": "Incorrect Usage",
      "severity": "High",
      "description": "FastAPI uses `uvicorn.run(app, ...)` to run the application in production, not `app.run(debug=True)`. `app.run()` is typically used in Flask for development."
    },
    {
      "type": "Logical Error",
      "severity": "Medium",
      "description": "The code initializes `db` and `migrate` but doesn't use them anywhere in the provided code snippet. This suggests that database interactions and migrations are not implemented, which might be unintentional."
    },
    {
      "type": "Missing Dependency",
      "severity": "Medium",
      "description": "The code attempts to use Jinja2 templating (through `render_template`) but doesn't explicitly install the `jinja2` package. This will likely lead to a runtime error if the package is not installed."
    },
    {
      "type": "Missing Dependency",
      "severity": "Medium",
      "description": "The code uses `alembic` and `fastapi-sqlalchemy` but doesn't explicitly install these packages. This will likely lead to a runtime error if the packages are not installed."
    }
  ]
}

```

## backend/_gemini_code_review/setup.py.review.json
```
{
  "filename": "setup.py",
  "category": "Bug Reports",
  "issues": [
    {
      "type": "Redundant Dependency",
      "severity": "Low",
      "description": "The 'asyncio' package is a standard library in Python 3.11 and later. Specifying it as a dependency when the minimum Python version is set to 3.11 is redundant."
    },
    {
      "type": "Potential Version Conflict",
      "severity": "Medium",
      "description": "The 'aiohttp' library might have dependencies that conflict with the specified versions of other libraries. It's recommended to use a dependency resolver or a virtual environment to manage dependencies and avoid potential conflicts."
    },
    {
      "type": "Missing Development Dependencies",
      "severity": "Low",
      "description": "The setup.py file only lists runtime dependencies. It's good practice to also include development dependencies like testing frameworks (e.g., pytest), linters (e.g., flake8, pylint), and type checkers (e.g., mypy) in a separate section (e.g., 'extras_require')."
    },
    {
      "type": "Missing Package Metadata",
      "severity": "Low",
      "description": "The setup.py file is missing important metadata like 'author', 'author_email', 'description', 'url', 'license', etc. Including this information makes the package more discoverable and usable."
    }
  ]
}

```

## backend/config/default.yaml
```
# Default configuration for Recipe Database API
# This file serves as the base configuration and can be overridden by environment-specific files

# Database configuration
database:
  host: localhost
  port: 5432
  name: recipe_db
  user: postgres
  schema: public

# API configuration
api:
  title: Recipe Database API
  version: 0.1.0
  prefix: /api/v1
  cors_origins:
    - http://localhost:3000

# Allergen definitions
allergens:
  - name: dairy
    keywords:
      - milk
      - cream
      - cheese
      - butter
      - yogurt
      - whey
      - casein
      - lactose
      - ghee
      - curd
      - kefir
      - buttermilk
      - custard
      - pudding
      - ice cream
      - gelato

  - name: soy
    keywords:
      - soy
      - soya
      - tofu
      - tempeh
      - edamame
      - miso
      - natto
      - tamari
      - shoyu
      - lecithin
      - textured vegetable protein
      - tvp
      - soybean

  - name: egg
    keywords:
      - egg
      - eggs
      - albumin
      - meringue
      - mayonnaise
      - eggnog
      - lysozyme
      - globulin
      - ovomucin
      - ovalbumin
      - surimi

  - name: sunflower
    keywords:
      - sunflower
      - sunflower seeds
      - sunflower oil
      - sunflower lecithin
      - sunflower butter
      - sunflower protein

  - name: fig
    keywords:
      - fig
      - figs
      - fig jam
      - fig paste
      - fig extract

  - name: peanut
    keywords:
      - peanut
      - peanuts
      - groundnut
      - arachis
      - goober
      - monkey nut
      - peanut butter
      - peanut oil
      - beer nuts

  - name: tree_nuts
    keywords:
      - almond
      - cashew
      - walnut
      - pecan
      - brazil nut
      - macadamia
      - pistachio
      - hazelnut
      - pine nut
      - chestnut
      - nutmeg
      - marzipan

  - name: shellfish
    keywords:
      - shrimp
      - crab
      - lobster
      - crawfish
      - prawn
      - crayfish
      - langoustine
      - scampi
      - krill
      - shellfish

  - name: fish
    keywords:
      - fish
      - salmon
      - tuna
      - cod
      - halibut
      - tilapia
      - sardine
      - anchovy
      - mackerel
      - fish sauce
      - worcestershire
      - caesar
      - caviar
      - roe

  - name: gluten
    keywords:
      - wheat
      - rye
      - barley
      - oats
      - spelt
      - kamut
      - triticale
      - seitan
      - malt
      - brewer's yeast
      - bread
      - pasta
      - couscous
      - bulgur
      - semolina
      - durum

```

## backend/config/schemas/api.py
```
"""API configuration schemas.

This module defines Pydantic models for validating API configuration.
It preserves type safety while allowing configuration via YAML.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, HttpUrl

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import ConfigurationError


class APIEndpoint(BaseModel):
    """Configuration for an API endpoint.

    Attributes:
        name: Name of the API provider
        base_url: Base URL for the API
        timeout: Request timeout in seconds
        required_keys: Set of required API keys
        optional_keys: Set of optional API keys
        rate_limit: Maximum requests per minute
    """

    name: str
    base_url: HttpUrl
    timeout: int = Field(default=30, ge=1)
    required_keys: set[str]
    optional_keys: set[str] = Field(default_factory=set)
    rate_limit: int = Field(default=60, ge=1)

    def validate_keys(self, available_keys: dict[str, str | None]) -> None:
        """Validate that all required API keys are present.

        Args:
            available_keys: Dictionary of available API keys

        Raises:
            ConfigurationError: If any required keys are missing
        """
        missing = self.required_keys - set(available_keys.keys())
        if missing:
            raise ConfigurationError(
                message_template=ErrorMessages.CONFIG_MISSING_KEY,
                code=ErrorCode.CONFIGURATION_ERROR,
                details={"provider": self.name, "missing_keys": list(missing)},
            )


class APIConfig(BaseModel):
    """API configuration settings.

    Attributes:
        endpoints: Dictionary of API endpoint configurations
        cache_ttl: Cache time-to-live in seconds
        max_concurrent: Maximum concurrent API requests
        retry_attempts: Number of retry attempts for failed requests
        retry_delay: Delay between retries in seconds
    """

    endpoints: dict[str, APIEndpoint]
    cache_ttl: int = Field(default=3600, ge=1)
    max_concurrent: int = Field(default=5, ge=1)
    retry_attempts: int = Field(default=3, ge=0)
    retry_delay: float = Field(default=1.0, ge=0.1)

    def get_endpoint(self, name: str) -> APIEndpoint:
        """Get endpoint configuration by name.

        Args:
            name: Name of the API endpoint

        Returns:
            APIEndpoint configuration

        Raises:
            ConfigurationError: If endpoint doesn't exist
        """
        try:
            return self.endpoints[name]
        except KeyError:
            raise ConfigurationError(
                message_template=ErrorMessages.CONFIG_INVALID_VALUE,
                code=ErrorCode.CONFIGURATION_ERROR,
                details={"key": "api_endpoint", "value": name},
            )

```

## backend/config/development.yaml
```
# Development environment configuration
# Overrides default.yaml for development environment

database:
  host: localhost
  port: 5432
  name: recipe_db_dev

api:
  cors_origins:
    - http://localhost:3000
    - http://localhost:8000
    - http://127.0.0.1:3000
    - http://127.0.0.1:8000

```

## backend/config/production.yaml
```
# Production environment configuration
# Overrides default.yaml for production environment

database:
  host: db.production.example.com
  port: 5432
  name: recipe_db_prod

api:
  cors_origins:
    - https://recipe.example.com
    - https://api.recipe.example.com

```

## backend/pytest.ini
```
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --cov=. --cov-report=term-missing

```

## backend/app/main.py
```
"""Main FastAPI application."""

from __future__ import annotations

import json
from contextlib import asynccontextmanager
from pathlib import Path
from typing import TYPE_CHECKING

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import (
    allergens,
    cuisine_types,
    dietary_restrictions,
    ingredients,
    meal_types,
    recipe_search,
    recipes,
)
from app.core.config import settings
from app.core.error_handlers import setup_error_handlers
from app.core.error_messages import ErrorMessages

if TYPE_CHECKING:
    from collections.abc import AsyncIterator


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Handle application lifespan events.

    Args:
        app: The FastAPI application instance
    """
    # Startup
    yield
    # Shutdown
    if app.openapi():
        openapi_path = Path(__file__).parent.parent / "openapi.json"
        with openapi_path.open("w", encoding="utf-8") as f:
            json.dump(app.openapi(), f, indent=2)


def create_application() -> FastAPI:
    """Create FastAPI application."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        lifespan=lifespan,
    )

    # Set up CORS
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Set up error handling
    setup_error_handlers(app)

    # Set up translations
    ErrorMessages.setup_translations(settings.LOCALE_DIR)

    # Include routers
    app.include_router(recipe_search.router, prefix=settings.API_V1_STR)
    app.include_router(recipes.router, prefix=settings.API_V1_STR)
    app.include_router(allergens.router, prefix=settings.API_V1_STR)
    app.include_router(cuisine_types.router, prefix=settings.API_V1_STR)
    app.include_router(dietary_restrictions.router, prefix=settings.API_V1_STR)
    app.include_router(ingredients.router, prefix=settings.API_V1_STR)
    app.include_router(meal_types.router, prefix=settings.API_V1_STR)

    return app


app = create_application()

```

## backend/app/py.typed
```

```

## backend/app/routes/routes.py
```
from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix="/recipes", tags=["recipes"], responses={404: {"description": "Recipe not found"}})


@router.get("/")
async def get_recipes() -> dict[str, str]:
    """Get a list of recipes."""
    return {"message": "List of recipes will be here."}

```

## backend/app/api/routes/ingredients.py
```
"""Ingredients router.

This module provides endpoints for managing ingredients in the recipe database.
It supports CRUD operations for ingredients with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.ingredients import router as ingredients_router
        app.include_router(ingredients_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import Ingredient
from app.schemas.models import Ingredient as IngredientSchema, IngredientCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Ingredient not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "INGREDIENT_NOT_FOUND",
                        "message": "Ingredient not found",
                        "details": {"ingredient_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Ingredient already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "INGREDIENT_EXISTS",
                        "message": "Ingredient with this name already exists",
                        "details": {"name": "Salt"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=IngredientSchema, status_code=status.HTTP_201_CREATED)
async def create_ingredient(
    ingredient: IngredientCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> Ingredient:
    """Create a new ingredient.

    This endpoint creates a new ingredient in the database. It validates
    the input data and ensures uniqueness of the ingredient name.

    Args:
        ingredient (:class:`~app.schemas.models.IngredientCreate`):
            The ingredient data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.Ingredient`: The created ingredient.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If an ingredient with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            ingredient = await create_ingredient(
                IngredientCreate(name="Salt", description="Table salt"),
                db_session
            )
    """
    try:
        db_ingredient = Ingredient(**ingredient.model_dump())
        db.add(db_ingredient)
        await db.commit()
        await db.refresh(db_ingredient)
        return db_ingredient
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="Ingredient", identifier=ingredient.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_ingredient", details={"ingredient_data": ingredient.model_dump()}
        ) from err


@router.get("/", response_model=list[IngredientSchema])
async def get_ingredients(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[Ingredient]:
    """Retrieve a list of ingredients.

    This endpoint returns a paginated list of ingredients.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.Ingredient`]:
            List of ingredients.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            ingredients = await get_ingredients(skip=0, limit=10, db_session)
            for ingredient in ingredients:
                print(ingredient.name)
    """
    try:
        stmt: Select[tuple[Ingredient]] = select(Ingredient).offset(skip).limit(limit)
        result: Result[tuple[Ingredient]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_ingredients", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{ingredient_id}", response_model=IngredientSchema)
async def get_ingredient(
    ingredient_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> Ingredient:
    """Retrieve a specific ingredient by ID.

    This endpoint returns a single ingredient identified by its ID.

    Args:
        ingredient_id (int):
            The unique identifier of the ingredient.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.Ingredient`:
            The requested ingredient.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the ingredient is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            ingredient = await get_ingredient(1, db_session)
            print(f"Found ingredient: {ingredient.name}")
    """
    try:
        stmt: Select[tuple[Ingredient]] = select(Ingredient).filter(Ingredient.ingredient_id == ingredient_id)
        result: Result[tuple[Ingredient]] = await db.execute(stmt)
        db_ingredient = result.scalar_one_or_none()

        if db_ingredient is None:
            raise ResourceNotFoundError(resource_type="Ingredient", identifier=ingredient_id, lang=lang)

        return db_ingredient
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_ingredient", details={"ingredient_id": ingredient_id}
        ) from err


@router.put("/{ingredient_id}", response_model=IngredientSchema)
async def update_ingredient(
    ingredient_id: int,
    ingredient: IngredientCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> Ingredient:
    """Update a specific ingredient.

    This endpoint updates an existing ingredient with new data.
    It validates the input and ensures uniqueness of the ingredient name.

    Args:
        ingredient_id (int):
            The unique identifier of the ingredient to update.
        ingredient (:class:`~app.schemas.models.IngredientCreate`):
            The updated ingredient data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.Ingredient`:
            The updated ingredient.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the ingredient is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_ingredient(
                1,
                IngredientCreate(name="Sea Salt", description="Updated description"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = ingredient.model_dump(exclude_unset=True)
        stmt = (
            update(Ingredient)
            .where(Ingredient.ingredient_id == ingredient_id)
            .values(**update_data)
            .returning(Ingredient)
        )
        result = await db.execute(stmt)
        db_ingredient = result.scalar_one_or_none()

        if db_ingredient is None:
            raise ResourceNotFoundError(resource_type="Ingredient", identifier=ingredient_id, lang=lang)

        await db.commit()
        return db_ingredient

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="Ingredient", identifier=ingredient.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_ingredient",
            details={"ingredient_id": ingredient_id, "update_data": ingredient.model_dump()},
        ) from err


@router.delete("/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ingredient(
    ingredient_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific ingredient.

    This endpoint removes an ingredient from the database.
    It fails if the ingredient is referenced by any recipes.

    Args:
        ingredient_id (int):
            The unique identifier of the ingredient to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the ingredient is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the ingredient is referenced by recipes.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_ingredient(1, db_session)
            # The ingredient is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(Ingredient).where(Ingredient.ingredient_id == ingredient_id).returning(Ingredient.ingredient_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="Ingredient", identifier=ingredient_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="Ingredient", identifier=ingredient_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_ingredient", details={"ingredient_id": ingredient_id}
        ) from err

```

## backend/app/api/routes/dietary_restrictions.py
```
"""Dietary restrictions router.

This module provides endpoints for managing dietary restrictions in the recipe database.
It supports CRUD operations for dietary restrictions with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.dietary_restrictions import router as dietary_restrictions_router
        app.include_router(dietary_restrictions_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import DietaryRestriction
from app.schemas.models import DietaryRestriction as DietaryRestrictionSchema, DietaryRestrictionCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/dietary-restrictions",
    tags=["dietary-restrictions"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Dietary restriction not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "DIETARY_RESTRICTION_NOT_FOUND",
                        "message": "Dietary restriction not found",
                        "details": {"restriction_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Dietary restriction already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "DIETARY_RESTRICTION_EXISTS",
                        "message": "Dietary restriction with this name already exists",
                        "details": {"name": "Vegan"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=DietaryRestrictionSchema, status_code=status.HTTP_201_CREATED)
async def create_dietary_restriction(
    dietary_restriction: DietaryRestrictionCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> DietaryRestriction:
    """Create a new dietary restriction.

    This endpoint creates a new dietary restriction in the database. It validates
    the input data and ensures uniqueness of the restriction name.

    Args:
        dietary_restriction (:class:`~app.schemas.models.DietaryRestrictionCreate`):
            The dietary restriction data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.DietaryRestriction`: The created dietary restriction.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a dietary restriction with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            restriction = await create_dietary_restriction(
                DietaryRestrictionCreate(name="Vegan", description="No animal products"),
                db_session
            )
    """
    try:
        db_dietary_restriction = DietaryRestriction(**dietary_restriction.model_dump())
        db.add(db_dietary_restriction)
        await db.commit()
        await db.refresh(db_dietary_restriction)
        return db_dietary_restriction
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(
            resource_type="DietaryRestriction", identifier=dietary_restriction.name, lang=lang
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="create_dietary_restriction",
            details={"dietary_restriction_data": dietary_restriction.model_dump()},
        ) from err


@router.get("/", response_model=list[DietaryRestrictionSchema])
async def get_dietary_restrictions(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[DietaryRestriction]:
    """Retrieve a list of dietary restrictions.

    This endpoint returns a paginated list of dietary restrictions, ordered by ID.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.DietaryRestriction`]:
            List of dietary restrictions.

    Raises:
        ValueError: If skip or limit is negative.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            restrictions = await get_dietary_restrictions(skip=0, limit=10, db_session)
            for restriction in restrictions:
                print(restriction.name)
    """
    if skip < 0 or limit < 0:
        msg = "Skip and limit must be non-negative integers"
        raise ValueError(msg)
    try:
        stmt: Select[tuple[DietaryRestriction]] = (
            select(DietaryRestriction).order_by(DietaryRestriction.restriction_id).offset(skip).limit(limit)
        )
        result: Result[tuple[DietaryRestriction]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_dietary_restrictions", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{restriction_id}", response_model=DietaryRestrictionSchema)
async def get_dietary_restriction(
    restriction_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> DietaryRestriction:
    """Retrieve a specific dietary restriction by ID.

    This endpoint returns a single dietary restriction identified by its ID.

    Args:
        restriction_id (int):
            The unique identifier of the dietary restriction.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.DietaryRestriction`:
            The requested dietary restriction.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the dietary restriction is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            restriction = await get_dietary_restriction(1, db_session)
            print(f"Found restriction: {restriction.name}")
    """
    try:
        stmt: Select[tuple[DietaryRestriction]] = select(DietaryRestriction).filter(
            DietaryRestriction.restriction_id == restriction_id
        )
        result: Result[tuple[DietaryRestriction]] = await db.execute(stmt)
        db_dietary_restriction = result.scalar_one_or_none()

        if db_dietary_restriction is None:
            raise ResourceNotFoundError(resource_type="DietaryRestriction", identifier=restriction_id, lang=lang)

        return db_dietary_restriction
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_dietary_restriction", details={"restriction_id": restriction_id}
        ) from err


@router.put("/{restriction_id}", response_model=DietaryRestrictionSchema)
async def update_dietary_restriction(
    restriction_id: int,
    dietary_restriction: DietaryRestrictionCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> DietaryRestriction:
    """Update a specific dietary restriction.

    This endpoint updates an existing dietary restriction with new data.
    It validates the input and ensures uniqueness of the restriction name.

    Args:
        restriction_id (int):
            The unique identifier of the dietary restriction to update.
        dietary_restriction (:class:`~app.schemas.models.DietaryRestrictionCreate`):
            The updated dietary restriction data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.DietaryRestriction`:
            The updated dietary restriction.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the dietary restriction is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_dietary_restriction(
                1,
                DietaryRestrictionCreate(name="Strict Vegan", description="Updated description"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = dietary_restriction.model_dump(exclude_unset=True)
        stmt = (
            update(DietaryRestriction)
            .where(DietaryRestriction.restriction_id == restriction_id)
            .values(**update_data)
            .returning(DietaryRestriction)
        )
        result = await db.execute(stmt)
        db_dietary_restriction = result.scalar_one_or_none()

        if db_dietary_restriction is None:
            raise ResourceNotFoundError(resource_type="DietaryRestriction", identifier=restriction_id, lang=lang)

        await db.commit()
        return db_dietary_restriction

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(
            resource_type="DietaryRestriction", identifier=dietary_restriction.name, lang=lang
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_dietary_restriction",
            details={"restriction_id": restriction_id, "update_data": dietary_restriction.model_dump()},
        ) from err


@router.delete("/{restriction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dietary_restriction(
    restriction_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific dietary restriction.

    This endpoint removes a dietary restriction from the database.
    It fails if the restriction is referenced by any family members.

    Args:
        restriction_id (int):
            The unique identifier of the dietary restriction to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the dietary restriction is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the dietary restriction is referenced by family members.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_dietary_restriction(1, db_session)
            # The restriction is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = (
            delete(DietaryRestriction)
            .where(DietaryRestriction.restriction_id == restriction_id)
            .returning(DietaryRestriction.restriction_id)
        )
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="DietaryRestriction", identifier=restriction_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="DietaryRestriction", identifier=restriction_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_dietary_restriction", details={"restriction_id": restriction_id}
        ) from err

```

## backend/app/api/routes/allergens.py
```
"""Allergens router.

This module provides endpoints for managing allergen records in the database.
It supports CRUD operations with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import FastAPI
        from app.api.routes.allergens import router as allergens_router
        app.include_router(allergens_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages, Language
from app.core.exceptions import BusinessError, DatabaseError, ResourceNotFoundError
from app.models.models import Allergen
from app.schemas.models import Allergen as AllergenSchema

if TYPE_CHECKING:
    from app.api.deps import DatabaseSession
    from app.schemas.models import AllergenCreate

router = APIRouter(
    prefix="/allergens",
    tags=["allergens"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Allergen not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.RESOURCE_NOT_FOUND.get_message(
                            lang=Language.EN, details={"resource_type": "Allergen", "identifier": "123"}
                        )
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Allergen operation failed due to constraint violation",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.BUSINESS_RULE_VIOLATION.get_message(
                            lang=Language.EN, details={"error": "Allergen with this name already exists"}
                        )
                    }
                }
            },
        },
    },
)


@router.post(
    "/",
    response_model=AllergenSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Allergen created successfully"},
        status.HTTP_409_CONFLICT: {"description": "Allergen with this name already exists"},
    },
)
async def create_allergen(allergen: AllergenCreate, db: DatabaseSession) -> Allergen:
    """Create a new allergen.

    This endpoint creates a new allergen record in the database.
    It ensures that no duplicate allergens exist with the same name.

    Args:
        allergen: Allergen data including name and description
        db: Injected database session for the operation

    Returns:
        Allergen: The newly created allergen with all fields populated

    Raises:
        BusinessError: If an allergen with the same name already exists
        DatabaseError: If the database operation fails
    """
    try:
        db_allergen = Allergen(**allergen.model_dump())
        db.add(db_allergen)
        await db.commit()
        await db.refresh(db_allergen)
        return db_allergen
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.ALLERGEN_EXISTS,
            details={"error": "Allergen with this name already exists"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="create_allergen") from err


@router.get(
    "/",
    response_model=list[AllergenSchema],
    responses={
        status.HTTP_200_OK: {"description": "List of allergens retrieved successfully"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Database operation failed",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.DATABASE_ERROR.get_message(
                            lang=Language.EN, details={"operation": "list_allergens"}
                        )
                    }
                }
            },
        },
    },
)
async def get_allergens(db: DatabaseSession, skip: int = 0, limit: int = 100) -> list[Allergen]:
    """Get a list of allergens with pagination.

    This endpoint retrieves a paginated list of allergens from the database.

    Args:
        db: Injected database session for the operation
        skip: Number of allergens to skip (for pagination)
        limit: Maximum number of allergens to return

    Returns:
        list[Allergen]: List of allergens within the specified range

    Raises:
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Allergen).offset(skip).limit(limit))
        return list(result.scalars().all())
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="list_allergens") from err


@router.get(
    "/{allergen_id}",
    response_model=AllergenSchema,
    responses={
        status.HTTP_200_OK: {"description": "Allergen retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Allergen not found"},
    },
)
async def get_allergen(allergen_id: int, db: DatabaseSession) -> Allergen:
    """Get a specific allergen by ID.

    This endpoint retrieves detailed information about a specific allergen.

    Args:
        allergen_id: ID of the allergen to retrieve
        db: Injected database session for the operation

    Returns:
        Allergen: The requested allergen's details

    Raises:
        ResourceNotFoundError: If the allergen does not exist
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Allergen).where(Allergen.allergen_id == allergen_id))
        db_allergen = result.scalar_one_or_none()
        if db_allergen is None:
            raise ResourceNotFoundError(resource_type="Allergen", identifier=str(allergen_id))
        return db_allergen
    except ResourceNotFoundError:
        raise
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="get_allergen") from err


@router.put(
    "/{allergen_id}",
    response_model=AllergenSchema,
    responses={
        status.HTTP_200_OK: {"description": "Allergen updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Allergen not found"},
        status.HTTP_409_CONFLICT: {"description": "Update violates unique constraints"},
    },
)
async def update_allergen(allergen_id: int, allergen: AllergenCreate, db: DatabaseSession) -> Allergen:
    """Update a specific allergen.

    This endpoint updates an existing allergen with new data while maintaining
    data integrity constraints.

    Args:
        allergen_id: ID of the allergen to update
        allergen: Updated allergen data
        db: Injected database session for the operation

    Returns:
        Allergen: The updated allergen with all changes applied

    Raises:
        ResourceNotFoundError: If the allergen does not exist
        BusinessError: If the update violates unique constraints
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Allergen).where(Allergen.allergen_id == allergen_id))
        db_allergen = result.scalar_one_or_none()
        if db_allergen is None:
            raise ResourceNotFoundError(resource_type="Allergen", identifier=str(allergen_id))

        update_data = allergen.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_allergen, key, value)

        await db.commit()
        await db.refresh(db_allergen)
        return db_allergen
    except ResourceNotFoundError:
        raise
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.ALLERGEN_EXISTS,
            details={"error": "Allergen with this name already exists"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="update_allergen") from err


@router.delete(
    "/{allergen_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Allergen deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Allergen not found"},
        status.HTTP_409_CONFLICT: {"description": "Cannot delete allergen that is referenced by recipes"},
    },
)
async def delete_allergen(allergen_id: int, db: DatabaseSession) -> None:
    """Delete a specific allergen.

    This endpoint removes an allergen from the database if it is not referenced by any recipes.

    Args:
        allergen_id: ID of the allergen to delete
        db: Injected database session for the operation

    Raises:
        ResourceNotFoundError: If the allergen does not exist
        BusinessError: If the allergen is referenced by recipes
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Allergen).where(Allergen.allergen_id == allergen_id))
        db_allergen = result.scalar_one_or_none()
        if db_allergen is None:
            raise ResourceNotFoundError(resource_type="Allergen", identifier=str(allergen_id))

        await db.delete(db_allergen)
        await db.commit()
    except ResourceNotFoundError:
        raise
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.ALLERGEN_IN_USE,
            details={"error": "Cannot delete allergen that is referenced by recipes"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="delete_allergen") from err

```

## backend/app/api/routes/family_members.py
```
"""Family members router.

This module provides endpoints for managing family members in the recipe database.
It supports CRUD operations for family members with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.family_members import router as family_members_router
        app.include_router(family_members_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import FamilyMember
from app.schemas.models import FamilyMember as FamilyMemberSchema, FamilyMemberCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/family-members",
    tags=["family-members"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Family member not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "FAMILY_MEMBER_NOT_FOUND",
                        "message": "Family member not found",
                        "details": {"member_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Family member already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "FAMILY_MEMBER_EXISTS",
                        "message": "Family member with this name already exists",
                        "details": {"name": "John Doe"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=FamilyMemberSchema, status_code=status.HTTP_201_CREATED)
async def create_family_member(
    family_member: FamilyMemberCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> FamilyMember:
    """Create a new family member.

    This endpoint creates a new family member in the database. It validates
    the input data and ensures uniqueness of the member name.

    Args:
        family_member (:class:`~app.schemas.models.FamilyMemberCreate`):
            The family member data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.FamilyMember`: The created family member.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a family member with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            member = await create_family_member(
                FamilyMemberCreate(
                    name="John Doe",
                    birth_date="1990-01-01",
                    notes="Allergic to peanuts"
                ),
                db_session
            )
    """
    try:
        db_family_member = FamilyMember(**family_member.model_dump())
        db.add(db_family_member)
        await db.commit()
        await db.refresh(db_family_member)
        return db_family_member
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="FamilyMember", identifier=family_member.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_family_member", details={"family_member_data": family_member.model_dump()}
        ) from err


@router.get("/", response_model=list[FamilyMemberSchema])
async def get_family_members(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[FamilyMember]:
    """Retrieve a list of family members.

    This endpoint returns a paginated list of family members.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.FamilyMember`]:
            List of family members.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            members = await get_family_members(skip=0, limit=10, db_session)
            for member in members:
                print(member.name)
    """
    try:
        stmt: Select[tuple[FamilyMember]] = select(FamilyMember).offset(skip).limit(limit)
        result: Result[tuple[FamilyMember]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_family_members", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{member_id}", response_model=FamilyMemberSchema)
async def get_family_member(
    member_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> FamilyMember:
    """Retrieve a specific family member by ID.

    This endpoint returns a single family member identified by their ID.

    Args:
        member_id (int):
            The unique identifier of the family member.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.FamilyMember`:
            The requested family member.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the family member is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            member = await get_family_member(1, db_session)
            print(f"Found member: {member.name}")
    """
    try:
        stmt: Select[tuple[FamilyMember]] = select(FamilyMember).filter(FamilyMember.member_id == member_id)
        result: Result[tuple[FamilyMember]] = await db.execute(stmt)
        db_family_member = result.scalar_one_or_none()

        if db_family_member is None:
            raise ResourceNotFoundError(resource_type="FamilyMember", identifier=member_id, lang=lang)

        return db_family_member
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_family_member", details={"member_id": member_id}
        ) from err


@router.put("/{member_id}", response_model=FamilyMemberSchema)
async def update_family_member(
    member_id: int,
    family_member: FamilyMemberCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> FamilyMember:
    """Update a specific family member.

    This endpoint updates an existing family member with new data.
    It validates the input and ensures uniqueness of the member name.

    Args:
        member_id (int):
            The unique identifier of the family member to update.
        family_member (:class:`~app.schemas.models.FamilyMemberCreate`):
            The updated family member data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.FamilyMember`:
            The updated family member.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the family member is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_family_member(
                1,
                FamilyMemberCreate(
                    name="John Smith",
                    birth_date="1990-01-01",
                    notes="Updated notes"
                ),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = family_member.model_dump(exclude_unset=True)
        stmt = (
            update(FamilyMember)
            .where(FamilyMember.member_id == member_id)
            .values(**update_data)
            .returning(FamilyMember)
        )
        result = await db.execute(stmt)
        db_family_member = result.scalar_one_or_none()

        if db_family_member is None:
            raise ResourceNotFoundError(resource_type="FamilyMember", identifier=member_id, lang=lang)

        await db.commit()
        return db_family_member

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="FamilyMember", identifier=family_member.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_family_member",
            details={"member_id": member_id, "update_data": family_member.model_dump()},
        ) from err


@router.delete("/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_family_member(
    member_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific family member.

    This endpoint removes a family member from the database.
    It fails if the member has associated data (e.g., meal plans, preferences).

    Args:
        member_id (int):
            The unique identifier of the family member to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the family member is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the family member has associated data.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_family_member(1, db_session)
            # The family member is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(FamilyMember).where(FamilyMember.member_id == member_id).returning(FamilyMember.member_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="FamilyMember", identifier=member_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="FamilyMember", identifier=member_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_family_member", details={"member_id": member_id}
        ) from err

```

## backend/app/api/routes/recipes.py
```
"""Recipes router.

This module provides endpoints for managing recipes in the database, including CRUD operations
and relationship management.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.recipes import router as recipe_router
        app.include_router(recipe_router)

Note:
    All endpoints in this module require database access and handle common error cases
    such as duplicate recipes, constraint violations, and missing resources.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages, Language
from app.core.exceptions import BusinessError, DatabaseError, ResourceNotFoundError
from app.models.models import Recipe
from app.schemas.models import Recipe as RecipeSchema

if TYPE_CHECKING:
    from app.api.deps import DatabaseSession
    from app.schemas.models import RecipeCreate

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Recipe not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.RESOURCE_NOT_FOUND.get_message(
                            lang=Language.EN, details={"resource_type": "Recipe", "identifier": "123"}
                        )
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Recipe operation failed due to constraint violation",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.BUSINESS_RULE_VIOLATION.get_message(
                            lang=Language.EN, details={"error": "Recipe with this title already exists"}
                        )
                    }
                }
            },
        },
    },
)


@router.post(
    "/",
    response_model=RecipeSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Recipe created successfully"},
        status.HTTP_409_CONFLICT: {"description": "Recipe with this title already exists"},
    },
)
async def create_recipe(recipe: RecipeCreate, db: DatabaseSession) -> Recipe:
    """Create a new recipe.

    This endpoint creates a new recipe in the database with the provided details.
    It ensures that no duplicate recipes exist with the same title.

    Args:
        recipe: Recipe data including title, times, servings, etc.
        db: Injected database session for the operation

    Returns:
        Recipe: The newly created recipe with all fields populated

    Raises:
        BusinessError: If a recipe with the same title already exists
        DatabaseError: If the database operation fails
    """
    try:
        db_recipe = Recipe(**recipe.model_dump())
        db.add(db_recipe)
        await db.commit()
        await db.refresh(db_recipe)
        return db_recipe
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.RECIPE_EXISTS,
            details={"error": "Recipe with this title already exists"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="create_recipe") from err


@router.get(
    "/",
    response_model=list[RecipeSchema],
    responses={
        status.HTTP_200_OK: {"description": "List of recipes retrieved successfully"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Database operation failed",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.DATABASE_ERROR.get_message(
                            lang=Language.EN, details={"operation": "list_recipes"}
                        )
                    }
                }
            },
        },
    },
)
async def get_recipes(db: DatabaseSession, skip: int = 0, limit: int = 100) -> list[Recipe]:
    """Get a list of recipes with pagination.

    This endpoint retrieves a paginated list of recipes from the database.

    Args:
        db: Injected database session for the operation
        skip: Number of recipes to skip (for pagination)
        limit: Maximum number of recipes to return

    Returns:
        list[Recipe]: List of recipes within the specified range

    Raises:
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Recipe).offset(skip).limit(limit))
        return list(result.scalars().all())
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="list_recipes") from err


@router.get(
    "/{recipe_id}",
    response_model=RecipeSchema,
    responses={
        status.HTTP_200_OK: {"description": "Recipe retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Recipe not found"},
    },
)
async def get_recipe(recipe_id: int, db: DatabaseSession) -> Recipe:
    """Get a specific recipe by ID.

    This endpoint retrieves detailed information about a specific recipe.

    Args:
        recipe_id: ID of the recipe to retrieve
        db: Injected database session for the operation

    Returns:
        Recipe: The requested recipe's details

    Raises:
        ResourceNotFoundError: If the recipe does not exist
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Recipe).where(Recipe.recipe_id == recipe_id))
        db_recipe = result.scalar_one_or_none()
        if db_recipe is None:
            raise ResourceNotFoundError(resource_type="Recipe", identifier=str(recipe_id))
        return db_recipe
    except ResourceNotFoundError:
        raise
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="get_recipe") from err


@router.put(
    "/{recipe_id}",
    response_model=RecipeSchema,
    responses={
        status.HTTP_200_OK: {"description": "Recipe updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Recipe not found"},
        status.HTTP_409_CONFLICT: {"description": "Update violates unique constraints"},
    },
)
async def update_recipe(recipe_id: int, recipe: RecipeCreate, db: DatabaseSession) -> Recipe:
    """Update a specific recipe.

    This endpoint updates an existing recipe with new data while maintaining
    data integrity constraints.

    Args:
        recipe_id: ID of the recipe to update
        recipe: Updated recipe data
        db: Injected database session for the operation

    Returns:
        Recipe: The updated recipe with all changes applied

    Raises:
        ResourceNotFoundError: If the recipe does not exist
        BusinessError: If the update violates unique constraints
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Recipe).where(Recipe.recipe_id == recipe_id))
        db_recipe = result.scalar_one_or_none()
        if db_recipe is None:
            raise ResourceNotFoundError(resource_type="Recipe", identifier=str(recipe_id))

        update_data = recipe.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_recipe, key, value)

        await db.commit()
        await db.refresh(db_recipe)
        return db_recipe
    except ResourceNotFoundError:
        raise
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.RECIPE_EXISTS,
            details={"error": "Recipe with this title already exists"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="update_recipe") from err


@router.delete(
    "/{recipe_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Recipe deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Recipe not found"},
        status.HTTP_409_CONFLICT: {"description": "Cannot delete recipe that is referenced by meal plans"},
    },
)
async def delete_recipe(recipe_id: int, db: DatabaseSession) -> None:
    """Delete a specific recipe.

    This endpoint removes a recipe from the database if it is not referenced by any meal plans.

    Args:
        recipe_id: ID of the recipe to delete
        db: Injected database session for the operation

    Raises:
        ResourceNotFoundError: If the recipe does not exist
        BusinessError: If the recipe is referenced by meal plans
        DatabaseError: If the database operation fails
    """
    try:
        result = await db.execute(select(Recipe).where(Recipe.recipe_id == recipe_id))
        db_recipe = result.scalar_one_or_none()
        if db_recipe is None:
            raise ResourceNotFoundError(resource_type="Recipe", identifier=str(recipe_id))

        await db.delete(db_recipe)
        await db.commit()
    except ResourceNotFoundError:
        raise
    except IntegrityError as err:
        await db.rollback()
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            code=ErrorCode.RECIPE_IN_USE,
            details={"error": "Cannot delete recipe that is referenced by meal plans"},
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(error=err, operation="delete_recipe") from err

```

## backend/app/api/routes/protein_types.py
```
"""Protein types router.

This module provides endpoints for managing protein types in the recipe database.
It supports CRUD operations for protein types with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.protein_types import router as protein_types_router
        app.include_router(protein_types_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import ProteinType
from app.schemas.models import ProteinType as ProteinTypeSchema, ProteinTypeCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/protein-types",
    tags=["protein-types"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Protein type not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "PROTEIN_TYPE_NOT_FOUND",
                        "message": "Protein type not found",
                        "details": {"protein_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Protein type already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "PROTEIN_TYPE_EXISTS",
                        "message": "Protein type with this name already exists",
                        "details": {"name": "Chicken"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=ProteinTypeSchema, status_code=status.HTTP_201_CREATED)
async def create_protein_type(
    protein_type: ProteinTypeCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> ProteinType:
    """Create a new protein type.

    This endpoint creates a new protein type in the database. It validates
    the input data and ensures uniqueness of the protein type name.

    Args:
        protein_type (:class:`~app.schemas.models.ProteinTypeCreate`):
            The protein type data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.ProteinType`: The created protein type.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a protein type with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            protein = await create_protein_type(
                ProteinTypeCreate(name="Chicken", description="Poultry protein"),
                db_session
            )
    """
    try:
        db_protein_type = ProteinType(**protein_type.model_dump())
        db.add(db_protein_type)
        await db.commit()
        await db.refresh(db_protein_type)
        return db_protein_type
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="ProteinType", identifier=protein_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_protein_type", details={"protein_type_data": protein_type.model_dump()}
        ) from err


@router.get("/", response_model=list[ProteinTypeSchema])
async def get_protein_types(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[ProteinType]:
    """Retrieve a list of protein types.

    This endpoint returns a paginated list of protein types.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.ProteinType`]:
            List of protein types.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            proteins = await get_protein_types(skip=0, limit=10, db_session)
            for protein in proteins:
                print(protein.name)
    """
    try:
        stmt: Select[tuple[ProteinType]] = select(ProteinType).order_by(ProteinType.name).offset(skip).limit(limit)
        result: Result[tuple[ProteinType]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_protein_types", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{protein_id}", response_model=ProteinTypeSchema)
async def get_protein_type(
    protein_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> ProteinType:
    """Retrieve a specific protein type by ID.

    This endpoint returns a single protein type identified by its ID.

    Args:
        protein_id (int):
            The unique identifier of the protein type.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.ProteinType`:
            The requested protein type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the protein type is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            protein = await get_protein_type(1, db_session)
            print(f"Found protein: {protein.name}")
    """
    try:
        stmt: Select[tuple[ProteinType]] = select(ProteinType).filter(ProteinType.protein_id == protein_id)
        result: Result[tuple[ProteinType]] = await db.execute(stmt)
        db_protein_type = result.scalar_one_or_none()

        if db_protein_type is None:
            raise ResourceNotFoundError(resource_type="ProteinType", identifier=protein_id, lang=lang)

        return db_protein_type
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_protein_type", details={"protein_id": protein_id}
        ) from err


@router.put("/{protein_id}", response_model=ProteinTypeSchema)
async def update_protein_type(
    protein_id: int,
    protein_type: ProteinTypeCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> ProteinType:
    """Update a specific protein type.

    This endpoint updates an existing protein type with new data.
    It validates the input and ensures uniqueness of the protein type name.

    Args:
        protein_id (int):
            The unique identifier of the protein type to update.
        protein_type (:class:`~app.schemas.models.ProteinTypeCreate`):
            The updated protein type data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.ProteinType`:
            The updated protein type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the protein type is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_protein_type(
                1,
                ProteinTypeCreate(name="Free-range Chicken", description="Updated description"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = protein_type.model_dump(exclude_unset=True)
        stmt = (
            update(ProteinType).where(ProteinType.protein_id == protein_id).values(**update_data).returning(ProteinType)
        )
        result = await db.execute(stmt)
        db_protein_type = result.scalar_one_or_none()

        if db_protein_type is None:
            raise ResourceNotFoundError(resource_type="ProteinType", identifier=protein_id, lang=lang)

        await db.commit()
        return db_protein_type

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="ProteinType", identifier=protein_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_protein_type",
            details={"protein_id": protein_id, "update_data": protein_type.model_dump()},
        ) from err


@router.delete("/{protein_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_protein_type(
    protein_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific protein type.

    This endpoint removes a protein type from the database.
    It fails if the protein type is referenced by any recipes.

    Args:
        protein_id (int):
            The unique identifier of the protein type to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the protein type is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the protein type is referenced by recipes.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_protein_type(1, db_session)
            # The protein type is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(ProteinType).where(ProteinType.protein_id == protein_id).returning(ProteinType.protein_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="ProteinType", identifier=protein_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="ProteinType", identifier=protein_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_protein_type", details={"protein_id": protein_id}
        ) from err

```

## backend/app/api/routes/meal_types.py
```
"""Meal types router.

This module provides endpoints for managing meal types in the recipe database.
It supports CRUD operations for meal types (breakfast, lunch, dinner, etc.) with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.meal_types import router as meal_types_router
        app.include_router(meal_types_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import MealType
from app.schemas.models import MealType as MealTypeSchema, MealTypeCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/meal-types",
    tags=["meal-types"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Meal type not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "MEAL_TYPE_NOT_FOUND",
                        "message": "Meal type not found",
                        "details": {"type_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Meal type already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "MEAL_TYPE_EXISTS",
                        "message": "Meal type with this name already exists",
                        "details": {"name": "Breakfast"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=MealTypeSchema, status_code=status.HTTP_201_CREATED)
async def create_meal_type(
    meal_type: MealTypeCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealType:
    """Create a new meal type.

    This endpoint creates a new meal type in the database. It validates
    the input data and ensures uniqueness of the meal type name.

    Args:
        meal_type (:class:`~app.schemas.models.MealTypeCreate`):
            The meal type data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealType`: The created meal type.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a meal type with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            meal_type = await create_meal_type(
                MealTypeCreate(name="Breakfast"),
                db_session
            )
    """
    try:
        db_meal_type = MealType(**meal_type.model_dump())
        db.add(db_meal_type)
        await db.commit()
        await db.refresh(db_meal_type)
        return db_meal_type
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="MealType", identifier=meal_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_meal_type", details={"meal_type_data": meal_type.model_dump()}
        ) from err


@router.get("/", response_model=list[MealTypeSchema])
async def get_meal_types(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[MealType]:
    """Retrieve a list of meal types.

    This endpoint returns a paginated list of meal types.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.MealType`]:
            List of meal types.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            meal_types = await get_meal_types(skip=0, limit=10, db_session)
            for meal_type in meal_types:
                print(meal_type.name)
    """
    try:
        stmt: Select[tuple[MealType]] = select(MealType).order_by(MealType.name).offset(skip).limit(limit)
        result: Result[tuple[MealType]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_meal_types", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{type_id}", response_model=MealTypeSchema)
async def get_meal_type(
    type_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealType:
    """Retrieve a specific meal type by ID.

    This endpoint returns a single meal type identified by its ID.

    Args:
        type_id (int):
            The unique identifier of the meal type.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealType`:
            The requested meal type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal type is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            meal_type = await get_meal_type(1, db_session)
            print(f"Found meal type: {meal_type.name}")
    """
    try:
        stmt: Select[tuple[MealType]] = select(MealType).filter(MealType.meal_type_id == type_id)
        result: Result[tuple[MealType]] = await db.execute(stmt)
        db_meal_type = result.scalar_one_or_none()

        if db_meal_type is None:
            raise ResourceNotFoundError(resource_type="MealType", identifier=type_id, lang=lang)

        return db_meal_type
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="get_meal_type", details={"type_id": type_id}) from err


@router.put("/{type_id}", response_model=MealTypeSchema)
async def update_meal_type(
    type_id: int, meal_type: MealTypeCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealType:
    """Update a specific meal type.

    This endpoint updates an existing meal type with new data.
    It validates the input and ensures uniqueness of the meal type name.

    Args:
        type_id (int):
            The unique identifier of the meal type to update.
        meal_type (:class:`~app.schemas.models.MealTypeCreate`):
            The updated meal type data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealType`:
            The updated meal type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal type is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_meal_type(
                1,
                MealTypeCreate(name="Early Breakfast"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = meal_type.model_dump(exclude_unset=True)
        stmt = update(MealType).where(MealType.meal_type_id == type_id).values(**update_data).returning(MealType)
        result = await db.execute(stmt)
        db_meal_type = result.scalar_one_or_none()

        if db_meal_type is None:
            raise ResourceNotFoundError(resource_type="MealType", identifier=type_id, lang=lang)

        await db.commit()
        return db_meal_type

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="MealType", identifier=meal_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="update_meal_type", details={"type_id": type_id, "update_data": meal_type.model_dump()}
        ) from err


@router.delete("/{type_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_meal_type(
    type_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific meal type.

    This endpoint removes a meal type from the database.
    It fails if the meal type is referenced by any meal plans.

    Args:
        type_id (int):
            The unique identifier of the meal type to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal type is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the meal type is referenced by meal plans.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_meal_type(1, db_session)
            # The meal type is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(MealType).where(MealType.meal_type_id == type_id).returning(MealType.meal_type_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="MealType", identifier=type_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="MealType", identifier=type_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_meal_type", details={"type_id": type_id}
        ) from err

```

## backend/app/api/routes/search/__init__.py
```
"""Search routes package."""

```

## backend/app/api/routes/search/recipe_search.py
```
"""Recipe search router.

This module provides endpoints for searching and filtering recipes in the database.
It supports advanced search functionality with filters for cuisine, diet, ingredients,
cooking time, and more.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.search.recipe_search import router as recipe_search_router
        app.include_router(recipe_search_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.exc import SQLAlchemyError

from app.core.error_messages import ErrorMessages, Language
from app.core.exceptions import BusinessError, DatabaseError
from app.database.session import get_async_db
from app.schemas.recipe import RecipeList, RecipeSearchFilter
from app.services.recipe_search import RecipeSearchService

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/search",
    tags=["recipe-search"],
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid search parameters",
            "content": {
                "application/json": {
                    "example": {
                        "code": "VALIDATION_ERROR",
                        "message": "Invalid search parameters",
                        "details": {"query": "Search query must not be empty"},
                    }
                }
            },
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid filter parameters",
            "content": {
                "application/json": {
                    "example": {
                        "code": "VALIDATION_ERROR",
                        "message": "Invalid filter parameters",
                        "details": {"max_cooking_time": "Must be a positive integer"},
                    }
                }
            },
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Database error during search",
            "content": {
                "application/json": {
                    "example": {
                        "code": "DATABASE_ERROR",
                        "message": "Failed to execute recipe search",
                        "details": {"error": "Database connection error"},
                    }
                }
            },
        },
    },
)


@router.get("/", response_model=RecipeList)
async def search_recipes(
    query: str = Query(..., description="Search query string", min_length=1),
    filters: RecipeSearchFilter | None = None,
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> RecipeList:
    """Search for recipes with filters and pagination.

    This endpoint provides advanced recipe search functionality with support for
    filtering by cuisine, diet, ingredients, cooking time, and more. Results are
    paginated and ordered by relevance.

    Args:
        query (str):
            Search query string. Must not be empty.
        filters (:class:`~app.schemas.recipe.RecipeSearchFilter`, optional):
            Optional search filters for cuisine, diet, ingredients, etc.
        page (int, optional):
            Page number for pagination. Must be positive. Defaults to 1.
        page_size (int, optional):
            Number of items per page. Must be between 1 and 100. Defaults to 20.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.schemas.recipe.RecipeList`:
            List of matching recipes with total count and source information.

    Raises:
        :exc:`~app.core.exceptions.BusinessError`:
            If the search parameters are invalid.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            # Search for Italian vegetarian recipes
            result = await search_recipes(
                query="pasta",
                filters=RecipeSearchFilter(
                    cuisine="Italian",
                    diet="vegetarian",
                    max_cooking_time=30
                ),
                page=1,
                page_size=20,
                db_session
            )
            print(f"Found {result.total} recipes")
            for recipe in result.results:
                print(f"{recipe.title} - {recipe.cooking_time} minutes")
    """
    filter_dict: dict[str, Any] = {}
    try:
        if not query.strip():
            raise BusinessError(
                message_template=ErrorMessages.SEARCH_QUERY_EMPTY,
                details={"query": "A non-empty search query is required"},
                lang=lang,
            )

        search_service = RecipeSearchService(db)
        if filters:
            filter_dict = filters.model_dump()

        # Calculate offset from page and page_size
        offset = (page - 1) * page_size

        # Perform search with pagination
        return await search_service.search(query=query, filters=filter_dict, offset=offset, limit=page_size)

    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="search_recipes",
            details={"query": query, "filters": filter_dict, "pagination": {"page": page, "page_size": page_size}},
        ) from err
    except ValueError as err:
        raise BusinessError(
            message_template=ErrorMessages.INVALID_FILTER_PARAMS,
            details={"error": str(err), "filters": filter_dict},
            lang=lang,
        ) from err

```

## backend/app/api/routes/cook_methods.py
```
"""Cook methods router.

This module provides endpoints for managing cooking methods in the recipe database.
It supports CRUD operations for cooking methods with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.cook_methods import router as cook_methods_router
        app.include_router(cook_methods_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import CookMethod
from app.schemas.models import CookMethod as CookMethodSchema, CookMethodCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/cook-methods",
    tags=["cook-methods"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Cook method not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "COOK_METHOD_NOT_FOUND",
                        "message": "Cook method not found",
                        "details": {"method_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Cook method already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "COOK_METHOD_EXISTS",
                        "message": "Cook method with this name already exists",
                        "details": {"name": "Baking"},
                    }
                }
            },
        },
    },
)
# amazonq-ignore-next-line


@router.post("/", response_model=CookMethodSchema, status_code=status.HTTP_201_CREATED)
async def create_cook_method(
    cook_method: CookMethodCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> CookMethod:
    """Create a new cooking method.

    This endpoint creates a new cooking method in the database. It validates
    the input data and ensures uniqueness of the method name.

    Args:
        cook_method (:class:`~app.schemas.models.CookMethodCreate`):
            The cooking method data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CookMethod`: The created cooking method.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a cooking method with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            method = await create_cook_method(
                CookMethodCreate(name="Baking", description="Cooking in an oven"),
                db_session
            )
    """
    try:
        db_cook_method = CookMethod(**cook_method.model_dump())
        db.add(db_cook_method)
        await db.commit()
        await db.refresh(db_cook_method)
        return db_cook_method
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="CookMethod", identifier=cook_method.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_cook_method", details={"cook_method_data": cook_method.model_dump()}
        ) from err


@router.get("/", response_model=list[CookMethodSchema])
async def get_cook_methods(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[CookMethod]:
    """Retrieve a list of cooking methods.

    This endpoint returns a paginated list of cooking methods.
    It supports pagination through skip and limit parameters.
    # amazonq-ignore-next-line

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.CookMethod`]:
            List of cooking methods.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            # amazonq-ignore-next-line
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            methods = await get_cook_methods(skip=0, limit=10, db_session)
            for method in methods:
                print(method.name)
    """
    try:
        stmt: Select[tuple[CookMethod]] = select(CookMethod).offset(skip).limit(limit)
        result: Result[tuple[CookMethod]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_cook_methods", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{method_id}", response_model=CookMethodSchema)
async def get_cook_method(
    method_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> CookMethod:
    """Retrieve a specific cooking method by ID.

    This endpoint returns a single cooking method identified by its ID.

    Args:
        method_id (int):
            The unique identifier of the cooking method.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CookMethod`:
            The requested cooking method.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cooking method is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            method = await get_cook_method(1, db_session)
            print(f"Found method: {method.name}")
    """
    try:
        stmt: Select[tuple[CookMethod]] = select(CookMethod).filter(CookMethod.method_id == method_id)
        result: Result[tuple[CookMethod]] = await db.execute(stmt)
        db_cook_method = result.scalar_one_or_none()

        if db_cook_method is None:
            raise ResourceNotFoundError(resource_type="CookMethod", identifier=method_id, lang=lang)

        return db_cook_method
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_cook_method", details={"method_id": method_id}
        ) from err


@router.put("/{method_id}", response_model=CookMethodSchema)
async def update_cook_method(
    method_id: int,
    cook_method: CookMethodCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> CookMethod:
    """Update a specific cooking method.

    This endpoint updates an existing cooking method with new data.
    It validates the input and ensures uniqueness of the method name.

    Args:
        method_id (int):
            The unique identifier of the cooking method to update.
        cook_method (:class:`~app.schemas.models.CookMethodCreate`):
            The updated cooking method data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CookMethod`:
            The updated cooking method.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cooking method is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_cook_method(
                1,
                CookMethodCreate(name="Deep Frying", description="Updated description"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = cook_method.model_dump(exclude_unset=True)
        stmt = update(CookMethod).where(CookMethod.method_id == method_id).values(**update_data).returning(CookMethod)
        result = await db.execute(stmt)
        db_cook_method = result.scalar_one_or_none()

        if db_cook_method is None:
            raise ResourceNotFoundError(resource_type="CookMethod", identifier=method_id, lang=lang)

        await db.commit()
        return db_cook_method

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="CookMethod", identifier=cook_method.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_cook_method",
            details={"method_id": method_id, "update_data": cook_method.model_dump()},
        ) from err


@router.delete("/{method_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cook_method(
    method_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific cooking method.

    This endpoint removes a cooking method from the database.
    It fails if the method is referenced by any recipes.

    Args:
        method_id (int):
            The unique identifier of the cooking method to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cooking method is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the cooking method is referenced by recipes.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_cook_method(1, db_session)
            # The cooking method is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(CookMethod).where(CookMethod.method_id == method_id).returning(CookMethod.method_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="CookMethod", identifier=method_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="CookMethod", identifier=method_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_cook_method", details={"method_id": method_id}
        ) from err

```

## backend/app/api/routes/__init__.py
```
"""API route handlers package.

This package contains all the API route handlers for the application. Each module
provides a FastAPI router with endpoints for specific domain entities.

Available Routers:
    - allergens: Endpoints for managing allergen records
    - cook_methods: Endpoints for managing cooking methods
    - cuisine_types: Endpoints for managing cuisine types
    - dietary_restrictions: Endpoints for managing dietary restrictions
    - family_members: Endpoints for managing family members
    - ingredients: Endpoints for managing ingredients
    - meal_plans: Endpoints for managing meal plans
    - meal_types: Endpoints for managing meal types
    - protein_types: Endpoints for managing protein types
    - recipe_search: Endpoints for searching recipes
    - recipes: Endpoints for managing recipes

Example:
    .. code-block:: python

        from fastapi import FastAPI
        from app.api.routes import recipes

        app = FastAPI()
        app.include_router(recipes.router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.api.routes.allergens import router as allergens
from app.api.routes.cook_methods import router as cook_methods
from app.api.routes.cuisine_types import router as cuisine_types
from app.api.routes.dietary_restrictions import router as dietary_restrictions
from app.api.routes.family_members import router as family_members
from app.api.routes.ingredients import router as ingredients
from app.api.routes.meal_plans import router as meal_plans
from app.api.routes.meal_types import router as meal_types
from app.api.routes.protein_types import router as protein_types
from app.api.routes.recipe_search import router as recipe_search
from app.api.routes.recipes import router as recipes

if TYPE_CHECKING:
    from fastapi import APIRouter

    # Type hints for exported routers
    allergens: APIRouter
    cook_methods: APIRouter
    cuisine_types: APIRouter
    dietary_restrictions: APIRouter
    family_members: APIRouter
    ingredients: APIRouter
    meal_plans: APIRouter
    meal_types: APIRouter
    protein_types: APIRouter
    recipe_search: APIRouter
    recipes: APIRouter

__version__ = "1.0.0"

__all__ = [
    "allergens",
    "cook_methods",
    "cuisine_types",
    "dietary_restrictions",
    "family_members",
    "ingredients",
    "meal_plans",
    "meal_types",
    "protein_types",
    "recipe_search",
    "recipes",
]

```

## backend/app/api/routes/cuisine_types.py
```
"""Cuisine types router.

This module provides endpoints for managing cuisine types in the recipe database.
It supports CRUD operations for cuisine types with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.cuisine_types import router as cuisine_types_router
        app.include_router(cuisine_types_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceInUseError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import CuisineType
from app.schemas.models import CuisineType as CuisineTypeSchema, CuisineTypeCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/cuisine-types",
    tags=["cuisine-types"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Cuisine type not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "CUISINE_TYPE_NOT_FOUND",
                        "message": "Cuisine type not found",
                        "details": {"cuisine_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Cuisine type already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "CUISINE_TYPE_EXISTS",
                        "message": "Cuisine type with this name already exists",
                        "details": {"name": "Italian"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=CuisineTypeSchema, status_code=status.HTTP_201_CREATED)
async def create_cuisine_type(
    cuisine_type: CuisineTypeCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> CuisineType:
    """Create a new cuisine type.

    This endpoint creates a new cuisine type in the database. It validates
    the input data and ensures uniqueness of the cuisine type name.

    Args:
        cuisine_type (:class:`~app.schemas.models.CuisineTypeCreate`):
            The cuisine type data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CuisineType`: The created cuisine type.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a cuisine type with the same name already exists.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python
    # amazonq-ignore-next-line

            cuisine = await create_cuisine_type(
                CuisineTypeCreate(name="Italian", description="Italian cuisine"),
                db_session
            )
    """
    try:
        db_cuisine_type = CuisineType(**cuisine_type.model_dump())
        db.add(db_cuisine_type)
        await db.commit()
        await db.refresh(db_cuisine_type)
        return db_cuisine_type
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="CuisineType", identifier=cuisine_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_cuisine_type", details={"cuisine_type_data": cuisine_type.model_dump()}
        ) from err


@router.get("/", response_model=list[CuisineTypeSchema])
async def get_cuisine_types(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[CuisineType]:
    """Retrieve a list of cuisine types.

    This endpoint returns a paginated list of cuisine types.
    It supports pagination through skip and limit parameters.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.CuisineType`]:
            List of cuisine types.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            cuisines = await get_cuisine_types(skip=0, limit=10, db_session)
            for cuisine in cuisines:
                print(cuisine.name)
    """
    try:
        stmt: Select[tuple[CuisineType]] = select(CuisineType).offset(skip).limit(limit)
        result: Result[tuple[CuisineType]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_cuisine_types", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{cuisine_id}", response_model=CuisineTypeSchema)
async def get_cuisine_type(
    cuisine_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> CuisineType:
    """Retrieve a specific cuisine type by ID.

    This endpoint returns a single cuisine type identified by its ID.

    Args:
        cuisine_id (int):
            The unique identifier of the cuisine type.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CuisineType`:
            The requested cuisine type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cuisine type is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            cuisine = await get_cuisine_type(1, db_session)
            print(f"Found cuisine: {cuisine.name}")
    """
    try:
        stmt: Select[tuple[CuisineType]] = select(CuisineType).filter(CuisineType.cuisine_id == cuisine_id)
        result: Result[tuple[CuisineType]] = await db.execute(stmt)
        db_cuisine_type = result.scalar_one_or_none()

        if db_cuisine_type is None:
            raise ResourceNotFoundError(resource_type="CuisineType", identifier=cuisine_id, lang=lang)

        return db_cuisine_type
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_cuisine_type", details={"cuisine_id": cuisine_id}
        ) from err


@router.put("/{cuisine_id}", response_model=CuisineTypeSchema)
async def update_cuisine_type(
    cuisine_id: int,
    cuisine_type: CuisineTypeCreate,
    db: AsyncSession = Depends(get_async_db),
    lang: Language = Language.EN,
) -> CuisineType:
    """Update a specific cuisine type.

    This endpoint updates an existing cuisine type with new data.
    It validates the input and ensures uniqueness of the cuisine type name.

    Args:
        cuisine_id (int):
            The unique identifier of the cuisine type to update.
        cuisine_type (:class:`~app.schemas.models.CuisineTypeCreate`):
            The updated cuisine type data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.CuisineType`:
            The updated cuisine type.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cuisine type is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a duplicate name.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_cuisine_type(
                1,
                CuisineTypeCreate(name="Northern Italian", description="Updated description"),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = cuisine_type.model_dump(exclude_unset=True)
        stmt = (
            update(CuisineType).where(CuisineType.cuisine_id == cuisine_id).values(**update_data).returning(CuisineType)
        )
        result = await db.execute(stmt)
        db_cuisine_type = result.scalar_one_or_none()

        if db_cuisine_type is None:
            raise ResourceNotFoundError(resource_type="CuisineType", identifier=cuisine_id, lang=lang)

        await db.commit()
        return db_cuisine_type

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(resource_type="CuisineType", identifier=cuisine_type.name, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err,
            operation="update_cuisine_type",
            details={"cuisine_id": cuisine_id, "update_data": cuisine_type.model_dump()},
        ) from err


@router.delete("/{cuisine_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cuisine_type(
    cuisine_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific cuisine type.

    This endpoint removes a cuisine type from the database.
    It fails if the cuisine type is referenced by any recipes.

    Args:
        cuisine_id (int):
            The unique identifier of the cuisine type to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the cuisine type is not found.
        :exc:`~app.core.exceptions.ResourceInUseError`:
            If the cuisine type is referenced by recipes.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_cuisine_type(1, db_session)
            # The cuisine type is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(CuisineType).where(CuisineType.cuisine_id == cuisine_id).returning(CuisineType.cuisine_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="CuisineType", identifier=cuisine_id, lang=lang)

        await db.commit()

    except IntegrityError as err:
        await db.rollback()
        raise ResourceInUseError(resource_type="CuisineType", identifier=cuisine_id, lang=lang) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_cuisine_type", details={"cuisine_id": cuisine_id}
        ) from err

```

## backend/app/api/routes/meal_plans.py
```
"""Meal plans router.

This module provides endpoints for managing meal plans in the recipe database.
It supports CRUD operations for meal plans with proper validation and error handling.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.meal_plans import router as meal_plans_router
        app.include_router(meal_plans_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy import Select, delete, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.core.error_messages import Language
from app.core.exceptions import DatabaseError, ResourceExistsError, ResourceNotFoundError
from app.database.session import get_async_db
from app.models.models import MealPlan
from app.schemas.models import MealPlan as MealPlanSchema, MealPlanCreate

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine import Result
    from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/meal-plans",
    tags=["meal-plans"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Meal plan not found",
            "content": {
                "application/json": {
                    "example": {
                        "code": "MEAL_PLAN_NOT_FOUND",
                        "message": "Meal plan not found",
                        "details": {"plan_id": 123},
                    }
                }
            },
        },
        status.HTTP_409_CONFLICT: {
            "description": "Meal plan conflicts with existing plan",
            "content": {
                "application/json": {
                    "example": {
                        "code": "MEAL_PLAN_EXISTS",
                        "message": "A meal plan already exists for this date and meal type",
                        "details": {"date": "2024-03-20", "meal_type": "Dinner"},
                    }
                }
            },
        },
    },
)


@router.post("/", response_model=MealPlanSchema, status_code=status.HTTP_201_CREATED)
async def create_meal_plan(
    meal_plan: MealPlanCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealPlan:
    """Create a new meal plan.

    This endpoint creates a new meal plan in the database. It validates
    the input data and ensures no conflicts with existing plans.

    Args:
        meal_plan (:class:`~app.schemas.models.MealPlanCreate`):
            The meal plan data to create.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealPlan`: The created meal plan.

    Raises:
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If a meal plan already exists for the same date and meal type.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            plan = await create_meal_plan(
                MealPlanCreate(
                    recipe_id=1,
                    planned_date="2024-03-20",
                    meal_type_id=1,
                    member_id=1,
                    notes="Family dinner"
                ),
                db_session
            )
    """
    try:
        db_meal_plan = MealPlan(**meal_plan.model_dump())
        db.add(db_meal_plan)
        await db.commit()
        await db.refresh(db_meal_plan)
        return db_meal_plan
    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(
            resource_type="MealPlan", identifier=f"{meal_plan.planned_date}-{meal_plan.meal_type_id}", lang=lang
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="create_meal_plan", details={"meal_plan_data": meal_plan.model_dump()}
        ) from err


@router.get("/", response_model=list[MealPlanSchema])
async def get_meal_plans(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)
) -> Sequence[MealPlan]:
    """Get a list of meal plans with pagination.

    This endpoint returns a paginated list of meal plans, ordered by date.

    Args:
        skip (int, optional):
            Number of records to skip. Must be non-negative. Defaults to 0.
        limit (int, optional):
            Maximum number of records to return. Must be non-negative. Defaults to 100.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.

    Returns:
        Sequence[:class:`~app.models.models.MealPlan`]:
            List of meal plans.

    Raises:
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            plans = await get_meal_plans(skip=0, limit=10, db_session)
            for plan in plans:
                print(f"{plan.planned_date}: {plan.recipe_id}")
    """
    try:
        stmt: Select[tuple[MealPlan]] = (
            select(MealPlan).order_by(MealPlan.planned_date.desc()).offset(skip).limit(limit)
        )
        result: Result[tuple[MealPlan]] = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="get_meal_plans", details={"pagination": {"skip": skip, "limit": limit}}
        ) from err


@router.get("/{plan_id}", response_model=MealPlanSchema)
async def get_meal_plan(
    plan_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealPlan:
    """Get a specific meal plan by ID.

    This endpoint returns a single meal plan identified by its ID.

    Args:
        plan_id (int):
            The unique identifier of the meal plan.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealPlan`:
            The requested meal plan.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal plan is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            plan = await get_meal_plan(1, db_session)
            print(f"Found plan for {plan.planned_date}")
    """
    try:
        stmt: Select[tuple[MealPlan]] = select(MealPlan).filter(MealPlan.plan_id == plan_id)
        result: Result[tuple[MealPlan]] = await db.execute(stmt)
        db_meal_plan = result.scalar_one_or_none()

        if db_meal_plan is None:
            raise ResourceNotFoundError(resource_type="MealPlan", identifier=plan_id, lang=lang)

        return db_meal_plan
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="get_meal_plan", details={"plan_id": plan_id}) from err


@router.put("/{plan_id}", response_model=MealPlanSchema)
async def update_meal_plan(
    plan_id: int, meal_plan: MealPlanCreate, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> MealPlan:
    """Update a specific meal plan.

    This endpoint updates an existing meal plan with new data.
    It validates the input and ensures no conflicts with other plans.

    Args:
        plan_id (int):
            The unique identifier of the meal plan to update.
        meal_plan (:class:`~app.schemas.models.MealPlanCreate`):
            The updated meal plan data.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Returns:
        :class:`~app.models.models.MealPlan`:
            The updated meal plan.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal plan is not found.
        :exc:`~app.core.exceptions.ResourceExistsError`:
            If the update would create a conflict with another plan.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            updated = await update_meal_plan(
                1,
                MealPlanCreate(
                    recipe_id=2,
                    planned_date="2024-03-21",
                    meal_type_id=1,
                    member_id=1,
                    notes="Updated dinner plan"
                ),
                db_session
            )
    """
    try:
        # Perform update and return updated record in a single query
        update_data = meal_plan.model_dump(exclude_unset=True)
        stmt = update(MealPlan).where(MealPlan.plan_id == plan_id).values(**update_data).returning(MealPlan)
        result = await db.execute(stmt)
        db_meal_plan = result.scalar_one_or_none()

        if db_meal_plan is None:
            raise ResourceNotFoundError(resource_type="MealPlan", identifier=plan_id, lang=lang)

        await db.commit()
        return db_meal_plan

    except IntegrityError as err:
        await db.rollback()
        raise ResourceExistsError(
            resource_type="MealPlan", identifier=f"{meal_plan.planned_date}-{meal_plan.meal_type_id}", lang=lang
        ) from err
    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="update_meal_plan", details={"plan_id": plan_id, "update_data": meal_plan.model_dump()}
        ) from err


@router.delete("/{plan_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_meal_plan(
    plan_id: int, db: AsyncSession = Depends(get_async_db), lang: Language = Language.EN
) -> None:
    """Delete a specific meal plan.

    This endpoint removes a meal plan from the database.

    Args:
        plan_id (int):
            The unique identifier of the meal plan to delete.
        db (:class:`~sqlalchemy.ext.asyncio.AsyncSession`):
            The database session.
        lang (:class:`~app.core.error_messages.Language`, optional):
            The language for error messages. Defaults to English.

    Raises:
        :exc:`~app.core.exceptions.ResourceNotFoundError`:
            If the meal plan is not found.
        :exc:`~app.core.exceptions.DatabaseError`:
            If there's an error during the database operation.

    Example:
        .. code-block:: python

            await delete_meal_plan(1, db_session)
            # The meal plan is now deleted
    """
    try:
        # Delete and verify existence in a single query
        stmt = delete(MealPlan).where(MealPlan.plan_id == plan_id).returning(MealPlan.plan_id)
        result = await db.execute(stmt)

        if result.scalar_one_or_none() is None:
            raise ResourceNotFoundError(resource_type="MealPlan", identifier=plan_id, lang=lang)

        await db.commit()

    except SQLAlchemyError as err:
        await db.rollback()
        raise DatabaseError.from_sqlalchemy(
            error=err, operation="delete_meal_plan", details={"plan_id": plan_id}
        ) from err

```

## backend/app/api/routes/recipe_search.py
```
"""Recipe search router.

This module provides endpoints for searching recipes from various sources.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.routes.recipe_search import router as recipe_search_router
        app.include_router(recipe_search_router)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx
from fastapi import APIRouter, Query, status
from fastapi_cache.decorator import cache
from sqlalchemy.exc import SQLAlchemyError

from app.core.error_messages import ErrorMessages, Language
from app.core.exceptions import BusinessError, DatabaseError, DomainError, ResourceNotFoundError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_search import RecipeSearchService

if TYPE_CHECKING:
    from app.api.deps import DatabaseSession

router = APIRouter(
    prefix="/recipe-search",
    tags=["recipe-search"],
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid search parameters",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.INVALID_FILTER_PARAMS.get_message(
                            lang=Language.EN, details="Invalid search parameters"
                        )
                    }
                }
            },
        },
        status.HTTP_503_SERVICE_UNAVAILABLE: {
            "description": "External recipe service unavailable",
            "content": {
                "application/json": {
                    "example": {
                        "detail": ErrorMessages.BUSINESS_RULE_VIOLATION.get_message(
                            lang=Language.EN, details="Recipe service is currently unavailable"
                        )
                    }
                }
            },
        },
    },
)


@router.get(
    "/",
    response_model=RecipeList,
    responses={
        status.HTTP_200_OK: {"description": "Recipe search results retrieved successfully"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid search parameters"},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"description": "External recipe service unavailable"},
    },
)
async def search_recipes(
    db: DatabaseSession,
    query: str = Query(..., description="Search query string"),
    cuisine: str | None = Query(None, description="Cuisine type filter"),
    diet: str | None = Query(None, description="Dietary restriction filter"),
    exclude: list[str] | None = Query(None, description="Ingredients to exclude"),
    max_time: int | None = Query(None, description="Maximum total time in minutes"),
    service: str | None = Query(None, description="Specific recipe service to use"),
) -> RecipeList:
    """Search for recipes across multiple services.

    This endpoint searches for recipes using the specified criteria across multiple
    recipe services (Spoonacular, Edamam, etc.) and returns a unified list of results.

    Args:
        db: Injected database session for the operation
        query: Search query string
        cuisine: Filter by cuisine type
        diet: Filter by dietary restriction
        exclude: List of ingredients to exclude
        max_time: Maximum total cooking time in minutes
        service: Specific recipe service to use (optional)

    Returns:
        RecipeList: List of recipes matching the search criteria

    Raises:
        BusinessError: If search parameters are invalid
        BusinessError: If recipe service is unavailable
        DatabaseError: If database operation fails
    """
    try:
        search_service = RecipeSearchService(db)
        return await search_service.search(
            query=query, cuisine=cuisine, diet=diet, exclude=exclude, max_time=max_time, service=service
        )
    except BusinessError:
        # Re-raise business errors (validation, service unavailable) as is
        raise
    except DatabaseError as err:
        # Re-raise database errors with operation context preserved
        raise DatabaseError.from_sqlalchemy(
            error=err.context.original_error or err, operation="recipe_search", details=err.context.details
        ) from err
    except httpx.HTTPStatusError as err:
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            details={"error": f"External service error: {err.response.status_code} - {err!s}"},
        ) from err
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="recipe_search") from err
    except DomainError as err:
        raise BusinessError(message_template=ErrorMessages.INVALID_FILTER_PARAMS, details={"error": str(err)}) from err


@router.get(
    "/{recipe_id}",
    response_model=RecipeSearchResult,
    responses={
        status.HTTP_200_OK: {"description": "Recipe details retrieved successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Recipe not found"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid recipe ID format"},
    },
)
@cache(expire=3600)
async def get_recipe(recipe_id: str, db: DatabaseSession) -> RecipeSearchResult:
    """Get detailed information for a specific recipe.

    Args:
        recipe_id: ID of the recipe to retrieve
        db: Injected database session for the operation

    Returns:
        RecipeSearchResult: Detailed recipe information

    Raises:
        BusinessError: If recipe ID format is invalid
        BusinessError: If recipe service is unavailable
        DatabaseError: If database operation fails
        ResourceNotFoundError: If recipe is not found
    """
    try:
        search_service = RecipeSearchService(db)
        results = await search_service.search(query=f"id:{recipe_id}", limit=1)
        if not results.total:
            raise ResourceNotFoundError(resource_type="Recipe", identifier=recipe_id)
        return results.results[0]
    except BusinessError:
        # Re-raise business errors (validation, service unavailable) as is
        raise
    except DatabaseError as err:
        # Re-raise database errors with operation context preserved
        raise DatabaseError.from_sqlalchemy(
            error=err.context.original_error or err, operation="get_recipe", details=err.context.details
        ) from err
    except ResourceNotFoundError:
        # Re-raise not found errors as is
        raise
    except httpx.HTTPStatusError as err:
        raise BusinessError(
            message_template=ErrorMessages.BUSINESS_RULE_VIOLATION,
            details={"error": f"External service error: {err.response.status_code} - {err!s}"},
        ) from err
    except SQLAlchemyError as err:
        raise DatabaseError.from_sqlalchemy(error=err, operation="get_recipe") from err
    except ValueError as err:
        raise BusinessError(
            message_template=ErrorMessages.INVALID_FILTER_PARAMS, details={"error": "Invalid recipe ID format"}
        ) from err

```

## backend/app/routes/__init__.py
```

```

## backend/app/api/__init__.py
```
"""API router registration.

This module provides the main API router that combines all route modules
into a single FastAPI router. It handles the registration and organization
of all API endpoints.

Example:
    .. code-block:: python

        from fastapi import FastAPI
        from app.api import api_router

        app = FastAPI()
        app.include_router(api_router)
"""

from __future__ import annotations

from typing import Final

from fastapi import APIRouter

from app.api.routes.allergens import router as allergens_router
from app.api.routes.cook_methods import router as cook_methods_router
from app.api.routes.cuisine_types import router as cuisine_types_router
from app.api.routes.dietary_restrictions import router as dietary_restrictions_router
from app.api.routes.family_members import router as family_members_router
from app.api.routes.ingredients import router as ingredients_router
from app.api.routes.meal_plans import router as meal_plans_router
from app.api.routes.meal_types import router as meal_types_router
from app.api.routes.protein_types import router as protein_types_router
from app.api.routes.recipe_search import router as recipe_search_router
from app.api.routes.recipes import router as recipes_router

# Package version
__version__: Final[str] = "1.0.0"

# Create the main API router
api_router: Final[APIRouter] = APIRouter(prefix="/api")

# Include all route modules
api_router.include_router(allergens_router, prefix="/allergens", tags=["allergens"])
api_router.include_router(cook_methods_router, prefix="/cook-methods", tags=["cook-methods"])
api_router.include_router(cuisine_types_router, prefix="/cuisine-types", tags=["cuisine-types"])
api_router.include_router(dietary_restrictions_router, prefix="/dietary-restrictions", tags=["dietary-restrictions"])
api_router.include_router(family_members_router, prefix="/family-members", tags=["family-members"])
api_router.include_router(ingredients_router, prefix="/ingredients", tags=["ingredients"])
api_router.include_router(meal_plans_router, prefix="/meal-plans", tags=["meal-plans"])
api_router.include_router(meal_types_router, prefix="/meal-types", tags=["meal-types"])
api_router.include_router(protein_types_router, prefix="/protein-types", tags=["protein-types"])
api_router.include_router(recipe_search_router, prefix="/recipe-search", tags=["recipe-search"])
api_router.include_router(recipes_router, prefix="/recipes", tags=["recipes"])

# Public API
__all__: Final[list[str]] = ["api_router", "__version__"]

```

## backend/migrations/README
```
Generic single-database configuration.

```

## backend/app/services/recipe_service.py
```
"""Recipe service layer."""

from __future__ import annotations

from app.core.config import settings
from app.core.error_messages import RECIPE_FETCH_FAILED, RECIPE_SEARCH_FAILED
from app.core.exceptions import ExternalServiceError, NotFoundError, RecipeFilterError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.factory import RecipeProviderFactory


class RecipeService:
    """Service layer for recipe operations."""

    ENABLED_PROVIDERS = ["edamam", "spoonacular", "mealdb"]  # Default providers

    def __init__(self) -> None:
        """Initialize the recipe service."""
        self.provider_factory = RecipeProviderFactory()

    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
        provider: str | None = None,
    ) -> RecipeList:
        """Search for recipes across all providers or a specific provider."""
        try:
            recipe_provider = self.provider_factory.get_provider(provider) if provider else None
            if recipe_provider:
                return await recipe_provider.search_recipes(
                    query=query,
                    offset=offset,
                    limit=limit,
                    cuisine=cuisine,
                    diet=diet,
                    exclude=exclude,
                    max_time=max_time,
                )

            # If no specific provider, search across all providers
            results: list[RecipeSearchResult] = []
            total = 0
            enabled_providers = self.ENABLED_PROVIDERS if settings.ENABLE_EXTERNAL_PROVIDERS else ["local"]

            for provider_name in enabled_providers:
                try:
                    provider_instance = self.provider_factory.get_provider(provider_name)
                    provider_results = await provider_instance.search_recipes(
                        query=query,
                        offset=offset,
                        limit=limit,
                        cuisine=cuisine,
                        diet=diet,
                        exclude=exclude,
                        max_time=max_time,
                    )
                    results.extend(provider_results.results)
                    total += provider_results.total
                except Exception:
                    # Log error but continue with other providers
                    continue

            # Sort and paginate combined results
            start = offset
            end = offset + limit
            paginated_results = results[start:end]

            return RecipeList(total=total, results=paginated_results, source="all")

        except ExternalServiceError:
            raise
        except Exception as e:
            raise ExternalServiceError(message=RECIPE_SEARCH_FAILED.format(details=str(e)))

    async def get_recipe_by_id(self, recipe_id: str, provider: str) -> RecipeSearchResult:
        """Get a recipe by ID from a specific provider."""
        try:
            recipe_provider = self.provider_factory.get_provider(provider)
            return await recipe_provider.get_recipe_by_id(recipe_id)

        except (ExternalServiceError, NotFoundError, RecipeFilterError):
            raise
        except Exception as e:
            raise ExternalServiceError(message=RECIPE_FETCH_FAILED.format(details=str(e)))

```

## backend/app/db/base.py
```
"""Database session management."""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from app.core.config import settings

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession

if not settings.SQLALCHEMY_DATABASE_URI:
    msg = "Database URI is not configured"
    raise ValueError(msg)

# Create async engine with optimized settings
engine = create_async_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    pool_pre_ping=True,
    pool_size=20,  # Maximum number of connections in the pool
    max_overflow=10,  # Maximum number of connections that can be created beyond pool_size
    pool_timeout=30,  # Seconds to wait before giving up on getting a connection from the pool
    pool_recycle=1800,  # Recycle connections after 30 minutes
    echo=settings.LOG_LEVEL.upper() == "DEBUG",
    echo_pool=False,  # Don't log pool checkouts/checkins unless debugging
    future=True,  # Enable SQLAlchemy 2.0 behavior
    execution_options={
        "isolation_level": "REPEATABLE READ",  # Default isolation level
        "postgresql_readonly": False,  # Default to read-write transactions
        "postgresql_synchronous_commit": True,  # Ensure writes are durable
    },
)

# Create async session factory with explicit transaction control
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,  # Don't auto-flush for better control and performance
)


@asynccontextmanager
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Get database session with transaction management.

    This context manager ensures proper handling of transactions:
    - Automatically rolls back uncommitted changes on exceptions
    - Closes the session when done
    - Provides transaction isolation
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


@asynccontextmanager
async def get_db_readonly() -> AsyncGenerator[AsyncSession, None]:
    """Get read-only database session.

    This context manager is optimized for read-only operations:
    - Sets transaction isolation level to READ COMMITTED
    - Disables autoflush and expire_on_commit
    - Automatically rolls back at the end to release locks quickly
    """
    async with AsyncSessionLocal() as session:
        try:
            # Set read-only mode and optimized isolation level
            await session.connection(
                execution_options={"isolation_level": "READ COMMITTED", "postgresql_readonly": True}
            )
            yield session
            await session.rollback()  # Always rollback read-only transactions
        except Exception:
            await session.rollback()
            raise


async def dispose_engine() -> None:
    """Dispose of the engine and connection pool.

    Call this when shutting down the application to clean up resources.
    """
    if isinstance(engine, AsyncEngine):
        await engine.dispose()

```

## backend/app/api/endpoints/recipes.py
```
"""Recipe endpoints."""
"""what the fuck is this file? don't be creating shit int he wrong spot, we have routes/"""
from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, ValidationError
from app.models.models import Recipe, RecipeRating
from app.schemas.recipe import (
    RecipeCreate,
    RecipeList,
    RecipeRatingCreate,
    RecipeResponse,
    RecipeSearchResult,
)
from app.services.recipe_search import RecipeSearchService

router = APIRouter()


@router.get("/search", response_model=RecipeList)
async def search_recipes(
    query: Annotated[str, Query(description="Search query string")],
    offset: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    cuisine: Annotated[str | None, Query(description="Filter by cuisine type")] = None,
    diet: Annotated[str | None, Query(description="Filter by diet type")] = None,
    exclude: Annotated[list[str] | None, Query(description="Ingredients to exclude")] = None,
    max_time: Annotated[int | None, Query(ge=0, description="Maximum cooking time in minutes")] = None,
    service: Annotated[str | None, Query(description="Specific service to search")] = None,
    cooking_method: Annotated[str | None, Query(description="Filter by cooking method")] = None,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> RecipeList:
    """Search for recipes across all providers.

    Args:
        query: Search query string
        offset: Number of results to skip
        limit: Maximum number of results to return
        cuisine: Filter by cuisine type
        diet: Filter by diet type
        exclude: List of ingredients to exclude
        max_time: Maximum cooking time in minutes
        service: Specific service to search
        cooking_method: Filter by cooking method
        db: Database session

    Returns:
        RecipeList: List of recipes matching the search criteria

    Raises:
        BusinessError: If no recipes match the criteria
    """
    search_service = RecipeSearchService(db)
    return await search_service.search(
        query=query,
        offset=offset,
        limit=limit,
        cuisine=cuisine,
        diet=diet,
        exclude=exclude,
        max_time=max_time,
        service=service,
        cooking_method=cooking_method,
    )


@router.post("/save", response_model=RecipeResponse)
async def save_recipe(
    recipe: Annotated[RecipeSearchResult, "Recipe to save"],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> Recipe:
    """Save a recipe to the local database.

    This endpoint saves a recipe from an external provider to the local database
    for future reference. It performs allergen checks and normalizes the data
    before saving.

    Args:
        recipe: Recipe to save
        db: Database session

    Returns:
        Recipe: Saved recipe model

    Raises:
        BusinessError: If the recipe contains allergens
        ValidationError: If the recipe data is invalid
    """
    search_service = RecipeSearchService(db)
    return await search_service.save_recipe(recipe)


@router.post("/{recipe_id}/rate", response_model=RecipeRating)
async def rate_recipe(
    recipe_id: Annotated[int, Path(description="Recipe ID")],
    rating: Annotated[RecipeRatingCreate, "Rating details"],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> RecipeRating:
    """Rate a recipe and optionally add a review.

    Args:
        recipe_id: ID of the recipe to rate
        rating: Rating details
        db: Database session

    Returns:
        RecipeRating: Created rating

    Raises:
        ValidationError: If the recipe ID is invalid
        BusinessError: If the recipe is not found
    """
    # Verify recipe exists
    recipe = await db.get(Recipe, recipe_id)
    if not recipe:
        raise ValidationError(
            message_template=ErrorMessages.RECIPE_NOT_FOUND,
            code=ErrorCode.NOT_FOUND,
            details={"recipe_id": recipe_id},
        )

    # Create rating
    db_rating = RecipeRating(
        recipe_id=recipe_id,
        member_id=rating.member_id,
        rating=rating.rating,
        review=rating.review,
    )

    try:
        db.add(db_rating)
        await db.commit()
        await db.refresh(db_rating)
        return db_rating

    except Exception as e:
        raise BusinessError(
            message_template=ErrorMessages.RATING_FAILED,
            code=ErrorCode.DATABASE_ERROR,
            details={"recipe_id": recipe_id, "error": str(e)},
        )


@router.get("/{recipe_id}/ratings", response_model=list[RecipeRating])
async def get_recipe_ratings(
    recipe_id: Annotated[int, Path(description="Recipe ID")],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> list[RecipeRating]:
    """Get all ratings for a recipe.

    Args:
        recipe_id: ID of the recipe
        db: Database session

    Returns:
        list[RecipeRating]: List of ratings for the recipe

    Raises:
        ValidationError: If the recipe ID is invalid
        BusinessError: If the recipe is not found
    """
    # Verify recipe exists
    recipe = await db.get(Recipe, recipe_id)
    if not recipe:
        raise ValidationError(
            message_template=ErrorMessages.RECIPE_NOT_FOUND,
            code=ErrorCode.NOT_FOUND,
            details={"recipe_id": recipe_id},
        )

    # Get ratings
    from sqlalchemy import select

    stmt = select(RecipeRating).where(RecipeRating.recipe_id == recipe_id)
    result = await db.execute(stmt)
    return result.scalars().all()

```

## backend/app/db/__init__.py
```

```

## backend/app/db/session.py
```
"""Database session configuration.

This module provides database session factories and dependencies for both
synchronous and asynchronous database operations.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING

from sqlalchemy.engine import create_engine, make_url
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator, Generator

    from sqlalchemy.engine import Engine
    from sqlalchemy.ext.asyncio import AsyncEngine
    from sqlalchemy.orm import Session

# Create declarative base
Base = declarative_base()

# Create engines
if not settings.SQLALCHEMY_DATABASE_URI:
    msg = "Database URI is not configured"
    raise ValueError(msg)

db_url = make_url(settings.SQLALCHEMY_DATABASE_URI)
engine: Engine = create_engine(
    db_url,
    pool_pre_ping=True,  # Enable connection health checks
    pool_recycle=3600,  # Recycle connections after 1 hour
)

# Create async engine with asyncpg driver
async_db_url = db_url.set(drivername="postgresql+asyncpg")
async_engine: AsyncEngine = create_async_engine(
    async_db_url,
    echo=settings.LOG_LEVEL == "DEBUG",  # Enable SQL debugging based on log level
    pool_pre_ping=True,
    pool_recycle=3600,
)

# Create session factories
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, class_=AsyncSession, expire_on_commit=False)

# Bind the async session after creation
AsyncSessionLocal.configure(bind=async_engine)


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Get a database session for synchronous operations.

    Yields:
        Session: SQLAlchemy database session

    Raises:
        Exception: Any database-related exception that occurs during the session
    """
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """Get a database session for asynchronous operations.

    Yields:
        AsyncSession: SQLAlchemy async database session

    Raises:
        Exception: Any database-related exception that occurs during the session
    """
    async with AsyncSessionLocal() as db:
        try:
            yield db
        except Exception:
            await db.rollback()
            raise


async def init_async_db() -> None:
    """Initialize the database asynchronously.

    This function should be called during application startup
    for asynchronous database initialization.
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_async_db() -> None:
    """Close the async database connection pool.

    This function should be called during application shutdown
    to properly close all database connections.
    """
    await async_engine.dispose()

```

## backend/app/db/base_class.py
```
"""SQLAlchemy declarative base and metadata."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

from sqlalchemy import DateTime, Integer, MetaData, func
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, registry

if TYPE_CHECKING:
    import builtins
    from datetime import datetime

    from sqlalchemy.orm import Mapped

# Naming convention for constraints and indices
# This ensures consistent naming across migrations
convention = {
    "ix": "ix_%(column_0_label)s",  # Index
    "uq": "uq_%(table_name)s_%(column_0_name)s",  # Unique constraint
    "ck": "ck_%(table_name)s_%(constraint_name)s",  # Check constraint
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",  # Foreign key
    "pk": "pk_%(table_name)s",  # Primary key
}

# Create metadata with naming convention
metadata = MetaData(naming_convention=convention)

# Create registry with our metadata
mapper_registry = registry(metadata=metadata)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy declarative models."""

    metadata = metadata


# Type variable for model references
ModelType = TypeVar("ModelType", bound="Base")


class BaseModel(Base):
    """Base class for all database models.

    This class provides:
    - Automatic table naming
    - Common columns (id, created_at, updated_at)
    - Dictionary conversion
    - Relationship helpers
    """

    __abstract__ = True

    # Automatic table name generation
    @declared_attr.directive
    def __tablename__(self) -> str:
        """Generate table name automatically.

        By default, uses the lowercase version of the class name.
        """
        return self.__name__.lower()

    # Common columns that all models should have
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    def to_dict(
        self,
        exclude: set[str] | None = None,
        include: set[str] | None = None,
    ) -> dict[str, Any]:
        """Convert model instance to dictionary.

        Args:
            exclude: Set of field names to exclude from the dictionary
            include: Set of field names to include in the dictionary (if None, includes all)

        Returns:
            Dictionary representation of the model
        """
        if exclude is None:
            exclude = set()

        result: dict[str, Any] = {}
        for key in self.__mapper__.attrs:
            if key.key not in exclude:
                result[key.key] = getattr(self, key.key)
        return result

    @classmethod
    def from_dict(cls: type[ModelType], data: builtins.dict[str, Any]) -> ModelType:
        """Create model instance from dictionary.

        Args:
            data: Dictionary containing model data

        Returns:
            Model instance
        """
        return cls(**data)

```

## backend/app/db/database.py
```
"""Database configuration."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if TYPE_CHECKING:
    from collections.abc import Generator

    from sqlalchemy.orm import Session

load_dotenv()  # Load environment variables from .env file

# Get database URL from environment variable with a default for development
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/recipe_db")

# Create database engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Enable connection pool "pre-ping" feature
    echo=os.getenv("SQL_ECHO", "false").lower() == "true",  # Enable SQL logging based on env var
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for declarative models
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Get database session.

    Yields:
        SQLAlchemy Session: Database session that is automatically closed after use.

    This function is designed to be used as a dependency in FastAPI endpoints.
    FastAPI's dependency injection system will automatically call this function
    for each request that needs a database session, ensuring proper session
    creation and closure.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

## backend/app/services/__init__.py
```
"""Services package.

This package contains service layer modules for business logic. Services handle
complex operations, database interactions, and external API calls while maintaining
separation of concerns.

Example:
    .. code-block:: python

        from app.services import RecipeSearchService

        # Search for recipes
        service = RecipeSearchService(db_session)
        results = await service.search(query="pasta", cuisine="italian")
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.services.recipe_search import RecipeSearchService
from app.services.recipe_service import RecipeService

if TYPE_CHECKING:
    from app.services.recipe_search import RecipeSearchService as RecipeSearchServiceType
    from app.services.recipe_service import RecipeService as RecipeServiceType

    # Type hints for exported services
    RecipeSearchService: type[RecipeSearchServiceType]
    RecipeService: type[RecipeServiceType]

__version__ = "1.0.0"

__all__ = ["RecipeSearchService", "RecipeService"]

```

## backend/app/services/recipe_search.py
```
"""Recipe search service.

This module provides functionality for searching recipes across multiple external services
and storing safe recipes locally.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sqlalchemy import and_, func, or_, select

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, DatabaseError
from app.models.models import CookMethod, Recipe
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.factory import RecipeProviderFactory

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class RecipeSearchService:
    """Service for searching recipes across multiple sources."""

    def __init__(self, db: AsyncSession) -> None:
        """Initialize the recipe search service.

        Args:
            db: Database session
        """
        self.db = db
        self.provider_factory = RecipeProviderFactory()

    async def search(
        self,
        query: str,
        filters: dict[str, Any] | None = None,
        offset: int | None = None,
        limit: int | None = 100,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
        service: str | None = None,
        cooking_method: str | None = None,
    ) -> RecipeList:
        """Search for recipes across multiple services.

        Args:
            query: Search query string
            filters: Additional filters to apply
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude: List of ingredients to exclude
            max_time: Maximum cooking time in minutes
            service: Specific service to search (e.g., 'spoonacular', 'edamam')
            cooking_method: Filter by cooking method (e.g., 'instant_pot', 'slow_cooker')

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            DatabaseError: If the database operation fails
            BusinessError: If no recipes match the criteria
        """
        try:
            # Extract cooking method from query if not explicitly provided
            if not cooking_method:
                # Create a temporary provider to use its method detection
                temp_provider = self.provider_factory.get_provider("spoonacular")
                cooking_method = temp_provider._detect_cooking_method(query)

            # If a specific service is requested, use only that provider
            if service:
                provider = self.provider_factory.get_provider(service)
                results = await provider.search_recipes(
                    query=query,
                    offset=offset or 0,
                    limit=limit or 100,
                    cuisine=cuisine,
                    diet=diet,
                    exclude=exclude,
                    max_time=max_time,
                )

                # Apply cooking method filter if specified
                if cooking_method:
                    filtered_results = []
                    for recipe in results.results:
                        recipe_text = " ".join(
                            [recipe.title, recipe.description or "", " ".join(recipe.instructions or [])]
                        )
                        if provider._detect_cooking_method(recipe_text) == cooking_method:
                            filtered_results.append(recipe)
                    results.results = filtered_results
                    results.total = len(filtered_results)

                return results

            # Search local database first
            local_results = await self._search_local(
                query=query, filters=filters, offset=offset, limit=limit, cooking_method=cooking_method
            )

            # If we have enough local results or external providers are disabled,
            # return local results only
            if local_results.total >= (limit or 100):
                return local_results

            # Search external providers
            try:
                providers = self.provider_factory.get_all_providers()
                all_results: list[RecipeSearchResult] = []

                # Add local results first
                all_results.extend(local_results.results)

                # Search each provider
                remaining_limit = (limit or 100) - len(all_results)
                if remaining_limit > 0:
                    for provider in providers:
                        try:
                            provider_results = await provider.search_recipes(
                                query=query,
                                offset=0,  # Start from beginning for each provider
                                limit=remaining_limit,
                                cuisine=cuisine,
                                diet=diet,
                                exclude=exclude,
                                max_time=max_time,
                            )

                            # Apply cooking method filter if specified
                            if cooking_method:
                                filtered_results = []
                                for recipe in provider_results.results:
                                    recipe_text = " ".join(
                                        [recipe.title, recipe.description or "", " ".join(recipe.instructions or [])]
                                    )
                                    if provider._detect_cooking_method(recipe_text) == cooking_method:
                                        filtered_results.append(recipe)
                                provider_results.results = filtered_results
                                provider_results.total = len(filtered_results)

                            all_results.extend(provider_results.results)
                            remaining_limit -= len(provider_results.results)
                            if remaining_limit <= 0:
                                break
                        except Exception:
                            # Log error but continue with other providers
                            continue

                if not all_results:
                    raise BusinessError(
                        message_template=ErrorMessages.NO_RECIPES_FOUND,
                        code=ErrorCode.NOT_FOUND,
                        details={"query": query, "cooking_method": cooking_method, "filters": filters},
                    )

                return RecipeList(
                    total=len(all_results), results=all_results[:limit] if limit else all_results, source="all"
                )

            except BusinessError:
                raise
            except Exception:
                # If external search fails, return local results
                return local_results

        except BusinessError:
            raise
        except Exception as e:
            raise DatabaseError.from_sqlalchemy(
                error=e,
                operation="search_recipes",
                details={"query": query, "filters": filters, "service": service, "cooking_method": cooking_method},
            ) from e

    async def _search_local(
        self,
        query: str,
        filters: dict[str, Any] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        cooking_method: str | None = None,
    ) -> RecipeList:
        """Search local database for recipes.

        Args:
            query: Search query string
            filters: Additional filters to apply
            offset: Number of results to skip
            limit: Maximum number of results to return
            cooking_method: Filter by cooking method

        Returns:
            RecipeList: List of recipes matching the search criteria
        """
        # Build the base query
        stmt = select(Recipe).where(or_(Recipe.title.ilike(f"%{query}%"), Recipe.variations.ilike(f"%{query}%")))

        # Apply filters
        if filters:
            if cuisine_type := filters.get("cuisine_type"):
                stmt = stmt.join(Recipe.cuisine_types).filter(Recipe.cuisine_types.any(name=cuisine_type))

            if max_cooking_time := filters.get("max_cooking_time"):
                stmt = stmt.filter(Recipe.cook_time_minutes <= max_cooking_time)

            if allergens_exclude := filters.get("allergens_exclude"):
                # Create a list of conditions for each allergen to exclude
                allergen_conditions = [~Recipe.allergens.any(name=allergen) for allergen in allergens_exclude]
                # Combine conditions with AND
                if allergen_conditions:
                    stmt = stmt.filter(and_(*allergen_conditions))

        # Apply cooking method filter
        if cooking_method:
            stmt = stmt.join(Recipe.cook_methods).filter(CookMethod.name == cooking_method)

        # Apply pagination
        if offset:
            stmt = stmt.offset(offset)
        if limit:
            stmt = stmt.limit(limit)

        # Execute query
        result = await self.db.execute(stmt)
        recipes = result.scalars().all()

        # Convert to search results
        results = [
            RecipeSearchResult(
                id=str(recipe.recipe_id),
                title=recipe.title,
                description=recipe.variations,
                image_url=recipe.image_url,
                source_url=recipe.source_url,
                prep_time=recipe.prep_time_minutes,
                cook_time=recipe.cook_time_minutes,
                total_time=(recipe.prep_time_minutes or 0) + (recipe.cook_time_minutes or 0),
                servings=recipe.servings,
                cuisine=recipe.cuisine_types[0].name if recipe.cuisine_types else None,
                diet=[],  # TODO: Implement diet types
                ingredients=[i.name for i in recipe.ingredients],
                instructions=[i.instruction for i in recipe.instructions],
                source="local",
            )
            for recipe in recipes
        ]

        return RecipeList(total=len(results), results=results, source="local")

    async def save_recipe(self, recipe: RecipeSearchResult) -> Recipe:
        """Save a recipe to the local database.

        Args:
            recipe: Recipe to save

        Returns:
            Recipe: Saved recipe model

        Raises:
            DatabaseError: If the database operation fails
            BusinessError: If the recipe contains allergens
        """
        try:
            # Create a temporary provider to check allergens
            temp_provider = self.provider_factory.get_provider("spoonacular")
            if not temp_provider._filter_allergens(recipe):
                raise BusinessError(
                    message_template=ErrorMessages.RECIPE_CONTAINS_ALLERGENS,
                    code=ErrorCode.ALLERGEN_CONFLICT,
                    details={"recipe_id": recipe.id, "title": recipe.title},
                )

            # Create new recipe
            db_recipe = Recipe(
                title=recipe.title,
                variations=recipe.description,
                image_url=recipe.image_url,
                source_url=recipe.source_url,
                prep_time_minutes=recipe.prep_time,
                cook_time_minutes=recipe.cook_time,
                servings=recipe.servings,
            )

            # Add ingredients
            if recipe.ingredients:
                for ing_name in recipe.ingredients:
                    ingredient = await self._get_or_create_ingredient(ing_name)
                    db_recipe.ingredients.append(ingredient)

            # Add instructions
            if recipe.instructions:
                from app.models import RecipeInstruction

                for i, instruction in enumerate(recipe.instructions, 1):
                    db_recipe.instructions.append(RecipeInstruction(step_number=i, instruction=instruction))

            # Add cuisine type if present
            if recipe.cuisine:
                cuisine = await self._get_or_create_cuisine(recipe.cuisine)
                db_recipe.cuisine_types.append(cuisine)

            # Detect and add cooking method
            recipe_text = " ".join([recipe.title, recipe.description or "", " ".join(recipe.instructions or [])])
            if method := temp_provider._detect_cooking_method(recipe_text):
                cook_method = await self._get_or_create_cook_method(method)
                db_recipe.cook_methods.append(cook_method)

            self.db.add(db_recipe)
            await self.db.commit()
            await self.db.refresh(db_recipe)

            return db_recipe

        except BusinessError:
            raise
        except Exception as e:
            raise DatabaseError.from_sqlalchemy(
                error=e, operation="save_recipe", details={"recipe_id": recipe.id, "title": recipe.title}
            ) from e

    async def _get_or_create_ingredient(self, name: str) -> Any:
        """Get or create an ingredient by name."""
        from app.models import Ingredient

        stmt = select(Ingredient).where(Ingredient.name == name)
        result = await self.db.execute(stmt)
        ingredient = result.scalar_one_or_none()
        if not ingredient:
            ingredient = Ingredient(name=name)
            self.db.add(ingredient)
        return ingredient

    async def _get_or_create_cuisine(self, name: str) -> Any:
        """Get or create a cuisine type by name."""
        from app.models import CuisineType

        stmt = select(CuisineType).where(CuisineType.name == name)
        result = await self.db.execute(stmt)
        cuisine = result.scalar_one_or_none()
        if not cuisine:
            cuisine = CuisineType(name=name)
            self.db.add(cuisine)
        return cuisine

    async def _get_or_create_cook_method(self, name: str) -> Any:
        """Get or create a cooking method by name."""
        from app.models import CookMethod

        stmt = select(CookMethod).where(CookMethod.name == name)
        result = await self.db.execute(stmt)
        method = result.scalar_one_or_none()
        if not method:
            method = CookMethod(name=name)
            self.db.add(method)
        return method

    async def count_search_results(self, query: str, filters: dict[str, Any] | None = None) -> int:
        """Count total number of recipes matching the search criteria.

        Args:
            query: Search query string
            filters: Additional filters to apply

        Returns:
            Total number of matching recipes
        """
        # Build the base query
        stmt = (
            select(func.count())
            .select_from(Recipe)
            .where(or_(Recipe.title.ilike(f"%{query}%"), Recipe.variations.ilike(f"%{query}%")))
        )

        # Apply filters
        if filters:
            if cuisine_type := filters.get("cuisine_type"):
                stmt = stmt.join(Recipe.cuisine_types).filter(Recipe.cuisine_types.any(name=cuisine_type))

            if max_cooking_time := filters.get("max_cooking_time"):
                stmt = stmt.filter(Recipe.cook_time_minutes <= max_cooking_time)

            if allergens_exclude := filters.get("allergens_exclude"):
                # Create a list of conditions for each allergen to exclude
                allergen_conditions = [~Recipe.allergens.any(name=allergen) for allergen in allergens_exclude]
                # Combine conditions with AND
                if allergen_conditions:
                    stmt = stmt.filter(and_(*allergen_conditions))

        # Execute query
        result = await self.db.execute(stmt)
        return result.scalar_one()

```

## backend/migrations/env.py
```
"""Alembic environment configuration."""

import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from app.core.config import settings
from app.db.base import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = settings.SQLALCHEMY_DATABASE_URI
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Run actual migrations."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Run migrations in 'online' mode."""
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = settings.SQLALCHEMY_DATABASE_URI
    connectable = async_engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```

## backend/migrations/script.py.mako
```
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    ${downgrades if downgrades else "pass"}

```

## backend/app/api/deps.py
```
"""API dependencies.

This module provides reusable FastAPI dependencies for route handlers.
Dependencies handle common concerns like database sessions, authentication,
and request validation.

Example:
    .. code-block:: python

        from fastapi import Depends
        from app.api.deps import get_db

        @router.get("/items")
        async def get_items(db: AsyncSession = Depends(get_db)):
            # Use db session here
            pass
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_async_db

# Type-annotated dependencies for better IDE support
DatabaseSession = Annotated[AsyncSession, Depends(get_async_db)]

__version__ = "1.0.0"

__all__ = ["DatabaseSession", "get_async_db"]

```

## backend/app/services/recipe_providers/mock.py
```
"""Mock recipe provider for testing."""

from __future__ import annotations

import random

from app.schemas.recipe import RecipeList, RecipeSearchResult

from .base import RecipeProvider


class MockRecipeProvider(RecipeProvider):
    """Mock recipe provider that returns generated data."""

    def __init__(self) -> None:
        """Initialize the mock provider."""
        super().__init__()
        self._mock_recipes = self._generate_mock_recipes()

    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search mock recipes."""
        # Filter recipes based on query
        results = [
            recipe
            for recipe in self._mock_recipes
            if query.lower() in recipe.title.lower()
            or (recipe.description and query.lower() in recipe.description.lower())
        ]

        # Apply filters
        if cuisine:
            results = [r for r in results if r.cuisine == cuisine]
        if diet:
            results = [r for r in results if diet in (r.diet or [])]
        if exclude:
            results = [r for r in results if not any(ing in " ".join(r.ingredients or []).lower() for ing in exclude)]
        if max_time:
            results = [r for r in results if r.total_time and r.total_time <= max_time]

        # Apply pagination
        paginated_results = results[offset : offset + limit] if limit else results[offset:]

        return RecipeList(total=len(results), results=paginated_results, source=self.source_name)

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get mock recipe by ID."""
        for recipe in self._mock_recipes:
            if recipe.id == recipe_id:
                return recipe
        msg = f"Recipe not found: {recipe_id}"
        raise ValueError(msg)

    def _generate_mock_recipes(self) -> list[RecipeSearchResult]:
        """Generate a list of mock recipes."""
        cuisines = ["Italian", "Mexican", "Chinese", "Indian", "American"]
        diets = ["Vegetarian", "Vegan", "Gluten-Free", "Keto", "Paleo"]

        recipes = []
        for i in range(100):  # Generate 100 mock recipes
            cuisine = random.choice(cuisines)
            recipe_diets = random.sample(diets, random.randint(0, 2))

            recipe = RecipeSearchResult(
                id=f"mock_{i}",
                title=f"Mock {cuisine} Recipe {i}",
                description=f"A delicious {cuisine} recipe with mock ingredients",
                image_url=f"https://example.com/images/recipe_{i}.jpg",
                source_url=f"https://example.com/recipes/{i}",
                prep_time=random.randint(5, 30),
                cook_time=random.randint(10, 60),
                total_time=random.randint(15, 90),
                servings=random.randint(2, 6),
                cuisine=cuisine,
                diet=recipe_diets,
                ingredients=[f"Mock Ingredient {j}" for j in range(random.randint(3, 8))],
                instructions=[f"Mock Step {j}" for j in range(random.randint(3, 6))],
                source=self.source_name,
            )
            recipes.append(recipe)

        return recipes

```

## backend/app/services/recipe_providers/base.py
```
"""Base recipe provider class.

This module provides the base class for all recipe providers, implementing
common functionality like allergen filtering and error handling.

Example:
    .. code-block:: python

        class SpoonacularProvider(RecipeProvider):
            async def search_recipes(self, query: str, **kwargs) -> RecipeList:
                # Provider-specific implementation
                results = await self._search_api(query, **kwargs)
                return self._apply_allergen_filtering(results)

Note:
    All recipe providers must implement the abstract methods and should use
    the provided allergen filtering utilities for consistency.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, ClassVar, Final

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, ValidationError

if TYPE_CHECKING:
    from app.schemas.recipe import RecipeList, RecipeSearchResult


# Type alias for provider-specific recipe data
ProviderRecipeData = dict[str, Any]


class RecipeProvider(ABC):
    """Base class for recipe providers.

    This class provides common functionality for recipe providers including:
    - Allergen filtering (dairy, soy, egg by default)
    - Error handling
    - Data normalization

    Attributes:
        DEFAULT_ALLERGENS: List of allergens to exclude by default
        ALLERGEN_KEYWORDS: Dictionary mapping allergens to their indicator keywords
        ALLERGEN_FILTERING_REQUIRED: Whether allergen filtering can be disabled
    """

    # Default allergens that must be excluded
    DEFAULT_ALLERGENS: ClassVar[list[str]] = ["dairy", "soy", "egg"]

    # Whether allergen filtering can be disabled
    ALLERGEN_FILTERING_REQUIRED: ClassVar[bool] = True

    # Common allergen keywords to check
    ALLERGEN_KEYWORDS: Final[dict[str, list[str]]] = {
        "dairy": [
            "milk",
            "cheese",
            "cream",
            "butter",
            "yogurt",
            "whey",
            "casein",
            "lactose",
            "dairy",
            "ghee",
            "buttermilk",
            "cottage cheese",
            "sour cream",
            "half and half",
            "creamy",
            "milky",
            "parmesan",
            "mozzarella",
            "ricotta",
            "cheddar",
        ],
        "soy": [
            "soy",
            "soya",
            "edamame",
            "tofu",
            "tempeh",
            "miso",
            "natto",
            "tamari",
            "shoyu",
            "soy sauce",
            "soy lecithin",
            "soybean",
            "textured vegetable protein",
            "tvp",
            "soy protein",
        ],
        "egg": [
            "egg",
            "eggs",
            "mayonnaise",
            "mayo",
            "meringue",
            "albumen",
            "albumin",
            "lysozyme",
            "ovalbumin",
            "surimi",
            "lecithin",
            "eggnog",
            "custard",
            "hollandaise",
            "aioli",
        ],
    }

    # Cooking method keywords
    COOKING_METHOD_KEYWORDS: Final[dict[str, list[str]]] = {
        "instant_pot": ["instant pot", "pressure cook", "pressure cooker", "instant-pot", "instantpot"],
        "slow_cooker": ["slow cook", "slow cooker", "crockpot", "crock pot", "crock-pot", "slow-cooker"],
        "air_fryer": ["air fry", "air fryer", "air-fry", "air-fryer"],
        "grill": ["grill", "grilled", "grilling", "barbecue", "bbq", "charcoal", "broil"],
        "bake": ["bake", "baked", "baking", "roast", "roasted", "roasting", "oven"],
        "stovetop": ["stovetop", "stove top", "stove-top", "pan fry", "sauté", "saute", "simmer", "boil"],
    }

    def __init__(self, api_key: str | None = None, disable_allergen_filter: bool = False) -> None:
        """Initialize the recipe provider.

        Args:
            api_key: Optional API key for authentication
            disable_allergen_filter: Whether to disable allergen filtering
                (only if ALLERGEN_FILTERING_REQUIRED is False)

        Raises:
            ValidationError: If trying to disable required allergen filtering
        """
        self.api_key = api_key
        self.source_name = self.__class__.__name__.replace("Provider", "").lower()

        if disable_allergen_filter and self.ALLERGEN_FILTERING_REQUIRED:
            raise ValidationError(
                message_template=ErrorMessages.INVALID_OPERATION,
                code=ErrorCode.INVALID_OPERATION,
                details={
                    "error": "Allergen filtering cannot be disabled for this provider",
                    "provider": self.source_name,
                },
            )
        self.allergen_filter_enabled = not disable_allergen_filter

    @abstractmethod
    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search for recipes using the provider's API.

        Args:
            query: Search query string
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude: List of ingredients to exclude
            max_time: Maximum cooking time in minutes

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            DomainError: If the API request fails
            ValidationError: If the search parameters are invalid
            BusinessError: If no recipes match the filters
        """

    @abstractmethod
    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Args:
            recipe_id: Recipe ID from the provider

        Returns:
            RecipeSearchResult: Detailed recipe information

        Raises:
            DomainError: If the API request fails
            ValidationError: If the recipe ID is invalid
            BusinessError: If the recipe contains allergens
        """

    def _normalize_recipe(self, raw_recipe: ProviderRecipeData) -> RecipeSearchResult:
        """Convert provider-specific recipe data to standard format.

        This method should be overridden by each provider to handle their specific data format.

        Args:
            raw_recipe: Raw recipe data from the provider

        Returns:
            RecipeSearchResult: Normalized recipe data

        Raises:
            NotImplementedError: If the provider hasn't implemented normalization
        """
        msg = f"Provider {self.source_name} must implement recipe normalization"
        raise NotImplementedError(msg)

    def _contains_allergen(self, text: str, allergen: str) -> bool:
        """Check if text contains any keywords for a specific allergen.

        Args:
            text: Text to check (ingredient list, title, etc.)
            allergen: Allergen type to check for

        Returns:
            bool: True if allergen keywords are found

        Raises:
            ValidationError: If checking an unknown allergen type
        """
        if allergen not in self.ALLERGEN_KEYWORDS:
            raise ValidationError(
                message_template=ErrorMessages.INVALID_FILTER_PARAMS,
                code=ErrorCode.VALIDATION_ERROR,
                details={
                    "error": "Unknown allergen type",
                    "allergen": allergen,
                    "valid_allergens": list(self.ALLERGEN_KEYWORDS.keys()),
                },
            )

        text = text.lower()
        return any(keyword in text for keyword in self.ALLERGEN_KEYWORDS[allergen])

    def _detect_cooking_method(self, text: str) -> str | None:
        """Detect cooking method from recipe text.

        Args:
            text: Text to analyze (title, instructions, etc.)

        Returns:
            str | None: Detected cooking method or None if not found
        """
        text = text.lower()
        for method, keywords in self.COOKING_METHOD_KEYWORDS.items():
            if any(keyword in text for keyword in keywords):
                return method
        return None

    def _filter_allergens(self, recipe: RecipeSearchResult) -> bool:
        """Check if recipe is safe according to default allergen profile.

        Args:
            recipe: Recipe to check

        Returns:
            bool: True if recipe is safe (contains no default allergens)
        """
        if not self.allergen_filter_enabled:
            return True

        # Combine all text fields that might mention allergens
        text_to_check = " ".join(
            filter(
                None,
                [
                    recipe.title,
                    recipe.description or "",
                    " ".join(recipe.ingredients or []),
                    " ".join(recipe.instructions or []),
                ],
            )
        ).lower()

        # Check for each default allergen
        return all(not self._contains_allergen(text_to_check, allergen) for allergen in self.DEFAULT_ALLERGENS)

    def _apply_allergen_filtering(
        self, results: list[RecipeSearchResult], raise_on_empty: bool = False
    ) -> list[RecipeSearchResult]:
        """Filter out recipes that contain default allergens.

        Args:
            results: List of recipes to filter
            raise_on_empty: Whether to raise an error if no recipes pass filtering

        Returns:
            List[RecipeSearchResult]: Filtered list of recipes

        Raises:
            BusinessError: If raise_on_empty is True and no recipes pass filtering
        """
        if not self.allergen_filter_enabled:
            return results

        filtered = [recipe for recipe in results if self._filter_allergens(recipe)]

        if not filtered and raise_on_empty:
            raise BusinessError(
                message_template=ErrorMessages.RECIPE_CONTAINS_ALLERGENS,
                code=ErrorCode.ALLERGEN_CONFLICT,
                details={"allergens": self.DEFAULT_ALLERGENS, "total_recipes": len(results)},
            )

        return filtered

```

## backend/app/services/recipe_providers/mealdb.py
```
"""TheMealDB recipe provider implementation."""

from __future__ import annotations

from typing import TypedDict, cast

import httpx

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, DomainError, ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.base import ProviderRecipeData, RecipeProvider


class MealDBRecipe(TypedDict, total=False):
    """Type definition for TheMealDB recipe data."""

    idMeal: str
    strMeal: str
    strDrinkAlternate: str | None
    strCategory: str
    strArea: str
    strInstructions: str
    strMealThumb: str
    strTags: str
    strYoutube: str
    strSource: str
    strImageSource: str
    strCreativeCommonsConfirmed: str | None
    dateModified: str | None
    # Dynamic fields for ingredients and measures (1-20)
    strIngredient1: str
    strIngredient2: str
    strIngredient3: str
    strIngredient4: str
    strIngredient5: str
    strIngredient6: str
    strIngredient7: str
    strIngredient8: str
    strIngredient9: str
    strIngredient10: str
    strIngredient11: str
    strIngredient12: str
    strIngredient13: str
    strIngredient14: str
    strIngredient15: str
    strIngredient16: str
    strIngredient17: str
    strIngredient18: str
    strIngredient19: str
    strIngredient20: str
    strMeasure1: str
    strMeasure2: str
    strMeasure3: str
    strMeasure4: str
    strMeasure5: str
    strMeasure6: str
    strMeasure7: str
    strMeasure8: str
    strMeasure9: str
    strMeasure10: str
    strMeasure11: str
    strMeasure12: str
    strMeasure13: str
    strMeasure14: str
    strMeasure15: str
    strMeasure16: str
    strMeasure17: str
    strMeasure18: str
    strMeasure19: str
    strMeasure20: str


class MealDBProvider(RecipeProvider):
    """TheMealDB recipe provider implementation."""

    BASE_URL = "https://www.themealdb.com/api/json/v1/1"  # Free tier API

    def __init__(self) -> None:
        """Initialize TheMealDB provider."""
        super().__init__()
        self.client = httpx.AsyncClient(base_url=self.BASE_URL, timeout=30.0)

    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search for recipes using TheMealDB API.

        Args:
            query: Search query string
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude: List of ingredients to exclude
            max_time: Maximum cooking time in minutes

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            DomainError: If the API request fails
            ValidationError: If the search parameters are invalid
            BusinessError: If no recipes match the filters
        """
        try:
            # TheMealDB only supports name search
            response = await self.client.get("/search.php", params={"s": query})
            response.raise_for_status()
            data = response.json()
            recipes = cast(list[ProviderRecipeData], data.get("meals", []) or [])

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply allergen filtering
            results = self._apply_allergen_filtering(results)

            # Apply additional filters
            if cuisine:
                results = [r for r in results if r.cuisine and cuisine.lower() in r.cuisine.lower()]
            if diet:
                results = [r for r in results if r.diet and diet in r.diet]
            if exclude:
                results = [
                    r
                    for r in results
                    if not any(excluded in " ".join(r.ingredients or []).lower() for excluded in exclude)
                ]
            if max_time:
                results = [r for r in results if r.total_time and r.total_time <= max_time]

            # Apply pagination
            start = offset
            end = offset + limit
            paginated_results = results[start:end]

            return RecipeList(total=len(results), results=paginated_results, source=self.source_name)

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "TheMealDB", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_SEARCH_FAILED, code=ErrorCode.API_ERROR, details={"error": str(e)}
            ) from e

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Args:
            recipe_id: Recipe ID from the provider

        Returns:
            RecipeSearchResult: Detailed recipe information

        Raises:
            DomainError: If the API request fails
            ValidationError: If the recipe ID is invalid
            BusinessError: If the recipe contains allergens
        """
        try:
            response = await self.client.get("/lookup.php", params={"i": recipe_id})
            response.raise_for_status()
            data = response.json()

            if not data.get("meals"):
                raise ValidationError(
                    message_template=ErrorMessages.RECIPE_NOT_FOUND,
                    code=ErrorCode.RECIPE_NOT_FOUND,
                    details={"recipe_id": recipe_id},
                )

            recipe = cast(ProviderRecipeData, data["meals"][0])
            recipe_result = self._normalize_recipe(recipe)

            # Check for allergens
            if not self._filter_allergens(recipe_result):
                raise BusinessError(
                    message_template=ErrorMessages.RECIPE_CONTAINS_ALLERGENS,
                    code=ErrorCode.ALLERGEN_CONFLICT,
                    details={"recipe_id": recipe_id, "allergens": self.DEFAULT_ALLERGENS},
                )

            return recipe_result

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "TheMealDB", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except (ValidationError, BusinessError):
            raise
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_FETCH_FAILED,
                code=ErrorCode.API_ERROR,
                details={"recipe_id": recipe_id, "error": str(e)},
            ) from e

    def _normalize_recipe(self, raw_recipe: ProviderRecipeData) -> RecipeSearchResult:
        """Convert TheMealDB recipe data to standard format.

        Args:
            raw_recipe: Raw recipe data from TheMealDB API

        Returns:
            RecipeSearchResult: Normalized recipe data
        """
        # Extract ingredients and measurements
        ingredients: list[str] = []
        for i in range(1, 21):  # TheMealDB has up to 20 ingredients
            ingredient = raw_recipe.get(f"strIngredient{i}")
            measure = raw_recipe.get(f"strMeasure{i}")
            if ingredient and ingredient.strip():
                ingredients.append(f"{measure} {ingredient}".strip())

        # Split instructions into steps
        instructions = [step.strip() for step in raw_recipe.get("strInstructions", "").split(".") if step.strip()]

        # Extract tags
        tags = []
        if raw_tags := raw_recipe.get("strTags"):
            tags = [tag.strip() for tag in raw_tags.split(",")]

        # Map category to diet if possible
        category = raw_recipe.get("strCategory", "").lower()
        diets: list[str] = []
        if "vegetarian" in category or "vegetarian" in tags:
            diets.append("vegetarian")
        if "vegan" in category or "vegan" in tags:
            diets.append("vegan")

        return RecipeSearchResult(
            id=str(raw_recipe.get("idMeal", "")),
            title=raw_recipe.get("strMeal", ""),
            description=None,  # TheMealDB doesn't provide descriptions
            image_url=raw_recipe.get("strMealThumb"),
            source_url=raw_recipe.get("strSource"),
            prep_time=None,  # TheMealDB doesn't provide timing info
            cook_time=None,
            total_time=None,
            servings=None,  # TheMealDB doesn't provide serving info
            cuisine=raw_recipe.get("strArea"),  # Geographic origin
            diet=diets,
            ingredients=ingredients,
            instructions=instructions,
            source=self.source_name,
        )

```

## backend/app/services/recipe_providers/spoonacular.py
```
"""Spoonacular recipe provider implementation.

This module provides integration with the Spoonacular Recipe API.
It handles recipe search, retrieval, and data normalization.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final, cast

import httpx
from typing_extensions import override

from app.core.config import settings
from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, DomainError, ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.base import RecipeProvider

if TYPE_CHECKING:
    from collections.abc import Sequence


class SpoonacularProvider(RecipeProvider):
    """Spoonacular recipe provider implementation.

    This class implements the RecipeProvider interface for the Spoonacular API.
    It provides methods for searching recipes and retrieving recipe details.

    Attributes:
        BASE_URL: The base URL for the Spoonacular API.
        source_name: The name identifier for this provider.
        _SUPPORTED_ALLERGENS: List of allergens directly supported by Spoonacular.
        _DEFAULT_TIMEOUT: Default timeout for API requests in seconds.
    """

    BASE_URL: Final[str] = "https://api.spoonacular.com"
    source_name: Final[str] = "spoonacular"

    _SUPPORTED_ALLERGENS: Final[list[str]] = ["dairy", "egg"]
    _DEFAULT_TIMEOUT: Final[float] = 30.0

    def __init__(self) -> None:
        """Initialize the Spoonacular provider.

        Raises:
            ValidationError: If the Spoonacular API key is not configured.
        """
        if not settings.SPOONACULAR_API_KEY:
            raise ValidationError(
                message_template=ErrorMessages.INVALID_CREDENTIALS,
                code=ErrorCode.VALIDATION_ERROR,
                details={"provider": self.source_name},
            )

        super().__init__(api_key=settings.SPOONACULAR_API_KEY)
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL, params={"apiKey": self.api_key}, timeout=self._DEFAULT_TIMEOUT
        )

    @override
    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: Sequence[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search for recipes using the Spoonacular API.

        Args:
            query: Search query string.
            offset: Number of results to skip.
            limit: Maximum number of results to return.
            cuisine: Filter by cuisine type.
            diet: Filter by diet type.
            exclude: List of ingredients to exclude.
            max_time: Maximum total cooking time in minutes.

        Returns:
            RecipeList containing search results.

        Raises:
            DomainError: If the API request fails.
            ValidationError: If the search parameters are invalid.
            BusinessError: If no recipes match the filters.
        """
        params: dict[str, Any] = {
            "query": query,
            "offset": offset,
            "number": limit,
            "intolerances": ",".join(self._SUPPORTED_ALLERGENS),
            "addRecipeInformation": True,  # Get full recipe details
            "fillIngredients": True,  # Get detailed ingredient info
            "instructionsRequired": True,  # Only recipes with instructions
        }

        if cuisine:
            params["cuisine"] = cuisine
        if diet:
            params["diet"] = diet
        if exclude:
            params["excludeIngredients"] = ",".join(exclude)
        if max_time:
            params["maxReadyTime"] = max_time

        try:
            response = await self.client.get("/recipes/complexSearch", params=params)
            response.raise_for_status()
            data = cast(dict[str, Any], response.json())
            recipes = data.get("results", [])

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply additional allergen filtering for soy and any missed items
            results = self._apply_allergen_filtering(results)

            return RecipeList(
                total=data.get("totalResults", len(results)), results=results[:limit], source=self.source_name
            )

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "Spoonacular", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_SEARCH_FAILED, code=ErrorCode.API_ERROR, details={"error": str(e)}
            ) from e

    @override
    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Args:
            recipe_id: The Spoonacular recipe ID.

        Returns:
            RecipeSearchResult containing the recipe details.

        Raises:
            DomainError: If the API request fails.
            ValidationError: If the recipe ID is invalid.
            BusinessError: If the recipe contains allergens.
        """
        try:
            response = await self.client.get(
                f"/recipes/{recipe_id}/information",
                params={
                    "includeNutrition": False  # Skip nutrition data to reduce API points
                },
            )
            response.raise_for_status()
            recipe_data = cast(dict[str, Any], response.json())

            recipe = self._normalize_recipe(recipe_data)

            # Check for allergens
            if not self._filter_allergens(recipe):
                raise BusinessError(
                    message_template=ErrorMessages.RECIPE_CONTAINS_ALLERGENS,
                    code=ErrorCode.ALLERGEN_CONFLICT,
                    details={"recipe_id": recipe_id, "allergens": self.DEFAULT_ALLERGENS},
                )

            return recipe

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise ValidationError(
                    message_template=ErrorMessages.RECIPE_NOT_FOUND,
                    code=ErrorCode.RECIPE_NOT_FOUND,
                    details={"recipe_id": recipe_id},
                ) from e
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "Spoonacular", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except BusinessError:
            raise
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_FETCH_FAILED,
                code=ErrorCode.API_ERROR,
                details={"recipe_id": recipe_id, "error": str(e)},
            ) from e

    def _normalize_recipe(self, raw_recipe: dict[str, Any]) -> RecipeSearchResult:
        """Convert Spoonacular recipe data to standard format.

        Args:
            raw_recipe: Raw recipe data from Spoonacular API.

        Returns:
            Normalized RecipeSearchResult object.
        """
        # Extract ingredients
        ingredients: list[str] = []
        for ingredient in raw_recipe.get("extendedIngredients", []):
            if original := ingredient.get("original"):
                ingredients.append(original)

        # Extract instructions
        instructions: list[str] = []
        for step in raw_recipe.get("analyzedInstructions", []):
            for step_detail in step.get("steps", []):
                if step_text := step_detail.get("step"):
                    instructions.append(step_text)

        # Extract diets
        diets: list[str] = []
        if raw_recipe.get("vegetarian"):
            diets.append("vegetarian")
        if raw_recipe.get("vegan"):
            diets.append("vegan")
        if raw_recipe.get("glutenFree"):
            diets.append("gluten-free")
        if raw_recipe.get("dairyFree"):
            diets.append("dairy-free")

        return RecipeSearchResult(
            id=str(raw_recipe.get("id", "")),
            title=raw_recipe.get("title", ""),
            description=raw_recipe.get("summary"),  # HTML summary
            image_url=raw_recipe.get("image"),
            source_url=raw_recipe.get("sourceUrl"),
            prep_time=raw_recipe.get("preparationMinutes"),
            cook_time=raw_recipe.get("cookingMinutes"),
            total_time=raw_recipe.get("readyInMinutes"),
            servings=raw_recipe.get("servings"),
            cuisine=raw_recipe.get("cuisines", [None])[0],  # Take first cuisine if available
            diet=diets,
            ingredients=ingredients,
            instructions=instructions,
            source=self.source_name,
        )

```

## backend/app/services/recipe_providers/tasty.py
```
"""Tasty recipe provider implementation."""

from __future__ import annotations

from typing import Any, cast

import httpx

from app.core.config import settings
from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, DomainError, ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.base import ProviderRecipeData, RecipeProvider


class TastyProvider(RecipeProvider):
    """Tasty recipe provider implementation."""

    BASE_URL = "https://tasty.p.rapidapi.com"

    def __init__(self) -> None:
        """Initialize the Tasty provider.

        Raises:
            ValidationError: If API key is not configured.
        """
        if not settings.TASTY_API_KEY:
            raise ValidationError(
                message_template=ErrorMessages.INVALID_CREDENTIALS,
                code=ErrorCode.VALIDATION_ERROR,
                details={"provider": "tasty"},
            )

        super().__init__(api_key=settings.TASTY_API_KEY)
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers=(
                {"X-RapidAPI-Key": self.api_key, "X-RapidAPI-Host": "tasty.p.rapidapi.com"} if self.api_key else {}
            ),
            timeout=30.0,
        )

    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search for recipes using the Tasty API.

        Args:
            query: Search query string
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude: List of ingredients to exclude
            max_time: Maximum cooking time in minutes

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            DomainError: If the API request fails
            ValidationError: If the search parameters are invalid
            BusinessError: If no recipes match the filters
        """
        params: dict[str, Any] = {
            "q": query,
            "from": offset,
            "size": limit,
            # Add dietary tags to API request for better filtering
            "tags": "dairy-free,egg-free",  # Tasty supports some dietary filters
        }

        try:
            response = await self.client.get("/recipes/list", params=params)
            response.raise_for_status()
            data = response.json()
            recipes = cast(list[ProviderRecipeData], data.get("results", []))

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply allergen filtering as a safety check
            results = self._apply_allergen_filtering(results)

            # Apply additional filters
            if cuisine:
                results = [r for r in results if r.cuisine and cuisine.lower() in r.cuisine.lower()]
            if diet:
                results = [r for r in results if r.diet and diet in r.diet]
            if exclude:
                results = [
                    r
                    for r in results
                    if not any(excluded in " ".join(r.ingredients or []).lower() for excluded in exclude)
                ]
            if max_time:
                results = [r for r in results if r.total_time and r.total_time <= max_time]

            return RecipeList(total=data.get("count", len(results)), results=results[:limit], source=self.source_name)

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "Tasty", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_SEARCH_FAILED, code=ErrorCode.API_ERROR, details={"error": str(e)}
            ) from e

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Args:
            recipe_id: Recipe ID from the provider

        Returns:
            RecipeSearchResult: Detailed recipe information

        Raises:
            DomainError: If the API request fails
            ValidationError: If the recipe ID is invalid
            BusinessError: If the recipe contains allergens
        """
        try:
            response = await self.client.get("/recipes/get-more-info", params={"id": recipe_id})
            response.raise_for_status()
            recipe_data = cast(ProviderRecipeData, response.json())

            recipe = self._normalize_recipe(recipe_data)

            # Check for allergens
            if not self._filter_allergens(recipe):
                raise BusinessError(
                    message_template=ErrorMessages.RECIPE_CONTAINS_ALLERGENS,
                    code=ErrorCode.ALLERGEN_CONFLICT,
                    details={"recipe_id": recipe_id, "allergens": self.DEFAULT_ALLERGENS},
                )

            return recipe

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise ValidationError(
                    message_template=ErrorMessages.RECIPE_NOT_FOUND,
                    code=ErrorCode.RECIPE_NOT_FOUND,
                    details={"recipe_id": recipe_id},
                ) from e
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "Tasty", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except BusinessError:
            raise
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_FETCH_FAILED,
                code=ErrorCode.API_ERROR,
                details={"recipe_id": recipe_id, "error": str(e)},
            ) from e

    def _normalize_recipe(self, raw_recipe: ProviderRecipeData) -> RecipeSearchResult:
        """Convert Tasty recipe data to standard format.

        Args:
            raw_recipe: Raw recipe data from Tasty API

        Returns:
            RecipeSearchResult: Normalized recipe data
        """
        # Extract instructions from components and instructions
        instructions: list[str] = []
        for section in raw_recipe.get("instructions", []):
            if step := section.get("display_text"):
                instructions.append(step)

        # Extract ingredients from components and measurements
        ingredients: list[str] = []
        for section in raw_recipe.get("sections", []):
            for component in section.get("components", []):
                if ingredient := component.get("raw_text"):
                    ingredients.append(ingredient)

        # Calculate total time from prep and cook time
        prep_time = raw_recipe.get("prep_time_minutes")
        cook_time = raw_recipe.get("cook_time_minutes")
        total_time = (prep_time or 0) + (cook_time or 0) if prep_time or cook_time else None

        # Extract cuisine and diet tags
        tags = raw_recipe.get("tags", [])
        cuisine_tags = [tag.get("display_name") for tag in tags if tag.get("type") == "cuisine"]
        diet_tags: list[str] = [tag.get("display_name") for tag in tags if tag.get("type") == "dietary"]

        return RecipeSearchResult(
            id=str(raw_recipe.get("id", "")),
            title=raw_recipe.get("name", ""),
            description=raw_recipe.get("description"),
            image_url=raw_recipe.get("thumbnail_url"),
            source_url=raw_recipe.get("original_video_url"),  # Tasty focuses on video content
            prep_time=prep_time,
            cook_time=cook_time,
            total_time=total_time,
            servings=raw_recipe.get("num_servings"),
            cuisine=cuisine_tags[0] if cuisine_tags else None,
            diet=diet_tags,
            ingredients=ingredients,
            instructions=instructions,
            source=self.source_name,
        )

```

## backend/app/services/recipe_providers/recipe_puppy.py
```
"""Recipe Puppy provider implementation."""

from __future__ import annotations

from typing import Any, cast

import httpx

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import DomainError, ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.base import ProviderRecipeData, RecipeProvider


class RecipePuppyProvider(RecipeProvider):
    """Recipe Puppy provider implementation."""

    BASE_URL = "http://www.recipepuppy.com/api"

    def __init__(self) -> None:
        """Initialize Recipe Puppy provider."""
        super().__init__()
        self.client = httpx.AsyncClient(base_url=self.BASE_URL, timeout=30.0)

    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search for recipes using Recipe Puppy API.

        Args:
            query: Search query string
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude: List of ingredients to exclude
            max_time: Maximum cooking time in minutes

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            DomainError: If the API request fails
            ValidationError: If the search parameters are invalid
            BusinessError: If no recipes match the filters
        """
        # Calculate page number (Recipe Puppy uses 10 results per page)
        page = (offset // 10) + 1

        params: dict[str, Any] = {"q": query, "p": page}

        # Add ingredients to exclude
        if exclude:
            params["excludedIngredients"] = ",".join(exclude)

        try:
            response = await self.client.get("/", params=params)
            response.raise_for_status()
            data = response.json()
            recipes = cast(list[ProviderRecipeData], data.get("results", []))

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply allergen filtering
            results = self._apply_allergen_filtering(results)

            # Apply additional filters
            if cuisine:
                results = [r for r in results if r.cuisine and cuisine.lower() in r.cuisine.lower()]
            if diet:
                results = [r for r in results if r.diet and diet in r.diet]
            if max_time:
                results = [r for r in results if r.total_time and r.total_time <= max_time]

            # Handle pagination
            start = offset % 10  # Offset within the current page
            paginated_results = results[start : start + limit]

            return RecipeList(
                total=len(results),  # Recipe Puppy doesn't provide total count
                results=paginated_results,
                source=self.source_name,
            )

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "Recipe Puppy", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_SEARCH_FAILED, code=ErrorCode.API_ERROR, details={"error": str(e)}
            ) from e

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Args:
            recipe_id: Recipe ID from the provider

        Returns:
            RecipeSearchResult: Detailed recipe information

        Raises:
            DomainError: If the API request fails
            ValidationError: If the recipe ID is invalid
            BusinessError: If the recipe contains allergens
        """
        # Recipe Puppy doesn't support direct recipe lookup by ID
        # We would need to search and filter by our generated ID
        raise ValidationError(
            message_template=ErrorMessages.OPERATION_NOT_SUPPORTED,
            code=ErrorCode.INVALID_OPERATION,
            details={
                "operation": "get_recipe_by_id",
                "provider": self.source_name,
                "reason": "Recipe Puppy API does not support direct recipe lookup",
            },
        )

    def _normalize_recipe(self, raw_recipe: ProviderRecipeData) -> RecipeSearchResult:
        """Convert Recipe Puppy data to standard format.

        Args:
            raw_recipe: Raw recipe data from Recipe Puppy API

        Returns:
            RecipeSearchResult: Normalized recipe data
        """
        # Split ingredients string into list
        ingredients = [ing.strip() for ing in raw_recipe.get("ingredients", "").split(",") if ing.strip()]

        # Generate a stable ID from the title and URL
        recipe_id = str(hash(f"{raw_recipe.get('title', '')}{raw_recipe.get('href', '')}"))

        return RecipeSearchResult(
            id=recipe_id,
            title=raw_recipe.get("title", ""),
            description=None,  # Recipe Puppy doesn't provide descriptions
            image_url=raw_recipe.get("thumbnail"),
            source_url=raw_recipe.get("href"),
            prep_time=None,  # Recipe Puppy doesn't provide timing info
            cook_time=None,
            total_time=None,
            servings=None,  # Recipe Puppy doesn't provide serving info
            cuisine=None,  # Recipe Puppy doesn't provide cuisine info
            diet=None,  # Recipe Puppy doesn't provide diet info
            ingredients=ingredients,
            instructions=[],  # Recipe Puppy doesn't provide instructions
            source=self.source_name,
        )

```

## backend/app/services/recipe_providers/factory.py
```
"""Recipe provider factory."""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.core.config import settings
from app.core.constants import ErrorMessages
from app.core.exceptions import ConfigurationError
from app.services.recipe_providers.api_ninjas import APINinjasProvider
from app.services.recipe_providers.edamam import EdamamProvider
from app.services.recipe_providers.mealdb import TheMealDBProvider
from app.services.recipe_providers.recipe_puppy import RecipePuppyProvider
from app.services.recipe_providers.spoonacular import SpoonacularProvider
from app.services.recipe_providers.tasty import TastyProvider

if TYPE_CHECKING:
    from collections.abc import Mapping

    from app.services.recipe_providers.base import RecipeProvider


class RecipeProviderFactory:
    """Factory for creating recipe providers."""

    PROVIDERS: Mapping[str, type[RecipeProvider]] = {
        "spoonacular": SpoonacularProvider,
        "tasty": TastyProvider,
        "edamam": EdamamProvider,
        "mealdb": TheMealDBProvider,
        "recipe_puppy": RecipePuppyProvider,
        "api_ninjas": APINinjasProvider,
    }

    def __init__(self) -> None:
        """Initialize the factory."""
        self._providers: dict[str, RecipeProvider] = {}

    def get_provider(self, provider_name: str) -> RecipeProvider:
        """Get a recipe provider by name.

        Args:
            provider_name: Name of the provider to get

        Returns:
            Recipe provider instance

        Raises:
            ConfigurationError: If provider initialization fails
        """
        if provider_name not in self._providers:
            if provider_name not in self.PROVIDERS:
                raise ConfigurationError(
                    ErrorMessages.CONFIG_INVALID_VALUE.format(
                        key="provider_name", details=f"Unknown provider: {provider_name}"
                    )
                )

            try:
                provider_class = self.PROVIDERS[provider_name]
                self._providers[provider_name] = provider_class()
            except Exception as e:
                raise ConfigurationError(
                    ErrorMessages.RECIPE_PROVIDER_INIT_FAILED.format(provider=provider_name, details=str(e))
                ) from e

        return self._providers[provider_name]

    def get_all_providers(self) -> list[RecipeProvider]:
        """Get all configured recipe providers.

        Returns:
            List of recipe provider instances
        """
        if not settings.ENABLE_EXTERNAL_PROVIDERS:
            return []

        providers: list[RecipeProvider] = []
        for provider_name in self.PROVIDERS:
            try:
                providers.append(self.get_provider(provider_name))
            except ConfigurationError:
                continue  # Skip providers that fail to initialize

        return providers

```

## backend/app/services/recipe_providers/api_ninjas.py
```
"""API Ninjas recipe provider implementation."""

from __future__ import annotations

from typing import Any, cast

import httpx

from app.core.config import settings
from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import DomainError, ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult
from app.services.recipe_providers.base import ProviderRecipeData, RecipeProvider


class APINinjasProvider(RecipeProvider):
    """API Ninjas recipe provider implementation."""

    BASE_URL = "https://api.api-ninjas.com/v1"

    def __init__(self) -> None:
        """Initialize the API Ninjas provider.

        Raises:
            ValidationError: If API key is not configured.
        """
        if not settings.API_NINJAS_API_KEY:
            raise ValidationError(
                message_template=ErrorMessages.INVALID_CREDENTIALS,
                code=ErrorCode.VALIDATION_ERROR,
                details={"provider": "api_ninjas"},
            )

        super().__init__(api_key=settings.API_NINJAS_API_KEY)
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL, headers={"X-Api-Key": self.api_key} if self.api_key else {}, timeout=30.0
        )

    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search for recipes using the API Ninjas API.

        Args:
            query: Search query string
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude: List of ingredients to exclude
            max_time: Maximum cooking time in minutes

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            DomainError: If the API request fails
            ValidationError: If the search parameters are invalid
            BusinessError: If no recipes match the filters
        """
        params: dict[str, Any] = {"query": query, "offset": offset, "limit": limit}

        try:
            response = await self.client.get("/recipes", params=params)
            response.raise_for_status()
            recipes = cast(list[ProviderRecipeData], response.json())

            # Convert recipes to standard format
            results = [self._normalize_recipe(recipe) for recipe in recipes]

            # Apply allergen filtering first
            results = self._apply_allergen_filtering(results)

            # Apply additional filters
            if cuisine:
                results = [r for r in results if r.cuisine and cuisine.lower() in r.cuisine.lower()]
            if diet:
                results = [r for r in results if r.diet and diet in r.diet]
            if exclude:
                results = [
                    r
                    for r in results
                    if not any(excluded in " ".join(r.ingredients or []).lower() for excluded in exclude)
                ]
            if max_time:
                results = [r for r in results if r.total_time and r.total_time <= max_time]

            return RecipeList(total=len(results), results=results[:limit], source=self.source_name)

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "API Ninjas", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_SEARCH_FAILED, code=ErrorCode.API_ERROR, details={"error": str(e)}
            ) from e

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Args:
            recipe_id: Recipe ID from the provider

        Returns:
            RecipeSearchResult: Detailed recipe information

        Raises:
            DomainError: If the API request fails
            ValidationError: If the recipe ID is invalid
            BusinessError: If the recipe contains allergens
        """
        # API Ninjas doesn't support direct recipe lookup by ID
        raise ValidationError(
            message_template=ErrorMessages.OPERATION_NOT_SUPPORTED,
            code=ErrorCode.INVALID_OPERATION,
            details={
                "operation": "get_recipe_by_id",
                "provider": self.source_name,
                "reason": "API Ninjas does not support direct recipe lookup",
            },
        )

    def _normalize_recipe(self, raw_recipe: ProviderRecipeData) -> RecipeSearchResult:
        """Convert API Ninjas recipe data to standard format.

        Args:
            raw_recipe: Raw recipe data from API Ninjas API

        Returns:
            RecipeSearchResult: Normalized recipe data
        """
        # Split instructions into steps
        instructions = [step.strip() for step in raw_recipe.get("instructions", "").split(".") if step.strip()]

        # Split ingredients into list
        ingredients = [ing.strip() for ing in raw_recipe.get("ingredients", "").split(",") if ing.strip()]

        return RecipeSearchResult(
            id=str(hash(raw_recipe.get("title", ""))),  # Generate stable ID from title
            title=raw_recipe.get("title", ""),
            description=None,  # API Ninjas doesn't provide descriptions
            image_url=None,  # API Ninjas doesn't provide images
            source_url=None,  # API Ninjas doesn't provide source URLs
            prep_time=None,  # API Ninjas doesn't separate prep/cook time
            cook_time=raw_recipe.get("cooking_time"),
            total_time=raw_recipe.get("cooking_time"),
            servings=raw_recipe.get("servings"),
            cuisine=None,  # API Ninjas doesn't provide cuisine info
            diet=None,  # API Ninjas doesn't provide diet info
            ingredients=ingredients,
            instructions=instructions,
            source=self.source_name,
        )

```

## backend/app/services/recipe_providers/__init__.py
```
"""Services package.

This package contains service layer modules for business logic.
"""

```

## backend/app/services/recipe_providers/edamam.py
```
"""Edamam recipe provider."""

from __future__ import annotations

from typing import Any

import httpx

from app.core.config import settings
from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, DomainError, ValidationError
from app.schemas.recipe import RecipeList, RecipeSearchResult

from .base import RecipeProvider


class EdamamProvider(RecipeProvider):
    """Edamam recipe provider implementation."""

    BASE_URL = "https://api.edamam.com"

    def __init__(self) -> None:
        """Initialize the Edamam provider.

        Raises:
            ValidationError: If API credentials are not configured.
        """
        super().__init__()
        if not settings.EDAMAM_APP_ID or not settings.EDAMAM_APP_KEY:
            raise ValidationError(
                message_template=ErrorMessages.INVALID_CREDENTIALS,
                code=ErrorCode.VALIDATION_ERROR,
                details={"provider": self.source_name},
            )
        self.app_id = settings.EDAMAM_APP_ID
        self.app_key = settings.EDAMAM_APP_KEY
        self.client = httpx.AsyncClient(base_url=self.BASE_URL, timeout=30.0)

    async def search_recipes(
        self,
        query: str,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude: list[str] | None = None,
        max_time: int | None = None,
    ) -> RecipeList:
        """Search for recipes using the Edamam API.

        Args:
            query: Search query string
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude: List of ingredients to exclude
            max_time: Maximum cooking time in minutes

        Returns:
            RecipeList: List of recipes matching the search criteria

        Raises:
            DomainError: If the API request fails
            ValidationError: If the search parameters are invalid
            BusinessError: If no recipes match the filters
        """
        # Build health labels for allergen filtering
        health_labels = ["dairy-free", "egg-free"]

        params: dict[str, Any] = {
            "q": query,
            "app_id": self.app_id,
            "app_key": self.app_key,
            "from": offset,
            "to": offset + limit,
            "health": health_labels,  # Apply allergen filters at API level
        }

        if cuisine:
            params["cuisineType"] = cuisine
        if diet:
            params["diet"] = diet
        if exclude:
            params["excluded"] = exclude
        if max_time:
            params["time"] = f"1-{max_time}"  # Format: min-max minutes

        try:
            response = await self.client.get("/api/recipes/v2", params=params)
            response.raise_for_status()
            data = response.json()
            hits = data.get("hits", [])

            # Convert recipes to standard format
            results = [self._normalize_recipe(hit["recipe"]) for hit in hits]

            # Apply additional allergen filtering for soy and any missed items
            results = self._apply_allergen_filtering(results)

            return RecipeList(total=data.get("count", len(results)), results=results[:limit], source=self.source_name)

        except httpx.HTTPStatusError as e:
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "Edamam", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_SEARCH_FAILED, code=ErrorCode.API_ERROR, details={"error": str(e)}
            ) from e

    async def get_recipe_by_id(self, recipe_id: str) -> RecipeSearchResult:
        """Get recipe details by ID.

        Args:
            recipe_id: Recipe ID from the provider

        Returns:
            RecipeSearchResult: Detailed recipe information

        Raises:
            DomainError: If the API request fails
            ValidationError: If the recipe ID is invalid
            BusinessError: If the recipe contains allergens
        """
        try:
            # Edamam uses URLs as IDs, so we need to decode it
            response = await self.client.get(
                recipe_id,  # Full URL from search results
                params={"app_id": self.app_id, "app_key": self.app_key, "type": "public"},
            )
            response.raise_for_status()
            recipe_data = response.json()["recipe"]

            recipe = self._normalize_recipe(recipe_data)

            # Check for allergens
            if not self._filter_allergens(recipe):
                raise BusinessError(
                    message_template=ErrorMessages.RECIPE_CONTAINS_ALLERGENS,
                    code=ErrorCode.ALLERGEN_CONFLICT,
                    details={"recipe_id": recipe_id, "allergens": self.DEFAULT_ALLERGENS},
                )

            return recipe

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise ValidationError(
                    message_template=ErrorMessages.RECIPE_NOT_FOUND,
                    code=ErrorCode.RECIPE_NOT_FOUND,
                    details={"recipe_id": recipe_id},
                ) from e
            raise DomainError(
                message_template=ErrorMessages.EXTERNAL_SERVICE_ERROR,
                code=ErrorCode.EXTERNAL_SERVICE_ERROR,
                details={"service": "Edamam", "status_code": e.response.status_code, "error": str(e)},
            ) from e
        except BusinessError:
            raise
        except Exception as e:
            raise DomainError(
                message_template=ErrorMessages.RECIPE_FETCH_FAILED,
                code=ErrorCode.API_ERROR,
                details={"recipe_id": recipe_id, "error": str(e)},
            ) from e

    def _normalize_recipe(self, raw_recipe: dict[str, Any]) -> RecipeSearchResult:
        """Convert Edamam recipe data to standard format."""
        # Extract cooking time
        total_time = raw_recipe.get("totalTime")
        if total_time and total_time > 0:
            prep_time = total_time * 0.3  # Estimate prep time as 30% of total
            cook_time = total_time * 0.7  # Estimate cook time as 70% of total
        else:
            prep_time = None
            cook_time = None

        # Extract diet labels
        diets: list[str] = []
        if raw_recipe.get("healthLabels"):
            for label in raw_recipe["healthLabels"]:
                label = label.lower()
                if any(d in label for d in ["vegetarian", "vegan", "pescatarian", "paleo", "keto"]):
                    diets.append(label)

        # Extract cuisine type
        cuisines = raw_recipe.get("cuisineType", [])
        cuisine = cuisines[0] if cuisines else None

        return RecipeSearchResult(
            id=raw_recipe.get("uri", "").split("#recipe_")[-1],  # Extract ID from URI
            title=raw_recipe.get("label", ""),
            description=raw_recipe.get("summary"),
            image_url=raw_recipe.get("image"),
            source_url=raw_recipe.get("url"),
            prep_time=prep_time,
            cook_time=cook_time,
            total_time=total_time if total_time and total_time > 0 else None,
            servings=raw_recipe.get("yield"),
            cuisine=cuisine,
            diet=diets,
            ingredients=[ing.get("text", "") for ing in raw_recipe.get("ingredients", [])],
            instructions=raw_recipe.get("instructionLines", []),  # Some recipes might not have instructions
            source=self.source_name,
        )

```

## backend/migrations/versions/01afbfc26ab3_initial_migration.py
```
"""Initial migration

Revision ID: 01afbfc26ab3
Revises:
Create Date: 2025-02-02 01:29:57.635743

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "01afbfc26ab3"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

```

## backend/app/schemas/base.py
```
"""Base schema classes."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """Base schema class with common configuration."""

    model_config = ConfigDict(from_attributes=True)

```

## backend/app/schemas/recipe.py
```
"""Recipe schemas."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field, ValidationInfo, field_validator

from app.schemas.base import BaseSchema

if TYPE_CHECKING:
    from datetime import datetime


class RecipeBase(BaseSchema):
    """Base recipe schema."""

    title: str = Field(..., description="Recipe title", min_length=1, max_length=255)
    description: str | None = Field(None, description="Recipe description")
    prep_time: int | None = Field(None, description="Preparation time in minutes", ge=0)
    cook_time: int | None = Field(None, description="Cooking time in minutes", ge=0)
    servings: int | None = Field(None, description="Number of servings", ge=1)
    difficulty: str | None = Field(None, description="Recipe difficulty level")
    source_url: str | None = Field(None, description="Original recipe URL")
    image_url: str | None = Field(None, description="Recipe image URL")
    notes: str | None = Field(None, description="Additional notes")
    is_favorite: bool = Field(False, description="Whether the recipe is marked as favorite")
    is_private: bool = Field(False, description="Whether the recipe is private")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Spaghetti Carbonara",
                "description": "Classic Italian pasta dish",
                "prep_time": 10,
                "cook_time": 30,
                "servings": 4,
                "difficulty": "medium",
                "source_url": "https://www.example.com/spaghetti-carbonara",
                "image_url": "https://www.example.com/spaghetti-carbonara.jpg",
                "notes": "This recipe is a classic Italian dish made with spaghetti, pancetta, eggs, and pecorino cheese. It's quick and easy to make, and it's perfect for a weeknight dinner.",
                "is_favorite": True,
                "is_private": False,
            }
        }
    )


class RecipeCreate(RecipeBase):
    """Recipe creation schema."""

    ingredients: list[str] = Field(..., description="List of ingredients")
    instructions: list[str] = Field(..., description="List of instructions")
    cuisine_type_id: int | None = Field(None, description="Cuisine type ID")
    cook_method_id: int | None = Field(None, description="Cooking method ID")
    protein_type_id: int | None = Field(None, description="Protein type ID")
    meal_type_id: int | None = Field(None, description="Meal type ID")
    allergens: list[int] = Field(default_factory=list, description="List of allergen IDs")
    dietary_restrictions: list[int] = Field(default_factory=list, description="List of dietary restriction IDs")


class RecipeUpdate(RecipeBase):
    """Recipe update schema."""

    ingredients: list[str] | None = Field(None, description="List of ingredients")
    instructions: list[str] | None = Field(None, description="List of instructions")
    cuisine_type_id: int | None = Field(None, description="Cuisine type ID")
    cook_method_id: int | None = Field(None, description="Cooking method ID")
    protein_type_id: int | None = Field(None, description="Protein type ID")
    meal_type_id: int | None = Field(None, description="Meal type ID")
    allergens: list[int] | None = Field(None, description="List of allergen IDs")
    dietary_restrictions: list[int] | None = Field(None, description="List of dietary restriction IDs")

    model_config = ConfigDict(
        json_schema_extra={"example": {"title": "Updated Spaghetti Carbonara", "cook_time": 25, "servings": 2}}
    )


class RecipeResponse(RecipeBase):
    """Recipe response schema."""

    model_config = ConfigDict(from_attributes=True)

    recipe_id: int = Field(..., description="Recipe ID")
    ingredients: list[str] = Field(..., description="List of ingredients")
    instructions: list[str] = Field(..., description="List of instructions")
    cuisine_type: str | None = Field(None, description="Cuisine type name")
    cook_method: str | None = Field(None, description="Cooking method name")
    protein_type: str | None = Field(None, description="Protein type name")
    meal_type: str | None = Field(None, description="Meal type name")
    allergens: list[str] = Field(default_factory=list, description="List of allergen names")
    dietary_restrictions: list[str] = Field(default_factory=list, description="List of dietary restriction names")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")


class RecipeSearchFilter(BaseModel):
    """Recipe search filter schema."""

    cuisine: str | None = Field(None, description="Filter by cuisine type")
    diet: str | None = Field(None, description="Filter by dietary restriction")
    allergens: list[str] | None = Field(None, description="Exclude recipes with these allergens")
    max_time: int | None = Field(None, description="Maximum total cooking time in minutes", ge=0)
    difficulty: str | None = Field(None, description="Filter by difficulty level")
    meal_type: str | None = Field(None, description="Filter by meal type")
    protein_type: str | None = Field(None, description="Filter by protein type")
    cook_method: str | None = Field(None, description="Filter by cooking method")
    is_favorite: bool | None = Field(None, description="Filter by favorite status")
    exclude_ingredients: list[str] | None = Field(None, description="Exclude recipes with these ingredients")
    include_ingredients: list[str] | None = Field(None, description="Include recipes with these ingredients")

    @field_validator("max_time")
    @classmethod
    def validate_max_time(cls, v: int | None) -> int | None:
        """Validate max_time is positive."""
        if v is not None and v < 0:
            msg = "max_time must be non-negative"
            raise ValueError(msg)
        return v


class RecipeSearchResult(BaseModel):
    """Recipe search result."""

    id: str = Field(..., description="Recipe ID")
    title: str = Field(..., description="Recipe title")
    description: str | None = Field(None, description="Recipe description")
    image_url: str | None = Field(None, description="URL to recipe image")
    source_url: str | None = Field(None, description="URL to recipe source")
    prep_time: int | None = Field(None, description="Preparation time in minutes")
    cook_time: int | None = Field(None, description="Cooking time in minutes")
    total_time: int | None = Field(None, description="Total time in minutes")
    servings: int | None = Field(None, description="Number of servings")
    cuisine: str | None = Field(None, description="Cuisine type")
    diet: list[str] | None = Field(None, description="Dietary restrictions")
    ingredients: list[str] | None = Field(None, description="List of ingredients")
    instructions: list[str] | None = Field(None, description="List of instructions")
    source: str = Field(..., description="Source of the recipe (e.g., 'spoonacular', 'edamam')")


class RecipeList(BaseModel):
    """List of recipe search results."""

    total: int = Field(..., description="Total number of results")
    results: list[RecipeSearchResult] = Field(..., description="List of recipe results")
    source: str = Field(..., description="Source of the results")


class PaginatedRecipeResponse(BaseModel):
    """Paginated recipe response schema."""

    items: list[RecipeResponse] = Field(..., description="List of recipes")
    total: int = Field(..., description="Total number of recipes matching the query")
    page: int = Field(..., description="Current page number")
    page_size: int = Field(..., description="Number of items per page")
    pages: int = Field(..., description="Total number of pages")

    @field_validator("pages")
    @classmethod
    def validate_pages(cls, v: int, info: ValidationInfo) -> int:
        """Validate pages is at least 1."""
        if v < 1:
            total = info.data.get("total", 0)
            page_size = info.data.get("page_size", 1)
            return max(1, (total + page_size - 1) // page_size)
        return v

```

## backend/app/schemas/__init__.py
```
"""Schemas package.

This package contains Pydantic models used for request/response validation
and data serialization. Each schema defines the structure and validation
rules for API data.

Example:
    .. code-block:: python

        from app.schemas import RecipeCreate

        # Validate recipe data
        recipe_data = RecipeCreate(
            title="Spaghetti",
            prep_time_minutes=15,
            cook_time_minutes=20
        )
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.schemas.models import (
    Allergen,
    AllergenCreate,
    CookMethod,
    CookMethodCreate,
    CuisineType,
    CuisineTypeCreate,
    DietaryRestriction,
    DietaryRestrictionCreate,
    FamilyMember,
    FamilyMemberCreate,
    Ingredient,
    IngredientCreate,
    MealPlan,
    MealPlanCreate,
    MealType,
    MealTypeCreate,
    ProteinType,
    ProteinTypeCreate,
    Recipe,
    RecipeCreate,
)
from app.schemas.recipe import RecipeList, RecipeSearchFilter, RecipeSearchResult

if TYPE_CHECKING:
    from pydantic import BaseModel

    # Type hints for exported schemas
    Allergen: type[BaseModel]
    AllergenCreate: type[BaseModel]
    CookMethod: type[BaseModel]
    CookMethodCreate: type[BaseModel]
    CuisineType: type[BaseModel]
    CuisineTypeCreate: type[BaseModel]
    DietaryRestriction: type[BaseModel]
    DietaryRestrictionCreate: type[BaseModel]
    FamilyMember: type[BaseModel]
    FamilyMemberCreate: type[BaseModel]
    Ingredient: type[BaseModel]
    IngredientCreate: type[BaseModel]
    MealPlan: type[BaseModel]
    MealPlanCreate: type[BaseModel]
    MealType: type[BaseModel]
    MealTypeCreate: type[BaseModel]
    ProteinType: type[BaseModel]
    ProteinTypeCreate: type[BaseModel]
    Recipe: type[BaseModel]
    RecipeCreate: type[BaseModel]
    RecipeList: type[BaseModel]
    RecipeSearchFilter: type[BaseModel]
    RecipeSearchResult: type[BaseModel]

__version__ = "1.0.0"

__all__ = [
    "Allergen",
    "AllergenCreate",
    "CookMethod",
    "CookMethodCreate",
    "CuisineType",
    "CuisineTypeCreate",
    "DietaryRestriction",
    "DietaryRestrictionCreate",
    "FamilyMember",
    "FamilyMemberCreate",
    "Ingredient",
    "IngredientCreate",
    "MealPlan",
    "MealPlanCreate",
    "MealType",
    "MealTypeCreate",
    "ProteinType",
    "ProteinTypeCreate",
    "Recipe",
    "RecipeCreate",
    "RecipeList",
    "RecipeSearchFilter",
    "RecipeSearchResult",
]

```

## backend/app/schemas/models.py
```
"""Pydantic schemas for database models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from datetime import date, datetime


# --- Recipe Schemas ---
class RecipeInstructionBase(BaseModel):
    step_number: int
    instruction: str


class RecipeInstructionCreate(RecipeInstructionBase):
    pass


class RecipeInstruction(RecipeInstructionBase):
    instruction_id: int
    recipe_id: int

    class Config:
        from_attributes = True


class RecipeBase(BaseModel):
    title: str
    image_url: str | None = None
    source_url: str | None = None
    prep_time_minutes: int | None = None
    cook_time_minutes: int | None = None
    servings: int | None = None
    is_favorite: bool = False
    variations: str | None = None


class RecipeCreate(RecipeBase):
    instructions: list[RecipeInstructionCreate] = []


class RecipeUpdate(BaseModel):
    """Schema for updating a recipe. All fields are optional."""

    title: str | None = None
    image_url: str | None = None
    source_url: str | None = None
    prep_time_minutes: int | None = None
    cook_time_minutes: int | None = None
    servings: int | None = None
    is_favorite: bool | None = None
    variations: str | None = None
    instructions: list[RecipeInstructionCreate] | None = None


class Recipe(RecipeBase):
    recipe_id: int
    last_made_date: date | None = None
    created_at: datetime
    updated_at: datetime
    instructions: list[RecipeInstruction] = []

    class Config:
        from_attributes = True


# --- Ingredient Schemas ---
class IngredientCategoryBase(BaseModel):
    name: str


class IngredientCategoryCreate(IngredientCategoryBase):
    pass


class IngredientCategory(IngredientCategoryBase):
    category_id: int

    class Config:
        orm_mode = True


class IngredientBase(BaseModel):
    name: str
    category_id: int


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(BaseModel):
    """Schema for updating an ingredient. All fields are optional."""

    name: str | None = None
    category_id: int | None = None


class Ingredient(IngredientBase):
    ingredient_id: int

    class Config:
        orm_mode = True


# --- Allergen Schemas ---
class AllergenBase(BaseModel):
    name: str
    severity: str | None = None


class AllergenCreate(AllergenBase):
    pass


class Allergen(AllergenBase):
    allergen_id: int

    class Config:
        orm_mode = True


# --- Cook Method Schemas ---
class CookMethodBase(BaseModel):
    name: str


class CookMethodCreate(CookMethodBase):
    pass


class CookMethod(CookMethodBase):
    method_id: int

    class Config:
        orm_mode = True


# --- Protein Type Schemas ---
class ProteinTypeBase(BaseModel):
    name: str


class ProteinTypeCreate(ProteinTypeBase):
    pass


class ProteinType(ProteinTypeBase):
    protein_id: int

    class Config:
        orm_mode = True


# --- Meal Type Schemas ---
class MealTypeBase(BaseModel):
    name: str


class MealTypeCreate(MealTypeBase):
    pass


class MealType(MealTypeBase):
    meal_type_id: int

    class Config:
        orm_mode = True


# --- Cuisine Type Schemas ---
class CuisineTypeBase(BaseModel):
    name: str
    last_used_date: date | None = None


class CuisineTypeCreate(CuisineTypeBase):
    pass


class CuisineType(CuisineTypeBase):
    cuisine_id: int

    class Config:
        orm_mode = True


# --- Dietary Restriction Schemas ---
class DietaryRestrictionBase(BaseModel):
    name: str


class DietaryRestrictionCreate(DietaryRestrictionBase):
    pass


class DietaryRestriction(DietaryRestrictionBase):
    restriction_id: int

    class Config:
        orm_mode = True


# --- Family Member Schemas ---
class FamilyMemberBase(BaseModel):
    name: str
    birth_date: date | None = None
    notes: str | None = None


class FamilyMemberCreate(FamilyMemberBase):
    pass


class FamilyMember(FamilyMemberBase):
    member_id: int

    class Config:
        orm_mode = True


# --- Allergen Substitution Schemas ---
class AllergenSubstitutionBase(BaseModel):
    allergen_id: int
    substitute_ingredient_id: int
    notes: str | None = None


class AllergenSubstitutionCreate(AllergenSubstitutionBase):
    pass


class AllergenSubstitution(AllergenSubstitutionBase):
    substitution_id: int

    class Config:
        orm_mode = True


# --- Meal Plan Schemas ---
class MealPlanBase(BaseModel):
    recipe_id: int
    planned_date: date
    meal_type_id: int
    notes: str | None = None
    member_id: int


class MealPlanCreate(MealPlanBase):
    pass


class MealPlan(MealPlanBase):
    plan_id: int

    class Config:
        orm_mode = True


# --- Recipe Rating Schemas ---
class RecipeRatingBase(BaseModel):
    recipe_id: int
    member_id: int
    rating: int
    review: str | None = None


class RecipeRatingCreate(RecipeRatingBase):
    pass


class RecipeRating(RecipeRatingBase):
    rating_id: int
    created_at: datetime

    class Config:
        orm_mode = True

```

## backend/app/__init__.py
```
"""Recipe Database Application.

This package provides a FastAPI-based recipe management system with features
for searching, storing, and managing recipes, meal plans, and related data.

Example:
    .. code-block:: python

        from fastapi import FastAPI
        from app import create_application

        app = create_application()
"""

from __future__ import annotations

from typing import Final

from app.main import create_application

# Package version - should match backend/__version__
__version__: Final[str] = "1.0.0"

# Public API
__all__: Final[list[str]] = ["create_application", "__version__"]

```

## backend/app/providers/recipe/http.py
```
"""Base HTTP client for recipe providers."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import httpx
from pydantic import BaseModel

from app.core.constants import ErrorMessages
from app.providers.recipe.exceptions import RecipeNotFoundError, RecipeProviderError, RecipeProviderTimeout

if TYPE_CHECKING:
    from collections.abc import Mapping


class APIResponse(BaseModel):
    """API response wrapper."""

    status_code: int
    data: Any
    headers: Mapping[str, str]


class RecipeHTTPClient:
    """Base HTTP client for recipe providers."""

    def __init__(
        self, base_url: str, api_key: str | None = None, timeout: float = 30.0, headers: dict[str, str] | None = None
    ) -> None:
        """Initialize the HTTP client.

        Args:
            base_url: Base URL for the API
            api_key: Optional API key
            timeout: Request timeout in seconds
            headers: Additional headers to include
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.headers = headers or {}
        self._client: httpx.AsyncClient | None = None

    @property
    def client(self) -> httpx.AsyncClient:
        """Get the HTTP client, creating it if necessary."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url, timeout=self.timeout, headers=self.headers, follow_redirects=True
            )
        return self._client

    async def get(self, path: str, *, params: dict[str, Any] | None = None) -> APIResponse:
        """Make a GET request.

        Args:
            path: API endpoint path
            params: Query parameters

        Returns:
            Wrapped API response

        Raises:
            RecipeProviderError: On API errors
            RecipeNotFoundError: When resource doesn't exist
            RecipeProviderTimeout: On timeout
        """
        try:
            response = await self.client.get(path.lstrip("/"), params=params)
            response.raise_for_status()

            return APIResponse(status_code=response.status_code, data=response.json(), headers=dict(response.headers))

        except httpx.TimeoutException as e:
            raise RecipeProviderTimeout(ErrorMessages.EXTERNAL_SERVICE_TIMEOUT) from e

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise RecipeNotFoundError(ErrorMessages.RECIPE_NOT_FOUND) from e
            raise RecipeProviderError(
                ErrorMessages.API_REQUEST_FAILED.format(details=e.response.text), status_code=e.response.status_code
            ) from e

        except httpx.HTTPError as e:
            raise RecipeProviderError(ErrorMessages.HTTP_ERROR.format(details=str(e))) from e

        except Exception as e:
            raise RecipeProviderError(ErrorMessages.UNKNOWN_ERROR) from e

    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> RecipeHTTPClient:
        """Enter async context."""
        return self

    async def __aexit__(self, *_: object) -> None:
        """Exit async context."""
        await self.close()

```

## backend/app/models/recipe.py
```
"""Recipe domain models."""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from datetime import datetime

    from pydantic import HttpUrl


class CuisineType(str, Enum):
    """Standardized cuisine types across providers."""

    AMERICAN = "american"
    ASIAN = "asian"
    MEDITERRANEAN = "mediterranean"
    ITALIAN = "italian"
    MEXICAN = "mexican"
    INDIAN = "indian"
    FRENCH = "french"
    CHINESE = "chinese"
    JAPANESE = "japanese"
    THAI = "thai"
    VIETNAMESE = "vietnamese"
    KOREAN = "korean"
    MIDDLE_EASTERN = "middle_eastern"
    GREEK = "greek"
    SPANISH = "spanish"
    OTHER = "other"


class DietType(str, Enum):
    """Standardized diet types across providers."""

    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    GLUTEN_FREE = "gluten_free"
    DAIRY_FREE = "dairy_free"
    KETO = "keto"
    PALEO = "paleo"
    LOW_CARB = "low_carb"
    LOW_FAT = "low_fat"
    OTHER = "other"


class CookingMethod(str, Enum):
    """Standardized cooking methods across providers."""

    BAKE = "bake"
    GRILL = "grill"
    FRY = "fry"
    ROAST = "roast"
    BOIL = "boil"
    STEAM = "steam"
    SLOW_COOK = "slow_cook"
    PRESSURE_COOK = "pressure_cook"
    SAUTE = "saute"
    OTHER = "other"


class Ingredient(BaseModel):
    """Standardized ingredient model."""

    name: str
    amount: float | None = None
    unit: str | None = None
    notes: str | None = None
    is_allergen: bool = False


class Instruction(BaseModel):
    """Standardized instruction model."""

    step_number: int
    description: str
    time_minutes: int | None = None
    temperature: float | None = None
    temperature_unit: str | None = None


class NutritionalInfo(BaseModel):
    """Standardized nutritional information."""

    calories: float | None = None
    protein_g: float | None = None
    carbohydrates_g: float | None = None
    fat_g: float | None = None
    fiber_g: float | None = None
    sugar_g: float | None = None
    sodium_mg: float | None = None


class Recipe(BaseModel):
    """Core recipe model that all providers map to."""

    id: str = Field(..., description="Unique identifier for the recipe")
    source_id: str = Field(..., description="Original ID from the provider")
    provider: str = Field(..., description="Name of the recipe provider")

    # Basic Information
    title: str
    description: str | None = None
    image_url: HttpUrl | None = None
    source_url: HttpUrl | None = None
    author: str | None = None
    date_published: datetime | None = None
    date_updated: datetime | None = None

    # Recipe Details
    cuisine: CuisineType | None = None
    diets: list[DietType] = Field(default_factory=list)
    cooking_method: CookingMethod | None = None

    # Time and Servings
    prep_time_minutes: int | None = None
    cook_time_minutes: int | None = None
    total_time_minutes: int | None = None
    servings: int | None = None

    # Ingredients and Instructions
    ingredients: list[Ingredient] = Field(..., min_items=1)
    instructions: list[Instruction] = Field(..., min_items=1)

    # Additional Information
    difficulty_level: int | None = Field(None, ge=1, le=5)
    rating: float | None = Field(None, ge=0, le=5)
    review_count: int | None = Field(None, ge=0)
    nutritional_info: NutritionalInfo | None = None

    # Allergen Information
    is_dairy_free: bool = False
    is_gluten_free: bool = False
    is_egg_free: bool = False
    is_nut_free: bool = False
    is_soy_free: bool = False

    # Tags and Categories
    tags: list[str] = Field(default_factory=list)
    equipment_needed: list[str] = Field(default_factory=list)

    class Config:
        """Pydantic model configuration."""

        json_schema_extra = {
            "example": {
                "id": "recipe_123",
                "source_id": "spoonacular_456",
                "provider": "spoonacular",
                "title": "Spaghetti Carbonara",
                "description": "Classic Italian pasta dish",
                "cuisine": "italian",
                "diets": ["dairy_free"],
                "cooking_method": "boil",
                "prep_time_minutes": 15,
                "cook_time_minutes": 20,
                "ingredients": [
                    {
                        "name": "spaghetti",
                        "amount": 500,
                        "unit": "g",
                    },
                ],
                "instructions": [
                    {
                        "step_number": 1,
                        "description": "Boil water and cook pasta",
                    },
                ],
            },
        }

```

## backend/app/providers/recipe/base.py
```
"""Base recipe provider interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, TypeVar

from app.models.recipe import Recipe

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

T = TypeVar("T", bound=Recipe)


class RecipeProvider(ABC):
    """Base class for recipe providers."""

    def __init__(self, api_key: str | None = None) -> None:
        """Initialize the provider.

        Args:
            api_key: Optional API key for the provider
        """
        self.api_key = api_key

    @property
    @abstractmethod
    def name(self) -> str:
        """Get the provider name."""
        ...

    @abstractmethod
    async def search_recipes(
        self,
        query: str,
        *,
        offset: int = 0,
        limit: int = 20,
        cuisine: str | None = None,
        diet: str | None = None,
        exclude_ingredients: list[str] | None = None,
        max_time: int | None = None,
    ) -> AsyncIterator[T]:
        """Search for recipes.

        Args:
            query: Search query string
            offset: Number of results to skip
            limit: Maximum number of results to return
            cuisine: Filter by cuisine type
            diet: Filter by diet type
            exclude_ingredients: List of ingredients to exclude
            max_time: Maximum total time in minutes

        Yields:
            Recipe objects matching the search criteria
        """
        ...

    @abstractmethod
    async def get_recipe(self, recipe_id: str) -> T:
        """Get a specific recipe by ID.

        Args:
            recipe_id: The recipe ID from this provider

        Returns:
            The recipe details

        Raises:
            RecipeNotFoundError: If the recipe doesn't exist
            RecipeProviderError: If there's an error fetching the recipe
        """
        ...

    @abstractmethod
    async def get_random_recipes(self, *, limit: int = 20, tags: list[str] | None = None) -> AsyncIterator[T]:
        """Get random recipes.

        Args:
            limit: Maximum number of recipes to return
            tags: Optional list of tags to filter by

        Yields:
            Random recipe objects
        """
        ...

    async def __aenter__(self) -> RecipeProvider:
        """Enter async context."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit async context and cleanup resources."""
        await self.close()

    async def close(self) -> None:
        """Close any open connections."""
        # Override if provider needs cleanup

```

## backend/app/models/__init__.py
```
"""Models package.

This package contains SQLAlchemy models that represent database tables
and their relationships. Each model maps to a specific table and defines
its structure and behavior.

Example:
    .. code-block:: python

        from app.models import Recipe

        # Create a new recipe
        recipe = Recipe(title="Spaghetti", prep_time_minutes=15)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.models.models import (
    Allergen,
    CookMethod,
    CuisineType,
    DietaryRestriction,
    FamilyMember,
    Ingredient,
    MealPlan,
    MealType,
    ProteinType,
    Recipe,
)

if TYPE_CHECKING:
    from sqlalchemy.orm import DeclarativeBase

    # Type hints for exported models
    Allergen: type[DeclarativeBase]
    CookMethod: type[DeclarativeBase]
    CuisineType: type[DeclarativeBase]
    DietaryRestriction: type[DeclarativeBase]
    FamilyMember: type[DeclarativeBase]
    Ingredient: type[DeclarativeBase]
    MealPlan: type[DeclarativeBase]
    MealType: type[DeclarativeBase]
    ProteinType: type[DeclarativeBase]
    Recipe: type[DeclarativeBase]

__version__ = "1.0.0"

__all__ = [
    "Allergen",
    "CookMethod",
    "CuisineType",
    "DietaryRestriction",
    "FamilyMember",
    "Ingredient",
    "MealPlan",
    "MealType",
    "ProteinType",
    "Recipe",
]

```

## backend/app/models/models.py
```
"""SQLAlchemy models for the recipe database."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Table, Text, func
from sqlalchemy.orm import mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from datetime import date, datetime

    from sqlalchemy.orm import Mapped

# Association tables for many-to-many relationships
recipe_allergens = Table(
    "recipe_allergens",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("allergen_id", Integer, ForeignKey("allergens.allergen_id"), primary_key=True),
)

recipe_ingredients = Table(
    "recipe_ingredients",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("ingredient_id", Integer, ForeignKey("ingredients.ingredient_id"), primary_key=True),
)

recipe_meal_types = Table(
    "recipe_meal_types",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("meal_type_id", Integer, ForeignKey("meal_types.meal_type_id"), primary_key=True),
)

recipe_cook_methods = Table(
    "recipe_cook_methods",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("method_id", Integer, ForeignKey("cook_methods.method_id"), primary_key=True),
)

recipe_protein_types = Table(
    "recipe_protein_types",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("protein_id", Integer, ForeignKey("protein_types.protein_id"), primary_key=True),
)

recipe_cuisine_types = Table(
    "recipe_cuisine_types",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.recipe_id"), primary_key=True),
    Column("cuisine_id", Integer, ForeignKey("cuisine_types.cuisine_id"), primary_key=True),
)

family_member_dietary_restrictions = Table(
    "family_member_dietary_restrictions",
    Base.metadata,
    Column("member_id", Integer, ForeignKey("family_members.member_id"), primary_key=True),
    Column(
        "restriction_id",
        Integer,
        ForeignKey("dietary_restrictions.restriction_id"),
        primary_key=True,
    ),
)


class RecipeInstruction(Base):
    """Recipe instruction model."""

    __tablename__ = "recipe_instructions"

    instruction_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.recipe_id"), nullable=False)
    step_number: Mapped[int] = mapped_column(Integer, nullable=False)
    instruction: Mapped[str] = mapped_column(Text, nullable=False)

    # Relationship
    recipe: Mapped[Recipe] = relationship("Recipe", back_populates="instructions")


class Recipe(Base):
    """Recipe model."""

    __tablename__ = "recipes"

    recipe_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    image_url: Mapped[str | None] = mapped_column(String(1024))
    source_url: Mapped[str | None] = mapped_column(String(1024))
    prep_time_minutes: Mapped[int | None] = mapped_column(Integer)
    cook_time_minutes: Mapped[int | None] = mapped_column(Integer)
    servings: Mapped[int | None] = mapped_column(Integer)
    is_favorite: Mapped[bool] = mapped_column(Boolean, default=False)
    variations: Mapped[str | None] = mapped_column(Text)
    last_made_date: Mapped[date | None] = mapped_column(Date)

    # Relationships
    instructions: Mapped[list[RecipeInstruction]] = relationship(
        "RecipeInstruction",
        back_populates="recipe",
        cascade="all, delete-orphan",
    )
    allergens: Mapped[list[Allergen]] = relationship("Allergen", secondary=recipe_allergens, back_populates="recipes")
    ingredients: Mapped[list[Ingredient]] = relationship(
        "Ingredient",
        secondary=recipe_ingredients,
        back_populates="recipes",
    )
    meal_types: Mapped[list[MealType]] = relationship(
        "MealType",
        secondary=recipe_meal_types,
        back_populates="recipes",
    )
    cook_methods: Mapped[list[CookMethod]] = relationship(
        "CookMethod",
        secondary=recipe_cook_methods,
        back_populates="recipes",
    )
    protein_types: Mapped[list[ProteinType]] = relationship(
        "ProteinType",
        secondary=recipe_protein_types,
        back_populates="recipes",
    )
    cuisine_types: Mapped[list[CuisineType]] = relationship(
        "CuisineType",
        secondary=recipe_cuisine_types,
        back_populates="recipes",
    )

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    def __repr__(self) -> str:
        """String representation of the recipe."""
        return f"<Recipe {self.title}>"


class IngredientCategory(Base):
    """Ingredient category model."""

    __tablename__ = "ingredient_categories"

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationships
    ingredients: Mapped[list[Ingredient]] = relationship("Ingredient", back_populates="category")


class Ingredient(Base):
    """Ingredient model."""

    __tablename__ = "ingredients"

    ingredient_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("ingredient_categories.category_id"))

    # Relationships
    category: Mapped[IngredientCategory] = relationship("IngredientCategory", back_populates="ingredients")
    recipes: Mapped[list[Recipe]] = relationship("Recipe", secondary=recipe_ingredients, back_populates="ingredients")


class Allergen(Base):
    """Allergen model."""

    __tablename__ = "allergens"

    allergen_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    severity: Mapped[str | None] = mapped_column(String(50))

    # Relationships
    recipes: Mapped[list[Recipe]] = relationship("Recipe", secondary=recipe_allergens, back_populates="allergens")


class CookMethod(Base):
    """Cook method model."""

    __tablename__ = "cook_methods"

    method_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationships
    recipes: Mapped[list[Recipe]] = relationship(
        "Recipe",
        secondary=recipe_cook_methods,
        back_populates="cook_methods",
    )


class ProteinType(Base):
    """Protein type model."""

    __tablename__ = "protein_types"

    protein_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationships
    recipes: Mapped[list[Recipe]] = relationship(
        "Recipe",
        secondary=recipe_protein_types,
        back_populates="protein_types",
    )


class MealType(Base):
    """Meal type model."""

    __tablename__ = "meal_types"

    meal_type_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationships
    recipes: Mapped[list[Recipe]] = relationship("Recipe", secondary=recipe_meal_types, back_populates="meal_types")
    meal_plans: Mapped[list[MealPlan]] = relationship("MealPlan", back_populates="meal_type")


class CuisineType(Base):
    """Cuisine type model."""

    __tablename__ = "cuisine_types"

    cuisine_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    last_used_date: Mapped[date | None] = mapped_column(Date)

    # Relationships
    recipes: Mapped[list[Recipe]] = relationship(
        "Recipe",
        secondary=recipe_cuisine_types,
        back_populates="cuisine_types",
    )


class DietaryRestriction(Base):
    """Dietary restriction model."""

    __tablename__ = "dietary_restrictions"

    restriction_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationships
    family_members: Mapped[list[FamilyMember]] = relationship(
        "FamilyMember",
        secondary=family_member_dietary_restrictions,
        back_populates="dietary_restrictions",
    )


class FamilyMember(Base):
    """Family member model."""

    __tablename__ = "family_members"

    member_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_date: Mapped[date | None] = mapped_column(Date)
    notes: Mapped[str | None] = mapped_column(Text)

    # Relationships
    meal_plans: Mapped[list[MealPlan]] = relationship("MealPlan", back_populates="family_member")
    ratings: Mapped[list[RecipeRating]] = relationship("RecipeRating", back_populates="family_member")
    dietary_restrictions: Mapped[list[DietaryRestriction]] = relationship(
        "DietaryRestriction",
        secondary=family_member_dietary_restrictions,
        back_populates="family_members",
    )


class AllergenSubstitution(Base):
    """Allergen substitution model."""

    __tablename__ = "allergen_substitutions"

    substitution_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    allergen_id: Mapped[int] = mapped_column(ForeignKey("allergens.allergen_id"), nullable=False)
    substitute_ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.ingredient_id"), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text)


class MealPlan(Base):
    """Meal plan model."""

    __tablename__ = "meal_plans"

    plan_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.recipe_id"), nullable=False)
    planned_date: Mapped[date] = mapped_column(Date, nullable=False)
    meal_type_id: Mapped[int] = mapped_column(ForeignKey("meal_types.meal_type_id"), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text)
    member_id: Mapped[int] = mapped_column(ForeignKey("family_members.member_id"), nullable=False)

    # Relationships
    recipe: Mapped[Recipe] = relationship("Recipe")
    meal_type: Mapped[MealType] = relationship("MealType", back_populates="meal_plans")
    family_member: Mapped[FamilyMember] = relationship("FamilyMember", back_populates="meal_plans")


class RecipeRating(Base):
    """Recipe rating model."""

    __tablename__ = "recipe_ratings"

    rating_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.recipe_id"), nullable=False)
    member_id: Mapped[int] = mapped_column(ForeignKey("family_members.member_id"), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Relationships
    recipe: Mapped[Recipe] = relationship("Recipe")
    family_member: Mapped[FamilyMember] = relationship("FamilyMember", back_populates="ratings")

```

## backend/app/providers/recipe/exceptions.py
```
"""Recipe provider exceptions."""

from __future__ import annotations

from http import HTTPStatus

from app.core.exceptions import ExternalServiceError, NotFoundError


class RecipeProviderError(ExternalServiceError):
    """Base exception for recipe provider errors."""

    def __init__(self, message: str, status_code: int | None = None) -> None:
        """Initialize the exception.

        Args:
            message: Error message
            status_code: Optional HTTP status code from provider
        """
        super().__init__(message=message)
        self.status_code = status_code or HTTPStatus.BAD_GATEWAY


class RecipeNotFoundError(NotFoundError):
    """Raised when a recipe cannot be found."""


class RecipeProviderTimeout(RecipeProviderError):
    """Raised when a provider request times out."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: Error message
        """
        super().__init__(message=message, status_code=HTTPStatus.GATEWAY_TIMEOUT)


class RecipeProviderAuthError(RecipeProviderError):
    """Raised when there are authentication/authorization issues."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: Error message
        """
        super().__init__(message=message, status_code=HTTPStatus.UNAUTHORIZED)


class RecipeProviderRateLimitError(RecipeProviderError):
    """Raised when rate limits are exceeded."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: Error message
        """
        super().__init__(message=message, status_code=HTTPStatus.TOO_MANY_REQUESTS)


class RecipeProviderValidationError(RecipeProviderError):
    """Raised when provider rejects request due to validation."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: Error message
        """
        super().__init__(message=message, status_code=HTTPStatus.BAD_REQUEST)


class RecipeProviderParseError(RecipeProviderError):
    """Raised when provider response cannot be parsed."""

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message: Error message
        """
        super().__init__(message=message, status_code=HTTPStatus.BAD_GATEWAY)

```

## backend/app/config/api_config.py
```
from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
from pydantic import BaseModel

from backend.app.core.config import ConfigurationError


class APIEndpoint(BaseModel):
    """Configuration for an API endpoint."""

    base_url: str
    timeout: int = 30
    required_keys: set[str]
    optional_keys: set[str] = set()


# Define API endpoints
ENDPOINTS: dict[str, APIEndpoint] = {
    "spoonacular": APIEndpoint(base_url="https://api.spoonacular.com", required_keys={"SPOONACULAR_API_KEY"}),
    "edamam": APIEndpoint(base_url="https://api.edamam.com", required_keys={"EDAMAM_APP_ID", "EDAMAM_APP_KEY"}),
    "api_ninjas": APIEndpoint(base_url="https://api.api-ninjas.com/v1", required_keys={"API_NINJAS_API_KEY"}),
    "tasty": APIEndpoint(base_url="https://tasty.p.rapidapi.com", required_keys={"TASTY_API_KEY"}),
}


class APIConfig(BaseModel):
    """API configuration settings."""

    dev_mode: bool = False
    cache_ttl: int = 3600
    max_concurrent_requests: int = 5

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        load_dotenv()
        self.dev_mode = os.getenv("FLASK_ENV") == "development"
        self.cache_ttl = int(os.getenv("CACHE_TTL", "3600"))
        max_requests: str = os.getenv("MAX_CONCURRENT_REQUESTS", "5")
        self.max_concurrent_requests = int(max_requests)
        self._validate_env_vars()

    def _validate_env_vars(self) -> None:
        """Validate that all required API keys are present in environment.

        Raises:
            ConfigurationError: If any required API keys are missing
        """
        missing_keys: list[str] = []
        for endpoint in ENDPOINTS.values():
            for key in endpoint.required_keys:
                env_key: str = key  # assumes the key in required_keys matches the env var
                if not os.getenv(env_key) and not self.dev_mode:
                    missing_keys.append(env_key)

        if missing_keys:
            missing_str: str = ", ".join(missing_keys)
            msg = f"Missing required API keys: {missing_str}. Please set these environment variables."
            raise ConfigurationError(msg)

    def get_endpoint(self, api_name: str) -> APIEndpoint:
        """Get endpoint configuration for an API."""
        if api_name not in ENDPOINTS:
            msg = f"Unknown API: {api_name}"
            raise ConfigurationError(msg)
        return ENDPOINTS[api_name]

    def get_api_key(self, api_name: str, key_name: str) -> str | None:
        """Get API key from environment."""
        api_key: str | None = os.getenv(key_name)
        if not api_key and not self.dev_mode:
            msg = f"Missing API key for {api_name}. Please set {key_name} environment variable."
            raise ConfigurationError(msg)
        return api_key

    def get_required_keys(self) -> list[str]:
        """Get all required API keys.

        Returns:
            List of required API key names
        """
        missing_keys: list[str] = []
        for endpoint in ENDPOINTS.values():
            for key in endpoint.required_keys:
                env_key: str = key  # assumes the key in required_keys matches the env var
                if env_key not in missing_keys:
                    missing_keys.append(env_key)
        return missing_keys


# Global instance
ENDPOINTS = APIConfig()

```

## backend/app/core/error_codes.py
```
"""Error codes for the application.

This module defines error codes that map to standard HTTP status codes where possible,
with additional specific codes for database, business rules, and integration errors.

Example:
    .. code-block:: python

        from app.core.error_codes import ErrorCode

        if not recipe:
            raise ResourceNotFoundError(
                resource_type="Recipe",
                identifier=recipe_id,
                code=ErrorCode.NOT_FOUND
            )

Note:
    Error codes are organized into ranges to maintain clarity and avoid conflicts:
    - 1-99: Standard HTTP-mapped errors
    - 100-199: Database errors
    - 200-299: Authentication/Authorization
    - 300-399: Business rules
    - 400-499: Integration/External services
    - 500-599: Recipe-specific errors
    - 600-699: Allergen-specific errors
    - 700-799: Validation errors
"""

from __future__ import annotations

from enum import IntEnum


class ErrorCode(IntEnum):
    """Application error codes aligned with HTTP status codes where possible.

    Attributes:
        BAD_REQUEST (int): Invalid request format or parameters (400)
        UNAUTHORIZED (int): Authentication required (401)
        FORBIDDEN (int): Permission denied (403)
        NOT_FOUND (int): Resource not found (404)
        CONFLICT (int): Resource conflict (409)
        UNPROCESSABLE (int): Validation failed (422)
        TOO_MANY_REQUESTS (int): Rate limit exceeded (429)
        INTERNAL_ERROR (int): Server error (500)
        SERVICE_UNAVAILABLE (int): Service unavailable (503)
        UNKNOWN (int): Unknown error (500)
    """

    # Standard HTTP-Mapped Errors (1-99)
    BAD_REQUEST = 1  # 400
    UNAUTHORIZED = 2  # 401
    FORBIDDEN = 3  # 403
    NOT_FOUND = 4  # 404
    CONFLICT = 5  # 409
    UNPROCESSABLE = 6  # 422
    TOO_MANY_REQUESTS = 7  # 429
    INTERNAL_ERROR = 8  # 500
    SERVICE_UNAVAILABLE = 9  # 503
    UNKNOWN = 10  # 500
    ALREADY_EXISTS = 11  # 409
    IN_USE = 12  # 409
    BUSINESS_RULE_VIOLATION = 13  # 400

    # Database Errors (100-199)
    DATABASE_ERROR = 100
    DATABASE_CONNECTION_ERROR = 101
    DATABASE_CONSTRAINT = 102
    DATABASE_DEADLOCK = 103
    DATABASE_TIMEOUT = 104
    DATABASE_STALE_DATA = 105

    # Authentication/Authorization (200-299)
    TOKEN_EXPIRED = 200
    TOKEN_INVALID = 201
    TOKEN_MISSING = 202
    INSUFFICIENT_PERMISSIONS = 203
    SESSION_EXPIRED = 204

    # Business Rules (300-399)
    VALIDATION_ERROR = 300
    INVALID_STATE = 301
    RESOURCE_LOCKED = 302
    RESOURCE_IN_USE = 303
    ALLERGEN_CONFLICT = 304
    RECIPE_IN_MEALPLAN = 305
    DUPLICATE_ENTRY = 306
    INVALID_OPERATION = 307

    # Integration/External (400-499)
    EXTERNAL_SERVICE_ERROR = 400
    EXTERNAL_SERVICE_TIMEOUT = 401
    EXTERNAL_SERVICE_UNAVAILABLE = 402
    API_ERROR = 403
    API_TIMEOUT = 404
    API_RATE_LIMIT = 405
    API_RESPONSE_INVALID = 406

    # Recipe-specific errors (500-599)
    RECIPE_EXISTS = 500
    RECIPE_NOT_FOUND = 501
    RECIPE_IN_USE = 502
    RECIPE_INVALID = 503
    RECIPE_ALLERGEN_CONFLICT = 504

    # Allergen-specific errors (600-699)
    ALLERGEN_EXISTS = 600
    ALLERGEN_NOT_FOUND = 601
    ALLERGEN_IN_USE = 602
    ALLERGEN_INVALID = 603

    # Validation errors (700-799)
    VALIDATION = 700
    VALIDATION_MISSING_FIELD = 701
    VALIDATION_INVALID_TYPE = 702
    VALIDATION_CONSTRAINT = 703

    @property
    def http_status_code(self) -> int:
        """Map error code to HTTP status code.

        Returns:
            int: Corresponding HTTP status code
        """
        if self == self.BAD_REQUEST:
            return 400
        elif self == self.UNAUTHORIZED:
            return 401
        elif self == self.FORBIDDEN:
            return 403
        elif self == self.NOT_FOUND:
            return 404
        elif self == self.CONFLICT:
            return 409
        elif self == self.UNPROCESSABLE:
            return 422
        elif self == self.TOO_MANY_REQUESTS:
            return 429
        elif self == self.SERVICE_UNAVAILABLE:
            return 503
        elif self in (self.TOKEN_EXPIRED, self.TOKEN_INVALID) or self == self.TOKEN_MISSING:
            return 401
        elif self == self.INSUFFICIENT_PERMISSIONS:
            return 403
        elif self == self.SESSION_EXPIRED:
            return 401
        elif self == self.API_RATE_LIMIT:
            return 429
        elif self == self.EXTERNAL_SERVICE_UNAVAILABLE:
            return 503
        # Default to 500 for unknown/internal errors
        return 500

    @property
    def is_retryable(self) -> bool:
        """Indicate if operation can be retried.

        Returns:
            bool: True if the error is transient and the operation can be retried
        """
        return self in {
            self.DATABASE_DEADLOCK,
            self.DATABASE_TIMEOUT,
            self.DATABASE_CONNECTION_ERROR,
            self.EXTERNAL_SERVICE_TIMEOUT,
            self.EXTERNAL_SERVICE_UNAVAILABLE,
            self.API_TIMEOUT,
            self.API_RATE_LIMIT,
            self.SERVICE_UNAVAILABLE,
        }

    @property
    def is_client_error(self) -> bool:
        """Indicate if error was caused by client.

        Returns:
            bool: True if the error was caused by client input or request
        """
        return self.http_status_code < 500

    @property
    def should_log_error(self) -> bool:
        """Indicate if error should be logged at ERROR level.

        Returns:
            bool: True if the error should be logged at ERROR level
        """
        return not self.is_client_error or self in {
            self.DATABASE_ERROR,
            self.DATABASE_CONSTRAINT,
            self.DATABASE_DEADLOCK,
            self.EXTERNAL_SERVICE_ERROR,
            self.API_ERROR,
        }


__version__ = "1.0.0"

__all__ = ["ErrorCode"]

```

## backend/app/core/error_handlers.py
```
"""FastAPI error handlers.

This module provides FastAPI exception handlers for converting domain errors
into HTTP responses. It includes handlers for all error types and provides
proper error logging.

Example:
    .. code-block:: python

        from fastapi import FastAPI
        from app.core.error_handlers import setup_error_handlers

        app = FastAPI()
        setup_error_handlers(app)

Note:
    The error handlers in this module are registered as FastAPI exception handlers
    and are not meant to be called directly. They are used by FastAPI's middleware
    to handle exceptions that occur during request processing.

Attributes:
    logger: Logger instance for error handling
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError as PydanticValidationError
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import BusinessError, DatabaseError, DomainError, ValidationError, get_status_code

if TYPE_CHECKING:
    from fastapi import FastAPI, Request

logger = logging.getLogger(__name__)


def setup_error_handlers(app: FastAPI) -> None:
    """Set up FastAPI error handlers.

    This function registers exception handlers for various error types
    and ensures proper error responses are returned.

    Args:
        app: FastAPI application instance

    Note:
        The handlers are registered using FastAPI's exception_handler decorator
        and are called automatically when exceptions occur during request processing.
    """

    @app.exception_handler(DomainError)  # type: ignore
    async def domain_error_handler(request: Request, error: DomainError) -> JSONResponse:  # type: ignore
        """Convert domain errors to HTTP responses.

        Args:
            request: FastAPI request
            error: Domain error instance

        Returns:
            JSON response with error details
        """
        # Log error with appropriate severity
        log_error(error, request)

        response_data = error.to_dict()

        # Add debug info in development environment
        if settings.FASTAPI_ENV == "development":
            if error.context.debug_info:
                response_data["debug"] = error.context.debug_info
            if error.context.original_error:
                response_data["debug"]["original_error"] = {
                    "type": error.context.original_error.__class__.__name__,
                    "message": str(error.context.original_error),
                }

        return JSONResponse(status_code=get_status_code(error), content=response_data)

    @app.exception_handler(RequestValidationError)  # type: ignore
    async def validation_error_handler(request: Request, error: RequestValidationError) -> JSONResponse:  # type: ignore
        """Handle FastAPI request validation errors.

        Args:
            request: FastAPI request
            error: Validation error

        Returns:
            JSON response with validation error details
        """
        logger.warning(f"Request validation failed: {error.errors()}")

        return JSONResponse(
            status_code=422,
            content={
                "code": ErrorCode.VALIDATION,
                "message": ErrorMessages.INVALID_DATA.get_message(
                    resource="request", details={"errors": error.errors()}
                ),
                "details": {"errors": error.errors()},
            },
        )

    @app.exception_handler(PydanticValidationError)  # type: ignore
    async def pydantic_validation_handler(request: Request, error: PydanticValidationError) -> JSONResponse:  # type: ignore
        """Handle Pydantic validation errors.

        Args:
            request: FastAPI request
            error: Validation error

        Returns:
            JSON response with validation error details
        """
        logger.warning(f"Pydantic validation failed: {error.errors()}")

        return JSONResponse(
            status_code=422,
            content={
                "code": ErrorCode.VALIDATION,
                "message": ErrorMessages.INVALID_DATA.get_message(resource="data", details={"errors": error.errors()}),
                "details": {"errors": error.errors()},
            },
        )

    @app.exception_handler(SQLAlchemyError)  # type: ignore
    async def db_error_handler(request: Request, error: SQLAlchemyError) -> JSONResponse:  # type: ignore
        """Handle unexpected SQLAlchemy errors.

        Args:
            request: FastAPI request
            error: SQLAlchemy error

        Returns:
            JSON response with database error details
        """
        db_error = DatabaseError.from_sqlalchemy(error=error)
        return await domain_error_handler(request, db_error)

    @app.exception_handler(Exception)  # type: ignore
    async def fallback_error_handler(request: Request, error: Exception) -> JSONResponse:  # type: ignore
        """Handle any unhandled exceptions.

        Args:
            request: FastAPI request
            error: Unhandled exception

        Returns:
            JSON response with error details
        """
        logger.exception("Unhandled exception occurred", exc_info=error)

        return JSONResponse(
            status_code=500,
            content={
                "code": ErrorCode.UNKNOWN,
                "message": ErrorMessages.UNKNOWN_ERROR.get_message(),
                "details": {"error": str(error)} if settings.FASTAPI_ENV == "development" else {},
            },
        )


def log_error(error: DomainError, request: Request) -> None:
    """Log error with appropriate severity level.

    Args:
        error: Domain error instance
        request: FastAPI request
    """
    # Determine log level based on error type and status code
    log_level = get_log_level(error)

    # Build log message
    log_msg = build_log_message(error, request)

    # Log with determined severity
    logger.log(log_level, log_msg, extra={"error_context": error.context})


def get_log_level(error: DomainError) -> int:
    """Determine appropriate log level for error.

    Args:
        error: Domain error instance

    Returns:
        Logging level to use
    """
    if isinstance(error, ValidationError | BusinessError):
        return logging.WARNING
    if get_status_code(error) >= 500:
        return logging.ERROR
    return logging.INFO


def build_log_message(error: DomainError, request: Request) -> str:
    """Build detailed log message for error.

    Args:
        error: Domain error instance
        request: FastAPI request

    Returns:
        Formatted log message
    """
    return (
        f"Error occurred processing {request.method} {request.url.path}\n"
        f"Error Type: {error.__class__.__name__}\n"
        f"Error Code: {error.context.code}\n"
        f"Message: {error.context.message}\n"
        f"Details: {error.context.details}"
    )


__version__ = "1.0.0"

__all__ = ["setup_error_handlers"]

```

## backend/app/core/exceptions.py
```
"""Core exception handling for the application.

This module provides a comprehensive exception hierarchy for handling all types
of errors in the application. It includes base classes for different error
categories and utility functions for error handling.

Example:
    .. code-block:: python

        from app.core.exceptions import BusinessError
        from app.core.error_messages import ErrorMessages
        from app.core.error_codes import ErrorCode

        try:
            # Some business logic
            if invalid_state:
                raise BusinessError(
                    message_template=ErrorMessages.INVALID_STATE,
                    code=ErrorCode.INVALID_STATE,
                    details={"current": state, "allowed": valid_states}
                )
        except BusinessError as err:
            # Handle business rule violation
            logger.error(f"Business rule violated: {err.context.message}")

Note:
    All exceptions in this module inherit from DomainError, which provides
    a consistent interface for error handling and logging.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from fastapi import status

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessageTemplate, Language


@dataclass
class ErrorContext:
    """Structured context for errors.

    This class provides a standardized way to capture error context including
    the error code, message, and additional details for debugging.

    Attributes:
        code: Error code identifying the type of error
        message: Human-readable error message
        details: Additional context about the error
        original_error: Original exception that caused this error
        debug_info: Additional debugging information
    """

    code: ErrorCode
    message: str
    details: dict[str, Any]
    original_error: Exception | None = None
    debug_info: dict[str, Any] | None = None


class DomainError(Exception):
    """Base exception for all domain errors.

    This is the root of our exception hierarchy. All other exceptions
    should inherit from this class.

    Attributes:
        context: Error context containing code, message, and details
        status_code: HTTP status code to use when converting to response
    """

    status_code: ClassVar[int] = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(
        self,
        message_template: ErrorMessageTemplate,
        code: ErrorCode,
        details: dict[str, Any] | None = None,
        original_error: Exception | None = None,
        debug_info: dict[str, Any] | None = None,
        lang: Language = Language.EN,
        **kwargs: Any,
    ) -> None:
        """Initialize domain error.

        Args:
            message_template: Template for error message
            code: Error code
            details: Additional error details
            original_error: Original exception
            debug_info: Debug information
            lang: Message language
            **kwargs: Additional format parameters for message
        """
        self.context = ErrorContext(
            code=code,
            message=message_template.get_message(lang, **kwargs),
            details=details or {},
            original_error=original_error,
            debug_info=debug_info,
        )
        super().__init__(self.context.message)

    def to_dict(self) -> dict[str, Any]:
        """Convert error to dict for response.

        Returns:
            Dictionary representation of error
        """
        return {
            "code": self.context.code,
            "message": self.context.message,
            "details": self.context.details,
            "error_type": self.__class__.__name__,
        }


class ConfigurationError(DomainError):
    """Configuration-related errors.

    Raised when there are issues with application configuration.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


class AuthenticationError(DomainError):
    """Authentication-related errors.

    Raised when there are issues with user authentication.
    """

    status_code = status.HTTP_401_UNAUTHORIZED


class AuthorizationError(DomainError):
    """Authorization-related errors.

    Raised when user lacks permission for an operation.
    """

    status_code = status.HTTP_403_FORBIDDEN


class ResourceError(DomainError):
    """Base for resource-related errors.

    Provides common functionality for handling resource errors.
    """

    def __init__(
        self,
        resource_type: str,
        identifier: Any,
        message_template: ErrorMessageTemplate,
        code: ErrorCode,
        **kwargs: Any,
    ) -> None:
        """Initialize resource error.

        Args:
            resource_type: Type of resource (e.g., "Recipe", "Allergen")
            identifier: Resource identifier
            message_template: Template for error message
            code: Error code
            **kwargs: Additional parameters
        """
        details = {"resource_type": resource_type, "identifier": identifier, **kwargs.get("details", {})}
        super().__init__(message_template=message_template, code=code, details=details, **kwargs)


class ResourceNotFoundError(ResourceError):
    """Resource does not exist."""

    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, resource_type: str, identifier: Any, **kwargs: Any) -> None:
        """Initialize not found error.

        Args:
            resource_type: Type of resource
            identifier: Resource identifier
            **kwargs: Additional parameters
        """
        from app.core.error_messages import ErrorMessages

        super().__init__(
            resource_type=resource_type,
            identifier=identifier,
            message_template=ErrorMessages.RESOURCE_NOT_FOUND,
            code=ErrorCode.NOT_FOUND,
            **kwargs,
        )


class ResourceExistsError(ResourceError):
    """Resource already exists."""

    status_code = status.HTTP_409_CONFLICT

    def __init__(self, resource_type: str, identifier: Any, **kwargs: Any) -> None:
        """Initialize exists error.

        Args:
            resource_type: Type of resource
            identifier: Resource identifier
            **kwargs: Additional parameters
        """
        from app.core.error_messages import ErrorMessages

        super().__init__(
            resource_type=resource_type,
            identifier=identifier,
            message_template=ErrorMessages.RESOURCE_EXISTS,
            code=ErrorCode.ALREADY_EXISTS,
            **kwargs,
        )


class ResourceInUseError(ResourceError):
    """Resource is in use and cannot be modified/deleted."""

    status_code = status.HTTP_409_CONFLICT

    def __init__(self, resource_type: str, identifier: Any, **kwargs: Any) -> None:
        """Initialize in use error.

        Args:
            resource_type: Type of resource
            identifier: Resource identifier
            **kwargs: Additional parameters
        """
        from app.core.error_messages import ErrorMessages

        super().__init__(
            resource_type=resource_type,
            identifier=identifier,
            message_template=ErrorMessages.RESOURCE_IN_USE,
            code=ErrorCode.IN_USE,
            **kwargs,
        )


class DatabaseError(DomainError):
    """Database operation failed."""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    @classmethod
    def from_sqlalchemy(cls, error: Exception, operation: str | None = None, **kwargs: Any) -> DatabaseError:
        """Create from SQLAlchemy error.

        Args:
            error: Original SQLAlchemy error
            operation: Database operation that failed
            **kwargs: Additional parameters

        Returns:
            DatabaseError instance
        """
        from app.core.error_messages import ErrorMessages

        details = {"operation": operation, "error_type": error.__class__.__name__, **kwargs.get("details", {})}

        # Add debug info in development
        debug_info = {"sql": getattr(error, "statement", None), "params": getattr(error, "params", None)}

        return cls(
            message_template=ErrorMessages.DATABASE_ERROR,
            code=ErrorCode.DATABASE_ERROR,
            details=details,
            original_error=error,
            debug_info=debug_info,
            **kwargs,
        )


class ValidationError(DomainError):
    """Validation error."""

    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY


class BusinessError(DomainError):
    """Business rule violation."""

    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(
        self, message_template: ErrorMessageTemplate, code: ErrorCode = ErrorCode.BUSINESS_RULE_VIOLATION, **kwargs: Any
    ) -> None:
        """Initialize business error.

        Args:
            message_template: Template for error message
            code: Error code
            **kwargs: Additional parameters
        """
        super().__init__(message_template=message_template, code=code, **kwargs)


class ExternalServiceError(DomainError):
    """External service error."""

    status_code = status.HTTP_502_BAD_GATEWAY


class ServiceUnavailableError(ExternalServiceError):
    """Service is unavailable."""

    status_code = status.HTTP_503_SERVICE_UNAVAILABLE


class ServiceTimeoutError(ExternalServiceError):
    """Service request timed out."""

    status_code = status.HTTP_504_GATEWAY_TIMEOUT


class RateLimitError(ExternalServiceError):
    """Rate limit exceeded."""

    status_code = status.HTTP_429_TOO_MANY_REQUESTS


def get_status_code(error: DomainError) -> int:
    """Map error codes to HTTP status codes.

    Args:
        error: Domain error instance

    Returns:
        HTTP status code
    """
    return error.status_code


__version__ = "1.0.0"

__all__ = [
    "AuthenticationError",
    "AuthorizationError",
    "BusinessError",
    "ConfigurationError",
    "DatabaseError",
    "DomainError",
    "ErrorContext",
    "ExternalServiceError",
    "RateLimitError",
    "ResourceError",
    "ResourceExistsError",
    "ResourceInUseError",
    "ResourceNotFoundError",
    "ServiceTimeoutError",
    "ServiceUnavailableError",
    "ValidationError",
    "get_status_code",
]

```

## backend/app/core/__init__.py
```
"""Core application components.

This package contains core application components like configuration,
error handling, and shared utilities.

Example:
    .. code-block:: python

        from app.core import Settings, ErrorCode, ConfigurationError
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, Final, TypeVar

from pydantic import BaseModel as PydanticBaseModel, Field as PydanticField, validator as PydanticValidator
from pydantic_settings import BaseSettings as PydanticBaseSettings, SettingsConfigDict as PydanticSettingsConfigDict

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages, ErrorMessageTemplate
from app.core.exceptions import ConfigurationError

# Type aliases for better IDE support and consistency
PydanticModel = PydanticBaseModel
PydanticField = PydanticField
PydanticValidator = PydanticValidator
PydanticSettings = PydanticBaseSettings
PydanticSettingsConfig = PydanticSettingsConfigDict

# Reusable type variables
T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

# Public API
__all__: Final[list[str]] = [
    # Core types
    "T",
    "T_co",
    "T_contra",
    "Callable",
    "Any",
    # Pydantic aliases
    "PydanticModel",
    "PydanticField",
    "PydanticValidator",
    "PydanticSettings",
    "PydanticSettingsConfig",
    # Error handling
    "ConfigurationError",
    "ErrorCode",
    "ErrorMessages",
    "ErrorMessageTemplate",
]

# Version
__version__: Final[str] = "1.0.0"

```

## backend/app/core/constants.py
```
"""Application constants."""

from __future__ import annotations


class ErrorMessages:
    """Error message constants."""

    # Generic Errors
    UNKNOWN_ERROR = "An unknown error occurred"
    INTERNAL_ERROR = "Internal server error: {details}"

    # External Service Errors
    EXTERNAL_SERVICE_ERROR = "{service} API error: {details}"
    EXTERNAL_SERVICE_TIMEOUT = "Request to {service} timed out"
    EXTERNAL_SERVICE_UNAVAILABLE = "{service} is currently unavailable"
    RATE_LIMIT_EXCEEDED = "Rate limit exceeded for {service}"
    API_REQUEST_FAILED = "API request failed: {details}"
    HTTP_ERROR = "HTTP error: {details}"

    # Recipe Errors
    RECIPE_NOT_FOUND = "Recipe not found: {recipe_id}"
    RECIPE_SEARCH_FAILED = "Failed to search recipes: {details}"
    RECIPE_FETCH_FAILED = "Failed to get recipe: {details}"
    RECIPE_CONTAINS_ALLERGENS = "Recipe contains allergens"
    RECIPE_PROVIDER_INIT_FAILED = "Failed to initialize {provider} provider: {details}"
    RECIPE_ALREADY_EXISTS = "Recipe with this title already exists"
    RECIPE_IN_USE = "Cannot delete recipe that is referenced by meal plans"

    # Resource Not Found Errors
    ALLERGEN_NOT_FOUND = "Allergen not found"
    MEAL_TYPE_NOT_FOUND = "Meal type not found"
    INGREDIENT_NOT_FOUND = "Ingredient not found"
    CUISINE_TYPE_NOT_FOUND = "Cuisine type not found"
    DIETARY_RESTRICTION_NOT_FOUND = "Dietary restriction not found"
    FAMILY_MEMBER_NOT_FOUND = "Family member not found"
    PROTEIN_TYPE_NOT_FOUND = "Protein type not found"
    COOK_METHOD_NOT_FOUND = "Cook method not found"
    MEAL_PLAN_NOT_FOUND = "Meal plan not found"

    # Resource Already Exists Errors
    ALLERGEN_EXISTS = "Allergen with this name already exists"
    MEAL_TYPE_EXISTS = "Meal type with this name already exists"
    INGREDIENT_EXISTS = "Ingredient with this name already exists"
    CUISINE_TYPE_EXISTS = "Cuisine type with this name already exists"
    DIETARY_RESTRICTION_EXISTS = "Dietary restriction with this name already exists"
    FAMILY_MEMBER_EXISTS = "Family member with this name already exists"
    PROTEIN_TYPE_EXISTS = "Protein type with this name already exists"
    COOK_METHOD_EXISTS = "Cook method with this name already exists"
    MEAL_PLAN_EXISTS = "Meal plan with this name already exists"

    # Resource In Use Errors
    ALLERGEN_IN_USE = "Cannot delete allergen that is referenced by other records"
    MEAL_TYPE_IN_USE = "Cannot delete meal type that is referenced by recipes"
    INGREDIENT_IN_USE = "Cannot delete ingredient that is referenced by recipes"
    CUISINE_TYPE_IN_USE = "Cannot delete cuisine type that is referenced by recipes"
    DIETARY_RESTRICTION_IN_USE = "Cannot delete dietary restriction that is referenced by family members"
    FAMILY_MEMBER_IN_USE = "Cannot delete family member that has associated data"
    PROTEIN_TYPE_IN_USE = "Cannot delete protein type that is referenced by other records"
    COOK_METHOD_IN_USE = "Cannot delete cook method that is referenced by recipes"
    MEAL_PLAN_IN_USE = "Cannot delete meal plan that is referenced by other records"

    # Validation Errors
    INVALID_SEARCH_PARAMS = "Invalid search parameters"
    INVALID_RECIPE_ID = "Invalid recipe ID format"
    INVALID_DATA = "Invalid {resource} data"

    # Database Errors
    DATABASE_ERROR = "Database error: {details}"
    DATABASE_CONNECTION_ERROR = "Failed to connect to database: {details}"
    DATABASE_QUERY_ERROR = "Failed to execute query: {details}"

    # Authentication Errors
    UNAUTHORIZED = "Unauthorized access"
    FORBIDDEN = "Access forbidden"
    INVALID_CREDENTIALS = "Invalid credentials"
    TOKEN_EXPIRED = "Token has expired"
    INVALID_TOKEN = "Invalid token"

    # Configuration Errors
    CONFIG_ERROR = "Configuration error: {details}"
    CONFIG_MISSING_KEY = "Missing required configuration key: {key}"
    CONFIG_INVALID_VALUE = "Invalid configuration value for {key}: {details}"

```

## backend/app/core/config.py
```
"""Application configuration.

This module provides a single source of truth for all application configuration,
combining settings from YAML files and environment variables.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseSettings, Field, validator
from pydantic_settings import SettingsConfigDict

from app.core.error_codes import ErrorCode
from app.core.error_messages import ErrorMessages
from app.core.exceptions import ConfigurationError


class Settings(BaseSettings):
    """Application settings combining YAML config and environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=True)

    # Environment
    ENVIRONMENT: str = Field("development", description="Application environment")

    # Core settings loaded from YAML
    _config: dict[str, Any] = {}

    # Required environment variables (secrets, etc.)
    POSTGRES_PASSWORD: str = Field(..., description="PostgreSQL password")
    SECRET_KEY: str = Field(..., description="Secret key for JWT")
    SPOONACULAR_API_KEY: str = Field(..., description="Spoonacular API key")

    @validator("ENVIRONMENT")
    def validate_environment(self, v: str) -> str:
        """Validate environment name and load corresponding config."""
        if v not in {"development", "production", "test"}:
            raise ConfigurationError(
                message_template=ErrorMessages.CONFIG_INVALID_VALUE,
                code=ErrorCode.VALIDATION_ERROR,
                details={"environment": v},
            )
        return v

    def __init__(self, **kwargs: Any) -> None:
        """Initialize settings and load YAML config."""
        super().__init__(**kwargs)
        self._load_yaml_config()

    def _load_yaml_config(self) -> None:
        """Load configuration from YAML files."""
        try:
            config_dir = Path(__file__).parent.parent.parent / "config"

            # Load default config
            with (config_dir / "default.yaml").open() as f:
                self._config = yaml.safe_load(f)

            # Load environment overrides
            env_config = config_dir / f"{self.ENVIRONMENT}.yaml"
            if env_config.exists():
                with env_config.open() as f:
                    self._config.update(yaml.safe_load(f))

        except Exception as e:
            raise ConfigurationError(
                message_template=ErrorMessages.CONFIG_LOAD_FAILED,
                code=ErrorCode.CONFIGURATION_ERROR,
                details={"error": str(e)},
            )

    @property
    def allergens(self) -> list[dict[str, Any]]:
        """Get allergen configuration."""
        return self._config.get("allergens", [])

    @property
    def database_url(self) -> str:
        """Get database URL with credentials."""
        db_config = self._config.get("database", {})
        return (
            f"postgresql+asyncpg://{db_config.get('user')}:{self.POSTGRES_PASSWORD}"
            f"@{db_config.get('host')}/{db_config.get('name')}"
        )

    @property
    def api_config(self) -> dict[str, Any]:
        """Get API configuration."""
        return self._config.get("api", {})


@lru_cache
def get_settings() -> Settings:
    """Get application settings singleton.

    Returns:
        Settings: Application settings instance
    """
    return Settings()


settings = get_settings()

```

## backend/app/core/exceptions.test.py
```
from __future__ import annotations

import unittest
from http import HTTPStatus
from typing import Never

import pytest
from fastapi import status

from app.core.exceptions import (
    AppErrorDetail,
    AppHTTPException,
    ErrorCode,
    ExternalServiceTimeoutError,
    NotFoundError,
    ValidationError,
)


class TestExceptions(unittest.TestCase):
    def test_app_error_detail(self) -> None:
        detail = AppErrorDetail(ErrorCode.UNKNOWN_ERROR, "Test error", HTTPStatus.BAD_REQUEST, {"key": "value"})
        assert detail.code == ErrorCode.UNKNOWN_ERROR
        assert detail.message == "Test error"
        assert detail.status_code == HTTPStatus.BAD_REQUEST
        assert detail.details == {"key": "value"}
        assert detail.to_dict()["code"] == ErrorCode.UNKNOWN_ERROR

    def test_app_http_exception(self) -> Never:
        with pytest.raises(AppHTTPException) as context:
            msg = "Test message"
            raise AppHTTPException(
                msg, status.HTTP_400_BAD_REQUEST, {"X-Custom": "value"}, {"detail_key": "detail_value"}
            )
        assert context.exception.status_code == status.HTTP_400_BAD_REQUEST
        assert context.exception.detail == {"message": "Test message", "details": {"detail_key": "detail_value"}}
        assert context.exception.headers == {"X-Custom": "value"}

    def test_validation_error(self) -> Never:
        with pytest.raises(ValidationError) as context:
            msg = "Validation failed"
            raise ValidationError(msg, {"field": "invalid"})
        assert context.exception.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert context.exception.detail == {"message": "Validation failed", "details": {"field": "invalid"}}

    def test_not_found_error(self) -> Never:
        with pytest.raises(NotFoundError) as context:
            msg = "Resource not found"
            raise NotFoundError(msg, {"id": 123})
        assert context.exception.status_code == status.HTTP_404_NOT_FOUND
        assert context.exception.detail == {"message": "Resource not found", "details": {"id": 123}}

    def test_external_service_timeout_error(self) -> Never:
        with pytest.raises(ExternalServiceTimeoutError) as context:
            msg = "Timeout"
            raise ExternalServiceTimeoutError(msg, {"service": "test"})
        assert context.exception.status_code == status.HTTP_504_GATEWAY_TIMEOUT
        assert context.exception.detail == {"message": "Timeout", "details": {"service": "test"}}

```

## backend/app/core/error_messages.py
```
"""Error message templates with i18n support.

This module provides a centralized location for all error message templates
with support for internationalization (i18n). Messages are organized by
domain and support multiple languages.

Example:
    .. code-block:: python

        from app.core.error_messages import ErrorMessages, Language

        msg = ErrorMessages.RESOURCE_NOT_FOUND.get_message(
            lang=Language.EN,
            resource_type="Recipe",
            identifier="123"
        )
"""

from __future__ import annotations

import gettext
from dataclasses import dataclass
from enum import Enum
from typing import Any


class Language(str, Enum):
    """Supported languages for error messages."""

    EN = "en"  # English
    ES = "es"  # Spanish


@dataclass
class ErrorMessageTemplate:
    """Template for error messages with translations.

    Attributes:
        key: Unique identifier for the message template
        en: English version of the message
        es: Spanish version of the message (optional)
    """

    key: str
    en: str
    es: str = ""

    def get_message(self, lang: Language = Language.EN, **kwargs: Any) -> str:
        """Get message in specified language with formatting.

        Args:
            lang: Target language for the message
            **kwargs: Format parameters for the message template

        Returns:
            Formatted message in the specified language
        """
        template = getattr(self, lang.value, self.en)
        return template.format(**kwargs)


class ErrorMessages:
    """Centralized error message templates.

    This class organizes error messages by domain and provides templates
    for all possible error scenarios in the application.
    """

    # Generic System Errors (1-999)
    UNKNOWN_ERROR = ErrorMessageTemplate(
        key="unknown_error", en="An unexpected error occurred", es="Se produjo un error inesperado"
    )
    INTERNAL_ERROR = ErrorMessageTemplate(
        key="internal_error", en="Internal server error: {details}", es="Error interno del servidor: {details}"
    )
    CONFIG_ERROR = ErrorMessageTemplate(
        key="config_error", en="Configuration error: {details}", es="Error de configuración: {details}"
    )
    CONFIG_MISSING_KEY = ErrorMessageTemplate(
        key="config_missing_key",
        en="Missing required configuration key: {key}",
        es="Falta la clave de configuración requerida: {key}",
    )
    CONFIG_INVALID_VALUE = ErrorMessageTemplate(
        key="config_invalid_value",
        en="Invalid configuration value for {key}: {details}",
        es="Valor de configuración inválido para {key}: {details}",
    )

    # Authentication/Authorization Errors (1000-1999)
    UNAUTHORIZED = ErrorMessageTemplate(key="unauthorized", en="Unauthorized access", es="Acceso no autorizado")
    FORBIDDEN = ErrorMessageTemplate(key="forbidden", en="Access forbidden", es="Acceso prohibido")
    INVALID_CREDENTIALS = ErrorMessageTemplate(
        key="invalid_credentials", en="Invalid credentials", es="Credenciales inválidas"
    )
    TOKEN_EXPIRED = ErrorMessageTemplate(key="token_expired", en="Token has expired", es="El token ha expirado")
    INVALID_TOKEN = ErrorMessageTemplate(key="invalid_token", en="Invalid token", es="Token inválido")

    # Resource Errors (2000-2999)
    RESOURCE_NOT_FOUND = ErrorMessageTemplate(
        key="resource_not_found",
        en="{resource_type} not found: {identifier}",
        es="{resource_type} no encontrado: {identifier}",
    )
    RESOURCE_EXISTS = ErrorMessageTemplate(
        key="resource_exists",
        en="{resource_type} already exists: {identifier}",
        es="{resource_type} ya existe: {identifier}",
    )
    RESOURCE_IN_USE = ErrorMessageTemplate(
        key="resource_in_use",
        en="{resource_type} is in use and cannot be modified: {identifier}",
        es="{resource_type} está en uso y no se puede modificar: {identifier}",
    )

    # Database Errors (3000-3999)
    DATABASE_ERROR = ErrorMessageTemplate(
        key="database_error",
        en="Database operation failed: {details}",
        es="Error en la operación de base de datos: {details}",
    )
    DATABASE_CONNECTION_ERROR = ErrorMessageTemplate(
        key="database_connection_error",
        en="Failed to connect to database: {details}",
        es="Error al conectar con la base de datos: {details}",
    )
    DATABASE_QUERY_ERROR = ErrorMessageTemplate(
        key="database_query_error",
        en="Failed to execute query: {details}",
        es="Error al ejecutar la consulta: {details}",
    )

    # External Service Errors (4000-4999)
    EXTERNAL_SERVICE_ERROR = ErrorMessageTemplate(
        key="external_service_error", en="{service} API error: {details}", es="Error en la API de {service}: {details}"
    )
    EXTERNAL_SERVICE_TIMEOUT = ErrorMessageTemplate(
        key="external_service_timeout",
        en="Request to {service} timed out",
        es="Tiempo de espera agotado para {service}",
    )
    EXTERNAL_SERVICE_UNAVAILABLE = ErrorMessageTemplate(
        key="external_service_unavailable",
        en="{service} is currently unavailable",
        es="{service} no está disponible actualmente",
    )
    RATE_LIMIT_EXCEEDED = ErrorMessageTemplate(
        key="rate_limit_exceeded",
        en="Rate limit exceeded for {service}",
        es="Límite de velocidad excedido para {service}",
    )

    # Recipe Domain Errors (5000-5999)
    RECIPE_NOT_FOUND = ErrorMessageTemplate(
        key="recipe_not_found", en="Recipe not found: {identifier}", es="Receta no encontrada: {identifier}"
    )
    RECIPE_EXISTS = ErrorMessageTemplate(
        key="recipe_exists",
        en="Recipe with title '{title}' already exists",
        es="Ya existe una receta con el título '{title}'",
    )
    RECIPE_IN_USE = ErrorMessageTemplate(
        key="recipe_in_use",
        en="Cannot delete recipe that is referenced by meal plans",
        es="No se puede eliminar la receta porque está siendo utilizada en planes de comida",
    )
    RECIPE_CONTAINS_ALLERGENS = ErrorMessageTemplate(
        key="recipe_contains_allergens",
        en="Recipe contains allergens: {allergens}",
        es="La receta contiene alérgenos: {allergens}",
    )
    RECIPE_SEARCH_FAILED = ErrorMessageTemplate(
        key="recipe_search_failed", en="Failed to search recipes: {details}", es="Error al buscar recetas: {details}"
    )
    RECIPE_FETCH_FAILED = ErrorMessageTemplate(
        key="recipe_fetch_failed", en="Failed to get recipe: {details}", es="Error al obtener la receta: {details}"
    )
    RECIPE_PROVIDER_INIT_FAILED = ErrorMessageTemplate(
        key="recipe_provider_init_failed",
        en="Failed to initialize {provider} provider: {details}",
        es="Error al inicializar el proveedor {provider}: {details}",
    )

    # Validation Errors (6000-6999)
    INVALID_SEARCH_PARAMS = ErrorMessageTemplate(
        key="invalid_search_params",
        en="Invalid search parameters: {details}",
        es="Parámetros de búsqueda inválidos: {details}",
    )
    INVALID_RECIPE_ID = ErrorMessageTemplate(
        key="invalid_recipe_id",
        en="Invalid recipe ID format: {details}",
        es="Formato de ID de receta inválido: {details}",
    )
    INVALID_DATA = ErrorMessageTemplate(
        key="invalid_data", en="Invalid {resource} data: {details}", es="Datos inválidos para {resource}: {details}"
    )
    INVALID_FILTER_PARAMS = ErrorMessageTemplate(
        key="invalid_filter_params",
        en="Invalid filter parameters: {details}",
        es="Parámetros de filtro inválidos: {details}",
    )
    OPERATION_NOT_SUPPORTED = ErrorMessageTemplate(
        key="operation_not_supported",
        en="Operation '{operation}' is not supported by {provider}: {reason}",
        es="La operación '{operation}' no está soportada por {provider}: {reason}",
    )
    INVALID_OPERATION = ErrorMessageTemplate(
        key="invalid_operation", en="Invalid operation: {details}", es="Operación inválida: {details}"
    )

    # Business Rule Errors (7000-7999)
    BUSINESS_RULE_VIOLATION = ErrorMessageTemplate(
        key="business_rule_violation",
        en="Business rule violation: {details}",
        es="Violación de regla de negocio: {details}",
    )
    INVALID_STATE = ErrorMessageTemplate(
        key="invalid_state", en="Invalid state: {details}", es="Estado inválido: {details}"
    )

    # Entity-Specific Errors (8000-8999)
    ALLERGEN_NOT_FOUND = ErrorMessageTemplate(
        key="allergen_not_found", en="Allergen not found: {identifier}", es="Alérgeno no encontrado: {identifier}"
    )
    ALLERGEN_EXISTS = ErrorMessageTemplate(
        key="allergen_exists",
        en="Allergen with name '{name}' already exists",
        es="Ya existe un alérgeno con el nombre '{name}'",
    )
    ALLERGEN_IN_USE = ErrorMessageTemplate(
        key="allergen_in_use",
        en="Cannot delete allergen '{name}' as it is referenced by recipes",
        es="No se puede eliminar el alérgeno '{name}' porque está siendo utilizado por recetas",
    )
    MEAL_TYPE_NOT_FOUND = ErrorMessageTemplate(
        key="meal_type_not_found",
        en="Meal type not found: {identifier}",
        es="Tipo de comida no encontrado: {identifier}",
    )
    MEAL_TYPE_EXISTS = ErrorMessageTemplate(
        key="meal_type_exists",
        en="Meal type with name '{name}' already exists",
        es="Ya existe un tipo de comida con el nombre '{name}'",
    )
    MEAL_TYPE_IN_USE = ErrorMessageTemplate(
        key="meal_type_in_use",
        en="Cannot delete meal type that is referenced by recipes",
        es="No se puede eliminar el tipo de comida porque está siendo utilizado por recetas",
    )

    @classmethod
    def setup_translations(cls, locale_dir: str) -> None:
        """Set up translations for the application.

        Args:
            locale_dir: Directory containing translation files
        """
        for lang in Language:
            try:
                translations = gettext.translation("messages", localedir=locale_dir, languages=[lang.value])
                translations.install()
            except FileNotFoundError:
                # Fallback to null translations if files not found
                gettext.NullTranslations().install()


__version__ = "1.0.0"

__all__ = ["ErrorMessageTemplate", "ErrorMessages", "Language"]

```

## backend/app/config/__init__.py
```

```

## backend/app/config.py
```
"""Application configuration.

This module provides a single source of truth for all application configuration,
using environment variables loaded from .env files.

Configuration Hierarchy:
    1. Environment variables (highest priority)
    2. Environment-specific .env file (.env.development or .env.production)
    3. Default .env file (lowest priority)

Example:
    .. code-block:: python

        from app.config import settings

        # Access configuration
        db_url = settings.DATABASE_URL
        api_key = settings.SPOONACULAR_API_KEY

Note:
    This module uses Pydantic for validation and type safety.
    All configuration is loaded lazily and cached.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any, Literal
from urllib.parse import quote_plus

from pydantic import AnyHttpUrl, BaseModel, PostgresDsn, validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AllergenConfig(BaseModel):
    """Allergen configuration with API mappings."""

    name: str
    keywords: list[str]
    api_mappings: dict[str, str]


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # Environment and API Settings
    ENVIRONMENT: Literal["development", "production", "test"] = "development"
    PROJECT_NAME: str = "Recipe Database API"
    API_V1_STR: str = "/api/v1"
    VERSION: str = "0.1.0"

    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 11520  # 8 days
    ALGORITHM: str = "HS256"

    # Database
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = "recipe_db"
    DATABASE_URL: PostgresDsn | None = None

    # CORS Origins as comma-separated string in .env
    BACKEND_CORS_ORIGINS: str = ""

    # Recipe API Keys
    SPOONACULAR_API_KEY: str
    EDAMAM_APP_ID: str
    EDAMAM_APP_KEY: str
    API_NINJAS_API_KEY: str
    TASTY_API_KEY: str

    # API Rate Limits
    SPOONACULAR_POINTS_PER_DAY: int = 150
    SPOONACULAR_REQUESTS_PER_MINUTE: int = 10
    EDAMAM_REQUESTS_PER_MINUTE: int = 10
    API_NINJAS_REQUESTS_PER_MINUTE: int = 10
    TASTY_REQUESTS_PER_MINUTE: int = 10

    # Cache Settings
    REDIS_URL: str = "redis://localhost"
    CACHE_TTL: int = 3600

    # Service Configuration
    MAX_CONCURRENT_REQUESTS: int = 5
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: Literal["json", "text"] = "json"
    LOG_FILE: str = "logs/recipe_service.log"
    MOCK_RESPONSES: bool = False
    MOCK_DELAY: int = 0
    DEFAULT_RECIPE_PROVIDER: str = "spoonacular"

    # User Management
    FIRST_SUPERUSER: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin"

    # Pydantic Config
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="allow")

    # Computed Properties and Validators
    @validator("DATABASE_URL", pre=True)
    def assemble_db_url(self, v: str | None, values: dict[str, Any]) -> Any:
        """Construct database URL from components if not provided directly."""
        if isinstance(v, str):
            return v

        password = quote_plus(values.get("POSTGRES_PASSWORD", ""))
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.get("POSTGRES_USER"),
            password=password,
            host=values.get("POSTGRES_HOST"),
            port=int(values.get("POSTGRES_PORT", 5432)),
            path=f"/{values.get('POSTGRES_DB', '')}",
        )

    @property
    def cors_origins(self) -> list[AnyHttpUrl]:
        """Get list of allowed CORS origins."""
        origins = self.BACKEND_CORS_ORIGINS.split(",")
        return [origin.strip() for origin in origins if origin.strip()]

    @property
    def allergens(self) -> list[AllergenConfig]:
        """Get list of configured allergens with API mappings."""
        return [
            AllergenConfig(
                name="dairy",
                keywords=["milk", "cream", "cheese", "butter", "yogurt", "casein", "whey"],
                api_mappings={"edamam": "dairy-free"},
            ),
            AllergenConfig(
                name="soy",
                keywords=["soy", "soya", "tofu", "tempeh", "miso", "edamame"],
                api_mappings={"edamam": "soy-free"},
            ),
            AllergenConfig(
                name="egg",
                keywords=["egg", "eggs", "albumin", "globulin", "lecithin", "livetin"],
                api_mappings={"edamam": "egg-free"},
            ),
        ]

    def get_allergen_keywords(self, allergen_name: str) -> list[str]:
        """Get keywords for a specific allergen."""
        for allergen in self.allergens:
            if allergen.name.lower() == allergen_name.lower():
                return allergen.keywords
        return []

    def get_allergen_api_param(self, allergen_name: str, api_name: str) -> str | None:
        """Get API-specific parameter for an allergen."""
        for allergen in self.allergens:
            if allergen.name.lower() == allergen_name.lower():
                return allergen.api_mappings.get(api_name.lower())
        return None


@lru_cache
def get_settings() -> Settings:
    """Get application settings singleton."""
    return Settings()


settings = get_settings()

```

## backend/app/database/__init__.py
```

```

## backend/app/database/session.py
```
"""Database session management."""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.db.base import get_db as base_get_db

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """Get async database session.

    This is a convenience wrapper around the base get_db function
    to make it clearer that we're using async sessions.
    """
    async with base_get_db() as session:
        yield session


# Alias for backward compatibility
get_db = get_async_db

```

## backend/app/routers/__init__.py
```
"""API route handlers package."""

from __future__ import annotations

from backend.app.api.routes.allergens import router as allergens
from backend.app.api.routes.cook_methods import router as cook_methods
from backend.app.api.routes.cuisine_types import router as cuisine_types
from backend.app.api.routes.dietary_restrictions import router as dietary_restrictions
from backend.app.api.routes.family_members import router as family_members
from backend.app.api.routes.ingredients import router as ingredients
from backend.app.api.routes.meal_plans import router as meal_plans
from backend.app.api.routes.meal_types import router as meal_types
from backend.app.api.routes.protein_types import router as protein_types
from backend.app.api.routes.recipe_search import router as recipe_search
from backend.app.api.routes.recipes import router as recipes

__all__ = [
    "allergens",
    "cook_methods",
    "cuisine_types",
    "dietary_restrictions",
    "family_members",
    "ingredients",
    "meal_plans",
    "meal_types",
    "protein_types",
    "recipe_search",
    "recipes",
]

```

## .pre-commit-config.yaml
```
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: check-json
      - id: check-added-large-files
      - id: debug-statements
      - id: detect-private-key
      - id: check-case-conflict
      - id: mixed-line-ending
        args: [--fix=lf]

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.3
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
        files: ^backend/
      - id: ruff-format
        files: ^backend/

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        files: ^backend/
        additional_dependencies:
          [
            "types-requests",
            "types-python-dateutil",
            "types-sqlalchemy",
            "sqlalchemy[mypy]",
            "pydantic",
            "types-redis",
            "types-passlib",
            "types-python-jose",
            "types-aiofiles",
            "types-pytz",
            "types-cachetools",
          ]

```

## frontend/.eslintrc.json
```
{
  "root": true,
  "env": {
    "browser": true,
    "es2021": true,
    "node": true,
    "jest": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
    "plugin:jsx-a11y/recommended",
    "plugin:import/recommended",
    "plugin:import/typescript",
    "plugin:prettier/recommended",
    "next/core-web-vitals"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaFeatures": {
      "jsx": true
    },
    "ecmaVersion": "latest",
    "sourceType": "module",
    "project": "./tsconfig.json"
  },
  "plugins": [
    "react",
    "react-hooks",
    "@typescript-eslint",
    "jsx-a11y",
    "import",
    "prettier"
  ],
  "rules": {
    // TypeScript
    "@typescript-eslint/explicit-module-boundary-types": "off",
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/no-unused-vars": [
      "error",
      {
        "argsIgnorePattern": "^_",
        "varsIgnorePattern": "^_"
      }
    ],
    "@typescript-eslint/consistent-type-imports": [
      "error",
      {
        "prefer": "type-imports"
      }
    ],
    "@typescript-eslint/no-non-null-assertion": "error",

    // React
    "react/react-in-jsx-scope": "off",
    "react/prop-types": "off",
    "react/jsx-curly-brace-presence": [
      "error",
      {
        "props": "never",
        "children": "never"
      }
    ],
    "react/self-closing-comp": [
      "error",
      {
        "component": true,
        "html": true
      }
    ],
    "react-hooks/rules-of-hooks": "error",
    "react-hooks/exhaustive-deps": "warn",

    // Import
    "import/order": [
      "error",
      {
        "groups": [
          ["builtin", "external"],
          "internal",
          ["parent", "sibling"],
          "index",
          "object",
          "type"
        ],
        "pathGroups": [
          {
            "pattern": "react",
            "group": "external",
            "position": "before"
          },
          {
            "pattern": "@/**",
            "group": "internal",
            "position": "after"
          }
        ],
        "pathGroupsExcludedImportTypes": ["react"],
        "newlines-between": "always",
        "alphabetize": {
          "order": "asc",
          "caseInsensitive": true
        }
      }
    ],
    "import/no-duplicates": "error",
    "import/no-unresolved": "error",
    "import/no-cycle": "error",
    "import/no-useless-path-segments": "error",

    // General
    "no-console": [
      "warn",
      {
        "allow": ["warn", "error"]
      }
    ],
    "curly": ["error", "all"],
    "eqeqeq": ["error", "always"],
    "no-floating-decimal": "error",
    "no-unused-private-class-members": "error",
    "no-use-before-define": [
      "error",
      {
        "functions": false,
        "classes": true,
        "variables": true
      }
    ]
  },
  "settings": {
    "react": {
      "version": "detect"
    },
    "import/parsers": {
      "@typescript-eslint/parser": [".ts", ".tsx"]
    },
    "import/resolver": {
      "typescript": {
        "alwaysTryTypes": true,
        "project": "./tsconfig.json"
      }
    }
  },
  "overrides": [
    {
      "files": [
        "**/__tests__/**/*.[jt]s?(x)",
        "**/?(*.)+(spec|test).[jt]s?(x)"
      ],
      "extends": ["plugin:testing-library/react", "plugin:jest/recommended"],
      "rules": {
        "@typescript-eslint/no-explicit-any": "off",
        "@typescript-eslint/no-non-null-assertion": "off"
      }
    }
  ],
  "ignorePatterns": [
    "node_modules",
    ".next",
    "coverage",
    "public",
    "*.config.js",
    "*.setup.ts"
  ]
}

```

## frontend/__tests__/RecipeList.test.tsx
```
import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import RecipeList from '../components/RecipeList';

// Mock fetch
global.fetch = jest.fn();

const mockRecipes = [
  {
    id: 1,
    title: 'Dairy-Free Chicken Curry',
    meal_type: 'dinner',
    is_collection: false,
    source_url: 'https://example.com',
    image_url: 'https://example.com/image.jpg',
    image_preview_url: 'https://example.com/preview.jpg',
    ingredients: [],
    instructions: [],
    prep_time: 10,
    cook_time: 30,
    cooking_method: 'stovetop',
    date_added: '2025-01-28T14:30:41-07:00',
    is_dairy_free: true,
    is_soy_free: false,
    is_gluten_free: false,
    is_nut_free: false,
    is_egg_free: false,
  },
  {
    id: 2,
    title: 'Gluten-Free Collection',
    meal_type: 'collection',
    is_collection: true,
    source_url: 'https://example.com',
    ingredients: [],
    instructions: [],
    date_added: '2025-01-28T14:30:41-07:00',
    is_dairy_free: false,
    is_soy_free: false,
    is_gluten_free: true,
    is_nut_free: false,
    is_egg_free: false,
  },
];

describe('RecipeList', () => {
  beforeEach(() => {
    (global.fetch as jest.Mock).mockReset();
  });

  it('renders recipe cards with correct information', async () => {
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockRecipes,
    });

    render(<RecipeList />);

    // Wait for recipes to load
    await waitFor(() => {
      expect(screen.getByText('Dairy-Free Chicken Curry')).toBeInTheDocument();
    });

    // Check if recipe details are displayed
    expect(screen.getAllByText('Dinner')).toHaveLength(2);
    expect(screen.getByText('Stovetop')).toBeInTheDocument();
    expect(screen.getAllByText('Dairy Free')).toHaveLength(2);
    expect(screen.getByText('Prep: 10m | Cook: 30m')).toBeInTheDocument();

    // Check if collection is displayed
    expect(screen.getByText('Gluten-Free Collection')).toBeInTheDocument();
    expect(screen.getAllByText('Gluten Free')).toHaveLength(2);
  });

  it('applies filters correctly', async () => {
    const mockFetch = global.fetch as jest.Mock;
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockRecipes,
    });

    render(<RecipeList />);

    // Wait for initial load
    await waitFor(() => {
      expect(screen.getByText('Dairy-Free Chicken Curry')).toBeInTheDocument();
    });

    // Apply meal type filter
    const mealTypeSelect = screen.getByLabelText('Meal Type');
    await userEvent.selectOptions(mealTypeSelect, 'dinner');

    // Check if fetch was called with correct params
    await waitFor(() => {
      expect(mockFetch).toHaveBeenCalledWith(expect.stringContaining('meal_type=dinner'));
    });

    // Apply allergen filter
    const dairyFreeCheckbox = screen.getByLabelText('Dairy Free');
    fireEvent.click(dairyFreeCheckbox);

    await waitFor(() => {
      expect(mockFetch).toHaveBeenCalledWith(expect.stringContaining('allergens=dairy'));
    });

    // Apply search query
    const searchInput = screen.getByLabelText('Search Recipes');
    await userEvent.type(searchInput, 'curry');

    await waitFor(() => {
      expect(mockFetch).toHaveBeenCalledWith(expect.stringContaining('q=curry'));
    });
  });

  it('handles empty state', async () => {
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => [],
    });

    render(<RecipeList />);

    // Wait for loading to finish
    await waitFor(() => {
      expect(screen.queryByRole('progressbar')).not.toBeInTheDocument();
    });

    // Verify no recipe cards are shown
    expect(screen.queryByRole('img')).not.toBeInTheDocument();
  });

  it('handles fetch errors gracefully', async () => {
    const consoleError = jest.spyOn(console, 'error').mockImplementation(() => {});
    (global.fetch as jest.Mock).mockRejectedValueOnce(new Error('Failed to fetch'));

    render(<RecipeList />);

    await waitFor(() => {
      expect(consoleError).toHaveBeenCalledWith('Error fetching recipes:', expect.any(Error));
    });

    consoleError.mockRestore();
  });
});

```

## frontend/__tests__/RecipeCuration.test.tsx
```
import { render, screen, waitFor } from '@testing-library/react';
import { RecipeSearch } from '../components/recipe/RecipeSearch';
import { useRecipeStore } from '../stores/recipeStore';
import { useFamilyProfileStore } from '../stores/familyProfileStore';
import * as mockStores from './mocks/mockStores';
import userEvent from '@testing-library/user-event';

// Mock the stores
jest.mock('../stores/recipeStore');
jest.mock('../stores/familyProfileStore');

const mockUseRecipeStore = useRecipeStore as jest.MockedFunction<typeof useRecipeStore>;
const mockUseFamilyProfileStore = useFamilyProfileStore as jest.MockedFunction<typeof useFamilyProfileStore>;

describe('RecipeSearch Component', () => {
  const mockSearchRecipes = jest.fn().mockResolvedValue(undefined);
  const mockToggleFavorite = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
    jest.useFakeTimers();

    // Mock store implementations
    mockUseRecipeStore.mockReturnValue(
      mockStores.createMockRecipeStore({
        searchRecipes: mockSearchRecipes,
        toggleFavorite: mockToggleFavorite,
      })
    );

    mockUseFamilyProfileStore.mockReturnValue(mockStores.mockFamilyProfile);
  });

  afterEach(() => {
    jest.useRealTimers();
  });

  describe('Search Functionality', () => {
    it('should debounce search requests by 300ms', async () => {
      render(<RecipeSearch />);
      const searchInput = screen.getByPlaceholderText(/search for recipes/i);

      // Type search query
      await userEvent.type(searchInput, 'test recipe');

      // Fast-forward timers
      jest.advanceTimersByTime(200);
      expect(mockSearchRecipes).not.toHaveBeenCalled();

      jest.advanceTimersByTime(100);
      await waitFor(() => {
        expect(mockSearchRecipes).toHaveBeenCalledWith(
          'test recipe',
          expect.any(Object)
        );
      });
    });
  });

  describe('Filter Functionality', () => {
    it('should apply family profile allergen filters automatically', async () => {
      mockUseRecipeStore.mockReturnValue(
        mockStores.createMockRecipeStore({
          searchRecipes: mockSearchRecipes,
          filters: {
            isDairyFree: false,
            isEggFree: false,
            isSoyFree: false
          }
        })
      );

      mockUseFamilyProfileStore.mockReturnValue({
        profile: {
          isDairyFree: true,
          isEggFree: false,
          isSoyFree: true
        }
      });

      render(<RecipeSearch />);
      const searchInput = screen.getByPlaceholderText(/search for recipes/i);

      await userEvent.type(searchInput, 'test');
      jest.advanceTimersByTime(300);

      expect(mockSearchRecipes).toHaveBeenCalledWith('test', {
        isDairyFree: true,
        isEggFree: false,
        isSoyFree: true
      });
    });

    it('should toggle filters when filter buttons are clicked', async () => {
      const setFilters = jest.fn();
      mockUseRecipeStore.mockReturnValue(
        mockStores.createMockRecipeStore({
          searchRecipes: mockSearchRecipes,
          setFilters,
          filters: {
            isDairyFree: false,
            isEggFree: false,
            isSoyFree: false
          }
        })
      );

      render(<RecipeSearch />);

      const dairyFreeButton = screen.getByRole('button', { name: /dairy free/i });
      await userEvent.click(dairyFreeButton);

      expect(setFilters).toHaveBeenCalledWith({
        isDairyFree: true,
        isEggFree: false,
        isSoyFree: false
      });
    });
  });

  describe('Loading and Error States', () => {
    it('should display loading spinner when searching', () => {
      mockUseRecipeStore.mockReturnValue(
        mockStores.createMockRecipeStore({
          searchRecipes: mockSearchRecipes,
          loading: true,
          recipes: []
        })
      );

      render(<RecipeSearch />);

      expect(screen.getByRole('status')).toBeInTheDocument();
      expect(screen.getByPlaceholderText(/search for recipes/i)).toBeDisabled();
    });

    it('should display error message when search fails', () => {
      const testErrorMessage = 'Failed to fetch recipes';

      mockUseRecipeStore.mockReturnValue(
        mockStores.createMockRecipeStore({
          searchRecipes: mockSearchRecipes,
          error: testErrorMessage
        })
      );

      render(<RecipeSearch />);
      expect(screen.getByText(testErrorMessage)).toBeInTheDocument();
    });
  });
});

```

## frontend/__tests__/utils/test-utils.tsx
```
import { render as rtlRender } from '@testing-library/react';
import type { RenderOptions } from '@testing-library/react';
import type { ReactElement } from 'react';
import { ChakraProvider } from '@chakra-ui/react';
import '@testing-library/jest-dom';

// Extend Jest matchers
declare global {
  namespace jest {
    interface Matchers<R> {
      toBeInTheDocument(): R;
      toHaveAttribute(attr: string, value?: string): R;
      toHaveTextContent(text: string | RegExp): R;
    }
  }
}

// Custom render function that includes providers
export function render(
  ui: ReactElement,
  options?: Omit<RenderOptions, 'wrapper'>
) {
  const Wrapper = ({ children }: { children: React.ReactNode }) => (
    <ChakraProvider>{children}</ChakraProvider>
  );

  return rtlRender(ui, { wrapper: Wrapper, ...options });
}

// Re-export everything
export * from '@testing-library/react';
export { default as userEvent } from '@testing-library/user-event';

```

## frontend/__tests__/components/RecipeCard.test.tsx
```
import { RecipeCard } from '../../components/recipe/RecipeCard';
import { render, screen } from '@testing-library/react';
import type { Recipe } from '../../types/recipe';

const mockRecipe: Recipe = {
  id: 1,
  title: 'Test Recipe',
  description: 'A delicious test recipe',
  ingredients: ['ingredient 1', 'ingredient 2'],
  instructions: ['step 1', 'step 2'],
  meal_type: 'dinner',
  is_collection: false,
  date_added: new Date().toISOString(),
  is_dairy_free: false,
  is_gluten_free: false,
  is_soy_free: false,
  is_nut_free: false,
  is_egg_free: false,
  is_fpies_friendly: false,
  fpies_triggers: [],
  fpies_safe_substitutes: {},
  allergens: [],
  times_made: 0,
  cooking_method: 'stovetop',
  protein_type: 'other',
  prep_time: 15,
  cook_time: 30,
  servings: 4,
  image_url: 'test.jpg',
  image_preview_url: 'test.jpg'
};

describe('RecipeCard', () => {
  it('renders recipe details correctly', () => {
    render(<RecipeCard recipe={mockRecipe} />);

    // Check basic recipe info
    expect(screen.getByText(mockRecipe.title)).toBeInTheDocument();
    expect(screen.getByText(mockRecipe.description)).toBeInTheDocument();
    expect(screen.getByText((content) => content.includes(mockRecipe.meal_type))).toBeInTheDocument();
    expect(screen.getByText((content) => content.includes('Stovetop'))).toBeInTheDocument();

    // Check cooking times
    expect(screen.getByText(/Prep: 15/)).toBeInTheDocument();
    expect(screen.getByText(/Cook: 30/)).toBeInTheDocument();
  });

  it('handles click events', () => {
    const handleClick = jest.fn();
    render(<RecipeCard recipe={mockRecipe} onClick={handleClick} />);

    const card = screen.getByRole('article');
    card.click();

    expect(handleClick).toHaveBeenCalled();
  });
});

```

## frontend/services/api.ts
```
import axios, { AxiosInstance } from 'axios';
import type {
  Allergen,
  AllergenCreate,
  CookMethod,
  CookMethodCreate,
  CuisineType,
  CuisineTypeCreate,
  DietaryRestriction,
  DietaryRestrictionCreate,
  FamilyMember,
  FamilyMemberCreate,
  Ingredient,
  IngredientCategory,
  IngredientCreate,
  MealPlan,
  MealPlanCreate,
  MealType,
  MealTypeCreate,
  ProteinType,
  ProteinTypeCreate,
  Recipe,
  RecipeCreate,
  RecipeList,
  RecipeRating,
  RecipeRatingCreate,
  RecipeSearchFilters,
  RecipeUpdate,
} from '../types/api';

class ApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api',
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  // Recipes
  async getRecipes(page = 1, limit = 20) {
    const { data } = await this.client.get<Recipe[]>('/recipes', {
      params: { skip: (page - 1) * limit, limit },
    });
    return data;
  }

  async getRecipe(id: number) {
    const { data } = await this.client.get<Recipe>(`/recipes/${id}`);
    return data;
  }

  async createRecipe(recipe: RecipeCreate) {
    const { data } = await this.client.post<Recipe>('/recipes', recipe);
    return data;
  }

  async updateRecipe(id: number, recipe: RecipeUpdate) {
    const { data } = await this.client.put<Recipe>(`/recipes/${id}`, recipe);
    return data;
  }

  async deleteRecipe(id: number) {
    await this.client.delete(`/recipes/${id}`);
  }

  // Recipe Search
  async searchRecipes(
    query: string,
    filters?: RecipeSearchFilters,
    page = 1,
    limit = 20
  ) {
    const { data } = await this.client.get<RecipeList>('/recipe-search', {
      params: {
        query,
        ...filters,
        page,
        page_size: limit,
      },
    });
    return data;
  }

  // Ingredients
  async getIngredients(page = 1, limit = 100) {
    const { data } = await this.client.get<Ingredient[]>('/ingredients', {
      params: { skip: (page - 1) * limit, limit },
    });
    return data;
  }

  async createIngredient(ingredient: IngredientCreate) {
    const { data } = await this.client.post<Ingredient>(
      '/ingredients',
      ingredient
    );
    return data;
  }

  // Ingredient Categories
  async getIngredientCategories() {
    const { data } = await this.client.get<IngredientCategory[]>(
      '/ingredient-categories'
    );
    return data;
  }

  // Allergens
  async getAllergens() {
    const { data } = await this.client.get<Allergen[]>('/allergens');
    return data;
  }

  async createAllergen(allergen: AllergenCreate) {
    const { data } = await this.client.post<Allergen>('/allergens', allergen);
    return data;
  }

  // Cook Methods
  async getCookMethods() {
    const { data } = await this.client.get<CookMethod[]>('/cook-methods');
    return data;
  }

  async createCookMethod(method: CookMethodCreate) {
    const { data } = await this.client.post<CookMethod>(
      '/cook-methods',
      method
    );
    return data;
  }

  // Protein Types
  async getProteinTypes() {
    const { data } = await this.client.get<ProteinType[]>('/protein-types');
    return data;
  }

  async createProteinType(type: ProteinTypeCreate) {
    const { data } = await this.client.post<ProteinType>(
      '/protein-types',
      type
    );
    return data;
  }

  // Meal Types
  async getMealTypes() {
    const { data } = await this.client.get<MealType[]>('/meal-types');
    return data;
  }

  async createMealType(type: MealTypeCreate) {
    const { data } = await this.client.post<MealType>('/meal-types', type);
    return data;
  }

  // Cuisine Types
  async getCuisineTypes() {
    const { data } = await this.client.get<CuisineType[]>('/cuisine-types');
    return data;
  }

  async createCuisineType(type: CuisineTypeCreate) {
    const { data } = await this.client.post<CuisineType>(
      '/cuisine-types',
      type
    );
    return data;
  }

  // Dietary Restrictions
  async getDietaryRestrictions() {
    const { data } = await this.client.get<DietaryRestriction[]>(
      '/dietary-restrictions'
    );
    return data;
  }

  async createDietaryRestriction(restriction: DietaryRestrictionCreate) {
    const { data } = await this.client.post<DietaryRestriction>(
      '/dietary-restrictions',
      restriction
    );
    return data;
  }

  // Family Members
  async getFamilyMembers() {
    const { data } = await this.client.get<FamilyMember[]>('/family-members');
    return data;
  }

  async createFamilyMember(member: FamilyMemberCreate) {
    const { data } = await this.client.post<FamilyMember>(
      '/family-members',
      member
    );
    return data;
  }

  // Meal Plans
  async getMealPlans(page = 1, limit = 20) {
    const { data } = await this.client.get<MealPlan[]>('/meal-plans', {
      params: { skip: (page - 1) * limit, limit },
    });
    return data;
  }

  async createMealPlan(plan: MealPlanCreate) {
    const { data } = await this.client.post<MealPlan>('/meal-plans', plan);
    return data;
  }

  // Recipe Ratings
  async getRecipeRatings(recipeId: number) {
    const { data } = await this.client.get<RecipeRating[]>(
      `/recipes/${recipeId}/ratings`
    );
    return data;
  }

  async createRecipeRating(rating: RecipeRatingCreate) {
    const { data } = await this.client.post<RecipeRating>(
      '/recipe-ratings',
      rating
    );
    return data;
  }
}

export const apiClient = new ApiClient();

```

## frontend/services/api/BaseApiClient.ts
```
import axios, {
  type AxiosInstance,
  type InternalAxiosRequestConfig,
  type AxiosResponse,
  type AxiosError,
  type RawAxiosRequestHeaders,
  type AxiosRequestConfig,
} from 'axios';
import type {
  ApiConfig,
  ApiRequestConfig,
  RequestInterceptor,
  ResponseInterceptor,
} from '../../types/api';

export class BaseApiClient {
  protected config: ApiConfig;
  protected axios: AxiosInstance;
  protected requestInterceptors: RequestInterceptor[] = [];
  protected responseInterceptors: ResponseInterceptor[] = [];

  constructor(config: Partial<ApiConfig>) {
    this.config = {
      baseUrl: '',
      defaultParams: {},
      headers: {},
      timeout: 10000,
      ...config,
    };

    this.axios = axios.create({
      baseURL: this.config.baseUrl,
      timeout: this.config.timeout,
      headers: this.config.headers,
    });

    // Setup default interceptors
    this.setupInterceptors();
  }

  protected setupInterceptors() {
    // Request interceptor
    this.axios.interceptors.request.use((config: InternalAxiosRequestConfig) => {
      const apiRequestConfig: ApiRequestConfig = {
        url: config.url || '',
        method: (config.method?.toUpperCase() as ApiRequestConfig['method']) || 'GET',
        params: { ...this.config.defaultParams, ...(config.params || {}) },
        data: config.data,
        headers: { ...this.config.headers, ...(config.headers || {}) } as RawAxiosRequestHeaders,
      };

      // Run through all request interceptors
      const modifiedConfig = this.requestInterceptors.reduce(
        (conf, interceptor) => interceptor.onRequest(conf),
        apiRequestConfig
      );

      return {
        ...config,
        ...modifiedConfig,
        headers: { ...config.headers, ...modifiedConfig.headers },
      } as InternalAxiosRequestConfig;
    });

    // Response interceptor
    this.axios.interceptors.response.use(
      async (response: AxiosResponse) => {
        let data = response.data;
        for (const interceptor of this.responseInterceptors) {
          data = await interceptor.onResponse(data);
        }
        return data;
      },
      async (error: AxiosError) => {
        let currentError = error;
        for (const interceptor of this.responseInterceptors) {
          currentError = await interceptor.onError(currentError);
        }
        throw currentError;
      }
    );
  }

  public addRequestInterceptor(interceptor: RequestInterceptor): void {
    this.requestInterceptors.push(interceptor);
  }

  public addResponseInterceptor(interceptor: ResponseInterceptor): void {
    this.responseInterceptors.push(interceptor);
  }

  public updateConfig(newConfig: Partial<ApiConfig>): void {
    this.config = {
      ...this.config,
      ...newConfig,
      defaultParams: {
        ...this.config.defaultParams,
        ...newConfig.defaultParams,
      },
      headers: {
        ...this.config.headers,
        ...newConfig.headers,
      },
    };

    Object.assign(this.axios.defaults, {
      baseURL: this.config.baseUrl,
      timeout: this.config.timeout,
      headers: { ...this.config.headers },
    });
  }

  protected async request<T>(config: ApiRequestConfig): Promise<T> {
    const response = await this.axios.request({
      ...config,
    });
    return response as T;
  }
}

```

## frontend/services/api/SpoonacularApiClient.ts
```
import type { ApiSource } from '../../types/api';
import type { Recipe } from '../../types/recipe';
import { BaseApiClient } from './BaseApiClient';

interface SpoonacularRecipe {
  id: number;
  title: string;
  image: string;
  imageType: string;
  servings: number;
  readyInMinutes: number;
  dairyFree: boolean;
  glutenFree: boolean;
  vegan: boolean;
  vegetarian: boolean;
  veryHealthy: boolean;
  // ... other Spoonacular specific fields
}

export class SpoonacularApiClient extends BaseApiClient {
  public static source: ApiSource = {
    name: 'Spoonacular',
    description: 'Comprehensive recipe database with detailed nutritional information',
    defaultConfig: {
      baseUrl: 'https://api.spoonacular.com',
      defaultParams: {
        apiKey: process.env.NEXT_PUBLIC_SPOONACULAR_API_KEY,
      },
    },
    parameterDocs: [
      {
        name: 'query',
        description: 'Search query for recipes',
        type: 'string',
        required: true,
      },
      {
        name: 'diet',
        description: 'Diet restrictions',
        type: 'string',
        required: false,
        options: ['vegetarian', 'vegan', 'gluten-free', 'dairy-free'],
      },
      {
        name: 'intolerances',
        description: 'Food intolerances to avoid',
        type: 'array',
        required: false,
        options: ['dairy', 'egg', 'gluten', 'peanut', 'seafood', 'shellfish', 'soy', 'wheat'],
      },
      {
        name: 'maxReadyTime',
        description: 'Maximum total cooking and prep time in minutes',
        type: 'number',
        required: false,
      },
    ],
  };

  constructor() {
    super(SpoonacularApiClient.source.defaultConfig);
  }

  private convertToRecipe(spoonacularRecipe: SpoonacularRecipe): Recipe {
    return {
      id: spoonacularRecipe.id,
      title: spoonacularRecipe.title,
      image_url: spoonacularRecipe.image,
      is_dairy_free: spoonacularRecipe.dairyFree,
      is_gluten_free: spoonacularRecipe.glutenFree,
      prep_time: spoonacularRecipe.readyInMinutes,
      servings: spoonacularRecipe.servings,
      // ... convert other fields
    } as Recipe;
  }

  public async searchRecipes(
    query: string,
    params: Record<string, string | number | boolean> = {}
  ): Promise<Recipe[]> {
    const response = await this.request<{ results: SpoonacularRecipe[] }>({
      url: '/recipes/complexSearch',
      method: 'GET',
      params: {
        query,
        addRecipeInformation: true,
        fillIngredients: true,
        ...params,
      },
    });

    return response.results.map((recipe) => this.convertToRecipe(recipe));
  }

  public async getRecipeById(id: number): Promise<Recipe> {
    const response = await this.request<SpoonacularRecipe>({
      url: `/recipes/${id}/information`,
      method: 'GET',
      params: {
        addRecipeInformation: true,
        fillIngredients: true,
      },
    });

    return this.convertToRecipe(response);
  }
}

```

## frontend/__tests__/mocks/mockStores.ts
```
import type { FamilyProfileState } from '../../stores/familyProfileStore';
import type { Recipe, SearchFilters } from '../../types';

export const mockRecipeWithAllergens: Recipe = {
  id: 1,
  title: 'Recipe with Hidden Allergens',
  description: 'A test recipe with allergens',
  ingredients: ['natural flavors', 'casein'],
  instructions: ['step 1'],
  meal_type: 'dinner',
  cooking_method: 'stovetop',
  allergenWarnings: ['Contains dairy derivatives'],
  is_collection: false,
  date_added: new Date().toISOString(),
  is_dairy_free: false,
  is_gluten_free: true,
  is_soy_free: true,
  is_nut_free: true,
  is_egg_free: true,
  is_fpies_friendly: true,
  fpies_triggers: [],
  fpies_safe_substitutes: {},
  allergens: ['dairy'],
  times_made: 0,
  protein_type: 'other',
  prep_time: 15,
  cook_time: 30,
  servings: 4,
  image_url: 'test.jpg',
  image_preview_url: 'test.jpg'
};

export const mockFamilyProfile: FamilyProfileState = {
  members: [
    {
      id: '1',
      name: 'Test User',
      allergies: ['dairy', 'eggs'],
      fpiesTriggers: [],
      safeSubstitutes: {},
      reactionHistory: []
    }
  ],
  activeProfile: '1',
  addMember: jest.fn(),
  updateMember: jest.fn(),
  setActiveProfile: jest.fn(),
  addReaction: jest.fn(),
  addSafeSubstitute: jest.fn()
};

export type RecipeStore = {
  recipes: Recipe[];
  loading: boolean;
  error: string | null;
  filters: SearchFilters;
  searchRecipes: () => Promise<void>;
  toggleFavorite: () => void;
  setFilters: () => void;
};

export const createMockRecipeStore = (overrides: Partial<RecipeStore> = {}): RecipeStore => ({
  recipes: [],
  loading: false,
  error: null,
  filters: {
    isDairyFree: false,
    isEggFree: false,
    isSoyFree: false,
    isGlutenFree: false,
    isNutFree: false,
    isFpiesFriendly: false
  },
  searchRecipes: jest.fn().mockResolvedValue(undefined),
  toggleFavorite: jest.fn(),
  setFilters: jest.fn(),
  ...overrides
});

```

## frontend/services/api/errors/ApiError.ts
```
import type { ApiRequestConfig } from '../../../types/api';

export class ApiError extends Error {
  constructor(
    message: string,
    public readonly config?: ApiRequestConfig,
    public readonly statusCode?: number,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'ApiError';
  }

  public static fromError(error: unknown, config?: ApiRequestConfig): ApiError {
    if (error instanceof ApiError) {
      return error;
    }

    if (error instanceof Error) {
      return new ApiError(error.message, config, undefined, error);
    }

    return new ApiError(
      typeof error === 'string' ? error : 'An unexpected error occurred',
      config
    );
  }
}

```

## frontend/services/api/_gemini_code_review/manifest.json
```
{
  "files": [
    {
      "file": "BaseApiClient.ts.review.json"
    }
  ]
}

```

## frontend/services/api/_gemini_code_review/BaseApiClient.ts.review.json
```
{
  "filename": "BaseApiClient.ts",
  "category": "Basic Code Review",
  "issues": [
    {
      "type": "Maintainability",
      "severity": "Medium",
      "description": "The `setupInterceptors` method directly modifies the `AxiosRequestConfig` object. This can lead to unexpected side effects if the original object is used elsewhere. It's better to create a new object with the modified values."
    },
    {
      "type": "Maintainability",
      "severity": "Medium",
      "description": "The `updateConfig` method updates the `axios.defaults` directly. This can be problematic if multiple instances of `BaseApiClient` are used, as they will share the same `axios` instance and its defaults. It's better to recreate the `axios` instance when the configuration changes."
    },
    {
      "type": "Maintainability",
      "severity": "Low",
      "description": "The `request` method casts the response to `T` without any type checking. This can lead to runtime errors if the response type doesn't match the expected type. Consider adding type checking or using a more robust type assertion mechanism."
    },
    {
      "type": "Code Quality",
      "severity": "Low",
      "description": "The code uses a mix of `const` and `let` for variables. For consistency, it's generally recommended to use `const` by default and only use `let` when the variable needs to be reassigned."
    },
    {
      "type": "Code Quality",
      "severity": "Low",
      "description": "The code uses `AxiosRequestConfig` from `axios` directly in the `setupInterceptors` method. It might be better to use the custom `ApiRequestConfig` type for consistency and to avoid direct dependency on `axios`'s internal types."
    },
    {
      "type": "Maintainability",
      "severity": "Low",
      "description": "The default timeout is hardcoded to 10000ms. It might be better to make this configurable through an environment variable or a constant."
    },
    {
      "type": "Adherence to Patterns",
      "severity": "Low",
      "description": "The code uses a combination of object spread and manual property assignment for merging objects. It might be more consistent to use a single approach, such as object spread, for all object merging operations."
    }
  ]
}

```

## frontend/biome.json
```
{
  "$schema": "./node_modules/@biomejs/biome/configuration_schema.json",
  "organizeImports": {
    "enabled": true
  },
  "javascript": {
    "globals": ["jest", "describe", "it", "expect", "beforeEach", "afterEach", "beforeAll", "afterAll"],
    "formatter": {
      "quoteStyle": "single",
      "trailingCommas": "es5",
      "semicolons": "always"
    }
  },
  "files": {
    "ignore": [
      ".next/**/*",
      "node_modules/**/*",
      "build/**/*",
      "dist/**/*",
      "coverage/**/*",
      "**/generated/**/*",
      "./coverage/**",
      "./dist/**",
      "./node_modules/**",
      "**/*.d.ts"
    ]
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "correctness": {
        "noUnusedVariables": "error",
        "noUndeclaredVariables": {
          "level": "info"
        },
        "useExhaustiveDependencies": "error",
        "noUnusedImports": "error",
        "noConstantCondition": "error"
      },
      "suspicious": {
        "noExplicitAny": "error",
        "noDoubleEquals": "error",
        "noConsoleLog": "warn",
        "noEmptyInterface": "error",
        "noRedeclare": "error",
        "noConfusingVoidType": "error",
        "noPrototypeBuiltins": "error",
        "noMisleadingInstantiator": "error"
      },
      "style": {
        "useBlockStatements": "error",
        "useShorthandArrayType": "error",
        "noNonNullAssertion": "error",
        "useTemplate": "error",
        "useConst": "error",
        "noUselessElse": "error",
        "useEnumInitializers": "error",
        "useImportType": "error",
        "useExportType": "error"
      },
      "complexity": {
        "noForEach": {
          "level": "off"
        },
        "noBannedTypes": "error",
        "noStaticOnlyClass": "error",
        "noUselessConstructor": "error",
        "noUselessFragments": "error",
        "noThisInStatic": "error",
        "noUselessTypeConstraint": "error"
      },
      "security": {
        "noDangerouslySetInnerHtml": "error",
        "noDangerouslySetInnerHtmlWithChildren": "error"
      },
      "performance": {
        "noDelete": "error",
        "noAccumulatingSpread": {
          "level": "info"
        }
      }
    }
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 100
  }
}

```

## frontend/playwright.config.ts
```
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
});

```

## frontend/tsconfig.json
```
{
  "compilerOptions": {
    // Type Checking
    "strict": true,
    "noImplicitAny": true,
    "noImplicitThis": true,
    "alwaysStrict": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noPropertyAccessFromIndexSignature": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,

    // Modules
    "target": "es2022",
    "lib": ["dom", "dom.iterable", "esnext"],
    "module": "esnext",
    "moduleResolution": "bundler",
    "baseUrl": ".",
    "paths": {
      "@/*": ["./*"],
      "@/components/*": ["./components/*"],
      "@/lib/*": ["./lib/*"],
      "@/types/*": ["./types/*"],
      "@/styles/*": ["./styles/*"]
    },
    "resolveJsonModule": true,
    "allowJs": true,
    "checkJs": true,

    // Emit
    "noEmit": true,
    "isolatedModules": true,
    "esModuleInterop": true,
    "preserveConstEnums": true,
    "skipLibCheck": true,
    "sourceMap": true,
    "removeComments": false,
    "forceConsistentCasingInFileNames": true,

    // Language and Environment
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ]
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules", "build", "dist", "coverage", ".next"]
}

```

## frontend/.prettierrc
```
{
  "endOfLine": "lf",
  "importOrder": ["^react", "^@/(.*)$", "^[./]"],
  "importOrderSeparation": true,
  "importOrderSortSpecifiers": true,
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "tabWidth": 2,
  "useTabs": false,
  "printWidth": 80,
  "bracketSpacing": true,
  "bracketSameLine": false,
  "arrowParens": "always"
}

```

## frontend/pages/_app.tsx
```
import { ChakraProvider } from '@chakra-ui/react';

import { theme } from '../theme';

import type { AppProps } from 'next/app';

// Optional: Add global styles
import '@/styles/globals.css';

export default function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider theme={theme}>
      <Component {...pageProps} />
    </ChakraProvider>
  );
}

```

## frontend/theme/index.ts
```
import { extendTheme } from '@chakra-ui/react';

const components = {
  Container: {
    baseStyle: {
      maxW: 'container.xl',
      px: { base: 4, md: 8 },
      py: 8,
    },
  },
  Card: {
    baseStyle: {
      container: {
        borderWidth: '1px',
        borderRadius: 'lg',
        overflow: 'hidden',
        bg: 'white',
        _dark: {
          bg: 'gray.800',
        },
        transition: 'all 0.2s',
        _hover: { shadow: 'md' },
      },
      body: {
        p: 6,
      },
      image: {
        height: '200px',
        width: '100%',
        objectFit: 'cover',
      },
    },
  },
  Heading: {
    baseStyle: {
      mb: 4,
    },
    variants: {
      pageTitle: {
        fontSize: '2xl',
        fontWeight: 'bold',
        mb: 8,
      },
      sectionTitle: {
        fontSize: 'xl',
        fontWeight: 'semibold',
        mb: 4,
      },
    },
  },
  Text: {
    variants: {
      secondary: {
        color: 'gray.600',
        _dark: {
          color: 'gray.400',
        },
      },
      error: {
        color: 'red.500',
      },
      empty: {
        color: 'gray.500',
        textAlign: 'center',
      },
    },
  },
  Button: {
    variants: {
      filter: {
        variant: 'ghost',
        size: 'sm',
      },
    },
  },
  Grid: {
    variants: {
      responsive: {
        templateColumns: {
          base: '1fr',
          md: 'repeat(2, 1fr)',
          lg: 'repeat(3, 1fr)',
        },
        gap: 6,
      },
      filters: {
        templateColumns: {
          base: '1fr',
          md: 'repeat(3, 1fr)',
        },
        gap: 4,
      },
    },
  },
  Form: {
    baseStyle: {
      container: {
        p: 4,
        borderWidth: '1px',
        borderRadius: 'lg',
        bg: 'white',
        _dark: {
          bg: 'gray.800',
        },
        shadow: 'sm',
      },
    },
  },
};

const theme = extendTheme({
  components,
  styles: {
    global: {
      body: {
        bg: 'gray.50',
        _dark: {
          bg: 'gray.900',
        },
      },
    },
  },
});

export default theme;

```

## frontend/theme/components/recipe.ts
```
import { defineStyle, defineStyleConfig } from '@chakra-ui/styled-system';

const baseStyle = defineStyle({
  card: {
    container: {
      bg: 'white',
      _dark: {
        bg: 'gray.800',
      },
      borderRadius: 'lg',
      boxShadow: 'md',
      overflow: 'hidden',
      transition: 'all 0.2s',
    },
    image: {
      height: '200px',
      objectFit: 'cover',
      width: '100%',
    },
    content: {
      p: 6,
    },
    title: {
      fontSize: 'xl',
      fontWeight: 'semibold',
      mb: 2,
    },
    description: {
      color: 'gray.600',
      _dark: {
        color: 'gray.300',
      },
    },
  },
  grid: {
    container: {
      width: '100%',
      gap: { base: 4, md: 6 },
      columns: { base: 1, md: 2, lg: 3 },
    },
  },
  filters: {
    container: {
      p: 4,
      bg: 'gray.50',
      _dark: {
        bg: 'gray.700',
      },
      borderRadius: 'md',
      mb: 6,
    },
  },
});

const variants = {
  featured: defineStyle({
    card: {
      container: {
        boxShadow: 'xl',
      },
      image: {
        height: '300px',
      },
    },
  }),
  compact: defineStyle({
    card: {
      container: {
        boxShadow: 'sm',
      },
      image: {
        height: '150px',
      },
      content: {
        p: 4,
      },
    },
  }),
};

export const recipeTheme = defineStyleConfig({
  baseStyle,
  variants,
  defaultProps: {
    variant: 'default',
  },
});

```

## frontend/hooks/useFilteredRecipes.ts
```
import { useFamilyProfile } from '@/stores/familyProfileStore';
import { useRecipes } from './useRecipes';

export function useFilteredRecipes(options?: {
  activeProfileId?: string;
  includeSubstitutions?: boolean;
}) {
  const { data: recipesData, ...queryInfo } = useRecipes();
  const { members } = useFamilyProfile();

  const activeProfile = options?.activeProfileId
    ? members.find((m) => m.id === options.activeProfileId)
    : null;

  const recipes = recipesData?.data || [];

  const filteredAndAnnotatedRecipes = recipes.map((recipe) => {
    const warnings: string[] = [];
    const substitutions: Record<string, string[]> = {};

    if (activeProfile) {
      // Check for allergens
      activeProfile.allergies.forEach((allergy) => {
        if (recipe.allergens?.includes(allergy)) {
          warnings.push(`Contains ${allergy}`);
        }
      });

      // Check for FPIES triggers
      activeProfile.fpiesTriggers.forEach((trigger) => {
        if (recipe.fpies_triggers?.includes(trigger)) {
          warnings.push(`FPIES Trigger: ${trigger}`);
        }

        // Add known safe substitutions
        if (options?.includeSubstitutions && activeProfile.safeSubstitutes[trigger]) {
          substitutions[trigger] = activeProfile.safeSubstitutes[trigger];
        }
      });
    }

    return {
      ...recipe,
      warnings,
      substitutions,
      isSafe: warnings.length === 0,
    };
  });

  // Sort recipes: safe ones first, then ones with substitutions, then others
  const sortedRecipes = filteredAndAnnotatedRecipes.sort((a, b) => {
    if (a.isSafe && !b.isSafe) {
      return -1;
    }
    if (!a.isSafe && b.isSafe) {
      return 1;
    }
    if (Object.keys(a.substitutions).length > Object.keys(b.substitutions).length) {
      return -1;
    }
    if (Object.keys(a.substitutions).length < Object.keys(b.substitutions).length) {
      return 1;
    }
    return 0;
  });

  return {
    ...queryInfo,
    data: sortedRecipes,
    safeRecipes: sortedRecipes.filter((r) => r.isSafe),
    recipesWithSubstitutions: sortedRecipes.filter((r) => Object.keys(r.substitutions).length > 0),
    unsafeRecipes: sortedRecipes.filter(
      (r) => !r.isSafe && Object.keys(r.substitutions).length === 0
    ),
  };
}

```

## frontend/theme/components/card.ts
```
import { defineStyle, defineStyleConfig } from '@chakra-ui/styled-system';

const baseStyle = defineStyle({
  container: {
    bg: 'white',
    _dark: {
      bg: 'gray.800',
    },
    borderRadius: 'lg',
    boxShadow: 'sm',
    transition: 'all 0.2s',
  },
});

const variants = {
  elevated: defineStyle({
    container: {
      boxShadow: 'md',
      _hover: {
        boxShadow: 'lg',
      },
    },
  }),
  outline: defineStyle({
    container: {
      border: '1px solid',
      borderColor: 'gray.200',
      _dark: {
        borderColor: 'gray.700',
      },
    },
  }),
};

export const cardTheme = defineStyleConfig({
  baseStyle,
  variants,
  defaultProps: {
    variant: 'elevated',
  },
});

```

## frontend/hooks/useThemeTokens.ts
```
import { useTheme } from '@chakra-ui/react';
import { get } from '@chakra-ui/utils';

/**
 * Custom hook to access theme tokens with TypeScript support
 * Provides easy access to colors, spacing, and other theme values
 */
export function useThemeTokens() {
  const theme = useTheme();

  return {
    /**
     * Get a color token from the theme
     * @example getColor('accent.500')
     */
    getColor: (token: string) => get(theme.colors, token),

    /**
     * Get a spacing token from the theme
     * @example getSpace(4) // returns '1rem'
     */
    getSpace: (token: string | number) => get(theme.space, token),

    /**
     * Get a font size token from the theme
     * @example getFontSize('md')
     */
    getFontSize: (token: string) => get(theme.fontSizes, token),

    /**
     * Get a radius token from the theme
     * @example getRadius('md')
     */
    getRadius: (token: string) => get(theme.radii, token),
  };
}

```

## frontend/theme/components/index.ts
```
import { buttonTheme } from './button';
import { cardTheme } from './card';
import { headingTheme } from './heading';
import { textTheme } from './text';
import { recipeTheme } from './recipe';

export const components = {
  Card: cardTheme,
  Button: buttonTheme,
  Text: textTheme,
  Heading: headingTheme,
  Recipe: recipeTheme,
};

```

## frontend/theme/components/recipe-card.ts
```
import type { ComponentStyleConfig } from '@chakra-ui/react';

export const Card: ComponentStyleConfig = {
  variants: {
    elevated: {
      backgroundColor: 'white',
      boxShadow: 'base',
      borderRadius: 'md',
      cursor: 'pointer',
      transition: 'all 0.2s',
      _hover: {
        transform: 'translateY(-2px)',
        boxShadow: 'md',
      },
    },
  },
  defaultProps: {
    variant: 'elevated',
  },
};

```

## frontend/hooks/useRecipeSearch.ts
```
import { api } from '@/utils/api';
import { useQuery } from '@tanstack/react-query';

export function useRecipeSearch(
  query: string,
  options?: {
    protein?: string;
    isDairyFree?: boolean;
    isSoyFree?: boolean;
    isEggFree?: boolean;
    page?: number;
    limit?: number;
  }
) {
  return useQuery({
    queryKey: ['recipes', 'search', query, options],
    queryFn: () => api.recipes.search(query, options),
    enabled: query.length > 0,
    staleTime: 1000 * 60 * 5, // Cache for 5 minutes
  });
}

```

## frontend/hooks/useBreakpointValue.ts
```
import { useBreakpointValue as useChakraBreakpointValue } from '@chakra-ui/react';

type ResponsiveValue<T> = T | Record<string, T> | Array<T | null>;

/**
 * Enhanced version of Chakra's useBreakpointValue with better TypeScript support
 * and fallback values
 */
export function useBreakpointValue<T>(values: ResponsiveValue<T>, defaultValue?: T): T | undefined {
  return useChakraBreakpointValue(values, { fallback: defaultValue });
}

```

## frontend/hooks/useRecipes.ts
```
import type { Recipe } from '@/types/recipe';
import { api } from '@/utils/api';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';

export const recipeKeys = {
  all: ['recipes'] as const,
  lists: () => [...recipeKeys.all, 'list'] as const,
  list: (filters: Record<string, unknown>) => [...recipeKeys.lists(), filters] as const,
  details: () => [...recipeKeys.all, 'detail'] as const,
  detail: (id: number) => [...recipeKeys.details(), id] as const,
};

export function useRecipes(params?: { page?: number; limit?: number }) {
  return useQuery({
    queryKey: recipeKeys.list(params || {}),
    queryFn: () => api.recipes.list(params),
  });
}

export function useRecipe(id: number) {
  return useQuery({
    queryKey: recipeKeys.detail(id),
    queryFn: () => api.recipes.get(id),
  });
}

export function useCreateRecipe() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (recipe: Omit<Recipe, 'id'>) => api.recipes.create(recipe),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: recipeKeys.lists() });
    },
  });
}

export function useUpdateRecipe() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, recipe }: { id: number; recipe: Partial<Recipe> }) =>
      api.recipes.update(id, recipe),
    onSuccess: (_, { id }) => {
      queryClient.invalidateQueries({ queryKey: recipeKeys.detail(id) });
      queryClient.invalidateQueries({ queryKey: recipeKeys.lists() });
    },
  });
}

export function useDeleteRecipe() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (id: number) => api.recipes.delete(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: recipeKeys.lists() });
    },
  });
}

```

## frontend/hooks/useAppState.ts
```
import { router } from '@/router';
import { uiState, useGlobalStore } from '@/stores/globalStore';
import { useCallback } from 'react';
import { useSnapshot } from 'valtio';

export function useAppState() {
  // Get reactive UI state from Valtio
  const ui = useSnapshot(uiState);

  // Get global state and actions from Zustand
  const { search, recipes, actions } = useGlobalStore();

  // Get URL state from TanStack Router
  const searchParams = router.state.search;

  // Computed values
  const isFiltered =
    search.filters.category.length > 0 || search.filters.dietary.length > 0 || search.query !== '';

  // Combined actions
  const viewRecipe = useCallback(
    (recipeId: number) => {
      actions.addRecentlyViewed(recipeId);
      router.navigate({
        to: '/recipe/$recipeId',
        params: { recipeId: recipeId.toString() },
      });
    },
    [actions]
  );

  const toggleTheme = useCallback(() => {
    uiState.theme = uiState.theme === 'light' ? 'dark' : 'light';
  }, []);

  const showToast = useCallback((message: string, type: 'success' | 'error' = 'success') => {
    uiState.toast = { message, type };
    setTimeout(() => {
      uiState.toast = null;
    }, 3000);
  }, []);

  return {
    // State
    ui,
    search,
    recipes,
    searchParams,
    isFiltered,

    // Actions
    ...actions,
    viewRecipe,
    toggleTheme,
    showToast,

    // URL navigation
    navigate: router.navigate,
  };
}

```

## frontend/theme/foundations/spacing.ts
```
// Using a 4-point grid system (multiply by 4 to get pixels)
export const spacing = {
  px: '1px',
  0: '0',
  0.5: '0.125rem',
  1: '0.25rem', // 4px
  1.5: '0.375rem',
  2: '0.5rem', // 8px
  2.5: '0.625rem',
  3: '0.75rem', // 12px
  3.5: '0.875rem',
  4: '1rem', // 16px
  5: '1.25rem', // 20px
  6: '1.5rem', // 24px
  7: '1.75rem', // 28px
  8: '2rem', // 32px
  9: '2.25rem', // 36px
  10: '2.5rem', // 40px
  12: '3rem', // 48px
  14: '3.5rem', // 56px
  16: '4rem', // 64px
  20: '5rem', // 80px
  24: '6rem', // 96px
  28: '7rem', // 112px
  32: '8rem', // 128px
  36: '9rem', // 144px
  40: '10rem', // 160px
  44: '11rem', // 176px
  48: '12rem', // 192px
  52: '13rem', // 208px
  56: '14rem', // 224px
  60: '15rem', // 240px
  64: '16rem', // 256px
  72: '18rem', // 288px
  80: '20rem', // 320px
  96: '24rem', // 384px
};

```

## frontend/theme/foundations/typography.ts
```
export const typography = {
  fonts: {
    heading: `'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif`,
    body: `'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif`,
    mono: `SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace`,
  },
  fontSizes: {
    xs: '0.75rem',
    sm: '0.875rem',
    md: '1rem',
    lg: '1.125rem',
    xl: '1.25rem',
    '2xl': '1.5rem',
    '3xl': '1.875rem',
    '4xl': '2.25rem',
    '5xl': '3rem',
    '6xl': '3.75rem',
    '7xl': '4.5rem',
    '8xl': '6rem',
    '9xl': '8rem',
  },
  fontWeights: {
    hairline: 100,
    thin: 200,
    light: 300,
    normal: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
    extrabold: 800,
    black: 900,
  },
  lineHeights: {
    normal: 'normal',
    none: 1,
    shorter: 1.25,
    short: 1.375,
    base: 1.5,
    tall: 1.625,
    taller: '2',
  },
  letterSpacings: {
    tighter: '-0.05em',
    tight: '-0.025em',
    normal: '0',
    wide: '0.025em',
    wider: '0.05em',
    widest: '0.1em',
  },
};

```

## frontend/theme/foundations/index.ts
```
import { breakpoints } from './breakpoints';
import { colors } from './colors';
import { radii } from './radii';
import { spacing } from './spacing';
import { typography } from './typography';

export const foundations = {
  colors,
  ...typography,
  space: spacing,
  sizes: spacing,
  breakpoints,
  radii,
};

```

## frontend/theme/foundations/breakpoints.ts
```
// Using mobile-first breakpoints
export const breakpoints = {
  sm: '30em', // 480px
  md: '48em', // 768px
  lg: '62em', // 992px
  xl: '80em', // 1280px
  '2xl': '96em', // 1536px
};

```

## frontend/theme/foundations/colors.ts
```
export const colors = {
  brand: {
    50: '#F7FAFC',
    100: '#EDF2F7',
    200: '#E2E8F0',
    300: '#CBD5E0',
    400: '#A0AEC0',
    500: '#718096', // Primary brand color
    600: '#4A5568',
    700: '#2D3748',
    800: '#1A202C',
    900: '#171923',
  },
  accent: {
    50: '#FFF5F5',
    100: '#FED7D7',
    200: '#FEB2B2',
    300: '#FC8181',
    400: '#F56565',
    500: '#E53E3E', // Primary accent color
    600: '#C53030',
    700: '#9B2C2C',
    800: '#822727',
    900: '#63171B',
  },
  success: {
    50: '#F0FFF4',
    100: '#C6F6D5',
    200: '#9AE6B4',
    300: '#68D391',
    400: '#48BB78',
    500: '#38A169', // Primary success color
    600: '#2F855A',
    700: '#276749',
    800: '#22543D',
    900: '#1C4532',
  },
  // Add your custom color palette here
};

```

## frontend/pages/recipes/index.tsx
```
import { PageLayout } from '@/components/layout/PageLayout';
import { RecipeGrid } from '@/components/recipe/RecipeGrid';
import type { Recipe } from '@/types/recipe';

export default function RecipesPage() {
  // Example recipes for testing
  const recipes: Recipe[] = [
    {
      id: 1,
      title: 'Spaghetti Carbonara',
      description: 'Classic Italian pasta dish with eggs and pancetta',
      image_url: 'https://example.com/carbonara.jpg',
      meal_type: 'dinner',
      cooking_method: 'stovetop_cooking',
      prep_time: 15,
      cook_time: 20,
      is_dairy_free: false,
      is_gluten_free: false,
      is_nut_free: true,
      is_egg_free: false,
      is_soy_free: true,
    },
    {
      id: 2,
      title: 'Quinoa Buddha Bowl',
      description:
        'Healthy bowl with quinoa, roasted vegetables, and tahini dressing',
      image_url: 'https://example.com/buddha-bowl.jpg',
      meal_type: 'lunch',
      cooking_method: 'meal_prep',
      prep_time: 20,
      cook_time: 30,
      is_dairy_free: true,
      is_gluten_free: true,
      is_nut_free: false,
      is_egg_free: true,
      is_soy_free: true,
    },
  ];

  return (
    <PageLayout>
      <RecipeGrid
        recipes={recipes}
        onRecipeClick={(recipe) => console.log('Clicked recipe:', recipe.title)}
      />
    </PageLayout>
  );
}

```

## frontend/pages/recipes.tsx
```
import type React from 'react';

import { Container, Typography } from '@mui/material';

import RecipeList from '../components/RecipeList';

const RecipesPage: React.FC = () => {
  return (
    <Container maxWidth="lg">
      <Typography
        variant="h4"
        component="h1"
        gutterBottom
        sx={{ mt: 4, mb: 2 }}
      >
        FPIES-Safe Recipes
      </Typography>
      <RecipeList />
    </Container>
  );
};

export default RecipesPage;

```

## frontend/hooks/api/useIngredients.ts
```
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '../../services/api';
import type { IngredientCreate } from '../../types/api';

// Query keys
export const ingredientKeys = {
  all: ['ingredients'] as const,
  lists: () => [...ingredientKeys.all, 'list'] as const,
  list: (page: number, limit: number) =>
    [...ingredientKeys.lists(), { page, limit }] as const,
  categories: () => [...ingredientKeys.all, 'categories'] as const,
};

export function useIngredients(page = 1, limit = 100) {
  return useQuery({
    queryKey: ingredientKeys.list(page, limit),
    queryFn: () => apiClient.getIngredients(page, limit),
  });
}

export function useIngredientCategories() {
  return useQuery({
    queryKey: ingredientKeys.categories(),
    queryFn: () => apiClient.getIngredientCategories(),
  });
}

export function useCreateIngredient() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (ingredient: IngredientCreate) =>
      apiClient.createIngredient(ingredient),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ingredientKeys.lists() });
    },
  });
}

```

## frontend/hooks/api/useRecipeSearch.ts
```
import { useQuery } from '@tanstack/react-query';
import { apiClient } from '../../services/api';
import type { RecipeSearchFilters } from '../../types/api';

// Query keys
export const recipeSearchKeys = {
  all: ['recipe-search'] as const,
  search: (
    query: string,
    filters?: RecipeSearchFilters,
    page?: number,
    limit?: number
  ) => [...recipeSearchKeys.all, { query, filters, page, limit }] as const,
};

export function useRecipeSearch(
  query: string,
  filters?: RecipeSearchFilters,
  page = 1,
  limit = 20,
  enabled = true
) {
  return useQuery({
    queryKey: recipeSearchKeys.search(query, filters, page, limit),
    queryFn: () => apiClient.searchRecipes(query, filters, page, limit),
    enabled: enabled && !!query,
  });
}

```

## frontend/hooks/api/useRecipes.ts
```
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '../../services/api';
import type { RecipeCreate, RecipeUpdate } from '../../types/api';

// Query keys
export const recipeKeys = {
  all: ['recipes'] as const,
  lists: () => [...recipeKeys.all, 'list'] as const,
  list: (page: number, limit: number) =>
    [...recipeKeys.lists(), { page, limit }] as const,
  details: () => [...recipeKeys.all, 'detail'] as const,
  detail: (id: number) => [...recipeKeys.details(), id] as const,
};

// Hooks
export function useRecipes(page = 1, limit = 20) {
  return useQuery({
    queryKey: recipeKeys.list(page, limit),
    queryFn: () => apiClient.getRecipes(page, limit),
  });
}

export function useRecipe(id: number) {
  return useQuery({
    queryKey: recipeKeys.detail(id),
    queryFn: () => apiClient.getRecipe(id),
    enabled: !!id,
  });
}

export function useCreateRecipe() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (recipe: RecipeCreate) => apiClient.createRecipe(recipe),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: recipeKeys.lists() });
    },
  });
}

export function useUpdateRecipe() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, recipe }: { id: number; recipe: RecipeUpdate }) =>
      apiClient.updateRecipe(id, recipe),
    onSuccess: (_, { id }) => {
      queryClient.invalidateQueries({ queryKey: recipeKeys.detail(id) });
      queryClient.invalidateQueries({ queryKey: recipeKeys.lists() });
    },
  });
}

export function useDeleteRecipe() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (id: number) => apiClient.deleteRecipe(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: recipeKeys.lists() });
    },
  });
}

```

## frontend/package.json
```
{
  "name": "fpies-recipe-platform-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "lint:fix": "next lint --fix",
    "format": "prettier --write \"**/*.{ts,tsx,js,jsx,json,md}\"",
    "format:check": "prettier --check \"**/*.{ts,tsx,js,jsx,json,md}\"",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "test:e2e": "playwright test",
    "test:e2e:ui": "playwright test --ui",
    "storybook": "storybook dev -p 6006",
    "build-storybook": "storybook build",
    "type-check": "tsc --noEmit",
    "validate": "npm run lint && npm run format:check && npm run type-check"
  },
  "dependencies": {
    "@chakra-ui/icons": "^2.2.4",
    "@chakra-ui/react": "^3.7.0",
    "@chakra-ui/theme": "^3.4.6",
    "@chakra-ui/theme-tools": "^2.2.6",
    "@chakra-ui/utils": "^2.2.2",
    "@emotion/react": "^11.14.0",
    "@emotion/styled": "^11.14.0",
    "@tanstack/react-query": "^5.66.0",
    "@tanstack/react-query-devtools": "^5.66.0",
    "@tanstack/router": "^0.0.1-beta.53",
    "@tanstack/router-devtools": "^1.99.6",
    "@tanstack/router-vite-plugin": "^1.99.6",
    "clsx": "^2.1.1",
    "framer-motion": "^12.1.0",
    "immer": "^10.1.1",
    "msw": "^2.7.0",
    "next": "^15.1.6",
    "next-mdx-remote": "^5.0.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-icons": "^5.4.0",
    "react-syntax-highlighter": "^15.6.1",
    "valtio": "^2.1.3",
    "zod": "^3.24.1",
    "zustand": "^5.0.3"
  },
  "devDependencies": {
    "@biomejs/biome": "^1.9.4",
    "@playwright/test": "^1.50.1",
    "@storybook/addon-essentials": "^8.5.3",
    "@storybook/blocks": "^8.5.3",
    "@storybook/nextjs": "^8.5.3",
    "@storybook/react": "^8.5.3",
    "@storybook/testing-library": "^0.2.2",
    "@testing-library/dom": "^10.4.0",
    "@testing-library/jest-dom": "^6.6.3",
    "@testing-library/react": "^16.2.0",
    "@testing-library/user-event": "^14.6.1",
    "@types/jest": "^29.5.14",
    "@types/node": "^22",
    "@types/react": "^19.0.8",
    "@types/react-dom": "^19.0.3",
    "@typescript-eslint/eslint-plugin": "^8.23.0",
    "@typescript-eslint/parser": "^8.23.0",
    "axios": "^1.7.9",
    "eslint-config-next": "^15.1.6",
    "eslint-config-prettier": "^10.0.1",
    "eslint-import-resolver-typescript": "^3.7.0",
    "eslint-plugin-import": "^2.31.0",
    "eslint-plugin-jest": "^28.11.0",
    "eslint-plugin-jsx-a11y": "^6.10.2",
    "eslint-plugin-prettier": "^5.2.3",
    "eslint-plugin-react": "^7.37.4",
    "eslint-plugin-react-hooks": "^5.1.0",
    "eslint-plugin-testing-library": "^7.1.1",
    "jest": "^29.7.0",
    "jest-environment-jsdom": "^29.7.0",
    "npm-check-updates": "^17.1.14",
    "prettier": "^3.4.2",
    "ts-jest": "^29.2.5",
    "typescript": "^5"
  }
}

```

## frontend/jest.setup.ts
```
// Add Jest DOM matchers
import '@testing-library/jest-dom';
import 'whatwg-fetch';
import { server } from './mocks/server';

// Establish API mocking before all tests
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));

// Reset any request handlers that we may add during the tests,
// so they don't affect other tests.
afterEach(() => server.resetHandlers());

// Clean up after the tests are finished.
afterAll(() => server.close());

// Mock IntersectionObserver
class MockIntersectionObserver {
  observe = jest.fn();
  disconnect = jest.fn();
  unobserve = jest.fn();
}

Object.defineProperty(window, 'IntersectionObserver', {
  writable: true,
  configurable: true,
  value: MockIntersectionObserver,
});

// Mock matchMedia
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: jest.fn().mockImplementation(query => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    dispatchEvent: jest.fn(),
  })),
});

```

## frontend/components/api/ApiConfigPanel.tsx
```
import type React from 'react';
import { useState } from 'react';

import type { ApiParameterDocs, ApiSource } from '../../types/api';

type ParamValue = string | number | boolean | string[];
type ParamRecord = Record<string, ParamValue>;

interface ApiConfigPanelProps {
  source: ApiSource;
  currentParams: ParamRecord;
  onUpdateParams: (params: ParamRecord) => void;
  onSaveDefaults: (params: ParamRecord) => void;
}

const ConfigInput: React.FC<{
  param: ApiParameterDocs;
  value: ParamValue;
  onChange: (value: ParamValue) => void;
}> = ({ param, value, onChange }) => {
  if (param.type === 'array' && param.options) {
    return (
      <select
        multiple
        value={(value as string[]) || []}
        onChange={(e) => {
          const values = Array.from(e.target.selectedOptions).map(
            (opt) => opt.value
          );
          onChange(values);
        }}
        className="w-full p-2 border rounded"
      >
        {param.options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
    );
  }

  if (param.type === 'boolean') {
    return (
      <input
        id={`param-${param.name}`}
        type="checkbox"
        checked={Boolean(value)}
        onChange={(e) => onChange(e.target.checked)}
        className="rounded border-gray-300"
      />
    );
  }

  if (param.options) {
    return (
      <select
        id={`param-${param.name}`}
        value={String(value) || ''}
        onChange={(e) => onChange(e.target.value)}
        className="w-full p-2 border rounded"
      >
        <option value="">Select...</option>
        {param.options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
    );
  }

  return (
    <input
      id={`param-${param.name}`}
      type={param.type === 'number' ? 'number' : 'text'}
      value={value === undefined ? '' : String(value)}
      onChange={(e) => {
        const newValue =
          param.type === 'number' ? Number(e.target.value) : e.target.value;
        onChange(newValue);
      }}
      className="w-full p-2 border rounded"
      placeholder={`Enter ${param.name}...`}
    />
  );
};

export const ApiConfigPanel: React.FC<ApiConfigPanelProps> = ({
  source,
  currentParams,
  onUpdateParams,
  onSaveDefaults,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [params, setParams] = useState<ParamRecord>(currentParams);

  const handleParamChange = (param: ApiParameterDocs, value: ParamValue) => {
    const newParams = { ...params, [param.name]: value };
    setParams(newParams);
    onUpdateParams(newParams);
  };

  const handleSaveDefaults = () => {
    onSaveDefaults(params);
  };

  if (!isOpen) {
    return (
      <button
        type="button"
        onClick={() => setIsOpen(true)}
        className="fixed bottom-4 right-4 bg-blue-500 text-white p-2 rounded-full shadow-lg hover:bg-blue-600"
        title="Configure API Parameters"
      >
        <svg
          className="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          aria-labelledby="configIconTitle"
        >
          <title id="configIconTitle">Configure API Parameters</title>
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
          />
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
          />
        </svg>
      </button>
    );
  }

  return (
    <div className="fixed bottom-4 right-4 bg-white p-4 rounded-lg shadow-xl border w-96">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-lg font-semibold">{source.name} Configuration</h3>
        <button
          type="button"
          onClick={() => setIsOpen(false)}
          className="text-gray-500 hover:text-gray-700"
        >
          ×
        </button>
      </div>

      <div className="space-y-4 max-h-96 overflow-y-auto">
        {source.parameterDocs.map((param) => (
          <div key={param.name} className="space-y-1">
            <label
              htmlFor={`param-${param.name}`}
              className="block text-sm font-medium"
            >
              {param.name}
              {param.required && <span className="text-red-500">*</span>}
            </label>
            <div className="text-xs text-gray-500 mb-1">
              {param.description}
            </div>
            <ConfigInput
              param={param}
              value={params[param.name] || ''}
              onChange={(value) => handleParamChange(param, value)}
            />
          </div>
        ))}
      </div>

      <div className="mt-4 flex justify-end space-x-2">
        <button
          type="button"
          onClick={handleSaveDefaults}
          className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
        >
          Save as Defaults
        </button>
      </div>
    </div>
  );
};

```

## frontend/components/meal/MealPlanner.tsx
```
import React, { useState } from 'react';

import { addDays, format, startOfWeek } from 'date-fns';

import { useMealPlanStore } from '../../stores/mealPlanStore';
import { useRecipeStore } from '../../stores/recipeStore';

import type { MealType, Recipe } from '../../types/recipe';

const MEAL_TYPES: MealType[] = ['breakfast', 'lunch', 'dinner', 'snack'];

export const MealPlanner: React.FC = () => {
  const { currentPlan, addMeal, removeMeal, createPlan, loading, error } =
    useMealPlanStore();
  const { recipes } = useRecipeStore();
  const [selectedRecipe, setSelectedRecipe] = useState<Recipe | null>(null);
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);
  const [selectedMealType, setSelectedMealType] = useState<MealType>('dinner');

  // Initialize a week-long meal plan if none exists
  React.useEffect(() => {
    if (!currentPlan) {
      const start = startOfWeek(new Date());
      const end = addDays(start, 6);
      createPlan(start.toISOString(), end.toISOString());
    }
  }, [currentPlan, createPlan]);

  const handleAddMeal = () => {
    if (selectedRecipe && selectedDate) {
      addMeal({
        recipeId: selectedRecipe.id.toString(),
        date: selectedDate.toISOString(),
        mealType: selectedMealType,
        servings: 4,
      });
      setSelectedRecipe(null);
      setSelectedDate(null);
    }
  };

  const getDayMeals = (date: Date) => {
    if (!currentPlan) {
      return [];
    }
    return currentPlan.meals.filter(
      (meal) =>
        format(new Date(meal.date), 'yyyy-MM-dd') === format(date, 'yyyy-MM-dd')
    );
  };

  const renderWeek = () => {
    if (!currentPlan) {
      return null;
    }

    const start = new Date(currentPlan.startDate);
    const days = Array.from({ length: 7 }, (_, i) => addDays(start, i));

    return (
      <div className="grid grid-cols-7 gap-4">
        {days.map((day) => (
          <div
            key={day.toISOString()}
            className="border rounded-lg p-4 min-h-[200px]"
          >
            <div className="font-semibold mb-2">
              {format(day, 'EEEE')}
              <br />
              {format(day, 'MMM d')}
            </div>

            {MEAL_TYPES.map((mealType) => {
              const meals = getDayMeals(day).filter(
                (m) => m.mealType === mealType
              );
              if (meals.length === 0) {
                return null;
              }

              return (
                <div key={mealType} className="mb-2">
                  <div className="text-sm text-gray-600 capitalize">
                    {mealType}
                  </div>
                  {meals.map((meal) => {
                    const recipe = recipes.find(
                      (r) => r.id.toString() === meal.recipeId
                    );
                    if (!recipe) {
                      return null;
                    }

                    return (
                      <div
                        key={meal.id}
                        className="text-sm p-2 bg-blue-50 rounded mt-1 flex justify-between items-center"
                      >
                        <span>{recipe.title}</span>
                        <button
                          type="button"
                          onClick={() => removeMeal(meal.id)}
                          className="text-red-500 hover:text-red-700"
                        >
                          ×
                        </button>
                      </div>
                    );
                  })}
                </div>
              );
            })}

            <button
              type="button"
              onClick={() => {
                setSelectedDate(day);
                setSelectedMealType('dinner');
              }}
              className="mt-2 text-sm text-blue-500 hover:text-blue-700"
            >
              + Add Meal
            </button>
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold">Meal Planner</h2>

      {/* Add Meal Form */}
      {selectedDate && (
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="font-semibold mb-4">
            Add Meal for {format(selectedDate, 'EEEE, MMMM d')}
          </h3>

          <div className="space-y-4">
            <div>
              <label
                htmlFor="mealType"
                className="block text-sm font-medium mb-1"
              >
                Meal Type
              </label>
              <select
                id="mealType"
                value={selectedMealType}
                onChange={(e) =>
                  setSelectedMealType(e.target.value as MealType)
                }
                className="w-full p-2 border rounded"
              >
                {MEAL_TYPES.map((type) => (
                  <option key={type} value={type}>
                    {type.charAt(0).toUpperCase() + type.slice(1)}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label
                htmlFor="recipe"
                className="block text-sm font-medium mb-1"
              >
                Recipe
              </label>
              <select
                id="recipe"
                value={selectedRecipe?.id || ''}
                onChange={(e) => {
                  const recipe = recipes.find(
                    (r) => r.id.toString() === e.target.value
                  );
                  setSelectedRecipe(recipe || null);
                }}
                className="w-full p-2 border rounded"
              >
                <option value="">Select a recipe...</option>
                {recipes.map((recipe) => (
                  <option key={recipe.id} value={recipe.id}>
                    {recipe.title}
                  </option>
                ))}
              </select>
            </div>

            <div className="flex justify-end gap-2">
              <button
                type="button"
                onClick={() => setSelectedDate(null)}
                className="px-4 py-2 text-gray-600 hover:text-gray-800"
              >
                Cancel
              </button>
              <button
                type="button"
                onClick={handleAddMeal}
                disabled={!selectedRecipe}
                className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:opacity-50"
              >
                Add to Plan
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Error Message */}
      {error && (
        <div className="p-4 bg-red-100 text-red-700 rounded-lg">{error}</div>
      )}

      {/* Weekly Plan */}
      {loading ? (
        <div className="flex justify-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500" />
        </div>
      ) : (
        renderWeek()
      )}
    </div>
  );
};

```

## frontend/components/RecipeList.tsx
```
import type React from 'react';
import { useEffect, useState } from 'react';

import { Box, Container, Grid, Stack, Spinner } from '@chakra-ui/react';

import { RecipeCard } from './recipe/RecipeCard';
import { RecipeFilterComponent } from './recipe/RecipeFilters';

import type { Recipe, RecipeFilters } from '../types/recipe';

const RecipeList: React.FC = () => {
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [filters, setFilters] = useState<RecipeFilters>({
    search_query: '',
    meal_type: '',
    cooking_method: '',
    is_dairy_free: false,
    is_soy_free: false,
    is_gluten_free: false,
    is_nut_free: false,
    is_egg_free: false,
    is_collection: false,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRecipes = async () => {
      setLoading(true);
      try {
        const queryParams = new URLSearchParams();

        if (filters.meal_type) {
          queryParams.append('meal_type', filters.meal_type);
        }
        if (filters.cooking_method) {
          queryParams.append('cooking_method', filters.cooking_method);
        }
        if (filters.search_query) {
          queryParams.append('q', filters.search_query);
        }
        if (filters.is_collection !== undefined) {
          queryParams.append('is_collection', filters.is_collection.toString());
        }

        const response = await fetch(`/api/recipes?${queryParams.toString()}`);
        const data = await response.json();
        setRecipes(data);
      } catch (error) {
        console.error('Failed to fetch recipes:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchRecipes();
  }, [filters]);

  const handleFilterChange = (
    key: keyof RecipeFilters,
    value: string | boolean
  ) => {
    setFilters((prev) => ({ ...prev, [key]: value }));
  };

  const filterRecipes = (recipes: Recipe[]): Recipe[] => {
    return recipes.filter((recipe) => {
      // Add allergen filters
      const allergens: string[] = [];
      if (filters.is_dairy_free) {
        allergens.push('dairy');
      }
      if (filters.is_soy_free) {
        allergens.push('soy');
      }
      if (filters.is_gluten_free) {
        allergens.push('gluten');
      }
      if (filters.is_nut_free) {
        allergens.push('nuts');
      }
      if (filters.is_egg_free) {
        allergens.push('eggs');
      }

      return allergens.every(
        (allergen) => !recipe.allergens.includes(allergen)
      );
    });
  };

  const filteredRecipes = filterRecipes(recipes);

  return (
    <Container maxW="container.xl" p={4}>
      <Stack spacing={4}>
        <RecipeFilterComponent
          filters={filters}
          onFilterChange={handleFilterChange}
        />

        {loading ? (
          <Box textAlign="center" py={8}>
            <Spinner size="xl" />
          </Box>
        ) : (
          <Grid
            templateColumns={{
              base: '1fr',
              sm: 'repeat(2, 1fr)',
              lg: 'repeat(3, 1fr)',
            }}
            gap={4}
          >
            {filteredRecipes.map((recipe) => (
              <RecipeCard key={recipe.id} recipe={recipe} />
            ))}
          </Grid>
        )}
      </Stack>
    </Container>
  );
};

export default RecipeList;

```

## frontend/components/family/FamilyProfileManager.tsx
```
import type React from 'react';
import { useState } from 'react';

import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Heading,
  Input,
  Tag,
  TagCloseButton,
  TagLabel,
  Text,
  VStack,
  Wrap,
  WrapItem,
  useToast,
} from '@chakra-ui/react';

import { useFamilyProfile } from '@/stores/familyProfileStore';

export function FamilyProfileManager() {
  const toast = useToast();
  const { members, addMember, updateMember } = useFamilyProfile();
  const [newAllergy, setNewAllergy] = useState('');
  const [newTrigger, setNewTrigger] = useState('');
  const [name, setName] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name) {
      toast({
        title: 'Name required',
        status: 'error',
        duration: 2000,
      });
      return;
    }

    addMember({
      name,
      allergies: [],
      fpiesTriggers: [],
      safeSubstitutes: {},
    });

    setName('');
    toast({
      title: 'Family member added',
      status: 'success',
      duration: 2000,
    });
  };

  const addAllergy = (memberId: string) => {
    if (!newAllergy) {
      return;
    }
    const member = members.find((m) => m.id === memberId);
    if (member && !member.allergies.includes(newAllergy)) {
      updateMember(memberId, {
        allergies: [...member.allergies, newAllergy],
      });
      setNewAllergy('');
    }
  };

  const addTrigger = (memberId: string) => {
    if (!newTrigger) {
      return;
    }
    const member = members.find((m) => m.id === memberId);
    if (member && !member.fpiesTriggers.includes(newTrigger)) {
      updateMember(memberId, {
        fpiesTriggers: [...member.fpiesTriggers, newTrigger],
      });
      setNewTrigger('');
    }
  };

  const removeAllergy = (memberId: string, allergy: string) => {
    const member = members.find((m) => m.id === memberId);
    if (member) {
      updateMember(memberId, {
        allergies: member.allergies.filter((a) => a !== allergy),
      });
    }
  };

  const removeTrigger = (memberId: string, trigger: string) => {
    const member = members.find((m) => m.id === memberId);
    if (member) {
      updateMember(memberId, {
        fpiesTriggers: member.fpiesTriggers.filter((t) => t !== trigger),
      });
    }
  };

  return (
    <Box p={6}>
      <VStack spacing={8} align="stretch">
        <Box>
          <Heading size="md" mb={4}>
            Add Family Member
          </Heading>
          <form onSubmit={handleSubmit}>
            <FormControl>
              <FormLabel>Name</FormLabel>
              <Input
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Enter name"
                mb={4}
              />
              <Button type="submit" colorScheme="blue">
                Add Family Member
              </Button>
            </FormControl>
          </form>
        </Box>

        {members.map((member) => (
          <Box key={member.id} p={4} borderWidth={1} borderRadius="md">
            <Heading size="md" mb={4}>
              {member.name}'s Profile
            </Heading>

            <VStack align="stretch" spacing={4}>
              {/* Allergies Section */}
              <Box>
                <Text fontWeight="bold" mb={2}>
                  Allergies
                </Text>
                <Wrap mb={2}>
                  {member.allergies.map((allergy) => (
                    <WrapItem key={allergy}>
                      <Tag size="md" colorScheme="red" borderRadius="full">
                        <TagLabel>{allergy}</TagLabel>
                        <TagCloseButton
                          onClick={() => removeAllergy(member.id, allergy)}
                        />
                      </Tag>
                    </WrapItem>
                  ))}
                </Wrap>
                <FormControl display="flex">
                  <Input
                    value={newAllergy}
                    onChange={(e) => setNewAllergy(e.target.value)}
                    placeholder="Add allergy"
                    size="sm"
                    mr={2}
                  />
                  <Button
                    size="sm"
                    onClick={() => addAllergy(member.id)}
                    colorScheme="blue"
                  >
                    Add
                  </Button>
                </FormControl>
              </Box>

              {/* FPIES Triggers Section */}
              <Box>
                <Text fontWeight="bold" mb={2}>
                  FPIES Triggers
                </Text>
                <Wrap mb={2}>
                  {member.fpiesTriggers.map((trigger) => (
                    <WrapItem key={trigger}>
                      <Tag size="md" colorScheme="orange" borderRadius="full">
                        <TagLabel>{trigger}</TagLabel>
                        <TagCloseButton
                          onClick={() => removeTrigger(member.id, trigger)}
                        />
                      </Tag>
                    </WrapItem>
                  ))}
                </Wrap>
                <FormControl display="flex">
                  <Input
                    value={newTrigger}
                    onChange={(e) => setNewTrigger(e.target.value)}
                    placeholder="Add FPIES trigger"
                    size="sm"
                    mr={2}
                  />
                  <Button
                    size="sm"
                    onClick={() => addTrigger(member.id)}
                    colorScheme="blue"
                  >
                    Add
                  </Button>
                </FormControl>
              </Box>
            </VStack>
          </Box>
        ))}
      </VStack>
    </Box>
  );
}

```

## frontend/components/recipe/RecipeActions.tsx
```
import React from 'react';

import { Button, HStack, Tooltip, Box, Text, useToast } from '@chakra-ui/react';
import { FaHeart, FaShare } from 'react-icons/fa';

import { useRecipeStore } from '../../stores/recipeStore';
import { api } from '../../utils/api';

interface Props {
  recipeId: number;
  isFavorite: boolean;
}

export const RecipeActions: React.FC<Props> = ({ recipeId, isFavorite }) => {
  const { toggleFavorite } = useRecipeStore();
  const [isSharing, setIsSharing] = React.useState(false);
  const [shareUrl, setShareUrl] = React.useState<string>();
  const toast = useToast();

  const handleFavorite = async () => {
    await toggleFavorite(recipeId);
  };

  const handleShare = async () => {
    try {
      setIsSharing(true);
      const response = await api.recipes.share(recipeId);
      setShareUrl(response.data.url);

      await navigator.clipboard.writeText(response.data.url);

      toast({
        title: 'Recipe link copied!',
        description: 'The recipe URL has been copied to your clipboard.',
        status: 'success',
        duration: 3000,
        isClosable: true,
      });
    } catch (error) {
      console.error('Failed to share recipe:', error);
      toast({
        title: 'Failed to share recipe',
        description: 'An error occurred while trying to share the recipe.',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    } finally {
      setIsSharing(false);
    }
  };

  return (
    <>
      <HStack justify="space-between">
        <HStack>
          <Button
            leftIcon={<FaHeart />}
            variant={isFavorite ? 'solid' : 'outline'}
            colorScheme={isFavorite ? 'red' : 'gray'}
            onClick={handleFavorite}
          >
            Favorite
          </Button>
          <Tooltip
            label={shareUrl ? 'Click to copy link again' : 'Share recipe'}
          >
            <Button
              leftIcon={<FaShare />}
              onClick={handleShare}
              isLoading={isSharing}
              colorScheme={shareUrl ? 'green' : 'gray'}
            >
              {shareUrl ? 'Shared' : 'Share'}
            </Button>
          </Tooltip>
        </HStack>
      </HStack>

      {shareUrl && (
        <Box p={2} bg="gray.50" borderRadius="md">
          <Text fontSize="sm" color="gray.600">
            Shared URL: {shareUrl}
          </Text>
        </Box>
      )}
    </>
  );
};

```

## frontend/components/recipe/RecipeCardSkeleton.tsx
```
import type { FC } from 'react';

import {
  Box,
  Card,
  CardBody,
  Skeleton,
  SkeletonText,
  VStack,
} from '@chakra-ui/react';

/**
 * RecipeCardSkeleton displays a loading state for recipe cards
 * matching the layout of the actual RecipeCard component
 */
export const RecipeCardSkeleton: FC = () => {
  return (
    <Card variant="elevated" shadow="md">
      <CardBody>
        <VStack spacing={4} align="stretch">
          <Skeleton height="200px" borderRadius="lg" />
          <SkeletonText noOfLines={2} spacing={2} skeletonHeight={6} />
          <Box pt={2}>
            <Skeleton height="24px" width="120px" />
          </Box>
          <SkeletonText noOfLines={2} spacing={2} />
        </VStack>
      </CardBody>
    </Card>
  );
};

```

## frontend/components/recipe/RecipeFilters.tsx
```
import type { ChangeEvent, FC } from 'react';

import { Search2Icon } from '@chakra-ui/icons';
import {
  Box,
  Card,
  CardBody,
  Checkbox,
  CheckboxGroup,
  FormControl,
  FormLabel,
  Heading,
  HStack,
  Input,
  InputGroup,
  InputLeftElement,
  Select,
  Stack,
  Text,
  useStyleConfig,
  VStack,
} from '@chakra-ui/react';

import type {
  CookingMethod,
  MealType,
  RecipeFilters,
} from '../../types/recipe';

interface Props {
  filters: RecipeFilters;
  onFilterChange: (key: keyof RecipeFilters, value: string | boolean) => void;
}

const mealTypes: MealType[] = [
  'breakfast',
  'lunch',
  'dinner',
  'dessert',
  'snack',
  'other',
];
const cookingMethods: CookingMethod[] = [
  'bake',
  'stovetop',
  'grill',
  'slow_cooker',
  'instant_pot',
  'air_fryer',
  'refrigerate',
  'freeze',
];

/**
 * RecipeFilterComponent component handles all filtering options for recipes
 * including search, meal type, cooking method, and dietary restrictions.
 */
export const RecipeFilterComponent: FC<Props> = ({
  filters,
  onFilterChange,
}) => {
  const styles = useStyleConfig('Recipe');

  return (
    <Card variant="elevated" shadow="md">
      <CardBody>
        <VStack spacing={6} align="stretch">
          <Box>
            <Heading size="md" mb={4}>
              Filters
            </Heading>
            <HStack spacing={4}>
              <InputGroup>
                <InputLeftElement pointerEvents="none">
                  <Search2Icon color="gray.400" />
                </InputLeftElement>
                <Input
                  value={filters.search_query ?? ''}
                  onChange={(e: ChangeEvent<HTMLInputElement>) =>
                    onFilterChange('search_query', e.target.value)
                  }
                  placeholder="Search recipes..."
                  variant="filled"
                  aria-label="Search recipes"
                />
              </InputGroup>
              <FormControl>
                <FormLabel htmlFor="meal-type" fontWeight="medium">
                  Meal Type
                </FormLabel>
                <Select
                  id="meal-type"
                  value={filters.meal_type ?? ''}
                  onChange={(e: ChangeEvent<HTMLSelectElement>) =>
                    onFilterChange('meal_type', e.target.value)
                  }
                  placeholder="Select meal type"
                  variant="filled"
                >
                  <option value="">All</option>
                  {mealTypes.map((type) => (
                    <option key={type} value={type}>
                      {type.charAt(0).toUpperCase() + type.slice(1)}
                    </option>
                  ))}
                </Select>
              </FormControl>
              <FormControl>
                <FormLabel htmlFor="cooking-method" fontWeight="medium">
                  Cooking Method
                </FormLabel>
                <Select
                  id="cooking-method"
                  value={filters.cooking_method ?? ''}
                  onChange={(e: ChangeEvent<HTMLSelectElement>) =>
                    onFilterChange('cooking_method', e.target.value)
                  }
                  placeholder="Select cooking method"
                  variant="filled"
                >
                  <option value="">All</option>
                  {cookingMethods.map((method) => (
                    <option key={method} value={method}>
                      {method
                        .split('_')
                        .map(
                          (word) => word.charAt(0).toUpperCase() + word.slice(1)
                        )
                        .join(' ')}
                    </option>
                  ))}
                </Select>
              </FormControl>
            </HStack>
          </Box>

          <Box>
            <Text fontWeight="medium" mb={3}>
              Dietary Restrictions
            </Text>
            <Stack spacing={3}>
              <CheckboxGroup>
                <VStack align="start" spacing={2}>
                  {[
                    { key: 'is_dairy_free', label: 'Dairy Free' },
                    { key: 'is_soy_free', label: 'Soy Free' },
                    { key: 'is_gluten_free', label: 'Gluten Free' },
                    { key: 'is_nut_free', label: 'Nut Free' },
                    { key: 'is_egg_free', label: 'Egg Free' },
                    { key: 'is_fpies_friendly', label: 'FPIES Friendly' },
                  ].map(({ key, label }) => (
                    <Checkbox
                      key={key}
                      isChecked={filters[key as keyof RecipeFilters] ?? false}
                      onChange={(e: ChangeEvent<HTMLInputElement>) =>
                        onFilterChange(
                          key as keyof RecipeFilters,
                          e.target.checked
                        )
                      }
                      colorScheme="green"
                    >
                      {label}
                    </Checkbox>
                  ))}
                  <Checkbox
                    isChecked={filters.is_collection ?? false}
                    onChange={(e: ChangeEvent<HTMLInputElement>) =>
                      onFilterChange('is_collection', e.target.checked)
                    }
                    colorScheme="purple"
                  >
                    Collections Only
                  </Checkbox>
                </VStack>
              </CheckboxGroup>
            </Stack>
          </Box>
        </VStack>
      </CardBody>
    </Card>
  );
};

```

## frontend/components/recipe/RecipeMetadata.tsx
```
import { HStack, Text } from '@chakra-ui/react';

import type { Recipe } from '../../types/recipe';

interface Props {
  recipe: Pick<Recipe, 'prep_time' | 'cook_time' | 'servings'>;
  showServings?: boolean;
}

export const RecipeMetadata: React.FC<Props> = ({
  recipe,
  showServings = true,
}) => {
  const { prep_time, cook_time, servings } = recipe;

  return (
    <HStack spacing={4}>
      {(prep_time > 0 || cook_time > 0) && (
        <HStack>
          {prep_time > 0 && <Text>Prep: {prep_time}m</Text>}
          {prep_time > 0 && cook_time > 0 && <Text>•</Text>}
          {cook_time > 0 && <Text>Cook: {cook_time}m</Text>}
        </HStack>
      )}
      {showServings && servings > 0 && (
        <HStack>
          <Text>{servings} servings</Text>
        </HStack>
      )}
    </HStack>
  );
};

```

## frontend/components/recipe/RecipeAllergenBadges.tsx
```
import { Badge, HStack } from '@chakra-ui/react';

import type { Recipe } from '../../types/recipe';

interface Props {
  recipe: Pick<
    Recipe,
    | 'is_dairy_free'
    | 'is_soy_free'
    | 'is_gluten_free'
    | 'is_nut_free'
    | 'is_egg_free'
  >;
}

export const RecipeAllergenBadges: React.FC<Props> = ({ recipe }) => {
  const {
    is_dairy_free,
    is_soy_free,
    is_gluten_free,
    is_nut_free,
    is_egg_free,
  } = recipe;

  return (
    <HStack spacing={2} wrap="wrap">
      {is_dairy_free && <Badge colorScheme="green">Dairy Free</Badge>}
      {is_soy_free && <Badge colorScheme="green">Soy Free</Badge>}
      {is_gluten_free && <Badge colorScheme="green">Gluten Free</Badge>}
      {is_nut_free && <Badge colorScheme="green">Nut Free</Badge>}
      {is_egg_free && <Badge colorScheme="green">Egg Free</Badge>}
    </HStack>
  );
};

```

## frontend/components/recipe/RecipeDetail.tsx
```
import React, { type JSX } from 'react';

import {
  Heading,
  Image,
  ListItem,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalHeader,
  ModalOverlay,
  OrderedList,
  UnorderedList,
  VStack,
} from '@chakra-ui/react';

import { RecipeActions } from './RecipeActions';
import { RecipeAllergenBadges } from './RecipeAllergenBadges';
import { RecipeMetadata } from './RecipeMetadata';

import type { Recipe } from '../../types/recipe';

interface Props {
  /**
   * The recipe object containing details about the recipe.
   */
  recipe: Recipe;

  /**
   * Callback function that is invoked to close the recipe detail view.
   * @returns {void}
   */
  onClose: () => void;
}

/**
 * A React component that displays a recipe's details in a modal.
 *
 * @param {Props} props - The component props.
 * @param {Recipe} props.recipe - The recipe object containing details about the recipe.
 * @param {() => void} props.onClose - The callback function that is invoked to close the recipe detail view.
 * @returns {JSX.Element} - The rendered component.
 */
export const RecipeDetail: React.FC<Props> = ({
  recipe,
  onClose,
}: Props): JSX.Element => {
  return (
    <Modal isOpen onClose={onClose} size="xl">
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>
          {recipe.title}
          <ModalCloseButton />
        </ModalHeader>
        <ModalBody>
          <VStack align="stretch" spacing={4}>
            {recipe.image_url && (
              <Image
                src={recipe.image_url}
                alt={recipe.title}
                borderRadius="lg"
                objectFit="cover"
                height={256}
              />
            )}

            <RecipeActions
              recipeId={recipe.id}
              isFavorite={Boolean(recipe.favorite)}
            />
            <RecipeMetadata recipe={recipe} />
            <RecipeAllergenBadges recipe={recipe} />

            {/* Ingredients */}
            <VStack align="stretch">
              <Heading as="h3" size="lg" mb={2}>
                Ingredients
              </Heading>
              <UnorderedList listStyleType="disc">
                {recipe.ingredients.map((ingredient: string) => (
                  <ListItem key={ingredient}>{ingredient}</ListItem>
                ))}
              </UnorderedList>
            </VStack>

            {/* Instructions */}
            <VStack align="stretch">
              <Heading as="h3" size="lg" mb={2}>
                Instructions
              </Heading>
              <OrderedList listStyleType="decimal">
                {recipe.instructions.map((instruction: string) => (
                  <ListItem key={instruction}>{instruction}</ListItem>
                ))}
              </OrderedList>
            </VStack>
          </VStack>
        </ModalBody>
      </ModalContent>
    </Modal>
  );
};

```

## frontend/components/recipe/RecipeGrid.tsx
```
import { SimpleGrid } from '@chakra-ui/react';

import { RecipeCard } from './RecipeCard';

import type { Recipe } from '../../types/recipe';

interface RecipeGridProps {
  recipes: Recipe[];
  onRecipeClick?: (recipe: Recipe) => void;
}

/**
 * RecipeGrid displays a responsive grid of RecipeCards
 */
export const RecipeGrid = ({ recipes, onRecipeClick }: RecipeGridProps) => (
  <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }}>
    {recipes.map((recipe) => (
      <RecipeCard
        key={recipe.id}
        recipe={recipe}
        onClick={() => onRecipeClick?.(recipe)}
      />
    ))}
  </SimpleGrid>
);

```

## frontend/components/recipe/RecipeCard.tsx
```
import { Box, Text, VStack } from '@chakra-ui/react';

import { RecipeAllergenBadges } from './RecipeAllergenBadges';
import { RecipeMetadata } from './RecipeMetadata';

import type { Recipe } from '../../types/recipe';

/**
 * RecipeCard displays a single recipe in a card format
 * with image, title, cooking info, and dietary restrictions.
 */
interface RecipeCardProps {
  recipe: Recipe;
  onClick?: () => void;
}

export const RecipeCard: React.FC<RecipeCardProps> = ({ recipe, onClick }) => {
  const {
    title,
    description,
    meal_type,
    cooking_method = 'other',
    image_url,
  } = recipe;

  return (
    <Box
      onClick={onClick}
      borderWidth="1px"
      borderRadius="lg"
      p={4}
      cursor="pointer"
      _hover={{ shadow: 'md' }}
      role="article"
    >
      <VStack align="stretch" spacing={4}>
        {image_url && (
          <Box
            height="200px"
            backgroundImage={`url(${image_url})`}
            backgroundSize="cover"
            backgroundPosition="center"
            borderRadius="md"
          />
        )}
        <Text fontSize="xl" fontWeight="bold">
          {title}
        </Text>
        <Text color="gray.600">{description}</Text>
        <Text>
          {meal_type} •{' '}
          {cooking_method
            .split('_')
            .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ')}
        </Text>
        <RecipeMetadata recipe={recipe} showServings={false} />
        <RecipeAllergenBadges recipe={recipe} />
      </VStack>
    </Box>
  );
};

```

## frontend/components/recipe/RecipeSearch.tsx
```
import type React from 'react';
import { useCallback, useState } from 'react';

import debounce from 'lodash/debounce';

import { useFamilyProfileStore } from '../../stores/familyProfileStore';
import { useRecipeStore } from '../../stores/recipeStore';

import type { SearchFilters } from '../../types';

export const RecipeSearch: React.FC = () => {
  const [query, setQuery] = useState('');
  const { profile } = useFamilyProfileStore();
  const { searchRecipes, recipes, loading, error, filters, setFilters } =
    useRecipeStore();

  // Debounced search function
  const debouncedSearch = useCallback(
    debounce((searchQuery: string, searchFilters: SearchFilters) => {
      searchRecipes(searchQuery, searchFilters);
    }, 300),
    []
  );

  // Handle search input
  const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newQuery = e.target.value;
    setQuery(newQuery);

    // Auto-apply family allergen filters
    const searchFilters: SearchFilters = {
      ...filters,
      isDairyFree: profile?.isDairyFree || false,
      isEggFree: profile?.isEggFree || false,
      isSoyFree: profile?.isSoyFree || false,
    };

    debouncedSearch(newQuery, searchFilters);
  };

  // Handle filter changes
  const handleFilterChange = (filterKey: keyof SearchFilters) => {
    const newFilters = {
      ...filters,
      [filterKey]: !filters[filterKey],
    };
    setFilters(newFilters);
  };

  return (
    <div className="space-y-4">
      {/* Search Input */}
      <div className="relative">
        <input
          type="text"
          value={query}
          onChange={handleSearch}
          placeholder="Search for recipes..."
          className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
          disabled={loading}
        />
        {loading && (
          <div className="absolute right-3 top-2" role="status">
            <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-500" />
          </div>
        )}
      </div>

      {/* Filters */}
      <div className="flex flex-wrap gap-2">
        <button
          type="button"
          onClick={() => handleFilterChange('isDairyFree')}
          className={`px-3 py-1 rounded-full text-sm ${
            filters.isDairyFree
              ? 'bg-blue-500 text-white'
              : 'bg-gray-200 text-gray-700'
          }`}
        >
          Dairy Free
        </button>
        <button
          type="button"
          onClick={() => handleFilterChange('isEggFree')}
          className={`px-3 py-1 rounded-full text-sm ${
            filters.isEggFree
              ? 'bg-blue-500 text-white'
              : 'bg-gray-200 text-gray-700'
          }`}
        >
          Egg Free
        </button>
        <button
          type="button"
          onClick={() => handleFilterChange('isSoyFree')}
          className={`px-3 py-1 rounded-full text-sm ${
            filters.isSoyFree
              ? 'bg-blue-500 text-white'
              : 'bg-gray-200 text-gray-700'
          }`}
        >
          Soy Free
        </button>
      </div>

      {/* Error Message */}
      {error && (
        <div className="p-4 bg-red-100 text-red-700 rounded-lg">{error}</div>
      )}

      {/* Results */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {recipes.map((recipe) => (
          <div
            key={recipe.id}
            className="p-4 border rounded-lg hover:shadow-lg transition-shadow"
          >
            {recipe.image_url && (
              <img
                src={recipe.image_url}
                alt={recipe.title}
                className="w-full h-48 object-cover rounded-lg mb-2"
              />
            )}
            <h3 className="font-semibold text-lg">{recipe.title}</h3>
            <div className="flex flex-wrap gap-1 mt-2">
              {recipe.is_dairy_free && (
                <span className="px-2 py-1 bg-green-100 text-green-800 rounded-full text-xs">
                  Dairy Free
                </span>
              )}
              {recipe.is_egg_free && (
                <span className="px-2 py-1 bg-green-100 text-green-800 rounded-full text-xs">
                  Egg Free
                </span>
              )}
              {recipe.is_soy_free && (
                <span className="px-2 py-1 bg-green-100 text-green-800 rounded-full text-xs">
                  Soy Free
                </span>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* No Results */}
      {!loading && recipes.length === 0 && query && (
        <div className="text-center text-gray-500 py-8">
          No recipes found. Try adjusting your search or filters.
        </div>
      )}
    </div>
  );
};

```

## frontend/components/layout/PageLayout.tsx
```
import type { ReactNode } from 'react';

import { Container } from '@chakra-ui/react';

interface PageLayoutProps {
  children: ReactNode;
}

export function PageLayout({ children }: PageLayoutProps) {
  return <Container maxW="container.xl">{children}</Container>;
}

```

## frontend/types.ts
```
export interface Recipe {
  id: number;
  title: string;
  description: string;
  ingredients: string[];
  instructions: string[];
  meal_type: string;
  cooking_method: string;
  allergenWarnings: string[];
  is_collection: boolean;
  date_added: string;
  is_dairy_free: boolean;
  is_gluten_free: boolean;
  is_soy_free: boolean;
  is_nut_free: boolean;
  is_egg_free: boolean;
  is_fpies_friendly: boolean;
  fpies_triggers: string[];
  fpies_safe_substitutes: Record<string, string>;
  allergens: string[];
  times_made: number;
  protein_type: string;
  prep_time: number;
  cook_time: number;
  servings: number;
  image_url: string;
  image_preview_url: string;
}

export interface SearchFilters {
  isDairyFree?: boolean;
  isEggFree?: boolean;
  isSoyFree?: boolean;
  isGlutenFree?: boolean;
  isNutFree?: boolean;
  isFpiesFriendly?: boolean;
}

export interface RecipeStore {
  recipes: Recipe[];
  loading: boolean;
  error: string | null;
  filters: SearchFilters;
  searchRecipes: (query: string, filters?: SearchFilters) => Promise<void>;
  toggleFavorite: (recipeId: number) => void;
  setFilters: (filters: SearchFilters) => void;
}

```

## frontend/next-env.d.ts
```
/// <reference types="next" />
/// <reference types="next/image-types/global" />
/// <reference types="next/navigation-types/compat/navigation" />

// NOTE: This file should not be edited
// see https://nextjs.org/docs/app/api-reference/config/typescript for more information.

```

## frontend/components/atoms/Button/index.ts
```
export * from './Button';

```

## frontend/components/atoms/Button/Button.tsx
```
import { Button as ChakraButton, type ButtonProps } from '@chakra-ui/react';

interface BaseButtonProps extends ButtonProps {
  label: string;
}

/**
 * Base Button component that follows the design system
 * Uses theme-based styling with no inline styles
 */
export const Button = ({ label, children, ...props }: BaseButtonProps) => (
  <ChakraButton {...props}>{label || children}</ChakraButton>
);

export default Button;

```

## frontend/components/atoms/Image/RecipeImage.tsx
```
import { Box, Image, type ImageProps } from '@chakra-ui/react';

interface RecipeImageProps extends Omit<ImageProps, 'fallback'> {
  title: string;
  imageUrl?: string;
}

/**
 * RecipeImage component with consistent styling and fallback
 */
export const RecipeImage = ({
  title,
  imageUrl,
  ...props
}: RecipeImageProps) => {
  if (!imageUrl) {
    return (
      <Box
        w="100%"
        h="200px"
        bg="gray.100"
        borderRadius="lg"
        _dark={{ bg: 'gray.700' }}
      />
    );
  }

  return (
    <Image
      src={imageUrl}
      alt={title}
      borderRadius="lg"
      objectFit="cover"
      w="100%"
      h="200px"
      fallback={
        <Box
          w="100%"
          h="200px"
          bg="gray.100"
          borderRadius="lg"
          _dark={{ bg: 'gray.700' }}
        />
      }
      {...props}
    />
  );
};

export default RecipeImage;

```

## frontend/utils/react-query.ts
```
import { QueryClient } from '@tanstack/react-query';

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60 * 1000, // 1 minute
      gcTime: 5 * 60 * 1000, // 5 minutes
      retry: 1,
      refetchOnWindowFocus: false,
    },
    mutations: {
      retry: 1,
    },
  },
});

```

## frontend/utils/api.ts
```
import type { Recipe, RecipeFilters } from '@/types/recipe';
import axios, { type AxiosResponse, isAxiosError } from 'axios';
import { mockApi } from '../mocks/recipeData';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface ApiResponse<T> {
  success: boolean;
  data: T;
  error?: string;
}

interface DeleteResponse {
  success: boolean;
  message?: string;
}

interface ApiError {
  error: string;
  message?: string;
}

async function handleResponse<T>(response: AxiosResponse<T>): Promise<ApiResponse<T>> {
  if (!response.data) {
    throw new Error('No data received from server');
  }

  return {
    success: true,
    data: response.data,
  };
}

function handleError(error: unknown): ApiError {
  if (isAxiosError(error)) {
    return {
      error: error.response?.data?.error || error.message,
      message: error.response?.data?.message || 'An error occurred while processing your request'
    };
  }
  return {
    error: error instanceof Error ? error.message : 'Unknown error occurred',
    message: 'An unexpected error occurred'
  };
}

export const api = {
  recipes: {
    async list(params?: { page?: number; limit?: number }): Promise<ApiResponse<Recipe[]>> {
      try {
        const searchParams = new URLSearchParams();
        if (params?.page) {
          searchParams.append('page', params.page.toString());
        }
        if (params?.limit) {
          searchParams.append('limit', params.limit.toString());
        }

        const response = await axios.get<Recipe[]>(`${API_BASE_URL}/api/recipes`, {
          params: searchParams,
        });

        return handleResponse<Recipe[]>(response);
      } catch (error) {
        if (process.env.NODE_ENV === 'development') {
          console.warn('Using mock data in development');
          return { success: true, data: mockApi.recipes };
        }
        throw handleError(error);
      }
    },

    async search(query: string, filters?: RecipeFilters): Promise<ApiResponse<Recipe[]>> {
      try {
        const response = await axios.get<Recipe[]>(`${API_BASE_URL}/api/recipes/search`, {
          params: {
            query,
            ...filters,
          },
        });
        return handleResponse<Recipe[]>(response);
      } catch (error) {
        if (process.env.NODE_ENV === 'development') {
          console.warn('Using mock data in development');
          const mockRecipes = await mockApi.searchRecipes(query, filters);
          return { success: true, data: mockRecipes };
        }
        throw handleError(error);
      }
    },

    async get(id: number): Promise<ApiResponse<Recipe>> {
      try {
        const response = await axios.get<Recipe>(`${API_BASE_URL}/api/recipes/${id}`);
        return handleResponse<Recipe>(response);
      } catch (error) {
        if (process.env.NODE_ENV === 'development') {
          console.warn('Using mock data in development');
          const mockRecipe = await mockApi.getRecipe(id.toString());
          return { success: true, data: mockRecipe };
        }
        throw handleError(error);
      }
    },

    async create(recipe: Omit<Recipe, 'id'>): Promise<ApiResponse<Recipe>> {
      try {
        const response = await axios.post<Recipe>(`${API_BASE_URL}/api/recipes`, recipe);
        return handleResponse<Recipe>(response);
      } catch (error) {
        throw handleError(error);
      }
    },

    async update(id: number, recipe: Partial<Recipe>): Promise<ApiResponse<Recipe>> {
      try {
        const response = await axios.put<Recipe>(`${API_BASE_URL}/api/recipes/${id}`, recipe);
        return handleResponse<Recipe>(response);
      } catch (error) {
        throw handleError(error);
      }
    },

    async delete(id: number): Promise<ApiResponse<DeleteResponse>> {
      try {
        const response = await axios.delete<DeleteResponse>(`${API_BASE_URL}/api/recipes/${id}`);
        return handleResponse<DeleteResponse>(response);
      } catch (error) {
        throw handleError(error);
      }
    },

    async favorite(id: number): Promise<ApiResponse<Recipe>> {
      try {
        const response = await axios.post<Recipe>(`${API_BASE_URL}/api/recipes/${id}/favorite`);
        return handleResponse<Recipe>(response);
      } catch (error) {
        throw handleError(error);
      }
    },

    async share(id: number): Promise<ApiResponse<{ url: string }>> {
      try {
        const response = await axios.post<{ url: string }>(`${API_BASE_URL}/api/recipes/${id}/share`);
        return handleResponse<{ url: string }>(response);
      } catch (error) {
        throw handleError(error);
      }
    },
  },
};

```

## frontend/utils/filters.ts
```
import type { Recipe, RecipeFilters } from '@/types/recipe';

export const filterRecipes = (recipes: Recipe[], filters: RecipeFilters): Recipe[] => {
  return recipes.filter((recipe) => {
    if (filters.searchQuery) {
      const query = filters.searchQuery.toLowerCase();
      const matchesTitle = recipe.title.toLowerCase().includes(query);
      const matchesDescription = recipe.description.toLowerCase().includes(query);
      if (!matchesTitle && !matchesDescription) {
        return false;
      }
    }

    if (filters.allergens?.length) {
      const hasAllergen = recipe.allergens.some((allergen) =>
        filters.allergens?.includes(allergen)
      );
      if (hasAllergen) {
        return false;
      }
    }

    return true;
  });
};

export const paginateRecipes = (recipes: Recipe[], page = 1, perPage = 12): Recipe[] => {
  const start = (page - 1) * perPage;
  const end = start + perPage;
  return recipes.slice(start, end);
};

```

## frontend/utils/responsive.ts
```
import type { SystemStyleObject } from '@chakra-ui/react';

type ResponsiveStyle<T> = T | Partial<Record<string, T>>;

/**
 * Creates responsive styles using a mobile-first approach
 * @example
 * createResponsiveStyle({
 *   base: { fontSize: 'sm' },
 *   md: { fontSize: 'md' },
 *   lg: { fontSize: 'lg' },
 * })
 */
export function createResponsiveStyle<T extends SystemStyleObject>(
  styles: ResponsiveStyle<T>
): SystemStyleObject {
  if (typeof styles !== 'object' || styles === null) {
    return styles as SystemStyleObject;
  }

  return Object.entries(styles).reduce((acc: SystemStyleObject, [breakpoint, style]) => {
    if (breakpoint === 'base') {
      Object.assign(acc, style);
      return acc;
    }
    acc[`@media screen and (min-width: ${breakpoint})`] = style;
    return acc;
  }, {});
}

/**
 * Creates a responsive value for Chakra UI props
 * @example
 * responsive('fontSize', ['sm', 'md', 'lg'])
 * // or
 * responsive('spacing', { base: 2, md: 4, lg: 6 })
 */
export function responsive<T>(
  property: string,
  value: ResponsiveStyle<T>
): { [key: string]: ResponsiveStyle<T> } {
  return { [property]: value };
}

export const getResponsiveValue = <T>(
  styles: ResponsiveStyle<T>,
  breakpoint: string
): T | undefined => {
  if (typeof styles === 'object' && !Array.isArray(styles)) {
    return (styles as Record<string, T>)[breakpoint];
  }
  return styles as T;
};

```

## frontend/components/ui/index.ts
```
export * from './Button';
export * from './Card';
export * from './Input';
export * from './Text';
export * from './Heading';
export * from './Container';
// Add more component exports as they are created

```

## frontend/components/ui/Card.tsx
```
import { forwardRef } from 'react';

import { Box, type BoxProps } from '@chakra-ui/react';

export interface CardProps extends BoxProps {
  variant?: 'elevated' | 'outline' | 'filled';
}

export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ variant = 'elevated', ...props }, ref) => {
    const variantStyles = {
      elevated: {
        bg: 'white',
        _dark: { bg: 'gray.800' },
        boxShadow: 'md',
        borderRadius: 'lg',
      },
      outline: {
        border: '1px solid',
        borderColor: 'gray.200',
        _dark: { borderColor: 'gray.700' },
        borderRadius: 'lg',
      },
      filled: {
        bg: 'gray.50',
        _dark: { bg: 'gray.700' },
        borderRadius: 'lg',
      },
    };

    return <Box ref={ref} {...variantStyles[variant]} {...props} />;
  }
);

Card.displayName = 'Card';

```

## frontend/components/ui/Container/index.tsx
```
import { forwardRef } from 'react';

import {
  Container as ChakraContainer,
  type ContainerProps,
} from '@chakra-ui/react';

export const Container = forwardRef<HTMLDivElement, ContainerProps>(
  ({ children, ...props }, ref) => {
    return (
      <ChakraContainer
        ref={ref}
        px={{ base: 4, md: 6, lg: 8 }}
        maxW={{
          base: '100%',
          sm: '540px',
          md: '720px',
          lg: '960px',
          xl: '1140px',
          '2xl': '1320px',
        }}
        {...props}
      >
        {children}
      </ChakraContainer>
    );
  }
);

Container.displayName = 'Container';

```

## frontend/components/ui/Card/index.tsx
```
import { forwardRef } from 'react';

import { Box, type BoxProps } from '@chakra-ui/react';

export interface CardProps extends BoxProps {
  variant?: 'elevated' | 'outline' | 'filled';
}

export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ variant = 'elevated', children, ...props }, ref) => {
    const variantStyles = {
      elevated: {
        bg: 'white',
        shadow: 'sm',
        _hover: { shadow: 'md' },
      },
      outline: {
        borderWidth: '1px',
      },
      filled: {
        bg: 'gray.50',
      },
    };

    return (
      <Box
        ref={ref}
        p={4}
        borderRadius="lg"
        transition="all 0.2s"
        {...variantStyles[variant]}
        {...props}
      >
        {children}
      </Box>
    );
  }
);

Card.displayName = 'Card';

```

## frontend/jest.config.js
```
const nextJest = require('next/jest');

const createJestConfig = nextJest({
  dir: './',
});

const customJestConfig = {
  setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
  testEnvironment: 'jest-environment-jsdom',
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/$1',
    '^.+\\.module\\.(css|sass|scss)$': 'identity-obj-proxy',
    '^.+\\.(jpg|jpeg|png|gif|webp|avif|svg)$':
      '<rootDir>/__mocks__/fileMock.js',
  },
  testPathIgnorePatterns: [
    '<rootDir>/node_modules/',
    '<rootDir>/.next/',
    '<rootDir>/e2e/',
  ],
  transformIgnorePatterns: [
    '/node_modules/',
    '^.+\\.module\\.(css|sass|scss)$',
  ],
  collectCoverageFrom: [
    'app/**/*.{js,jsx,ts,tsx}',
    'components/**/*.{js,jsx,ts,tsx}',
    'hooks/**/*.{js,jsx,ts,tsx}',
    'utils/**/*.{js,jsx,ts,tsx}',
    '!**/*.d.ts',
    '!**/node_modules/**',
    '!**/.next/**',
    '!**/coverage/**',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
  watchPlugins: [
    'jest-watch-typeahead/filename',
    'jest-watch-typeahead/testname',
  ],
};

module.exports = createJestConfig(customJestConfig);

```

## frontend/router.ts
```
import { RootRoute, Route, Router, createHashHistory } from '@tanstack/router';
import { z } from 'zod';

// Define type-safe search params
const searchParamsSchema = z.object({
  q: z.string().optional(),
  category: z.string().optional(),
  page: z.coerce.number().optional(),
  filters: z.string().optional(), // JSON stringified filters
});

export type SearchParams = z.infer<typeof searchParamsSchema>;

// Root route
const rootRoute = new RootRoute();

// Routes with type-safe params and search params
const indexRoute = new Route({
  getParentRoute: () => rootRoute,
  path: '/',
  validateSearch: searchParamsSchema,
});

const recipeRoute = new Route({
  getParentRoute: () => rootRoute,
  path: 'recipe/$recipeId',
  parseParams: (params) => ({
    recipeId: Number(params.recipeId),
  }),
  validateSearch: searchParamsSchema,
});

// Create and export the router
const routeTree = rootRoute.addChildren([indexRoute, recipeRoute]);

export const router = new Router({
  routeTree,
  history: createHashHistory(),
  defaultPreload: 'intent',
});

declare module '@tanstack/router' {
  interface Register {
    router: typeof router;
  }
}

```

## frontend/jest.setup.js
```
import '@testing-library/jest-dom';

// Mock IntersectionObserver
global.IntersectionObserver = class IntersectionObserver {
  disconnect() {}
  observe() {}
  unobserve() {}
};

```

## frontend/app/providers.tsx
```
'use client';

import { useState, type ReactNode } from 'react';

import { ChakraProvider } from '@chakra-ui/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';

import { theme } from '@/theme';

interface ProvidersProps {
  children: ReactNode;
}

export function Providers({ children }: ProvidersProps) {
  const [queryClient] = useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            staleTime: 60 * 1000, // 1 minute
            gcTime: 5 * 60 * 1000, // 5 minutes
            retry: 1,
            refetchOnWindowFocus: false,
          },
        },
      })
  );

  return (
    <QueryClientProvider client={queryClient}>
      <ChakraProvider theme={theme}>{children}</ChakraProvider>
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  );
}

```

## frontend/app/page.tsx
```
'use client';

import { useState } from 'react';

import { RecipeCard } from '@/components/RecipeCard';
import { RecipeFilters } from '@/components/RecipeFilters';
import type { RecipeFilters as Filters, Recipe } from '@/types/recipe';

export default function Home() {
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [loading, setLoading] = useState(false);

  const handleFilterChange = async (filters: Filters) => {
    setLoading(true);
    try {
      const params = new URLSearchParams();
      if (filters.searchQuery) {
        params.append('q', filters.searchQuery);
      }
      if (filters.allergens?.length) {
        for (const allergen of filters.allergens) {
          params.append('allergens', allergen);
        }
      }

      const response = await fetch(`/api/recipes?${params.toString()}`);
      const data = await response.json();
      setRecipes(data);
    } catch (error) {
      console.error('Failed to fetch recipes:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleLike = async (recipeId: number) => {
    try {
      await fetch(`/api/recipes/${recipeId}/like`, {
        method: 'POST',
      });

      setRecipes((prev) =>
        prev.map((recipe) =>
          recipe.id === recipeId
            ? { ...recipe, isLiked: !recipe.isLiked }
            : recipe
        )
      );
    } catch (error) {
      console.error('Failed to like recipe:', error);
    }
  };

  return (
    <main className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold text-gray-900 mb-8">
        FPIES-Friendly Recipes
      </h1>

      <div className="mb-8">
        <RecipeFilters onFilterChange={handleFilterChange} />
      </div>

      {loading ? (
        <div className="text-center py-12">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900 mx-auto" />
          <p className="mt-4 text-gray-600">Loading recipes...</p>
        </div>
      ) : recipes.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {recipes.map((recipe) => (
            <RecipeCard key={recipe.id} recipe={recipe} onLike={handleLike} />
          ))}
        </div>
      ) : (
        <div className="text-center py-12">
          <p className="text-gray-600">
            No recipes found. Try adjusting your filters.
          </p>
        </div>
      )}
    </main>
  );
}

```

## frontend/app/layout.tsx
```
import type { Metadata } from 'next';

import type React from 'react';

import { Inter } from 'next/font/google';

import { theme } from '@/theme';
import { ChakraProvider } from '@chakra-ui/react';
import './globals.css';
import { Providers } from './providers';

const inter = Inter({ subsets: ['latin'] });

if (process.env.NODE_ENV === 'development') {
  require('@/mocks').initMocks();
}

export const metadata: Metadata = {
  title: 'FPIES-Friendly Recipes',
  description:
    'A recipe platform for families managing FPIES and food allergies',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <ChakraProvider theme={theme}>
          <Providers>{children}</Providers>
        </ChakraProvider>
      </body>
    </html>
  );
}

```

## frontend/app/recipes/page.tsx
```
import { RecipeSearch } from '@/components/RecipeSearch';
import { RecipeGrid } from '@/components/organisms/RecipeGrid';
import type { RecipeList } from '@/types/api';
import { Container, Heading, Stack } from '@chakra-ui/react';
import { useState } from 'react';

export default function RecipesPage() {
  const [searchResults, setSearchResults] = useState<RecipeList | null>(null);

  const handleSearchResults = (results: RecipeList) => {
    setSearchResults(results);
  };

  return (
    <Container maxW="container.xl" py={8}>
      <Stack spacing={8}>
        <Heading size="xl">Recipe Search</Heading>
        <RecipeSearch onSearch={handleSearchResults} />
        <RecipeGrid recipes={searchResults} />
      </Stack>
    </Container>
  );
}

```

## frontend/.storybook/preview.tsx
```
import { CSSReset, ChakraProvider } from '@chakra-ui/react';
import type { Preview } from '@storybook/react';
import { theme } from '../theme';

const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: '^on[A-Z].*' },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/i,
      },
    },
  },
  decorators: [
    (Story) => (
      <ChakraProvider theme={theme}>
        <CSSReset />
        <Story />
      </ChakraProvider>
    ),
  ],
};

export default preview;

```

## frontend/.storybook/main.ts
```
import type { StorybookConfig } from '@storybook/nextjs';

const config: StorybookConfig = {
  stories: ['../components/**/*.stories.@(js|jsx|ts|tsx)', '../app/**/*.stories.@(js|jsx|ts|tsx)'],
  addons: [
    '@storybook/addon-links',
    '@storybook/addon-essentials',
    '@storybook/addon-interactions',
  ],
  framework: {
    name: '@storybook/nextjs',
    options: {},
  },
  docs: {
    autodocs: 'tag',
  },
};

export default config;

```

## frontend/app/recipes/[id]/page.tsx
```
import { useRecipe } from '@/hooks/api/useRecipes';
import {
  Badge,
  Box,
  Container,
  Divider,
  Grid,
  Heading,
  Image,
  List,
  ListIcon,
  ListItem,
  Stack,
  Text,
  useColorModeValue,
} from '@chakra-ui/react';
import { MdCheckCircle, MdTimer } from 'react-icons/md';

export default function RecipeDetailPage({
  params,
}: {
  params: { id: string };
}) {
  const { data: recipe, isLoading, error } = useRecipe(parseInt(params.id));
  const borderColor = useColorModeValue('gray.200', 'gray.700');

  if (isLoading) {
    return (
      <Container maxW="container.xl" py={8}>
        <Text>Loading recipe...</Text>
      </Container>
    );
  }

  if (error) {
    return (
      <Container maxW="container.xl" py={8}>
        <Text color="red.500">Error loading recipe: {error.message}</Text>
      </Container>
    );
  }

  if (!recipe) {
    return (
      <Container maxW="container.xl" py={8}>
        <Text>Recipe not found</Text>
      </Container>
    );
  }

  return (
    <Container maxW="container.xl" py={8}>
      <Stack spacing={8}>
        <Box>
          <Heading size="2xl" mb={4}>
            {recipe.title}
          </Heading>
          {recipe.image_url && (
            <Image
              src={recipe.image_url}
              alt={recipe.title}
              borderRadius="lg"
              width="100%"
              maxH="400px"
              objectFit="cover"
            />
          )}
        </Box>

        <Grid templateColumns={{ base: '1fr', md: '2fr 1fr' }} gap={8}>
          <Stack spacing={6}>
            {recipe.description && (
              <Text fontSize="lg">{recipe.description}</Text>
            )}

            <Box>
              <Heading size="md" mb={4}>
                Instructions
              </Heading>
              <List spacing={4}>
                {recipe.instructions?.map((instruction, index) => (
                  <ListItem key={index} display="flex">
                    <ListIcon as={MdCheckCircle} color="green.500" mt={1} />
                    <Text>{instruction}</Text>
                  </ListItem>
                ))}
              </List>
            </Box>
          </Stack>

          <Stack
            spacing={6}
            borderWidth="1px"
            borderRadius="lg"
            p={6}
            borderColor={borderColor}
          >
            <Box>
              <Heading size="md" mb={4}>
                Details
              </Heading>
              <Stack spacing={3}>
                {recipe.prep_time_minutes && (
                  <Box display="flex" alignItems="center">
                    <ListIcon as={MdTimer} color="blue.500" />
                    <Text>Prep time: {recipe.prep_time_minutes} minutes</Text>
                  </Box>
                )}
                {recipe.cook_time_minutes && (
                  <Box display="flex" alignItems="center">
                    <ListIcon as={MdTimer} color="blue.500" />
                    <Text>Cook time: {recipe.cook_time_minutes} minutes</Text>
                  </Box>
                )}
                {recipe.servings && <Text>Servings: {recipe.servings}</Text>}
              </Stack>
            </Box>

            <Divider />

            <Box>
              <Heading size="md" mb={4}>
                Ingredients
              </Heading>
              <List spacing={2}>
                {recipe.ingredients?.map((ingredient, index) => (
                  <ListItem key={index}>
                    <ListIcon as={MdCheckCircle} color="green.500" />
                    {ingredient}
                  </ListItem>
                ))}
              </List>
            </Box>

            {recipe.cuisine_types?.length > 0 && (
              <>
                <Divider />
                <Box>
                  <Heading size="md" mb={4}>
                    Cuisine
                  </Heading>
                  <Stack direction="row" wrap="wrap" spacing={2}>
                    {recipe.cuisine_types.map((cuisine) => (
                      <Badge
                        key={cuisine.cuisine_id}
                        colorScheme="purple"
                        px={2}
                        py={1}
                        borderRadius="full"
                      >
                        {cuisine.name}
                      </Badge>
                    ))}
                  </Stack>
                </Box>
              </>
            )}
          </Stack>
        </Grid>
      </Stack>
    </Container>
  );
}

```

## frontend/app/components/RecipeSearch.tsx
```
import { useRecipeSearch } from '@/hooks/api/useRecipeSearch';
import {
  Box,
  Button,
  Collapse,
  FormControl,
  FormLabel,
  Grid,
  HStack,
  IconButton,
  Input,
  NumberInput,
  NumberInputField,
  Select,
  Stack,
  useDisclosure,
} from '@chakra-ui/react';
import { useEffect, useState } from 'react';
import { FaFilter } from 'react-icons/fa';

const cuisineOptions = [
  'Italian',
  'Mexican',
  'Chinese',
  'Indian',
  'Japanese',
  'Thai',
  'Mediterranean',
  'American',
  'French',
  'Greek',
];

const dietOptions = [
  'Vegetarian',
  'Vegan',
  'Gluten-Free',
  'Dairy-Free',
  'Keto',
  'Paleo',
  'Low-Carb',
];

interface RecipeSearchProps {
  onSearch: (results: any) => void;
}

export default function RecipeSearch({ onSearch }: RecipeSearchProps) {
  const [query, setQuery] = useState('');
  const [cuisine, setCuisine] = useState<string>('');
  const [diet, setDiet] = useState<string>('');
  const [maxTime, setMaxTime] = useState<number | ''>('');
  const { isOpen, onToggle } = useDisclosure();

  const { data, isLoading, refetch } = useRecipeSearch(
    query,
    {
      cuisine_type: cuisine || undefined,
      diet: diet || undefined,
      max_cooking_time: maxTime || undefined,
    },
    1,
    20,
    false
  );

  useEffect(() => {
    if (data) {
      onSearch(data);
    }
  }, [data, onSearch]);

  const handleSearch = () => {
    if (query.trim()) {
      refetch();
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  const handleClear = () => {
    setQuery('');
    setCuisine('');
    setDiet('');
    setMaxTime('');
  };

  return (
    <Stack spacing={4} width="100%">
      <HStack>
        <FormControl>
          <Input
            placeholder="Search recipes..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyPress={handleKeyPress}
            variant="filled"
            size="lg"
          />
        </FormControl>
        <IconButton
          aria-label="Toggle filters"
          icon={<FaFilter />}
          variant="filter"
          size="lg"
          onClick={onToggle}
        />
        <Button
          onClick={handleSearch}
          isLoading={isLoading}
          size="lg"
          colorScheme="blue"
          variant="solid"
        >
          Search
        </Button>
      </HStack>

      <Collapse in={isOpen}>
        <Box layerStyle="form">
          <Grid variant="filters">
            <FormControl>
              <FormLabel>Cuisine Type</FormLabel>
              <Select
                placeholder="Select cuisine"
                value={cuisine}
                onChange={(e) => setCuisine(e.target.value)}
                variant="filled"
              >
                {cuisineOptions.map((option) => (
                  <option key={option} value={option.toLowerCase()}>
                    {option}
                  </option>
                ))}
              </Select>
            </FormControl>

            <FormControl>
              <FormLabel>Dietary Restriction</FormLabel>
              <Select
                placeholder="Select diet"
                value={diet}
                onChange={(e) => setDiet(e.target.value)}
                variant="filled"
              >
                {dietOptions.map((option) => (
                  <option key={option} value={option.toLowerCase()}>
                    {option}
                  </option>
                ))}
              </Select>
            </FormControl>

            <FormControl>
              <FormLabel>Max Cooking Time (minutes)</FormLabel>
              <NumberInput
                value={maxTime}
                onChange={(_, value) => setMaxTime(value)}
                min={0}
                variant="filled"
              >
                <NumberInputField placeholder="Enter time" />
              </NumberInput>
            </FormControl>
          </Grid>

          <Button
            onClick={handleClear}
            mt={4}
            variant="filter"
            size="md"
            width="auto"
          >
            Clear Filters
          </Button>
        </Box>
      </Collapse>
    </Stack>
  );
}

```

## frontend/types/api.ts
```
import type { AxiosError, RawAxiosRequestHeaders } from 'axios';

export interface ApiConfig {
  baseUrl: string;
  defaultParams: Record<string, string | number | boolean>;
  headers: RawAxiosRequestHeaders;
  timeout: number;
}

export interface RequestInterceptor<TRequest = unknown> {
  id?: string;
  onRequest: (config: ApiRequestConfig<TRequest>) => ApiRequestConfig<TRequest>;
}

export interface ResponseInterceptor<TResponse = unknown> {
  id?: string;
  onResponse: (response: TResponse) => Promise<TResponse> | TResponse;
  onError: (error: ApiError) => Promise<never>;
}

export interface ApiRequestConfig<TRequest = unknown> {
  url: string;
  method: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';
  params?: Record<string, string | number | boolean>;
  data?: TRequest;
  headers?: RawAxiosRequestHeaders;
  timeout?: number;
  validateStatus?: (status: number) => boolean;
  retry?: {
    maxRetries: number;
    delayMs: number;
    retryCondition?: (error: ApiError) => boolean;
  };
}

export interface ApiError extends AxiosError {
  details: ApiErrorDetails;
  isRetryable?: boolean;
}

export interface ApiErrorDetails {
  message: string;
  statusCode?: number;
  config?: ApiRequestConfig;
  originalError?: Error;
  context?: Record<string, unknown>;
  retryAttempt?: number;
}

export interface ApiSource {
  name: string;
  description: string;
  defaultConfig: Partial<ApiConfig>;
  parameterDocs: ApiParameterDocs[];
}

export interface ApiParameterDocs {
  name: string;
  description: string;
  type: 'string' | 'number' | 'boolean' | 'array';
  required: boolean;
  default?: string | number | boolean | string[];
  options?: string[];
}

// Recipe Types
export interface Recipe {
  recipe_id: number;
  title: string;
  image_url?: string;
  source_url?: string;
  prep_time_minutes?: number;
  cook_time_minutes?: number;
  servings?: number;
  is_favorite: boolean;
  variations?: string;
  last_made_date?: string;
  created_at: string;
  updated_at: string;
  instructions: RecipeInstruction[];
  allergens: Allergen[];
  ingredients: Ingredient[];
  meal_types: MealType[];
  cook_methods: CookMethod[];
  protein_types: ProteinType[];
  cuisine_types: CuisineType[];
}

export interface RecipeCreate {
  title: string;
  image_url?: string;
  source_url?: string;
  prep_time_minutes?: number;
  cook_time_minutes?: number;
  servings?: number;
  is_favorite?: boolean;
  variations?: string;
  instructions: RecipeInstructionCreate[];
}

export interface RecipeUpdate {
  title?: string;
  image_url?: string;
  source_url?: string;
  prep_time_minutes?: number;
  cook_time_minutes?: number;
  servings?: number;
  is_favorite?: boolean;
  variations?: string;
  instructions?: RecipeInstructionCreate[];
}

// Recipe Instructions
export interface RecipeInstruction {
  instruction_id: number;
  recipe_id: number;
  step_number: number;
  instruction: string;
}

export interface RecipeInstructionCreate {
  step_number: number;
  instruction: string;
}

// Ingredients
export interface Ingredient {
  ingredient_id: number;
  name: string;
  category_id: number;
}

export interface IngredientCreate {
  name: string;
  category_id: number;
}

export interface IngredientCategory {
  category_id: number;
  name: string;
}

// Allergens
export interface Allergen {
  allergen_id: number;
  name: string;
  severity?: string;
}

export interface AllergenCreate {
  name: string;
  severity?: string;
}

// Cook Methods
export interface CookMethod {
  method_id: number;
  name: string;
}

export interface CookMethodCreate {
  name: string;
}

// Protein Types
export interface ProteinType {
  protein_id: number;
  name: string;
}

export interface ProteinTypeCreate {
  name: string;
}

// Meal Types
export interface MealType {
  meal_type_id: number;
  name: string;
}

export interface MealTypeCreate {
  name: string;
}

// Cuisine Types
export interface CuisineType {
  cuisine_id: number;
  name: string;
  last_used_date?: string;
}

export interface CuisineTypeCreate {
  name: string;
  last_used_date?: string;
}

// Dietary Restrictions
export interface DietaryRestriction {
  restriction_id: number;
  name: string;
}

export interface DietaryRestrictionCreate {
  name: string;
}

// Family Members
export interface FamilyMember {
  member_id: number;
  name: string;
  birth_date?: string;
  notes?: string;
}

export interface FamilyMemberCreate {
  name: string;
  birth_date?: string;
  notes?: string;
}

// Meal Plans
export interface MealPlan {
  plan_id: number;
  recipe_id: number;
  planned_date: string;
  meal_type_id: number;
  notes?: string;
  member_id: number;
}

export interface MealPlanCreate {
  recipe_id: number;
  planned_date: string;
  meal_type_id: number;
  notes?: string;
  member_id: number;
}

// Recipe Search
export interface RecipeSearchFilters {
  cuisine_type?: string;
  difficulty?: string;
  max_cooking_time?: number;
  tags?: string[];
  ingredients?: string[];
  allergens_exclude?: string[];
  dietary_restrictions?: string[];
}

export interface RecipeSearchResult {
  id: string;
  title: string;
  description?: string;
  image_url?: string;
  source_url?: string;
  prep_time?: number;
  cook_time?: number;
  total_time?: number;
  servings?: number;
  cuisine?: string;
  diet?: string[];
  ingredients?: string[];
  instructions?: string[];
  source: string;
}

export interface RecipeList {
  total: number;
  results: RecipeSearchResult[];
  source: string;
}

// Recipe Ratings
export interface RecipeRating {
  rating_id: number;
  recipe_id: number;
  member_id: number;
  rating: number;
  review?: string;
  created_at: string;
}

export interface RecipeRatingCreate {
  recipe_id: number;
  member_id: number;
  rating: number;
  review?: string;
}

```

## frontend/types/utils.ts
```
/**
 * Type guard to ensure a value is not undefined
 */
export function isDefined<T>(value: T | undefined): value is T {
  return value !== undefined;
}

/**
 * Type guard to ensure a value is not null
 */
export function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}

/**
 * Ensures all properties in an object are required
 */
export type Required<T> = {
  [P in keyof T]-?: T[P];
};

/**
 * Makes specific properties in a type required
 */
export type RequiredProps<T, K extends keyof T> = T & Required<Pick<T, K>>;

/**
 * Type guard for checking if a value is a Promise
 */
export function isPromise<T = unknown>(value: unknown): value is Promise<T> {
  return value instanceof Promise;
}

/**
 * Ensures a function returns a non-Promise type
 */
export type NonPromise<T> = T extends Promise<infer U> ? U : T;

/**
 * Type guard for checking if an object has a specific property
 */
export function hasProperty<T extends object, K extends PropertyKey>(
  obj: T,
  prop: K
): obj is T & Record<K, unknown> {
  return Object.prototype.hasOwnProperty.call(obj, prop);
}

/**
 * Type guard for checking if a value matches a specific type
 */
export function isType<T>(value: unknown, check: (value: unknown) => value is T): value is T {
  return check(value);
}

/**
 * Utility type for API responses that ensures proper typing
 */
export type ApiResponseType<T> = {
  data: T;
  error?: string;
};

```

## frontend/types/recipe.ts
```
export type ProteinType =
  | 'chicken'
  | 'beef'
  | 'pork'
  | 'fish'
  | 'shellfish'
  | 'turkey'
  | 'lamb'
  | 'vegetarian'
  | 'other';

export type MealType = 'breakfast' | 'lunch' | 'dinner' | 'dessert' | 'snack' | 'other';

export type CookingMethod =
  | 'bake'
  | 'stovetop'
  | 'grill'
  | 'slow_cooker'
  | 'instant_pot'
  | 'air_fryer'
  | 'refrigerate'
  | 'freeze';

export interface User {
  id: number;
  name: string;
  allergies: string[];
  preferences: Record<string, unknown>;
  healthConditions: string[];
}

export interface MethodDifference {
  type: string;
  description: string;
  base: string;
  variation: string;
}

export interface TimingDifference {
  type: string;
  base: string;
  variation: string;
}

export interface KeyDifferences {
  ingredients: {
    added: string[];
    removed: string[];
  };
  methods: MethodDifference[];
  timing: TimingDifference[];
}

export interface VariationGroup {
  base_title: string;
  recipe_count: number;
  description: string;
}

export interface Recipe {
  id: number;
  title: string;
  description: string;
  meal_type: MealType;
  is_collection: boolean;
  source_url?: string;
  image_url?: string;
  image_preview_url?: string;
  ingredients: string[];
  instructions: string[];
  prep_time?: number;
  cook_time?: number;
  cooking_method?: CookingMethod;
  protein_type?: ProteinType;
  servings?: number;
  date_added: string;
  is_dairy_free: boolean;
  is_soy_free: boolean;
  is_gluten_free: boolean;
  is_nut_free: boolean;
  is_egg_free: boolean;
  is_fpies_friendly: boolean;
  fpies_triggers: string[];
  fpies_safe_substitutes: Record<string, string>;
  allergens: string[];
  last_made?: string;
  times_made: number;
  rating?: number;
  variation_group?: {
    base_title: string;
    recipe_count: number;
    description: string;
  };
  variation_notes?: string;
  favorite?: boolean;
  key_differences?: {
    ingredients: {
      added: string[];
      removed: string[];
    };
    methods: Array<{
      type: string;
      description: string;
      base: string;
      variation: string;
    }>;
    timing: Array<{
      type: string;
      base: string;
      variation: string;
    }>;
  };
}

export interface CookingHistory {
  id: number;
  recipeId: number;
  dateCooked: string;
  notes?: string;
  recipe?: Recipe;
}

export interface RecipeFilters {
  meal_type?: MealType;
  cooking_method?: CookingMethod;
  protein_type?: ProteinType;
  is_collection?: boolean;
  allergens?: string[];
  is_fpies_friendly?: boolean;
  is_dairy_free?: boolean;
  search_query?: string;
}

// Export RecipeFilters as SearchFilters for API compatibility
export type SearchFilters = RecipeFilters;

export interface MealPlan {
  id: string;
  startDate: string;
  endDate: string;
  meals: MealPlanItem[];
}

export interface MealPlanItem {
  id: string;
  recipeId: string;
  date: string;
  mealType: MealType;
  servings: number;
  notes?: string;
}

export interface RecipeCategory {
  id: string;
  name: string;
  description?: string;
  recipes: string[]; // Recipe IDs
}

```

## frontend/app/components/atoms/RecipeMetadata.tsx
```
import { HStack, Icon, Text } from '@chakra-ui/react';
import { IconType } from 'react-icons';
import { FaClock, FaGlobe, FaUtensils } from 'react-icons/fa';

interface MetadataItemProps {
  icon: IconType;
  label: string;
}

function MetadataItem({ icon, label }: MetadataItemProps) {
  return (
    <HStack spacing={1} color="gray.600">
      <Icon as={icon} fontSize="sm" />
      <Text fontSize="sm" fontWeight="medium">
        {label}
      </Text>
    </HStack>
  );
}

interface RecipeMetadataProps {
  cookingTime?: number;
  servings?: number;
  cuisine?: string;
}

export function RecipeMetadata({
  cookingTime,
  servings,
  cuisine,
}: RecipeMetadataProps) {
  return (
    <HStack spacing={4} mt={2}>
      {cookingTime && (
        <MetadataItem icon={FaClock} label={`${cookingTime} min`} />
      )}
      {servings && (
        <MetadataItem icon={FaUtensils} label={`${servings} servings`} />
      )}
      {cuisine && <MetadataItem icon={FaGlobe} label={cuisine} />}
    </HStack>
  );
}

```

## frontend/app/components/atoms/RecipeImage.tsx
```
import { Box, Image, ImageProps } from '@chakra-ui/react';

interface RecipeImageProps extends Omit<ImageProps, 'src'> {
  imageUrl?: string;
  title: string;
}

export function RecipeImage({ imageUrl, title, ...props }: RecipeImageProps) {
  if (!imageUrl) return null;

  return (
    <Box position="relative" height="200px" overflow="hidden" borderRadius="lg">
      <Image
        src={imageUrl}
        alt={title}
        objectFit="cover"
        width="100%"
        height="100%"
        fallbackSrc="/images/recipe-placeholder.jpg"
        transition="transform 0.3s ease-in-out"
        _hover={{ transform: 'scale(1.05)' }}
        {...props}
      />
    </Box>
  );
}

```

## frontend/app/components/molecules/RecipeCard.tsx
```
import type { RecipeSearchResult } from '@/types/api';
import {
  Card,
  CardBody,
  Heading,
  LinkBox,
  LinkOverlay,
} from '@chakra-ui/react';
import NextLink from 'next/link';
import { RecipeImage } from '../atoms/RecipeImage';
import { RecipeMetadata } from '../atoms/RecipeMetadata';

interface RecipeCardProps {
  recipe: RecipeSearchResult;
}

export function RecipeCard({ recipe }: RecipeCardProps) {
  return (
    <LinkBox
      as={Card}
      variant="outline"
      _hover={{ shadow: 'lg' }}
      transition="all 0.2s"
    >
      <RecipeImage imageUrl={recipe.image_url} title={recipe.title} />
      <CardBody>
        <LinkOverlay as={NextLink} href={`/recipes/${recipe.id}`}>
          <Heading size="md" mb={2} noOfLines={2}>
            {recipe.title}
          </Heading>
        </LinkOverlay>

        <RecipeMetadata
          cookingTime={recipe.total_time}
          servings={recipe.servings}
          cuisine={recipe.cuisine}
        />
      </CardBody>
    </LinkBox>
  );
}

```

## frontend/app/components/organisms/RecipeGrid.tsx
```
import type { RecipeList } from '@/types/api';
import { Box, Grid, Text } from '@chakra-ui/react';
import { RecipeCard } from '../molecules/RecipeCard';

interface RecipeGridProps {
  recipes: RecipeList | null;
}

export function RecipeGrid({ recipes }: RecipeGridProps) {
  if (!recipes?.results?.length) {
    return (
      <Box textAlign="center" py={8}>
        <Text color="gray.600" fontSize="lg">
          No recipes found. Try adjusting your search criteria.
        </Text>
      </Box>
    );
  }

  return (
    <Grid
      templateColumns={{
        base: '1fr',
        md: 'repeat(2, 1fr)',
        lg: 'repeat(3, 1fr)',
      }}
      gap={6}
      width="100%"
    >
      {recipes.results.map((recipe) => (
        <RecipeCard key={recipe.id} recipe={recipe} />
      ))}
    </Grid>
  );
}

```

## frontend/stores/recipeStore.ts
```
import { create } from 'zustand';
import type { Recipe, RecipeFilters } from '../types';
import { api } from '../utils/api';

interface RecipeStore {
  // State
  recipes: Recipe[];
  loading: boolean;
  error: string | null;
  selectedRecipe: Recipe | null;
  searchQuery: string;
  filters: RecipeFilters;

  // Actions
  searchRecipes: (query: string, filters: RecipeFilters) => Promise<void>;
  saveRecipe: (recipe: Recipe) => Promise<void>;
  deleteRecipe: (id: number) => Promise<void>;
  setSelectedRecipe: (recipe: Recipe | null) => void;
  setFilters: (filters: RecipeFilters) => void;
  toggleFavorite: (id: number) => Promise<void>;
  shareRecipe: (id: number) => Promise<void>;
  clearError: () => void;
}

export const useRecipeStore = create<RecipeStore>((set, get) => ({
  // Initial state
  recipes: [],
  loading: false,
  error: null,
  selectedRecipe: null,
  searchQuery: '',
  filters: {
    is_dairy_free: false,
    is_egg_free: false,
    is_soy_free: false,
    protein_type: undefined,
  },

  // Actions
  searchRecipes: async (query: string, filters: RecipeFilters) => {
    try {
      set({ loading: true, error: null });
      const response = await api.recipes.search(query, filters);
      set({
        recipes: response.data,
        searchQuery: query,
        filters,
        loading: false,
      });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to search recipes',
        loading: false,
      });
    }
  },

  saveRecipe: async (recipe: Recipe) => {
    try {
      set({ loading: true, error: null });
      const response = await api.recipes.create(recipe);

      // Update recipes list if it exists in current search
      const { recipes, searchQuery, filters } = get();
      if (searchQuery) {
        const updatedResponse = await api.recipes.search(searchQuery, filters);
        set({ recipes: updatedResponse.data });
      } else {
        set({ recipes: [...recipes, response.data] });
      }

      set({ loading: false });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to save recipe',
        loading: false,
      });
    }
  },

  deleteRecipe: async (id: number) => {
    try {
      set({ loading: true, error: null });
      await api.recipes.delete(id);

      // Remove from current list
      const { recipes } = get();
      set({
        recipes: recipes.filter((r) => r.id !== id),
        loading: false,
      });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to delete recipe',
        loading: false,
      });
    }
  },

  setSelectedRecipe: (recipe: Recipe | null) => {
    set({ selectedRecipe: recipe });
  },

  setFilters: (filters: RecipeFilters) => {
    set({ filters });

    // Re-run search with new filters if we have a query
    const { searchQuery } = get();
    if (searchQuery) {
      get().searchRecipes(searchQuery, filters);
    }
  },

  toggleFavorite: async (id: number) => {
    try {
      const response = await api.recipes.favorite(id);

      // Update recipe in state
      const { recipes, selectedRecipe } = get();
      const updatedRecipes = recipes.map((recipe) => (recipe.id === id ? response.data : recipe));

      set({
        recipes: updatedRecipes,
        selectedRecipe: selectedRecipe?.id === id ? response.data : selectedRecipe,
      });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to update favorite',
      });
    }
  },

  shareRecipe: async (id: number) => {
    try {
      await api.recipes.share(id);
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to share recipe',
      });
    }
  },

  clearError: () => {
    set({ error: null });
  },
}));

```

## frontend/stores/globalStore.ts
```
import { proxy, subscribe } from 'valtio';
import { create } from 'zustand';
import { devtools, subscribeWithSelector } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';
import { router } from '../router';
import type { SearchParams } from '../router';

// Valtio state for reactive UI elements
export const uiState = proxy({
  theme: 'light' as 'light' | 'dark',
  sidebarOpen: true,
  modals: new Set<string>(),
  toast: null as { message: string; type: 'success' | 'error' } | null,
});

// Subscribe to theme changes
subscribe(uiState, () => {
  document.documentElement.classList.toggle('dark', uiState.theme === 'dark');
});

// Types for our main store
interface GlobalState {
  // URL-synced state
  search: {
    query: string;
    filters: {
      category: string[];
      dietary: string[];
      cookingTime: [number, number];
    };
    page: number;
  };
  // App state
  recipes: {
    favorites: number[];
    recentlyViewed: number[];
    userNotes: Record<number, string>;
  };
  // Action creators
  actions: {
    updateSearch: (params: Partial<SearchParams>) => void;
    toggleFavorite: (recipeId: number) => void;
    addRecentlyViewed: (recipeId: number) => void;
    updateNote: (recipeId: number, note: string) => void;
    clearHistory: () => void;
  };
}

// Create store with all middleware
export const useGlobalStore = create<GlobalState>()(
  subscribeWithSelector(
    devtools(
      immer((set, _get) => ({
        // Initial state
        search: {
          query: '',
          filters: {
            category: [],
            dietary: [],
            cookingTime: [0, 180],
          },
          page: 1,
        },
        recipes: {
          favorites: [],
          recentlyViewed: [],
          userNotes: {},
        },
        // Actions
        actions: {
          updateSearch: (params) => {
            set((state) => {
              // Update internal state
              if (params.q) {
                state.search.query = params.q;
              }
              if (params.page) {
                state.search.page = params.page;
              }
              if (params.filters) {
                const filters = JSON.parse(params.filters);
                state.search.filters = { ...state.search.filters, ...filters };
              }
            });
            // Sync with URL
            router.navigate({
              search: (old) => ({ ...old, ...params }),
            });
          },

          toggleFavorite: (recipeId) => {
            set((state) => {
              const favorites = state.recipes.favorites;
              const index = favorites.indexOf(recipeId);
              if (index === -1) {
                favorites.push(recipeId);
              } else {
                favorites.splice(index, 1);
              }
            });
          },

          addRecentlyViewed: (recipeId) => {
            set((state) => {
              const recent = state.recipes.recentlyViewed;
              const index = recent.indexOf(recipeId);
              if (index !== -1) {
                recent.splice(index, 1);
              }
              recent.unshift(recipeId);
              if (recent.length > 10) {
                recent.pop();
              }
            });
          },

          updateNote: (recipeId, note) => {
            set((state) => {
              state.recipes.userNotes[recipeId] = note;
            });
          },

          clearHistory: () => {
            set((state) => {
              state.recipes.recentlyViewed = [];
            });
          },
        },
      }))
    )
  )
);

// Subscribe to relevant state changes
useGlobalStore.subscribe(
  (state) => state.recipes.favorites,
  (favorites) => {
    localStorage.setItem('favorites', JSON.stringify(favorites));
  }
);

// Create a middleware for analytics
export const withAnalytics = (_config: Record<string, unknown>) => (next: (args: unknown[]) => unknown) => (args: unknown[]) => {
  const result = next(args);
  if (args[0]?.type?.includes('action')) {
    // Send to analytics service
  }
  return result;
};

```

## frontend/stores/userPreferencesStore.ts
```
import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';

type UserPreferences = {
  theme: 'light' | 'dark';
  fontSize: 'small' | 'medium' | 'large';
  allergies: string[];
  // Actions
  setTheme: (theme: UserPreferences['theme']) => void;
  setFontSize: (size: UserPreferences['fontSize']) => void;
  updateAllergies: (allergies: string[]) => void;
};

export const useUserPreferences = create<UserPreferences>()(
  devtools(
    persist(
      (set) => ({
        // Initial state
        theme: 'light',
        fontSize: 'medium',
        allergies: [],

        // Actions
        setTheme: (theme) => set({ theme }),
        setFontSize: (fontSize) => set({ fontSize }),
        updateAllergies: (allergies) => set({ allergies }),
      }),
      {
        name: 'user-preferences', // name in localStorage
      }
    ),
    { name: 'User Preferences Store' }
  )
);

```

## frontend/stores/apiConfigStore.ts
```
import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { ApiConfig } from '../types/api';

interface ApiConfigState {
  configs: Record<string, ApiConfig>;
  setConfig: (apiName: string, config: Partial<ApiConfig>) => void;
  getConfig: (apiName: string) => ApiConfig | undefined;
  resetConfig: (apiName: string) => void;
}

export const useApiConfigStore = create<ApiConfigState>()(
  persist(
    (set, get) => ({
      configs: {},

      setConfig: (apiName: string, config: Partial<ApiConfig>) => {
        set((state) => ({
          configs: {
            ...state.configs,
            [apiName]: {
              ...state.configs[apiName],
              ...config,
              defaultParams: {
                ...state.configs[apiName]?.defaultParams,
                ...config.defaultParams,
              },
              headers: {
                ...state.configs[apiName]?.headers,
                ...config.headers,
              },
            },
          },
        }));
      },

      getConfig: (apiName: string) => {
        return get().configs[apiName];
      },

      resetConfig: (apiName: string) => {
        set((state) => {
          const { [apiName]: _, ...rest } = state.configs;
          return { configs: rest };
        });
      },
    }),
    {
      name: 'api-config-storage',
    }
  )
);

```

## frontend/stores/uiStore.ts
```
import { create } from 'zustand';
import { devtools } from 'zustand/middleware';

type UIState = {
  isSidebarOpen: boolean;
  activeModal: string | null;
  filters: {
    searchTerm: string;
    dietaryRestrictions: string[];
  };
  // Actions
  toggleSidebar: () => void;
  setActiveModal: (modal: string | null) => void;
  updateFilters: (filters: Partial<UIState['filters']>) => void;
};

export const useUIStore = create<UIState>()(
  devtools(
    (set) => ({
      // Initial state
      isSidebarOpen: true,
      activeModal: null,
      filters: {
        searchTerm: '',
        dietaryRestrictions: [],
      },

      // Actions
      toggleSidebar: () => set((state) => ({ isSidebarOpen: !state.isSidebarOpen })),

      setActiveModal: (modal) => set({ activeModal: modal }),

      updateFilters: (newFilters) =>
        set((state) => ({
          filters: { ...state.filters, ...newFilters },
        })),
    }),
    { name: 'UI Store' }
  )
);

```

## frontend/stores/mealPlanStore.ts
```
import { create } from 'zustand';
import type { MealPlan, MealPlanItem } from '../types/recipe';

interface MealPlanStore {
  // State
  currentPlan: MealPlan | null;
  loading: boolean;
  error: string | null;

  // Actions
  createPlan: (startDate: string, endDate: string) => Promise<void>;
  addMeal: (meal: Omit<MealPlanItem, 'id'>) => Promise<void>;
  removeMeal: (mealId: string) => Promise<void>;
  updateMeal: (mealId: string, updates: Partial<MealPlanItem>) => Promise<void>;
  loadPlan: (planId: string) => Promise<void>;
  clearError: () => void;
}

export const useMealPlanStore = create<MealPlanStore>((set, get) => ({
  // Initial state
  currentPlan: null,
  loading: false,
  error: null,

  // Actions
  createPlan: async (startDate: string, endDate: string) => {
    try {
      set({ loading: true, error: null });

      // In development, use mock data
      if (process.env.NODE_ENV === 'development') {
        const plan: MealPlan = {
          id: Date.now().toString(),
          startDate,
          endDate,
          meals: [],
        };
        set({ currentPlan: plan, loading: false });
        return;
      }

      // TODO: Add API call for production
      throw new Error('Not implemented');
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to create meal plan',
        loading: false,
      });
    }
  },

  addMeal: async (meal: Omit<MealPlanItem, 'id'>) => {
    try {
      set({ loading: true, error: null });
      const { currentPlan } = get();

      if (!currentPlan) {
        throw new Error('No active meal plan');
      }

      const newMeal: MealPlanItem = {
        ...meal,
        id: Date.now().toString(),
      };

      // In development, update local state
      if (process.env.NODE_ENV === 'development') {
        set({
          currentPlan: {
            ...currentPlan,
            meals: [...currentPlan.meals, newMeal],
          },
          loading: false,
        });
        return;
      }

      // TODO: Add API call for production
      throw new Error('Not implemented');
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to add meal',
        loading: false,
      });
    }
  },

  removeMeal: async (mealId: string) => {
    try {
      set({ loading: true, error: null });
      const { currentPlan } = get();

      if (!currentPlan) {
        throw new Error('No active meal plan');
      }

      // In development, update local state
      if (process.env.NODE_ENV === 'development') {
        set({
          currentPlan: {
            ...currentPlan,
            meals: currentPlan.meals.filter((meal) => meal.id !== mealId),
          },
          loading: false,
        });
        return;
      }

      // TODO: Add API call for production
      throw new Error('Not implemented');
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to remove meal',
        loading: false,
      });
    }
  },

  updateMeal: async (mealId: string, updates: Partial<MealPlanItem>) => {
    try {
      set({ loading: true, error: null });
      const { currentPlan } = get();

      if (!currentPlan) {
        throw new Error('No active meal plan');
      }

      // In development, update local state
      if (process.env.NODE_ENV === 'development') {
        set({
          currentPlan: {
            ...currentPlan,
            meals: currentPlan.meals.map((meal) =>
              meal.id === mealId ? { ...meal, ...updates } : meal
            ),
          },
          loading: false,
        });
        return;
      }

      // TODO: Add API call for production
      throw new Error('Not implemented');
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to update meal',
        loading: false,
      });
    }
  },

  loadPlan: async (planId: string) => {
    try {
      set({ loading: true, error: null });

      // In development, create mock plan
      if (process.env.NODE_ENV === 'development') {
        const plan: MealPlan = {
          id: planId,
          startDate: new Date().toISOString(),
          endDate: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(),
          meals: [],
        };
        set({ currentPlan: plan, loading: false });
        return;
      }

      // TODO: Add API call for production
      throw new Error('Not implemented');
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to load meal plan',
        loading: false,
      });
    }
  },

  clearError: () => {
    set({ error: null });
  },
}));

```

## frontend/stores/familyProfileStore.ts
```
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export interface FamilyMember {
  id: string;
  name: string;
  allergies: string[];
  fpiesTriggers: string[];
  safeSubstitutes: Record<string, string[]>;
  reactionHistory: Array<{
    date: string;
    food: string;
    symptoms: string[];
    notes: string;
  }>;
}

interface FamilyProfileState {
  members: FamilyMember[];
  activeProfile: string | null;
  // Actions
  addMember: (member: Omit<FamilyMember, 'id' | 'reactionHistory'>) => void;
  updateMember: (id: string, updates: Partial<FamilyMember>) => void;
  setActiveProfile: (id: string | null) => void;
  addReaction: (
    memberId: string,
    reaction: Omit<FamilyMember['reactionHistory'][0], 'date'>
  ) => void;
  addSafeSubstitute: (memberId: string, ingredient: string, substitute: string) => void;
}

export const useFamilyProfileStore = create<FamilyProfileState>()(
  persist(
    (set, _get) => ({
      members: [],
      activeProfile: null,

      addMember: (member) =>
        set((state) => ({
          members: [
            ...state.members,
            {
              ...member,
              id: crypto.randomUUID(),
              reactionHistory: [],
            },
          ],
        })),

      updateMember: (id, updates) =>
        set((state) => ({
          members: state.members.map((member) =>
            member.id === id ? { ...member, ...updates } : member
          ),
        })),

      setActiveProfile: (id) => set({ activeProfile: id }),

      addReaction: (memberId, reaction) =>
        set((state) => ({
          members: state.members.map((member) =>
            member.id === memberId
              ? {
                  ...member,
                  reactionHistory: [
                    {
                      ...reaction,
                      date: new Date().toISOString(),
                    },
                    ...member.reactionHistory,
                  ],
                }
              : member
          ),
        })),

      addSafeSubstitute: (memberId, ingredient, substitute) =>
        set((state) => ({
          members: state.members.map((member) =>
            member.id === memberId
              ? {
                  ...member,
                  safeSubstitutes: {
                    ...member.safeSubstitutes,
                    [ingredient]: [...(member.safeSubstitutes[ingredient] || []), substitute],
                  },
                }
              : member
          ),
        })),
    }),
    {
      name: 'family-profiles',
    }
  )
);

```

## frontend/mocks/index.ts
```
async function initMocks() {
  if (typeof window === 'undefined') {
    const { server } = await import('./server');
    server.listen();
  } else {
    const { worker } = await import('./browser');
    await worker.start({
      onUnhandledRequest: 'bypass',
    });
  }
}

export { initMocks };

```

## frontend/mocks/handlers.ts
```
import type { Recipe } from '@/types/recipe';
import { http, HttpResponse } from 'msw';

const mockRecipes: Recipe[] = [
  {
    id: 1,
    title: 'Spaghetti Carbonara',
    description: 'Classic Italian pasta dish',
    ingredients: ['pasta', 'eggs', 'pecorino cheese', 'guanciale', 'black pepper'],
    instructions: ['Cook pasta', 'Mix eggs and cheese', 'Combine with hot pasta'],
    cookingTime: 30,
    servings: 4,
  },
  // Add more mock recipes as needed
];

export const handlers = [
  // List recipes
  http.get('*/api/recipes', () => {
    return HttpResponse.json({ data: mockRecipes });
  }),

  // Get single recipe
  http.get('*/api/recipes/:id', ({ params }) => {
    const { id } = params;
    const recipe = mockRecipes.find((r) => r.id === Number(id));

    if (!recipe) {
      return new HttpResponse(null, { status: 404 });
    }

    return HttpResponse.json({ data: recipe });
  }),

  // Create recipe
  http.post('*/api/recipes', async ({ request }) => {
    const newRecipe = await request.json();
    return HttpResponse.json({
      data: { ...newRecipe, id: (Math.random() * 1000) | 0 },
    });
  }),

  // Update recipe
  http.put('*/api/recipes/:id', async ({ params, request }) => {
    const { id } = params;
    const updates = await request.json();
    const recipe = mockRecipes.find((r) => r.id === Number(id));

    if (!recipe) {
      return new HttpResponse(null, { status: 404 });
    }

    return HttpResponse.json({
      data: { ...recipe, ...updates },
    });
  }),

  // Delete recipe
  http.delete('*/api/recipes/:id', ({ params }) => {
    const { id } = params;
    const recipe = mockRecipes.find((r) => r.id === Number(id));

    if (!recipe) {
      return new HttpResponse(null, { status: 404 });
    }

    return new HttpResponse(null, { status: 204 });
  }),
];

```

## frontend/mocks/browser.ts
```
import { setupWorker } from 'msw/browser';
import { recipeHandlers } from './handlers/recipes';

export const worker = setupWorker(...recipeHandlers);

// Expose worker globally
declare global {
  interface Window {
    msw: {
      worker: typeof worker;
    };
  }
}

window.msw = { worker };

```

## frontend/mocks/recipeData.ts
```
import type { Recipe, RecipeFilters } from '../types';

export const mockRecipes: Recipe[] = [
  {
    id: 1,
    title: 'Dairy-Free Mac and "Cheese"',
    description: 'A creamy, dairy-free version of mac and cheese',
    meal_type: 'dinner',
    is_collection: false,
    ingredients: [
      '1 package gluten-free macaroni',
      '1 cup cashews, soaked',
      '1/4 cup nutritional yeast',
      '2 cloves garlic',
      '1 cup plant-based milk',
      'Salt and pepper to taste',
    ],
    instructions: [
      'Cook macaroni according to package instructions',
      'Blend cashews, nutritional yeast, garlic, and milk until smooth',
      'Mix sauce with cooked pasta',
      'Season to taste',
    ],
    image_url: 'https://example.com/mac.jpg',
    is_dairy_free: true,
    is_egg_free: true,
    is_soy_free: true,
    is_gluten_free: true,
    is_nut_free: false,
    is_fpies_friendly: true,
    protein_type: 'vegetarian',
    cook_time: 25,
    servings: 4,
    date_added: new Date().toISOString(),
    fpies_triggers: [],
    fpies_safe_substitutes: {},
    allergens: ['nuts'],
    times_made: 0,
  },
  {
    id: 2,
    title: 'Allergen-Free Chicken Stir Fry',
    description: 'A simple and delicious allergen-free stir fry',
    meal_type: 'dinner',
    is_collection: false,
    ingredients: [
      '2 chicken breasts, diced',
      '2 cups mixed vegetables',
      '1 cup coconut aminos',
      '2 tbsp olive oil',
      'Ginger and garlic to taste',
    ],
    instructions: [
      'Cook chicken in olive oil until golden',
      'Add vegetables and stir-fry',
      'Season with coconut aminos, ginger, and garlic',
      'Serve hot',
    ],
    image_url: 'https://example.com/stirfry.jpg',
    is_dairy_free: true,
    is_egg_free: true,
    is_soy_free: true,
    is_gluten_free: true,
    is_nut_free: true,
    is_fpies_friendly: true,
    protein_type: 'chicken',
    cook_time: 30,
    servings: 4,
    date_added: new Date().toISOString(),
    fpies_triggers: [],
    fpies_safe_substitutes: {},
    allergens: [],
    times_made: 0,
  },
];

// Simulate API delay
const delay = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

// Mock API functions
export const mockApi = {
  recipes: mockRecipes,

  async searchRecipes(query: string, filters: RecipeFilters): Promise<Recipe[]> {
    await delay(500); // Simulate network delay

    return mockRecipes.filter((recipe) => {
      const matchesQuery = recipe.title.toLowerCase().includes(query.toLowerCase());
      const matchesFilters =
        (!filters.is_dairy_free || recipe.is_dairy_free) &&
        (!filters.is_egg_free || recipe.is_egg_free) &&
        (!filters.is_soy_free || recipe.is_soy_free) &&
        (!filters.protein_type || recipe.protein_type === filters.protein_type) &&
        (!filters.meal_type || recipe.meal_type === filters.meal_type) &&
        (!filters.cooking_method || recipe.cooking_method === filters.cooking_method) &&
        (!filters.is_fpies_friendly || recipe.is_fpies_friendly);
      return matchesQuery && matchesFilters;
    });
  },

  async getRecipe(id: string): Promise<Recipe> {
    await delay(300);
    const recipe = mockRecipes.find((r) => r.id === parseInt(id, 10));
    if (!recipe) {
      throw new Error('Recipe not found');
    }
    return recipe;
  },

  async favorite(id: number): Promise<Recipe> {
    await delay(300);
    const recipe = mockRecipes.find((r) => r.id === id);
    if (!recipe) {
      throw new Error('Recipe not found');
    }
    return recipe;
  },

  async share(id: number): Promise<{ url: string }> {
    await delay(300);
    return { url: `https://example.com/recipes/${id}` };
  },
};

```

## frontend/mocks/handlers/recipes.ts
```
import { http, HttpResponse } from 'msw';
import { mockRecipes } from '../data/recipes';

export const recipeHandlers = [
  // Search recipes
  http.get('/api/recipe-search', ({ request }) => {
    const url = new URL(request.url);
    const query = url.searchParams.get('query')?.toLowerCase() || '';
    const cuisine = url.searchParams.get('cuisine_type')?.toLowerCase();
    const diet = url.searchParams.get('diet')?.toLowerCase();
    const maxTime = url.searchParams.get('max_cooking_time');

    let filteredRecipes = mockRecipes;

    // Apply filters
    if (query) {
      filteredRecipes = filteredRecipes.filter(
        (recipe) =>
          recipe.title.toLowerCase().includes(query) ||
          recipe.description?.toLowerCase().includes(query)
      );
    }

    if (cuisine) {
      filteredRecipes = filteredRecipes.filter(
        (recipe) => recipe.cuisine?.toLowerCase() === cuisine
      );
    }

    if (diet) {
      filteredRecipes = filteredRecipes.filter((recipe) =>
        recipe.diet?.includes(diet)
      );
    }

    if (maxTime) {
      const maxMinutes = parseInt(maxTime);
      filteredRecipes = filteredRecipes.filter(
        (recipe) => recipe.total_time && recipe.total_time <= maxMinutes
      );
    }

    return HttpResponse.json({
      total: filteredRecipes.length,
      results: filteredRecipes,
      source: 'mock',
    });
  }),

  // Get recipe by ID
  http.get('/api/recipes/:id', ({ params }) => {
    const recipe = mockRecipes.find((r) => r.id === params.id);

    if (!recipe) {
      return new HttpResponse(null, { status: 404 });
    }

    return HttpResponse.json(recipe);
  }),
];

```

## frontend/mocks/data/recipes.ts
```
import type { RecipeList, RecipeSearchResult } from '@/types/api';

export const mockRecipes: RecipeSearchResult[] = [
  {
    id: '1',
    title: 'Classic Spaghetti Carbonara',
    description:
      'Traditional Italian pasta dish with eggs, cheese, pancetta, and black pepper',
    image_url: 'https://images.unsplash.com/photo-1612874742237-6526221588e3',
    source_url: 'https://example.com/recipes/carbonara',
    prep_time: 15,
    cook_time: 20,
    total_time: 35,
    servings: 4,
    cuisine: 'Italian',
    diet: ['dairy-free'],
    ingredients: [
      'spaghetti',
      'eggs',
      'pecorino romano',
      'pancetta',
      'black pepper',
      'salt',
    ],
    instructions: [
      'Bring a large pot of salted water to boil',
      'Cook spaghetti according to package instructions',
      'Meanwhile, cook pancetta until crispy',
      'Mix eggs, cheese, and pepper in a bowl',
      'Combine pasta with egg mixture and pancetta',
    ],
    source: 'internal',
  },
  {
    id: '2',
    title: 'Vegan Buddha Bowl',
    description:
      'Nutritious bowl filled with quinoa, roasted vegetables, and tahini dressing',
    image_url: 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd',
    source_url: 'https://example.com/recipes/buddha-bowl',
    prep_time: 20,
    cook_time: 30,
    total_time: 50,
    servings: 2,
    cuisine: 'Mediterranean',
    diet: ['vegan', 'gluten-free'],
    ingredients: [
      'quinoa',
      'sweet potato',
      'chickpeas',
      'kale',
      'avocado',
      'tahini',
    ],
    instructions: [
      'Cook quinoa according to package instructions',
      'Roast sweet potato and chickpeas',
      'Massage kale with olive oil',
      'Make tahini dressing',
      'Assemble bowls with all ingredients',
    ],
    source: 'internal',
  },
  {
    id: '3',
    title: 'Thai Green Curry',
    description: 'Aromatic coconut curry with vegetables and tofu',
    image_url: 'https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd',
    source_url: 'https://example.com/recipes/thai-curry',
    prep_time: 25,
    cook_time: 35,
    total_time: 60,
    servings: 6,
    cuisine: 'Thai',
    diet: ['dairy-free', 'gluten-free'],
    ingredients: [
      'coconut milk',
      'green curry paste',
      'tofu',
      'bamboo shoots',
      'bell peppers',
      'thai basil',
    ],
    instructions: [
      'Press and cube tofu',
      'Sauté curry paste in oil',
      'Add coconut milk and simmer',
      'Add vegetables and tofu',
      'Garnish with thai basil',
    ],
    source: 'internal',
  },
];

export const mockRecipeList: RecipeList = {
  total: mockRecipes.length,
  results: mockRecipes,
  source: 'internal',
};

```
