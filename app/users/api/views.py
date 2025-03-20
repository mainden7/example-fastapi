import uuid
from typing import Any

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body
from fastapi.params import Depends

from app.containers import Container
from app.users.api.schemas import UserPOST, UserGET
from app.users.services import UserService

router = APIRouter(prefix="users")


@router.post("/", response_model=UserGET)
@inject
def users_create_one(
    request_body: UserPOST = Body(),
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> Any:
    # API contract is really hard to update/manage if it was already consumed by API clients. So decoupling it from
    #  all the rest app logic makes us more flexible in manipulating objects further
    return user_service.users_register_one(**request_body.model_dump())


@router.get("/{pk}", response_model=UserGET)
def users_get_one(
    pk: uuid.UUID,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> Any:
    return user_service.users_get_one(pk)
