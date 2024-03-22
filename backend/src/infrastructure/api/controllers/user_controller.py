from litestar import Controller, post, patch, delete, get
from litestar.di import Provide
from litestar.exceptions import NotFoundException, ClientException

from domain.exceptions.incorrect_password_exception import IncorrectPasswordException
from domain.exceptions.user_not_found_exception import UserNotFoundException
from domain.user import User
from infrastructure.api.schemas.create_user_schema import CreateUserSchema
from infrastructure.api.schemas.update_user_password_schema import UpdateUserPasswordSchema
from infrastructure.api.service import provide_formative_service
from service.formative_service import FormativeService


class UserController(Controller):
    path = "/user"

    dependencies = {
        "service": Provide(provide_formative_service)
    }

    @post(path="/")
    async def create_user(self, service: FormativeService, data: CreateUserSchema) -> None:
        await service.create_user(
            username=data.username,
            password=data.password,
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email
        )

    @get(path="/")
    async def get_all_users(self, service: FormativeService, page: int = None, page_size: int = 25) -> list[User]:
        return await service.get_all_users(page=page, page_size=page_size)

    @get(path="/{username:str}")
    async def get_user_by_username(self, service: FormativeService, username: str) -> User:
        try:
            return await service.get_user_by_username(username)
        except UserNotFoundException as exception:
            raise NotFoundException(exception.message)

    @patch(path="/{username:str}/password/update")
    async def change_user_password(self, service: FormativeService, username: str,
                                   data: UpdateUserPasswordSchema) -> None:
        if not data.new_password == data.new_password_confirmation:
            raise ClientException("The new password and the confirmation of the new password do not match!")
        try:
            await service.change_user_password(username, data.old_password, data.new_password)
        except IncorrectPasswordException as exception:
            raise ClientException(exception.message)

    @delete(path="/{username:str}")
    async def delete_user(self, service: FormativeService, username: str) -> None:
        await service.delete_user(username)
