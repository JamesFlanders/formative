from abc import abstractmethod, ABC

from domain.group import Group
from infrastructure.models.group_model import GroupModel


class GroupRepository(ABC):

    @abstractmethod
    async def create(self, role: Group) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, offset: int = None, limit: int = None) -> list[GroupModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_name(self, name: str) -> GroupModel:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_name(self, name: str) -> None:
        raise NotImplementedError
