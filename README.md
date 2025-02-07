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
