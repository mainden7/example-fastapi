from typing import AsyncIterator

from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.orders.repositories import OrderRepository
from app.orders.services import OrderService
from app.settings import APISettings
from app.users.repositories import UserRepository
from app.users.services import UserService


class Container(containers.DeclarativeContainer):
    """All dependencies are defined here."""

    wiring_config = containers.WiringConfiguration(
        modules=["app.users.api.views", "app.orders.api.vires"]
    )

    # core deps
    config: APISettings = providers.Configuration(pydantic_settings=[APISettings()])

    # database
    engine = providers.Singleton(create_engine, **config.database_engine_settings)
    # i don't remember how to properly instantiate sync session here, so it is shared across threads
    #  without interfering each another, maybe the implementation is a little bit different
    session_factory = providers.Singleton(sessionmaker, **config.session_settings)

    # repositories
    user_repository = providers.Factory(UserRepository, session_factory=session_factory)
    order_repository = providers.Factory(
        OrderRepository, session_factory=session_factory
    )

    # services
    user_service = providers.Factory(UserService, user_repository=user_repository)
    order_service = providers.Factory(OrderService, order_repository=order_repository)
