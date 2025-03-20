import uuid
from abc import ABC
from types import get_original_bases
from typing import get_args, Any

from sqlalchemy import select, Select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.sql.dml import ReturningInsert


class SQLAlchemyCoreRepository[T](ABC):  # noqa: B024
    def __init__(self, session_factory):
        self.session_factory = session_factory

    @property
    def __model(self) -> type[T]:
        """Retrieves the dataclass domain model associated with the repository."""
        return get_args(get_original_bases(self.__class__)[0])[0]

    def add_one(self, **kwargs: Any) -> T:
        stmt = insert(self.__model).values(**kwargs).returning(self.__model)
        return self._insert_scalar(stmt)

    def get_one(self, pk: uuid.UUID, /) -> T:
        # assuming all models derived from some base one, having id as uuid everywhere
        stmt = select(self.__model).where(self.__model.id == pk)
        return self._select_scalar(stmt)

    def _select_scalar(self, stmt: Select) -> T:
        with self.session_factory() as sess:
            res = sess.execute(stmt)
        try:
            return res.scalar_one()
        except NoResultFound as e:
            # swap sqla exception with app exception
            raise NotFoundError from e
        except MultipleResultsFound as e:
            # swap sqla exception with app exception
            raise MultipleResultsFoundError from e


    def _insert_scalar(self, stmt: ReturningInsert) -> T:
        with self.session_factory() as sess:
            res = sess.execute(stmt)

        return res.scalar_one()
