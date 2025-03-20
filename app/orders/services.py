import uuid

from sqlalchemy import Connection

from app.orders.models import Order
from app.orders.repositories import OrderRepository, OrderLineRepository

"""
Business logic goes here
"""

class OrderService:
    def __init__(self, order_repository: OrderRepository, order_line_repository: OrderLineRepository) -> None:
        self._order_repository = order_repository
        self.__order_lines_repository = order_line_repository

    def orders_place_one(self, conn: Connection, order_lines_data: list[dict]) -> Order:
        """Logic to add order"""
        with conn.begin():
            # happens in one transaction
            order = self._order_repository.add_one(conn=conn)
            order_lines = self.__order_lines_repository.add_bulk(conn=conn, order_id=order.id, data=order_lines_data)

        # post create hooks
        self._process_post_create_hooks(order)

        return order

    def orders_get_one(self, pk: uuid.UUID, /, *, conn: Connection) -> Order:
        # order goes with all order lines: order.order_lines
        return self._order_repository.get_one(pk, conn=conn)

    @staticmethod
    def _process_post_create_hooks(order: Order) -> None:
        # some background tasks to do with just created order
        some_sync_actor.send(str(order.id))
        some_sync_actor2.send(str(order.id))
