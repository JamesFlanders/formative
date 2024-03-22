import pytest
from sqlmodel import select

from domain.user import User
from infrastructure.models.user_model import UserModel
from infrastructure.repositories.user_database_repository import UserDatabaseRepository


@pytest.fixture
def user_database_repository(session):
    return UserDatabaseRepository(session)


async def test_create(user_database_repository):
    user = User(username="dwights", email="dwights@dundermifflin.com", first_name="Dwight", last_name="Schrute",
                password="test")
    await user_database_repository.create(user)
    await user_database_repository.session.commit()

    query = select(UserModel).where(UserModel.username == "dwights")
    result = await user_database_repository.session.execute(query)
    expected_user: UserModel = result.scalar()

    assert expected_user.username == user.username


async def test_get_all_without_pagination(user_database_repository):
    users: list[UserModel] = list(await user_database_repository.get_all())
    assert len(users) == 2


@pytest.mark.parametrize("expected, offset, limit", [
    (1, 1, 1), (2, 1, 2), (0, 2, 2)
])
async def test_get_all_with_pagination(user_database_repository, expected, offset, limit):
    users: list[UserModel] = list(await user_database_repository.get_all(offset, limit))
    assert len(users) == expected


@pytest.mark.parametrize("username", ["michaels", "jimh"])
async def test_get_by_username(user_database_repository, username):
    user: UserModel = await user_database_repository.get_by_username(username)
    assert user.username == username


async def test_change_password(user_database_repository):
    new_password = "il0v3j4n!"
    await user_database_repository.change_password("michaels", new_password)
    await user_database_repository.session.commit()

    query = select(UserModel).where(UserModel.username == "michaels")
    result = await user_database_repository.session.execute(query)
    expected_user: UserModel = result.scalar()

    assert expected_user.password == new_password


@pytest.mark.parametrize("expected, username, password", [
    (False, "michaels", "il0v3j4n!"), (True, "jimh", "il0v3p4m!")
])
async def test_validate_password(user_database_repository, expected, username, password):
    is_password_valid = await user_database_repository.validate_password(username, password)
    assert expected == is_password_valid


async def test_delete_by_username(user_database_repository):
    await user_database_repository.delete_by_username("jimh")
    await user_database_repository.session.commit()

    query = select(UserModel).where(UserModel.username == "jimh")
    result = await user_database_repository.session.execute(query)
    expected_user: UserModel = result.scalar()

    assert not expected_user
