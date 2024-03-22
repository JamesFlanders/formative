from abc import abstractmethod, ABC

from domain.role import Role
from infrastructure.models.role_model import RoleModel


class RoleRepository(ABC):

    @abstractmethod
    async def create(self, role: Role) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, offset: int = None, limit: int = None) -> list[RoleModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_name(self, name: str) -> RoleModel:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_name(self, name: str) -> None:
        raise NotImplementedError
