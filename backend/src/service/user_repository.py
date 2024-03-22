from abc import abstractmethod, ABC

from domain.role import Role
from domain.user import User
from infrastructure.models.user_model import UserModel


class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, offset: int = None, limit: int = None) -> list[UserModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_username(self, username: str) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    async def change_password(self, username: str, new_password: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def validate_password(self, username: str, password: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_username(self, username: str) -> None:
        raise NotImplementedError
