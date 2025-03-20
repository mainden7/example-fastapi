import uuid
from typing import Any

from sqlalchemy import Table, Connection

from app.core.database.repositories import SQLAlchemyCoreRepository
from app.orders.models import Order, OrderLine
from app.orders.tables import orders_table, order_lines_table


class OrderRepository(SQLAlchemyCoreRepository[Order]):
    @property
    def table(self) -> Table:
        return orders_table

    def _make_row(self, raw_data):
        pass


class OrderLineRepository(SQLAlchemyCoreRepository[OrderLine]):
    @property
    def table(self) -> Table:
        return order_lines_table

    def _make_row(self, raw_data):
        pass

    def add_bulk(self, data: list[dict], /, *, conn: Connection, order_id: uuid.UUID, **kwargs: Any) -> list[OrderLine]: ...
    

