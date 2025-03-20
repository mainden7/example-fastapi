from typing import Any

from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    # include routes
    ...

    # add middlewares
    ...

    return app


def create_cli_app() -> Any:
    """Create CLI app if needed."""
