import pytest
from sqlmodel import select

from domain.role import Role
from infrastructure.models.role_model import RoleModel
from infrastructure.repositories.role_database_repository import RoleDatabaseRepository


@pytest.fixture
def role_database_repository(session):
    return RoleDatabaseRepository(session)


async def test_create(role_database_repository):
    role = Role(name="moderator")
    await role_database_repository.create(role)
    await role_database_repository.session.commit()

    query = select(RoleModel).where(RoleModel.name == "moderator")
    result = await role_database_repository.session.execute(query)
    expected_role: RoleModel = result.scalar()

    assert expected_role


async def test_get_all_without_pagination(role_database_repository):
    role_models: list[RoleModel] = list(await role_database_repository.get_all())
    assert len(role_models) == 3


@pytest.mark.parametrize("expected, offset, limit", [
    (1, 1, 1), (2, 1, 2), (1, 2, 2), (3, 1, 3)
])
async def test_get_all_with_pagination(role_database_repository, expected, offset, limit):
    role_models: list[RoleModel] = list(await role_database_repository.get_all(offset, limit))
    assert len(role_models) == expected


@pytest.mark.parametrize("name", ["admin", "user", "guest"])
async def test_get_by_name(role_database_repository, name):
    role_model: RoleModel = await role_database_repository.get_by_name(name)
    assert role_model.name == name


async def test_delete_by_name(role_database_repository):
    await role_database_repository.delete_by_name("admin")
    await role_database_repository.session.commit()

    query = select(RoleModel).where(RoleModel.name == "admin")
    result = await role_database_repository.session.execute(query)
    expected_role: RoleModel = result.scalar()

    assert not expected_role
