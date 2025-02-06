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
