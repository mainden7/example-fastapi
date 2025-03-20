from sqlalchemy import Table

from app.core.database.repositories import SQLAlchemyCoreRepository
from app.users.models import User
from app.users.tables import users_table


class UserRepository(SQLAlchemyCoreRepository[User]):
    @property
    def table(self) -> Table:
        return users_table

    def _make_row(self, raw_data):
        pass


class UserHTTPRepository: ...
