import uuid
from typing import Any

from app.users.models import User
from app.users.repositories import UserRepository

"""
Business logic goes here
"""

class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def users_register_one(self, **kwargs: Any) -> User:
        """Logic to add user"""
        user = self._user_repository.add_one(**kwargs)

        # post create hooks
        self._process_post_create_hooks(user)

        return user

    def users_get_one(self, pk: uuid.UUID, /) -> User:
        return self._user_repository.get_one(pk)

    def _process_post_create_hooks(self, user: User) -> None:
        # some background tasks to do with just created user
        some_sync_actor.send(str(user.id))
        some_sync_actor2.send(str(user.id))
