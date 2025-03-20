from collections.abc import Iterator
from functools import lru_cache

from fastapi import Depends
from sqlalchemy import Connection, create_engine, Engine

from app.settings import APISettings


@lru_cache(maxsize=1)
def get_settings() -> APISettings:
    return APISettings()


def get_engine(settings: APISettings = Depends(get_settings)) -> Engine:
    return create_engine(settings.postgres.dsn)


def get_connection(engine: Engine = Depends(get_engine)) -> Iterator[Connection]:
    conn = engine.connect()
    try:
        yield conn
    finally:
        conn.close()
