from fastapi.params import Depends

from app.users.repositories import UserRepository
from app.users.services import UserService

def get_user_repository() -> UserRepository:
    return UserRepository()

def get_user_service(user_repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(user_repository=user_repository)