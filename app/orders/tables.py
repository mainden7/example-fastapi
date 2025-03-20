from app.core.database.common import (
    some_common_columns_factory,
    metadata,
)
from sqlalchemy import Table, Column, ForeignKey

orders_table = Table(
    "orders",
    metadata,
    *some_common_columns_factory(),
    # ... other columns go here
)

order_lines_table = Table(
    "order_lines",
    metadata,
    *some_common_columns_factory(),
    Column("order_id", ForeignKey("orders.id"), nullable=False, index=True),
    # ... other columns go here
)

