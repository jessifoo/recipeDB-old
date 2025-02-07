from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix="/recipes", tags=["recipes"], responses={404: {"description": "Recipe not found"}})


@router.get("/")
async def get_recipes() -> dict[str, str]:
    """Get a list of recipes."""
    return {"message": "List of recipes will be here."}
