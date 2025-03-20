import uuid
from abc import ABC, abstractmethod
from types import get_original_bases
from typing import get_args, Any

from sqlalchemy import Select, Connection, Table
from sqlalchemy.sql.dml import ReturningInsert


class SQLAlchemyCoreRepository[T](ABC):  # noqa: B024
    def __model(self) -> type[T]:
        """Retrieves the dataclass domain model associated with the repository."""
        return get_args(get_original_bases(self.__class__)[0])[0]

    @abstractmethod
    @property
    def table(self) -> Table: ...

    @abstractmethod
    def _make_row(self, raw_data): ...

    def add_one(self, *, conn: Connection, **kwargs: Any) -> T:
        stmt = self.table.insert().values(**kwargs).returning(self.table.c)
        return self._insert(conn, stmt)

    def add_bulk(self, data: list[dict], /, *, conn: Connection, **kwargs: Any) -> list[T]: ...

    def get_one(self, pk: uuid.UUID, /, *, conn: Connection) -> T:
        # assuming all models derived from some base one, having id as uuid everywhere
        stmt = self.table.select().where(self.table.c.id == pk)
        return self._select(conn, stmt)

    def _select(self, conn: Connection, stmt: Select) -> T:
        res = conn.execute(stmt)
        return self._make_row(res.fetchone())

    def _insert(self, conn: Connection, stmt: ReturningInsert) -> T:
        res = conn.execute(stmt)
        return self._make_row(res.fetchone())
