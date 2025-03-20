from contextlib import contextmanager
from typing import AsyncIterator, Any

from fastapi import FastAPI

from app.containers import Container
from app.orders.tables import map_table_with_model as order_mapper
from app.users.tables import map_table_with_model as user_mapper


class MYAPI(FastAPI):
    def __init__(self, container: Container, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.container = container


@contextmanager
def lifespan(app: MYAPI) -> AsyncIterator[None]:
    # here are going all domain model <-> core tables mappings
    app.container.init_resources()
    _map_tables_with_models()
    yield
    app.container.shutdown_resources()


def create_app(container: Container) -> MYAPI:
    app = MYAPI(container=container, lifespan=lifespan)

    # include routes
    ...

    # add middlewares
    ...

    return app


def create_cli_app() -> Any:
    """Create CLI app if needed."""


def _map_tables_with_models():
    order_mapper()
    user_mapper()