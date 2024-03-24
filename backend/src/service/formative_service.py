from domain.exceptions.incorrect_password_exception import IncorrectPasswordException
from domain.exceptions.role_not_found_exception import RoleNotFoundException
from domain.exceptions.user_not_found_exception import UserNotFoundException
from domain.group import Group
from domain.role import Role
from domain.user import User
from infrastructure.models.group_model import GroupModel
from infrastructure.models.user_model import UserModel
from service.group_repository import GroupRepository
from service.user_repository import UserRepository


class FormativeService:

    def __init__(self, user_repository: UserRepository, group_repository: GroupRepository):
        self.user_repository = user_repository
        self.group_repository = group_repository

    async def create_user(self, username: str, first_name: str, last_name: str, email: str, role: Role,
                          password: str) -> None:
        user = User(username=username, first_name=first_name, last_name=last_name, email=email, role=role,
                    password=password)
        await self.user_repository.create(user)

    async def get_all_users(self, page: int = None, page_size: int = None) -> list[User]:
        user_models: list[UserModel] = await self.user_repository.get_all(offset=page, limit=page_size)
        return [User.model_validate(user_model.model_dump()) for user_model in user_models]

    async def get_user_by_username(self, username: str) -> User:
        if user_model := await self.user_repository.get_by_username(username):
            return User.model_validate(user_model.model_dump())
        raise UserNotFoundException(username)

    async def change_user_password(self, username: str, old_password: str, new_password: str) -> None:
        if not await self.user_repository.validate_password(username, old_password):
            raise IncorrectPasswordException(username)
        await self.user_repository.change_password(username, new_password)

    async def delete_user(self, username: str) -> None:
        await self.user_repository.delete_by_username(username)

    async def create_group(self, name: str) -> None:
        role = Group(name=name)
        await self.group_repository.create(role)

    async def get_all_groups(self, page: int = None, page_size: int = None) -> list[Group]:
        role_models: list[GroupModel] = await self.group_repository.get_all(offset=page, limit=page_size)
        return [Group.model_validate(role_model.model_dump()) for role_model in role_models]

    async def get_group_by_name(self, name: str) -> Group:
        if role_model := await self.group_repository.get_by_name(name):
            return Group.model_validate(role_model.model_dump())
        raise RoleNotFoundException(name)

    async def delete_group_by_name(self, name: str) -> None:
        await self.group_repository.delete_by_name(name)
