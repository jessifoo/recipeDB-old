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
