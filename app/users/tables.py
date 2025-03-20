from app.core.database.common import some_common_columns_factory, metadata
from sqlalchemy import Table, Column

from app.core.database.field_types import LowercaseText

users_table = Table(
    "users",
    metadata,
    *some_common_columns_factory(),
    Column("email", LowercaseText, nullable=False, unique=True, index=True),
    # ... other columns go here
)
