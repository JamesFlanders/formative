from litestar import Controller, post, delete, get
from litestar.di import Provide
from litestar.exceptions import NotFoundException

from domain.exceptions.role_not_found_exception import RoleNotFoundException
from domain.role import Role
from infrastructure.api.schemas.create_role_schema import CreateRoleSchema
from infrastructure.api.service import provide_formative_service
from service.formative_service import FormativeService


class RoleController(Controller):
    path = "/role"

    dependencies = {
        "service": Provide(provide_formative_service)
    }

    @post(path="/")
    async def create_role(self, service: FormativeService, data: CreateRoleSchema) -> None:
        await service.create_role(name=data.name)

    @get(path="/")
    async def get_all_roles(self, service: FormativeService, page: int = None, page_size: int = 25) -> list[Role]:
        return await service.get_all_roles(page=page, page_size=page_size)

    @get(path="/{name:str}")
    async def get_role_by_name(self, service: FormativeService, name: str) -> Role:
        try:
            return await service.get_role_by_name(name=name)
        except RoleNotFoundException as exception:
            raise NotFoundException(exception.message)

    @delete(path="/{name:str}")
    async def delete_role_by_name(self, service: FormativeService, name: str) -> None:
        await service.delete_role_by_name(name=name)
