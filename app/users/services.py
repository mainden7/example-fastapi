import uuid
from typing import Any

from sqlalchemy import Connection

from app.users.models import User
from app.users.repositories import UserRepository

"""
Business logic goes here
"""

class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def users_register_one(self, conn: Connection, **kwargs: Any) -> User:
        """Logic to add user"""
        user = self._user_repository.add_one(conn=conn, **kwargs)

        # post create hooks
        self._process_post_create_hooks(user)

        return user

    def users_get_one(self, pk: uuid.UUID, /, *, conn: Connection) -> User:
        return self._user_repository.get_one(pk, conn=conn)

    def _process_post_create_hooks(self, user: User) -> None:
        # some background tasks to do with just created user
        some_sync_actor.send(str(user.id))
        some_sync_actor2.send(str(user.id))
