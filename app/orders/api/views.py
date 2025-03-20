import uuid
from typing import Any

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body
from fastapi.params import Depends

from app.containers import Container
from app.orders.api.schemas import OrderGET, OrderPOST
from app.orders.services import OrderService

router = APIRouter(prefix="orders")


@router.post("/", response_model=OrderGET)
@inject
def orders_create_one(
    request_body: OrderPOST = Body(),
    order_service: OrderService = Depends(Provide[Container.order_service]),
) -> Any:
    return order_service.orders_place_one(**request_body.model_dump())


@router.get("/{pk}", response_model=OrderGET)
def orders_get_one(
    pk: uuid.UUID,
    order_service: OrderService = Depends(Provide[Container.order_service]),
) -> Any:
    return order_service.orders_get_one(pk)
