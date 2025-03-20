import uuid

from app.orders.models import Order
from app.orders.repositories import OrderRepository

"""
Business logic goes here
"""

class OrderService:
    def __init__(self, order_repository: OrderRepository) -> None:
        self._order_repository = order_repository

    def orders_place_one(self, order_lines_data: list[dict]) -> Order:
        """Logic to add order"""
        order = self._order_repository.add_one(order_lines_data)

        # post create hooks
        self._process_post_create_hooks(order)

        return order

    def orders_get_one(self, pk: uuid.UUID, /) -> Order:
        # order goes with all order lines: order.order_lines
        return self._order_repository.get_one(pk)

    @staticmethod
    def _process_post_create_hooks(order: Order) -> None:
        # some background tasks to do with just created order
        some_sync_actor.send(str(order.id))
        some_sync_actor2.send(str(order.id))
