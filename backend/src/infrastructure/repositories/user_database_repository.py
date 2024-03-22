from sqlalchemy.ext.asyncio import AsyncSession

from domain.role import Role
from domain.user import User
from infrastructure.models.role_model import RoleModel
from infrastructure.models.user_model import UserModel
from infrastructure.repositories.database_repository import DatabaseRepository
from service.user_repository import UserRepository


class UserDatabaseRepository(UserRepository, DatabaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, user: User):
        user_model = UserModel(**user.model_dump())
        await self.add_model(user_model)

    async def get_all(self, offset: int = None, limit: int = None) -> list[UserModel]:
        return await self.get_all_models(UserModel, offset=offset, limit=limit)

    async def get_by_username(self, username: str) -> UserModel:
        return await self.get_model(UserModel, username=username)

    async def change_password(self, username: str, new_password: str) -> None:
        return await self.update_model(UserModel, "username", username, password=new_password)

    async def validate_password(self, username: str, password: str) -> bool:
        user: UserModel = await self.get_by_username(username)
        return user.password == password

    async def delete_by_username(self, username: str) -> None:
        await self.delete_model(UserModel, username=username)
