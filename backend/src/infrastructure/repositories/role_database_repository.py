from sqlalchemy.ext.asyncio import AsyncSession

from domain.group import Group
from infrastructure.models.group_model import GroupModel
from infrastructure.repositories.database_repository import DatabaseRepository
from service.group_repository import GroupRepository


class GroupDatabaseRepository(GroupRepository, DatabaseRepository):

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, role: Group) -> None:
        role_model = GroupModel(**role.model_dump())
        await self.add_model(role_model)

    async def get_all(self, offset: int = None, limit: int = None) -> list[GroupModel]:
        return await self.get_all_models(GroupModel, offset=offset, limit=limit)

    async def get_by_name(self, name: str) -> GroupModel:
        return await self.get_model(GroupModel, name=name)

    async def delete_by_name(self, name: str) -> None:
        await self.delete_model(GroupModel, name=name)
