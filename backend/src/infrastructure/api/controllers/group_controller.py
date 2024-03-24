from litestar import Controller, post, delete, get
from litestar.exceptions import NotFoundException

from domain.exceptions.role_not_found_exception import RoleNotFoundException
from domain.group import Group
from infrastructure.api.schemas.create_group_schema import CreateGroupSchema
from service.formative_service import FormativeService


class GroupController(Controller):
    path = "/group"

    @post(path="/")
    async def create_group(self, service: FormativeService, data: CreateGroupSchema) -> None:
        await service.create_group(name=data.name)

    @get(path="/")
    async def get_all_groups(self, service: FormativeService, page: int = None, page_size: int = 25) -> list[Group]:
        return await service.get_all_groups(page=page, page_size=page_size)

    @get(path="/{name:str}")
    async def get_group_by_name(self, service: FormativeService, name: str) -> Group:
        try:
            return await service.get_group_by_name(name=name)
        except RoleNotFoundException as exception:
            raise NotFoundException(exception.message)

    @delete(path="/{name:str}")
    async def delete_group_by_name(self, service: FormativeService, name: str) -> None:
        await service.delete_group_by_name(name=name)
