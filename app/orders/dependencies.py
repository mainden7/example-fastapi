from fastapi.params import Depends

from app.orders.repositories import OrderRepository, OrderLineRepository
from app.orders.services import OrderService


def get_order_repository() -> OrderRepository:
    return OrderRepository()


def get_order_line_repository() -> OrderLineRepository:
    return OrderLineRepository()


def get_order_service(
    order_repository: OrderRepository = Depends(get_order_repository),
    order_line_repository: OrderLineRepository = Depends(get_order_line_repository),
) -> OrderService:
    return OrderService(
        order_repository=order_repository, order_line_repository=order_line_repository
    )
