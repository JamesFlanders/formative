import pytest
from sqlmodel import select

from domain.group import Group
from infrastructure.models.group_model import GroupModel
from infrastructure.repositories.role_database_repository import GroupDatabaseRepository


@pytest.fixture
def group_database_repository(session):
    return GroupDatabaseRepository(session)


async def test_create(group_database_repository):
    group = Group(name="developers")
    await group_database_repository.create(group)
    await group_database_repository.session.commit()

    query = select(GroupModel).where(GroupModel.name == "developers")
    result = await group_database_repository.session.execute(query)
    expected_group: GroupModel = result.scalar()

    assert expected_group


async def test_get_all_without_pagination(group_database_repository):
    group_models: list[GroupModel] = list(await group_database_repository.get_all())
    assert len(group_models) == 3


@pytest.mark.parametrize("expected, offset, limit", [
    (1, 1, 1), (2, 1, 2), (1, 2, 2), (3, 1, 3)
])
async def test_get_all_with_pagination(group_database_repository, expected, offset, limit):
    group_models: list[GroupModel] = list(await group_database_repository.get_all(offset, limit))
    assert len(group_models) == expected


@pytest.mark.parametrize("name", ["helpers", "moderators", "marketeers"])
async def test_get_by_name(group_database_repository, name):
    group_model: GroupModel = await group_database_repository.get_by_name(name)
    assert group_model.name == name


async def test_delete_by_name(group_database_repository):
    await group_database_repository.delete_by_name("helpers")
    await group_database_repository.session.commit()

    query = select(GroupModel).where(GroupModel.name == "helpers")
    result = await group_database_repository.session.execute(query)
    expected_group: GroupModel = result.scalar()

    assert not expected_group
