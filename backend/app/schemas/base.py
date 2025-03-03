"""Base schema classes."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """Base schema class with common configuration."""

    model_config = ConfigDict(from_attributes=True)
