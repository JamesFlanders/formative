from sqlalchemy.ext.asyncio import AsyncSession

from domain.role import Role
from infrastructure.models.role_model import RoleModel
from infrastructure.repositories.database_repository import DatabaseRepository
from service.role_repository import RoleRepository


class RoleDatabaseRepository(RoleRepository, DatabaseRepository):

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, role: Role) -> None:
        role_model = RoleModel(**role.model_dump())
        await self.add_model(role_model)

    async def get_all(self, offset: int = None, limit: int = None) -> list[RoleModel]:
        return await self.get_all_models(RoleModel, offset=offset, limit=limit)

    async def get_by_name(self, name: str) -> RoleModel:
        return await self.get_model(RoleModel, name=name)

    async def delete_by_name(self, name: str) -> None:
        await self.delete_model(RoleModel, name=name)
