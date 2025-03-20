from pydantic.v1 import BaseSettings
from pydantic_core.core_schema import computed_field


class PostgresSettings(BaseSettings):
    @computed_field
    @property
    def dsn(self) -> str:
        return ""


class APISettings(BaseSettings):
    postgres: PostgresSettings

    @computed_field
    @property
    def database_engine_settings(self) -> dict:
        return {}

    @computed_field
    @property
    def session_settings(self) -> dict:
        return {}
