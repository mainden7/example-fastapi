from app.core.database.repositories import SQLAlchemyCoreRepository
from app.users.models import User


class UserRepository(SQLAlchemyCoreRepository[User]): ...


class UserHTTPRepository: ...