from sqlalchemy.orm import relationship

from app.core.database.common import (
    mapper_registry,
    some_common_columns_factory,
    metadata,
)
from sqlalchemy import Table, Column, ForeignKey

from app.orders.models import Order, OrderLine
from app.users.models import User

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


def map_table_with_model() -> None:
    mapper_registry.map_imperatively(
        Order,
        orders_table,
        properties={
            "_creator": relationship(User, lazy="noload", uselist=False),
            "order_lines": relationship(OrderLine, uselist=True, lazy="noload"),
        },
    )
    mapper_registry.map_imperatively(OrderLine, order_lines_table)
