from app.core.database.common import mapper_registry, some_common_columns_factory, metadata
from sqlalchemy import Table, Column

from app.core.database.field_types import LowercaseText
from app.users.models import User

users_table = Table(
    "users",
    metadata,
    *some_common_columns_factory(),
    Column("email", LowercaseText, nullable=False, unique=True, index=True),
    # ... other columns go here
)


def map_table_with_model() -> None:
    mapper_registry.map_imperatively(User, users_table)
